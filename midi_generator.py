import pretty_midi
import os

def get_chord_notes(chord_name):
    """Convert chord name to MIDI note numbers"""
    # Basic chord definitions
    chord_definitions = {
        "C": [60, 64, 67],      # C major
        "Cm": [60, 63, 67],     # C minor
        "C7": [60, 64, 67, 70], # C dominant 7
        "Cmaj7": [60, 64, 67, 71], # C major 7
        "Am": [57, 60, 64],     # A minor
        "A": [57, 61, 64],      # A major
        "F": [53, 57, 60],      # F major
        "G": [55, 59, 62],      # G major
        "G7": [55, 59, 62, 65], # G dominant 7
        "Dm": [50, 53, 57],     # D minor
        "Dm7": [50, 53, 57, 60], # D minor 7
        "Em": [52, 55, 59],     # E minor
        "Bm": [47, 50, 54],     # B minor
    }
    
    return chord_definitions.get(chord_name, [60, 64, 67])  # Default to C major

def note_name_to_midi(note_name):
    """Convert note name (e.g., 'C4', 'A#5') to MIDI pitch"""
    note_map = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6,
        'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
    }
    
    # Parse note name (e.g., "C4", "A#5")
    if len(note_name) >= 2:
        note = note_name[:-1]
        octave = int(note_name[-1])
        base_pitch = note_map.get(note, 0)
        return base_pitch + (octave + 1) * 12
    else:
        return 60  # Default to middle C

def make_music_midi(parsed_data, filename="midi_output/music.mid"):
    """Generate MIDI music from parsed data (drums, chords, melody)"""
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Initialize MIDI with tempo
    bpm = parsed_data.get("bpm", 90)
    midi = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    
    # Get music type
    music_type = parsed_data.get("music_type", "drums")
    
    # Create instruments
    if music_type in ["drums", "mixed"]:
        drum = pretty_midi.Instrument(program=0, is_drum=True)
        midi.instruments.append(drum)
    
    if music_type in ["chords", "melody", "mixed"]:
        piano = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano
        midi.instruments.append(piano)
    
    # Drum note mapping (General MIDI drum map)
    drum_map = {
        "kick": 36,      # Bass Drum 1
        "snare": 38,     # Acoustic Snare
        "hats": 42,      # Closed Hi-Hat
        "crash": 49,     # Crash Cymbal 1
        "tom": 45,       # Low Tom
        "clap": 39       # Hand Clap
    }
    
    # Beat position to time mapping (4-bar pattern)
    step_map = {
        "1": 0.0, "1.2": 0.25, "1.3": 0.5, "1.4": 0.75,
        "2": 1.0, "2.2": 1.25, "2.3": 1.5, "2.4": 1.75,
        "3": 2.0, "3.2": 2.25, "3.3": 2.5, "3.4": 2.75,
        "4": 3.0, "4.2": 3.25, "4.3": 3.5, "4.4": 3.75
    }
    
    # Generate drum notes if needed
    if music_type in ["drums", "mixed"] and "pattern" in parsed_data:
        pattern = parsed_data["pattern"]
        for drum_type, hits in pattern.items():
            if drum_type in drum_map:
                hit_positions = [hit.strip() for hit in hits.split(",")]
                
                for hit in hit_positions:
                    if hit in step_map:
                        time = step_map[hit]
                        velocity = 100 if drum_type == "kick" else 80
                        note = pretty_midi.Note(
                            velocity=velocity, 
                            pitch=drum_map[drum_type], 
                            start=time, 
                            end=time+0.1
                        )
                        drum.notes.append(note)
    
    # Generate chords if needed
    if music_type in ["chords", "mixed"] and "chords" in parsed_data and parsed_data["chords"]:
        chords = parsed_data["chords"]
        chord_duration = 4.0 / len(chords)  # Spread chords across 4 bars
        
        for i, chord in enumerate(chords):
            chord_notes = get_chord_notes(chord)
            start_time = i * chord_duration
            
            for note_pitch in chord_notes:
                note = pretty_midi.Note(
                    velocity=70,
                    pitch=note_pitch,
                    start=start_time,
                    end=start_time + chord_duration
                )
                piano.notes.append(note)
    
    # Generate melody if needed
    if music_type in ["melody", "mixed"] and "melody" in parsed_data and parsed_data["melody"]:
        melody = parsed_data["melody"]
        note_duration = 4.0 / len(melody)  # Spread melody across 4 bars
        
        for i, note_name in enumerate(melody):
            note_pitch = note_name_to_midi(note_name)
            start_time = i * note_duration
            
            note = pretty_midi.Note(
                velocity=80,
                pitch=note_pitch,
                start=start_time,
                end=start_time + note_duration
            )
            piano.notes.append(note)
    
    # Write MIDI file
    midi.write(filename)
    print(f"MIDI file generated: {filename}")
    return filename

def make_drum_midi(pattern, bpm=90, filename="midi_output/drums.mid"):
    """Generate MIDI drum pattern from structured instructions (legacy function)"""
    parsed_data = {
        "bpm": bpm,
        "music_type": "drums",
        "pattern": pattern
    }
    return make_music_midi(parsed_data, filename)

def create_melody_midi(notes, bpm=90, filename="midi_output/melody.mid"):
    """Generate MIDI melody from note list"""
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    midi = pretty_midi.PrettyMIDI(initial_tempo=bpm)
    piano = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano
    
    # Note name to MIDI pitch mapping
    note_map = {
        'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65, 'F#': 66,
        'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71
    }
    
    current_time = 0.0
    for note_info in notes:
        if isinstance(note_info, dict):
            note_name = note_info.get('note', 'C')
            duration = note_info.get('duration', 0.5)
            octave = note_info.get('octave', 4)
            
            # Calculate MIDI pitch
            base_note = note_name.replace('#', '')
            pitch = note_map.get(base_note, 60) + (octave - 4) * 12
            if '#' in note_name:
                pitch += 1
            
            # Create note
            note = pretty_midi.Note(
                velocity=80,
                pitch=pitch,
                start=current_time,
                end=current_time + duration
            )
            piano.notes.append(note)
            current_time += duration
    
    midi.instruments.append(piano)
    midi.write(filename)
    print(f"Melody MIDI file generated: {filename}")
    return filename 
# Spotify Playlist Generator

This Python program generates a personalized playlist based on the most streamed songs and artists on Spotify. It uses two CSV files, `songs.csv` (top 2,500 most streamed songs) and `artists.csv` (top 3,000 most streamed artists), to tailor recommendations according to user preferences.

## Features
- Generates a playlist based on user-selected favorite and least favorite artists and songs.
- Validates user inputs against the CSV datasets.
- Handles multiple input attempts for the first questions to ensure accurate matching.
- Implements a structured selection approach to create playlists.
- Identifies and informs about edge cases such as duplicate songs, missing artist songs, and special characters in names.

## How to Use
1. Ensure `myProject.py`, `songs.csv`, and `artists.csv` are in the same folder.
2. Run the program using Python:
   ```bash
   python myProject.py
## Notes on Using the Program
- Make sure artist and song names are spelled correctly and match the CSV files.
- For the last question, input as many artists as you like separated by commas to make the playlist more diverse. Leaving it empty will base the playlist only on your favorite and second favorite artists.
- The program provides multiple attempts to correct inputs for the first two questions to help ensure accuracy.

## Edge Cases
- If a popular artist is in the dataset but has no songs listed, the program may crash.
- Duplicate songs may appear in the playlist if the CSV contains multiple versions of the same song.
- Artists with accents, special characters, or commas in their names may not be recognized correctly in certain inputs.

## Future Improvements
- Expand the dataset to include more artists and songs.
- Improve error handling for incorrect user input.
- Limit duplicate songs in generated playlists.
- Allow user customization for playlist size, randomness, or top tracks selection.

## Skills & Tools
- Python
- CSV data handling
- User input validation
- Algorithmic playlist generation
- Debugging edge cases

## Example Scenarios
**Best-case scenario:** All user inputs match entries in the CSVs and the playlist is generated correctly.  

**Worst-case scenario:** None of the user inputs match the CSVs, and the program provides guidance to correct inputs.


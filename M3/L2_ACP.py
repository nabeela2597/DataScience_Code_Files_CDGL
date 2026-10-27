# ================================
# SMART NOTES ORGANIZER
# ================================

# ---------- SETUP (given to you) ----------
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample file 'class-notes.txt' created.")


# ---------- PART 1: read(40) ----------
print("\nPART 1: Preview with read(40)")
# YOUR CODE HERE
# Open class-notes.txt in read mode, print the first 40 characters, close it.


# ---------- PART 2: readlines() ----------
print("\nPART 2: readlines()")
# YOUR CODE HERE
# Open the file, use readlines() to get a list, close the file.
# Print how many lines there are.
# Then print each line with its number, like:  1 -> IMPORTANT: ...
# Use .strip() so you do not get blank lines between them.


# ---------- PART 3: loop line by line ----------
print("\nPART 3: Loop line by line")
# YOUR CODE HERE
# Open the file again and use  for line in file:  to print each line.
# Print it as:  Reading: <the line>


# ---------- PART 4: filter with a condition ----------
print("\nPART 4: Filter with a condition")
# YOUR CODE HERE
# Loop through the file. If the line starts with "SKIP", print  Skipped: <line>
# Otherwise print  Kept: <line>
# Count how many you kept and how many you skipped, and print the totals at the end.


# ---------- PART 5: copy selected lines ----------
print("\nPART 5: Copy selected lines to a new file")
# YOUR CODE HERE
# Read all the lines into a list.
# Open organized-notes.txt in WRITE mode.
# Write only the lines that start with "IMPORTANT" or "TODO".
# Close both files. Print how many lines you copied.


# ---------- PART 6: show the result ----------
print("\nPART 6: Organized notes")
# YOUR CODE HERE
# Open organized-notes.txt and print ev
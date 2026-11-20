# race_qualifiers.py

total_athletes = 0
qualified = 0
winner_name = ""
winner_time_str = ""
winner_seconds = 999999  # start very high so first valid time wins

while True:
    name = input("Enter athlete's name (x to end): ")
    if name == "x" or name == "X":
        break

    time_str = input("Enter time as mm:ss: ")

    # --- Validate time ---
    # Must contain :  e.g. "abc", "5" have no colon = invalid
    if ":" not in time_str:
        print("Invalid time - ignored")
        continue

    parts = time_str.split(":")
    if len(parts) != 2:
        print("Invalid time - ignored")
        continue

    min_part = parts[0]
    sec_part = parts[1]

    # Both parts must be digits
    if not min_part.isdigit() or not sec_part.isdigit():
        print("Invalid time - ignored")
        continue

    minutes = int(min_part)
    seconds = int(sec_part)

    # Seconds must be 0-59, e.g. 22:75 is invalid
    if seconds >= 60 or seconds < 0 or minutes < 0:
        print("Invalid time - ignored")
        continue

    # --- Valid time ---
    total_seconds = minutes * 60 + seconds
    total_athletes = total_athletes + 1

    # Qualifier: 25:00 or less = 1500 seconds or less
    if total_seconds <= 25 * 60:
        qualified = qualified + 1

    # Winner: lowest time. Use < not <= so tie keeps FIRST athlete
    if total_seconds < winner_seconds:
        winner_seconds = total_seconds
        winner_name = name
        winner_time_str = time_str

# --- Output ---
if total_athletes == 0:
    print("No athletes entered")
else:
    print(f"Winner: {winner_name} ({winner_time_str})")
    print(f"Qualified: {qualified} of {total_athletes}")
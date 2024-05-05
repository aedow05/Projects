from race import run_the_race
from shotput import go_shotput

competitor_count = 3


while competitor_count < 3 or competitor_count > 8:
    competitor_count = int(input('How many competitors are there? (3 to 8) '))

# Run the race
run_the_race(competitor_count)

# Wait for the user to press Enter before going to the next event
input('Enter to go to the next event.')

# Run the shotput event
go_shotput(competitor_count)


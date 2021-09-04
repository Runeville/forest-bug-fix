# All my classes
physics = 100
programming = 45
reading = 40
music = 30

studies = [physics, programming, reading, music]
full_time = sum(studies)


def percent_from_number(part: int, number: int):
    """ Returns percent from number """
    return part * 100 / number


# Defining all percents
physics_percent = percent_from_number(physics, full_time)
programming_percent = percent_from_number(programming, full_time)
reading_percent = percent_from_number(reading, full_time)
music_percent = percent_from_number(music, full_time)

percents = [physics_percent, programming_percent, reading_percent, music_percent]

# Defining all rounded percents
physics_percent_rounded = round(percent_from_number(physics, full_time))
programming_percent_rounded = round(percent_from_number(programming, full_time))
reading_percent_rounded = round(percent_from_number(reading, full_time))
music_percent_rounded = round(percent_from_number(music, full_time))

percents_rounded = [physics_percent_rounded, programming_percent_rounded, reading_percent_rounded, music_percent_rounded]

# Getting a list with values after dots like 0.8784, 0.1734
after_dot_percents = [num - int(num) for num in percents]

print(f"Result with bug: {sum(percents_rounded)}%")
print(f"Percentage with bug: {[str(percent) + '%' for percent in percents_rounded]}")
print()

if sum(percents_rounded) > 100:  # If sum of "percents_rounded" > 100
    minimal_after_dot_percent = min(after_dot_percents)  # Find minimal value after dot from "after_dot_percents" list
    minimal_after_dot_percent_index = after_dot_percents.index(minimal_after_dot_percent)  # Getting its index in a list
    percents_rounded[minimal_after_dot_percent_index] \
        = percents_rounded[minimal_after_dot_percent_index] - 1  # Increasing it by one

if sum(percents_rounded) < 100:  # If sum of "percents_rounded" < 100
    max_after_dot_percent = max(after_dot_percents)  # Find max value after dot from "after_dot_percents" list
    max_after_dot_percent_index = after_dot_percents.index(max_after_dot_percent)  # Getting its index in a list
    percents_rounded[max_after_dot_percent_index] \
        = percents_rounded[max_after_dot_percent_index] + 1  # Decreasing it by one

print(f"Real percentage: {[str(percent) + '%' for percent in percents_rounded]}")
print(f"Real result: {sum(percents_rounded)}%")

input()

with open('f:/jsw20042025/jsw_object_training/combined_detection.py', 'r') as file:
    content = file.read()

# Add inversion for Line 1 in both places
modified_content = content.replace(
    '                                direction = calculate_direction(\n                                    previous_positions[id], center, \n                                    line[\'start\'], line[\'end\']\n                                )\n                                \n                                # Get current time',
    '                                direction = calculate_direction(\n                                    previous_positions[id], center, \n                                    line[\'start\'], line[\'end\']\n                                )\n                                \n                                # Invert direction for Line 1 only\n                                if line[\'name\'] == \'Line 1\':\n                                    direction = \"OUT\" if direction == \"IN\" else \"IN\"\n                                \n                                # Get current time',
    2  # Replace both occurrences - one in video and one in RTSP
)

with open('f:/jsw20042025/jsw_object_training/combined_detection.py', 'w') as file:
    file.write(modified_content)

print("Successfully added inversion of direction for Line 1!")

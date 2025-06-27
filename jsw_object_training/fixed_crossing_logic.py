# This code snippet contains the fixed line crossing detection logic
# to be added to the combined_detection.py file

def calculate_direction(old_point, new_point, line_start, line_end):
    """Calculate the direction of movement relative to the line"""
    # Get the line vector
    line_vector = (line_end[0] - line_start[0], line_end[1] - line_start[1])
    
    # Get the movement vector
    movement_vector = (new_point[0] - old_point[0], new_point[1] - old_point[1])
    
    # Calculate the cross product for direction
    cross_product = line_vector[0] * movement_vector[1] - line_vector[1] * movement_vector[0]
    
    # Determine the direction based on the cross product
    # This gives us more accurate IN/OUT detection based on object movement direction
    return "IN" if cross_product > 0 else "OUT"

# Improved line crossing detection code block (for video processing)
"""
# Create a unique key for this object-line pair
crossing_key = f"{id}_{line_idx}"

# Only process if the object has crossed the line
if prev_side != current_side:
    # Determine the direction using vector calculation
    direction = calculate_direction(
        previous_positions[id], center, 
        line['start'], line['end']
    )
    
    # Get current time
    current_time = time.time()
    
    # Check if object already crossed this line recently
    if crossing_key in crossed_lines:
        last_cross_time, last_direction = crossed_lines[crossing_key]
        # Only count if it's been more than 1.5 seconds since last crossing
        # or the direction has changed
        if (current_time - last_cross_time > 1.5) or (direction != last_direction):
            if direction == "IN":
                line['in_count'] += 1
            else:
                line['out_count'] += 1
            # Update with new timestamp and direction
            crossed_lines[crossing_key] = (current_time, direction)
    else:
        # First time crossing this line
        if direction == "IN":
            line['in_count'] += 1
        else:
            line['out_count'] += 1
        # Record the crossing
        crossed_lines[crossing_key] = (current_time, direction)
"""

# Initialization section change:
"""
# Dictionary to track which lines objects have crossed and in which direction
# Format: {object_id_line_idx: (timestamp, direction)}
crossed_lines = {}
"""

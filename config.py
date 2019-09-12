import os

data_path = 'images/'
file_name = 'current_clock.png'
test_name = 'test.jpg'
full_path = os.path.join(data_path, file_name)

line_width = 10
correction = 10
image_dimension = 650
large_circle_diameter = 450 - correction
little_circle_diameter = line_width * 2 - correction
large_circle_radius = large_circle_diameter / 2
little_circle_radius = little_circle_diameter / 2
image_center = image_dimension / 2
large_top_point = image_center - large_circle_radius
large_bottom_point = image_center + large_circle_radius
little_top_point = image_center - little_circle_radius
little_bottom_point = image_center + little_circle_radius
minutes_hand_length = 80
hours_hand_length = 60

# little lines
lines_length = 20

# other
log_info_message = 'Clock image was updated'
log_warning_message = 'Clock image was NOT updated'
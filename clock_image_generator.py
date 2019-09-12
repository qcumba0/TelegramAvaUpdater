import sys, os
from PIL import Image, ImageDraw
from config import *

from math import sin, cos, pi, radians
from datetime import timedelta,datetime

def draw_ellipse(image, bounds,width=line_width, outline='black', antialias=10):
    """Improved ellipse drawing function, based on PIL.ImageDraw."""

    mask = Image.new(
        size=[int(dim * antialias) for dim in image.size],
        mode='L', color='black')
    draw = ImageDraw.Draw(mask)

    for offset, fill in (width/-2.0, 'white'), (width/2.0, 'black'):
        left, top = [(value + offset) * antialias for value in bounds[:2]]
        right, bottom = [(value - offset) * antialias for value in bounds[2:]]
        draw.ellipse([left, top, right, bottom], fill=fill)

    mask = mask.resize(image.size, Image.LANCZOS)
    image.paste(outline, mask=mask)
    
def draw_line(image, points, color='black'):
    draw  =  ImageDraw.Draw(image)
    linePoints = []
    for point in points:
        draw.ellipse((point[0]-3, point[1]-3, point[0]+3, point[1]+3), fill=color)
        linePoints.append(point[0])
        linePoints.append(point[1])
    draw.line(linePoints, fill=color, width=line_width)

def draw_aa_line(image, bounds,width=line_width, outline='black', antialias=10):
    mask = Image.new(
        size=[int(dim * antialias) for dim in image.size],
        mode='L', color='black')
    draw = ImageDraw.Draw(mask)

    for offset, fill in (width/-2.0, 'white'), (width/2.0, 'black'):
        left, top = [(value + offset) * antialias for value in bounds[:2]]
        right, bottom = [(value - offset) * antialias for value in bounds[2:]]
        draw.line([left, top, right, bottom], fill=fill,width=width)

    mask = mask.resize(image.size, Image.LANCZOS)
    image.paste(outline, mask=mask)
      
def draw_main_circles():
  image = Image.new(mode='RGB', size=(image_dimension, image_dimension), color = 'white')

  big_ellipse_box = [large_top_point, large_top_point, large_bottom_point, large_bottom_point]
  little_ellipse_box = [little_top_point, little_top_point, little_bottom_point, little_bottom_point]

  draw_ellipse(image, big_ellipse_box)
  draw_ellipse(image, little_ellipse_box)
  
  return image

def get_coordinates_for_minute_hand():
  m = int(datetime.now().strftime("%M"))
  angle = radians(m * 6)
  x, y = sin(angle) * minutes_hand_length * 2, cos(angle) * minutes_hand_length * 2

  return x, y

def get_coordinates_for_hour_hand():
  h = int(datetime.now().strftime("%I"))
  m = int(datetime.now().strftime("%M"))
  angle = radians(0.5 * (60 * h + m))
  x, y = sin(angle) * hours_hand_length *2, cos(angle)*hours_hand_length *2
  return x, y 

def generate_clock_image():
	image = draw_main_circles()
	image = draw_hours_lines(image)
	
	draw = ImageDraw.Draw(image)

	x_minutes, y_minutes  = get_coordinates_for_minute_hand()
	x_hours, y_hours  = get_coordinates_for_hour_hand()

	minute_line_coordinate = (image_center, image_center, int(round(x_minutes + image_center)), int(round(abs(y_minutes - image_center))))
	hour_line_coordinate = (image_center, image_center, int(round(x_hours + image_center)), int(round(abs(y_hours - image_center))))

	draw.line(minute_line_coordinate, fill='black', width=line_width-2)
	draw.line(hour_line_coordinate, fill='black', width=line_width-2)

	image = image.resize((image_dimension//2, image_dimension//2), Image.ANTIALIAS)

	
	image.save(full_path)
	return full_path
	
def draw_hours_lines(image):
	  lines_coordinates = list()
  
	  bottom = [(image_center, image_center+large_circle_radius), (image_center, image_center+large_circle_radius - lines_length)]
	  lines_coordinates.append(bottom)
	  
	  top = [(image_center, image_center-large_circle_radius), (image_center, image_center-large_circle_radius + lines_length)]
	  lines_coordinates.append(top)
	  
	  right = [(image_center-large_circle_radius, image_center), (image_center-large_circle_radius + lines_length, image_center)]
	  lines_coordinates.append(right)
	  
	  left = [(image_center+large_circle_radius, image_center), (image_center+large_circle_radius - lines_length, image_center)]
	  lines_coordinates.append(left)
	  
	  for line_coordinate in lines_coordinates:
		  draw = ImageDraw.Draw(image)
		  draw.line(line_coordinate, fill='black', width=line_width)
	  
	  return image
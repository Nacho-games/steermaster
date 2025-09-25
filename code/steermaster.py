#importamos librerias
import pygame 
import math
import sys
import random

#text file stuff
# Save a time (minutes, seconds, milliseconds as a fraction, e.g., .27) for a specific level
def save_time(level, minutes, seconds, milliseconds, deaths=None):
    global pb
    current_times = load_times()  # Load all current times from the file


    # Convert the new time into total milliseconds for comparison
    new_time_total = convert_to_total_milliseconds(minutes, seconds, milliseconds)
    
    if level in current_times:
        if level == 4:  # Special handling for level 4
            current_best_time, current_best_deaths = current_times[level][:3], current_times[level][3]
            current_best_total = convert_to_total_milliseconds(*current_best_time)

            # Update only if the new time is better or deaths are fewer
            if new_time_total < current_best_total or (new_time_total == current_best_total and deaths < current_best_deaths):
                current_times[level] = (minutes, seconds, milliseconds, deaths)
        else:  # Handle levels 1–3
            current_best_time = current_times[level]
            current_best_total = convert_to_total_milliseconds(*current_best_time)
            # Update only if the new time is better
            if new_time_total < current_best_total:
                current_times[level] = (minutes, seconds, milliseconds)
                pb = True

            else:
            	pb = False
    else:
        # Save the time if no time exists for the level
        if level == 4:
            current_times[level] = (minutes, seconds, milliseconds, deaths)
        else:
            current_times[level] = (minutes, seconds, milliseconds)

        pb = True

    save_all_times(current_times)  # Save the updated times


# Load all saved times from the file
def load_times():
	try:
		with open("steer_master_times.txt", "r") as file:
			times = {}
			for line in file:
				line = line.strip()  # Remove any leading/trailing spaces
                
				# Skip empty lines
				if not line:
					continue
                
				# Ensure the line contains exactly 4 values (level, minutes, seconds, milliseconds)
				parts = line.split(",")
				# Handle level 4 with the additional 'deaths' field
				if len(parts) == 5 and int(parts[0]) == 4:  # Level 4 format
					level, minutes, seconds, milliseconds, deaths = parts
					times[int(level)] = (int(minutes), int(seconds), int(milliseconds), int(deaths))
				elif len(parts) == 4:  # Levels 1–3 format
					level, minutes, seconds, milliseconds = parts
					times[int(level)] = (int(minutes), int(seconds), int(milliseconds))
 
			return times
	except FileNotFoundError:
		return {} 

		
# Save all times to the file (overwrite the file with updated data)
def save_all_times(times):
    with open("steer_master_times.txt", "w") as file:
        for level, time_data in times.items():
            if level == 4:  # Handle level 4 separately
                minutes, seconds, milliseconds, deaths = time_data
                file.write(f"{level},{minutes},{seconds},{milliseconds},{deaths}\n")
            else:  # Handle levels 1–3
                minutes, seconds, milliseconds = time_data
                file.write(f"{level},{minutes},{seconds},{milliseconds}\n")

# Convert a time to total milliseconds for comparison
def convert_to_total_milliseconds(minutes, seconds, milliseconds):
    return (minutes * 60 * 1000) + (seconds * 1000) + milliseconds

# Find the lowest time across all levels
def get_lowest_time():
    current_times = load_times()  # Load all current times
    if not current_times:
        return None  # No times saved yet
    lowest_level = min(
        current_times,
        key=lambda level: convert_to_total_milliseconds(*current_times[level])
    )
    return lowest_level, current_times[lowest_level]






#people
people_x_size = 70
people_y_size = people_x_size / 2
people_velocity = -3	

#PERSONAS INTERSECCION 1
people1_1 = pygame.Rect(295, 110, people_x_size, people_y_size)
people1_2 = pygame.Rect(295, 330, people_x_size, people_y_size)
people1_3 = pygame.Rect(295, 550, people_x_size, people_y_size)
people1_4 = pygame.Rect(295, 770, people_x_size, people_y_size)
people1_5 = pygame.Rect(295, 990, people_x_size, people_y_size)

# LISTA DE PERSONAS INTERSECCION 1
people_first_intersection_list = [people1_1, people1_2, people1_3, people1_4, people1_5]

#PERSONAS INTERSECCION 2
people2_1 = pygame.Rect(435 -30, 220, people_y_size - 10, people_x_size -20)
people2_2 = pygame.Rect(670 -30, 220, people_y_size - 10, people_x_size -20)
people2_3 = pygame.Rect(895 -30, 220, people_y_size - 10, people_x_size -20)
people2_4 = pygame.Rect(1120 -30, 220, people_y_size - 10, people_x_size -20)
people2_5 = pygame.Rect(210 -30, 220, people_y_size - 10, people_x_size -20)
people2_6 = pygame.Rect(-15 -30, 220, people_y_size - 10, people_x_size -20)
people2_7 = pygame.Rect(-240 -30, 220, people_y_size - 10, people_x_size -20)

# LISTA DE PERSONAS INTERSECCION 2
people_second_intersection_list = [people2_1, people2_2, people2_3, people2_4, people2_5, people2_6, people2_7]

#PERSONAS INTERSECCION 3
people3_1 = pygame.Rect(435, 325, people_y_size - 10, people_x_size -20)
people3_2 = pygame.Rect(670, 325, people_y_size - 10, people_x_size -20)
people3_3 = pygame.Rect(895, 325, people_y_size - 10, people_x_size -20)
people3_4 = pygame.Rect(1120, 395, people_y_size - 10, people_x_size -20)
people3_5 = pygame.Rect(210, 325, people_y_size - 10, people_x_size -20)
people3_6 = pygame.Rect(-15, 395, people_y_size - 10, people_x_size -20)
people3_7 = pygame.Rect(-240, 395, people_y_size - 10, people_x_size -20)

# LISTA DE PERSONAS INTERSECCION 3
people_third_intersection_list = [people3_1, people3_2, people3_3,people3_4, people3_5, people3_6, people3_7]

#paredes nivel 1
rect1_1 = pygame.Rect(0, 0, 200, 265)
rect1_2 = pygame.Rect(0, 0, 1200, 75)
rect1_3 = pygame.Rect(407, 0, 65, 465)
rect1_4 = pygame.Rect(0, 335, 335, 270)
rect1_5 = pygame.Rect(270, 135, 65, 200)
rect1_6 = pygame.Rect(0, 535, 1200, 65)
rect1_7 = pygame.Rect(810, 75, 400, 200)
rect1_8 = pygame.Rect(540, 400, 325, 135)
rect1_9 = pygame.Rect(540, 145, 67, 270)
rect1_10 = pygame.Rect(607, 145, 135, 67)
rect1_11 = pygame.Rect(677, 280, 318, 53)
rect1_12 = pygame.Rect(930, 335, 65, 140)
rect1_13 = pygame.Rect(1065, 335, 255, 200)
Info_lvl_1 = pygame.Rect(860, 10, 330, 175)


#LISTA DE PAREDES NIVEL 1
rects_to_collide_map1 = [

rect1_1, rect1_2, rect1_3, rect1_4, 
rect1_5, rect1_6, rect1_7, rect1_8, 
rect1_9, rect1_10, rect1_11, rect1_12, 
rect1_13

]

#momentarily effects
splash = pygame.Rect(0, 0, 150, 150)
particles_rect = pygame.Rect(0, 0, 35, 35)
cross_rect = pygame.Rect(0, 0, 25, 25)



#paredes nivel 2
rect2_1 = pygame.Rect(0,0, 100, 265)
rect2_2 = pygame.Rect(110,230, 285, 30)
rect2_3 = pygame.Rect(100,210, 40, 55)
rect2_4 = pygame.Rect(0,0, 1200, 35)
rect2_5 = pygame.Rect(0,35, 130, 30)
rect2_6 = pygame.Rect(192, 120, 330, 40)
rect2_7 = pygame.Rect(490, 160, 40, 205)
rect2_8 = pygame.Rect(0, 337, 530, 40)
rect2_9 = pygame.Rect(0, 337, 110, 223)
rect2_10 = pygame.Rect(0, 555, 1200, 45)
rect2_11 = pygame.Rect(192, 450, 450, 30)
rect2_12 = pygame.Rect(605, 0, 35, 480)
rect2_13 = pygame.Rect(710, 490, 490, 60)
rect2_14 = pygame.Rect(720, 340, 160, 400)
rect2_15 = pygame.Rect(840, 170, 40, 400)
rect2_16 = pygame.Rect(1080, 345, 150, 400)
rect2_17 = pygame.Rect(660, 0, 540, 100)
rect2_18 = pygame.Rect(660, 0, 100, 260)
rect2_19 = pygame.Rect(950, 100, 50, 320)
rect2_20 = pygame.Rect(1000, 100, 200, 160)

#LISTA DE PAREDES NIVEL 2
rects_to_collide_map2 = [

rect2_1, rect2_2, rect2_3, rect2_4, 
rect2_5, rect2_6, rect2_7, rect2_8, 
rect2_9, rect2_10, rect2_11, rect2_12, 
rect2_13, rect2_14, rect2_15, rect2_16, 
rect2_17, rect2_18, rect2_19, rect2_20

] 

#Nieve nivel 3
snow_1 = pygame.Rect(640, 200, 150, 300)
snow_2 = pygame.Rect(430, 450, 200, 100)
snow_3 = pygame.Rect(580, 410, 150, 140)


#Lista nieve
snow_block = pygame.Rect(240, 260, 75, 75)
snow_rects = [snow_1, snow_2, snow_3]


#paredes nivel 3
rect3_1 = pygame.Rect(0, 0, 1200, 65)
rect3_2 = pygame.Rect(0, 185, 170, 80)
rect3_3 = pygame.Rect(160, 185, 40, 45)
rect3_4 = pygame.Rect(0, 60, 637, 137)
rect3_5 = pygame.Rect(347, 185, 135, 50)
rect3_6 = pygame.Rect(385, 210, 75, 50)
rect3_7 = pygame.Rect(480, 185, 25, 40)
rect3_8 = pygame.Rect(460, 210, 25, 37)
rect3_9 = pygame.Rect(485, 180, 130, 27)
rect3_10 = pygame.Rect(0, 335, 165, 270)
rect3_11 = pygame.Rect(165, 372, 37, 270)
rect3_12 = pygame.Rect(200, 405, 263, 270)
rect3_13 = pygame.Rect(0, 518, 1200, 100)
rect3_14 = pygame.Rect(463, 495, 25, 25)
rect3_15 = pygame.Rect(347, 372, 133, 30)
rect3_16 = pygame.Rect(385, 330, 147, 35)
rect3_17 = pygame.Rect(385, 365, 120, 10)
rect3_18 = pygame.Rect(532, 330, 22, 28)
rect3_19 = pygame.Rect(460, 318, 125, 15)
rect3_20 = pygame.Rect(545, 325, 20, 20)
rect3_21 = pygame.Rect(482, 298, 95, 20)
rect3_22 = pygame.Rect(505, 273, 60, 25)
rect3_23 = pygame.Rect(528, 261, 27, 12)
rect3_24 = pygame.Rect(580, 195, 92, 30)
rect3_25 = pygame.Rect(605, 225, 80, 25)
rect3_26 = pygame.Rect(630, 185, 30, 10)
rect3_27 = pygame.Rect(615, 250, 70, 20)
rect3_28 = pygame.Rect(625, 270, 60, 25)
rect3_29 = pygame.Rect(640, 295, 45, 80)
rect3_30 = pygame.Rect(605, 367, 60, 30)
rect3_31 = pygame.Rect(628, 345, 15, 30)
rect3_32 = pygame.Rect(670, 210, 15, 15)
rect3_33 = pygame.Rect(580, 390, 55, 30)
rect3_34 = pygame.Rect(532, 408, 80, 37)
rect3_35 = pygame.Rect(537, 445, 50, 23)
rect3_36 = pygame.Rect(512, 425, 20, 20)
rect3_37 = pygame.Rect(630, 65, 20, 70)
rect3_38 = pygame.Rect(650, 65, 55, 17)
rect3_39 = pygame.Rect(650, 82, 28, 15)
rect3_40 = pygame.Rect(615, 493, 585, 25)
rect3_41 = pygame.Rect(640, 468, 565, 25)
rect3_42 = pygame.Rect(665, 443	, 545, 25)
rect3_43 = pygame.Rect(690, 436, 510, 7)
rect3_44 = pygame.Rect(690, 424, 275, 17)
rect3_45 = pygame.Rect(715, 404, 225, 20)
rect3_46 = pygame.Rect(740, 392, 200, 12)
rect3_47 = pygame.Rect(740, 372, 180, 20)
rect3_48 = pygame.Rect(740, 332, 170, 40)
rect3_49 = pygame.Rect(740, 252, 160, 80)
rect3_50 = pygame.Rect(740, 225, 150, 27)
rect3_51 = pygame.Rect(740, 195, 140, 30)
rect3_52 = pygame.Rect(725, 167, 135, 27)
rect3_53 = pygame.Rect(725, 145, 110, 22)
rect3_54 = pygame.Rect(725, 115, 60, 30)
rect3_55 = pygame.Rect(785, 125, 24, 20)
rect3_56 = pygame.Rect(700, 130, 25, 35)
rect3_57 = pygame.Rect(1055, 410, 145, 30)
rect3_58 = pygame.Rect(1080, 385, 120, 25)
rect3_59 = pygame.Rect(1110, 360, 90, 25)
rect3_60 = pygame.Rect(1135, 335, 65, 25)
rect3_61 = pygame.Rect(1145, 325, 55, 10)
rect3_62 = pygame.Rect(1155, 315, 45, 10)
rect3_63 = pygame.Rect(800, 65, 400, 15)
rect3_64 = pygame.Rect(835, 80, 635, 15)
rect3_65 = pygame.Rect(860, 95, 340, 25)
rect3_66 = pygame.Rect(885, 120, 315, 20)
rect3_67 = pygame.Rect(915, 140, 285, 30)
rect3_68 = pygame.Rect(935, 170, 265, 35)
rect3_69 = pygame.Rect(945, 205, 255, 35)
rect3_70 = pygame.Rect(955, 240, 245, 25)
rect3_71 = pygame.Rect(955, 265, 187, 7)
rect3_72 = pygame.Rect(955, 272, 160, 7)
rect3_73 = pygame.Rect(955, 279, 145, 33)
rect3_74 = pygame.Rect(960, 312, 120, 30)
rect3_75 = pygame.Rect(970, 342, 80, 25)
rect3_76 = pygame.Rect(990, 367, 35, 20)

#LISTA DE PAREDES NIVEL 3
rects_to_collide_map3 = [

	snow_block,

	rect3_1, rect3_2, rect3_3, rect3_4, 
	rect3_5, rect3_6, rect3_7, rect3_8, 
	rect3_9, rect3_10, rect3_11, rect3_12,
	rect3_13, rect3_14, rect3_15, rect3_16, 
	rect3_17, rect3_18, rect3_19, rect3_20, 
	rect3_21, rect3_22, rect3_23, rect3_24,
	rect3_25, rect3_26, rect3_27, rect3_28, 
	rect3_29, rect3_30, rect3_31, rect3_32, 
	rect3_33, rect3_34, rect3_35, rect3_36,
	rect3_37, rect3_38, rect3_39, rect3_40, 
	rect3_41, rect3_42, rect3_43, rect3_44, 
	rect3_45, rect3_46, rect3_47, rect3_48,
	rect3_49, rect3_50, rect3_51, rect3_52,
	rect3_53, rect3_54, rect3_55, rect3_56,
	rect3_57, rect3_58, rect3_59, rect3_60,
	rect3_61, rect3_62, rect3_63, rect3_64,
	rect3_65, rect3_66, rect3_67, rect3_68,
	rect3_69, rect3_70, rect3_71, rect3_72,
	rect3_73, rect3_74, rect3_75, rect3_76

]	

higlighted_rect = rect3_1


#BOTONES DE MENU
sound_but = pygame.Rect(380, 400, 400, 100)
speedrun = pygame.Rect(350, 200, 520, 100)
levels_but = pygame.Rect(350, 300, 520, 100)
level_1_but = pygame.Rect(200, 0, 800, 120)
level_2_but = pygame.Rect(200, 120, 800, 120)
level_3_but = pygame.Rect(200, 240, 800, 120)
back_arrow_but = pygame.Rect(0, 10, 125, 100)
difficulty_but = pygame.Rect(20, 365, 290, 80)
skins_but = pygame.Rect(880, 200, 290, 80)
info_but = pygame.Rect(460, 510, 235, 80)
leaderboard_but = pygame.Rect(20, 230, 310, 70)
car_gift = pygame.Rect(940, 300, 75, 37.5)

#cheater rects
cheater_rect1 = pygame.Rect(0, 0, 200, 50)
cheater_rect2 = pygame.Rect(200, 0, 200, 50)
cheater_rect3 = pygame.Rect(400, 0, 200, 50)
cheater_rect4 = pygame.Rect(600, 0, 200, 50)
cheater_rect5 = pygame.Rect(800, 0, 200, 50)
cheater_rect6 = pygame.Rect(1000, 0, 200, 50)
cheater_rect7 = pygame.Rect(0, 550, 200, 50)
cheater_rect8 = pygame.Rect(200, 550, 200, 50)
cheater_rect9 = pygame.Rect(400, 550, 200, 50)
cheater_rect10 = pygame.Rect(600, 550, 200, 50)
cheater_rect11 = pygame.Rect(800, 550, 200, 50)
cheater_rect12 = pygame.Rect(1000, 550, 200, 50)

cheater_rect13 = pygame.Rect(0, 50, 30, 125)
cheater_rect14 = pygame.Rect(0, 175, 30, 125)
cheater_rect15 = pygame.Rect(0, 300, 30, 125)
cheater_rect16 = pygame.Rect(0, 425, 30, 125)

cheater_rect17 = pygame.Rect(1170, 50, 30, 125)
cheater_rect18 = pygame.Rect(1170, 175, 30, 125)
cheater_rect19 = pygame.Rect(1170, 300, 30, 125)
cheater_rect20 = pygame.Rect(1170, 425, 30, 125)


#vallas
wall_1 = pygame.Rect(385, 15, 35, 250)
wall_2 = pygame.Rect(385, 325, 35, 275)
wall_3 = pygame.Rect(650, 200, 35, 170)
wall_4 = pygame.Rect(720, 130, 45, 90)
wall_5 = pygame.Rect(720, 190, 165, 30)
wall_6 = pygame.Rect(870, 190, 30, 165)
wall_7 = pygame.Rect(525, 435, 75, 30)
wall_8 = pygame.Rect(575, 400, 65, 35)
wall_9 = pygame.Rect(625, 365, 50, 35)

#lista vallas
walls_list = [snow_block, wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9]	

#snow men
snow_man_rect_1 = pygame.Rect(279, 94, 62, 62)
snow_man_rect_2 = pygame.Rect(279, 444, 62, 62)
snow_man_rect_3 = pygame.Rect(777, 258, 62, 62)
snow_man_rect_4 = pygame.Rect(1000, 185, 62, 62)

#cosa de los snowmen
snowballs = []
snow_men_list = [snow_man_rect_1, snow_man_rect_2, snow_man_rect_3, snow_man_rect_4]
cycle_count = 0


#car but rects

car_but_1 = pygame.Rect(20, 10, 300, 120)
car_but_2  = pygame.Rect(880, 10, 300, 120)
car_but_3 = pygame.Rect(20, 150, 300, 120)
car_but_4 = pygame.Rect(330, 140, 270, 130)
car_but_5 = pygame.Rect(620, 140, 270, 130)
car_but_6 = pygame.Rect(900, 140, 270, 130)
car_but_7 = pygame.Rect(20, 300, 300, 120)
car_but_8 = pygame.Rect(330, 300, 270, 130)
car_but_9 = pygame.Rect(615, 295, 270, 130)
car_but_10 = pygame.Rect(900, 300, 270, 130)
car_but_11 = pygame.Rect(20, 450, 300, 120)
car_but_12 = pygame.Rect(330, 450, 270, 130)
car_but_13 = pygame.Rect(615, 450, 270, 130)
car_but_14 = pygame.Rect(900, 450, 270, 130)
tick_box = pygame.Rect(1200, 600, 100, 100)



car_buts = [

	car_but_1, car_but_2, car_but_3,
	car_but_4, car_but_5, car_but_6,
	car_but_7, car_but_8, car_but_9,
	car_but_10, car_but_11, car_but_12,
	car_but_13, car_but_14

	]


# Función para rotar un punto alrededor de un centro
def rotate_point(point, angle, center):
	angle_rad = math.radians(-angle)
	x, y = point
	cx, cy = center

	# Rotación del punto (x, y) alrededor del centro (cx, cy)
	rotated_x = cx + math.cos(angle_rad) * (x - cx) - math.sin(angle_rad) * (y - cy)
	rotated_y = cy + math.sin(angle_rad) * (x - cx) + math.cos(angle_rad) * (y - cy)
	return rotated_x, rotated_y


#definimos colores RGB
Black = (0, 0, 0)
White = (255, 255, 255)
Yellow = (255, 255, 0)
Red = (255, 102, 102)
Blue = (0, 0, 255, 128)
Green = (0, 255, 0)
Dark_Green = (0, 100, 0)
Light_blue = (0, 255, 255)
Purple = (120, 0, 200)
Pink = (255, 0, 255)
Cool_blue = (0, 104, 132)
Grey = (50, 50, 50)
Light_grey = (128, 128, 128)
Orange = (255, 168, 0)
Grey = (50, 50, 50)

#inicializamos pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

#texto
font_size = 70  
font = pygame.font.Font(None, font_size)
font_size2 = 60
font2 = pygame.font.Font(None, font_size2)
font_size3 = 95
font3 = pygame.font.Font(None, font_size3)
font_size4 = 40
font4 = pygame.font.Font(None, font_size4)
font_size5 = 60
font5 = pygame.font.Font(None, font_size5)

#definimos variables

# PANTALLA
screen_width = 1200
screen_length = 600
half_width = screen_width / 2
half_length = screen_length / 2


#COCHE
carxsize = 75
carysize = 37
rot_speed = 4.5
angle = 0
speed = 4
car_init_y = half_length - 20
car_init_x = 25
car_x = car_init_x
car_y = car_init_y
velocity_x = 0
velocity_y = 0
touching_ice = True
snowball_hit_number = 0
max_health = 3
current_health = max_health
health_length = 192  
health_per_point = health_length // max_health
current_health_length = health_length
reduce_health = False
health_reduction_speed = 2
force_reset_health = False
inflation_min = 15
inflation_value = 27.5

#PANATLLAS VISUALES
menu = True
sound = True
mouse_visibility = True	


#CUADRADO DE INFORMACION
level_txt_x = Info_lvl_1.centerx
level_txt_y =Info_lvl_1.top + 30
death_txt_x = Info_lvl_1.centerx
death_txt_y =Info_lvl_1.top + 85
time_txt_x = Info_lvl_1.centerx -40
time_txt_y =Info_lvl_1.top + 140
text_level_hight_end_of_levels = 375
level_name_info_rect_longness = 440
level_name_info_rect = pygame.Rect(0, 540, level_name_info_rect_longness, 60)
tickx = 1500
ticky = 1300

#variables de menus
level_selected = False
is_selector_active = True
end_of_levels = False
back_action = False
pb = False


#VALORES DEL CUADRADO DE INFORMACION
death = 0
start_time = None
starting_timer = True
data_box = True
ballx = 600



# CHEAT CODE LOGIC
key = pygame.key.get_pressed()

cheat_sequence = [

pygame.K_c, pygame.K_h, pygame.K_e, 
pygame.K_a, pygame.K_t, pygame.K_s, 

]
current_index = 0  # Tracks current position in the cheat sequence
cheat = False
cheater = False

#SPLASH
splash_v = False
splash_time = 0
just_died = False



#NIVEL
level_map = 1
level_selector_menu = False
number_of_levels = 3
first_time = True

#Señal
frist_time_touching_snow = True
first_time_touching_ice = True
sound_first_time = True
sound_first_time2 = True
sign_time = 0
ice_count = 0
snow_count = 0
sign = True
dragging = False
percentage_of_difficulty = 50
right_difficulty = True
first_time_difficulty = True
dk_how_2_call_this_variable = 0

#jugador
rect_surface = pygame.Surface((carxsize, carysize)) 
car = pygame.Rect(car_init_x, car_init_y, carxsize, carysize)
smaller_hit_box = car.inflate(-35, -20)
car_chosen = False

#screen
screen_rect = pygame.Rect(0, 0, screen_width, screen_length)

#cargamos archivos
map1_image= pygame.image.load("Map1.png")
map1_adjus = pygame.transform.scale(map1_image,(screen_width, screen_length))
map2_image= pygame.image.load("Map2.png")
map2_adjus = pygame.transform.scale(map2_image,(screen_width, screen_length))
map3_image= pygame.image.load("Map_3.png")
map3_adjus = pygame.transform.scale(map3_image,(screen_width, screen_length))
menu_on = pygame.image.load("menu_sound_on.png")
menu_off = pygame.image.load("menu_sound_off.png")
Level_selector_i = pygame.image.load("Level_Selector.png")
difficulty_menu_i = pygame.image.load("difficulty_menu.png")
skins_menu_i = pygame.image.load("skins_menu.png")
info_menu_i = pygame.image.load("Info.png")
leaderboard_i = pygame.image.load("leaderboard.png")
menu_adjus_on = pygame.transform.scale(menu_on,(screen_width, screen_length))
menu_adjus_off = pygame.transform.scale(menu_off,(screen_width, screen_length))
Level_selector_adjus = pygame.transform.scale(Level_selector_i,(screen_width, screen_length))
difficulty_menu_background = pygame.transform.scale(difficulty_menu_i,(screen_width, screen_length))
skins_menu_background = pygame.transform.scale(skins_menu_i,(screen_width, screen_length))
info_menu_background = pygame.transform.scale(info_menu_i,(screen_width, screen_length))
leaderboard_background = pygame.transform.scale(leaderboard_i,(screen_width, screen_length))
back_arrow = pygame.image.load("back_arrow.png")
back_arrow_adjus = pygame.transform.scale(back_arrow,(125, 100))
cheater_i = pygame.image.load("cheater.jpg")
cheater_adjus = pygame.transform.scale(cheater_i, (200, 50))
cheater_vert_i = pygame.image.load("cheater_verticle.jpg")
cheater_vert_adjus = pygame.transform.scale(cheater_vert_i, (30, 125))
snow_man_i = pygame.image.load("snow_man.png")
snow_man_adjus = pygame.transform.scale(snow_man_i, (62, 62))
snow_ball_i = pygame.image.load("snow_ball.png")
snow_ball_adjus = pygame.transform.scale(snow_ball_i, (20, 20))

level_1_completed = pygame.image.load("level_1_completed.png")
level_1_completed_adjus = pygame.transform.scale(level_1_completed,(screen_width, screen_length))
level_2_completed = pygame.image.load("level_2_completed.png")
level_2_completed_adjus = pygame.transform.scale(level_2_completed,(screen_width, screen_length))
level_3_completed = pygame.image.load("level_3_completed.png")
level_3_completed_adjus = pygame.transform.scale(level_3_completed,(screen_width, screen_length))
game_completed = pygame.image.load("game_completed.png")
game_completed_adjus = pygame.transform.scale(game_completed,(screen_width, screen_length))
color_bar_i = pygame.image.load("color_bar.png")
color_bar_adjus = pygame.transform.scale(color_bar_i,(1140, 25))
color_bar_rect = pygame.Rect(30, 185, 1140, 25)
settings_ball = [(600, 185), (20)]
new_pb_i = pygame.image.load("new_pb.png")
pb_adjus = pygame.transform.scale(new_pb_i,(400, 175))

persona_i = pygame.image.load("persona.png")
persona_adjus =  pygame.transform.scale(persona_i,(people_x_size, people_y_size))
persona_i_2 = pygame.image.load("persona_2.png")
persona_adjus_2 =  pygame.transform.scale(persona_i_2,(people_y_size - 10, people_x_size -20))
splash_i = pygame.image.load("splash.png")
splash_adjus = pygame.transform.scale(splash_i,(150, 150))
particles = pygame.image.load("particles.png")
splash_adjus = pygame.transform.scale(splash_i,(150, 150))
cross = pygame.image.load("RED-CROSS.png")
cross_adjus = pygame.transform.scale(cross,(25, 25))
particles_adjus = pygame.transform.scale(particles,(35, 35))
heart_i = pygame.image.load("Heart.png")
heart_adjus = pygame.transform.scale(heart_i,(85, 85))
heart_rect = pygame.Rect(235, 5, 95, 85)
life_background = pygame.Rect(275, 20, 220, 52)
life_bar = pygame.Rect(290, 30, health_length, 32)
tick = pygame.image.load("tick.png")
tick_adjus = pygame.transform.scale(tick,(100, 100))
tick_adjus2 = pygame.transform.scale(tick,(50, 50))
sign_i = pygame.image.load("sign.png")
sign_adjus = pygame.transform.scale(sign_i,(200, 175))
smaller_sign_adjus = pygame.transform.scale(sign_i,(100, 87))
no_cross_sign_i = pygame.image.load("no_cross_sign.png")
no_cross_sign_adjus = pygame.transform.scale(no_cross_sign_i,(200, 175))
smaller_no_cross_sign_adjus = pygame.transform.scale(no_cross_sign_i,(100, 87))
sign_rect = pygame.Rect(100, 10, 200, 175)
smaller_sign_rect = pygame.Rect(162, 15, 75, 65)
sad_i = pygame.image.load("sad.png")
sad_adjus = pygame.transform.scale(sad_i,(350, 150))

#cars
car_image_1 = pygame.image.load("Bugatti_Veyron.png")
car_image_2 = pygame.image.load("Dodge_Viper_GTS.png")
car_image_3 = pygame.image.load("Chevrolet_Corvette.png")
car_image_4 = pygame.image.load("Ferrari_458_Italia.png")
car_image_5 = pygame.image.load("Audi_R8Gt.png")
car_image_6 = pygame.image.load("Mclaren_F1.png")
car_image_7 = pygame.image.load("Pagani_Zonda_F.png")
car_image_8 = pygame.image.load(" Koenigsegg_CCX.png")
car_image_9 = pygame.image.load("Lotus_Elise.png")
car_image_10 = pygame.image.load("Porsche_911.png")
car_image_11 = pygame.image.load("Mercedes_Benz_SLS_AMG.png")
car_image_12= pygame.image.load("Aston_Martin_DB9.png")
car_image_13 = pygame.image.load("Lamborghini_Murcielago.png")
car_image_14 = pygame.image.load("Toyota_Supra.png")
car_adjus_1 = pygame.transform.scale(car_image_1, (carxsize, carysize))
car_adjus_2 = pygame.transform.scale(car_image_2, (carxsize, carysize))
car_adjus_3 = pygame.transform.scale(car_image_3, (carxsize, carysize))
car_adjus_4 = pygame.transform.scale(car_image_4, (carxsize, carysize))
car_adjus_5 = pygame.transform.scale(car_image_5, (carxsize, carysize))
car_adjus_6 = pygame.transform.scale(car_image_6, (carxsize, carysize))
car_adjus_7 = pygame.transform.scale(car_image_7, (carxsize, carysize))
car_adjus_8 = pygame.transform.scale(car_image_8, (carxsize, carysize))
car_adjus_9 = pygame.transform.scale(car_image_9, (carxsize, carysize))
car_adjus_10 = pygame.transform.scale(car_image_10, (carxsize, carysize))
car_adjus_11 = pygame.transform.scale(car_image_11, (carxsize, carysize))
car_adjus_12 = pygame.transform.scale(car_image_12, (carxsize, carysize))
car_adjus_13 = pygame.transform.scale(car_image_13, (carxsize, carysize))
car_adjus_14 = pygame.transform.scale(car_image_14, (carxsize, carysize))

car_adjus2_1 = pygame.transform.scale(car_image_1, (200, 100))
car_adjus2_2 = pygame.transform.scale(car_image_2, (200, 100))
car_adjus2_3 = pygame.transform.scale(car_image_3, (200, 100))
car_adjus2_4 = pygame.transform.scale(car_image_4, (200, 100))
car_adjus2_5 = pygame.transform.scale(car_image_5, (200, 100))
car_adjus2_6 = pygame.transform.scale(car_image_6, (200, 100))
car_adjus2_7 = pygame.transform.scale(car_image_7, (200, 100))
car_adjus2_8 = pygame.transform.scale(car_image_8, (200, 100))
car_adjus2_9 = pygame.transform.scale(car_image_9, (200, 100))
car_adjus2_10 = pygame.transform.scale(car_image_10, (200, 100))
car_adjus2_11 = pygame.transform.scale(car_image_11, (200, 100))
car_adjus2_12 = pygame.transform.scale(car_image_12, (200, 100))
car_adjus2_13 = pygame.transform.scale(car_image_13, (200, 100))
car_adjus2_14 = pygame.transform.scale(car_image_14, (200, 100))
cars_for_the_gift = car_adjus2_1


car_adjus = random.choice([

	car_adjus_1, car_adjus_2, car_adjus_3, car_adjus_4,
	car_adjus_5, car_adjus_6, car_adjus_7, car_adjus_8,
	car_adjus_9, car_adjus_10, car_adjus_11, car_adjus_12,
	car_adjus_13, car_adjus_14

	])


splash_sound = pygame.mixer.Sound("splash.mp3")

menu_song = pygame.mixer.Sound('menu_song.mp3')
out = pygame.mixer.Sound('out.mp3')
out_crash = pygame.mixer.Sound('out_level_3.mp3')
scream = pygame.mixer.Sound('scream.mp3')
click = pygame.mixer.Sound('click.mp3')
level_up = pygame.mixer.Sound('level_up.mp3')
cheats_sound = pygame.mixer.Sound('cheats.mp3')
player_is_cheater = pygame.mixer.Sound("You_are_a_cheater.mp3")
snow_intro = pygame.mixer.Sound("snow_intro_txt.mp3")
ice_intro = pygame.mixer.Sound("ice_intro_txt.mp3")
snowball_car_hit = pygame.mixer.Sound("snowball_car_hit.mp3")
snowball_hit = pygame.mixer.Sound("snowball_hit.mp3")
snowball_throw = pygame.mixer.Sound("snowball_throw.mp3")
health_down = pygame.mixer.Sound("health_down.mp3")


Level_1_sound = pygame.mixer.Sound('Level_1.wav')
Level_1_song = pygame.mixer.Sound('Level_1_song.mp3')
Level_1_voice= pygame.mixer.Sound('Level_1_completed.mp3')

Level_2_sound = pygame.mixer.Sound('Level_2.wav')
Level_2_song = pygame.mixer.Sound('Level_2_song.mp3')
Level_2_voice= pygame.mixer.Sound('Level_2_completed.mp3')

Level_3_sound = pygame.mixer.Sound('Level_3.wav')
Level_3_song = pygame.mixer.Sound('Level_3_song.mp3')
Level_3_voice= pygame.mixer.Sound('Level_3_completed.mp3')

Level_4_sound = pygame.mixer.Sound('Level_4.wav')

Level_5_sound = pygame.mixer.Sound('Level_5.wav')

Final_speech = pygame.mixer.Sound('Final_speech.mp3')
win_song = pygame.mixer.Sound('wiin.mp3')
difficulty_speech = pygame.mixer.Sound('difficulty_speech.mp3')
difficulty_speech2 = pygame.mixer.Sound('difficulty_speech2.mp3')
speechf = 0

def reset_game_state():

	global car_x, car_y, angle, level_map, death, elapsed_time, level_selected
	global is_selector_active, level_completed, cheat, velocity_x, velocity_y, cheater, cheater_rect
	global frist_time_touching_snow, sign, sign_introduction, sound_first_time, sound_first_time2
	global no_cross_sign_adjus, sign_rect, first_time_touching_ice, ice_count, snow_count, snowball_hit_number
	global current_health_length, health_length, first_time_difficulty, dk_how_2_call_this_variable
	global car_chosen, car_adjus, snowballs, snowball

	# Reset car position and physics
	car.x = car_init_x
	car.y = car_init_y
	car_x = car_init_x
	car_y = car_init_y
	angle = 0
	velocity_x = 0
	velocity_y = 0
    
	# Reset game state
	pygame.mixer.stop()
	pygame.mixer.init()
	menu_song.play(loops=-1)
	level_map = 1
	death = 0

	start_time = None
	starting_timer = True
	elapsed_time = 0
	sign_time = 0
	frist_time_touching_snow = True
	first_time_touching_ice = True
	sound_first_time = True
	sound_first_time2 = True
	snow_count = 0
	ice_count = 0
	snowball_hit_number = 0
	current_health_length = health_length
	first_time_difficulty = True
	dk_how_2_call_this_variable = 0
	
	# Reset flags
	level_selected = False
	is_selector_active = False
	level_completed = False
	cheat = False
	cheater = False


	if not car_chosen:
		car_adjus = random.choice([

			car_adjus_1, car_adjus_2, car_adjus_3, car_adjus_4,
			car_adjus_5, car_adjus_6, car_adjus_7, car_adjus_8,
			car_adjus_9, car_adjus_10, car_adjus_11, car_adjus_12,
			car_adjus_13, car_adjus_14

			])

	for snowball in snowballs:
		snowballs.remove(snowball)
	
def show_level_completed():

	global level_map, level_selected, speed_run, end_of_levels
	global text_level_hight_end_of_levels, font_size3, font3, percentage_of_difficulty
	global first_time_difficulty, dk_how_2_call_this_variable, milliseconds, minutes, seconds
	global deaths

	

	pygame.mixer.stop()
	pygame.mixer.init()

	win_song.play()

	if end_of_levels:
		Final_speech.play()
	elif level_map == 2:
		Level_1_voice.play()
	elif level_map == 3:
		Level_2_voice.play()
	elif level_map == 4:
		Level_3_voice.play()

	cheater_count = 0
	cheater_2_count = 0

    
	level_down = level_map - 1

	if not level_selected:

		level_down = 4


	milliseconds = round(float(f'{milliseconds:02.0f}'))
	deaths = death

	times = load_times()
	if not cheater and right_difficulty:
		save_time(level_down, minutes, seconds, milliseconds, death)
	
	times = load_times()



	if not speed_run:
		while True:
			key = pygame.key.get_pressed()


			screen.fill(Black)
			

			if end_of_levels:
				screen.blit(game_completed_adjus, screen_rect)
				text_level_hight_end_of_levels = 320
				
			elif level_map == 2:
				screen.blit(level_1_completed_adjus, screen_rect)
				text_level_hight_end_of_levels = 375
				

			elif level_map == 3:
				screen.blit(level_2_completed_adjus, screen_rect)
				text_level_hight_end_of_levels = 375
				

			elif level_map == 4:
				screen.blit(level_3_completed_adjus, screen_rect)
				text_level_hight_end_of_levels = 375
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if key[pygame.K_ESCAPE]:
					pygame.quit()
					sys.exit()

				if key[pygame.K_b]:
					click.play()
					end_of_levels = False
					reset_game_state()
					menu()
					return  

				if event.type == pygame.KEYDOWN:
					if event.key == 1073742094:
						click.play()
						end_of_levels = False
						reset_game_state()
						menu()
						return

				elif event.type == pygame.MOUSEBUTTONDOWN:
					if back_arrow_but.collidepoint(event.pos):
						click.play()
						end_of_levels = False
						reset_game_state()
						menu()
						return  # Exit the function after returning to menu

			#TEXTO DE TIEMPO
			if level_selected:
				time_txt = font3.render(str(f"{final_time_string}"), True, White)
			else:
				time_txt = font3.render(str(f"{final_time_string}, {death} deaths"), True, White)

			time_txt_rect = time_txt.get_rect(center=(600, text_level_hight_end_of_levels))
			screen.blit(time_txt, time_txt_rect)

			if final_time_string_long:
				font_size3 = 80
				font3 = pygame.font.Font(None, font_size3)
			else:
				font_size3 = 95
				font3 = pygame.font.Font(None, font_size3)

			if cheater:

				if cheater_2_count == 350:
					player_is_cheater.play(loops = -1)
				else:
					cheater_2_count +=1

				if cheater_count >= 25:
					screen.blit(cheater_adjus, cheater_rect1)
					screen.blit(cheater_adjus, cheater_rect2)
					screen.blit(cheater_adjus, cheater_rect3)
					screen.blit(cheater_adjus, cheater_rect4)
					screen.blit(cheater_adjus, cheater_rect5)
					screen.blit(cheater_adjus, cheater_rect6)
					screen.blit(cheater_adjus, cheater_rect7)
					screen.blit(cheater_adjus, cheater_rect8)
					screen.blit(cheater_adjus, cheater_rect9)
					screen.blit(cheater_adjus, cheater_rect10)
					screen.blit(cheater_adjus, cheater_rect11)
					screen.blit(cheater_adjus, cheater_rect12)

					screen.blit(cheater_vert_adjus, cheater_rect13)
					screen.blit(cheater_vert_adjus, cheater_rect14)
					screen.blit(cheater_vert_adjus, cheater_rect15)
					screen.blit(cheater_vert_adjus, cheater_rect16)
					screen.blit(cheater_vert_adjus, cheater_rect17)
					screen.blit(cheater_vert_adjus, cheater_rect18)
					screen.blit(cheater_vert_adjus, cheater_rect19)
					screen.blit(cheater_vert_adjus, cheater_rect20)

					cheater_count += 1

					if cheater_count >= 40:
						cheater_count = 0
						
				else:
					cheater_count += 1

			right_difficulty_rect = pygame.Rect(30, 400, 350, 150)
			white_rect = pygame.Rect(40, 410, 330, 100)

			if not right_difficulty:
				pygame.draw.rect(screen, White, white_rect)
				screen.blit(sad_adjus, right_difficulty_rect)

			if not cheater and not right_difficulty:

				if first_time_difficulty and dk_how_2_call_this_variable >= 350:
					difficulty_speech2.play()
					first_time_difficulty = False
				else:
					dk_how_2_call_this_variable += 1

			level_down = level_map - 1


			pb_rect = pygame.Rect(400, 412, 400, 175)
			screen.blit(pb_adjus, pb_rect)

			screen.blit(back_arrow_adjus, back_arrow_but)
			pygame.display.update()

def update_car_movement_slow(key):

	global car_x, car_y, angle, speed, velocity_x, velocity_y

	ICE_FRICTION = 0.02
	ICE_ACCELERATION = 3.5
	ICE_ROTATION_SPEED = 3.0
	ICE_MAX_SPEED = 1.75

	# Steering
	if key[pygame.K_d] or key[pygame.K_RIGHT]:
		angle -= ICE_ROTATION_SPEED
	if key[pygame.K_a] or key[pygame.K_LEFT]:
		angle += ICE_ROTATION_SPEED

	# Convert angle to radians
	radians = math.radians(angle)

	# Calculate direction vector
	dir_x = math.cos(radians)
	dir_y = -math.sin(radians)

	# Apply acceleration in the direction the car is facing
	if key[pygame.K_w] or key[pygame.K_UP]:
		velocity_x += dir_x * ICE_ACCELERATION
		velocity_y += dir_y * ICE_ACCELERATION
	elif key[pygame.K_s] or key[pygame.K_DOWN]:
		velocity_x -= dir_x * ICE_ACCELERATION
		velocity_y -= dir_y * ICE_ACCELERATION

    # Apply ice friction
	velocity_x *= (1 - ICE_FRICTION)
	velocity_y *= (1 - ICE_FRICTION)

	# Limit maximum speed
	current_speed = math.sqrt(velocity_x ** 2 + velocity_y ** 2)
	if current_speed > ICE_MAX_SPEED:
		speed_factor = ICE_MAX_SPEED / current_speed
		velocity_x *= speed_factor
		velocity_y *= speed_factor

	# Update position based on velocity
	car_x += velocity_x
	car_y += velocity_y

	return car_x, car_y, angle

def update_car_movement_fast(key):

	global car_x, car_y, angle, speed, velocity_x, velocity_y

	ICE_FRICTION = 0.04
	ICE_ACCELERATION = 5 
	ICE_ROTATION_SPEED = 4.5  
	ICE_MAX_SPEED = 3.0

	# Steering
	if key[pygame.K_d] or key[pygame.K_RIGHT]:
		angle -= ICE_ROTATION_SPEED
	if key[pygame.K_a] or key[pygame.K_LEFT]:
		angle += ICE_ROTATION_SPEED

	# Convert angle to radians
	radians = math.radians(angle)

	# Calculate direction vector
	dir_x = math.cos(radians)
	dir_y = -math.sin(radians)

	# Apply acceleration in the direction the car is facing
	if key[pygame.K_w] or key[pygame.K_UP]:
		velocity_x += dir_x * ICE_ACCELERATION
		velocity_y += dir_y * ICE_ACCELERATION
	elif key[pygame.K_s] or key[pygame.K_DOWN]:
		velocity_x -= dir_x * ICE_ACCELERATION
		velocity_y -= dir_y * ICE_ACCELERATION

    # Apply ice friction
	velocity_x *= (1 - ICE_FRICTION)
	velocity_y *= (1 - ICE_FRICTION)

	# Limit maximum speed
	current_speed = math.sqrt(velocity_x ** 2 + velocity_y ** 2)
	if current_speed > ICE_MAX_SPEED:
		speed_factor = ICE_MAX_SPEED / current_speed
		velocity_x *= speed_factor
		velocity_y *= speed_factor

	# Update position based on velocity
	car_x += velocity_x
	car_y += velocity_y

	return car_x, car_y, angle

def update_car_movement_no_friction(key):

	global car_x, car_y, angle, speed, velocity_x, velocity_y

	ICE_FRICTION = 0.8
	ICE_ACCELERATION = 7.5
	ICE_ROTATION_SPEED = 4.5  
	ICE_MAX_SPEED = 7.5

	# Steering
	if key[pygame.K_d] or key[pygame.K_RIGHT]:
		angle -= ICE_ROTATION_SPEED
	if key[pygame.K_a] or key[pygame.K_LEFT]:
		angle += ICE_ROTATION_SPEED

	# Convert angle to radians
	radians = math.radians(angle)

	# Calculate direction vector
	dir_x = math.cos(radians)
	dir_y = -math.sin(radians)

	# Apply acceleration in the direction the car is facing
	if key[pygame.K_w] or key[pygame.K_UP]:
		velocity_x += dir_x * ICE_ACCELERATION
		velocity_y += dir_y * ICE_ACCELERATION
	elif key[pygame.K_s] or key[pygame.K_DOWN]:
		velocity_x -= dir_x * ICE_ACCELERATION
		velocity_y -= dir_y * ICE_ACCELERATION


    # Apply ice friction
	velocity_x *= (1 - ICE_FRICTION)
	velocity_y *= (1 - ICE_FRICTION)

	# Limit maximum speed
	current_speed = math.sqrt(velocity_x ** 2 + velocity_y ** 2)
	if current_speed > ICE_MAX_SPEED:
		speed_factor = ICE_MAX_SPEED / current_speed
		velocity_x *= speed_factor
		velocity_y *= speed_factor

	# Update position based on velocity
	car_x += velocity_x
	car_y += velocity_y

	return car_x, car_y, angle

#pantalla principal
screen = pygame.display.set_mode((screen_width, screen_length))

# Inicializamos el reloj para los FPS
clock = pygame.time.Clock()

def leaderboard_menu():

	global mouse_pressed, key

	mouse_pressed = False
	is_leaderboard_active = True


	while is_leaderboard_active:	

		key = pygame.key.get_pressed()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_arrow_but.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					back_action = True
					is_leaderboard_active = False
			if event.type == pygame.KEYDOWN:
				if event.key == 1073742094:	
					click.play()
					back_action = True
					is_leaderboard_active = False


			if key[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()
				
			if key[pygame.K_b]:
				click.play()
				back_action = True
				is_leaderboard_active = False

			
		times = load_times()
		creator_time_1 = (f"30.5 secs")
		creator_time_2 = (f"57.2 secs")
		creator_time_3 = (f"43.23 secs")
		creator_time_4 = (f"2m 40.5 secs and 3 deaths")


		if 1 in times:  
			minutes, seconds, milliseconds = times[1]
			if minutes == 0:
				player_time_1 = (f"{seconds}.{milliseconds} secs")
			else:
				player_time_1 = (f"{minutes}m {seconds}.{milliseconds} secs")

			player_time_1_seconds = minutes * 60 + seconds + milliseconds / 100

			if player_time_1_seconds > 30.5:

				player_time_1_color = Red
				creator_time_1_color = Green

			else:

				player_time_1_color = Green
				creator_time_1_color = Red

		else:
			player_time_1 = ("---")
			player_time_1_color = Red
			creator_time_1_color = Green


		if 2 in times:  
			minutes, seconds, milliseconds = times[2]
			if minutes == 0:
				player_time_2 = (f"{seconds}.{milliseconds} secs")
			else:
				player_time_2 = (f"{minutes}m {seconds}.{milliseconds} secs")

			player_time_2_seconds = minutes * 60 + seconds + milliseconds / 100

			if player_time_2_seconds > 57.2:

				player_time_2_color = Red
				creator_time_2_color = Green

			else:

				player_time_2_color = Green
				creator_time_2_color = Red

		else:
			player_time_2 = ("---")
			player_time_2_color = Red
			creator_time_2_color = Green


		if 3 in times:  
			minutes, seconds, milliseconds = times[3]

			if minutes == 0:
				player_time_3 = (f"{seconds}.{milliseconds} secs")
			else:
				player_time_3 = (f"{minutes}m {seconds}.{milliseconds} secs")

			player_time_3_seconds = minutes * 60 + seconds + milliseconds / 100

			if player_time_3_seconds > 43.23:

				player_time_3_color = Red
				creator_time_3_color = Green

			else:

				player_time_3_color = Green
				creator_time_3_color = Red

		else:
			player_time_3 = ("---")
			player_time_3_color = Red
			creator_time_3_color = Green

	
		if 4 in times:  
			minutes, seconds, milliseconds, deaths = times[4]

			if minutes == 0:
				player_time_4 = (f"{seconds}.{milliseconds} secs and {death} deaths")
			else:
				player_time_4 = (f"{minutes}m {seconds}.{milliseconds} secs and {death} deaths")

			player_time_4_seconds = minutes * 60 + seconds + milliseconds / 100 + deaths * 5

			if player_time_4_seconds > 170.5:

				player_time_4_color = Red
				creator_time_4_color = Green

			else:

				player_time_4_color = Green
				creator_time_4_color = Red


		else:
			player_time_4 = ("---")
			player_time_4_color = Red
			creator_time_4_color = Green


		player_time_1_txt = font5.render(str(f"{player_time_1}"), True, player_time_1_color)
		player_time_1_txt_rect = player_time_1_txt.get_rect(center=(600, 215))
		player_time_2_txt = font5.render(str(f"{player_time_2}"), True, player_time_2_color)
		player_time_2_txt_rect = player_time_2_txt.get_rect(center=(600, 290))
		player_time_3_txt = font5.render(str(f"{player_time_3}"), True, player_time_3_color)
		player_time_3_txt_rect = player_time_3_txt.get_rect(center=(600, 360))
		player_time_4_txt = font4.render(str(f"{player_time_4}"), True, player_time_4_color)
		player_time_4_txt_rect = player_time_4_txt.get_rect(center=(600, 135))


		x = 970
		creator_time_1_txt = font5.render(str(f"{creator_time_1}"), True, creator_time_1_color)
		creator_time_1_txt_rect = creator_time_1_txt.get_rect(center=(x, 215))
		creator_time_2_txt = font5.render(str(f"{creator_time_2}"), True, creator_time_2_color)
		creator_time_2_txt_rect = creator_time_2_txt.get_rect(center=(x, 290))
		creator_time_3_txt = font5.render(str(f"{creator_time_3}"), True, creator_time_3_color)
		creator_time_3_txt_rect = creator_time_3_txt.get_rect(center=(x, 360))
		creator_time_4_txt = font4.render(str(f"{creator_time_4}"), True, creator_time_4_color)
		creator_time_4_txt_rect = creator_time_4_txt.get_rect(center=(x, 135))
		

		screen.fill(Black)
		screen.blit(back_arrow_adjus, back_arrow_but)
		screen.blit(leaderboard_background, screen_rect)
		screen.blit(back_arrow_adjus, back_arrow_but)
		screen.blit(player_time_1_txt, player_time_1_txt_rect)
		screen.blit(player_time_2_txt, player_time_2_txt_rect)
		screen.blit(player_time_3_txt, player_time_3_txt_rect)
		screen.blit(player_time_4_txt, player_time_4_txt_rect)
		screen.blit(creator_time_1_txt, creator_time_1_txt_rect)
		screen.blit(creator_time_2_txt, creator_time_2_txt_rect)
		screen.blit(creator_time_3_txt, creator_time_3_txt_rect)
		screen.blit(creator_time_4_txt, creator_time_4_txt_rect)
		pygame.display.update()

def info_menu():

	global mouse_pressed

	mouse_pressed = False
	is_info_active = True

	while is_info_active:

		key = pygame.key.get_pressed()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if key[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

			if key[pygame.K_b]:
				click.play()
				back_action = True
				is_info_active = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_arrow_but.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					back_action = True
					is_info_active = False

			if event.type == pygame.MOUSEBUTTONUP:
				mouse_pressed = False

			if event.type == pygame.KEYDOWN:
				if event.key == 1073742094:
					click.play()
					back_action = True
					is_info_active = False


		screen.fill(Black)
		screen.blit(info_menu_background, screen_rect)
		pygame.display.update()

def skins_menu():

	global mouse_pressed, car_adjus, car_chosen, tick_box, tickx, ticky, cars_for_the_gift 

	mouse_pressed = False
	is_skins_active = True

	while is_skins_active:

		key = pygame.key.get_pressed()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if key[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

			if key[pygame.K_b]:
				click.play()
				back_action = True
				is_skins_active = False

			if event.type == pygame.KEYDOWN:
				if event.key == 1073742094:
					click.play()
					back_action = True
					is_skins_active = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_arrow_but.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					back_action = True
					is_skins_active = False
				if car_but_1.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_1
					cars_for_the_gift = car_adjus2_1
					car_chosen = True
					tickx = car_but_1.centerx
					ticky = car_but_1.centery
				if car_but_2.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_2
					cars_for_the_gift = car_adjus2_2
					car_chosen = True
					tickx = car_but_2.centerx
					ticky = car_but_2.centery
				if car_but_3.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_3
					cars_for_the_gift = car_adjus2_3
					car_chosen = True
					tickx = car_but_3.centerx
					ticky = car_but_3.centery
				if car_but_4.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_4
					cars_for_the_gift = car_adjus2_4
					car_chosen = True
					tickx = car_but_4.centerx
					ticky = car_but_4.centery
				if car_but_5.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_5
					cars_for_the_gift = car_adjus2_5
					car_chosen = True
					tickx = car_but_5.centerx
					ticky = car_but_5.centery
				if car_but_6.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_6
					cars_for_the_gift = car_adjus2_6
					car_chosen = True
					tickx = car_but_6.centerx
					ticky = car_but_6.centery
				if car_but_7.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_7
					cars_for_the__gift = car_adjus2_7
					car_chosen = True
					tickx = car_but_7.centerx
					ticky = car_but_7.centery
				if car_but_8.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_8
					cars_for_the_gift = car_adjus2_8
					car_chosen = True
					tickx = car_but_8.centerx
					ticky = car_but_8.centery
				if car_but_9.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_9
					cars_for_the_gift = car_adjus2_9
					car_chosen = True
					tickx = car_but_9.centerx
					ticky = car_but_9.centery
				if car_but_10.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_10
					cars_for_the_gift = car_adjus2_10
					car_chosen = True
					tickx = car_but_10.centerx
					ticky = car_but_10.centery
				if car_but_11.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_11
					cars_for_the_gift = car_adjus2_11
					car_chosen = True
					tickx = car_but_11.centerx
					ticky = car_but_11.centery
				if car_but_12.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_12
					cars_for_the_gift = car_adjus2_12
					car_chosen = True
					tickx = car_but_12.centerx
					ticky = car_but_12.centery
				if car_but_13.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_13
					cars_for_the_gift = car_adjus2_13
					car_chosen = True
					tickx = car_but_13.centerx
					ticky = car_but_13.centery
				if car_but_14.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					car_adjus = car_adjus_14
					cars_for_the_gift = car_adjus2_14
					car_chosen = True
					tickx = car_but_14.centerx
					ticky = car_but_14.centery
					

					
					
					

			if event.type == pygame.MOUSEBUTTONUP:
				mouse_pressed = False



		screen.fill(Black)
		screen.blit(skins_menu_background, screen_rect)

		if car_chosen:
			tick_box = pygame.Rect(1200, 600, 50, 50)
			tick_box.centerx = tickx
			tick_box.centery = ticky
		
		screen.blit(tick_adjus2, tick_box)
		screen.blit(back_arrow_adjus, back_arrow_but)
		

		pygame.display.update()

def difficulty_menu():

	global mouse_pressed, ballx, dragging, inflation_value, inflation_min, speechf, right_difficulty
	mouse_pressed = False
	is_difficulty_active = True

	while is_difficulty_active:

		key = pygame.key.get_pressed()
		ball_rect = pygame.Rect(ballx - 25, 170, 60, 60)


		if speechf >= 40:  
			difficulty_speech.play()  
			speechf = -1 
		elif speechf >= 0: 
			speechf += 1 


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if key[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()
			if key[pygame.K_b]:

				click.play()
				back_action = True
				is_difficulty_active = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_arrow_but.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					back_action = True
					is_difficulty_active = False

			if event.type == pygame.KEYDOWN:
				if event.key == 1073742094:	

					click.play()
					back_action = True
					is_difficulty_active = False

			if event.type == pygame.MOUSEBUTTONUP:
				mouse_pressed = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:

					if ballx >= 30:
						ballx -= 20

					else:
						ballx = 30

				
				if event.key == pygame.K_RIGHT:
					
					if ballx <= 1170:
						ballx += 25

					else:
						ballx = 1170

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = event.pos  # Get the mouse position
				ball_radius = 30  # Radius of the ball
					
				if ball_rect.collidepoint(mouse_x, mouse_y): 
					ballx = mouse_x

					if ballx > 1170:
						ballx = 1170

					elif ballx < 30:
						ballx = 30

					dragging = True

			if event.type == pygame.MOUSEMOTION and dragging:
				mouse_x, mouse_y = event.pos  
				ballx = mouse_x 

				if ballx > 1170:
						ballx = 1170

				elif ballx < 30:
					ballx = 30

				
			if event.type == pygame.MOUSEBUTTONUP:
				dragging = False
				 
		percentage_of_difficulty_string = f"{round((ballx / 1140) * 100 - 2.631578947368421)}%"
		percentage_of_difficulty= round((ballx / 1140) * 100 - 2.631578947368421)
		percentage_of_difficulty_adjus = 100 - percentage_of_difficulty
		inflation_chosen = 25 * (percentage_of_difficulty_adjus / 100)
		
		inflation_value = inflation_min + inflation_chosen
		percentage = font4.render(str(percentage_of_difficulty_string), True, Black)
		percentage_rect = percentage.get_rect(center=(ballx, 195))
		

		black_bar = pygame.Rect(ballx, 185, 1165 - ballx, 24 )
		screen.fill(Black)
		screen.blit(difficulty_menu_background, screen_rect)
		screen.blit(back_arrow_adjus, back_arrow_but)
		screen.blit(color_bar_adjus, color_bar_rect)
		pygame.draw.rect(screen, Black, black_bar)
		pygame.draw.circle(screen, White, (ballx, 195), 30)
		screen.blit(percentage, percentage_rect)

		car_repre_inflate_value = (425 * inflation_value) / 75
		
		
		car_repre = pygame.Rect(705, 400, 425, 170)
		car_repre.inflate_ip(-car_repre_inflate_value / 2, -car_repre_inflate_value / 2)		
		pygame.draw.rect(screen, Green, car_repre)

		tick_box = pygame.Rect(305, 290, 100, 100)
		if percentage_of_difficulty >= 50:
			screen.blit(tick_adjus, tick_box)
			right_difficulty = True
		else:
			right_difficulty = False


		pygame.display.update()

def level_selector_menu():
	global mouse_pressed, level_selected, back_action, is_selector_active, running , level_map,  speed_run, start_time
	mouse_pressed = False
	is_selector_active = True
	while is_selector_active:

		speed_run = False
		key = pygame.key.get_pressed()

		#LIMPIAMOS PANTALLA
		screen.fill(Black)

		#para poder salir
		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN:
				if event.key == 1073742094:
					click.play()
					back_action = True
					is_selector_active = False
					
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if key[pygame.K_ESCAPE]:
				pygame.quit()
				sys.exit()

			if key[pygame.K_b]:
				click.play()
				back_action = True
				is_selector_active = False
				start_time = pygame.time.get_ticks()

			starting_timer = True
			if key[pygame.K_1]:
				pygame.mixer.stop()
				pygame.mixer.init()
				
				level_map = 1
				Level_1_sound.play()
				Level_1_song.play(loops = -1)
					
				click.play()
				level_selected = True
				running = False
				start_time = pygame.time.get_ticks()
				is_selector_active = False


			if key[pygame.K_2]:
				pygame.mixer.stop()
				pygame.mixer.init()
				
				level_map = 2
				Level_2_sound.play()
				Level_2_song.play(loops = -1)

				click.play()
				level_selected = True
				running = False
				start_time = pygame.time.get_ticks()
				is_selector_active = False

			if key[pygame.K_3]:
				pygame.mixer.stop()
				pygame.mixer.init()
				
				level_map = 3
				sign_introduction = True
				Level_3_sound.play()
				Level_3_song.play(loops = -1)
					
				click.play()
				level_selected = True
				running = False
				start_time = pygame.time.get_ticks()
				is_selector_active = False

			#DETECTA EL MOUSE
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_arrow_but.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					back_action = True
					is_selector_active = False
					start_time = pygame.time.get_ticks()
				
				# BOTONES DE NIVELES 
				starting_timer = True
				if level_1_but.collidepoint(event.pos) and not mouse_pressed:
					pygame.mixer.stop()
					pygame.mixer.init()
					mouse_pressed = True
					level_map = 1
					Level_1_sound.play()
					Level_1_song.play(loops = -1)
					
					click.play()
					level_selected = True
					running = False
					start_time = pygame.time.get_ticks()
					is_selector_active = False


				if level_2_but.collidepoint(event.pos) and not mouse_pressed:
					pygame.mixer.stop()
					pygame.mixer.init()
					mouse_pressed = True
					level_map = 2
					Level_2_sound.play()
					Level_2_song.play(loops = -1)

					click.play()
					level_selected = True
					running = False
					start_time = pygame.time.get_ticks()
					is_selector_active = False

				if level_3_but.collidepoint(event.pos) and not mouse_pressed:
					pygame.mixer.stop()
					pygame.mixer.init()
					mouse_pressed = True
					level_map = 3
					sign_introduction = True
					Level_3_sound.play()
					Level_3_song.play(loops = -1)
					
					click.play()
					level_selected = True
					running = False
					start_time = pygame.time.get_ticks()
					is_selector_active = False

				if back_arrow_but.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					back_action = True
					is_selector_active = False
					start_time = pygame.time.get_ticks()

		#LOGICA PARA LOS CLICKS
			if event.type == pygame.MOUSEBUTTONUP:
				mouse_pressed = False

		# DIBUJAMOS FONDO
		screen.blit(Level_selector_adjus, screen_rect)
		screen.blit(back_arrow_adjus, back_arrow_but)
		# ACTUALIZAMOS
		pygame.display.update()



#INICIAMOS CANCION
menu_song.play(loops = -1)
def menu():
	global sound, level_selected, level_map,  speed_run, start_time, cars_for_the__gift
	mouse_pressed = False
	running = True 
	back_action = False
	sound_key = True
	gift = 0

	while running:


		#TIEMPO
		current_time = pygame.time.get_ticks()

		#SHOERTCUT DE INPUTS
		key = pygame.key.get_pressed()

		#LIMPIAMOS PANTALLA
		screen.fill(Black)
		
		#para poder salir
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:  
					sound = not sound


				if event.key == pygame.K_l: 
					click.play()		
					level_selector_menu()					
					if level_selected:
						running = False
						break
				if event.key == pygame.K_d: 
					click.play()				
					difficulty_menu()
				if event.key == pygame.K_k: 
					click.play()				
					skins_menu()
				if event.key == pygame.K_i: 
					click.play()				
					info_menu()
				if event.key == pygame.K_t: 
					click.play()				
					leaderboard_menu()

				if event.key == pygame.K_r:
					click.play()
					speed_run = True
					pygame.mixer.stop()
					pygame.mixer.init()
					starting_timer = True
					start_time = pygame.time.get_ticks()

					if level_map == 1:
						Level_1_sound.play()
						Level_1_song.play(loops = -1)
						
					elif level_map == 2:
						Level_2_sound.play()
						Level_2_song.play(loops = -1)
					elif level_map == 3:
						Level_3_sound.play()
						
					elif level_map == 4:
						Level_4_sound.play()
					elif level_map == 5:
						Level_5_sound.play()

					level_selected = False
					back_action = False
					is_selector_active = False
					running = False
					break

				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
					
				#DETECTA EL MOUSE
			if event.type == pygame.MOUSEBUTTONDOWN:
			
				#SOUND BUTTON
				if sound_but.collidepoint(event.pos) and not mouse_pressed:
					sound = not sound
					mouse_pressed = True
					click.play()
				
				#SPEEDRUN BUTTON
				elif speedrun.collidepoint(event.pos) and not mouse_pressed:
					mouse_pressed = True
					click.play()
					speed_run = True
					pygame.mixer.stop()
					pygame.mixer.init()
					starting_timer = True
					start_time = pygame.time.get_ticks()

					if level_map == 1:
						Level_1_sound.play()
						Level_1_song.play(loops = -1)
						
					elif level_map == 2:
						Level_2_sound.play()
						Level_2_song.play(loops = -1)
					elif level_map == 3:
						Level_3_sound.play()
						
					elif level_map == 4:
						Level_4_sound.play()
					elif level_map == 5:
						Level_5_sound.play()

					level_selected = False
					back_action = False
					is_selector_active = False
					running = False
					break

					

				#LEVELS BUTTON
				elif levels_but.collidepoint(event.pos) and not mouse_pressed:
					click.play()
					mouse_pressed = True
					level_selector_menu()
					
					if level_selected:
						running = False
						break
					
				elif difficulty_but.collidepoint(event.pos) and not mouse_pressed:
					click.play()
					mouse_pressed = True
					difficulty_menu()
				elif skins_but.collidepoint(event.pos) and not mouse_pressed:
					click.play()
					mouse_pressed = True
					skins_menu()
				elif info_but.collidepoint(event.pos) and not mouse_pressed:
					click.play()
					mouse_pressed = True
					info_menu()
				elif leaderboard_but.collidepoint(event.pos) and not mouse_pressed:
					click.play()
					mouse_pressed = True
					leaderboard_menu()
					


			#LOGICA PARA LOS CLICKS
			if event.type == pygame.MOUSEBUTTONUP:
				mouse_pressed = False

		#OPCION DE SONIDO
		if sound:
			screen.blit( menu_adjus_on, screen_rect)
			splash_sound.set_volume(0.5)
			click.set_volume(1.0)
			level_up.set_volume(0.2)
			out.set_volume(1.0)
			menu_song.set_volume(0.12)
			scream.set_volume(1.0)
			cheats_sound.set_volume(1.0)
			win_song.set_volume(0.5)
			Final_speech.set_volume(1.0)
			player_is_cheater.set_volume(0.5)
			snow_intro.set_volume(2.0)
			ice_intro.set_volume(1.0)
			snowball_throw.set_volume(1.0)
			snowball_hit.set_volume(1.0)
			snowball_car_hit.set_volume(0.5)
			health_down.set_volume(0.2)
			difficulty_speech.set_volume(1.0)
			difficulty_speech2.set_volume(1.0)

			Level_1_sound.set_volume(1.0)
			Level_1_song.set_volume(0.3)
			Level_1_voice.set_volume(1.0)


			Level_2_sound.set_volume(1.0)
			Level_2_song.set_volume(0.1)
			Level_2_voice.set_volume(1.0)


			Level_3_sound.set_volume(1.0)
			Level_3_song.set_volume(0.3)
			Level_3_voice.set_volume(1.0)

			Level_4_sound.set_volume(1.0)
			Level_5_sound.set_volume(1.0)
			out_crash.set_volume(1.0)

		else:

			screen.blit(menu_adjus_off, screen_rect)
			splash_sound.set_volume(0.0)
			click.set_volume(0.0)
			level_up.set_volume(0.0)
			menu_song.set_volume(0.0)
			Level_2_song.set_volume(0.0)
			out.set_volume(0.0)
			scream.set_volume(0.0)
			cheats_sound.set_volume(0.0)
			win_song.set_volume(0.0)
			Final_speech.set_volume(0.0)
			player_is_cheater.set_volume(0.0)
			snow_intro.set_volume(0.0)
			ice_intro.set_volume(0.0)
			snowball_throw.set_volume(0.0)
			snowball_hit.set_volume(0.0)
			snowball_car_hit.set_volume(0.0)
			health_down.set_volume(0.0)
			difficulty_speech.set_volume(0.0)
			difficulty_speech2.set_volume(0.0)

			Level_1_sound.set_volume(0.0)
			Level_1_song.set_volume(0.0)
			Level_1_voice.set_volume(0.0)

			Level_2_sound.set_volume(0.0)
			Level_2_song.set_volume(0.0)
			Level_2_voice.set_volume(0.0)

			Level_3_sound.set_volume(0.0)
			Level_3_song.set_volume(0.0)
			Level_3_voice.set_volume(0.0)

			Level_4_sound.set_volume(0.0)
			Level_5_sound.set_volume(0.0)
			out_crash.set_volume(0.0)

		
		if car_chosen:
			screen.blit(cars_for_the_gift, car_gift)

		else:

			if gift == 0:
				cars_for_gift = random.choice([

					car_adjus2_1, car_adjus2_2, car_adjus2_3, car_adjus2_4,
					car_adjus2_5, car_adjus2_6, car_adjus2_7, car_adjus2_8,
					car_adjus2_9, car_adjus2_10, car_adjus2_11, car_adjus2_12,
					car_adjus2_13, car_adjus2_14

					]) 

				gift += 1

			elif gift == 20:

				gift = 0

			else:

				gift += 1

			screen.blit(cars_for_gift, car_gift)
	
		#ACTUALIZAMOS
		pygame.display.update()

if first_time:
	menu()
	first_time = False


#INICIAMOS CANCION Y PARAMOS LA DEL MENU
if level_selected:  
    menu_song.stop()
   
elif back_action:
    menu()  

menu_song.stop()
#BUCLE PRINCIPAL
run = True

while run:

	#SHORTCUT PARA LAS TECLAS
	key = pygame.key.get_pressed()

	if not mouse_visibility:
		pygame.mouse.set_visible(False)

	else:
		pygame.mouse.set_visible(True)

	#TIMER
	if starting_timer:
		start_time = pygame.time.get_ticks()
		starting_timer = False

	#para poder salir y trampillas
	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			if event.key == 1073742094 or event.key == pygame.K_b :
				reset_game_state()
				menu()

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if key[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if back_arrow_but.collidepoint(event.pos):
				reset_game_state()
				menu()

		if event.type == pygame.KEYDOWN:
			if event.key == cheat_sequence[current_index]:  # Check if the key matches the current sequence
				current_index += 1
				if current_index == len(cheat_sequence):  # Full sequence entered
					cheater = True
					cheat = True

					cheats_sound.play()
					current_index = 0  # Reset sequence
			else:
				current_index = 0  # Reset on wrong key

	# Convert angle from degrees to radians for trig functions
	radians = math.radians(angle)


	if level_map == 3 and touching_ice:
		if car.x > 400:
			car_x, car_y, angle = update_car_movement_slow(key)
		else:

			car_x, car_y, angle = update_car_movement_fast(key)

		car.x = car_x
		car.y = car_y

	elif level_map == 3 and not touching_ice:

		car_x, car_y, angle = update_car_movement_no_friction(key)

		car.x = car_x
		car.y = car_y
	
	else:

		if level_map == 3:
			speed = 2
			rot_speed = 2.5
		else:
			speed = 4
			rot_speed = 4.5

		radians = math.radians(angle)
		
		car_x = car.x
		car_y = car.y

		if key[pygame.K_w] or key[pygame.K_UP]:
			# Move forward in the direction of the angle
			car.x += speed * math.cos(radians)
			car.y -= speed * math.sin(radians)

		if key[pygame.K_s] or key[pygame.K_DOWN]:
			# Move backward in the direction of the angle
			car.x -= speed * math.cos(radians)
			car.y += speed * math.sin(radians)  

		if key[pygame.K_d] or key[pygame.K_RIGHT] == True:
			angle -= rot_speed
		if key[pygame.K_a] or key[pygame.K_LEFT] == True:
			angle += rot_speed

	#para no salirsez
	if car.left < 0:
		car.left = 0

	if car.right > screen_width or cheat:
		car.x = car_init_x
		car.y = car_init_y
		car_x = car_init_x
		car_y = car_init_y
		angle = 0
		level_map += 1
		level_up.play()
		cheat = False

		if cheat:
			pass
		elif level_selected == True and speed_run == False :
			show_level_completed()

		#SONIDITO CUANDO CAMBIAS DE NIVEL
		if level_map == 2:
			Level_2_sound.play()
			Level_2_song.play(loops = -1)
			Level_1_song.stop()
		elif level_map == 3:
			Level_3_sound.play()
			Level_3_song.play(loops = -1)
			Level_2_song.stop()
			sign_introduction = True
			splash = pygame.Rect(0, 0, 50, 50)
		elif level_map == 4:
			Level_4_sound.play()
		elif level_map == 5:
			Level_5_sound.play()


		if not car_chosen:
			car_adjus = random.choice([

				car_adjus_1, car_adjus_2, car_adjus_3, car_adjus_4,
				car_adjus_5, car_adjus_6, car_adjus_7, car_adjus_8,
				car_adjus_9, car_adjus_10, car_adjus_11, car_adjus_12,
				car_adjus_13, car_adjus_14

				])


		

	if car.top < 0:
		car.top = 0
	if car.bottom > screen_length:
		car.bottom = screen_length

	# Rotate the car image based on the current angle

	rotated_car_image = pygame.transform.rotate(car_adjus, angle)
	rotated_surface = pygame.transform.rotate(rect_surface, angle)


	# Adjust the rect to the new rotated image size, keeping the center
	rotated_rect = rotated_car_image.get_rect(center=car.center)
	
	#LA HITBOX MAS PEQUEÑA PARA DETETAR LAS COLISIONES
	smaller_hit_box = car.inflate(-inflation_value, -inflation_value)  
	corners = [
		(smaller_hit_box.topleft),
		(smaller_hit_box.topright),
		(smaller_hit_box.bottomright),
		(smaller_hit_box.bottomleft),
		(smaller_hit_box.center)
    ]

	

    #LOGICA DE LA HITBOX MAS PEQUEÑA
	rotated_corners = [rotate_point(corner, angle, car.center) for corner in corners]

	# Clear the screen
	screen.fill(Black)

	#background
	if level_map == 1:
		if not level_selected:
			Info_lvl_1 = pygame.Rect(860, 10, 330, 175)
		else:
			Info_lvl_1 = pygame.Rect(860, 10, 330, 115)

		screen.blit(map1_adjus, screen_rect)
		if data_box:
			pygame.draw.rect(screen, Black, Info_lvl_1 )

	elif level_map == 2:
		if not level_selected:
			Info_lvl_1 = pygame.Rect(960, 10, 230, 175)
		else:
			Info_lvl_1 = pygame.Rect(960, 10, 230, 115)

		screen.blit(map2_adjus, screen_rect)

		if data_box:
			pygame.draw.rect(screen, Black, Info_lvl_1 )

	elif level_map == 3:
		if not level_selected:
			Info_lvl_1 = pygame.Rect(960, 10, 230, 175)
		else:
			Info_lvl_1 = pygame.Rect(960, 10, 230, 115)
			
		screen.blit(map3_adjus, screen_rect)
		if data_box:
			pygame.draw.rect(screen, Black, Info_lvl_1 )

	#car blitting
	smaller_hit_box.center = car.center

	

	
	if level_map == 3:
		defaul_sign = True
		screen.blit(rotated_car_image, rotated_rect)
	else:
		screen.blit(rotated_car_image, rotated_rect)
		defaul_sign = False

	

	# Verificar colisión con el rectángulo en el mapa 1
	if level_map == 1:
		for rect in rects_to_collide_map1:
			for corner in rotated_corners:
				if pygame.Rect(corner, (1, 1)).colliderect(rect):
					death += 1
					splash_v = True
					splash.center = corner
					splash_sound.play()
					if level_selected:
						starting_timer = True
					car.x = car_init_x
					car.y = car_init_y
					angle = 0

					break

		#ANIMACION DEL SPLASH
		if splash_v:
			if splash_time < 22:
				screen.blit(splash_adjus, splash)
				splash_time += 1
			else:
				splash_v = False
				splash_time = 0 

	#RECTANGULOS DE COLISION MAPA 2 Y DETECTOR DE COLISIONES
	elif level_map == 2:
		for rect in rects_to_collide_map2:
			for corner in rotated_corners:
				if pygame.Rect(corner, (1, 1)).colliderect(rect):
					death += 1
					out.play()

					splash_v = True
					cross_rect.center = corner

					car.x = car_init_x
					car.y = car_init_y
					car_x = car_init_x
					car_y = car_init_y

					angle = 0

					if level_selected:
						starting_timer = True

					break
		if splash_v:
			if splash_time < 22:
				screen.blit(cross_adjus, cross_rect)
				splash_time += 1
			else:
				splash_v = False
				splash_time = 0   

		# PERSONAS 1 INTERSECCION
		for people in people_first_intersection_list:

			#MOVIENDO PERSONAS (1 INTERSECCION)
			people.move_ip(0, people_velocity)

			#DETECCION DE COLISIONES CON PERSONAS (1 INTERSECCION)
			for corner in rotated_corners:
				if pygame.Rect(corner, (1, 1)).colliderect(people):
					death += 1
					scream.play()
					out.play()

					if level_selected:
						starting_timer = True

					car.x = car_init_x
					car.y = car_init_y
					car_x = car_init_x
					car_y = car_init_y

					angle = 0
					break 

			#DIBUJANDO PERSONAS (1 INTERSECCION)
			screen.blit(persona_adjus, people)

		#MOVIENDO PARA ATRAS LAS PERSONAS EN BUCLE (1 INTERSECCION)
		if people1_3.y < 110:
			for people in people_first_intersection_list:
				people.y += 440

		# PERSONAS 2 INTERSECCION
		for people in people_second_intersection_list:

			#MOVIENDO PERSONAS (2 INTERSECCION)
			people.move_ip(-people_velocity , 0)

			#DETECCION DE COLISIONES CON PERSONAS (2 INTERSECCION)
			for corner in rotated_corners:
				if pygame.Rect(corner, (1, 1)).colliderect(people):
					death += 1
					scream.play()
					out.play()

					if level_selected:
						starting_timer = True

					car.x = car_init_x
					car.y = car_init_y
					car_x = car_init_x
					car_y = car_init_y

					angle = 0
					break  

			
			#DIBUJANDO PERSONAS (2 INTERSECCION)
			screen.blit(persona_adjus_2, people)

			#MOVIENDO PARA ATRAS LAS PERSONAS EN BUCLE (2 INTERSECCION)
			if people2_7.x > -45:
				for people in people_second_intersection_list:
					people.x -= 225

		#DETECCION DE COLISIONES CON PERSONAS (3 INTERSECCION)
		for people in people_third_intersection_list:
			for corner in rotated_corners:
				if pygame.Rect(corner, (1, 1)).colliderect(people):
					death += 1
					scream.play()
					out.play()


					if level_selected:
						starting_timer = True

					car.x = car_init_x
					car.y = car_init_y
					car_x = car_init_x
					car_y = car_init_y
					angle = 0
					
					break  

			#MOVIENDO PERSONAS DEL NIVEL 2 PARA ATRAS EN BUCLE (3 INTERSECCION)
			if people3_5.x >= 285:
				people.x -= 225

			#MOVIENDO PERSONAS DEL NIVEL 2 EN DIAGONAL (3 INTERSECCION)
			if people.x >= 570 and people.x <= 640: 
				person_adjus_2_rotated = pygame.transform.rotate(persona_adjus_2, -45)
				people.move_ip(-people_velocity -0.5, -people_velocity * 0.85 -0.5)
				screen.blit(person_adjus_2_rotated, people)

			#MOVIENDO PERSONAS DEL NIVEL 2 EN DIAGONAL RECTO (3 INTERSECCION)
			elif people.x < 570:
				screen.blit(persona_adjus_2, people)
				people.move_ip(-people_velocity -0.5 , 0)
				people.y = 325

			#MOVIENDO PERSONAS DEL NIVEL 2 RECTO (3 INTERSECCION)
			elif people.x > 640:
				screen.blit(persona_adjus_2, people)
				people.move_ip(-people_velocity -0.5 , 0)
				people.y = 385
	
	#COLISIONES, YETIS, NIEVE DEL NIVEL 3		
	elif level_map == 3:
		touching_ice = True
		for rect in snow_rects:
			for corner in rotated_corners:
				if pygame.Rect(corner, (1, 1)).colliderect(rect):
					touching_ice = False
					break

			if not touching_ice:
				if sound_first_time2:
					snow_intro.play()
					sound_first_time2 = False

				break

		for rect in rects_to_collide_map3:
			for corner in rotated_corners:
				if pygame.Rect(corner, (1, 1)).colliderect(rect):
					splash_v = True
					particles_rect.center = corner

					if level_selected:
						starting_timer = True

					death += 1
					snowball_hit_number = 0
					car.x = car_init_x
					car.y = car_init_y
					car_x = car_init_x						
					car_y = car_init_y
					velocity_x = 0
					velocity_y = 0
					angle = 0
					force_reset_health = True
					
					out_crash.play()
					break


		for rect in snow_men_list:

			dx, dy = car.centerx - rect.centerx, car.centery - rect.centery
			angle_of_men = math.degrees(math.atan2(-dy, dx)) - 270

			
			rotated_image = pygame.transform.rotate(snow_man_adjus, angle_of_men)
			rotated_rect = rotated_image.get_rect(center=rect.center)

			
			screen.blit(rotated_image, rotated_rect.topleft)
			if random.randint(1, 75) == 1:
				
				speed = 3.75  # Velocidad de la bola de nieve
				random_offset = random.uniform(-25, 25)
				angle_radians = math.radians(angle_of_men + 270 + random_offset) 
				snowball_dx = math.cos(angle_radians) * speed
				snowball_dy = -math.sin(angle_radians) * speed

				# Creamos un rect para la bola de nieve
				snowball_rect = pygame.Rect(rect.centerx, rect.centery, 20, 20)  # Tamaño de 10x10
				snowballs.append({'rect': snowball_rect, 'dx': snowball_dx, 'dy': snowball_dy})

				snowball_throw.play()

		snowballs_to_remove = []

		for snowball in snowballs[:]:
			# Move the snowball
			snowball['rect'].x += snowball['dx']
			snowball['rect'].y += snowball['dy']
			screen.blit(snow_ball_adjus, snowball['rect'])

		    # Check if the snowball goes out of bounds
			if not screen.get_rect().colliderect(snowball['rect']):
				snowballs_to_remove.append(snowball)

		    # Check for collisions with walls
			for rect in walls_list:
				if snowball['rect'].colliderect(rect):
					snowballs_to_remove.append(snowball)
					snowball_hit.play()

					break  # No need to check further if the snowball already collided
			if snowball['rect'].colliderect(car):
				snowball_car_hit.play()
				snowballs_to_remove.append(snowball)
				snowball_hit_number += 1
				splash_v = True
				particles_rect.center = snowball['rect'].center
				health_down.play()
				
				
				reduce_health = True

			if key[pygame.K_u]: print(snowball_hit_number)

		# Remove the snowballs after the loop
		for snowball in snowballs_to_remove:
			if snowball in snowballs:  # Ensure the snowball is still in the list
				snowballs.remove(snowball)

		cycle_count += 1

	# Splash animation logic
		if splash_v:
			if splash_time < 22:
				screen.blit(particles_adjus, particles_rect)
				splash_time += 1
			else:
				splash_v = False
				splash_time = 0

		if defaul_sign:
			if sign_time <= 20:
				if sign:
					sign_time += 1
				sign = not sign
			elif sign_time > 20 and sign_time < 70:
				if touching_ice:
					if first_time_touching_ice:
						screen.blit(no_cross_sign_adjus, sign_rect)

						if sound_first_time:
							ice_intro.play()
							sound_first_time = False

					elif not first_time_touching_ice:
						screen.blit(smaller_no_cross_sign_adjus, smaller_sign_rect)
				elif not touching_ice:				
					if frist_time_touching_snow:			
						screen.blit(sign_adjus, sign_rect)
					elif not frist_time_touching_snow:
						screen.blit(smaller_sign_adjus, smaller_sign_rect)
				if sign:
					sign_time += 1
				sign = not sign

			else:
				if touching_ice and first_time_touching_ice and ice_count >= 1:
					first_time_touching_ice = False
					
				if not touching_ice and frist_time_touching_snow and snow_count >= 1:
					frist_time_touching_snow = False

				sign_time = 0
				ice_count += 1

				if not touching_ice:
					snow_count += 1


		if key[pygame.K_j]:
			for rect in walls_list:
				pygame.draw.rect(screen, Red, rect)
		if key[pygame.K_k]:
			for rect in snow_men_list:
				pygame.draw.rect(screen, Light_blue, rect)

			for snowball in snowballs:
				pygame.draw.rect(screen, Light_blue, snowball['rect'])

		pygame.draw.rect(screen, Grey, life_background)
		

		 # Reduce health progressively
		if reduce_health and current_health > 0:
			target_length = (current_health - 1) * health_per_point
			if current_health_length > target_length:
				current_health_length -= health_reduction_speed
			else:
				current_health -= 1
				
				reduce_health = False

		# Reset health when it reaches zero
		if current_health == 0 and current_health_length <= 0:
			current_health = max_health

			if level_selected:
				starting_timer = True

			death += 1
			snowball_hit_number = 0
			car.x = car_init_x
			car.y = car_init_y		
			car_x = car_init_x
			car_y = car_init_y
			velocity_x = 0
			velocity_y = 0
			angle = 0
			force_reset_health = True
					
			current_health_length = health_length

		if force_reset_health:
			current_health = max_health
			current_health_length = health_length
			force_reset_health = False

		pygame.draw.rect(screen, Green, pygame.Rect(290, 30, current_health_length, 32))
		screen.blit(heart_adjus, heart_rect)

	if key[pygame.K_h] and current_index == 0:
		if level_map == 1:
			for rect in rects_to_collide_map1:
				pygame.draw.rect(screen, Yellow, rect)
		elif level_map == 2:
			for rect in rects_to_collide_map2:
				pygame.draw.rect(screen, Dark_Green, rect)
		elif level_map == 3:
			for rect in rects_to_collide_map3:
				pygame.draw.rect(screen, Purple, rect)
		data_box = False

	else:


		data_box = True


	#PASAR EL TIEMPO A MINUTOS Y SEGUNDOS
	if start_time is not None:

		elapsed_time = pygame.time.get_ticks() - start_time
		milliseconds = (elapsed_time % 1000) / 10  # Get last 2 decimal places
		seconds = elapsed_time // 1000  # Convert to full seconds
		minutes = seconds // 60  # Get full minutes
		seconds = seconds % 60  # Get remaining seconds

		# Format the time string with proper rounding
		time_string = f"{minutes:02}:{seconds:02}"
		time_value = float(f'{seconds}.{milliseconds:02.0f}')

		rounded_time = '{:.2f}'.format(time_value).rstrip('0').rstrip('.')

		if minutes >= 1:
			final_time_string = f"{minutes} min/s {rounded_time} secs"
			final_time_string_long = True
		else:
			final_time_string = f"{rounded_time} secs"
			final_time_string_long = False

	#DEFINIR EL TEXTO DE "LEVEL: X"
	level = f"Level: {level_map}"

	#CUADRADO DE INFORMACION DEL MAPA 1
	if level_map == 1:
		if data_box:
			#NUMERO DE NIVEL
			level_txt = font.render(str(level), True, White)
			level_txt_rect = level_txt.get_rect(center=(level_txt_x, level_txt_y))
			screen.blit(level_txt, level_txt_rect)

			#TEXTO DE MUERTES

			if not level_selected:
				death_txt = font.render(str(f" Deaths: {death}"), True, White)
				death_txt_rect = death_txt.get_rect(center=(death_txt_x, death_txt_y))
				screen.blit(death_txt, death_txt_rect)

				time_txt_x = Info_lvl_1.centerx -40
				time_txt_y =Info_lvl_1.top + 140

			else:
				time_txt_x = Info_lvl_1.centerx -40
				time_txt_y = death_txt_y

			#TEXTO DE TIEMPO
			time_txt = font.render(str(f"Time: {time_string}"), True, White)
			time_txt_rect = level_txt.get_rect(center=(time_txt_x, time_txt_y))
			screen.blit(time_txt, time_txt_rect)

	#DEFINIENDO EL OMBRE DEL NIVEL Y LOS CUADRADOS DE TEXTO DEPENDIENDO DEL NIVEL
	if level_map == 1:
		level_name = "The Flooded Pathway"
		level_name_info_rect = pygame.Rect(0, 540, 525, 60)
		fps_rect = pygame.Rect(1115, 545, 80, 50)
	elif level_map == 2:
		level_name = "Roads of Chaos"
		level_name_info_rect = pygame.Rect(0, 550, 400, 50)
		fps_rect = pygame.Rect(1115, 545, 80, 50)
	elif level_map == 3:
		level_name = "Icy Peaks"
		level_name_info_rect = pygame.Rect(0, 540, 250, 60)
		fps_rect = pygame.Rect(1115, 545, 80, 50)

	#TEXTO DEL NIVEL
	level_name_txt = font.render(str(f"{level_name}"), True, White)
	level_name_txt_rect = level_name_txt.get_rect(center=(level_name_info_rect.center))

	#TEXTO DE FPS
	fps = clock.get_fps()
	fps_txt = font.render(str(f"{int(fps)}"), True, White)
	fps_txt_rect = fps_txt.get_rect(center=(fps_rect.center))

	#DIBUJANDO FPS Y NOMBRE DEL NIVEL 
	
	pygame.draw.rect(screen, Black, level_name_info_rect)
	pygame.draw.rect(screen, Black, fps_rect)
	screen.blit(level_name_txt, level_name_txt_rect)
	screen.blit(fps_txt, fps_txt_rect)
	screen.blit(back_arrow_adjus, back_arrow_but)


	#CUADRADO DE INFORMACION DEL MAPA 2
	if level_map == 2 or level_map == 3:
		if data_box:

			#NUMERO DEL NIVEL
			level_txt = font.render(str(level), True, White)
			level_txt_rect = level_txt.get_rect(center=(level_txt_x + 50, level_txt_y ))
			screen.blit(level_txt, level_txt_rect)

			#HACIENDO EL TEXTO DE MUERTES MAS PEQEUÑO SI ES MAS DE 10
			if not level_selected:
				if death > 9:
					death_txt = font2.render(str(f" Deaths: {death}"), True, White)
				else:
					death_txt = font.render(str(f" Deaths: {death}"), True, White)

				#TEXTO DE MUERTE
				death_txt_rect = death_txt.get_rect(center=(death_txt_x + 45, death_txt_y ))
				screen.blit(death_txt, death_txt_rect)

				time_txt_x = Info_lvl_1.centerx -40
				time_txt_y =Info_lvl_1.top + 140

			else:
				time_txt_x = Info_lvl_1.centerx -40
				time_txt_y = death_txt_y -5

			#TEXTO DE TIEMPO
			time_txt = font2.render(str(f"Time: {time_string}"), True, White)
			time_txt_rect = level_txt.get_rect(center=(time_txt_x + 18, time_txt_y + 8 ))
			screen.blit(time_txt, time_txt_rect)

	if level_map > number_of_levels:
		end_of_levels = True
		speed_run = False
		show_level_completed()

	#actualiza
	pygame.display.update()

	#TICK DEL RELOJ
	clock.tick(30)

#TERMINAR EL PROGRAMA :(
pygame.quit()
sys.exit()

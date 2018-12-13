file_path = "/Users/juancasian/Documents/PickAndPlace/video.gcode"

def move_piece(init_x, init_y, init_z, final_x, final_y, final_z, angle):
    speed = 5000
    watch_delay = 2
    watch_height = 90
    moving_delay = 1
    pump_delay = 1
    servo_delay = 2
    glue_delay = 1
    glue_x = -51
    glue_y = -11
    glue_z = 12
    with open(file_path, "a") as myfile:
        # watch piece
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(init_x, init_y, watch_height, speed))
        # wait to see
        myfile.write("G4 S{}\n".format(watch_delay))
        # go down to piece
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(init_x, init_y, init_z, speed))
        # wait to go down
        myfile.write("G4 S{}\n".format(moving_delay))
        # turn on pump
        myfile.write("M42 P57 S255\n")
        # wait for pump to start
        myfile.write("G4 S{}\n".format(pump_delay))
        # go up again
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(init_x, init_y, watch_height, speed))

        # travel above glue
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(glue_x, glue_y, watch_height, speed))
        # wait for a sexond
        myfile.write("G4 S{}\n".format(glue_delay))
        # dip in glue
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(glue_x, glue_y, glue_z, speed))
        # wait before going up
        myfile.write(" G4 S{}\n".format(glue_delay))
        # go up again
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(glue_x, glue_y, watch_height, speed))

        # travel above end position
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(final_x, final_y, watch_height, speed))
        # rotate the piece
        myfile.write("M280 P0 S{}\n".format(angle))
        # servomotor delay
        myfile.write("G4 S{}\n".format(servo_delay))
        # go down to leave piece
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(final_x, final_y, final_z, speed))
        # wait for nozzle to go down
        myfile.write("G4 S{}\n".format(moving_delay))
        # turn pump off
        myfile.write("M42 P57 S0\n")
        # wait for pump to wait
        myfile.write("G4 S{}\n".format(pump_delay))
        # go up again
        myfile.write("G0 X{} Y{} Z{} F{}\n".format(final_x, final_y, watch_height, speed))
        # wait for it to go up
        myfile.write("G4 S{}\n".format(moving_delay))
        # rotate nozzle to home
        myfile.write("M280 P0 S0\n")
        # wait for rotation
        myfile.write("G4 S{}\n".format(servo_delay))
        # go home
        myfile.write("G0 X0 Y0 Z120 F5000\n")

def initialize_gcode():
    with open(file_path, "a") as myfile:
        myfile.write("G28\n")
        myfile.write("G90\n")
        myfile.write("M280 P0 S0\n")
        myfile.write("G4 S1\n")

def close_gcode():
    with open(file_path, "a") as myfile:
        myfile.write("G28\n")

initialize_gcode()
move_piece(30, -70, 15, -60, 60, 4, 0)
move_piece(30, -70, 12, 60, 60, 4, 0)
move_piece(30, -70, 9, -50, 60, 7, 0)
move_piece(30, -70, 6, 50, 60, 7, 0)
move_piece(30, -70, 3, -40, 60, 10, 0)

move_piece(-29, -70, 12, 40, 60, 10, 0)
move_piece(-29, -70, 9, -30, 60, 13, 0)
move_piece(-29, -70, 6, 30, 60, 13, 0)
move_piece(-29, -70, 3, 0, 60, 16, 0)
close_gcode()

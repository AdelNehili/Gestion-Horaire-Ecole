from Classes.NodesEdgesClass import MapManager

master = MapManager(32 * 5) #MotherClass of NodeEdgesClass.py
master.setup()


if __name__ == "__main__":
    table = master.convert_color_hours()
    for element in table:
        print(element)

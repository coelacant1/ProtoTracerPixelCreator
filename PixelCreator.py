name = "KaiborgV1Pixels"
origFileName = "Example Files\KaiborgV1.csv"
outputFileName = "Output\\" + name + ".h"

with open(origFileName, 'r') as file:
    data = file.read()

    f = open(outputFileName, "w")

    lines = data.splitlines()

    f.write("#pragma once\n\n")

    x = []
    y = []

    for line in lines:
        split = line.split(",")

        x.append(float(split[1]))
        y.append(float(split[2]))

    f.write("Vector2D " + name + "[" + str(len(x)) + "] = {\n")

    for i, line in enumerate(x):
        if i < len(x) - 1:
            f.write("\t Vector2D(" + f'{x[i]:.2f}' + "f," + f'{y[i]:.2f}' + "f),\n")
        else:
            f.write("\t Vector2D(" + f'{x[i]:.2f}' + "f," + f'{y[i]:.2f}' + "f)\n};\n")
    
    f.close()

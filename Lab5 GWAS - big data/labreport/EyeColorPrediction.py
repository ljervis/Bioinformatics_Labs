# Finds Sample Eye Color Probabilities and Region Eye Color Probabilities 
# SNP's for 6 varients supplied in "Lab5_eyecolor_with_population.txt" which can be created with RegionInformation.py
# Outputs information in "lab5_eye_color_complete.txt"

import sys 
import math


def main():
    beta = populate_beta()
    list_pop = open_file()
    eye_color(beta, list_pop)
    output_data(list_pop)

def open_file():
    list_pop = []
    with open("lab5_eyecolor_with_population.txt") as f:
        for line in f:
            temp_list = line.split()
            allele = {}
            allele["rs12913832"] = temp_list[4].count("A")
            allele["rs1800407"] = temp_list[3].count("T")
            allele["rs12896399"] = temp_list[2].count("G")
            allele["rs16891982"] = temp_list[5].count("C")
            allele["rs1393350"] = temp_list[1].count("A")
            allele["rs12203592"] = temp_list[6].count("T")
            allele["origin"] = temp_list[7]
            allele["sample"] = temp_list[0]
            list_pop.append(allele)
    return list_pop

def populate_beta():
    beta = {}
    beta["rs12913832"] = (-4.81,-1.790)
    beta["rs1800407"] = (1.4,0.87)
    beta["rs12896399"] = (-0.58,-0.03)
    beta["rs16891982"] = (-1.3,-0.5)
    beta["rs1393350"] = (0.47,0.27)
    beta["rs12203592"] = (0.7,0.73)
    return beta

def eye_color(beta, list_pop):
    alpha = (3.94, 0.65)
    for ind in list_pop:
        sum_beta1 = 0
        sum_beta2 = 0
        for k,v in ind.items():
            if k != "origin" and k != "sample":
                sum_beta1 += v * beta[k][0]
                sum_beta2 += v * beta[k][1]
        exp = (math.exp(sum_beta1+alpha[0]), math.exp(sum_beta2+alpha[1]))
        ind["blue_prob"] = exp[0] / (1.0 + exp[0] + exp[1])
        ind["brown_prob"] = exp[1] / (1.0 + exp[0] + exp[1])
        ind["other_prob"] = 1 - (exp[0] / (1.0 + exp[0] + exp[1])) - (exp[1] / (1.0 + exp[0] + exp[1]))

def pop_average(list_pop):
    north = [0,0,0]
    south = [0,0,0]
    countn = 0
    counts = 0
    for i in list_pop:
        if i["origin"] == "CEU":
            countn += 1
            north[0] += i["blue_prob"]
            north[1] += i["brown_prob"]
            north[2] += i["other_prob"]
        elif i["origin"] == "TSI":
            counts += 1
            south[0] += i["blue_prob"]
            south[1] += i["brown_prob"]
            south[2] += i["other_prob"]
    north[0] /= countn
    north[1] /= countn
    north[2] /= countn
    south[0] /= counts
    south[1] /= counts
    south[2] /= counts
    return north, south

def output_data(list_pop):
    with open("lab5_eye_color_complete.txt", "w+") as f:
        north, south = pop_average(list_pop)
        f.write("european region\tblue prob.\t brown prob\tother prob\n")
        f.write("north\t" + str(north[0]) + "\t" + str(north[1]) + "\t" + str(north[2]) + "\n")
        f.write("south\t" + str(south[0]) + "\t" + str(south[1]) + "\t" + str(south[2]) + "\n")
        f.write("ID\tcount:rs12913832\tcount:rs1800407\tcount:rs12896399\tcount:rs16891982\tcount:rs1393350\tcount:rs12203592\torigin\tblue prob.\tbrown prob.\tother prob\n")
        for i in list_pop:
            f.write(i["sample"] + "\t" + str(i["rs12913832"]) + "\t" + str(i["rs1800407"]) + "\t" + str(i["rs12896399"]) + "\t" + 
            str(i["rs16891982"]) + "\t" + str(i["rs1393350"]) + "\t" + str(i["rs12203592"]) + "\t" + i["origin"] + "\t" + 
            str(i["blue_prob"]) + "\t" + str(i["brown_prob"]) + "\t" + str(i["other_prob"]) + "\n")

            

if __name__ == "__main__":
    main()
    





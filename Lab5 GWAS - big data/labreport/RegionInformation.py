# Adds Popultion Region Information to SNP File for use with EyeColorPrediction.py

def main():
    f = open("lab5_pred_eyecolor_transpose.tab")
    r = open("ceu_tsi_population_labels.txt")
    dict_pop = {}
    for line in r:
        dict_pop[line.split()[0]] = line.split()[1]
    r.close()
    c = open("lab5_eyecolor_with_population.txt", "w+")
    f.readline()
    for line in f:
        list_line = line.split()
        list_line.append(dict_pop[line.split()[0]])
        c.write(" ".join(list_line))
        c.write("\n")
    f.close()
    c.close()
    
if __name__ == "__main__":
    main()

        


#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    read=pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities= read["Akaa": "Äänekoski"]
    mask_speaking= municipalities["Share of Swedish-speakers of the population, %"]>5
    foreigners_mask= municipalities["Share of foreign citizens of the population, %"]>5
    masks= municipalities[mask_speaking & foreigners_mask]
    only_needed=masks[["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]
    return only_needed
    # print(only_needed)

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()

#!/usr/bin/python3

import sys
import requests


sep = ','
linecount = 1
result = ''

# Download COVID-19 CSV data from https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
covidcsv = requests.get(url, allow_redirects=True)
open('covidcsv', 'wb').write(covidcsv.content)


with open('covidcsv') as f:
    lines = f.readlines()

for line in lines:
    if linecount == 1: # skip 1st line, because it's the header's names
        linecount = linecount + 1
    else:
        #iso_code,continent,location,date,total_cases,new_cases,
        #new_cases_smoothed,total_deaths,new_deaths,new_deaths_smoothed,
        #total_cases_per_million,new_cases_per_million,
        #new_cases_smoothed_per_million,total_deaths_per_million,new_deaths_per_million,
        #new_deaths_smoothed_per_million,reproduction_rate,icu_patients,
        #icu_patients_per_million,hosp_patients,hosp_patients_per_million,
        #weekly_icu_admissions,weekly_icu_admissions_per_million,weekly_hosp_admissions,
        #weekly_hosp_admissions_per_million,new_tests,total_tests,
        #total_tests_per_thousand,new_tests_per_thousand,new_tests_smoothed,
        #new_tests_smoothed_per_thousand,positive_rate,tests_per_case,
        #tests_units,total_vaccinations,people_vaccinated,people_fully_vaccinated,
        #total_boosters,new_vaccinations,new_vaccinations_smoothed,
        #total_vaccinations_per_hundred,people_vaccinated_per_hundred,
        #people_fully_vaccinated_per_hundred,total_boosters_per_hundred,
        #new_vaccinations_smoothed_per_million,stringency_index,population,
        #population_density,median_age,aged_65_older,aged_70_older,gdp_per_capita,
        #extreme_poverty,cardiovasc_death_rate,diabetes_prevalence,female_smokers,
        #male_smokers,handwashing_facilities,hospital_beds_per_thousand,
        #life_expectancy,human_development_index,excess_mortality_cumulative,excess_mortality
        parts  = line.split(sep)
        isoco  = parts[0]
        conti  = parts[1]
        locat  = parts[2]
        date   = parts[3].replace('-', '')
        ncases = parts[5].split('.')
        deaths = parts[8].split('.')
        cases  = str(ncases[0])
        deaths = str(deaths[0])

        if len(isoco) > 0:
            # Data contain Cases_on_an_international_conveyance_Japan,
            # but we are not interested on it. Hence, filter it out.
            # There are also aggregated data by continents, so are filtered.
            if len(isoco) < 4:
                result = date + cases.zfill(8) + deaths.zfill(8) + isoco + locat.ljust(40)
                print(result)

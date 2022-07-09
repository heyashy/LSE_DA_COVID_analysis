# LSE_DA_COVID_analysis

## Assignment 2: Import and explore the data

![Gibralter Time Series](https://raw.githubusercontent.com/heyashy/LSE_DA_COVID_analysis/main/images/gib_time_series.png)

### *Findings*

Our data set contains time-series data from 2020-01-22 until 2021-10-15. In the above example we examined the case, death, recovery and hospitalisation data fro Gibralter. From the above chart we can extrapulate:

- There were disproportionate hospitalisations at the start of the data set
- Hospitalisations don't mimic cases. We should look into this more
- Deats are relatively low
- Recvoered cases closley follow reported cases but suddenly fall off in a sharp drop. This should be looked into further

We may have possible errors and missing information in our data that would need to be examined further. This includes:

- Mismatch of hospitalisations to case numbers
- Sudden drop in recovered data

Things to look at include:

- Why there was a sudden spike of cases mid way through the data set
- Hospitalisations exceed case numbers several times and actually dropped to nearlly zero at the peak of the cases

## Assignment activity 3: Merge and analyse the data

![3.1-normalised-cases](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-cases.png?raw=true)
![3.1-normalised-deaths](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-deaths.png?raw=true)
![3.1-normalised-hospital](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-hospital.png?raw=true)
![3.1-normalised-recovered](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-recovered.png?raw=true)
![3.1-normalised-vaccinations](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-vaccinations.png?raw=true)

## *Findings*

There are several anomalies with our data set that need to be taken into account when we review our findings. We need to go over these as possible errors in data and would need to add a low confidence margin to any finding below

> **NOTE:** OTHERS is going to skew our dataset so we should remove it from all analysis

- Normalised vaccinations and hospital admissions charts show that every Province has an exact match to the other in terms of shape. This is impossible in the real world and there would be variances. We should look into the source of this data and find errors
- Gibraltar, Turs and Caicos Islands Isle of Man and British Virgin Islands all have a significat spike in cases mid way through our timeframe. We should look into this further.
- Anguilla, Montserrat, Cayman Islands and Stain Helena, Ascension and Tristian de Cunha all have very weird plots for the normalised deaths. We should look into this further
- Falkland Islands has had no deaths. This could be an error.
- Our recovery data looks incomplete. We need to look at why the data suddenly stops todards the end of the data set.
- Many of the normalised graphs in the dataframe have a step pattern which is not possible from complete data of the nature we are dealing with. We should look at the raw data to see if there are missing or incorret values within it.

### Insights

- Anguilla, The Isle of Man and British Virgin Islands controlled the spread of infection the best
- The Falkland Islands had not deaths
- Montesrrat had the most deaths per capita.
- There is a odd spike in hospital admissions at the start of the pandemic. There is also a major spike towards the end of 2020. This is then followed by a major drop in admissions. This would impy that the hospital beds were full and it has a direct correlation to the rise in death rates across all regions.
- Apart from Others, who only had recovered patinets at the start of the pandemic the rest of the countries had recovery in-line with the rise in infection rates.

## Assignment activity 4: Merge and analyse the data

The anomalies in our dataset are truly visible when we look at vaccination interest and first does over second dose as percentages in the barchart below:

![4.1-vaccination-interest](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/vaccination_interest.png?raw=true)
![first-dose-percentage](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/first_dose_over_second.png?raw=true)


Although impossible, ever Province/Region has an exact match of vaccination interest to the other. In the real world and there would be variances and we should look into the source of this data and find errors.

Plotting with months over dates really helps make our data more readable. As we can see below the chart plotted with months is much easier to read as the resolution of the data we are looking at is less granular.

> **The percentage of the first dose to fully vaccinated individuals is 96.28%**

![recovered-monthly](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/recovered_over_time.png?raw=true)
![recoverd-over-time-high-dpi](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/recovered_over_time_high_dpi.png?raw=true)

From our recovery chart we can see that:

- The Channel Islands had the best performance when it came to recoveries from early on in the pandemic.
- The British Virgin Islands had the worst performance  when it came to recoveries and they only started to pickup after July 2021
- Gibraltar had a slow start to recovery but then soared to the top

### Heatmaps

![heatmap](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/corr_heatmap.png?raw=true)

From our correlation heatmap we can see that the most correlated variables are:

- Recovered  cases against second dose
- Recovered cases against fully vaccinated
- Recovered against cases and deaths shows that more people recovered than died from the virus

###  Deaths

![deaths](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/deaths_over_time_global.png?raw=true)

From our global death data we can see two main spikes in deaths during our data set that plateau for a short period between each spike. It can be assumed that governement intervention and policy casued the spikes to plateau. We should look into this further.

---
## Assignment activity 5: Analyse the Twitter data

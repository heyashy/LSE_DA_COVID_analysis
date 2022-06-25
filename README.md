# LSE_DA_COVID_analysis

---
## Assignment 2: Import and explore the data

![Gibralter Time Series](https://raw.githubusercontent.com/heyashy/LSE_DA_COVID_analysis/main/images/gib_time_series.png)

# Initial findings

<p>Our data set contains time-series data from 2020-01-22 until 2021-10-15. In the above example we examined the case, death, recovery and hospitalisation data fro Gibralter. From the above chart we can extrapulate:</p>

- There were disproportionate hospitalisations at the start of the data set
- Hospitalisations don't mimic cases. We should look into this more
- Deats are relatively low
- Recvoered cases closley follow reported cases but suddenly fall off in a sharp drop. This should be looked into further

<p>We may have possible errors and missing information in our data that would need to be examined further. This includes:</p>

- Mismatch of hospitalisations to case numbers
- Sudden drop in recovered data

<p>Things to look at include:</p>
- Why there was a sudden spike of cases mid way through the data set
- Hospitalisations exceed case numbers several times and actually dropped to nearlly zero at the peak of the cases

## Assignment activity 3: Merge and analyse the data

![3.1-normalised-cases](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-cases.png?raw=true)
![3.1-normalised-deaths](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-deaths.png?raw=true)
![3.1-normalised-hospital](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-hospital.png?raw=true)
![3.1-normalised-recovered](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-recovered.png?raw=true)
![3.1-normalised-vaccinations](https://github.com/heyashy/LSE_DA_COVID_analysis/blob/main/images/3.1-normalised-vaccinations.png?raw=true)

## <u>Findings</u>

<p>There are several anomalies with our data set that need to be taken into account when we review our findings. We need to go over these as possible errors in data and would need to add a low confidence margin to any finding below</p>

<p><u><strong>OTHERS</strong> is going to skew our dataset so we should remove it from all analysis</u></p>

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

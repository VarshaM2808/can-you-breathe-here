# can you breathe here
Air Quality &amp; Public Health Risk Analysis using Python

## Project Overview

Air pollution affects millions of people every day, yet its impact is often communicated using technical numbers that are difficult to interpret. Air Quality Index (AQI) values and public health statistics exist, but they are rarely connected in a way that clearly answers a simple question:

 **Can people breathe safely where they live?**

This project combines air quality and public health data to create a clear, easy-to-understand picture of environmental health risk across countries and years. Instead of focusing only on raw numbers or charts, the project introduces a new, interpretable metric called the **Breathability Score**, designed to make complex data meaningful for everyone — including non-technical audiences.

---

##  Objectives

This project aims to:

- Understand how air pollution varies across countries and over time  
- Explore the relationship between air pollution and respiratory health outcomes  
- Combine datasets that were originally reported at different geographic levels  
- Communicate health risk in a clear way  
- Present insights responsibly and transparently  

---

##  Data Sources

- **Air Quality Data:** City-level AQI dataset sourced from Kaggle
   https://www.kaggle.com/datasets/beridzeg45/air-quality-index-across-the-world
- **Public Health Data:** Country-level respiratory health indicators sourced from Kaggle
   https://www.kaggle.com/datasets/malaiarasugraj/global-health-statistics

---

##  Data Cleaning & Preparation

Before analysis, the raw datasets required preparation to ensure accuracy and consistency:

- Country names were extracted from city names to align records  
- Only relevant variables were retained to reduce noise  
- Data types and missing values were checked to ensure reliability  

This ensured all further analysis was based on clean, trustworthy data.

---

##  Solving a Real-World Data Challenge  
### City-Level vs Country-Level Data

A key challenge was that:

- Air quality data was reported at the **city level**  
- Health data was reported at the **country level**

Because these geographic levels did not match, the datasets could not be compared directly.

###  Solution

City-level AQI values were aggregated into **country-year averages**.  
For each country and year, the following were calculated:

- Average AQI  
- Median AQI  
- Number of cities contributing data  

This mirrors how real-world analysts reconcile datasets from different sources.

---

##  Preparing the Health Data

The health dataset already summarized information at the country level but still required refinement:

- Only respiratory health indicators were selected  
- Column names were simplified for clarity  
- Duplicate country - year records were aggregated  

This resulted in one clean health profile per country per year.

---

##  Data Integration

Once both datasets were prepared:

- They were merged using **Country** and **Year**  
- Only years with both air quality and health data were retained  

The result was a single, aligned dataset that allowed pollution and health outcomes to be analyzed together.

---

##  Exploratory Data Analysis (EDA)

### Key Patterns Observed

- Countries with higher air pollution often experience worse respiratory health outcomes  
- Urbanization and pollution tend to increase together  
- Strong healthcare systems reduce risk but cannot fully offset poor air quality  

These patterns were explored using:

- Scatter plots (AQI vs respiratory mortality)  
- Correlation heatmaps  
- Country-level comparisons  

---

##  The Breathability Score

### Why Create a New Score?

Raw AQI values or mortality rates can be difficult to interpret, especially for non-technical audiences. To address this, the project introduces the **Breathability Score** — a single number that summarizes how safe the air is to breathe in a given country and year.

The goal is not to replace medical or environmental assessments, but to translate complex data into a human-centered metric.

---

###  How the Score Is Calculated

Two equally important factors are used:

1. **Air Pollution Level** (average AQI)  
2. **Respiratory Health Impact** (respiratory mortality rate)  

Both values are normalized to a common scale and given equal weight.


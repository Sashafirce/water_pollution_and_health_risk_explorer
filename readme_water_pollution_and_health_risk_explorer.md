<p align="center">
  <img src="water_pollution_and_ health_ risk_ explorer.jpg" 
</p>

## WATER POLLUTION AND HEALTH RISK EXPLORER

This Water Pollution & Health Risk Explorer project is an evidence-based, interdisciplinary 

project aiming to describe the ways environmental determinants like water pollution, access 

to clean water, sanitation, and healthcare facilities contribute to public health 

outcomes—specifically infant mortality and disease burden—in low- and middle-income 

countries.

In my role as **Project Manager**, I oversaw the entire life cycle of the project, from scoping 

research questions through timelines coordination, to ensuring all deliverables were 

integrated into strategic goals.

As a **Data Analyst and Econometrist**, I performed extensive data wrangling, hypothesis 

testing, and regression modeling to test key hypotheses from real world global datasets. I 

applied multiple linear regression, interaction terms, and Random Forest modeling to 

identify insights and build evidence-driven predictive models.

As a **Data Visualiser**, I designed intuitive, easy-to-understand visualisations using 

Python libraries (Matplotlib, Seaborn, Plotly) and visualisations on Tableau and integrated 

them into an interactive Streamlit dashboard that supports users—especially non-technical 

stakeholders—to quickly grasp complex relationships in an instant.

As a **Design Thinker**, I applied empathy and user-centred design principles to ensure an understable data analysis and the 

dashboard is accessible, actionable, and decision-maker-focused for public health and 

development fields.

Finally, as a Developer, I built and validated the dashboard for later deployment on Heroku, 

combining frontend UI/UX and backend machine learning algorithms to create an intuitive 

interactive process.

This combined process—researched, analyzed, designed, and developed—allowed the project to 

function both as an analytical investigation and as a useful tool for policymakers and 

researchers coordinating water-related public health dangers.



### **Dataset Content**

    Describe your dataset. Choose a dataset of reasonable size to avoid exceeding the repository's maximum size of 100Gb.

### **Business Requirements**
- Identify drivers of infant mortality and disease outbreaks at the socioeconomic and 

environmental levels.

- Predict health risk based on available indicators (e.g., sanitation, water access, GDP, 

pollution).

- Create an interactive dashboard for policymakers to map and act on hotspots of health 

burden.

    Describe your business requirements

## Hypotheses and Supporting Literature

### H1: Water Contamination vs Disease Burden

**Hypothesis:** Higher levels of water contamination are associated with increased disease burden.  

-  **Supporting Literature:** WHO and UN Water reports consistently show that contaminated 

water sources increase the spread of waterborne diseases such as diarrhoea, cholera, and 

typhoid fever.

- Industrial pollutants, heavy metals, and untreated sewage have been directly linked to a 

rise in Disability-Adjusted Life Years (DALYs) in multiple developing regions.

🔗 _Supporting literature:_  
> - Prüss-Ustün, A., et al. (2019). *Burden of disease from inadequate water, sanitation and hygiene for selected adverse health outcomes: An updated analysis with a focus on low- and middle-income countries.* International Journal of Hygiene and Environmental Health, 222(5), 765–777.  
> - WHO (2023). *Drinking-water*. [https://www.who.int/news-room/fact-sheets/detail/drinking-water](https://www.who.int/news-room/fact-sheets/detail/drinking-water)

### H2: Healthcare Access Index vs Disease Burden

**Hypothesis:** Countries with stronger healthcare access tend to experience lower overall 

disease burden.  

- **Supporting Literature:** The Global Burden of Disease study and World Bank research 

highlight the role of healthcare accessibility in reducing preventable disease and mortality.

-  Countries with higher scores in healthcare infrastructure and access demonstrate better 

health outcomes and resilience against environmental risk factors.

🔗 _Supporting literature:_  
> - Boerma, T., et al. (2014). *Monitoring progress towards universal health coverage at country and global levels*. PLoS Med, 11(9), e1001731.  
> - Jamison, D. T., et al. (2013). *Global Health 2035: a world converging within a generation*. The Lancet, 382(9908), 1898–1955.

### H3: Water & Sanitation Index vs Infant Mortality

**Hypothesis:** Better water and sanitation services are associated with lower infant 

mortality rates. 

- **Supporting Literature:** UNICEF and WHO studies reveal that lack of access to clean 

water and safe sanitation is one of the leading causes of neonatal and infant deaths, 

especially in low-income countries.

- Hygiene education, proper sewage systems, and access to potable water are identified as 

key drivers in reducing under-five mortality.

🔗 _Supporting literature:_  
> - UNICEF & WHO (2021). *Progress on household drinking water, sanitation and hygiene 2000–2020: Five years into the SDGs*.  
> - Esrey, S. A., et al. (1991). *Effects of improved water supply and sanitation on ascariasis, diarrhoea, dracunculiasis, hookworm infection, schistosomiasis, and trachoma*. Bulletin of the World Health Organization, 69(5), 609–621.


### Machine Learning: Predicting Infant Mortality Rate

**Objective:** Predict infant mortality based on a range of socioeconomic and environmental 

indicators.  


## Project Plan

This project followed a structured data analysis pipeline to investigate the relationships 

between water pollution, public health outcomes, and socioeconomic factors.

### Workflow Overview:

1. **Data Collection:**

   - Publicly available datasets on water contamination levels, health burden indices, 
   
   healthcare access, GDP, infant mortality, and sanitation were gathered and merged.

   - Sources included WHO, World Bank, and national statistics.

2. **Data Management:**

   - Raw files were imported into a Jupyter Notebook.

   - Datasets were stored and versioned locally and documented via GitHub.

   - A CSV file was cleaned and transformed into a final dataset used for Tableau and app 
   
   development.

3. **Exploratory Data Analysis (EDA):**

   - EDA was conducted using pandas, seaborn, and matplotlib to understand data 
   
   distributions, correlations, and outliers.

4. **Hypothesis Testing:**

   - Three hypotheses were defined and visualised using Tableau dashboards:

     - H1: Water Contamination vs Disease Burden
     - H2: Healthcare Access vs Disease Burden
     - H3: Water & Sanitation vs Infant Mortality

5. **Machine Learning:**

   - A Random Forest Regressor was trained to predict Infant Mortality Rate using 
   
   socioeconomic and environmental variables.

   - Predictions were added to the dataset and visualised.

6. **Dashboard Development:**

   - Tableau dashboards were created for each hypothesis and ML prediction.

   - Dashboards were embedded in a Streamlit app with interactive filters and KPI styling.


### Research Methodology:

It has been adopted a hybrid research approach combining descriptive analytics, inferential 

visualisation, and predictive modelling to enable both exploration and insight communication.

The use of design thinking guided the dashboard structure, prioritising user experience and 

data storytelling.

##Design Thinking Implemented in the app creation


1.  **Human-Centric Navigation**

•	Sidebar navigation is simple and uses intuitive language.

•	Clear section titles: Hypotheses, ML, About.

2.  **Easy to Understand**

•	Plain English markdown introduces each page.

•	Avoids jargon to make it accessible to a general audience.

3. **Engaging Aesthetic**

•	Soft background colours

•	Accessible text contrast (dark blue headers)

•	Clean layout with white space

4. 📊 Seamless Tableau Integration

•	Direct links to dashboards (replace <PASTE_LINK> placeholders).



## Rationale to Map Business Requirements to Data Visualisations

| Business Requirement | Mapped Visualisation | Rationale |
|----------------------|----------------------|-----------|
| Understand public health risk from water pollution | H1 Bubble Map + Filterable Contamination Levels | Easily reveals hotspots for disease burden linked to pollution levels |
| Identify countries with weak healthcare systems & high disease burden | H2 Scatter Plot (Healthcare Index vs Disease Burden) | Visualises systemic healthcare gaps impacting public health |
| Explore sanitation impact on infant mortality | H3 Bubble Map (Sanitation Index vs Infant Mortality) | Helps decision-makers prioritise sanitation interventions |
| Assess data-driven policy scenarios | ML Predicted Infant Mortality Map | Offers forward-looking insights to plan for vulnerable countries |

---

## Analysis Techniques Used

- **Descriptive Statistics:** to summarise key indicators (mean, median, skewness, kurtosis)

- **Correlation Matrices:** to detect multicollinearity and patterns

- **Visual Mapping (Tableau):** for regional comparisons and interactivity

- **Random Forest Regression:** for prediction modelling of Infant Mortality

### Structuring the Analysis:
- Each hypothesis was explored visually before applying modelling.
- The ML model used a curated set of variables and validated via R² and feature importance.

## Bugs / Limitations

- Some missing values were imputed via mean, which may dilute extreme signals.

- The model's R² could be improved with local data.

- Real-time prediction dashboard still in beta.


### Limitations & Alternative Approaches:

- **Data gaps** for certain regions limited completeness; handled by using averages or 

excluding from the visual.

- **No time-series analysis** was conducted due to inconsistent yearly data; future work 

could incorporate panel data.

- **Alternative model testing (e.g., XGBoost)** was skipped for simplicity and 

interpretability.

## Dashboard design

Dashboard Features:

- Global Overview Map – Average Health Burden (Choropleth)

- Country Profiles – Sanitation, Water, Pollution, Mortality

- Trend Explorer – Temporal and economic trends

- Health Risk Predictor – User input + live predictions

- Designed for both policy stakeholders and data-savvy users

  Clikc the links below to explore the dashboards:

 - [Machine Learning model](https://public.tableau.com/app/profile/sasha.firce/viz/WaterpollutionHealthriskML/Dashboard4)

 - [Hipothesis 1](https://public.tableau.com/app/profile/sasha.firce/viz/Waterpollutionhealthriskh1/Dashboard1)

 - [Hipothesis 2](https://public.tableau.com/app/profile/sasha.firce/viz/WaterpollutionHealthriskh2/Dashboard2)

 - [Hypothesis 3](https://public.tableau.com/app/profile/sasha.firce/viz/WaterpollutionHealthriskH3real/Dashboard3)

### Use of Generative AI:

- Assisted with:

  - Code debugging and optimising scripts

  - Visual design ideation (colour schemes, layout guidance)

  - Machine learning model correction framing and structuring



### Ethical Considerations

- **Data Privacy:**

  - All data was aggregated at the national level with no personal identifiers.

- **Bias & Fairness:**

  - Country data imbalance was addressed using clear visual indicators for missing or 
  
  limited data.

  - The ML model's limitations were communicated transparently.

- **Responsible AI:**

  - Model results are descriptive, not prescriptive.

  - Predictions are designed to provoke further exploration, not policy enforcement.

- **Transparency:**

  - All methods and assumptions are documented.

  - The app empowers users with filters and tooltips to avoid misleading narratives.

- **Social Impact:**

  - Designed to inform public health planning and environmental justice efforts.

  - Highlighted the intersection between resource access and health outcomes.



**Development Roadmap**

 The challenges I faced included technical issues, particularly with the internet 
 
 connection, and a mid-level mistake I made during the ETL pipeline process.  The main issue 
 
 was that I noticed the error while creating the app for the project, which required 
 
 restarting almost the entire project. There is a final issue: I am unable to deploy the app 
 
 on Heroku because I deleted the Authentication app that was required to create the Heroku 
 
 account, and now I cannot log in to my account. I tried to download the app again, but all 
 
 the information from my Heroku account was deleted. In summary, I have an app that I cannot 
 
 show as I wanted. The good thing is that anyone can open the app and activate it through VS 
 
 Code.

**Deployment Heroku**


I could not deploy my app due to technical issues however it can be opened through VS Code. I can also provide the link of the Local server. 

    

**Main Data Analysis Libraries**

- Pandas, Numpy, Matplotlib, Plotly, Seaborn, Scipy.stats, Sklearn, and Statmodelsapi.
   

**Credits**

 https://www.w3schools.com/python/pandas/pandas_analyzing.asp. It helped me understand and learn how to analyse the data properly.
• https://copilot.microsoft.com/chats/NdbvxkFKX1cA4RBrX4jtu I used it specifically for logic and syntax errors.
• https://www.markdownguide.org/basic-syntax/ I needed to write the README document.

**Media**

    The image used for the cover of the jupyter notebook and the README document was made with Canva.

**Acknowledgements**

    Thank you to my classmates for all their support especially to Ivy, Faiza, Jane, Celia, 
    
    Ronnie, Angel, Shema, Andrei and Celina and the rest of the group. Also to my tutor 
    
    Emma, Mark, Spencer and Neil, they are the best teachers and experts.

    "Last but not least, I wanna thank me, I wanna thank me for believing in me I wanna 
    
    thank me for doing all this hard work, I wanna thank me for having no days off, I wanna 
    
    thank me for never quitting."




import pandas as pd
from IPython.display import display

# Read the ASC file into a DataFrame, skipping the first row as it contains variable names
dat = pd.read_table("GermanCredit/SouthGermanCredit.asc", header=0, delimiter=" ")

# Rename the headers to match the R script
nam_evtree = ["status", "duration", "credit_history", "purpose", "amount", 
              "savings", "employment_duration", "installment_rate",
              "personal_status_sex", "other_debtors",
              "present_residence", "property",
              "age", "other_installment_plans",
              "housing", "number_credits",
              "job", "people_liable", "telephone", "foreign_worker",
              "credit_risk"]
dat.columns = nam_evtree

# Make factors for all except the numeric variables
# Make sure that even empty level of factor purpose is included
for col in dat.columns.difference(["duration", "amount", "age", "installment_rate", "present_residence", "number_credits"]):
    dat[col] = dat[col].astype('category')

# Assign level codes
dat["credit_risk"] = dat["credit_risk"].astype('category').cat.set_categories(["bad", "good"])

# Assign level codes for each categorical variable
# (you can copy the code block from the previous response)

# dat["status"] = pd.Categorical(dat["status"], categories=[
#     "no checking account",
#     "... < 0 DM",
#     "0<= ... < 200 DM",
#     "... >= 200 DM / salary for at least 1 year"
# ])

# dat["credit_history"] = pd.Categorical(dat["credit_history"], categories=[
#     "delay in paying off in the past",
#     "critical account/other credits elsewhere",
#     "no credits taken/all credits paid back duly",
#     "existing credits paid back duly till now",
#     "all credits at this bank paid back duly"
# ])

# dat["savings"] = pd.Categorical(dat["savings"], categories=[
#     "unknown/no savings account",
#     "... <  100 DM",
#     "100 <= ... <  500 DM",
#     "500 <= ... < 1000 DM",
#     "... >= 1000 DM"
# ])

# dat["employment_duration"] = pd.Categorical(dat["employment_duration"], categories=[
#     "unemployed",
#     "< 1 yr",
#     "1 <= ... < 4 yrs",
#     "4 <= ... < 7 yrs",
#     ">= 7 yrs"
# ])

# dat["installment_rate"] = pd.Categorical(dat["installment_rate"], categories=[
#     ">= 35",
#     "25 <= ... < 35",
#     "20 <= ... < 25",
#     "< 20"
# ])

# dat["other_debtors"] = pd.Categorical(dat["other_debtors"], categories=[
#     "none",
#     "co-applicant",
#     "guarantor"
# ])

# dat["personal_status_sex"] = pd.Categorical(dat["personal_status_sex"], categories=[
#     "male : divorced/separated",
#     "female : non-single or male : single",
#     "male : married/widowed",
#     "female : single"
# ])

# dat["present_residence"] = pd.Categorical(dat["present_residence"], categories=[
#     "< 1 yr",
#     "1 <= ... < 4 yrs",
#     "4 <= ... < 7 yrs",
#     ">= 7 yrs"
# ])

# dat["property"] = pd.Categorical(dat["property"], categories=[
#     "unknown / no property",
#     "car or other",
#     "building soc. savings agr./life insurance",
#     "real estate"
# ])

# dat["other_installment_plans"] = pd.Categorical(dat["other_installment_plans"], categories=[
#     "bank",
#     "stores",
#     "none"
# ])

# dat["housing"] = pd.Categorical(dat["housing"], categories=[
#     "for free",
#     "rent",
#     "own"
# ])

# dat["number_credits"] = pd.Categorical(dat["number_credits"], categories=[
#     "1",
#     "2-3",
#     "4-5",
#     ">= 6"
# ])

# dat["job"] = pd.Categorical(dat["job"], categories=[
#     "unemployed/unskilled - non-resident",
#     "unskilled - resident",
#     "skilled employee/official",
#     "manager/self-empl./highly qualif. employee"
# ])

# dat["people_liable"] = pd.Categorical(dat["people_liable"], categories=[
#     "3 or more",
#     "0 to 2"
# ])

# dat["telephone"] = pd.Categorical(dat["telephone"], categories=[
#     "no",
#     "yes (under customer name)"
# ])

# dat["foreign_worker"] = pd.Categorical(dat["foreign_worker"], categories=[
#     "yes",
#     "no"
# ])


# Display the DataFrame
# display(dat)

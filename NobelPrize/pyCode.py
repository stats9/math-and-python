# %%
import requests
import pandas as pd

# Define the base URL of the Nobel Prize API
url = "https://api.nobelprize.org/v1/prize.json"

# Send a GET request to the API and retrieve the response
response = requests.get(url)

# Convert the response into JSON format
data = response.json()

# Initialize an empty list to store extracted records
records = []

# Loop through each prize entry in the dataset
for prize in data["prizes"]:
    # Extract the year of the prize
    year = prize.get("year")
    # Extract the category of the prize (e.g., physics, chemistry, medicine)
    category = prize.get("category")
    
    # Each prize may have multiple laureates, so loop through them
    for laureate in prize.get("laureates", []):
        # Build a dictionary for each laureate with relevant fields
        records.append({
            "Year": year,  # Year when the prize was awarded
            "Category": category,  # Prize category
            "Laureate_ID": laureate.get("id"),  # Unique ID of the laureate
            "Name": laureate.get("firstname", "") + " " + laureate.get("surname", ""),  # Full name
            "Motivation": laureate.get("motivation", ""),  # Reason for awarding the prize
            "Share": laureate.get("share", ""),  # Share of the prize (if divided among laureates)
        })
# %%
# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(records)

# Save the DataFrame into a CSV file with UTF-8 encoding
df.to_csv("nobel_prize_winners.csv", index=False, encoding="utf-8")

# Print a confirmation message once the file is created
print("The file 'nobel_prize_winners.csv' has been successfully created.")
# %%
df
# %%

import requests
import pandas as pd
import numpy as np

# Define the base URLs of the Nobel Prize API
prize_url = "https://api.nobelprize.org/v1/prize.json"
laureate_url = "https://api.nobelprize.org/v1/laureate.json"

# Step 1: Fetch prize data
prize_response = requests.get(prize_url)
prize_data = prize_response.json()

# Step 2: Fetch laureate data (contains country of birth and affiliations)
laureate_response = requests.get(laureate_url)
laureate_data = laureate_response.json()

# Step 3: Build a dictionary mapping laureate IDs to their details
laureate_info_map = {}
for laureate in laureate_data["laureates"]:
    laureate_id = laureate.get("id")
    born_country = laureate.get("bornCountry", np.nan)
    affiliations = laureate.get("affiliations", [])
    laureate_info_map[laureate_id] = {
        "bornCountry": born_country,
        "affiliations": affiliations
    }

# Step 4: Combine prize and laureate data into a clean DataFrame
records = []
for prize in prize_data["prizes"]:
    year = prize.get("year")
    category = prize.get("category")
    
    for laureate in prize.get("laureates", []):
        laureate_id = laureate.get("id")
        name = laureate.get("firstname", "") + " " + laureate.get("surname", "")
        motivation = laureate.get("motivation", "")
        share = laureate.get("share", "")
        
        # Get laureate details from the map
        info = laureate_info_map.get(laureate_id, {})
        born_country = info.get("bornCountry", np.nan)
        
        # For Peace and Literature prizes, set university fields as missing
        if category in ["peace", "literature"]:
            records.append({
                "Year": year,
                "Category": category,
                "Laureate_ID": laureate_id,
                "Name": name,
                "Motivation": motivation,
                "Share": share,
                "Born_Country": born_country,
                "University": np.nan,
                "University_Country": np.nan
            })
        else:
            # For scientific categories, extract affiliations if available
            affiliations = info.get("affiliations", [])
            if affiliations:
                for aff in affiliations:
                    records.append({
                        "Year": year,
                        "Category": category,
                        "Laureate_ID": laureate_id,
                        "Name": name,
                        "Motivation": motivation,
                        "Share": share,
                        "Born_Country": born_country,
                        "University": aff.get("name", np.nan),
                        "University_Country": aff.get("country", np.nan)
                    })
            else:
                # If no affiliation is listed, mark as missing
                records.append({
                    "Year": year,
                    "Category": category,
                    "Laureate_ID": laureate_id,
                    "Name": name,
                    "Motivation": motivation,
                    "Share": share,
                    "Born_Country": born_country,
                    "University": np.nan,
                    "University_Country": np.nan
                })

# Step 5: Create the DataFrame
df = pd.DataFrame(records)

# Step 6: Save the DataFrame into a CSV file
df.to_csv("nobel_prize_clean.csv", index=False, encoding="utf-8")

print("The file 'nobel_prize_clean.csv' has been successfully created.")
print(df.head())
# %%
import pandas as pd 
import numpy as np 
dat = pd.read_csv("./nobel_prize_clean.csv", encoding="latin1")
# dat.loc[dat['Year'] == 2025, 'Name']

# %%

import pandas as pd
import gender_guesser.detector as gender

# Define a list of keywords that typically indicate an organization rather than a person
org_keywords = ["University", "Institute", "Committee", "Organization", "Academy", "Council"]

def detect_gender(name):
    """
    Detect gender based on the given name.
    If the name contains organization-related keywords, return 'Organization'.
    Otherwise, extract the first name and use the gender-guesser library to predict gender.
    """
    # Check if the name belongs to an organization
    if any(word.lower() in name.lower() for word in org_keywords):
        return "Organization"
    
    # If not an organization, assume it is a person's name
    # Extract the first name (the first word in the string)
    first_name = name.split()[0]
    
    # Initialize the gender detector
    d = gender.Detector()
    
    # Return the predicted gender for the first name
    return d.get_gender(first_name)

# Create a sample DataFrame with author names

# Apply the detect_gender function to each author name
dat["GenderGuess"] = dat["Name"].apply(detect_gender)

# Print the resulting DataFrame with gender predictions
print(dat.head())
# %%
dat.to_csv("datNobel.csv")

# %%
import pandas as pd 
dat2 = pd.read_csv("./nobel_prize_clean.csv", encoding="latin1")
dat2.columns
# %%
dat2.Gender.value_counts()

# %%
import country_converter as coco

cc = coco.CountryConverter()
# %%
def country_to_continent(country_name):
    if country_name == "ORGANIZATION":
        return "International"
    return cc.convert(names=country_name, to='continent')

print(country_to_continent("Japan"))         # Asia
print(country_to_continent("Egypt"))         # Africa
print(country_to_continent("ORGANIZATION"))  # International
# %%
dat2['Continent'] = list(map(country_to_continent, 
                                dat2["Born_Country"]))
# %%
dat2["Continent"].value_counts()
# %%



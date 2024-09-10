# scrapes alumni data in a csv file from linkedin
# input: name, linkedin
# output: name, linkedin, email, position, company, city, area, past, grad_year
import csv
import re
import time
import requests
import sys

# extract the linkedin username from a linkedin link
def extract_linkedin_username(link):
  m = re.search('linkedin.com/in/(.+?)/', link)
  if m:
    return m.group(1)
  raise

# get data of the person from linkedin
def get_linkedin_data(name, linkedin, username):
  url = "https://linkedin-profiles-and-company-data.p.rapidapi.com/profile-details"
  payload = {
	  "profile_id": username,
	  "profile_type": "personal",
	  "contact_info": False,
	  "recommendations": False,
	  "related_profiles": False
  }
  headers = {
	  "x-rapidapi-key": sys.argv[1],
	  "x-rapidapi-host": "linkedin-profiles-and-company-data.p.rapidapi.com",
	  "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)
  print(response.status_code)
  json = response.json()

  try:
    grad_year = json["education"][0]["date"]["end"]["year"]
  except (AttributeError, KeyError):
    grad_year = None
  
  past_experience = ""
  curr_position = None
  curr_company = None
  curr_location_long = None
  curr_location = None

  first_time = 1
  for position in json["position_groups"]:
    if first_time:
      first_time = 0
      curr_position = position["profile_positions"][0]["title"]
      curr_company = position["profile_positions"][0]["company"]
      curr_location_long = position["profile_positions"][0]["location"]
      curr_location = None if curr_location_long is None else curr_location_long.split(",")[0]
    else:
      past_title = position["profile_positions"][0]["title"]
      past_company = position["profile_positions"][0]["company"]
      if past_company is not None and past_title is not None and past_company != "WestPeak Research Association":
        past_experience += (past_company + " - " + past_title + "; ")
  return([name, linkedin, "", curr_position, curr_company, curr_location, "", past_experience, grad_year])

# Begin main script
with open("input.csv", newline="") as infile, open("output.csv", "a+", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    for row in reader:
      name = row["name"]
      linkedin = row["linkedin"]
      username = extract_linkedin_username(linkedin)
      data = get_linkedin_data(name, linkedin, username)
      print(data)
      writer.writerow(data)
      time.sleep(3)
    
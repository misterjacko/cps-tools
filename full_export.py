import requests
import pandas as pd
from datetime import datetime, timedelta

def save_as_csv(api_tag, response):
    time = datetime.now() - timedelta(hours=6) #Central time offset
    time = time.strftime("%Y-%m-%d-%H%M")
    df = pd.read_json(response.text, orient="records")
    filename = "{0}-{1}.csv".format(api_tag, time)
    df.to_csv(filename, index=False)
    print("{0} saved".format(filename))


def export_data(apis, save_files):
    print("Calling APIs. This can take some time")
    for api_tag in apis.keys():
        print("Calling: {0}".format(api_tag))
        response = requests.get(apis[api_tag])
        if save_files:
            save_as_csv(api_tag, response)       

apis = {
    # "district_weekly_actionable21": "https://api.cps.edu/health/cps/District2021WeeklyCovidActionable",
    "district_daily_actionable21": "https://api.cps.edu/health/cps/District2021DailyCovidActionable",
    # "district_no_admit": "https://api.cps.edu/health/cps/DistrictNoAdmittanceSummary",
    # "School_no_admit": "https://api.cps.edu/health/cps/SchoolNoAdmittanceSummary",
    # "school_weekly_actionable": "https://api.cps.edu/health/cps/SchoolWeeklyCovidActionable",
    # "district_weekly_actionable": "https://api.cps.edu/health/cps/DistrictWeeklyCovidActionable",
    # "district_weekly_testing": "https://api.cps.edu/health/cps/District2021WeeklyCOVIDTesting",
    # "district_daily_testing": "https://api.cps.edu/health/cps/District2021DailyCOVIDTesting",
    # "school_daily_actionable": "https://api.cps.edu/health/cps/School2021DailyCovidActionable",
    # "school_daily_surveillance": "https://api.cps.edu/health/cps/SchoolDailyCOVIDSurveillance",
    # "network_daily_surveillance": "https://api.cps.edu/health/cps/NetworkDailyCOVIDSurveillance",
    # "district_daily_surveillance": "https://api.cps.edu/health/cps/DistrictDailyCOVIDSurveillance",
}

if __name__ == "__main__":
    # save_files: save a time stampped copy of the api response as csv (True/False)
    save_files = True

    # returns a dictionary similar to apis above with the api name as the key and
    # the raw response of the call as the value.
    export_data(apis, save_files)
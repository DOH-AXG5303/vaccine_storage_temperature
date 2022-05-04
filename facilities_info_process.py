import redcap
from credentials import api_keys #dictionary of 4 api keys: prod_pid100, dev_pid100, prod_pid278, dev_pid278
from credentials import dev_url
from credentials import prod_url
from credentials import unique_event

def facility_info_transform(df_facility_info):
    """
    A single function to capture 3 transformations of facility_info event
    
    args:
        df_facility_info - dataframe of facility info report (report_id:2137)
    return:
        Dataframe - transformed dataframe
    """
    df_facility_info = df_facility_info.copy()
    
    # Create new event field, set all values to "facility_arm_1"
    df_facility_info["redcap_event_name"] = "facility_arm_1"
    # Create new field for complete/incomplete tag, and set all values to 2
    df_facility_info["facility_info_complete"] = 2
    # Move "redcap_event_name" to first column in prep for import
    col = df_facility_info.pop("redcap_event_name")
    df_facility_info.insert(0, col.name, col)
    
    return df_facility_info

if __name__ == "__main__":

    #API connection
    prod100 = redcap.Project(prod_url, api_keys["prod_pid100"])
    dev278 = redcap.Project(dev_url, api_keys["dev_pid278"])

    # 1)Export Report #38 prod
    df_facility_info = prod100.export_report(report_id=2137 ,format_type = "df")
    print("export complete")

    # 2) complete several transformations
    df_facility_info = facility_info_transform(df_facility_info)
    print("transform complete")
    
    # 3) import into dev environment
    dev278.import_records(df_facility_info, import_format = "df")
    print("process complete")









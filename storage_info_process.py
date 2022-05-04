import redcap
from credentials import api_keys #dictionary of 4 api keys: prod_pid100, dev_pid100, prod_pid278, dev_pid278
from credentials import dev_url
from credentials import prod_url
from credentials import unique_event


def storage_info_transform(df_storage_info):
    """
    A single function to capture 5 transformations of storage_info event
    
    args:
        df_storage_info - dataframe of storage info report (report_id:2111)
    return:
        Dataframe - transformed dataframe
    """
    
    df_storage_info = df_storage_info.copy()
    
    # Create new event field, set all values to "facility_arm_1"
    df_storage_info["redcap_event_name"] = unique_event
    # Create new field for complete/incomplete tag, and set all values to 2
    df_storage_info["storage_info_complete"] = 2
    # Rename columns 
    mapper = {"waiis_fac_name":"waiis_fac_name_s", 
                 "loc_vfc_pin":"loc_vfc_pin_s",
                 "org_name":"org_name_s" }
    df_storage_info = df_storage_info.rename(columns = mapper)
    # move "redcap_event_name" to first column in prep for import
    col = df_storage_info.pop("redcap_event_name")
    df_storage_info.insert(0, col.name, col)
    # conver float fields to int
    float_fields = df_storage_info.dtypes[df_storage_info.dtypes == float].index
    df_storage_info.loc[:, float_fields] = df_storage_info.loc[:, float_fields].astype("Int64")
    
    return df_storage_info


if __name__ == "__main__":

    #API Connection
    prod100 = redcap.Project(prod_url, api_keys["prod_pid100"])
    dev278 = redcap.Project(dev_url, api_keys["dev_pid278"])

    # 1)Export Report #38 prod
    df_storage_info = prod100.export_report(report_id = 2111 ,format_type = "df")
    print("export complete")

    # 2) Complete transformation
    df_storage_info = storage_info_transform(df_storage_info)

    #3) import into dev environment
    dev278.import_records(df_storage_info, import_format = "df")
    print("process complete")










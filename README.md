# Vaccine temp pipeline
REDCap Project lead: Wu, Jia (DOH) <jia.wu@doh.wa.gov>
Data process owner: Alexey Gilman <alexey.gilman@doh.wa.gov>
Frequency: monthly, last day of the month

### Process Description:
Report ID = [2137, 2111] (report numbers 38 and 39 respectively)

A:
1) export report: "Export facility info for temperature logs upload", #38 (2137)
2) Complete 3 transformations
    - add field: "redcap_event_name" = "facility_arm_1", for all records
    - add field: "facility_info_complete" = 2, for all records
    - set field "redcap_event_name" as second index
3) import into PID278

B:
1) export report: "Export storage info for temperature logs upload", #39 (2111)
2) Complete 4 transformations
    - add field: "redcap_event_name" = "month_year_arm_1", month spelled out, all lower case, 4 digit integer for year, global variable
    - add field: "storage_info_complete" = 2, for all records
    - rename columns according to:
        {
         "waiis_fac_name":"waiis_fac_name_s",
         "loc_vfc_pin":"loc_vfc_pin_s",
         "org_name":"org_name_s"
         }
     - set field "redcap_event_name" as second index
3) import into PID278

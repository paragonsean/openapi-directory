from typing import List, Dict
from aiohttp import web

from openapi_server.models.sdw_rest_services_get_qid_get200_response import SdwRestServicesGetQidGet200Response
from openapi_server.models.sdw_rest_services_get_systems_get200_response import SdwRestServicesGetSystemsGet200Response
from openapi_server import util


async def sdw_rest_services_get_download_get(request: web.Request, qid, output=None, qcolumns=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Download Data Service

    Based on the QID obtained from a get_systems query, return a comma separated value (CSV) file of the water systems found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default).
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def sdw_rest_services_get_download_post(request: web.Request, qid, output=None, qcolumns=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Download Data Service

    Based on the QID obtained from a get_systems query, return a comma separated value (CSV) file of the water systems found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default).
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def sdw_rest_services_get_qid_get(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Paginated Results Service

    GET_QID is passed with a query ID corresponding to a previously run get_systems query. It then returns a Systems object containing all matching water systems. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param pageno: Indicates the number of the page to display. It is used only when the results are paginated.
    :type pageno: 
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param newsort: Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    :type newsort: 
    :param descending: Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    :type descending: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def sdw_rest_services_get_qid_post(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Paginated Results Service

    GET_QID is passed with a query ID corresponding to a previously run get_systems query. It then returns a Systems object containing all matching water systems. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param pageno: Indicates the number of the page to display. It is used only when the results are paginated.
    :type pageno: 
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param newsort: Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    :type newsort: 
    :param descending: Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    :type descending: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def sdw_rest_services_get_systems_get(request: web.Request, output=None, p_fn=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_zip=None, p_reg=None, p_trb=None, p_act=None, p_qiv=None, p_ico=None, p_pid=None, p_owop=None, p_systyp=None, p_swtyp=None, p_popsv=None, p_cntysv=None, p_cs=None, p_mr=None, p_health=None, p_other=None, p_pn=None, p_sv=None, p_qs=None, p_sfs=None, p_pswpol=None, p_pswvio=None, p_pbale=None, p_cuale=None, p_rc350v=None, p_pbv=None, p_cuv=None, p_lcrv=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_qis=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_ss5yr=None, p_sdc=None, p_sdc_ils=None, p_ysl=None, p_ysly=None, p_ysla=None, p_idt1=None, p_idt2=None, p_cms_flag=None, queryset=None, responseset=None, param_callback=None, qcolumns=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Systems Search Service

    Returns an array of public water systems that meet the specified search criteria.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_fn: Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    :type p_fn: str
    :param p_ct: Facility City Filter. Enter a single case-insensitive city name to filter results.
    :type p_ct: str
    :param p_co: Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    :type p_co: str
    :param p_fips: FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    :type p_fips: str
    :param p_st: Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    :type p_st: str
    :param p_zip: 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    :type p_zip: str
    :param p_reg: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_reg: str
    :param p_trb: Tribe name
    :type p_trb: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    :type p_act: str
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_ico: Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_owop: Owner/Operator code filter.  Enter one of the following codes to filter results: - F &#x3D; Federal Government - S &#x3D; State Government - L &#x3D; Local Government - M &#x3D; Public/Private - N &#x3D; Native American - P &#x3D; Private
    :type p_owop: str
    :param p_systyp: Type of public water system: - CWS&#x3D;Community water system - NCWS&#x3D;Non-community water system - NTCWS&#x3D;Non-transient non-community water system - TNCWS&#x3D;Transient non-community water system
    :type p_systyp: str
    :param p_swtyp: Source Water Type: - SW &#x3D; Surface water  - GW&#x3D; Ground water - GU &#x3D; Ground water under direct influence of (UDI) surface water - SWP &#x3D; Purchased Surface water - GWP &#x3D; Purchased Ground water - GUP &#x3D; Purchased Ground water UDI surface water
    :type p_swtyp: str
    :param p_popsv: Estimated average daily population served by a system: - LE500 &#x3D; 500 or less - IN501_3K &#x3D; 501-3,300 - IN3K_10K &#x3D; 3,301-10,000 - IN10K_100K &#x3D; 10,001-100,000 - IN100K_1M &#x3D; 100,001-1,000,000 - GT1M &#x3D; More than 1,000,000 May contain multiple comma-separated values.
    :type p_popsv: str
    :param p_cntysv: 
    :type p_cntysv: str
    :param p_cs: Current violations: - M &#x3D; Monitoring and Reporting Violations - H &#x3D; Health-based Violations - O &#x3D; Other Violations - P &#x3D; Public Notice Violations - S &#x3D; Serious Violator - N &#x3D; No Violations May contain multiple comma-separated values.
    :type p_cs: str
    :param p_mr: Monitoring and Reporting Violations (failure to conduct regular monitoring of drinking water quality or submit monitoring results in a timely fashion).
    :type p_mr: str
    :param p_health: Violations of health-based drinking water standards (maximum contaminant levels, maximum residual disinfectant levels, or treatment technique rules).
    :type p_health: str
    :param p_other: Other violations, such as failing to issue annual consumer confidence reports or maintain required records.
    :type p_other: str
    :param p_pn: Public Notice Violations (failure to immediately alert consumers of serious problem with drinking water).
    :type p_pn: str
    :param p_sv: Serious Violator (unresolved serious, multiple, and/or continuing violations). A value of Y will return only SDWIS systems that are Serious Violators, while a value of N will only return SDWIS Systems that are not Serious Violators.
    :type p_sv: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_sfs: Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    :type p_sfs: str
    :param p_pswpol: For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    :type p_pswpol: str
    :param p_pswvio: Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    :type p_pswvio: str
    :param p_pbale: Lead Action Level Exceedance.  A \&quot;Y\&quot; value will select water systems with at least 1 Lead Action Level Exceedance.
    :type p_pbale: str
    :param p_cuale: Copper Action Level Exceedance.  A \&quot;Y\&quot; value will select water systems with at least 1 Copper Action Level Exceedance.
    :type p_cuale: str
    :param p_rc350v: Rule code 350 violation. A \&quot;Y\&quot; value will select water systems with at least one rule code 350 violation.
    :type p_rc350v: str
    :param p_pbv: Lead Violations.  A \&quot;Y\&quot; value will select water systems with at least 1 Lead Violation.
    :type p_pbv: str
    :param p_cuv: Copper Violation.  A \&quot;Y\&quot; value will select water systems with at least 1 Copper Violation.
    :type p_cuv: str
    :param p_lcrv: Lead or Copper rule violations.  A \&quot;Y\&quot; value will select water systems with at least 1 Lead or Copper Rule Violation.
    :type p_lcrv: str
    :param p_fea: Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_fea: str
    :param p_feay: Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    :type p_feay: 
    :param p_feaa: Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All
    :type p_feaa: str
    :param p_iea: Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_iea: str
    :param p_ieay: Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    :type p_ieay: 
    :param p_ieaa: Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State
    :type p_ieaa: str
    :param p_qis: Significant Quarters in Noncompliance Limiter.  Enter one of the following codes to limit results to facilities having given quarters of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GE1 &#x3D; One or more quarters in noncompliance. - GT1 &#x3D; More than one quarters in noncompliance. - GE2 &#x3D; Two or more quarters in noncompliance. - GT2 &#x3D; More than two quarters in noncompliance. - GE4 &#x3D; Four or more quarters in noncompliance. - GT4 &#x3D; More than four quarters in noncompliance. - GE8 &#x3D; Eight or more quarters in noncompliance. - GT8 &#x3D; More than eight quarters in noncompliance. - GE12 &#x3D; Twelve or more quarters in noncompliance. - GT12 &#x3D; Twelve or more quarters in noncompliance. - 12 &#x3D; Exactly twelve quarters in noncompliance. Note the seemingly incongruous of GT12 is deliberate.
    :type p_qis: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_ss5yr: Sanitary Surveys (in past 5 years) flag.  Values of visit_reason_code are either \&quot;SNSV\&quot; or \&quot;SNSP\&quot; in the past 5 years indicate a Sanitary Survey.    Enter \&quot;Y\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \&quot;N\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for greater for facilities with a quantity than or equal to that value.   
    :type p_ss5yr: str
    :param p_sdc: Significant Deficiency Count (in past 5 years) flag.    Enter \&quot;Y\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \&quot;N\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for facilities with a quantity greater than or equal to that value.
    :type p_sdc: str
    :param p_sdc_ils: 
    :type p_sdc_ils: str
    :param p_ysl: Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_ysl: str
    :param p_ysly: Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    :type p_ysly: str
    :param p_ysla: Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State
    :type p_ysla: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_cms_flag: 
    :type p_cms_flag: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def sdw_rest_services_get_systems_post(request: web.Request, output=None, p_fn=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_zip=None, p_reg=None, p_trb=None, p_act=None, p_qiv=None, p_ico=None, p_pid=None, p_owop=None, p_systyp=None, p_swtyp=None, p_popsv=None, p_cntysv=None, p_cs=None, p_mr=None, p_health=None, p_other=None, p_pn=None, p_sv=None, p_qs=None, p_sfs=None, p_pswpol=None, p_pswvio=None, p_pbale=None, p_cuale=None, p_rc350v=None, p_pbv=None, p_cuv=None, p_lcrv=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_qis=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_ss5yr=None, p_sdc=None, p_sdc_ils=None, p_ysl=None, p_ysly=None, p_ysla=None, p_idt1=None, p_idt2=None, p_cms_flag=None, queryset=None, responseset=None, param_callback=None, qcolumns=None) -> web.Response:
    """Safe Drinking Water Act (SDWA) Systems Search Service

    Returns an array of public water systems that meet the specified search criteria.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_fn: Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    :type p_fn: str
    :param p_ct: Facility City Filter. Enter a single case-insensitive city name to filter results.
    :type p_ct: str
    :param p_co: Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    :type p_co: str
    :param p_fips: FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    :type p_fips: str
    :param p_st: Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    :type p_st: str
    :param p_zip: 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    :type p_zip: str
    :param p_reg: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_reg: str
    :param p_trb: Tribe name
    :type p_trb: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    :type p_act: str
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_ico: Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_owop: Owner/Operator code filter.  Enter one of the following codes to filter results: - F &#x3D; Federal Government - S &#x3D; State Government - L &#x3D; Local Government - M &#x3D; Public/Private - N &#x3D; Native American - P &#x3D; Private
    :type p_owop: str
    :param p_systyp: Type of public water system: - CWS&#x3D;Community water system - NCWS&#x3D;Non-community water system - NTCWS&#x3D;Non-transient non-community water system - TNCWS&#x3D;Transient non-community water system
    :type p_systyp: str
    :param p_swtyp: Source Water Type: - SW &#x3D; Surface water  - GW&#x3D; Ground water - GU &#x3D; Ground water under direct influence of (UDI) surface water - SWP &#x3D; Purchased Surface water - GWP &#x3D; Purchased Ground water - GUP &#x3D; Purchased Ground water UDI surface water
    :type p_swtyp: str
    :param p_popsv: Estimated average daily population served by a system: - LE500 &#x3D; 500 or less - IN501_3K &#x3D; 501-3,300 - IN3K_10K &#x3D; 3,301-10,000 - IN10K_100K &#x3D; 10,001-100,000 - IN100K_1M &#x3D; 100,001-1,000,000 - GT1M &#x3D; More than 1,000,000 May contain multiple comma-separated values.
    :type p_popsv: str
    :param p_cntysv: 
    :type p_cntysv: str
    :param p_cs: Current violations: - M &#x3D; Monitoring and Reporting Violations - H &#x3D; Health-based Violations - O &#x3D; Other Violations - P &#x3D; Public Notice Violations - S &#x3D; Serious Violator - N &#x3D; No Violations May contain multiple comma-separated values.
    :type p_cs: str
    :param p_mr: Monitoring and Reporting Violations (failure to conduct regular monitoring of drinking water quality or submit monitoring results in a timely fashion).
    :type p_mr: str
    :param p_health: Violations of health-based drinking water standards (maximum contaminant levels, maximum residual disinfectant levels, or treatment technique rules).
    :type p_health: str
    :param p_other: Other violations, such as failing to issue annual consumer confidence reports or maintain required records.
    :type p_other: str
    :param p_pn: Public Notice Violations (failure to immediately alert consumers of serious problem with drinking water).
    :type p_pn: str
    :param p_sv: Serious Violator (unresolved serious, multiple, and/or continuing violations). A value of Y will return only SDWIS systems that are Serious Violators, while a value of N will only return SDWIS Systems that are not Serious Violators.
    :type p_sv: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_sfs: Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    :type p_sfs: str
    :param p_pswpol: For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    :type p_pswpol: str
    :param p_pswvio: Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    :type p_pswvio: str
    :param p_pbale: Lead Action Level Exceedance.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Lead Action Level Exceedance.
    :type p_pbale: str
    :param p_cuale: Copper Action Level Exceedance.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Copper Action Level Exceedance.
    :type p_cuale: str
    :param p_rc350v: Rule code 350 violation. A \\\&quot;Y\\\&quot; value will select water systems with at least one rule code 350 violation.
    :type p_rc350v: str
    :param p_pbv: Lead Violations.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Lead Violation.
    :type p_pbv: str
    :param p_cuv: Copper Violation.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Copper Violation.
    :type p_cuv: str
    :param p_lcrv: Lead or Copper rule violations.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Lead or Copper Rule Violation.
    :type p_lcrv: str
    :param p_fea: Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_fea: str
    :param p_feay: Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
    :type p_feay: 
    :param p_feaa: Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All
    :type p_feaa: str
    :param p_iea: Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_iea: str
    :param p_ieay: Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
    :type p_ieay: 
    :param p_ieaa: Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State
    :type p_ieaa: str
    :param p_qis: Significant Quarters in Noncompliance Limiter.  Enter one of the following codes to limit results to facilities having given quarters of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GE1 &#x3D; One or more quarters in noncompliance. - GT1 &#x3D; More than one quarters in noncompliance. - GE2 &#x3D; Two or more quarters in noncompliance. - GT2 &#x3D; More than two quarters in noncompliance. - GE4 &#x3D; Four or more quarters in noncompliance. - GT4 &#x3D; More than four quarters in noncompliance. - GE8 &#x3D; Eight or more quarters in noncompliance. - GT8 &#x3D; More than eight quarters in noncompliance. - GE12 &#x3D; Twelve or more quarters in noncompliance. - GT12 &#x3D; Twelve or more quarters in noncompliance. - 12 &#x3D; Exactly twelve quarters in noncompliance. Note the seemingly incongruous of GT12 is deliberate.
    :type p_qis: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_ss5yr: Sanitary Surveys (in past 5 years) flag.  Values of visit_reason_code are either \\\&quot;SNSV\\\&quot; or \\\&quot;SNSP\\\&quot; in the past 5 years indicate a Sanitary Survey.    Enter \\\&quot;Y\\\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \\\&quot;N\\\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for greater for facilities with a quantity than or equal to that value.   
    :type p_ss5yr: str
    :param p_sdc: Significant Deficiency Count (in past 5 years) flag.    Enter \\\&quot;Y\\\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \\\&quot;N\\\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for facilities with a quantity greater than or equal to that value.
    :type p_sdc: str
    :param p_sdc_ils: 
    :type p_sdc_ils: str
    :param p_ysl: Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_ysl: str
    :param p_ysly: Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    :type p_ysly: str
    :param p_ysla: Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State
    :type p_ysla: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_cms_flag: 
    :type p_cms_flag: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)

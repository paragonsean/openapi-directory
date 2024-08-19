from typing import List, Dict
from aiohttp import web

from openapi_server.models.rcra_rest_services_get_facilities_get200_response import RcraRestServicesGetFacilitiesGet200Response
from openapi_server.models.rcra_rest_services_get_facility_info_get200_response import RcraRestServicesGetFacilityInfoGet200Response
from openapi_server.models.rcra_rest_services_get_geojson_get200_response import RcraRestServicesGetGeojsonGet200Response
from openapi_server.models.rcra_rest_services_get_map_get200_response import RcraRestServicesGetMapGet200Response
from openapi_server.models.rcra_rest_services_get_qid_get200_response import RcraRestServicesGetQidGet200Response
from openapi_server import util


async def rcra_rest_services_get_download_get(request: web.Request, qid, output=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Download Data Service

    Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_download_post(request: web.Request, qid, output=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Download Data Service

    Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_facilities_get(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_stdist=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_act=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_cmps=None, p_law=None, p_section=None, p_qiv=None, p_impw=None, p_trep=None, p_olr=None, p_oct=None, p_trichem=None, p_tri_lr_pol=None, p_tri_lr_yr=None, p_tri_lr_amt=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_wbd=None, p_pid=None, p_med=None, p_owc=None, p_owd=None, p_opc=None, p_opd=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_owop=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_cifdi=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_psncq=None, p_dwd=None, p_violy=None, p_ncv=None, p_fcv=None, p_violt=None, p_des=None, p_fntype=None, p_pidall=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_decouple=None, p_ejscreen_over80cnt=None, queryset=None, responseset=None, tablelist=None, maplist=None, summarylist=None, param_callback=None, qcolumns=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Facility Search Service

    Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_fn: Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    :type p_fn: str
    :param p_sa: Facility street address. Enter a complete or partial street address.
    :type p_sa: str
    :param p_sa1: Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    :type p_sa1: str
    :param p_ct: Facility City Filter. Enter a single case-insensitive city name to filter results.
    :type p_ct: str
    :param p_co: Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    :type p_co: str
    :param p_fips: FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    :type p_fips: str
    :param p_st: Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    :type p_st: str
    :param p_stdist: State District Filter.  Enter a single state district to restrict results.
    :type p_stdist: str
    :param p_zip: 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    :type p_zip: str
    :param p_frs: Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    :type p_frs: str
    :param p_reg: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_reg: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    :type p_sic: str
    :param p_ncs: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_ncs: str
    :param p_pen: Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    :type p_pen: str
    :param p_c1lat: In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lat: 
    :param p_c1lon: In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lon: 
    :param p_c2lat: In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lat: 
    :param p_c2lon: In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lon: 
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_sic2: Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc.
    :type p_sic2: str
    :param p_sic4: Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    :type p_sic4: str
    :param p_fa: Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    :type p_fa: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    :type p_act: str
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
    :param p_cmps: RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
    :type p_cmps: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_olr: Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases.
    :type p_olr: str
    :param p_oct: Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases.
    :type p_oct: str
    :param p_trichem: 
    :type p_trichem: str
    :param p_tri_lr_pol: 
    :type p_tri_lr_pol: str
    :param p_tri_lr_yr: 
    :type p_tri_lr_yr: str
    :param p_tri_lr_amt: 
    :type p_tri_lr_amt: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA
    :type p_med: str
    :param p_owc: 
    :type p_owc: str
    :param p_owd: 
    :type p_owd: str
    :param p_opc: 
    :type p_opc: str
    :param p_opd: 
    :type p_opd: str
    :param p_ysl: Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_ysl: str
    :param p_ysly: Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    :type p_ysly: 
    :param p_ysla: Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State
    :type p_ysla: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_sfs: Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    :type p_sfs: str
    :param p_tribeid: Numeric code for tribe (or list of tribes).
    :type p_tribeid: 
    :param p_tribename: Tribe Name Filter.  Enter a single tribe name to filter results.
    :type p_tribename: str
    :param p_tribedist: Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    :type p_tribedist: 
    :param p_owop: Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
    :type p_owop: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values.
    :type p_pityp: str
    :param p_cifdi: Compliance issuess found during inspection.
    :type p_cifdi: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_violy: Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
    :type p_violy: 
    :param p_ncv: Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
    :type p_ncv: str
    :param p_fcv: Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
    :type p_fcv: str
    :param p_violt: RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violt: str
    :param p_des: Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \&quot;TSDF\&quot; to return the full enforcement TSDF universe and \&quot;Operating TSDF\&quot; to return the operating TSDF universe.
    :type p_des: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_decouple: Decouple Inspection Code Search Flag.  Enter \&quot;Y\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    :type p_decouple: str
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param tablelist: Table List Flag. Enter a Y to display the first page of facility results.
    :type tablelist: str
    :param maplist: Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    :type maplist: str
    :param summarylist: Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    :type summarylist: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def rcra_rest_services_get_facilities_post(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_stdist=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_act=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_cmps=None, p_law=None, p_section=None, p_qiv=None, p_impw=None, p_trep=None, p_olr=None, p_oct=None, p_trichem=None, p_tri_lr_pol=None, p_tri_lr_yr=None, p_tri_lr_amt=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_wbd=None, p_pid=None, p_med=None, p_owc=None, p_owd=None, p_opc=None, p_opd=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_owop=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_cifdi=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_psncq=None, p_dwd=None, p_violy=None, p_ncv=None, p_fcv=None, p_violt=None, p_des=None, p_fntype=None, p_pidall=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_decouple=None, p_ejscreen_over80cnt=None, queryset=None, responseset=None, tablelist=None, maplist=None, summarylist=None, param_callback=None, qcolumns=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Facility Search Service

    Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_fn: Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    :type p_fn: str
    :param p_sa: Facility street address. Enter a complete or partial street address.
    :type p_sa: str
    :param p_sa1: Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    :type p_sa1: str
    :param p_ct: Facility City Filter. Enter a single case-insensitive city name to filter results.
    :type p_ct: str
    :param p_co: Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    :type p_co: str
    :param p_fips: FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    :type p_fips: str
    :param p_st: Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    :type p_st: str
    :param p_stdist: State District Filter.  Enter a single state district to restrict results.
    :type p_stdist: str
    :param p_zip: 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    :type p_zip: str
    :param p_frs: Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    :type p_frs: str
    :param p_reg: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_reg: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    :type p_sic: str
    :param p_ncs: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_ncs: str
    :param p_pen: Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    :type p_pen: str
    :param p_c1lat: In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lat: 
    :param p_c1lon: In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lon: 
    :param p_c2lat: In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lat: 
    :param p_c2lon: In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lon: 
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_sic2: Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc.
    :type p_sic2: str
    :param p_sic4: Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    :type p_sic4: str
    :param p_fa: Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    :type p_fa: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    :type p_act: str
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
    :param p_cmps: RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
    :type p_cmps: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_olr: Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases.
    :type p_olr: str
    :param p_oct: Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases.
    :type p_oct: str
    :param p_trichem: 
    :type p_trichem: str
    :param p_tri_lr_pol: 
    :type p_tri_lr_pol: str
    :param p_tri_lr_yr: 
    :type p_tri_lr_yr: str
    :param p_tri_lr_amt: 
    :type p_tri_lr_amt: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA
    :type p_med: str
    :param p_owc: 
    :type p_owc: str
    :param p_owd: 
    :type p_owd: str
    :param p_opc: 
    :type p_opc: str
    :param p_opd: 
    :type p_opd: str
    :param p_ysl: Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_ysl: str
    :param p_ysly: Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    :type p_ysly: 
    :param p_ysla: Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State
    :type p_ysla: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_sfs: Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    :type p_sfs: str
    :param p_tribeid: Numeric code for tribe (or list of tribes).
    :type p_tribeid: 
    :param p_tribename: Tribe Name Filter.  Enter a single tribe name to filter results.
    :type p_tribename: str
    :param p_tribedist: Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    :type p_tribedist: 
    :param p_owop: Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
    :type p_owop: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values.
    :type p_pityp: str
    :param p_cifdi: Compliance issuess found during inspection.
    :type p_cifdi: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_violy: Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
    :type p_violy: 
    :param p_ncv: Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
    :type p_ncv: str
    :param p_fcv: Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
    :type p_fcv: str
    :param p_violt: RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violt: str
    :param p_des: Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\&quot;TSDF\\\&quot; to return the full enforcement TSDF universe and \\\&quot;Operating TSDF\\\&quot; to return the operating TSDF universe.
    :type p_des: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_decouple: Decouple Inspection Code Search Flag.  Enter \\\&quot;Y\\\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    :type p_decouple: str
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param tablelist: Table List Flag. Enter a Y to display the first page of facility results.
    :type tablelist: str
    :param maplist: Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    :type maplist: str
    :param summarylist: Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    :type summarylist: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def rcra_rest_services_get_facility_info_get(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_stdist=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, xmin=None, ymin=None, xmax=None, ymax=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_act=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_cmps=None, p_law=None, p_section=None, p_qiv=None, p_impw=None, p_trep=None, p_olr=None, p_oct=None, p_trichem=None, p_tri_lr_pol=None, p_tri_lr_yr=None, p_tri_lr_amt=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_wbd=None, p_pid=None, p_med=None, p_owc=None, p_owd=None, p_opc=None, p_opd=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_owop=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_cifdi=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_psncq=None, p_dwd=None, p_violy=None, p_ncv=None, p_fcv=None, p_violt=None, p_des=None, p_fntype=None, p_pidall=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_decouple=None, p_ejscreen_over80cnt=None, queryset=None, responseset=None, summarylist=None, param_callback=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Facility Enhanced Search Service

    Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. - CSV &#x3D; Facility results formatted as comma delimited file download. - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection. - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param p_fn: Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    :type p_fn: str
    :param p_sa: Facility street address. Enter a complete or partial street address.
    :type p_sa: str
    :param p_sa1: Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    :type p_sa1: str
    :param p_ct: Facility City Filter. Enter a single case-insensitive city name to filter results.
    :type p_ct: str
    :param p_co: Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    :type p_co: str
    :param p_fips: FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    :type p_fips: str
    :param p_st: Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    :type p_st: str
    :param p_stdist: State District Filter.  Enter a single state district to restrict results.
    :type p_stdist: str
    :param p_zip: 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    :type p_zip: str
    :param p_frs: Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    :type p_frs: str
    :param p_reg: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_reg: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    :type p_sic: str
    :param p_ncs: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_ncs: str
    :param p_pen: Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    :type p_pen: str
    :param xmin: Minimum longitude value in decimal degrees.
    :type xmin: 
    :param ymin: Minimum latitude value in decimal degrees.
    :type ymin: 
    :param xmax: Maximum longitude value in decimal degrees.
    :type xmax: 
    :param ymax: Maximum latitude value in decimal degrees.
    :type ymax: 
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_sic2: Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc.
    :type p_sic2: str
    :param p_sic4: Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    :type p_sic4: str
    :param p_fa: Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    :type p_fa: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    :type p_act: str
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
    :param p_cmps: RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
    :type p_cmps: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_olr: Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases.
    :type p_olr: str
    :param p_oct: Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases.
    :type p_oct: str
    :param p_trichem: 
    :type p_trichem: str
    :param p_tri_lr_pol: 
    :type p_tri_lr_pol: str
    :param p_tri_lr_yr: 
    :type p_tri_lr_yr: str
    :param p_tri_lr_amt: 
    :type p_tri_lr_amt: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA
    :type p_med: str
    :param p_owc: 
    :type p_owc: str
    :param p_owd: 
    :type p_owd: str
    :param p_opc: 
    :type p_opc: str
    :param p_opd: 
    :type p_opd: str
    :param p_ysl: Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_ysl: str
    :param p_ysly: Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    :type p_ysly: 
    :param p_ysla: Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State
    :type p_ysla: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_sfs: Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    :type p_sfs: str
    :param p_tribeid: Numeric code for tribe (or list of tribes).
    :type p_tribeid: 
    :param p_tribename: Tribe Name Filter.  Enter a single tribe name to filter results.
    :type p_tribename: str
    :param p_tribedist: Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    :type p_tribedist: 
    :param p_owop: Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
    :type p_owop: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values.
    :type p_pityp: str
    :param p_cifdi: Compliance issuess found during inspection.
    :type p_cifdi: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_violy: Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
    :type p_violy: 
    :param p_ncv: Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
    :type p_ncv: str
    :param p_fcv: Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
    :type p_fcv: str
    :param p_violt: RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violt: str
    :param p_des: Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \&quot;TSDF\&quot; to return the full enforcement TSDF universe and \&quot;Operating TSDF\&quot; to return the operating TSDF universe.
    :type p_des: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_decouple: Decouple Inspection Code Search Flag.  Enter \&quot;Y\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    :type p_decouple: str
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param summarylist: Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    :type summarylist: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_facility_info_post(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_stdist=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, xmin=None, ymin=None, xmax=None, ymax=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_act=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_cmps=None, p_law=None, p_section=None, p_qiv=None, p_impw=None, p_trep=None, p_olr=None, p_oct=None, p_trichem=None, p_tri_lr_pol=None, p_tri_lr_yr=None, p_tri_lr_amt=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_wbd=None, p_pid=None, p_med=None, p_owc=None, p_owd=None, p_opc=None, p_opd=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_owop=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_cifdi=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_psncq=None, p_dwd=None, p_violy=None, p_ncv=None, p_fcv=None, p_violt=None, p_des=None, p_fntype=None, p_pidall=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_decouple=None, p_ejscreen_over80cnt=None, queryset=None, responseset=None, summarylist=None, param_callback=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Facility Enhanced Search Service

    Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. - CSV &#x3D; Facility results formatted as comma delimited file download. - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection. - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param p_fn: Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
    :type p_fn: str
    :param p_sa: Facility street address. Enter a complete or partial street address.
    :type p_sa: str
    :param p_sa1: Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
    :type p_sa1: str
    :param p_ct: Facility City Filter. Enter a single case-insensitive city name to filter results.
    :type p_ct: str
    :param p_co: Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
    :type p_co: str
    :param p_fips: FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
    :type p_fips: str
    :param p_st: Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
    :type p_st: str
    :param p_stdist: State District Filter.  Enter a single state district to restrict results.
    :type p_stdist: str
    :param p_zip: 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
    :type p_zip: str
    :param p_frs: Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
    :type p_frs: str
    :param p_reg: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_reg: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
    :type p_sic: str
    :param p_ncs: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_ncs: str
    :param p_pen: Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
    :type p_pen: str
    :param xmin: Minimum longitude value in decimal degrees.
    :type xmin: 
    :param ymin: Minimum latitude value in decimal degrees.
    :type ymin: 
    :param xmax: Maximum longitude value in decimal degrees.
    :type xmax: 
    :param ymax: Maximum latitude value in decimal degrees.
    :type ymax: 
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_sic2: Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc.
    :type p_sic2: str
    :param p_sic4: Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
    :type p_sic4: str
    :param p_fa: Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
    :type p_fa: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
    :type p_act: str
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
    :param p_cmps: RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
    :type p_cmps: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_olr: Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases.
    :type p_olr: str
    :param p_oct: Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases.
    :type p_oct: str
    :param p_trichem: 
    :type p_trichem: str
    :param p_tri_lr_pol: 
    :type p_tri_lr_pol: str
    :param p_tri_lr_yr: 
    :type p_tri_lr_yr: str
    :param p_tri_lr_amt: 
    :type p_tri_lr_amt: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA
    :type p_med: str
    :param p_owc: 
    :type p_owc: str
    :param p_owd: 
    :type p_owd: str
    :param p_opc: 
    :type p_opc: str
    :param p_opd: 
    :type p_opd: str
    :param p_ysl: Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range
    :type p_ysl: str
    :param p_ysly: Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
    :type p_ysly: 
    :param p_ysla: Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State
    :type p_ysla: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_sfs: Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
    :type p_sfs: str
    :param p_tribeid: Numeric code for tribe (or list of tribes).
    :type p_tribeid: 
    :param p_tribename: Tribe Name Filter.  Enter a single tribe name to filter results.
    :type p_tribename: str
    :param p_tribedist: Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
    :type p_tribedist: 
    :param p_owop: Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
    :type p_owop: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values.
    :type p_pityp: str
    :param p_cifdi: Compliance issuess found during inspection.
    :type p_cifdi: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_violy: Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
    :type p_violy: 
    :param p_ncv: Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
    :type p_ncv: str
    :param p_fcv: Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
    :type p_fcv: str
    :param p_violt: RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violt: str
    :param p_des: Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\&quot;TSDF\\\&quot; to return the full enforcement TSDF universe and \\\&quot;Operating TSDF\\\&quot; to return the operating TSDF universe.
    :type p_des: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_decouple: Decouple Inspection Code Search Flag.  Enter \\\&quot;Y\\\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
    :type p_decouple: str
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param summarylist: Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
    :type summarylist: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_geojson_get(request: web.Request, qid, output=None, param_callback=None, newsort=None, descending=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) GeoJSON Service

    Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection (default). - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param newsort: Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    :type newsort: 
    :param descending: Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    :type descending: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_geojson_post(request: web.Request, qid, output=None, param_callback=None, newsort=None, descending=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) GeoJSON Service

    Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection (default). - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param newsort: Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    :type newsort: 
    :param descending: Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    :type descending: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_info_clusters_get(request: web.Request, p_qid, output=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Info Clusters Service

    Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

    :param p_qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type p_qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_info_clusters_post(request: web.Request, p_qid, output=None, p_pretty_print=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Info Clusters Service

    Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

    :param p_qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type p_qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_map_get(request: web.Request, qid, p_id, output=None, param_callback=None, tablelist=None, c1_lat=None, c1_long=None, c2_lat=None, c2_long=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Map Service

    The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param tablelist: Table List Flag. Enter a Y to display the first page of facility results.
    :type tablelist: str
    :param c1_lat: Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c1_lat: 
    :param c1_long: Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c1_long: 
    :param c2_lat: Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c2_lat: 
    :param c2_long: Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c2_long: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_map_post(request: web.Request, qid, p_id, output=None, param_callback=None, tablelist=None, c1_lat=None, c1_long=None, c2_lat=None, c2_long=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Map Service

    The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param tablelist: Table List Flag. Enter a Y to display the first page of facility results.
    :type tablelist: str
    :param c1_lat: Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c1_lat: 
    :param c1_long: Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c1_long: 
    :param c2_lat: Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c2_lat: 
    :param c2_long: Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type c2_long: 

    """
    return web.Response(status=200)


async def rcra_rest_services_get_qid_get(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Paginated Results Service

    GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

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


async def rcra_rest_services_get_qid_post(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Resource Conservation and Recovery Act (RCRA) Paginated Results Service

    GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

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

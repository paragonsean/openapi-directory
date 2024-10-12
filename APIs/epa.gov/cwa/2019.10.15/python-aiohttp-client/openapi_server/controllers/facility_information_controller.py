from typing import List, Dict
from aiohttp import web

from openapi_server.models.cwa_rest_services_get_facilities_get200_response import CwaRestServicesGetFacilitiesGet200Response
from openapi_server.models.cwa_rest_services_get_facility_info_get200_response import CwaRestServicesGetFacilityInfoGet200Response
from openapi_server.models.cwa_rest_services_get_geojson_get200_response import CwaRestServicesGetGeojsonGet200Response
from openapi_server.models.cwa_rest_services_get_map_get200_response import CwaRestServicesGetMapGet200Response
from openapi_server.models.cwa_rest_services_get_qid_get200_response import CwaRestServicesGetQidGet200Response
from openapi_server import util


async def cwa_rest_services_get_download_get(request: web.Request, qid, output=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Clean Water Act (CWA) Download Data Service

    Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default).
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def cwa_rest_services_get_download_post(request: web.Request, qid, output=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Clean Water Act (CWA) Download Data Service

    Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default).
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def cwa_rest_services_get_facilities_get(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_ff=None, p_act=None, p_maj=None, p_mact=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_qiv=None, p_iv=None, p_impw=None, p_imp_cau_grp=None, p_imp_pol=None, p_trep=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_pid=None, p_med=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_pstat=None, p_ptype=None, p_pcomp=None, p_plimits=None, p_pcss=None, p_pexp=None, p_owop=None, p_ipfti=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_pccs=None, p_pexcd=None, p_psncq=None, p_pctrack=None, p_dwd=None, p_pt=None, p_pdwdist=None, p_pswdpc=None, p_pswdmp=None, p_pswpol=None, p_pswcas=None, p_pswparam=None, p_pswvio=None, p_wbd=None, p_radwbd=None, p_frswbd=None, p_fntype=None, p_pidall=None, p_months_last_dmr=None, p_last_dmr_within=None, p_indsw=None, p_msgp_ptype=None, p_mon_type=None, p_iagency=None, p_permitting_agency=None, p_isws=None, p_iswss=None, p_iswss_id=None, p_ds1=None, p_ds2=None, p_da1=None, p_da2=None, p_ms4=None, p_oo_fn=None, p_oo_f_ntype=None, p_oo_sa=None, p_oo_sa1=None, p_oo_ct=None, p_oo_st=None, p_oo_zip=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_alrexceed=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_ejscreen_over80cnt=None, p_bio_flag=None, p_bio_fac_type=None, p_bio_trtmnt_procs=None, p_bio_analy_method_catgry=None, p_bio_total_volume_amt=None, p_bio_mgmt_prctce_type=None, p_bio_mgmt_prctce_stype=None, p_bio_mgmt_prctce_handler=None, p_bio_mgmt_container=None, p_bio_mgmt_pathogen=None, p_bio_mgmt_pathred=None, p_bio_mgmt_vector=None, p_bio_mgmt_def_category=None, p_bio_mgmt_deficiencies=None, p_bio_vio_code=None, p_bio_current_vio=None, p_bio_qtrs_in_vio=None, p_bio_rpt_year=None, p_bio_vio_last_year=None, p_msgp_rpt_year=None, p_vio_last_year=None, queryset=None, responseset=None, tablelist=None, maplist=None, summarylist=None, param_callback=None, qcolumns=None, p_e90_count=None, p_e90_years=None, p_psc=None) -> web.Response:
    """Clean Water Act (CWA) Facility Search Service

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
    :param p_ff: Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    :type p_ff: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    :type p_act: str
    :param p_maj: Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    :type p_maj: str
    :param p_mact: CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    :type p_mact: str
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
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_iv: Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    :type p_iv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_imp_cau_grp: Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    :type p_imp_cau_grp: str
    :param p_imp_pol: Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    :type p_imp_pol: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water
    :type p_med: str
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
    :param p_pstat: Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued
    :type p_pstat: str
    :param p_ptype: Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility
    :type p_ptype: str
    :param p_pcomp: Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction
    :type p_pcomp: str
    :param p_plimits: Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    :type p_plimits: str
    :param p_pcss: Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows.
    :type p_pcss: str
    :param p_pexp: Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago.
    :type p_pexp: str
    :param p_owop: Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \&quot;non-municipals\&quot; or \&quot;industrials\&quot;.
    :type p_owop: str
    :param p_ipfti: 
    :type p_ipfti: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    :type p_pityp: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_pccs: Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values.
    :type p_pccs: str
    :param p_pexcd: 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances
    :type p_pexcd: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_pctrack: Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    :type p_pctrack: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_pt: POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    :type p_pt: str
    :param p_pdwdist: Distance (in miles) to downstream drinking water intake.
    :type p_pdwdist: str
    :param p_pswdpc: Pollutant Category Code:  Values: WTR for Water, AIR for Air
    :type p_pswdpc: str
    :param p_pswdmp: Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    :type p_pswdmp: str
    :param p_pswpol: For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    :type p_pswpol: str
    :param p_pswcas: CAS numbers for surface water discharges. May contain multiple comma-separated values.
    :type p_pswcas: str
    :param p_pswparam: Parameter codes for surface water discharges. May contain multiple comma-separated values.
    :type p_pswparam: str
    :param p_pswvio: Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    :type p_pswvio: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_radwbd: 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \&quot;reach indexing\&quot; NPDES permits against the medium resolution National Hydrography Dataset. 
    :type p_radwbd: str
    :param p_frswbd: Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_frswbd: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_months_last_dmr: The number of months since the last Discharge Monitoring Report has been submitted.
    :type p_months_last_dmr: 
    :param p_last_dmr_within: W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    :type p_last_dmr_within: str
    :param p_indsw: Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_indsw: str
    :param p_msgp_ptype: Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification
    :type p_msgp_ptype: str
    :param p_mon_type: For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    :type p_mon_type: str
    :param p_iagency: Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \&quot;State\&quot; or \&quot;EPA\&quot;.
    :type p_iagency: str
    :param p_permitting_agency: 
    :type p_permitting_agency: str
    :param p_isws: Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    :type p_isws: str
    :param p_iswss: Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    :type p_iswss: str
    :param p_iswss_id: Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    :type p_iswss_id: str
    :param p_ds1: Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    :type p_ds1: str
    :param p_ds2: Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    :type p_ds2: str
    :param p_da1: Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    :type p_da1: str
    :param p_da2: Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    :type p_da2: str
    :param p_ms4: Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_ms4: str
    :param p_oo_fn: Owner/Operator Name. Enter the owner/operator name of the facility.
    :type p_oo_fn: str
    :param p_oo_f_ntype: Owner/Operator Name Multiple Selection Evaluator.  
    :type p_oo_f_ntype: str
    :param p_oo_sa: Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    :type p_oo_sa: str
    :param p_oo_sa1: Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    :type p_oo_sa1: str
    :param p_oo_ct: Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    :type p_oo_ct: str
    :param p_oo_st: Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    :type p_oo_st: str
    :param p_oo_zip: Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    :type p_oo_zip: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_alrexceed: Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    :type p_alrexceed: 
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param p_bio_flag: A Y value will select all biosolid-related permits.
    :type p_bio_flag: str
    :param p_bio_fac_type: The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above
    :type p_bio_fac_type: str
    :param p_bio_trtmnt_procs: The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\&quot;
    :type p_bio_trtmnt_procs: str
    :param p_bio_analy_method_catgry: The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes
    :type p_bio_analy_method_catgry: str
    :param p_bio_total_volume_amt: Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000
    :type p_bio_total_volume_amt: str
    :param p_bio_mgmt_prctce_type: The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal
    :type p_bio_mgmt_prctce_type: str
    :param p_bio_mgmt_prctce_stype: This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    :type p_bio_mgmt_prctce_stype: str
    :param p_bio_mgmt_prctce_handler: This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer
    :type p_bio_mgmt_prctce_handler: str
    :param p_bio_mgmt_container: The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container
    :type p_bio_mgmt_container: str
    :param p_bio_mgmt_pathogen: This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration)
    :type p_bio_mgmt_pathogen: str
    :param p_bio_mgmt_pathred: This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage)
    :type p_bio_mgmt_pathred: str
    :param p_bio_mgmt_vector: The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    :type p_bio_mgmt_vector: str
    :param p_bio_mgmt_def_category: This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal
    :type p_bio_mgmt_def_category: str
    :param p_bio_mgmt_deficiencies: The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    :type p_bio_mgmt_deficiencies: 
    :param p_bio_vio_code: The Biosolids Single Event Violation Code.  Enter one or mode codes.
    :type p_bio_vio_code: str
    :param p_bio_current_vio: Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No
    :type p_bio_current_vio: str
    :param p_bio_qtrs_in_vio: The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    :type p_bio_qtrs_in_vio: 
    :param p_bio_rpt_year: The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    :type p_bio_rpt_year: str
    :param p_bio_vio_last_year: Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    :type p_bio_vio_last_year: str
    :param p_msgp_rpt_year: The last year that a MSGP report was submitted for the permit.  Valid values are \&quot;NONE\&quot; and any year Greater or Eqal to 2015.
    :type p_msgp_rpt_year: str
    :param p_vio_last_year: Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    :type p_vio_last_year: str
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
    :param p_e90_count: Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value.
    :type p_e90_count: 
    :param p_e90_years: Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    :type p_e90_years: 
    :param p_psc: Point Source Category.
    :type p_psc: str

    """
    return web.Response(status=200)


async def cwa_rest_services_get_facilities_post(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_ff=None, p_act=None, p_maj=None, p_mact=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_qiv=None, p_iv=None, p_impw=None, p_imp_cau_grp=None, p_imp_pol=None, p_trep=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_pid=None, p_med=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_pstat=None, p_ptype=None, p_pcomp=None, p_plimits=None, p_pcss=None, p_pexp=None, p_owop=None, p_ipfti=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_pccs=None, p_pexcd=None, p_psncq=None, p_pctrack=None, p_dwd=None, p_pt=None, p_pdwdist=None, p_pswdpc=None, p_pswdmp=None, p_pswpol=None, p_pswcas=None, p_pswparam=None, p_pswvio=None, p_wbd=None, p_radwbd=None, p_frswbd=None, p_fntype=None, p_pidall=None, p_months_last_dmr=None, p_last_dmr_within=None, p_indsw=None, p_msgp_ptype=None, p_mon_type=None, p_iagency=None, p_permitting_agency=None, p_isws=None, p_iswss=None, p_iswss_id=None, p_ds1=None, p_ds2=None, p_da1=None, p_da2=None, p_ms4=None, p_oo_fn=None, p_oo_f_ntype=None, p_oo_sa=None, p_oo_sa1=None, p_oo_ct=None, p_oo_st=None, p_oo_zip=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_alrexceed=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_ejscreen_over80cnt=None, p_bio_flag=None, p_bio_fac_type=None, p_bio_trtmnt_procs=None, p_bio_analy_method_catgry=None, p_bio_total_volume_amt=None, p_bio_mgmt_prctce_type=None, p_bio_mgmt_prctce_stype=None, p_bio_mgmt_prctce_handler=None, p_bio_mgmt_container=None, p_bio_mgmt_pathogen=None, p_bio_mgmt_pathred=None, p_bio_mgmt_vector=None, p_bio_mgmt_def_category=None, p_bio_mgmt_deficiencies=None, p_bio_vio_code=None, p_bio_current_vio=None, p_bio_qtrs_in_vio=None, p_bio_rpt_year=None, p_bio_vio_last_year=None, p_msgp_rpt_year=None, p_vio_last_year=None, queryset=None, responseset=None, tablelist=None, maplist=None, summarylist=None, param_callback=None, qcolumns=None, p_e90_count=None, p_e90_years=None, p_psc=None) -> web.Response:
    """Clean Water Act (CWA) Facility Search Service

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
    :param p_ff: Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    :type p_ff: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    :type p_act: str
    :param p_maj: Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    :type p_maj: str
    :param p_mact: CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    :type p_mact: str
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
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_iv: Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    :type p_iv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_imp_cau_grp: Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    :type p_imp_cau_grp: str
    :param p_imp_pol: Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    :type p_imp_pol: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water
    :type p_med: str
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
    :param p_pstat: Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued
    :type p_pstat: str
    :param p_ptype: Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility
    :type p_ptype: str
    :param p_pcomp: Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction
    :type p_pcomp: str
    :param p_plimits: Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    :type p_plimits: str
    :param p_pcss: Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows.
    :type p_pcss: str
    :param p_pexp: Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago.
    :type p_pexp: str
    :param p_owop: Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \\\&quot;non-municipals\\\&quot; or \\\&quot;industrials\\\&quot;.
    :type p_owop: str
    :param p_ipfti: 
    :type p_ipfti: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    :type p_pityp: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_pccs: Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values.
    :type p_pccs: str
    :param p_pexcd: 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances
    :type p_pexcd: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_pctrack: Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    :type p_pctrack: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_pt: POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    :type p_pt: str
    :param p_pdwdist: Distance (in miles) to downstream drinking water intake.
    :type p_pdwdist: str
    :param p_pswdpc: Pollutant Category Code:  Values: WTR for Water, AIR for Air
    :type p_pswdpc: str
    :param p_pswdmp: Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    :type p_pswdmp: str
    :param p_pswpol: For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    :type p_pswpol: str
    :param p_pswcas: CAS numbers for surface water discharges. May contain multiple comma-separated values.
    :type p_pswcas: str
    :param p_pswparam: Parameter codes for surface water discharges. May contain multiple comma-separated values.
    :type p_pswparam: str
    :param p_pswvio: Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    :type p_pswvio: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_radwbd: 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \\\&quot;reach indexing\\\&quot; NPDES permits against the medium resolution National Hydrography Dataset. 
    :type p_radwbd: str
    :param p_frswbd: Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_frswbd: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_months_last_dmr: The number of months since the last Discharge Monitoring Report has been submitted.
    :type p_months_last_dmr: 
    :param p_last_dmr_within: W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    :type p_last_dmr_within: str
    :param p_indsw: Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_indsw: str
    :param p_msgp_ptype: Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification
    :type p_msgp_ptype: str
    :param p_mon_type: For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    :type p_mon_type: str
    :param p_iagency: Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \\\&quot;State\\\&quot; or \\\&quot;EPA\\\&quot;.
    :type p_iagency: str
    :param p_permitting_agency: 
    :type p_permitting_agency: str
    :param p_isws: Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    :type p_isws: str
    :param p_iswss: Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    :type p_iswss: str
    :param p_iswss_id: Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    :type p_iswss_id: str
    :param p_ds1: Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    :type p_ds1: str
    :param p_ds2: Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    :type p_ds2: str
    :param p_da1: Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    :type p_da1: str
    :param p_da2: Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    :type p_da2: str
    :param p_ms4: Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_ms4: str
    :param p_oo_fn: Owner/Operator Name. Enter the owner/operator name of the facility.
    :type p_oo_fn: str
    :param p_oo_f_ntype: Owner/Operator Name Multiple Selection Evaluator.  
    :type p_oo_f_ntype: str
    :param p_oo_sa: Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    :type p_oo_sa: str
    :param p_oo_sa1: Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    :type p_oo_sa1: str
    :param p_oo_ct: Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    :type p_oo_ct: str
    :param p_oo_st: Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    :type p_oo_st: str
    :param p_oo_zip: Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    :type p_oo_zip: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_alrexceed: Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    :type p_alrexceed: 
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param p_bio_flag: A Y value will select all biosolid-related permits.
    :type p_bio_flag: str
    :param p_bio_fac_type: The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above
    :type p_bio_fac_type: str
    :param p_bio_trtmnt_procs: The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\\\&quot;
    :type p_bio_trtmnt_procs: str
    :param p_bio_analy_method_catgry: The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes
    :type p_bio_analy_method_catgry: str
    :param p_bio_total_volume_amt: Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000
    :type p_bio_total_volume_amt: str
    :param p_bio_mgmt_prctce_type: The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal
    :type p_bio_mgmt_prctce_type: str
    :param p_bio_mgmt_prctce_stype: This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    :type p_bio_mgmt_prctce_stype: str
    :param p_bio_mgmt_prctce_handler: This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer
    :type p_bio_mgmt_prctce_handler: str
    :param p_bio_mgmt_container: The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container
    :type p_bio_mgmt_container: str
    :param p_bio_mgmt_pathogen: This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration)
    :type p_bio_mgmt_pathogen: str
    :param p_bio_mgmt_pathred: This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage)
    :type p_bio_mgmt_pathred: str
    :param p_bio_mgmt_vector: The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    :type p_bio_mgmt_vector: str
    :param p_bio_mgmt_def_category: This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal
    :type p_bio_mgmt_def_category: str
    :param p_bio_mgmt_deficiencies: The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    :type p_bio_mgmt_deficiencies: 
    :param p_bio_vio_code: The Biosolids Single Event Violation Code.  Enter one or mode codes.
    :type p_bio_vio_code: str
    :param p_bio_current_vio: Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No
    :type p_bio_current_vio: str
    :param p_bio_qtrs_in_vio: The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    :type p_bio_qtrs_in_vio: 
    :param p_bio_rpt_year: The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    :type p_bio_rpt_year: str
    :param p_bio_vio_last_year: Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    :type p_bio_vio_last_year: str
    :param p_msgp_rpt_year: The last year that a MSGP report was submitted for the permit.  Valid values are \\\&quot;NONE\\\&quot; and any year Greater or Eqal to 2015.
    :type p_msgp_rpt_year: str
    :param p_vio_last_year: Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    :type p_vio_last_year: str
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
    :param p_e90_count: Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value.
    :type p_e90_count: 
    :param p_e90_years: Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    :type p_e90_years: 
    :param p_psc: Point Source Category.
    :type p_psc: str

    """
    return web.Response(status=200)


async def cwa_rest_services_get_facility_info_get(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, xmin=None, ymin=None, xmax=None, ymax=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_ff=None, p_act=None, p_maj=None, p_mact=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_qiv=None, p_iv=None, p_impw=None, p_imp_pol=None, p_imp_cau_grp=None, p_trep=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_pid=None, p_med=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_pstat=None, p_ptype=None, p_pcomp=None, p_plimits=None, p_pcss=None, p_pexp=None, p_owop=None, p_ipfti=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_pccs=None, p_pexcd=None, p_psncq=None, p_pctrack=None, p_dwd=None, p_pt=None, p_pdwdist=None, p_pswdpc=None, p_pswdmp=None, p_pswpol=None, p_pswcas=None, p_pswparam=None, p_pswvio=None, p_wbd=None, p_radwbd=None, p_frswbd=None, p_fntype=None, p_pidall=None, p_months_last_dmr=None, p_last_dmr_within=None, p_indsw=None, p_msgp_ptype=None, p_mon_type=None, p_iagency=None, p_permitting_agency=None, p_isws=None, p_iswss=None, p_iswss_id=None, p_ds1=None, p_ds2=None, p_da1=None, p_da2=None, p_ms4=None, p_oo_fn=None, p_oo_f_ntype=None, p_oo_sa=None, p_oo_sa1=None, p_oo_ct=None, p_oo_st=None, p_oo_zip=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_alrexceed=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_ejscreen_over80cnt=None, p_bio_flag=None, p_bio_fac_type=None, p_bio_trtmnt_procs=None, p_bio_analy_method_catgry=None, p_bio_total_volume_amt=None, p_bio_mgmt_prctce_type=None, p_bio_mgmt_prctce_stype=None, p_bio_mgmt_prctce_handler=None, p_bio_mgmt_container=None, p_bio_mgmt_pathogen=None, p_bio_mgmt_pathred=None, p_bio_mgmt_vector=None, p_bio_mgmt_def_category=None, p_bio_mgmt_deficiencies=None, p_bio_vio_code=None, p_bio_current_vio=None, p_bio_qtrs_in_vio=None, p_bio_rpt_year=None, p_bio_vio_last_year=None, p_msgp_rpt_year=None, p_vio_last_year=None, responseset=None, param_callback=None, qcolumns=None, p_pretty_print=None, p_e90_count=None, p_e90_years=None, p_psc=None) -> web.Response:
    """Clean Water Act (CWA) Facility Enhanced Search Service

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
    :param p_ff: Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    :type p_ff: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    :type p_act: str
    :param p_maj: Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    :type p_maj: str
    :param p_mact: CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    :type p_mact: str
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
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_iv: Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    :type p_iv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_imp_pol: Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    :type p_imp_pol: str
    :param p_imp_cau_grp: Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    :type p_imp_cau_grp: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water
    :type p_med: str
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
    :param p_pstat: Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued
    :type p_pstat: str
    :param p_ptype: Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility
    :type p_ptype: str
    :param p_pcomp: Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction
    :type p_pcomp: str
    :param p_plimits: Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    :type p_plimits: str
    :param p_pcss: Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows.
    :type p_pcss: str
    :param p_pexp: Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago.
    :type p_pexp: str
    :param p_owop: Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \&quot;non-municipals\&quot; or \&quot;industrials\&quot;.
    :type p_owop: str
    :param p_ipfti: 
    :type p_ipfti: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    :type p_pityp: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_pccs: Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values.
    :type p_pccs: str
    :param p_pexcd: 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances
    :type p_pexcd: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_pctrack: Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    :type p_pctrack: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_pt: POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    :type p_pt: str
    :param p_pdwdist: Distance (in miles) to downstream drinking water intake.
    :type p_pdwdist: str
    :param p_pswdpc: Pollutant Category Code:  Values: WTR for Water, AIR for Air
    :type p_pswdpc: str
    :param p_pswdmp: Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    :type p_pswdmp: str
    :param p_pswpol: For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    :type p_pswpol: str
    :param p_pswcas: CAS numbers for surface water discharges. May contain multiple comma-separated values.
    :type p_pswcas: str
    :param p_pswparam: Parameter codes for surface water discharges. May contain multiple comma-separated values.
    :type p_pswparam: str
    :param p_pswvio: Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    :type p_pswvio: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_radwbd: 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \&quot;reach indexing\&quot; NPDES permits against the medium resolution National Hydrography Dataset. 
    :type p_radwbd: str
    :param p_frswbd: Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_frswbd: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_months_last_dmr: The number of months since the last Discharge Monitoring Report has been submitted.
    :type p_months_last_dmr: 
    :param p_last_dmr_within: W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    :type p_last_dmr_within: str
    :param p_indsw: Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_indsw: str
    :param p_msgp_ptype: Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification
    :type p_msgp_ptype: str
    :param p_mon_type: For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    :type p_mon_type: str
    :param p_iagency: Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \&quot;State\&quot; or \&quot;EPA\&quot;.
    :type p_iagency: str
    :param p_permitting_agency: 
    :type p_permitting_agency: str
    :param p_isws: Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    :type p_isws: str
    :param p_iswss: Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    :type p_iswss: str
    :param p_iswss_id: Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    :type p_iswss_id: str
    :param p_ds1: Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    :type p_ds1: str
    :param p_ds2: Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    :type p_ds2: str
    :param p_da1: Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    :type p_da1: str
    :param p_da2: Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    :type p_da2: str
    :param p_ms4: Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_ms4: str
    :param p_oo_fn: Owner/Operator Name. Enter the owner/operator name of the facility.
    :type p_oo_fn: str
    :param p_oo_f_ntype: Owner/Operator Name Multiple Selection Evaluator.  
    :type p_oo_f_ntype: str
    :param p_oo_sa: Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    :type p_oo_sa: str
    :param p_oo_sa1: Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    :type p_oo_sa1: str
    :param p_oo_ct: Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    :type p_oo_ct: str
    :param p_oo_st: Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    :type p_oo_st: str
    :param p_oo_zip: Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    :type p_oo_zip: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_alrexceed: Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    :type p_alrexceed: 
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param p_bio_flag: A Y value will select all biosolid-related permits.
    :type p_bio_flag: str
    :param p_bio_fac_type: The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above
    :type p_bio_fac_type: str
    :param p_bio_trtmnt_procs: The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\&quot;
    :type p_bio_trtmnt_procs: str
    :param p_bio_analy_method_catgry: The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes
    :type p_bio_analy_method_catgry: str
    :param p_bio_total_volume_amt: Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000
    :type p_bio_total_volume_amt: str
    :param p_bio_mgmt_prctce_type: The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal
    :type p_bio_mgmt_prctce_type: str
    :param p_bio_mgmt_prctce_stype: This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    :type p_bio_mgmt_prctce_stype: str
    :param p_bio_mgmt_prctce_handler: This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer
    :type p_bio_mgmt_prctce_handler: str
    :param p_bio_mgmt_container: The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container
    :type p_bio_mgmt_container: str
    :param p_bio_mgmt_pathogen: This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration)
    :type p_bio_mgmt_pathogen: str
    :param p_bio_mgmt_pathred: This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage)
    :type p_bio_mgmt_pathred: str
    :param p_bio_mgmt_vector: The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    :type p_bio_mgmt_vector: str
    :param p_bio_mgmt_def_category: This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal
    :type p_bio_mgmt_def_category: str
    :param p_bio_mgmt_deficiencies: The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    :type p_bio_mgmt_deficiencies: 
    :param p_bio_vio_code: The Biosolids Single Event Violation Code.  Enter one or mode codes.
    :type p_bio_vio_code: str
    :param p_bio_current_vio: Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No
    :type p_bio_current_vio: str
    :param p_bio_qtrs_in_vio: The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    :type p_bio_qtrs_in_vio: 
    :param p_bio_rpt_year: The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    :type p_bio_rpt_year: str
    :param p_bio_vio_last_year: Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    :type p_bio_vio_last_year: str
    :param p_msgp_rpt_year: The last year that a MSGP report was submitted for the permit.  Valid values are \&quot;NONE\&quot; and any year Greater or Eqal to 2015.
    :type p_msgp_rpt_year: str
    :param p_vio_last_year: Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    :type p_vio_last_year: str
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 
    :param p_e90_count: Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value.
    :type p_e90_count: 
    :param p_e90_years: Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    :type p_e90_years: 
    :param p_psc: Point Source Category.
    :type p_psc: str

    """
    return web.Response(status=200)


async def cwa_rest_services_get_facility_info_post(request: web.Request, output=None, p_fn=None, p_sa=None, p_sa1=None, p_ct=None, p_co=None, p_fips=None, p_st=None, p_zip=None, p_frs=None, p_reg=None, p_sic=None, p_ncs=None, p_pen=None, xmin=None, ymin=None, xmax=None, ymax=None, p_usmex=None, p_sic2=None, p_sic4=None, p_fa=None, p_ff=None, p_act=None, p_maj=None, p_mact=None, p_fea=None, p_feay=None, p_feaa=None, p_iea=None, p_ieay=None, p_ieaa=None, p_qiv=None, p_iv=None, p_impw=None, p_imp_pol=None, p_imp_cau_grp=None, p_trep=None, p_pm=None, p_pd=None, p_ico=None, p_huc=None, p_pid=None, p_med=None, p_ysl=None, p_ysly=None, p_ysla=None, p_qs=None, p_sfs=None, p_tribeid=None, p_tribename=None, p_tribedist=None, p_pstat=None, p_ptype=None, p_pcomp=None, p_plimits=None, p_pcss=None, p_pexp=None, p_owop=None, p_ipfti=None, p_agoo=None, p_idt1=None, p_idt2=None, p_pityp=None, p_pfead1=None, p_pfead2=None, p_pfeat=None, p_pccs=None, p_pexcd=None, p_psncq=None, p_pctrack=None, p_dwd=None, p_pt=None, p_pdwdist=None, p_pswdpc=None, p_pswdmp=None, p_pswpol=None, p_pswcas=None, p_pswparam=None, p_pswvio=None, p_wbd=None, p_radwbd=None, p_frswbd=None, p_fntype=None, p_pidall=None, p_months_last_dmr=None, p_last_dmr_within=None, p_indsw=None, p_msgp_ptype=None, p_mon_type=None, p_iagency=None, p_permitting_agency=None, p_isws=None, p_iswss=None, p_iswss_id=None, p_ds1=None, p_ds2=None, p_da1=None, p_da2=None, p_ms4=None, p_oo_fn=None, p_oo_f_ntype=None, p_oo_sa=None, p_oo_sa1=None, p_oo_ct=None, p_oo_st=None, p_oo_zip=None, p_fac_ico=None, p_icoo=None, p_fac_icos=None, p_ejscreen=None, p_alrexceed=None, p_limit_addr=None, p_lat=None, p_long=None, p_radius=None, p_ejscreen_over80cnt=None, p_bio_flag=None, p_bio_fac_type=None, p_bio_trtmnt_procs=None, p_bio_analy_method_catgry=None, p_bio_total_volume_amt=None, p_bio_mgmt_prctce_type=None, p_bio_mgmt_prctce_stype=None, p_bio_mgmt_prctce_handler=None, p_bio_mgmt_container=None, p_bio_mgmt_pathogen=None, p_bio_mgmt_pathred=None, p_bio_mgmt_vector=None, p_bio_mgmt_def_category=None, p_bio_mgmt_deficiencies=None, p_bio_vio_code=None, p_bio_current_vio=None, p_bio_qtrs_in_vio=None, p_bio_rpt_year=None, p_bio_vio_last_year=None, p_msgp_rpt_year=None, p_vio_last_year=None, responseset=None, param_callback=None, qcolumns=None, p_pretty_print=None, p_e90_count=None, p_e90_years=None, p_psc=None) -> web.Response:
    """Clean Water Act (CWA) Facility Enhanced Search Service

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
    :param p_ff: Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
    :type p_ff: str
    :param p_act: Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.  A Y will select ICIS NPDES permits with a status of effective, continued, or expired.
    :type p_act: str
    :param p_maj: Major Facility Flag.  Enter Y to restrict results to Major facilities only.
    :type p_maj: str
    :param p_mact: CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
    :type p_mact: str
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
    :param p_qiv: Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance.
    :type p_qiv: str
    :param p_iv: Facility has a violation status of &#39;In Viol&#39; during any of the selected quarters.   Range: Fiscal Year 2020 Quarter 2 to Fiscal Year 2017 Quarter 2  Multiple values are comma delimited.   ||||||  Fiscal Years |||||| - FY2020 or FY20 or 2020 or 20 - FY2019 or FY19 or 2019 or 19 - FY2018 or FY18 or 2018 or 18 - FY2017 or FY17 or 2017 or 17  ||||| Fiscal Quarters ||||| - FY2020Q2 or FY20Q2 or 20202 or 202 or 13 - FY2020Q1 or FY20Q1 or 20201 or 201 or 12 - FY2019Q4 or FY19Q4 or 20194 or 194 or 11 - FY2019Q3 or FY19Q3 or 20193 or 193 or 10 - FY2019Q2 or FY19Q2 or 20192 or 192 or 9 - FY2019Q1 or FY19Q1 or 20191 or 191 or 8 - FY2018Q4 or FY18Q4 or 20184 or 184 or 7 - FY2018Q3 or FY18Q3 or 20183 or 183 or 6 - FY2018Q2 or FY18Q2 or 20182 or 182 or 5 - FY2018Q1 or FY18Q1 or 20181 or 181 or 4 - FY2017Q4 or FY17Q4 or 20174 or 174 or 3 - FY2017Q3 or FY17Q3 or 20173 or 173 or 2 - FY2017Q2 or FY17Q2 or 20172 or 172 or 1
    :type p_iv: str
    :param p_impw: Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
    :type p_impw: str
    :param p_imp_pol: Facility is discharging pollutants that are potentially contributing to the impairment of local waterbodies according to the ATTAINS database.
    :type p_imp_pol: str
    :param p_imp_cau_grp: Facility is discharging a pollutant group causing a waterbody to be impaired.  Enter 1 through 34 (the internal number of the pollutant group); or enter a partial name such as Dioxin,Temp,tUrBidity.
    :type p_imp_cau_grp: str
    :param p_trep: Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year.
    :type p_trep: str
    :param p_pm: Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75%
    :type p_pm: str
    :param p_pd: Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile
    :type p_pd: str
    :param p_ico: Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country.
    :type p_ico: str
    :param p_huc: 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
    :type p_huc: str
    :param p_pid: Nine-digit permit IDs. May contain up to 2000 comma-separated values.
    :type p_pid: str
    :param p_med: Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - ALL &#x3D; Air and RCRA and Water
    :type p_med: str
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
    :param p_pstat: Permit Status Filter.  Enter one or more of the following codes.  Provide multiple values as a comma-delimited list. - EFF &#x3D; Effective - EXP &#x3D; Expired - PND &#x3D; Pending - TRM &#x3D; Terminated - RET &#x3D; Retired - NON &#x3D; Not Needed - ADC &#x3D; Admin Continued
    :type p_pstat: str
    :param p_ptype: Permit Type Filter. Enter one or more code values to filter results.  Provide multiple values as a comma-delimited list. - NPD &#x3D; NPDES Individual Permit - NGP &#x3D; NPDES Master General Permit - GPC &#x3D; General Permit Covered Facility - SNN &#x3D; State Issued Master General Permit (Non-NPDES) - IIU &#x3D; Individual IU Permit (Non-NPDES) - SIN &#x3D; Individual State Issued Permit (Non-NPDES) - APR &#x3D; Associated Permit Record - UFT &#x3D; Unpermitted Facility
    :type p_ptype: str
    :param p_pcomp: Permit Component Code Filter.  Enter one or more codes to filter results.  Provide multiple values as a comma-delimited list. - PRE &#x3D; Pretreatment - CAF &#x3D; CAFO - CSO &#x3D; CSO - POT &#x3D; POTW - BIO &#x3D; Biosolids - SWS &#x3D; Storm Water Small MS4s - SWM &#x3D; Storm Water Medium/Large MS4s - SWI &#x3D; Storm Water Industrial - SWC &#x3D; Storm Water Construction
    :type p_pcomp: str
    :param p_plimits: Permit Limits Present Flag.  Enter Y to limit results to facilities have present permit limits.
    :type p_plimits: str
    :param p_pcss: Combined Sewer Systems Outflows Limiter.  Enter one of the following to limit results to facilities having the given count of CSS outflows. - ALL &#x3D; returns all facilities, regardless of the number of outflows. - GE1 &#x3D; returns facilities with one or more outflows. - GE10 &#x3D; returns facilities with ten or more outflows. - GE50 &#x3D; returns facilities with fifty or more outflows.
    :type p_pcss: str
    :param p_pexp: Permit Expired or Administratively Continued Limiter.  Enter one of the following values to filter results. - EXP &#x3D; limit results to facilities with permits expired or administratively continued. - EXPLE1YR &#x3D; limit resuls to facilities with permits expired administratively continued within the past year. - EXPGT1YR &#x3D; limit resuls to facilities with permits expired administratively continued more than a year ago.
    :type p_pexp: str
    :param p_owop: Owner/Operator code filter.  Enter one of the following values to restrict results. - Federal &#x3D; Federal facilities regulated under the NPDES program. - POTW &#x3D; Publicly owned treatment works. Treatment works that are owned by a State, Tribe, or municipality. - Non-POTW &#x3D; Non-publicly owned treatment works. Often referred to as \\\&quot;non-municipals\\\&quot; or \\\&quot;industrials\\\&quot;.
    :type p_owop: str
    :param p_ipfti: 
    :type p_ipfti: str
    :param p_agoo: Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
    :type p_agoo: str
    :param p_idt1: Beginning of date range of most recent facility inspection.
    :type p_idt1: str
    :param p_idt2: End of date range of most recent facility inspection.
    :type p_idt2: str
    :param p_pityp: Inspection Type Code.  See ICIS Compliance Monitor Types lookup serivce for a list of available codes and descriptions.
    :type p_pityp: str
    :param p_pfead1: Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead1: str
    :param p_pfead2: Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
    :type p_pfead2: str
    :param p_pfeat: Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
    :type p_pfeat: str
    :param p_pccs: Current Compliance Status: |||||||||||||||||||||||||||  Significant Noncompliance (SNC)  ||||||||||||||||||||||||||| - SNC &#x3D; E, S, X, T, D - E�&#x3D; E(EffViol) - S�&#x3D; S(CSchVio) - X &#x3D; X(EffNMth) - T &#x3D; T(CSchRpt) - D�&#x3D; D(DMR NR)  ||||||||||||||||||||||||||| Noncompliance (NC) ||||||||||||||||||||||||||| - NC &#x3D; N, V - N�&#x3D; N(RptViol) - V�&#x3D; V(NonRNCV)  ||||||||||||||||||||||||||| New Violations (PQV) ||||||||||||||||||||||||||| - PQV &#x3D; New Violations (13th Quarter)  ||||||||||||||||||||||||||| No Violations (NV) ||||||||||||||||||||||||||| - NV &#x3D; R, P, M, U, W , Blank, and No New Violations (no PQV) - R�&#x3D; R(Resolvd) - P�&#x3D; P(ResPend) - M�&#x3D; C(Manual) - U &#x3D; U(N/A) - W &#x3D; W(N/A) - Blank &#x3D; (null)  May contain multiple comma-separated values.
    :type p_pccs: str
    :param p_pexcd: 3-Year Effluent Exceedances Limiter.  Enter a value to restrict results to facilities with the given amount of exceedances in the past 3 years. - 0 &#x3D; facilities with no exceedances - GE0 &#x3D; facilities with one or more exceedances - GE10 &#x3D; facilities with ten or more exceedances - GE50 &#x3D; facilities with fifty or more exceedances - GE100 &#x3D; facilities with one hundred or more exceedances
    :type p_pexcd: str
    :param p_psncq: Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
    :type p_psncq: str
    :param p_pctrack: Compliance Tracking Limiter. Provide a keyword to indicate the extent to which data is being entered and effluent exceedances are being identified. - Off - Partial - On
    :type p_pctrack: str
    :param p_dwd: Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
    :type p_dwd: str
    :param p_pt: POTW Transfers. Pounds of toxic chemicals transferred to a Publicly Operated Treatment Works (POTW) as reported to the Toxics Release Inventory.
    :type p_pt: str
    :param p_pdwdist: Distance (in miles) to downstream drinking water intake.
    :type p_pdwdist: str
    :param p_pswdpc: Pollutant Category Code:  Values: WTR for Water, AIR for Air
    :type p_pswdpc: str
    :param p_pswdmp: Used to determine limit begin and end dates for surface water discharges. Number represents years from current date.
    :type p_pswdmp: str
    :param p_pswpol: For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
    :type p_pswpol: str
    :param p_pswcas: CAS numbers for surface water discharges. May contain multiple comma-separated values.
    :type p_pswcas: str
    :param p_pswparam: Parameter codes for surface water discharges. May contain multiple comma-separated values.
    :type p_pswparam: str
    :param p_pswvio: Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
    :type p_pswvio: str
    :param p_wbd: 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_wbd: str
    :param p_radwbd: 2-, 4-, 6-, 8-, 10-, or 12 character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Will search against WBD values otained by \\\&quot;reach indexing\\\&quot; NPDES permits against the medium resolution National Hydrography Dataset. 
    :type p_radwbd: str
    :param p_frswbd: Works exactly the same as the p_wbd parameter.  2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
    :type p_frswbd: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_pidall: Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
    :type p_pidall: str
    :param p_months_last_dmr: The number of months since the last Discharge Monitoring Report has been submitted.
    :type p_months_last_dmr: 
    :param p_last_dmr_within: W value returns facilities that have submitted DMRs within the number of months specified by p_months_last_dmr. An N value returns facilities that have not submitted a DMR within the specified number of months.
    :type p_last_dmr_within: str
    :param p_indsw: Industrial Stormwater Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_indsw: str
    :param p_msgp_ptype: Multi-Sector General Purpose Permit Type.  Enter a value to filter results by MSGP Permit Type. - NOI &#x3D; Notice of Intent - NOE &#x3D; No Exposure Certification
    :type p_msgp_ptype: str
    :param p_mon_type: For use with the Industrial Stormwater search only. Valid values are BENCHGS fro Benchmark (Alert Limit) G2 Ore, BENCH for Benchmark (Alert Limit), and ELG fro Effluent Limitation Guidelines(ELG)(Effluent Limit).  
    :type p_mon_type: str
    :param p_iagency: Issuing Agency Limiter.  Enter a single value to filter results by the issuing agency, e.g. \\\&quot;State\\\&quot; or \\\&quot;EPA\\\&quot;.
    :type p_iagency: str
    :param p_permitting_agency: 
    :type p_permitting_agency: str
    :param p_isws: Multi-Sector General Purpose Permit Subsector Individual Identifier.  Enter a value to filter results.
    :type p_isws: str
    :param p_iswss: Multi-Sector General Purpose Permit Subsector Group Code.  Enter a value to filter results.
    :type p_iswss: str
    :param p_iswss_id: Multi-Sector General Purpose Permit Sector Code.  Enter a value to filter results.
    :type p_iswss_id: str
    :param p_ds1: Submitted Date Filter Start.  To filter by the date of submission, enter a start date here and an end date in the p_ds2 parameter.  Both dates are required for filtering.
    :type p_ds1: str
    :param p_ds2: Submitted Date Filter End.  To filter by the date of submission, enter an end date here and a start date in the p_ds1 parameter.  Both dates are required for filtering.
    :type p_ds2: str
    :param p_da1: Active Date Filter Start.  To filter by the active date, enter a start date here and an end date in the p_da2 parameter.  Both dates are required for filtering.
    :type p_da1: str
    :param p_da2: Active Date Filter End.  To filter by the active date, enter an end date here and a start date in the p_da1 parameter.  Both dates are required for filtering.
    :type p_da2: str
    :param p_ms4: Municipal Separate Storm Water Sewer (MS4) Permit Flag.  Enter a Y or N to filter results by this type of permit.
    :type p_ms4: str
    :param p_oo_fn: Owner/Operator Name. Enter the owner/operator name of the facility.
    :type p_oo_fn: str
    :param p_oo_f_ntype: Owner/Operator Name Multiple Selection Evaluator.  
    :type p_oo_f_ntype: str
    :param p_oo_sa: Owner/Operator Address.  Enter the address of the owner/operator of the facility.
    :type p_oo_sa: str
    :param p_oo_sa1: Owner/Operator Address Line 2.  Enter the line 2 address of the owner/operator of the facility.
    :type p_oo_sa1: str
    :param p_oo_ct: Owner/Operator City. Enter the city where the owner/operator of the facility is located.
    :type p_oo_ct: str
    :param p_oo_st: Owner/Operator State.  Enter the standardized postal state code where the owner/operator of the facility is located.
    :type p_oo_st: str
    :param p_oo_zip: Owner/Operator Zip Code.  Enter the postal zip code where the owner/operator of the facility is located.
    :type p_oo_zip: str
    :param p_fac_ico: FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code.
    :type p_fac_ico: str
    :param p_icoo: Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
    :type p_icoo: str
    :param p_fac_icos: FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag.
    :type p_fac_icos: str
    :param p_ejscreen: Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
    :type p_ejscreen: str
    :param p_alrexceed: Alert Limits Exceedences Limiter.  Enter a numeric value to restrict results to facilities having the given amount or more of alert limits exceedances.
    :type p_alrexceed: 
    :param p_limit_addr: Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
    :type p_limit_addr: str
    :param p_lat: Latitude location in decimal degrees.
    :type p_lat: 
    :param p_long: Longitude location in decimal degrees.
    :type p_long: 
    :param p_radius: Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
    :type p_radius: 
    :param p_ejscreen_over80cnt: The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
    :type p_ejscreen_over80cnt: str
    :param p_bio_flag: A Y value will select all biosolid-related permits.
    :type p_bio_flag: str
    :param p_bio_fac_type: The code indicating the reporting obligation reason:  - POT &#x3D; A POTW with a design flow rate equal to or greater than one million gallons per day - CLI &#x3D; A Class I Sludge Management Facility as defined in 40 CFR 503.9 - PPL &#x3D; A POTW that serves 10,000 people or more - OTH &#x3D; Otherwise required to report (e.g., permit condition, enforcement action) - NOA &#x3D; None of the above
    :type p_bio_fac_type: str
    :param p_bio_trtmnt_procs: The biosolids or sewage sludge treatment process or processes at the facility:  - AER &#x3D; Aerobic Digestion - AIR &#x3D; Air Drying (or Sludge Drying Beds) - ANA &#x3D; Anaerobic Digestion - COD &#x3D; Beta Ray Irradiation - COM &#x3D; Lower Temperature Composting - DEW &#x3D; Pasteurization - DIS &#x3D; Gamma Ray Irradiation - HEA &#x3D; Heat Drying (e.g., Flash Dryer, Spray Dryer, Rotary Dryer) - HET &#x3D; Heat Treatment (Liquid Sewage Sludge Heated to 356 Deg. F/180 Deg. C or Higher for 30 min.) - HTC &#x3D; Higher Temperature Composting - MET &#x3D; Methane or Biogas Capture and Recovery - OTH &#x3D; Other Treatment Process - PRE &#x3D; Preliminary Operations (e.g., Sludge Grinding, Degritting, Blending) - SLU &#x3D; Sludge Lagoon - STA &#x3D; Lime Stabilization - THE &#x3D; Temporary Sludge Storage (Sewage Sludge Stored on Land 2 Years or Less, Not in Sewage Sludge Unit) - THI &#x3D; Thickening (Gravity and/or Flotation Thickening, Centrifugation, Belt Filter Press, Vacuum Filter) - THM &#x3D; Thermophilic Aerobic Digestion - UND &#x3D; Long-Term Sludge Storage (Sewage Sludge Stored on Land 2 Years or More, not in Sewage Sludge Unit)\\\&quot;
    :type p_bio_trtmnt_procs: str
    :param p_bio_analy_method_catgry: The unique code for the category of the analytic methods used by the facility to analyze regulated parameters (including enteric viruses, fecal coliforms, helminth ova, and Salmonella sp.) at the facility:  - PAT &#x3D; Pathogens - MET &#x3D; Metals - NIT &#x3D; Nitrogen Compounds - OTH &#x3D; Other Analytes
    :type p_bio_analy_method_catgry: str
    :param p_bio_total_volume_amt: Total annual amount (in dry metric tons) of biosolids or sewage sludge generated at the facility.  - EQ0 &#x3D; 0 - IN0_1 &#x3D; GT 0 but LT 1 - IN0_289  &#x3D;  GT 0 but LT 290 MT/year - IN290_1499  &#x3D;  GE 290 but LT 1500 MT/year - IN1500_14999  &#x3D;  GE 1500 but LT 15,000 - GE15000  &#x3D;  GE 15,000
    :type p_bio_total_volume_amt: str
    :param p_bio_mgmt_prctce_type: The unique code that identifies the type of biosolids or sewage sludge management practice (e.g., land application, surface disposal, incineration) used by the facility. The facility will separately report the management practice for each biosolids or sewage sludge form and pathogen class. This data element will also identify the management practices used by surface disposal site owners/operators (see 40 CFR 503.24):  - BIN &#x3D; Incineration - BLN &#x3D; Land Application - BOT &#x3D; Other Management Practice - BSD &#x3D; Surface Disposal
    :type p_bio_mgmt_prctce_type: str
    :param p_bio_mgmt_prctce_stype: This is the code indicating additional detail about the type of Management Practice used for a volume of Biosolids or Sewage Sludge:  - ADV &#x3D; Advanced Alkaline Stabilized Biosolids Distribution &amp; Marketing - AGR &#x3D; Agricultural Land Application - COM &#x3D; Distribution and Marketing - Compost - DEE &#x3D; Deep-well Injection Disposal - DIS &#x3D; Disposal in a Municipal Landfill (under 40 CFR 258) - DMO &#x3D; Distribution and Marketing - Other - HEA &#x3D; Heat Dried Biosolids Distribution &amp; Marketing - OTL &#x3D; Other Land Application Management Practice Detail - OTO &#x3D; Other Management Practice Detail - RSA &#x3D; Reclamation Site Application - SEN &#x3D; Sent to Cement Kiln for Use as Alternative Energy - STO &#x3D; Storage - UIC &#x3D; Use in Construction - UPS &#x3D; Used in Production of Syngas - USE &#x3D; Use as Daily Cover for Municipal Landfill (under 40 CFR 258)
    :type p_bio_mgmt_prctce_stype: str
    :param p_bio_mgmt_prctce_handler: This is the code indicating the type of Biosolids or Sewage Sludge handlers/preparers.  - OWN &#x3D; Owner or Operator - OFF &#x3D; Off-Site Third-Party Handler or Preparer
    :type p_bio_mgmt_prctce_handler: str
    :param p_bio_mgmt_container: The code that identifies the nature of each biosolids and sewage sludge material generated by the facility in terms of whether the material is a biosolid or sewage sludge and whether the material is ultimately conveyed off-site in bulk or in bags. The facility separately reports the form for each biosolids or sewage sludge management practice or practices used by the facility and pathogen class:  - BUL &#x3D; Bulk - BAG &#x3D; Bag or Container
    :type p_bio_mgmt_container: str
    :param p_bio_mgmt_pathogen: This code identifies the pathogen class [e.g., Class A, Class B, Not Applicable (Incineration)] for biosolids or sewage sludge generated by the facility. The facility will separately report the pathogen class for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form. It also is used to filter applicable Pathogen Reduction and Vector Attraction Reduction Options as well as Land Application Management Practice Deficiencies. Only reqired for some of the mgmt. practice types:  - AAA &#x3D; Class A - AEQ &#x3D; Class A EQ (sale/give away) - BBB &#x3D; Class B - NAP &#x3D; Not Applicable (Incineration)
    :type p_bio_mgmt_pathogen: str
    :param p_bio_mgmt_pathred: This is the description of the option used by the facility to control pathogen for a Biosolids Management Practice:  - A1 &#x3D; Class A - Alternative 1: Time/Temperature - A2 &#x3D; Class A - Alternative 2: pH/Temperature/Percent Solids - A3 &#x3D; Class A - Alternative 3: Test Enteric Viruses and Helminth ova; Operating Parameters - A4 &#x3D; Class A - Alternative 4: Test Enteric Viruses and Helminth ova; No New Solids - A51 &#x3D; Class A - Alternative 5: PFRP 1: Composting - A52 &#x3D; Class A - Alternative 5: PFRP 2: Heat Drying - A53 &#x3D; Class A - Alternative 5: PFRP 3: Liquid heat treatment - A54 &#x3D; Class A - Alternative 5: PFRP 4: Thermophilic Aerobic Digestion (ATAD) - A55 &#x3D; Class A - Alternative 5 PFPR 5: Beta Ray Irradiation - A56 &#x3D; Class A - Alternative 5 PFPR 6: Gamma Ray Irradiation - A57 &#x3D; Class A - Alternative 5: PFRP 7: Pasteurization - A6 &#x3D; Class A - Alternative 6: PFRP Equivalency - B1 &#x3D; Class B - Alternative 1: Fecal Coliform Geometric Mean - B21 &#x3D; Class B - Alternative 2 PSRP 1: Aerobic Digestion - B22 &#x3D; Class B - Alternative 2 PSRP 2: Air Drying - B23 &#x3D; Class B - Alternative 2 PSRP 3: Anaerobic Digestion - B24 &#x3D; Class B - Alternative 2 PSRP 4: Composting - B25 &#x3D; Class B - Alternative 2 PSRP 5: Lime Stabilization - B3 &#x3D; Class B - Alternative 3: PSRP Equivalency - PH &#x3D; pH Adjustment (Domestic Septage)
    :type p_bio_mgmt_pathred: str
    :param p_bio_mgmt_vector: The unique code that identifies the option used by the facility for vector attraction reduction. See a listing of these vector attraction reduction options at 40 CFR 503.33(b)(1) through (11). The facility will separately report the vector attraction reduction options for each biosolids or sewage sludge management practice used by the facility and by each biosolids or sewage sludge form as well as by each biosolids or sewage sludge pathogen class:  - VR1 &#x3D; Option 1 - Volatile Solids Reduction - VR2 &#x3D; Option 2 - Bench-Scale Volatile Solids Reduction (Anaerobic Bench Test) - VR3 &#x3D; Option 3 - Bench-Scale Volatile Solids Reduction (Aerobic Bench Test w/ Percent Solids - 2% or Less) - VR4 &#x3D; Option 4 - Specific Oxygen Uptake Rate - VR5 &#x3D; Option 5 - Aerobic Processing (Thermophilic Aerobic Digestion/Composting) - VR6 &#x3D; Option 6 - Alkaline Treatment - VR7 &#x3D; Option 7 - Drying (Equal to or Greater than 75 Percent) - VR8 &#x3D; Option 8 - Drying (Equal to or Greater than 90 Percent) - VR9 &#x3D; Option 9 - Sewage Sludge Injection - V10 &#x3D; Option 10 - Sewage Sludge Timely Incorporation into Land - V11 &#x3D; Option 11 - Sewage Sludge Covered at the End of Each Operating Day
    :type p_bio_mgmt_vector: str
    :param p_bio_mgmt_def_category: This is the code indicating the type of NPDES special regulatory program deficiency:  - INC &#x3D; Biosolids Incineration - LNA &#x3D; Biosolids Land Application - LNB &#x3D; Biosolids Land Application - Pathogen Class B - OTB &#x3D; Biosolids Other Management Practice - SFD &#x3D; Biosolids Surface Disposal
    :type p_bio_mgmt_def_category: str
    :param p_bio_mgmt_deficiencies: The number of times noncompliance was reported by the facility in the last 3 years. The results returned will include facilities whose number of reported noncompliance events is greater than or equal to the number entered.
    :type p_bio_mgmt_deficiencies: 
    :param p_bio_vio_code: The Biosolids Single Event Violation Code.  Enter one or mode codes.
    :type p_bio_vio_code: str
    :param p_bio_current_vio: Indicator of whether the facility is currently in violation for biosolids under the Clean Water Act, in the 12th or 13th quarter:  - Y &#x3D; Yes - N &#x3D; No
    :type p_bio_current_vio: str
    :param p_bio_qtrs_in_vio: The number of quarters, in the last three years, where the facility was in violation for a biosolids violation type.  The results returned will include facilities whose number of quarters with violations is greater than or equal to the number entered.
    :type p_bio_qtrs_in_vio: 
    :param p_bio_rpt_year: The last year that the permittee submitted an annual Biosolids report.  Valid values are NONE and any year greater or equal to 2016.
    :type p_bio_rpt_year: str
    :param p_bio_vio_last_year: Identifies if a biosolids violation has occured in the last year.  Valid values are Y and N.
    :type p_bio_vio_last_year: str
    :param p_msgp_rpt_year: The last year that a MSGP report was submitted for the permit.  Valid values are \\\&quot;NONE\\\&quot; and any year Greater or Eqal to 2015.
    :type p_msgp_rpt_year: str
    :param p_vio_last_year: Identifies if a permit violation has occured in the last year.  Valid values are Y and N.
    :type p_vio_last_year: str
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 
    :param p_e90_count: Number of E90 Exceedances.  Identifies water permits with a number of E90 (Effluient Exceedances) &gt;&#x3D; the value provided for the last number of years provided by the p_e90_years value.
    :type p_e90_count: 
    :param p_e90_years: Number of years for the p_e90_count search.  Identified the past number of years to be used for the p_e90_count search.
    :type p_e90_years: 
    :param p_psc: Point Source Category.
    :type p_psc: str

    """
    return web.Response(status=200)


async def cwa_rest_services_get_geojson_get(request: web.Request, qid, output=None, param_callback=None, newsort=None, descending=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Clean Water Act (CWA) GeoJSON Service

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


async def cwa_rest_services_get_geojson_post(request: web.Request, qid, output=None, param_callback=None, newsort=None, descending=None, qcolumns=None, p_pretty_print=None) -> web.Response:
    """Clean Water Act (CWA) GeoJSON Service

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


async def cwa_rest_services_get_info_clusters_get(request: web.Request, p_qid, output=None, p_pretty_print=None) -> web.Response:
    """Clean Water Act (CWA) Info Clusters Service

    Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

    :param p_qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type p_qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def cwa_rest_services_get_info_clusters_post(request: web.Request, p_qid, output=None, p_pretty_print=None) -> web.Response:
    """Clean Water Act (CWA) Info Clusters Service

    Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

    :param p_qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type p_qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download.
    :type output: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 

    """
    return web.Response(status=200)


async def cwa_rest_services_get_map_get(request: web.Request, qid, p_id, output=None, param_callback=None, tablelist=None, c1_lat=None, c1_long=None, c2_lat=None, c2_long=None) -> web.Response:
    """Clean Water Act (CWA) Map Service

    The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param p_id: Nine-character code used to uniquely identify a permitted NPDES facility. The NPDES permit program regulates the direct discharge of pollutants into US waters.
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


async def cwa_rest_services_get_map_post(request: web.Request, qid, p_id, output=None, param_callback=None, tablelist=None, c1_lat=None, c1_long=None, c2_lat=None, c2_long=None) -> web.Response:
    """Clean Water Act (CWA) Map Service

    The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param p_id: Nine-character code used to uniquely identify a permitted NPDES facility. The NPDES permit program regulates the direct discharge of pollutants into US waters.
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


async def cwa_rest_services_get_qid_get(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Clean Water Act (CWA) Paginated Results Service

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


async def cwa_rest_services_get_qid_post(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Clean Water Act (CWA) Paginated Results Service

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

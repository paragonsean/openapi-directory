from typing import List, Dict
from aiohttp import web

from openapi_server.models.case_rest_services_get_case_info_get200_response import CaseRestServicesGetCaseInfoGet200Response
from openapi_server.models.case_rest_services_get_case_report_get200_response import CaseRestServicesGetCaseReportGet200Response
from openapi_server.models.case_rest_services_get_cases_from_facility_get200_response import CaseRestServicesGetCasesFromFacilityGet200Response
from openapi_server.models.case_rest_services_get_cases_get200_response import CaseRestServicesGetCasesGet200Response
from openapi_server.models.case_rest_services_get_crcase_report_get200_response import CaseRestServicesGetCrcaseReportGet200Response
from openapi_server.models.case_rest_services_get_facilities_from_case_get200_response import CaseRestServicesGetFacilitiesFromCaseGet200Response
from openapi_server.models.case_rest_services_get_map_get200_response import CaseRestServicesGetMapGet200Response
from openapi_server.models.case_rest_services_get_qid_get200_response import CaseRestServicesGetQidGet200Response
from openapi_server import util


async def case_rest_services_get_case_info_get(request: web.Request, output=None, p_case_category=None, p_case_status=None, p_milestone=None, p_from_date=None, p_to_date=None, p_milestone_fy=None, p_name=None, p_name_type=None, p_case_number=None, p_docket_number=None, p_court_docket_number=None, p_activity_number=None, p_case_lead=None, p_case_sens_flg=None, p_region=None, p_state=None, p_district=None, p_sic=None, p_sic_ao_naics=None, p_sic_primary_flg=None, p_sic_frs_flg=None, p_naics=None, p_naics_primary_flg=None, p_naics_frs_flg=None, p_enf_type=None, p_law=None, p_section=None, p_cp_citation=None, p_rank_order=None, p_enf_program=None, p_violation=None, p_priority_area=None, p_priority_area_desc=None, p_tribal=None, p_oeca_core=None, p_multimedia=None, p_fed_case=None, p_activity_contact=None, p_role=None, p_fed_penalty=None, p_total_fed_penalty=None, p_cost_recovery=None, p_total_cost_recovery=None, p_complying_actions=None, p_comp_act_val=None, p_total_comp_act_val=None, p_sep_cats=None, p_sep_val=None, p_total_sep_val=None, p_lodged_date=None, p_entered_date=None, p_facility_id=None, p_fac_city=None, p_fac_zip=None, p_fac_county=None, p_case_summary=None, p_case_summary_type=None, p_usmex=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_voluntary=None, p_fed_indicator=None, p_fntype=None, p_civil_criminal_indicator=None, queryset=None, responseset=None, mapset=None, param_callback=None, qcolumns=None, p_pretty_print=None, p_ocmap_fy=None, p_qs=None, p_has_map=None) -> web.Response:
    """Enforcement Case Search (new version)

    The get_case_info service end point searches for civil enforcement and criminal cases based on the provided selection criteria and returns either individual cases or clusters of case facility locations.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_case_category: Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial
    :type p_case_category: str
    :param p_case_status: Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_case_status: str
    :param p_milestone: Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_milestone: str
    :param p_from_date: Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    :type p_from_date: str
    :param p_to_date: Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    :type p_to_date: str
    :param p_milestone_fy: Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    :type p_milestone_fy: str
    :param p_name: Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    :type p_name: str
    :param p_name_type: Case Name Filter Modifier.
    :type p_name_type: str
    :param p_case_number: Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_case_number: str
    :param p_docket_number: DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \&quot;%\&quot; as a wildcard for more complex filtering.
    :type p_docket_number: str
    :param p_court_docket_number: 
    :type p_court_docket_number: str
    :param p_activity_number: Case Activity Number Filter.  Enter a single case activity number to filter results.
    :type p_activity_number: str
    :param p_case_lead: Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead.
    :type p_case_lead: str
    :param p_case_sens_flg: Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    :type p_case_sens_flg: str
    :param p_region: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_region: str
    :param p_state: Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    :type p_state: str
    :param p_district: Case Location Court District Limiter.  Enter a single state court district code to limit results.
    :type p_district: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    :type p_sic: str
    :param p_sic_ao_naics: Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    :type p_sic_ao_naics: str
    :param p_sic_primary_flg: Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    :type p_sic_primary_flg: str
    :param p_sic_frs_flg: Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    :type p_sic_frs_flg: str
    :param p_naics: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_naics: str
    :param p_naics_primary_flg: Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    :type p_naics_primary_flg: str
    :param p_naics_frs_flg: Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    :type p_naics_frs_flg: str
    :param p_enf_type: Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_enf_type: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_cp_citation: Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_cp_citation: str
    :param p_rank_order: Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    :type p_rank_order: str
    :param p_enf_program: Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    :type p_enf_program: str
    :param p_violation: Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violation: str
    :param p_priority_area: Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    :type p_priority_area: str
    :param p_priority_area_desc: Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \&quot;%\&quot; as a wild-card match for more complex searches.
    :type p_priority_area_desc: str
    :param p_tribal: Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    :type p_tribal: str
    :param p_oeca_core: OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    :type p_oeca_core: str
    :param p_multimedia: Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    :type p_multimedia: str
    :param p_fed_case: Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    :type p_fed_case: str
    :param p_activity_contact: Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \&quot;%\&quot; as a wild-card for advanced searching.
    :type p_activity_contact: str
    :param p_role: Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    :type p_role: str
    :param p_fed_penalty: Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000.
    :type p_fed_penalty: str
    :param p_total_fed_penalty: Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    :type p_total_fed_penalty: str
    :param p_cost_recovery: Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_cost_recovery: str
    :param p_total_cost_recovery: Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_total_cost_recovery: str
    :param p_complying_actions: Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_complying_actions: str
    :param p_comp_act_val: Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    :type p_comp_act_val: str
    :param p_total_comp_act_val: Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    :type p_total_comp_act_val: str
    :param p_sep_cats: Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_sep_cats: str
    :param p_sep_val: Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000.
    :type p_sep_val: str
    :param p_total_sep_val: Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000.
    :type p_total_sep_val: str
    :param p_lodged_date: Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    :type p_lodged_date: str
    :param p_entered_date: Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    :type p_entered_date: str
    :param p_facility_id: Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    :type p_facility_id: str
    :param p_fac_city: Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    :type p_fac_city: str
    :param p_fac_zip: Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    :type p_fac_zip: str
    :param p_fac_county: Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    :type p_fac_county: str
    :param p_case_summary: Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_case_summary: str
    :param p_case_summary_type: Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    :type p_case_summary_type: str
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_c1lat: In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lat: 
    :param p_c1lon: In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lon: 
    :param p_c2lat: In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lat: 
    :param p_c2lon: In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lon: 
    :param p_voluntary: Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    :type p_voluntary: str
    :param p_fed_indicator: Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    :type p_fed_indicator: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_civil_criminal_indicator: Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases.
    :type p_civil_criminal_indicator: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param mapset: Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    :type mapset: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 
    :param p_ocmap_fy: Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    :type p_ocmap_fy: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_has_map: 
    :type p_has_map: str

    """
    return web.Response(status=200)


async def case_rest_services_get_case_info_post(request: web.Request, output=None, p_case_category=None, p_case_status=None, p_milestone=None, p_from_date=None, p_to_date=None, p_milestone_fy=None, p_name=None, p_name_type=None, p_case_number=None, p_docket_number=None, p_court_docket_number=None, p_activity_number=None, p_case_lead=None, p_case_sens_flg=None, p_region=None, p_state=None, p_district=None, p_sic=None, p_sic_ao_naics=None, p_sic_primary_flg=None, p_sic_frs_flg=None, p_naics=None, p_naics_primary_flg=None, p_naics_frs_flg=None, p_enf_type=None, p_law=None, p_section=None, p_cp_citation=None, p_rank_order=None, p_enf_program=None, p_violation=None, p_priority_area=None, p_priority_area_desc=None, p_tribal=None, p_oeca_core=None, p_multimedia=None, p_fed_case=None, p_activity_contact=None, p_role=None, p_fed_penalty=None, p_total_fed_penalty=None, p_cost_recovery=None, p_total_cost_recovery=None, p_complying_actions=None, p_comp_act_val=None, p_total_comp_act_val=None, p_sep_cats=None, p_sep_val=None, p_total_sep_val=None, p_lodged_date=None, p_entered_date=None, p_facility_id=None, p_fac_city=None, p_fac_zip=None, p_fac_county=None, p_case_summary=None, p_case_summary_type=None, p_usmex=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_voluntary=None, p_fed_indicator=None, p_fntype=None, p_civil_criminal_indicator=None, queryset=None, responseset=None, mapset=None, param_callback=None, qcolumns=None, p_pretty_print=None, p_ocmap_fy=None, p_qs=None, p_has_map=None) -> web.Response:
    """Enforcement Case Search (new version)

    The get_case_info service end point searches for civil enforcement and criminal cases based on the provided selection criteria and returns either individual cases or clusters of case facility locations.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_case_category: Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial
    :type p_case_category: str
    :param p_case_status: Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_case_status: str
    :param p_milestone: Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_milestone: str
    :param p_from_date: Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    :type p_from_date: str
    :param p_to_date: Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    :type p_to_date: str
    :param p_milestone_fy: Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    :type p_milestone_fy: str
    :param p_name: Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    :type p_name: str
    :param p_name_type: Case Name Filter Modifier.
    :type p_name_type: str
    :param p_case_number: Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_case_number: str
    :param p_docket_number: DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\&quot;%\\\&quot; as a wildcard for more complex filtering.
    :type p_docket_number: str
    :param p_court_docket_number: 
    :type p_court_docket_number: str
    :param p_activity_number: Case Activity Number Filter.  Enter a single case activity number to filter results.
    :type p_activity_number: str
    :param p_case_lead: Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead.
    :type p_case_lead: str
    :param p_case_sens_flg: Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    :type p_case_sens_flg: str
    :param p_region: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_region: str
    :param p_state: Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    :type p_state: str
    :param p_district: Case Location Court District Limiter.  Enter a single state court district code to limit results.
    :type p_district: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    :type p_sic: str
    :param p_sic_ao_naics: Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    :type p_sic_ao_naics: str
    :param p_sic_primary_flg: Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    :type p_sic_primary_flg: str
    :param p_sic_frs_flg: Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    :type p_sic_frs_flg: str
    :param p_naics: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_naics: str
    :param p_naics_primary_flg: Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    :type p_naics_primary_flg: str
    :param p_naics_frs_flg: Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    :type p_naics_frs_flg: str
    :param p_enf_type: Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_enf_type: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_cp_citation: Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_cp_citation: str
    :param p_rank_order: Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    :type p_rank_order: str
    :param p_enf_program: Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    :type p_enf_program: str
    :param p_violation: Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violation: str
    :param p_priority_area: Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    :type p_priority_area: str
    :param p_priority_area_desc: Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\&quot;%\\\&quot; as a wild-card match for more complex searches.
    :type p_priority_area_desc: str
    :param p_tribal: Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    :type p_tribal: str
    :param p_oeca_core: OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    :type p_oeca_core: str
    :param p_multimedia: Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    :type p_multimedia: str
    :param p_fed_case: Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    :type p_fed_case: str
    :param p_activity_contact: Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\&quot;%\\\&quot; as a wild-card for advanced searching.
    :type p_activity_contact: str
    :param p_role: Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    :type p_role: str
    :param p_fed_penalty: Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000.
    :type p_fed_penalty: str
    :param p_total_fed_penalty: Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    :type p_total_fed_penalty: str
    :param p_cost_recovery: Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_cost_recovery: str
    :param p_total_cost_recovery: Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_total_cost_recovery: str
    :param p_complying_actions: Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_complying_actions: str
    :param p_comp_act_val: Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    :type p_comp_act_val: str
    :param p_total_comp_act_val: Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    :type p_total_comp_act_val: str
    :param p_sep_cats: Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_sep_cats: str
    :param p_sep_val: Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000.
    :type p_sep_val: str
    :param p_total_sep_val: Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000.
    :type p_total_sep_val: str
    :param p_lodged_date: Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    :type p_lodged_date: str
    :param p_entered_date: Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    :type p_entered_date: str
    :param p_facility_id: Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    :type p_facility_id: str
    :param p_fac_city: Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    :type p_fac_city: str
    :param p_fac_zip: Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    :type p_fac_zip: str
    :param p_fac_county: Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    :type p_fac_county: str
    :param p_case_summary: Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_case_summary: str
    :param p_case_summary_type: Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    :type p_case_summary_type: str
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_c1lat: In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lat: 
    :param p_c1lon: In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lon: 
    :param p_c2lat: In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lat: 
    :param p_c2lon: In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lon: 
    :param p_voluntary: Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    :type p_voluntary: str
    :param p_fed_indicator: Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    :type p_fed_indicator: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_civil_criminal_indicator: Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases.
    :type p_civil_criminal_indicator: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param mapset: Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    :type mapset: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_pretty_print: Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    :type p_pretty_print: 
    :param p_ocmap_fy: Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    :type p_ocmap_fy: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_has_map: 
    :type p_has_map: str

    """
    return web.Response(status=200)


async def case_rest_services_get_case_report_get(request: web.Request, p_id=None, output=None, param_callback=None) -> web.Response:
    """Enforcement Case Summary Report Search

    The get_case_report service endpoint returns a complex object of civil enforcement case details based on the provided case id.

    :param p_id: Case Number. Enter the case number identifier to retrieve the case report.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def case_rest_services_get_case_report_post(request: web.Request, p_id=None, output=None, param_callback=None) -> web.Response:
    """Enforcement Case Summary Report Search

    The get_case_report service endpoint returns a complex object of civil enforcement case details based on the provided case id.

    :param p_id: Case Number. Enter the case number identifier to retrieve the case report.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def case_rest_services_get_cases_from_facility_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def case_rest_services_get_cases_from_facility_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def case_rest_services_get_cases_get(request: web.Request, output=None, p_case_category=None, p_case_status=None, p_violation=None, p_milestone=None, p_from_date=None, p_to_date=None, p_milestone_fy=None, p_name=None, p_name_type=None, p_case_number=None, p_docket_number=None, p_court_docket_number=None, p_activity_number=None, p_case_lead=None, p_case_sens_flg=None, p_region=None, p_state=None, p_district=None, p_sic=None, p_sic_ao_naics=None, p_sic_primary_flg=None, p_sic_frs_flg=None, p_naics=None, p_naics_primary_flg=None, p_naics_frs_flg=None, p_enf_type=None, p_law=None, p_section=None, p_cp_citation=None, p_rank_order=None, p_enf_program=None, p_priority_area=None, p_priority_area_desc=None, p_tribal=None, p_oeca_core=None, p_multimedia=None, p_fed_case=None, p_activity_contact=None, p_role=None, p_fed_penalty=None, p_total_fed_penalty=None, p_cost_recovery=None, p_total_cost_recovery=None, p_complying_actions=None, p_comp_act_val=None, p_total_comp_act_val=None, p_sep_cats=None, p_sep_val=None, p_total_sep_val=None, p_lodged_date=None, p_entered_date=None, p_facility_id=None, p_fac_city=None, p_fac_zip=None, p_fac_county=None, p_case_summary=None, p_case_summary_type=None, p_usmex=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_voluntary=None, p_fed_indicator=None, p_fntype=None, p_civil_criminal_indicator=None, queryset=None, responseset=None, maplist=None, tablelist=None, param_callback=None, qcolumns=None, p_ocmap_fy=None, p_qs=None, p_has_map=None) -> web.Response:
    """Enforcement Case Search

    The get_cases service end point searches for civil enforcement and criminal cases based on the provided selection criteria.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_case_category: Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial
    :type p_case_category: str
    :param p_case_status: Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_case_status: str
    :param p_violation: Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violation: str
    :param p_milestone: Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_milestone: str
    :param p_from_date: Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    :type p_from_date: str
    :param p_to_date: Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    :type p_to_date: str
    :param p_milestone_fy: Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    :type p_milestone_fy: str
    :param p_name: Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    :type p_name: str
    :param p_name_type: Case Name Filter Modifier.
    :type p_name_type: str
    :param p_case_number: Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_case_number: str
    :param p_docket_number: DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \&quot;%\&quot; as a wildcard for more complex filtering.
    :type p_docket_number: str
    :param p_court_docket_number: 
    :type p_court_docket_number: str
    :param p_activity_number: Case Activity Number Filter.  Enter a single case activity number to filter results.
    :type p_activity_number: str
    :param p_case_lead: Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead.
    :type p_case_lead: str
    :param p_case_sens_flg: Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    :type p_case_sens_flg: str
    :param p_region: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_region: str
    :param p_state: Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    :type p_state: str
    :param p_district: Case Location Court District Limiter.  Enter a single state court district code to limit results.
    :type p_district: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    :type p_sic: str
    :param p_sic_ao_naics: Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    :type p_sic_ao_naics: str
    :param p_sic_primary_flg: Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    :type p_sic_primary_flg: str
    :param p_sic_frs_flg: Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    :type p_sic_frs_flg: str
    :param p_naics: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_naics: str
    :param p_naics_primary_flg: Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    :type p_naics_primary_flg: str
    :param p_naics_frs_flg: Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    :type p_naics_frs_flg: str
    :param p_enf_type: Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_enf_type: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_cp_citation: Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_cp_citation: str
    :param p_rank_order: Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    :type p_rank_order: str
    :param p_enf_program: Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    :type p_enf_program: str
    :param p_priority_area: Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    :type p_priority_area: str
    :param p_priority_area_desc: Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \&quot;%\&quot; as a wild-card match for more complex searches.
    :type p_priority_area_desc: str
    :param p_tribal: Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    :type p_tribal: str
    :param p_oeca_core: OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    :type p_oeca_core: str
    :param p_multimedia: Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    :type p_multimedia: str
    :param p_fed_case: Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    :type p_fed_case: str
    :param p_activity_contact: Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \&quot;%\&quot; as a wild-card for advanced searching.
    :type p_activity_contact: str
    :param p_role: Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    :type p_role: str
    :param p_fed_penalty: Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000.
    :type p_fed_penalty: str
    :param p_total_fed_penalty: Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    :type p_total_fed_penalty: str
    :param p_cost_recovery: Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_cost_recovery: str
    :param p_total_cost_recovery: Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_total_cost_recovery: str
    :param p_complying_actions: Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_complying_actions: str
    :param p_comp_act_val: Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    :type p_comp_act_val: str
    :param p_total_comp_act_val: Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    :type p_total_comp_act_val: str
    :param p_sep_cats: Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_sep_cats: str
    :param p_sep_val: Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000.
    :type p_sep_val: str
    :param p_total_sep_val: Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000.
    :type p_total_sep_val: str
    :param p_lodged_date: Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    :type p_lodged_date: str
    :param p_entered_date: Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    :type p_entered_date: str
    :param p_facility_id: Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    :type p_facility_id: str
    :param p_fac_city: Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    :type p_fac_city: str
    :param p_fac_zip: Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    :type p_fac_zip: str
    :param p_fac_county: Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    :type p_fac_county: str
    :param p_case_summary: Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_case_summary: str
    :param p_case_summary_type: Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    :type p_case_summary_type: str
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_c1lat: In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lat: 
    :param p_c1lon: In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lon: 
    :param p_c2lat: In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lat: 
    :param p_c2lon: In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lon: 
    :param p_voluntary: Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    :type p_voluntary: str
    :param p_fed_indicator: Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    :type p_fed_indicator: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_civil_criminal_indicator: Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases.
    :type p_civil_criminal_indicator: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param maplist: Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    :type maplist: str
    :param tablelist: Table List Flag. Enter a Y to display the first page of facility results.
    :type tablelist: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_ocmap_fy: Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    :type p_ocmap_fy: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_has_map: 
    :type p_has_map: str

    """
    return web.Response(status=200)


async def case_rest_services_get_cases_post(request: web.Request, output=None, p_case_category=None, p_case_status=None, p_milestone=None, p_from_date=None, p_to_date=None, p_milestone_fy=None, p_name=None, p_name_type=None, p_case_number=None, p_docket_number=None, p_court_docket_number=None, p_activity_number=None, p_case_lead=None, p_case_sens_flg=None, p_region=None, p_state=None, p_district=None, p_sic=None, p_sic_ao_naics=None, p_sic_primary_flg=None, p_sic_frs_flg=None, p_naics=None, p_naics_primary_flg=None, p_naics_frs_flg=None, p_enf_type=None, p_law=None, p_section=None, p_cp_citation=None, p_rank_order=None, p_enf_program=None, p_violation=None, p_priority_area=None, p_priority_area_desc=None, p_tribal=None, p_oeca_core=None, p_multimedia=None, p_fed_case=None, p_activity_contact=None, p_role=None, p_fed_penalty=None, p_total_fed_penalty=None, p_cost_recovery=None, p_total_cost_recovery=None, p_complying_actions=None, p_comp_act_val=None, p_total_comp_act_val=None, p_sep_cats=None, p_sep_val=None, p_total_sep_val=None, p_lodged_date=None, p_entered_date=None, p_facility_id=None, p_fac_city=None, p_fac_zip=None, p_fac_county=None, p_case_summary=None, p_case_summary_type=None, p_usmex=None, p_c1lat=None, p_c1lon=None, p_c2lat=None, p_c2lon=None, p_voluntary=None, p_fed_indicator=None, p_fntype=None, p_civil_criminal_indicator=None, queryset=None, responseset=None, maplist=None, tablelist=None, param_callback=None, qcolumns=None, p_ocmap_fy=None, p_qs=None, p_has_map=None) -> web.Response:
    """Enforcement Case Search

    The get_cases service end point searches for civil enforcement and criminal cases based on the provided selection criteria.

    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param p_case_category: Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial
    :type p_case_category: str
    :param p_case_status: Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_case_status: str
    :param p_milestone: Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_milestone: str
    :param p_from_date: Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    :type p_from_date: str
    :param p_to_date: Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    :type p_to_date: str
    :param p_milestone_fy: Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    :type p_milestone_fy: str
    :param p_name: Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    :type p_name: str
    :param p_name_type: Case Name Filter Modifier.
    :type p_name_type: str
    :param p_case_number: Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_case_number: str
    :param p_docket_number: DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\&quot;%\\\&quot; as a wildcard for more complex filtering.
    :type p_docket_number: str
    :param p_court_docket_number: 
    :type p_court_docket_number: str
    :param p_activity_number: Case Activity Number Filter.  Enter a single case activity number to filter results.
    :type p_activity_number: str
    :param p_case_lead: Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead.
    :type p_case_lead: str
    :param p_case_sens_flg: Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    :type p_case_sens_flg: str
    :param p_region: EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    :type p_region: str
    :param p_state: Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    :type p_state: str
    :param p_district: Case Location Court District Limiter.  Enter a single state court district code to limit results.
    :type p_district: str
    :param p_sic: Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    :type p_sic: str
    :param p_sic_ao_naics: Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    :type p_sic_ao_naics: str
    :param p_sic_primary_flg: Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    :type p_sic_primary_flg: str
    :param p_sic_frs_flg: Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    :type p_sic_frs_flg: str
    :param p_naics: North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    :type p_naics: str
    :param p_naics_primary_flg: Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    :type p_naics_primary_flg: str
    :param p_naics_frs_flg: Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    :type p_naics_frs_flg: str
    :param p_enf_type: Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_enf_type: str
    :param p_law: Law Statute Code Filter.  Enter a single statute code to limit results.
    :type p_law: str
    :param p_section: Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_section: str
    :param p_cp_citation: Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_cp_citation: str
    :param p_rank_order: Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    :type p_rank_order: str
    :param p_enf_program: Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    :type p_enf_program: str
    :param p_violation: Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_violation: str
    :param p_priority_area: Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    :type p_priority_area: str
    :param p_priority_area_desc: Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\&quot;%\\\&quot; as a wild-card match for more complex searches.
    :type p_priority_area_desc: str
    :param p_tribal: Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    :type p_tribal: str
    :param p_oeca_core: OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    :type p_oeca_core: str
    :param p_multimedia: Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    :type p_multimedia: str
    :param p_fed_case: Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    :type p_fed_case: str
    :param p_activity_contact: Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\&quot;%\\\&quot; as a wild-card for advanced searching.
    :type p_activity_contact: str
    :param p_role: Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    :type p_role: str
    :param p_fed_penalty: Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000.
    :type p_fed_penalty: str
    :param p_total_fed_penalty: Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    :type p_total_fed_penalty: str
    :param p_cost_recovery: Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_cost_recovery: str
    :param p_total_cost_recovery: Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    :type p_total_cost_recovery: str
    :param p_complying_actions: Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    :type p_complying_actions: str
    :param p_comp_act_val: Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    :type p_comp_act_val: str
    :param p_total_comp_act_val: Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    :type p_total_comp_act_val: str
    :param p_sep_cats: Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    :type p_sep_cats: str
    :param p_sep_val: Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000.
    :type p_sep_val: str
    :param p_total_sep_val: Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000.
    :type p_total_sep_val: str
    :param p_lodged_date: Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    :type p_lodged_date: str
    :param p_entered_date: Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    :type p_entered_date: str
    :param p_facility_id: Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    :type p_facility_id: str
    :param p_fac_city: Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    :type p_fac_city: str
    :param p_fac_zip: Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    :type p_fac_zip: str
    :param p_fac_county: Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    :type p_fac_county: str
    :param p_case_summary: Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    :type p_case_summary: str
    :param p_case_summary_type: Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    :type p_case_summary_type: str
    :param p_usmex: US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    :type p_usmex: str
    :param p_c1lat: In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lat: 
    :param p_c1lon: In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c1lon: 
    :param p_c2lat: In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lat: 
    :param p_c2lon: In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    :type p_c2lon: 
    :param p_voluntary: Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    :type p_voluntary: str
    :param p_fed_indicator: Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    :type p_fed_indicator: str
    :param p_fntype: Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D; 
    :type p_fntype: str
    :param p_civil_criminal_indicator: Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases.
    :type p_civil_criminal_indicator: str
    :param queryset: Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    :type queryset: 
    :param responseset: Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    :type responseset: 
    :param maplist: Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    :type maplist: str
    :param tablelist: Table List Flag. Enter a Y to display the first page of facility results.
    :type tablelist: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str
    :param p_ocmap_fy: Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    :type p_ocmap_fy: str
    :param p_qs: Quick Search. Allows entry for city, state, and/or zip code.
    :type p_qs: str
    :param p_has_map: 
    :type p_has_map: str

    """
    return web.Response(status=200)


async def case_rest_services_get_crcase_report_get(request: web.Request, p_id=None, output=None, param_callback=None, mapset=None) -> web.Response:
    """Enforcement Criminal Case Summary Report Search

    The get_crcase_report service end point returns a complex object of criminal case detials based on the provided criminal case id.

    :param p_id: Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str
    :param mapset: Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    :type mapset: str

    """
    return web.Response(status=200)


async def case_rest_services_get_crcase_report_post(request: web.Request, p_id=None, output=None, param_callback=None) -> web.Response:
    """Enforcement Criminal Case Summary Report Search

    The get_crcase_report service end point returns a complex object of criminal case detials based on the provided criminal case id.

    :param p_id: Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def case_rest_services_get_download_get(request: web.Request, qid, output=None, qcolumns=None) -> web.Response:
    """Enforcement Case Download Data Service

    Based on the QID obtained from a get_cases query, return a comma separated value (CSV) file of the cases found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default).
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def case_rest_services_get_download_post(request: web.Request, qid, output=None, qcolumns=None) -> web.Response:
    """Enforcement Case Download Data Service

    Based on the QID obtained from a get_cases query, return a comma separated value (CSV) file of the cases found.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
    :param output: Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default).
    :type output: str
    :param qcolumns: Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    :type qcolumns: str

    """
    return web.Response(status=200)


async def case_rest_services_get_facilities_from_case_get(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def case_rest_services_get_facilities_from_case_post(request: web.Request, p_id, output=None, param_callback=None) -> web.Response:
    """Placeholder

    

    :param p_id: Identifier for the service.
    :type p_id: str
    :param output: Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language.
    :type output: str
    :param param_callback: JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    :type param_callback: str

    """
    return web.Response(status=200)


async def case_rest_services_get_map_get(request: web.Request, qid, output=None, param_callback=None, tablelist=None, c1_lat=None, c1_long=None, c2_lat=None, c2_long=None) -> web.Response:
    """Enforcement Case Map Service

    The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_cases query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
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


async def case_rest_services_get_map_post(request: web.Request, qid, output=None, param_callback=None, tablelist=None, c1_lat=None, c1_long=None, c2_lat=None, c2_long=None, mapset=None) -> web.Response:
    """Enforcement Case Map Service

    The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_cases query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

    :param qid: Query ID Selector.  Enter the QueryID number from a previously run query.
    :type qid: str
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
    :param mapset: Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    :type mapset: str

    """
    return web.Response(status=200)


async def case_rest_services_get_qid_get(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Enforcement Case Paginated Results Service

    GET_QID is passed with a query ID corresponding to a previously run get_cases query. It then returns a CASES object containing all matching cases. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

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


async def case_rest_services_get_qid_post(request: web.Request, qid, output=None, pageno=None, param_callback=None, newsort=None, descending=None, qcolumns=None) -> web.Response:
    """Enforcement Case Paginated Results Service

    GET_QID is passed with a query ID corresponding to a previously run get_cases query. It then returns a CASES object containing all matching cases. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

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

# USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**caseRestServicesGetCaseInfoGet**](CaseEnforcementApi.md#caseRestServicesGetCaseInfoGet) | **GET** /case_rest_services.get_case_info | Enforcement Case Search (new version)
[**caseRestServicesGetCaseInfoPost**](CaseEnforcementApi.md#caseRestServicesGetCaseInfoPost) | **POST** /case_rest_services.get_case_info | Enforcement Case Search (new version)
[**caseRestServicesGetCaseReportGet**](CaseEnforcementApi.md#caseRestServicesGetCaseReportGet) | **GET** /case_rest_services.get_case_report | Enforcement Case Summary Report Search
[**caseRestServicesGetCaseReportPost**](CaseEnforcementApi.md#caseRestServicesGetCaseReportPost) | **POST** /case_rest_services.get_case_report | Enforcement Case Summary Report Search
[**caseRestServicesGetCasesFromFacilityGet**](CaseEnforcementApi.md#caseRestServicesGetCasesFromFacilityGet) | **GET** /case_rest_services.get_cases_from_facility | Placeholder
[**caseRestServicesGetCasesFromFacilityPost**](CaseEnforcementApi.md#caseRestServicesGetCasesFromFacilityPost) | **POST** /case_rest_services.get_cases_from_facility | Placeholder
[**caseRestServicesGetCasesGet**](CaseEnforcementApi.md#caseRestServicesGetCasesGet) | **GET** /case_rest_services.get_cases | Enforcement Case Search
[**caseRestServicesGetCasesPost**](CaseEnforcementApi.md#caseRestServicesGetCasesPost) | **POST** /case_rest_services.get_cases | Enforcement Case Search
[**caseRestServicesGetCrcaseReportGet**](CaseEnforcementApi.md#caseRestServicesGetCrcaseReportGet) | **GET** /case_rest_services.get_crcase_report | Enforcement Criminal Case Summary Report Search
[**caseRestServicesGetCrcaseReportPost**](CaseEnforcementApi.md#caseRestServicesGetCrcaseReportPost) | **POST** /case_rest_services.get_crcase_report | Enforcement Criminal Case Summary Report Search
[**caseRestServicesGetDownloadGet**](CaseEnforcementApi.md#caseRestServicesGetDownloadGet) | **GET** /case_rest_services.get_download | Enforcement Case Download Data Service
[**caseRestServicesGetDownloadPost**](CaseEnforcementApi.md#caseRestServicesGetDownloadPost) | **POST** /case_rest_services.get_download | Enforcement Case Download Data Service
[**caseRestServicesGetFacilitiesFromCaseGet**](CaseEnforcementApi.md#caseRestServicesGetFacilitiesFromCaseGet) | **GET** /case_rest_services.get_facilities_from_case | Placeholder
[**caseRestServicesGetFacilitiesFromCasePost**](CaseEnforcementApi.md#caseRestServicesGetFacilitiesFromCasePost) | **POST** /case_rest_services.get_facilities_from_case | Placeholder
[**caseRestServicesGetMapGet**](CaseEnforcementApi.md#caseRestServicesGetMapGet) | **GET** /case_rest_services.get_map | Enforcement Case Map Service
[**caseRestServicesGetMapPost**](CaseEnforcementApi.md#caseRestServicesGetMapPost) | **POST** /case_rest_services.get_map | Enforcement Case Map Service
[**caseRestServicesGetQidGet**](CaseEnforcementApi.md#caseRestServicesGetQidGet) | **GET** /case_rest_services.get_qid | Enforcement Case Paginated Results Service
[**caseRestServicesGetQidPost**](CaseEnforcementApi.md#caseRestServicesGetQidPost) | **POST** /case_rest_services.get_qid | Enforcement Case Paginated Results Service



## caseRestServicesGetCaseInfoGet

> CaseRestServicesGetCaseInfoGet200Response caseRestServicesGetCaseInfoGet(opts)

Enforcement Case Search (new version)

The get_case_info service end point searches for civil enforcement and criminal cases based on the provided selection criteria and returns either individual cases or clusters of case facility locations.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pCaseCategory': "pCaseCategory_example", // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
  'pCaseStatus': "pCaseStatus_example", // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
  'pMilestone': "pMilestone_example", // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
  'pFromDate': "pFromDate_example", // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
  'pToDate': "pToDate_example", // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
  'pMilestoneFy': "pMilestoneFy_example", // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
  'pName': "pName_example", // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
  'pNameType': "pNameType_example", // String | Case Name Filter Modifier.
  'pCaseNumber': "pCaseNumber_example", // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
  'pDocketNumber': "pDocketNumber_example", // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \"%\" as a wildcard for more complex filtering.
  'pCourtDocketNumber': "pCourtDocketNumber_example", // String | 
  'pActivityNumber': "pActivityNumber_example", // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
  'pCaseLead': "pCaseLead_example", // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
  'pCaseSensFlg': "pCaseSensFlg_example", // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
  'pRegion': "pRegion_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pState': "pState_example", // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
  'pDistrict': "pDistrict_example", // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
  'pSicAoNaics': "pSicAoNaics_example", // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
  'pSicPrimaryFlg': "pSicPrimaryFlg_example", // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
  'pSicFrsFlg': "pSicFrsFlg_example", // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
  'pNaics': "pNaics_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pNaicsPrimaryFlg': "pNaicsPrimaryFlg_example", // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
  'pNaicsFrsFlg': "pNaicsFrsFlg_example", // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
  'pEnfType': "pEnfType_example", // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pCpCitation': "pCpCitation_example", // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pRankOrder': "pRankOrder_example", // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
  'pEnfProgram': "pEnfProgram_example", // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
  'pViolation': "pViolation_example", // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pPriorityArea': "pPriorityArea_example", // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
  'pPriorityAreaDesc': "pPriorityAreaDesc_example", // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \"%\" as a wild-card match for more complex searches.
  'pTribal': "pTribal_example", // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
  'pOecaCore': "pOecaCore_example", // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
  'pMultimedia': "pMultimedia_example", // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
  'pFedCase': "pFedCase_example", // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
  'pActivityContact': "pActivityContact_example", // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \"%\" as a wild-card for advanced searching.
  'pRole': "pRole_example", // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
  'pFedPenalty': "pFedPenalty_example", // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
  'pTotalFedPenalty': "pTotalFedPenalty_example", // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
  'pCostRecovery': "pCostRecovery_example", // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pTotalCostRecovery': "pTotalCostRecovery_example", // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pComplyingActions': "pComplyingActions_example", // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
  'pCompActVal': "pCompActVal_example", // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
  'pTotalCompActVal': "pTotalCompActVal_example", // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
  'pSepCats': "pSepCats_example", // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
  'pSepVal': "pSepVal_example", // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
  'pTotalSepVal': "pTotalSepVal_example", // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
  'pLodgedDate': "pLodgedDate_example", // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
  'pEnteredDate': "pEnteredDate_example", // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
  'pFacilityId': "pFacilityId_example", // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
  'pFacCity': "pFacCity_example", // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
  'pFacZip': "pFacZip_example", // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
  'pFacCounty': "pFacCounty_example", // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
  'pCaseSummary': "pCaseSummary_example", // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pCaseSummaryType': "pCaseSummaryType_example", // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pC1lat': 3.4, // Number | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC1lon': 3.4, // Number | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lat': 3.4, // Number | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lon': 3.4, // Number | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pVoluntary': "pVoluntary_example", // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
  'pFedIndicator': "pFedIndicator_example", // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pCivilCriminalIndicator': "pCivilCriminalIndicator_example", // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'mapset': "'1400'", // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4, // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
  'pOcmapFy': "pOcmapFy_example", // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pHasMap': "pHasMap_example" // String | 
};
apiInstance.caseRestServicesGetCaseInfoGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] 
 **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] 
 **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] 
 **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] 
 **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] 
 **pNameType** | **String**| Case Name Filter Modifier. | [optional] 
 **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \&quot;%\&quot; as a wildcard for more complex filtering. | [optional] 
 **pCourtDocketNumber** | **String**|  | [optional] 
 **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] 
 **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] 
 **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] 
 **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] 
 **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] 
 **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] 
 **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] 
 **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] 
 **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] 
 **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] 
 **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] 
 **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \&quot;%\&quot; as a wild-card match for more complex searches. | [optional] 
 **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] 
 **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] 
 **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] 
 **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] 
 **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \&quot;%\&quot; as a wild-card for advanced searching. | [optional] 
 **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] 
 **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] 
 **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] 
 **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] 
 **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] 
 **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] 
 **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] 
 **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] 
 **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] 
 **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] 
 **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] 
 **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] 
 **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] 
 **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pC1lat** | **Number**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC1lon** | **Number**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lat** | **Number**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lon** | **Number**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] 
 **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to &#39;1400&#39;]
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 
 **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pHasMap** | **String**|  | [optional] 

### Return type

[**CaseRestServicesGetCaseInfoGet200Response**](CaseRestServicesGetCaseInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetCaseInfoPost

> CaseRestServicesGetCaseInfoGet200Response caseRestServicesGetCaseInfoPost(opts)

Enforcement Case Search (new version)

The get_case_info service end point searches for civil enforcement and criminal cases based on the provided selection criteria and returns either individual cases or clusters of case facility locations.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pCaseCategory': "pCaseCategory_example", // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
  'pCaseStatus': "pCaseStatus_example", // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
  'pMilestone': "pMilestone_example", // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
  'pFromDate': "pFromDate_example", // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
  'pToDate': "pToDate_example", // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
  'pMilestoneFy': "pMilestoneFy_example", // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
  'pName': "pName_example", // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
  'pNameType': "pNameType_example", // String | Case Name Filter Modifier.
  'pCaseNumber': "pCaseNumber_example", // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
  'pDocketNumber': "pDocketNumber_example", // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\"%\\\" as a wildcard for more complex filtering.
  'pCourtDocketNumber': "pCourtDocketNumber_example", // String | 
  'pActivityNumber': "pActivityNumber_example", // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
  'pCaseLead': "pCaseLead_example", // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
  'pCaseSensFlg': "pCaseSensFlg_example", // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
  'pRegion': "pRegion_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pState': "pState_example", // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
  'pDistrict': "pDistrict_example", // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
  'pSicAoNaics': "pSicAoNaics_example", // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
  'pSicPrimaryFlg': "pSicPrimaryFlg_example", // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
  'pSicFrsFlg': "pSicFrsFlg_example", // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
  'pNaics': "pNaics_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pNaicsPrimaryFlg': "pNaicsPrimaryFlg_example", // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
  'pNaicsFrsFlg': "pNaicsFrsFlg_example", // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
  'pEnfType': "pEnfType_example", // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pCpCitation': "pCpCitation_example", // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pRankOrder': "pRankOrder_example", // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
  'pEnfProgram': "pEnfProgram_example", // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
  'pViolation': "pViolation_example", // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pPriorityArea': "pPriorityArea_example", // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
  'pPriorityAreaDesc': "pPriorityAreaDesc_example", // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\"%\\\" as a wild-card match for more complex searches.
  'pTribal': "pTribal_example", // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
  'pOecaCore': "pOecaCore_example", // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
  'pMultimedia': "pMultimedia_example", // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
  'pFedCase': "pFedCase_example", // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
  'pActivityContact': "pActivityContact_example", // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\"%\\\" as a wild-card for advanced searching.
  'pRole': "pRole_example", // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
  'pFedPenalty': "pFedPenalty_example", // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
  'pTotalFedPenalty': "pTotalFedPenalty_example", // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
  'pCostRecovery': "pCostRecovery_example", // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pTotalCostRecovery': "pTotalCostRecovery_example", // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pComplyingActions': "pComplyingActions_example", // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
  'pCompActVal': "pCompActVal_example", // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
  'pTotalCompActVal': "pTotalCompActVal_example", // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
  'pSepCats': "pSepCats_example", // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
  'pSepVal': "pSepVal_example", // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
  'pTotalSepVal': "pTotalSepVal_example", // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
  'pLodgedDate': "pLodgedDate_example", // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
  'pEnteredDate': "pEnteredDate_example", // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
  'pFacilityId': "pFacilityId_example", // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
  'pFacCity': "pFacCity_example", // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
  'pFacZip': "pFacZip_example", // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
  'pFacCounty': "pFacCounty_example", // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
  'pCaseSummary': "pCaseSummary_example", // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pCaseSummaryType': "pCaseSummaryType_example", // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pC1lat': 3.4, // Number | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC1lon': 3.4, // Number | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lat': 3.4, // Number | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lon': 3.4, // Number | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pVoluntary': "pVoluntary_example", // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
  'pFedIndicator': "pFedIndicator_example", // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pCivilCriminalIndicator': "pCivilCriminalIndicator_example", // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'mapset': "'1400'", // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4, // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
  'pOcmapFy': "pOcmapFy_example", // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pHasMap': "pHasMap_example" // String | 
};
apiInstance.caseRestServicesGetCaseInfoPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] 
 **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] 
 **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] 
 **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] 
 **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] 
 **pNameType** | **String**| Case Name Filter Modifier. | [optional] 
 **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\&quot;%\\\&quot; as a wildcard for more complex filtering. | [optional] 
 **pCourtDocketNumber** | **String**|  | [optional] 
 **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] 
 **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] 
 **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] 
 **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] 
 **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] 
 **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] 
 **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] 
 **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] 
 **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] 
 **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] 
 **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] 
 **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\&quot;%\\\&quot; as a wild-card match for more complex searches. | [optional] 
 **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] 
 **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] 
 **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] 
 **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] 
 **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\&quot;%\\\&quot; as a wild-card for advanced searching. | [optional] 
 **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] 
 **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] 
 **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] 
 **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] 
 **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] 
 **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] 
 **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] 
 **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] 
 **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] 
 **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] 
 **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] 
 **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] 
 **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] 
 **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pC1lat** | **Number**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC1lon** | **Number**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lat** | **Number**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lon** | **Number**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] 
 **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to &#39;1400&#39;]
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 
 **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pHasMap** | **String**|  | [optional] 

### Return type

[**CaseRestServicesGetCaseInfoGet200Response**](CaseRestServicesGetCaseInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## caseRestServicesGetCaseReportGet

> CaseRestServicesGetCaseReportGet200Response caseRestServicesGetCaseReportGet(opts)

Enforcement Case Summary Report Search

The get_case_report service endpoint returns a complex object of civil enforcement case details based on the provided case id.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'pId': "pId_example", // String | Case Number. Enter the case number identifier to retrieve the case report.
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesGetCaseReportGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Case Number. Enter the case number identifier to retrieve the case report. | [optional] 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**CaseRestServicesGetCaseReportGet200Response**](CaseRestServicesGetCaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetCaseReportPost

> CaseRestServicesGetCaseReportGet200Response caseRestServicesGetCaseReportPost(opts)

Enforcement Case Summary Report Search

The get_case_report service endpoint returns a complex object of civil enforcement case details based on the provided case id.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'pId': "pId_example", // String | Case Number. Enter the case number identifier to retrieve the case report.
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesGetCaseReportPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Case Number. Enter the case number identifier to retrieve the case report. | [optional] 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**CaseRestServicesGetCaseReportGet200Response**](CaseRestServicesGetCaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## caseRestServicesGetCasesFromFacilityGet

> CaseRestServicesGetCasesFromFacilityGet200Response caseRestServicesGetCasesFromFacilityGet(pId, opts)

Placeholder

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesGetCasesFromFacilityGet(pId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Identifier for the service. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**CaseRestServicesGetCasesFromFacilityGet200Response**](CaseRestServicesGetCasesFromFacilityGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetCasesFromFacilityPost

> CaseRestServicesGetCasesFromFacilityGet200Response caseRestServicesGetCasesFromFacilityPost(pId, opts)

Placeholder

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesGetCasesFromFacilityPost(pId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Identifier for the service. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**CaseRestServicesGetCasesFromFacilityGet200Response**](CaseRestServicesGetCasesFromFacilityGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetCasesGet

> CaseRestServicesGetCasesGet200Response caseRestServicesGetCasesGet(opts)

Enforcement Case Search

The get_cases service end point searches for civil enforcement and criminal cases based on the provided selection criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pCaseCategory': "pCaseCategory_example", // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
  'pCaseStatus': "pCaseStatus_example", // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
  'pViolation': "pViolation_example", // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pMilestone': "pMilestone_example", // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
  'pFromDate': "pFromDate_example", // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
  'pToDate': "pToDate_example", // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
  'pMilestoneFy': "pMilestoneFy_example", // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
  'pName': "pName_example", // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
  'pNameType': "pNameType_example", // String | Case Name Filter Modifier.
  'pCaseNumber': "pCaseNumber_example", // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
  'pDocketNumber': "pDocketNumber_example", // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \"%\" as a wildcard for more complex filtering.
  'pCourtDocketNumber': "pCourtDocketNumber_example", // String | 
  'pActivityNumber': "pActivityNumber_example", // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
  'pCaseLead': "pCaseLead_example", // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
  'pCaseSensFlg': "pCaseSensFlg_example", // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
  'pRegion': "pRegion_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pState': "pState_example", // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
  'pDistrict': "pDistrict_example", // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
  'pSicAoNaics': "pSicAoNaics_example", // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
  'pSicPrimaryFlg': "pSicPrimaryFlg_example", // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
  'pSicFrsFlg': "pSicFrsFlg_example", // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
  'pNaics': "pNaics_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pNaicsPrimaryFlg': "pNaicsPrimaryFlg_example", // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
  'pNaicsFrsFlg': "pNaicsFrsFlg_example", // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
  'pEnfType': "pEnfType_example", // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pCpCitation': "pCpCitation_example", // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pRankOrder': "pRankOrder_example", // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
  'pEnfProgram': "pEnfProgram_example", // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
  'pPriorityArea': "pPriorityArea_example", // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
  'pPriorityAreaDesc': "pPriorityAreaDesc_example", // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \"%\" as a wild-card match for more complex searches.
  'pTribal': "pTribal_example", // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
  'pOecaCore': "pOecaCore_example", // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
  'pMultimedia': "pMultimedia_example", // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
  'pFedCase': "pFedCase_example", // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
  'pActivityContact': "pActivityContact_example", // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \"%\" as a wild-card for advanced searching.
  'pRole': "pRole_example", // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
  'pFedPenalty': "pFedPenalty_example", // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
  'pTotalFedPenalty': "pTotalFedPenalty_example", // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
  'pCostRecovery': "pCostRecovery_example", // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pTotalCostRecovery': "pTotalCostRecovery_example", // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pComplyingActions': "pComplyingActions_example", // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
  'pCompActVal': "pCompActVal_example", // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
  'pTotalCompActVal': "pTotalCompActVal_example", // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
  'pSepCats': "pSepCats_example", // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
  'pSepVal': "pSepVal_example", // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
  'pTotalSepVal': "pTotalSepVal_example", // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
  'pLodgedDate': "pLodgedDate_example", // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
  'pEnteredDate': "pEnteredDate_example", // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
  'pFacilityId': "pFacilityId_example", // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
  'pFacCity': "pFacCity_example", // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
  'pFacZip': "pFacZip_example", // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
  'pFacCounty': "pFacCounty_example", // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
  'pCaseSummary': "pCaseSummary_example", // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pCaseSummaryType': "pCaseSummaryType_example", // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pC1lat': 3.4, // Number | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC1lon': 3.4, // Number | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lat': 3.4, // Number | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lon': 3.4, // Number | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pVoluntary': "pVoluntary_example", // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
  'pFedIndicator': "pFedIndicator_example", // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pCivilCriminalIndicator': "pCivilCriminalIndicator_example", // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'maplist': "maplist_example", // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pOcmapFy': "pOcmapFy_example", // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pHasMap': "pHasMap_example" // String | 
};
apiInstance.caseRestServicesGetCasesGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] 
 **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] 
 **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] 
 **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] 
 **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] 
 **pNameType** | **String**| Case Name Filter Modifier. | [optional] 
 **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \&quot;%\&quot; as a wildcard for more complex filtering. | [optional] 
 **pCourtDocketNumber** | **String**|  | [optional] 
 **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] 
 **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] 
 **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] 
 **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] 
 **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] 
 **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] 
 **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] 
 **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] 
 **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] 
 **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] 
 **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] 
 **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \&quot;%\&quot; as a wild-card match for more complex searches. | [optional] 
 **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] 
 **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] 
 **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] 
 **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] 
 **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \&quot;%\&quot; as a wild-card for advanced searching. | [optional] 
 **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] 
 **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] 
 **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] 
 **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] 
 **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] 
 **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] 
 **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] 
 **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] 
 **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] 
 **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] 
 **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] 
 **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] 
 **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] 
 **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pC1lat** | **Number**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC1lon** | **Number**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lat** | **Number**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lon** | **Number**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] 
 **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pHasMap** | **String**|  | [optional] 

### Return type

[**CaseRestServicesGetCasesGet200Response**](CaseRestServicesGetCasesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetCasesPost

> CaseRestServicesGetCasesGet200Response caseRestServicesGetCasesPost(opts)

Enforcement Case Search

The get_cases service end point searches for civil enforcement and criminal cases based on the provided selection criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pCaseCategory': "pCaseCategory_example", // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
  'pCaseStatus': "pCaseStatus_example", // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
  'pMilestone': "pMilestone_example", // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
  'pFromDate': "pFromDate_example", // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
  'pToDate': "pToDate_example", // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
  'pMilestoneFy': "pMilestoneFy_example", // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
  'pName': "pName_example", // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
  'pNameType': "pNameType_example", // String | Case Name Filter Modifier.
  'pCaseNumber': "pCaseNumber_example", // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
  'pDocketNumber': "pDocketNumber_example", // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\"%\\\" as a wildcard for more complex filtering.
  'pCourtDocketNumber': "pCourtDocketNumber_example", // String | 
  'pActivityNumber': "pActivityNumber_example", // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
  'pCaseLead': "pCaseLead_example", // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
  'pCaseSensFlg': "pCaseSensFlg_example", // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
  'pRegion': "pRegion_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pState': "pState_example", // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
  'pDistrict': "pDistrict_example", // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
  'pSicAoNaics': "pSicAoNaics_example", // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
  'pSicPrimaryFlg': "pSicPrimaryFlg_example", // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
  'pSicFrsFlg': "pSicFrsFlg_example", // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
  'pNaics': "pNaics_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pNaicsPrimaryFlg': "pNaicsPrimaryFlg_example", // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
  'pNaicsFrsFlg': "pNaicsFrsFlg_example", // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
  'pEnfType': "pEnfType_example", // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pCpCitation': "pCpCitation_example", // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pRankOrder': "pRankOrder_example", // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
  'pEnfProgram': "pEnfProgram_example", // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
  'pViolation': "pViolation_example", // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
  'pPriorityArea': "pPriorityArea_example", // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
  'pPriorityAreaDesc': "pPriorityAreaDesc_example", // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\"%\\\" as a wild-card match for more complex searches.
  'pTribal': "pTribal_example", // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
  'pOecaCore': "pOecaCore_example", // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
  'pMultimedia': "pMultimedia_example", // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
  'pFedCase': "pFedCase_example", // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
  'pActivityContact': "pActivityContact_example", // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\"%\\\" as a wild-card for advanced searching.
  'pRole': "pRole_example", // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
  'pFedPenalty': "pFedPenalty_example", // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
  'pTotalFedPenalty': "pTotalFedPenalty_example", // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
  'pCostRecovery': "pCostRecovery_example", // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pTotalCostRecovery': "pTotalCostRecovery_example", // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
  'pComplyingActions': "pComplyingActions_example", // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
  'pCompActVal': "pCompActVal_example", // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
  'pTotalCompActVal': "pTotalCompActVal_example", // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
  'pSepCats': "pSepCats_example", // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
  'pSepVal': "pSepVal_example", // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
  'pTotalSepVal': "pTotalSepVal_example", // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
  'pLodgedDate': "pLodgedDate_example", // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
  'pEnteredDate': "pEnteredDate_example", // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
  'pFacilityId': "pFacilityId_example", // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
  'pFacCity': "pFacCity_example", // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
  'pFacZip': "pFacZip_example", // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
  'pFacCounty': "pFacCounty_example", // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
  'pCaseSummary': "pCaseSummary_example", // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
  'pCaseSummaryType': "pCaseSummaryType_example", // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pC1lat': 3.4, // Number | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC1lon': 3.4, // Number | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lat': 3.4, // Number | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lon': 3.4, // Number | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pVoluntary': "pVoluntary_example", // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
  'pFedIndicator': "pFedIndicator_example", // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pCivilCriminalIndicator': "pCivilCriminalIndicator_example", // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'maplist': "maplist_example", // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pOcmapFy': "pOcmapFy_example", // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pHasMap': "pHasMap_example" // String | 
};
apiInstance.caseRestServicesGetCasesPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] 
 **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] 
 **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] 
 **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] 
 **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] 
 **pNameType** | **String**| Case Name Filter Modifier. | [optional] 
 **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\&quot;%\\\&quot; as a wildcard for more complex filtering. | [optional] 
 **pCourtDocketNumber** | **String**|  | [optional] 
 **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] 
 **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] 
 **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] 
 **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] 
 **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] 
 **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] 
 **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] 
 **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] 
 **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] 
 **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] 
 **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] 
 **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\&quot;%\\\&quot; as a wild-card match for more complex searches. | [optional] 
 **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] 
 **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] 
 **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] 
 **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] 
 **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\&quot;%\\\&quot; as a wild-card for advanced searching. | [optional] 
 **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] 
 **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] 
 **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] 
 **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] 
 **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] 
 **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] 
 **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] 
 **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] 
 **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] 
 **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] 
 **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] 
 **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] 
 **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] 
 **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] 
 **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] 
 **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pC1lat** | **Number**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC1lon** | **Number**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lat** | **Number**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lon** | **Number**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] 
 **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pHasMap** | **String**|  | [optional] 

### Return type

[**CaseRestServicesGetCasesGet200Response**](CaseRestServicesGetCasesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## caseRestServicesGetCrcaseReportGet

> CaseRestServicesGetCrcaseReportGet200Response caseRestServicesGetCrcaseReportGet(opts)

Enforcement Criminal Case Summary Report Search

The get_crcase_report service end point returns a complex object of criminal case detials based on the provided criminal case id.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'pId': "pId_example", // String | Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report.
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'mapset': "'1400'" // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
};
apiInstance.caseRestServicesGetCrcaseReportGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report. | [optional] 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to &#39;1400&#39;]

### Return type

[**CaseRestServicesGetCrcaseReportGet200Response**](CaseRestServicesGetCrcaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetCrcaseReportPost

> CaseRestServicesGetCrcaseReportGet200Response caseRestServicesGetCrcaseReportPost(opts)

Enforcement Criminal Case Summary Report Search

The get_crcase_report service end point returns a complex object of criminal case detials based on the provided criminal case id.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let opts = {
  'pId': "pId_example", // String | Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report.
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesGetCrcaseReportPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report. | [optional] 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**CaseRestServicesGetCrcaseReportGet200Response**](CaseRestServicesGetCrcaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## caseRestServicesGetDownloadGet

> File caseRestServicesGetDownloadGet(qid, opts)

Enforcement Case Download Data Service

Based on the QID obtained from a get_cases query, return a comma separated value (CSV) file of the cases found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.caseRestServicesGetDownloadGet(qid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetDownloadPost

> File caseRestServicesGetDownloadPost(qid, opts)

Enforcement Case Download Data Service

Based on the QID obtained from a get_cases query, return a comma separated value (CSV) file of the cases found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.caseRestServicesGetDownloadPost(qid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## caseRestServicesGetFacilitiesFromCaseGet

> CaseRestServicesGetFacilitiesFromCaseGet200Response caseRestServicesGetFacilitiesFromCaseGet(pId, opts)

Placeholder

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesGetFacilitiesFromCaseGet(pId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Identifier for the service. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**CaseRestServicesGetFacilitiesFromCaseGet200Response**](CaseRestServicesGetFacilitiesFromCaseGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetFacilitiesFromCasePost

> CaseRestServicesGetFacilitiesFromCaseGet200Response caseRestServicesGetFacilitiesFromCasePost(pId, opts)

Placeholder

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesGetFacilitiesFromCasePost(pId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pId** | **String**| Identifier for the service. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**CaseRestServicesGetFacilitiesFromCaseGet200Response**](CaseRestServicesGetFacilitiesFromCaseGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetMapGet

> CaseRestServicesGetMapGet200Response caseRestServicesGetMapGet(qid, opts)

Enforcement Case Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_cases query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'c1Lat': 3.4, // Number | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c1Long': 3.4, // Number | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Lat': 3.4, // Number | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Long': 3.4 // Number | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
};
apiInstance.caseRestServicesGetMapGet(qid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **c1Lat** | **Number**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c1Long** | **Number**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Lat** | **Number**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Long** | **Number**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 

### Return type

[**CaseRestServicesGetMapGet200Response**](CaseRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetMapPost

> CaseRestServicesGetMapGet200Response caseRestServicesGetMapPost(qid, opts)

Enforcement Case Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_cases query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'c1Lat': 3.4, // Number | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c1Long': 3.4, // Number | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Lat': 3.4, // Number | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Long': 3.4, // Number | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'mapset': "'1400'" // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
};
apiInstance.caseRestServicesGetMapPost(qid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **c1Lat** | **Number**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c1Long** | **Number**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Lat** | **Number**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Long** | **Number**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to &#39;1400&#39;]

### Return type

[**CaseRestServicesGetMapGet200Response**](CaseRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## caseRestServicesGetQidGet

> CaseRestServicesGetQidGet200Response caseRestServicesGetQidGet(qid, opts)

Enforcement Case Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_cases query. It then returns a CASES object containing all matching cases. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.caseRestServicesGetQidGet(qid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **pageno** | **Number**| Indicates the number of the page to display. It is used only when the results are paginated. | [optional] [default to 1.0]
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **newsort** | **Number**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] 
 **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**CaseRestServicesGetQidGet200Response**](CaseRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesGetQidPost

> CaseRestServicesGetQidGet200Response caseRestServicesGetQidPost(qid, opts)

Enforcement Case Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_cases query. It then returns a CASES object containing all matching cases. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.CaseEnforcementApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.caseRestServicesGetQidPost(qid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **pageno** | **Number**| Indicates the number of the page to display. It is used only when the results are paginated. | [optional] [default to 1.0]
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **newsort** | **Number**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] 
 **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**CaseRestServicesGetQidGet200Response**](CaseRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


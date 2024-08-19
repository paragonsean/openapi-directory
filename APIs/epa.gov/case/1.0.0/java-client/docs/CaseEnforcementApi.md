# CaseEnforcementApi

All URIs are relative to *https://echodata.epa.gov/echo*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**caseRestServicesGetCaseInfoGet**](CaseEnforcementApi.md#caseRestServicesGetCaseInfoGet) | **GET** /case_rest_services.get_case_info | Enforcement Case Search (new version) |
| [**caseRestServicesGetCaseInfoPost**](CaseEnforcementApi.md#caseRestServicesGetCaseInfoPost) | **POST** /case_rest_services.get_case_info | Enforcement Case Search (new version) |
| [**caseRestServicesGetCaseReportGet**](CaseEnforcementApi.md#caseRestServicesGetCaseReportGet) | **GET** /case_rest_services.get_case_report | Enforcement Case Summary Report Search |
| [**caseRestServicesGetCaseReportPost**](CaseEnforcementApi.md#caseRestServicesGetCaseReportPost) | **POST** /case_rest_services.get_case_report | Enforcement Case Summary Report Search |
| [**caseRestServicesGetCasesFromFacilityGet**](CaseEnforcementApi.md#caseRestServicesGetCasesFromFacilityGet) | **GET** /case_rest_services.get_cases_from_facility | Placeholder |
| [**caseRestServicesGetCasesFromFacilityPost**](CaseEnforcementApi.md#caseRestServicesGetCasesFromFacilityPost) | **POST** /case_rest_services.get_cases_from_facility | Placeholder |
| [**caseRestServicesGetCasesGet**](CaseEnforcementApi.md#caseRestServicesGetCasesGet) | **GET** /case_rest_services.get_cases | Enforcement Case Search |
| [**caseRestServicesGetCasesPost**](CaseEnforcementApi.md#caseRestServicesGetCasesPost) | **POST** /case_rest_services.get_cases | Enforcement Case Search |
| [**caseRestServicesGetCrcaseReportGet**](CaseEnforcementApi.md#caseRestServicesGetCrcaseReportGet) | **GET** /case_rest_services.get_crcase_report | Enforcement Criminal Case Summary Report Search |
| [**caseRestServicesGetCrcaseReportPost**](CaseEnforcementApi.md#caseRestServicesGetCrcaseReportPost) | **POST** /case_rest_services.get_crcase_report | Enforcement Criminal Case Summary Report Search |
| [**caseRestServicesGetDownloadGet**](CaseEnforcementApi.md#caseRestServicesGetDownloadGet) | **GET** /case_rest_services.get_download | Enforcement Case Download Data Service |
| [**caseRestServicesGetDownloadPost**](CaseEnforcementApi.md#caseRestServicesGetDownloadPost) | **POST** /case_rest_services.get_download | Enforcement Case Download Data Service |
| [**caseRestServicesGetFacilitiesFromCaseGet**](CaseEnforcementApi.md#caseRestServicesGetFacilitiesFromCaseGet) | **GET** /case_rest_services.get_facilities_from_case | Placeholder |
| [**caseRestServicesGetFacilitiesFromCasePost**](CaseEnforcementApi.md#caseRestServicesGetFacilitiesFromCasePost) | **POST** /case_rest_services.get_facilities_from_case | Placeholder |
| [**caseRestServicesGetMapGet**](CaseEnforcementApi.md#caseRestServicesGetMapGet) | **GET** /case_rest_services.get_map | Enforcement Case Map Service |
| [**caseRestServicesGetMapPost**](CaseEnforcementApi.md#caseRestServicesGetMapPost) | **POST** /case_rest_services.get_map | Enforcement Case Map Service |
| [**caseRestServicesGetQidGet**](CaseEnforcementApi.md#caseRestServicesGetQidGet) | **GET** /case_rest_services.get_qid | Enforcement Case Paginated Results Service |
| [**caseRestServicesGetQidPost**](CaseEnforcementApi.md#caseRestServicesGetQidPost) | **POST** /case_rest_services.get_qid | Enforcement Case Paginated Results Service |


<a id="caseRestServicesGetCaseInfoGet"></a>
# **caseRestServicesGetCaseInfoGet**
> CaseRestServicesGetCaseInfoGet200Response caseRestServicesGetCaseInfoGet(output, pCaseCategory, pCaseStatus, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pViolation, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, mapset, paramCallback, qcolumns, pPrettyPrint, pOcmapFy, pQs, pHasMap)

Enforcement Case Search (new version)

The get_case_info service end point searches for civil enforcement and criminal cases based on the provided selection criteria and returns either individual cases or clusters of case facility locations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pCaseCategory = "pCaseCategory_example"; // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
    String pCaseStatus = "pCaseStatus_example"; // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    String pMilestone = "pMilestone_example"; // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    String pFromDate = "pFromDate_example"; // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    String pToDate = "pToDate_example"; // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    String pMilestoneFy = "pMilestoneFy_example"; // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    String pName = "pName_example"; // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    String pNameType = "pNameType_example"; // String | Case Name Filter Modifier.
    String pCaseNumber = "pCaseNumber_example"; // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    String pDocketNumber = "pDocketNumber_example"; // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \"%\" as a wildcard for more complex filtering.
    String pCourtDocketNumber = "pCourtDocketNumber_example"; // String | 
    String pActivityNumber = "pActivityNumber_example"; // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
    String pCaseLead = "E"; // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
    String pCaseSensFlg = "pCaseSensFlg_example"; // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    String pRegion = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pState = "pState_example"; // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    String pDistrict = "pDistrict_example"; // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    String pSicAoNaics = "AND"; // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    String pSicPrimaryFlg = "Y"; // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    String pSicFrsFlg = "Y"; // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    String pNaics = "pNaics_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pNaicsPrimaryFlg = "Y"; // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    String pNaicsFrsFlg = "Y"; // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    String pEnfType = "pEnfType_example"; // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pLaw = "pLaw_example"; // String | Law Statute Code Filter.  Enter a single statute code to limit results.
    String pSection = "pSection_example"; // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    String pCpCitation = "pCpCitation_example"; // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pRankOrder = "1"; // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    String pEnfProgram = "pEnfProgram_example"; // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    String pViolation = "pViolation_example"; // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pPriorityArea = "pPriorityArea_example"; // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    String pPriorityAreaDesc = "pPriorityAreaDesc_example"; // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \"%\" as a wild-card match for more complex searches.
    String pTribal = "Y"; // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    String pOecaCore = "Y"; // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    String pMultimedia = "Y"; // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    String pFedCase = "Y"; // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    String pActivityContact = "pActivityContact_example"; // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \"%\" as a wild-card for advanced searching.
    String pRole = "pRole_example"; // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    String pFedPenalty = "ANY"; // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
    String pTotalFedPenalty = "pTotalFedPenalty_example"; // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    String pCostRecovery = "pCostRecovery_example"; // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pTotalCostRecovery = "pTotalCostRecovery_example"; // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pComplyingActions = "pComplyingActions_example"; // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    String pCompActVal = "ANY"; // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    String pTotalCompActVal = "pTotalCompActVal_example"; // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    String pSepCats = "pSepCats_example"; // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    String pSepVal = "ANY"; // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
    String pTotalSepVal = "pTotalSepVal_example"; // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
    String pLodgedDate = "pLodgedDate_example"; // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    String pEnteredDate = "pEnteredDate_example"; // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    String pFacilityId = "pFacilityId_example"; // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    String pFacCity = "pFacCity_example"; // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    String pFacZip = "pFacZip_example"; // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    String pFacCounty = "pFacCounty_example"; // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    String pCaseSummary = "pCaseSummary_example"; // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pCaseSummaryType = "ALL"; // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pVoluntary = "pVoluntary_example"; // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    String pFedIndicator = "pFedIndicator_example"; // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pCivilCriminalIndicator = "CI"; // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String mapset = "1400"; // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    String pOcmapFy = "pOcmapFy_example"; // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pHasMap = "pHasMap_example"; // String | 
    try {
      CaseRestServicesGetCaseInfoGet200Response result = apiInstance.caseRestServicesGetCaseInfoGet(output, pCaseCategory, pCaseStatus, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pViolation, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, mapset, paramCallback, qcolumns, pPrettyPrint, pOcmapFy, pQs, pHasMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCaseInfoGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] |
| **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] |
| **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] |
| **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] |
| **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] |
| **pNameType** | **String**| Case Name Filter Modifier. | [optional] |
| **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \&quot;%\&quot; as a wildcard for more complex filtering. | [optional] |
| **pCourtDocketNumber** | **String**|  | [optional] |
| **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] |
| **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] [enum: E, S] |
| **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] |
| **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] |
| **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] [enum: AND, OR] |
| **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] [enum: Y, N] |
| **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] [enum: Y, N] |
| **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] |
| **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] [enum: 1, 0] |
| **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] |
| **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \&quot;%\&quot; as a wild-card match for more complex searches. | [optional] |
| **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] [enum: Y, N] |
| **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] [enum: Y, N] |
| **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] [enum: Y, N] |
| **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] [enum: Y, N] |
| **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \&quot;%\&quot; as a wild-card for advanced searching. | [optional] |
| **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] |
| **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] [enum: ANY, LE5000, GT5000, GT50000, GT100000, GT500000, GT1000000, GT2500000] |
| **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] |
| **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] [enum: ANY, LE5000, GT5000, GT100000, GT1000000, GT50000000] |
| **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] |
| **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] [enum: ANY, LE10000, GT10000, GT50000, GT100000, GT500000, GT1000000] |
| **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] |
| **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] |
| **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] |
| **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] |
| **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] |
| **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] |
| **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] |
| **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] [enum: ALL, CONTAINS, WITHIN] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] |
| **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] [enum: CI, CR, ALL] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to 1400] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |
| **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pHasMap** | **String**|  | [optional] |

### Return type

[**CaseRestServicesGetCaseInfoGet200Response**](CaseRestServicesGetCaseInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of cases that meet the selection criteria. |  -  |

<a id="caseRestServicesGetCaseInfoPost"></a>
# **caseRestServicesGetCaseInfoPost**
> CaseRestServicesGetCaseInfoGet200Response caseRestServicesGetCaseInfoPost(output, pCaseCategory, pCaseStatus, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pViolation, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, mapset, paramCallback, qcolumns, pPrettyPrint, pOcmapFy, pQs, pHasMap)

Enforcement Case Search (new version)

The get_case_info service end point searches for civil enforcement and criminal cases based on the provided selection criteria and returns either individual cases or clusters of case facility locations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pCaseCategory = "pCaseCategory_example"; // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
    String pCaseStatus = "pCaseStatus_example"; // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    String pMilestone = "pMilestone_example"; // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    String pFromDate = "pFromDate_example"; // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    String pToDate = "pToDate_example"; // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    String pMilestoneFy = "pMilestoneFy_example"; // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    String pName = "pName_example"; // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    String pNameType = "pNameType_example"; // String | Case Name Filter Modifier.
    String pCaseNumber = "pCaseNumber_example"; // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    String pDocketNumber = "pDocketNumber_example"; // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\"%\\\" as a wildcard for more complex filtering.
    String pCourtDocketNumber = "pCourtDocketNumber_example"; // String | 
    String pActivityNumber = "pActivityNumber_example"; // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
    String pCaseLead = "E"; // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
    String pCaseSensFlg = "pCaseSensFlg_example"; // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    String pRegion = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pState = "pState_example"; // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    String pDistrict = "pDistrict_example"; // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    String pSicAoNaics = "AND"; // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    String pSicPrimaryFlg = "Y"; // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    String pSicFrsFlg = "Y"; // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    String pNaics = "pNaics_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pNaicsPrimaryFlg = "Y"; // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    String pNaicsFrsFlg = "Y"; // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    String pEnfType = "pEnfType_example"; // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pLaw = "pLaw_example"; // String | Law Statute Code Filter.  Enter a single statute code to limit results.
    String pSection = "pSection_example"; // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    String pCpCitation = "pCpCitation_example"; // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pRankOrder = "1"; // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    String pEnfProgram = "pEnfProgram_example"; // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    String pViolation = "pViolation_example"; // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pPriorityArea = "pPriorityArea_example"; // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    String pPriorityAreaDesc = "pPriorityAreaDesc_example"; // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\"%\\\" as a wild-card match for more complex searches.
    String pTribal = "Y"; // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    String pOecaCore = "Y"; // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    String pMultimedia = "Y"; // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    String pFedCase = "Y"; // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    String pActivityContact = "pActivityContact_example"; // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\"%\\\" as a wild-card for advanced searching.
    String pRole = "pRole_example"; // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    String pFedPenalty = "ANY"; // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
    String pTotalFedPenalty = "pTotalFedPenalty_example"; // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    String pCostRecovery = "pCostRecovery_example"; // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pTotalCostRecovery = "pTotalCostRecovery_example"; // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pComplyingActions = "pComplyingActions_example"; // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    String pCompActVal = "ANY"; // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    String pTotalCompActVal = "pTotalCompActVal_example"; // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    String pSepCats = "pSepCats_example"; // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    String pSepVal = "ANY"; // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
    String pTotalSepVal = "pTotalSepVal_example"; // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
    String pLodgedDate = "pLodgedDate_example"; // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    String pEnteredDate = "pEnteredDate_example"; // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    String pFacilityId = "pFacilityId_example"; // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    String pFacCity = "pFacCity_example"; // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    String pFacZip = "pFacZip_example"; // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    String pFacCounty = "pFacCounty_example"; // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    String pCaseSummary = "pCaseSummary_example"; // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pCaseSummaryType = "ALL"; // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pVoluntary = "pVoluntary_example"; // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    String pFedIndicator = "pFedIndicator_example"; // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pCivilCriminalIndicator = "CI"; // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String mapset = "1400"; // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    BigDecimal pPrettyPrint = new BigDecimal(78); // BigDecimal | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
    String pOcmapFy = "pOcmapFy_example"; // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pHasMap = "pHasMap_example"; // String | 
    try {
      CaseRestServicesGetCaseInfoGet200Response result = apiInstance.caseRestServicesGetCaseInfoPost(output, pCaseCategory, pCaseStatus, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pViolation, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, mapset, paramCallback, qcolumns, pPrettyPrint, pOcmapFy, pQs, pHasMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCaseInfoPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] |
| **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] |
| **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] |
| **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] |
| **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] |
| **pNameType** | **String**| Case Name Filter Modifier. | [optional] |
| **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\&quot;%\\\&quot; as a wildcard for more complex filtering. | [optional] |
| **pCourtDocketNumber** | **String**|  | [optional] |
| **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] |
| **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] [enum: E, S] |
| **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] |
| **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] |
| **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] [enum: AND, OR] |
| **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] [enum: Y, N] |
| **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] [enum: Y, N] |
| **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] |
| **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] [enum: 1, 0] |
| **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] |
| **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\&quot;%\\\&quot; as a wild-card match for more complex searches. | [optional] |
| **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] [enum: Y, N] |
| **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] [enum: Y, N] |
| **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] [enum: Y, N] |
| **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] [enum: Y, N] |
| **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\&quot;%\\\&quot; as a wild-card for advanced searching. | [optional] |
| **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] |
| **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] [enum: ANY, LE5000, GT5000, GT50000, GT100000, GT500000, GT1000000, GT2500000] |
| **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] |
| **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] [enum: ANY, LE5000, GT5000, GT100000, GT1000000, GT50000000] |
| **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] |
| **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] [enum: ANY, LE10000, GT10000, GT50000, GT100000, GT500000, GT1000000] |
| **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] |
| **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] |
| **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] |
| **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] |
| **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] |
| **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] |
| **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] |
| **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] [enum: ALL, CONTAINS, WITHIN] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] |
| **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] [enum: CI, CR, ALL] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to 1400] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pPrettyPrint** | **BigDecimal**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] |
| **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pHasMap** | **String**|  | [optional] |

### Return type

[**CaseRestServicesGetCaseInfoGet200Response**](CaseRestServicesGetCaseInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of cases that meet the selection criteria. |  -  |

<a id="caseRestServicesGetCaseReportGet"></a>
# **caseRestServicesGetCaseReportGet**
> CaseRestServicesGetCaseReportGet200Response caseRestServicesGetCaseReportGet(pId, output, paramCallback)

Enforcement Case Summary Report Search

The get_case_report service endpoint returns a complex object of civil enforcement case details based on the provided case id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Case Number. Enter the case number identifier to retrieve the case report.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      CaseRestServicesGetCaseReportGet200Response result = apiInstance.caseRestServicesGetCaseReportGet(pId, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCaseReportGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Case Number. Enter the case number identifier to retrieve the case report. | [optional] |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**CaseRestServicesGetCaseReportGet200Response**](CaseRestServicesGetCaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a complex object containing detailed case information for the provided Case Identifier. |  -  |

<a id="caseRestServicesGetCaseReportPost"></a>
# **caseRestServicesGetCaseReportPost**
> CaseRestServicesGetCaseReportGet200Response caseRestServicesGetCaseReportPost(pId, output, paramCallback)

Enforcement Case Summary Report Search

The get_case_report service endpoint returns a complex object of civil enforcement case details based on the provided case id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Case Number. Enter the case number identifier to retrieve the case report.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      CaseRestServicesGetCaseReportGet200Response result = apiInstance.caseRestServicesGetCaseReportPost(pId, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCaseReportPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Case Number. Enter the case number identifier to retrieve the case report. | [optional] |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**CaseRestServicesGetCaseReportGet200Response**](CaseRestServicesGetCaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a complex object containing detailed case information for the provided Case Identifier. |  -  |

<a id="caseRestServicesGetCasesFromFacilityGet"></a>
# **caseRestServicesGetCasesFromFacilityGet**
> CaseRestServicesGetCasesFromFacilityGet200Response caseRestServicesGetCasesFromFacilityGet(pId, output, paramCallback)

Placeholder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      CaseRestServicesGetCasesFromFacilityGet200Response result = apiInstance.caseRestServicesGetCasesFromFacilityGet(pId, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCasesFromFacilityGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**CaseRestServicesGetCasesFromFacilityGet200Response**](CaseRestServicesGetCasesFromFacilityGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results |  -  |

<a id="caseRestServicesGetCasesFromFacilityPost"></a>
# **caseRestServicesGetCasesFromFacilityPost**
> CaseRestServicesGetCasesFromFacilityGet200Response caseRestServicesGetCasesFromFacilityPost(pId, output, paramCallback)

Placeholder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      CaseRestServicesGetCasesFromFacilityGet200Response result = apiInstance.caseRestServicesGetCasesFromFacilityPost(pId, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCasesFromFacilityPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**CaseRestServicesGetCasesFromFacilityGet200Response**](CaseRestServicesGetCasesFromFacilityGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results |  -  |

<a id="caseRestServicesGetCasesGet"></a>
# **caseRestServicesGetCasesGet**
> CaseRestServicesGetCasesGet200Response caseRestServicesGetCasesGet(output, pCaseCategory, pCaseStatus, pViolation, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, maplist, tablelist, paramCallback, qcolumns, pOcmapFy, pQs, pHasMap)

Enforcement Case Search

The get_cases service end point searches for civil enforcement and criminal cases based on the provided selection criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pCaseCategory = "pCaseCategory_example"; // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
    String pCaseStatus = "pCaseStatus_example"; // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    String pViolation = "pViolation_example"; // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pMilestone = "pMilestone_example"; // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    String pFromDate = "pFromDate_example"; // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    String pToDate = "pToDate_example"; // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    String pMilestoneFy = "pMilestoneFy_example"; // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    String pName = "pName_example"; // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    String pNameType = "pNameType_example"; // String | Case Name Filter Modifier.
    String pCaseNumber = "pCaseNumber_example"; // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    String pDocketNumber = "pDocketNumber_example"; // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \"%\" as a wildcard for more complex filtering.
    String pCourtDocketNumber = "pCourtDocketNumber_example"; // String | 
    String pActivityNumber = "pActivityNumber_example"; // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
    String pCaseLead = "E"; // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
    String pCaseSensFlg = "pCaseSensFlg_example"; // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    String pRegion = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pState = "pState_example"; // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    String pDistrict = "pDistrict_example"; // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    String pSicAoNaics = "AND"; // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    String pSicPrimaryFlg = "Y"; // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    String pSicFrsFlg = "Y"; // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    String pNaics = "pNaics_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pNaicsPrimaryFlg = "Y"; // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    String pNaicsFrsFlg = "Y"; // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    String pEnfType = "pEnfType_example"; // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pLaw = "pLaw_example"; // String | Law Statute Code Filter.  Enter a single statute code to limit results.
    String pSection = "pSection_example"; // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    String pCpCitation = "pCpCitation_example"; // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pRankOrder = "1"; // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    String pEnfProgram = "pEnfProgram_example"; // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    String pPriorityArea = "pPriorityArea_example"; // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    String pPriorityAreaDesc = "pPriorityAreaDesc_example"; // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \"%\" as a wild-card match for more complex searches.
    String pTribal = "Y"; // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    String pOecaCore = "Y"; // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    String pMultimedia = "Y"; // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    String pFedCase = "Y"; // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    String pActivityContact = "pActivityContact_example"; // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \"%\" as a wild-card for advanced searching.
    String pRole = "pRole_example"; // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    String pFedPenalty = "ANY"; // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
    String pTotalFedPenalty = "pTotalFedPenalty_example"; // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    String pCostRecovery = "pCostRecovery_example"; // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pTotalCostRecovery = "pTotalCostRecovery_example"; // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pComplyingActions = "pComplyingActions_example"; // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    String pCompActVal = "ANY"; // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    String pTotalCompActVal = "pTotalCompActVal_example"; // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    String pSepCats = "pSepCats_example"; // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    String pSepVal = "ANY"; // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
    String pTotalSepVal = "pTotalSepVal_example"; // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
    String pLodgedDate = "pLodgedDate_example"; // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    String pEnteredDate = "pEnteredDate_example"; // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    String pFacilityId = "pFacilityId_example"; // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    String pFacCity = "pFacCity_example"; // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    String pFacZip = "pFacZip_example"; // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    String pFacCounty = "pFacCounty_example"; // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    String pCaseSummary = "pCaseSummary_example"; // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pCaseSummaryType = "ALL"; // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pVoluntary = "pVoluntary_example"; // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    String pFedIndicator = "pFedIndicator_example"; // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pCivilCriminalIndicator = "CI"; // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    String pOcmapFy = "pOcmapFy_example"; // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pHasMap = "pHasMap_example"; // String | 
    try {
      CaseRestServicesGetCasesGet200Response result = apiInstance.caseRestServicesGetCasesGet(output, pCaseCategory, pCaseStatus, pViolation, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, maplist, tablelist, paramCallback, qcolumns, pOcmapFy, pQs, pHasMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCasesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] |
| **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] |
| **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] |
| **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] |
| **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] |
| **pNameType** | **String**| Case Name Filter Modifier. | [optional] |
| **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \&quot;%\&quot; as a wildcard for more complex filtering. | [optional] |
| **pCourtDocketNumber** | **String**|  | [optional] |
| **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] |
| **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] [enum: E, S] |
| **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] |
| **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] |
| **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] [enum: AND, OR] |
| **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] [enum: Y, N] |
| **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] [enum: Y, N] |
| **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] |
| **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] [enum: 1, 0] |
| **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] |
| **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \&quot;%\&quot; as a wild-card match for more complex searches. | [optional] |
| **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] [enum: Y, N] |
| **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] [enum: Y, N] |
| **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] [enum: Y, N] |
| **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] [enum: Y, N] |
| **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \&quot;%\&quot; as a wild-card for advanced searching. | [optional] |
| **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] |
| **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] [enum: ANY, LE5000, GT5000, GT50000, GT100000, GT500000, GT1000000, GT2500000] |
| **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] |
| **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] [enum: ANY, LE5000, GT5000, GT100000, GT1000000, GT50000000] |
| **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] |
| **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] [enum: ANY, LE10000, GT10000, GT50000, GT100000, GT500000, GT1000000] |
| **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] |
| **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] |
| **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] |
| **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] |
| **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] |
| **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] |
| **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] |
| **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] [enum: ALL, CONTAINS, WITHIN] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] |
| **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] [enum: CI, CR, ALL] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pHasMap** | **String**|  | [optional] |

### Return type

[**CaseRestServicesGetCasesGet200Response**](CaseRestServicesGetCasesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of cases that meet the selection criteria. |  -  |

<a id="caseRestServicesGetCasesPost"></a>
# **caseRestServicesGetCasesPost**
> CaseRestServicesGetCasesGet200Response caseRestServicesGetCasesPost(output, pCaseCategory, pCaseStatus, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pViolation, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, maplist, tablelist, paramCallback, qcolumns, pOcmapFy, pQs, pHasMap)

Enforcement Case Search

The get_cases service end point searches for civil enforcement and criminal cases based on the provided selection criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String pCaseCategory = "pCaseCategory_example"; // String | Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR = Administrative - Formal - AIF = Administrative - Informal - JDC = Judicial
    String pCaseStatus = "pCaseStatus_example"; // String | Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list.
    String pMilestone = "pMilestone_example"; // String | Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list.
    String pFromDate = "pFromDate_example"; // String | Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option.
    String pToDate = "pToDate_example"; // String | Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option.
    String pMilestoneFy = "pMilestoneFy_example"; // String | Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year.
    String pName = "pName_example"; // String | Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required.
    String pNameType = "pNameType_example"; // String | Case Name Filter Modifier.
    String pCaseNumber = "pCaseNumber_example"; // String | Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list.
    String pDocketNumber = "pDocketNumber_example"; // String | DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\"%\\\" as a wildcard for more complex filtering.
    String pCourtDocketNumber = "pCourtDocketNumber_example"; // String | 
    String pActivityNumber = "pActivityNumber_example"; // String | Case Activity Number Filter.  Enter a single case activity number to filter results.
    String pCaseLead = "E"; // String | Case Lead Limiter.  Enter E or S to limit results. - E = EPA is the case lead. - S = The state is the case lead.
    String pCaseSensFlg = "pCaseSensFlg_example"; // String | Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data.
    String pRegion = "01"; // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
    String pState = "pState_example"; // String | Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list.
    String pDistrict = "pDistrict_example"; // String | Case Location Court District Limiter.  Enter a single state court district code to limit results.
    String pSic = "pSic_example"; // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.
    String pSicAoNaics = "AND"; // String | Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND = Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR = Search will return results having either the provided SIC code(s) or the provided NAICS code(s).
    String pSicPrimaryFlg = "Y"; // String | Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only.
    String pSicFrsFlg = "Y"; // String | Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets.
    String pNaics = "pNaics_example"; // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
    String pNaicsPrimaryFlg = "Y"; // String | Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only.
    String pNaicsFrsFlg = "Y"; // String | Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets.
    String pEnfType = "pEnfType_example"; // String | Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pLaw = "pLaw_example"; // String | Law Statute Code Filter.  Enter a single statute code to limit results.
    String pSection = "pSection_example"; // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
    String pCpCitation = "pCpCitation_example"; // String | Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pRankOrder = "1"; // String | Law Status Rank Order Limiter.  Enter a single integer rank order to limit results.
    String pEnfProgram = "pEnfProgram_example"; // String | Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.  
    String pViolation = "pViolation_example"; // String | Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list.
    String pPriorityArea = "pPriorityArea_example"; // String | Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list.
    String pPriorityAreaDesc = "pPriorityAreaDesc_example"; // String | Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\"%\\\" as a wild-card match for more complex searches.
    String pTribal = "Y"; // String | Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land.
    String pOecaCore = "Y"; // String | OECA Core Program Flag.  Enter Y or N to include or exclude core program cases.
    String pMultimedia = "Y"; // String | Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases.
    String pFedCase = "Y"; // String | Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities.
    String pActivityContact = "pActivityContact_example"; // String | Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\"%\\\" as a wild-card for advanced searching.
    String pRole = "pRole_example"; // String | Activity Contact Role Code Filter.  Enter a single role code to restrict results.
    String pFedPenalty = "ANY"; // String | Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY = cases with any penalty amount. - LE5000 = cases with penalty amount less than or equal to $5,000. - GT5000 = cases with penalty amount more than $5,000. - GT50000 = cases with penalty amount more than $50,000. - GT100000 = cases with penalty amount more than $100,000. - GT500000 = cases with penalty amount more than $500,000. - GT1000000 = cases with penalty amount more than $1,000,000. - GT2500000 = cases with penalty amount more than $2,500,000.
    String pTotalFedPenalty = "pTotalFedPenalty_example"; // String | Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY = Cases with any federal penalty greater than zero. - LEXX = Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with federal penalty greater than the given amount.
    String pCostRecovery = "pCostRecovery_example"; // String | Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pTotalCostRecovery = "pTotalCostRecovery_example"; // String | Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY = Cases with any cost recovery amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount.
    String pComplyingActions = "pComplyingActions_example"; // String | Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list.
    String pCompActVal = "ANY"; // String | Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY = Cases with any compliance cost amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount.
    String pTotalCompActVal = "pTotalCompActVal_example"; // String | Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY = Cases with any total compliance action amount greater than zero. - LEXX = Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX = Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount.
    String pSepCats = "pSepCats_example"; // String | Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list.
    String pSepVal = "ANY"; // String | Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP activity amount. - LE10000 = return cases with SEP activity amount less than or equal to $10,000. - GT10000 = return cases with SEP activity amount greater than $10,000. - GT50000 = return cases with SEP activity amount greater than $50,000. - GT100000 = return cases with SEP activity amount greater than $100,000. - GT500000 = return cases with SEP activity amount greater than $500,000. - GT1000000 = return cases with SEP activity amount greater than $1,000,000.
    String pTotalSepVal = "pTotalSepVal_example"; // String | Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY = return cases with any SEP total amount. - LE10000 = return cases with SEP total amount less than or equal to $10,000. - GT10000 = return cases with SEP total amount greater than $10,000. - GT50000 = return cases with SEP total amount greater than $50,000. - GT100000 = return cases with SEP total amount greater than $100,000. - GT500000 = return cases with SEP total amount greater than $500,000. - GT1000000 = return cases with SEP total amount greater than $1,000,000.
    String pLodgedDate = "pLodgedDate_example"; // String | Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results.
    String pEnteredDate = "pEnteredDate_example"; // String | Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results.
    String pFacilityId = "pFacilityId_example"; // String | Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results.
    String pFacCity = "pFacCity_example"; // String | Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city.
    String pFacZip = "pFacZip_example"; // String | Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code.
    String pFacCounty = "pFacCounty_example"; // String | Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name.
    String pCaseSummary = "pCaseSummary_example"; // String | Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers.
    String pCaseSummaryType = "ALL"; // String | Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary.
    String pUsmex = "Y"; // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
    BigDecimal pC1lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC1lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lat = new BigDecimal(78); // BigDecimal | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal pC2lon = new BigDecimal(78); // BigDecimal | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String pVoluntary = "pVoluntary_example"; // String | Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure.
    String pFedIndicator = "pFedIndicator_example"; // String | Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media.
    String pFntype = "ALL"; // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
    String pCivilCriminalIndicator = "CI"; // String | Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY = return both civil and criminal cases. - CI = return only civil cases. - CR = return only criminal cases.
    BigDecimal queryset = new BigDecimal(78); // BigDecimal | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
    BigDecimal responseset = new BigDecimal(78); // BigDecimal | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
    String maplist = "Y"; // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    String pOcmapFy = "pOcmapFy_example"; // String | Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services
    String pQs = "pQs_example"; // String | Quick Search. Allows entry for city, state, and/or zip code.
    String pHasMap = "pHasMap_example"; // String | 
    try {
      CaseRestServicesGetCasesGet200Response result = apiInstance.caseRestServicesGetCasesPost(output, pCaseCategory, pCaseStatus, pMilestone, pFromDate, pToDate, pMilestoneFy, pName, pNameType, pCaseNumber, pDocketNumber, pCourtDocketNumber, pActivityNumber, pCaseLead, pCaseSensFlg, pRegion, pState, pDistrict, pSic, pSicAoNaics, pSicPrimaryFlg, pSicFrsFlg, pNaics, pNaicsPrimaryFlg, pNaicsFrsFlg, pEnfType, pLaw, pSection, pCpCitation, pRankOrder, pEnfProgram, pViolation, pPriorityArea, pPriorityAreaDesc, pTribal, pOecaCore, pMultimedia, pFedCase, pActivityContact, pRole, pFedPenalty, pTotalFedPenalty, pCostRecovery, pTotalCostRecovery, pComplyingActions, pCompActVal, pTotalCompActVal, pSepCats, pSepVal, pTotalSepVal, pLodgedDate, pEnteredDate, pFacilityId, pFacCity, pFacZip, pFacCounty, pCaseSummary, pCaseSummaryType, pUsmex, pC1lat, pC1lon, pC2lat, pC2lon, pVoluntary, pFedIndicator, pFntype, pCivilCriminalIndicator, queryset, responseset, maplist, tablelist, paramCallback, qcolumns, pOcmapFy, pQs, pHasMap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCasesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pCaseCategory** | **String**| Case Category Filter.  Enter one or more case category codes to filter results.   Provide multiple values as a comma-delimited list. - AFR &#x3D; Administrative - Formal - AIF &#x3D; Administrative - Informal - JDC &#x3D; Judicial | [optional] |
| **pCaseStatus** | **String**| Case Status Code Filter.  Enter one or more case status codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pMilestone** | **String**| Administrative or Judicial Milestone Filter.  Enter one or milestone values to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pFromDate** | **String**| Administrative or Judicial Milestone Date Range Start Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_to_date must also be populated when using this parameter option. | [optional] |
| **pToDate** | **String**| Administrative or Judicial Milestone Date Range End Limiter.  Enter a date value in MM/DD/YYYY format to limit milestone results.  Parameter p_from_date must also be populated when using this parameter option. | [optional] |
| **pMilestoneFy** | **String**| Administrative or Judicial Milestone Fiscal Year Limiter.  Enter a single fiscal year value to limit milestone searches to a given fiscal year. | [optional] |
| **pName** | **String**| Case Name Filter.  Enter one or more case names to restrict results.  Provide multiple values as a comma-delimited list.  When using this parameter the p_name_type parameter is required. | [optional] |
| **pNameType** | **String**| Case Name Filter Modifier. | [optional] |
| **pCaseNumber** | **String**| Case Number Filter.  Enter one or more case numbers to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDocketNumber** | **String**| DOJ Docket Number Filter.  Enter a single docket number or partial docket number to restrict results.  Use \\\&quot;%\\\&quot; as a wildcard for more complex filtering. | [optional] |
| **pCourtDocketNumber** | **String**|  | [optional] |
| **pActivityNumber** | **String**| Case Activity Number Filter.  Enter a single case activity number to filter results. | [optional] |
| **pCaseLead** | **String**| Case Lead Limiter.  Enter E or S to limit results. - E &#x3D; EPA is the case lead. - S &#x3D; The state is the case lead. | [optional] [enum: E, S] |
| **pCaseSensFlg** | **String**| Case Sensitive Data Flag.  Enter a Y or N to include or exclude cases with sensitive data. | [optional] |
| **pRegion** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] [enum: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10] |
| **pState** | **String**| Case Location State Filter.  Enter one or more state USPS postal codes to filter results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pDistrict** | **String**| Case Location Court District Limiter.  Enter a single state court district code to limit results. | [optional] |
| **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results. | [optional] |
| **pSicAoNaics** | **String**| Case Location SIC/NAICS And/Or Modifier.  Enter either AND or OR to govern the search logic of SIC and NAICS codes. - AND &#x3D; Search will return results having both the provided SIC code(s) and provided NAICS code(s). - OR &#x3D; Search will return results having either the provided SIC code(s) or the provided NAICS code(s). | [optional] [enum: AND, OR] |
| **pSicPrimaryFlg** | **String**| Case Location Primary SIC Flag.  Enter Y to limit SIC search results to primary SIC codes only. | [optional] [enum: Y, N] |
| **pSicFrsFlg** | **String**| Case Location Extended FRS SIC Search Flag.  Enter Y to expand SIC search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pNaics** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] |
| **pNaicsPrimaryFlg** | **String**| Case Location Primary NAICS Flag.  Enter Y to limit NAICS search results to primary NAICS codes only. | [optional] [enum: Y, N] |
| **pNaicsFrsFlg** | **String**| Case Location Extended FRS NAICS Search Flag.  Enter Y to expand NAICS search to include Federal Registry Service datasets. | [optional] [enum: Y, N] |
| **pEnfType** | **String**| Case Enforcement Type Filter. Enter one or more case enforcement type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] |
| **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCpCitation** | **String**| Law Section Code Filter Alternative. Enter a single law section code to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pRankOrder** | **String**| Law Status Rank Order Limiter.  Enter a single integer rank order to limit results. | [optional] [enum: 1, 0] |
| **pEnfProgram** | **String**| Enforcement Program Code Limiter.  Enter one or more enforcement program codes to limit results.  Provide multiple values as a comma-delimited list.   | [optional] |
| **pViolation** | **String**| Violation Type Code Filter.  Enter one or more violation type codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pPriorityArea** | **String**| Case Priority Area Filter.  Enter one or more case priority areas to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pPriorityAreaDesc** | **String**| Case Priority Area Description Filter.  Enter a single case priority area description or partial case priority area description to limit results.  Use \\\&quot;%\\\&quot; as a wild-card match for more complex searches. | [optional] |
| **pTribal** | **String**| Case Location Tribal Land Flag.  Enter Y or N to include or disallow cases on tribal land. | [optional] [enum: Y, N] |
| **pOecaCore** | **String**| OECA Core Program Flag.  Enter Y or N to include or exclude core program cases. | [optional] [enum: Y, N] |
| **pMultimedia** | **String**| Enforcement Multimedia Case Flag.  Enter Y or N to include or exclude multimedia cases. | [optional] [enum: Y, N] |
| **pFedCase** | **String**| Federal Facility Involvement Flag.  Enter a Y or N to include or exclude cases involving federal facilities. | [optional] [enum: Y, N] |
| **pActivityContact** | **String**| Activity Contact Last Name Filter.  Enter a single last name or partial last name to filter results.  Use \\\&quot;%\\\&quot; as a wild-card for advanced searching. | [optional] |
| **pRole** | **String**| Activity Contact Role Code Filter.  Enter a single role code to restrict results. | [optional] |
| **pFedPenalty** | **String**| Federal Penalty Assessed Amount Filter.  Provide one of the following keywords to restrict results. - ANY &#x3D; cases with any penalty amount. - LE5000 &#x3D; cases with penalty amount less than or equal to $5,000. - GT5000 &#x3D; cases with penalty amount more than $5,000. - GT50000 &#x3D; cases with penalty amount more than $50,000. - GT100000 &#x3D; cases with penalty amount more than $100,000. - GT500000 &#x3D; cases with penalty amount more than $500,000. - GT1000000 &#x3D; cases with penalty amount more than $1,000,000. - GT2500000 &#x3D; cases with penalty amount more than $2,500,000. | [optional] [enum: ANY, LE5000, GT5000, GT50000, GT100000, GT500000, GT1000000, GT2500000] |
| **pTotalFedPenalty** | **String**| Total Federal Penalty Limiter.  Enter a keyword value to limit results to cases with given total federal penalties. - ANY &#x3D; Cases with any federal penalty greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with federal penalty greater than the given amount. | [optional] |
| **pCostRecovery** | **String**| Cost Recovery Awarded Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pTotalCostRecovery** | **String**| Total Cost Recovery Amount Limiter.  Enter a keyword value to limit results to cases with given cost recovery amounts. - ANY &#x3D; Cases with any cost recovery amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with cost recovery amount greater than the given amount. | [optional] |
| **pComplyingActions** | **String**| Complying Actions Type Code Limiter.  Enter one or more complying action codes to restrict results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pCompActVal** | **String**| Compliance Action Cost Limiter. Enter a keyword value to limit results to cases with given compliance cost amounts. - ANY &#x3D; Cases with any compliance cost amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with compliance cost amount greater than the given amount. | [optional] [enum: ANY, LE5000, GT5000, GT100000, GT1000000, GT50000000] |
| **pTotalCompActVal** | **String**| Total Compliance Action Amount Limiter.  Enter a keyword value to limit results to cases with given total compliance action amounts. - ANY &#x3D; Cases with any total compliance action amount greater than zero. - LEXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount less than or equal to the given amount. - GTXX &#x3D; Replacing XX with a dollar value, return cases with total compliance action amount greater than the given amount. | [optional] |
| **pSepCats** | **String**| Supplemental Environmental Projects Activity Category Code Limiter.  Provide one or more SEP activity category codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] |
| **pSepVal** | **String**| Supplemental Environmental Projects Activity Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP activity amount. - LE10000 &#x3D; return cases with SEP activity amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP activity amount greater than $10,000. - GT50000 &#x3D; return cases with SEP activity amount greater than $50,000. - GT100000 &#x3D; return cases with SEP activity amount greater than $100,000. - GT500000 &#x3D; return cases with SEP activity amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP activity amount greater than $1,000,000. | [optional] [enum: ANY, LE10000, GT10000, GT50000, GT100000, GT500000, GT1000000] |
| **pTotalSepVal** | **String**| Supplemental Environmental Projects Total Value Limiter.  Provide a keyword to limit results. - ANY &#x3D; return cases with any SEP total amount. - LE10000 &#x3D; return cases with SEP total amount less than or equal to $10,000. - GT10000 &#x3D; return cases with SEP total amount greater than $10,000. - GT50000 &#x3D; return cases with SEP total amount greater than $50,000. - GT100000 &#x3D; return cases with SEP total amount greater than $100,000. - GT500000 &#x3D; return cases with SEP total amount greater than $500,000. - GT1000000 &#x3D; return cases with SEP total amount greater than $1,000,000. | [optional] |
| **pLodgedDate** | **String**| Settlement Lodged Date Limiter.  Enter a single settlement lodged date in MM/DD/YYYY format to limit results. | [optional] |
| **pEnteredDate** | **String**| Settlement Entered Date Limiter.  Enter a single settlement entered date in MM/DD/YYYY format to limit results. | [optional] |
| **pFacilityId** | **String**| Case Facility Registration Identifier Limiter.  Enter a single complete facility identifier to limit results. | [optional] |
| **pFacCity** | **String**| Case Facility City Limiter.  Enter a single complete city name to filter cases by facility location city. | [optional] |
| **pFacZip** | **String**| Case Facility ZIP Code Limiter.  Enter a single 5-digit zip code to filter cases by facility location zip code. | [optional] |
| **pFacCounty** | **String**| Case Facility County Limiter.  Enter a single complete county name to filter cases by facility location county name. | [optional] |
| **pCaseSummary** | **String**| Case Summary Search Limiter.  Enter a single case summary to limit results.  This parameter accepts partial codes and allows for advanced search modifiers. | [optional] |
| **pCaseSummaryType** | **String**| Identifies how the the search terms enterened in p_case_summary are searched.  Valid values are ALL (Default), WITHIN, and CONTAINS.  Must be used with p_case_summary. | [optional] [enum: ALL, CONTAINS, WITHIN] |
| **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] [enum: Y, N] |
| **pC1lat** | **BigDecimal**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC1lon** | **BigDecimal**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lat** | **BigDecimal**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pC2lon** | **BigDecimal**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **pVoluntary** | **String**| Voluntary Self Disclosure Flag.  Enter Y or N to include or exclude cases results having voluntary disclosure. | [optional] |
| **pFedIndicator** | **String**| Federal Facility/Cross Media Flag.  Enter Y or N to limit results to cases with federal facility cross media. | [optional] |
| **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] [enum: ALL, CONTAINS, EXACT, BEGINS] |
| **pCivilCriminalIndicator** | **String**| Civil/Criminal Case Limiter.  Provide a keyword to limit results. - ANY &#x3D; return both civil and criminal cases. - CI &#x3D; return only civil cases. - CR &#x3D; return only criminal cases. | [optional] [enum: CI, CR, ALL] |
| **queryset** | **BigDecimal**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] |
| **responseset** | **BigDecimal**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] |
| **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] [enum: Y, N] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |
| **pOcmapFy** | **String**| Fiscal Year to select cases that are displayed in the Office of Complicance Fiscal Year Map Services | [optional] |
| **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] |
| **pHasMap** | **String**|  | [optional] |

### Return type

[**CaseRestServicesGetCasesGet200Response**](CaseRestServicesGetCasesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of cases that meet the selection criteria. |  -  |

<a id="caseRestServicesGetCrcaseReportGet"></a>
# **caseRestServicesGetCrcaseReportGet**
> CaseRestServicesGetCrcaseReportGet200Response caseRestServicesGetCrcaseReportGet(pId, output, paramCallback, mapset)

Enforcement Criminal Case Summary Report Search

The get_crcase_report service end point returns a complex object of criminal case detials based on the provided criminal case id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String mapset = "1400"; // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    try {
      CaseRestServicesGetCrcaseReportGet200Response result = apiInstance.caseRestServicesGetCrcaseReportGet(pId, output, paramCallback, mapset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCrcaseReportGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report. | [optional] |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to 1400] |

### Return type

[**CaseRestServicesGetCrcaseReportGet200Response**](CaseRestServicesGetCrcaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a complex object containing detailed criminal case information for the provided Case Identifier. |  -  |

<a id="caseRestServicesGetCrcaseReportPost"></a>
# **caseRestServicesGetCrcaseReportPost**
> CaseRestServicesGetCrcaseReportGet200Response caseRestServicesGetCrcaseReportPost(pId, output, paramCallback)

Enforcement Criminal Case Summary Report Search

The get_crcase_report service end point returns a complex object of criminal case detials based on the provided criminal case id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      CaseRestServicesGetCrcaseReportGet200Response result = apiInstance.caseRestServicesGetCrcaseReportPost(pId, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetCrcaseReportPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Prosecution Summary Identifier. Enter the numeric prosecution summary identifier to retrieve the criminal case report. | [optional] |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**CaseRestServicesGetCrcaseReportGet200Response**](CaseRestServicesGetCrcaseReportGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a complex object containing detailed criminal case information for the provided Case Identifier. |  -  |

<a id="caseRestServicesGetDownloadGet"></a>
# **caseRestServicesGetDownloadGet**
> File caseRestServicesGetDownloadGet(qid, output, qcolumns)

Enforcement Case Download Data Service

Based on the QID obtained from a get_cases query, return a comma separated value (CSV) file of the cases found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      File result = apiInstance.caseRestServicesGetDownloadGet(qid, output, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetDownloadGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are a comma separated value (CSV) file. |  -  |

<a id="caseRestServicesGetDownloadPost"></a>
# **caseRestServicesGetDownloadPost**
> File caseRestServicesGetDownloadPost(qid, output, qcolumns)

Enforcement Case Download Data Service

Based on the QID obtained from a get_cases query, return a comma separated value (CSV) file of the cases found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "output_example"; // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      File result = apiInstance.caseRestServicesGetDownloadPost(qid, output, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetDownloadPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). | [optional] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are a comma separated value (CSV) file. |  -  |

<a id="caseRestServicesGetFacilitiesFromCaseGet"></a>
# **caseRestServicesGetFacilitiesFromCaseGet**
> CaseRestServicesGetFacilitiesFromCaseGet200Response caseRestServicesGetFacilitiesFromCaseGet(pId, output, paramCallback)

Placeholder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      CaseRestServicesGetFacilitiesFromCaseGet200Response result = apiInstance.caseRestServicesGetFacilitiesFromCaseGet(pId, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetFacilitiesFromCaseGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**CaseRestServicesGetFacilitiesFromCaseGet200Response**](CaseRestServicesGetFacilitiesFromCaseGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results |  -  |

<a id="caseRestServicesGetFacilitiesFromCasePost"></a>
# **caseRestServicesGetFacilitiesFromCasePost**
> CaseRestServicesGetFacilitiesFromCaseGet200Response caseRestServicesGetFacilitiesFromCasePost(pId, output, paramCallback)

Placeholder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String pId = "pId_example"; // String | Identifier for the service.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    try {
      CaseRestServicesGetFacilitiesFromCaseGet200Response result = apiInstance.caseRestServicesGetFacilitiesFromCasePost(pId, output, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetFacilitiesFromCasePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pId** | **String**| Identifier for the service. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |

### Return type

[**CaseRestServicesGetFacilitiesFromCaseGet200Response**](CaseRestServicesGetFacilitiesFromCaseGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results |  -  |

<a id="caseRestServicesGetMapGet"></a>
# **caseRestServicesGetMapGet**
> CaseRestServicesGetMapGet200Response caseRestServicesGetMapGet(qid, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long)

Enforcement Case Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_cases query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    BigDecimal c1Lat = new BigDecimal(78); // BigDecimal | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c1Long = new BigDecimal(78); // BigDecimal | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Lat = new BigDecimal(78); // BigDecimal | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Long = new BigDecimal(78); // BigDecimal | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    try {
      CaseRestServicesGetMapGet200Response result = apiInstance.caseRestServicesGetMapGet(qid, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetMapGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **c1Lat** | **BigDecimal**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c1Long** | **BigDecimal**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Lat** | **BigDecimal**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Long** | **BigDecimal**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |

### Return type

[**CaseRestServicesGetMapGet200Response**](CaseRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="caseRestServicesGetMapPost"></a>
# **caseRestServicesGetMapPost**
> CaseRestServicesGetMapGet200Response caseRestServicesGetMapPost(qid, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long, mapset)

Enforcement Case Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_cases query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    String tablelist = "Y"; // String | Table List Flag. Enter a Y to display the first page of facility results.
    BigDecimal c1Lat = new BigDecimal(78); // BigDecimal | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c1Long = new BigDecimal(78); // BigDecimal | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Lat = new BigDecimal(78); // BigDecimal | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    BigDecimal c2Long = new BigDecimal(78); // BigDecimal | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
    String mapset = "1400"; // String | Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query.
    try {
      CaseRestServicesGetMapGet200Response result = apiInstance.caseRestServicesGetMapPost(qid, output, paramCallback, tablelist, c1Lat, c1Long, c2Lat, c2Long, mapset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetMapPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] [enum: Y, N] |
| **c1Lat** | **BigDecimal**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c1Long** | **BigDecimal**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Lat** | **BigDecimal**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **c2Long** | **BigDecimal**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] |
| **mapset** | **String**| Identifies the maxium number of case facilities to return from the case_rest_services.get_case_info query. | [optional] [default to 1400] |

### Return type

[**CaseRestServicesGetMapGet200Response**](CaseRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are either an array of State, County, Zip Code facility cluster map coordinates or individual facility coordinates.  Coordinates provided are in WGS84. |  -  |

<a id="caseRestServicesGetQidGet"></a>
# **caseRestServicesGetQidGet**
> CaseRestServicesGetQidGet200Response caseRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Enforcement Case Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_cases query. It then returns a CASES object containing all matching cases. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      CaseRestServicesGetQidGet200Response result = apiInstance.caseRestServicesGetQidGet(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetQidGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pageno** | **BigDecimal**| Indicates the number of the page to display. It is used only when the results are paginated. | [optional] [default to 1.0] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **newsort** | **BigDecimal**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] |
| **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] [enum: Y, N] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**CaseRestServicesGetQidGet200Response**](CaseRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page)  of Cases from ICIS with the number of cases equal to the responseset (page size). |  -  |

<a id="caseRestServicesGetQidPost"></a>
# **caseRestServicesGetQidPost**
> CaseRestServicesGetQidGet200Response caseRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns)

Enforcement Case Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_cases query. It then returns a CASES object containing all matching cases. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CaseEnforcementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://echodata.epa.gov/echo");

    CaseEnforcementApi apiInstance = new CaseEnforcementApi(defaultClient);
    String qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
    String output = "JSONP"; // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
    BigDecimal pageno = new BigDecimal("1.0"); // BigDecimal | Indicates the number of the page to display. It is used only when the results are paginated.
    String paramCallback = "paramCallback_example"; // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
    BigDecimal newsort = new BigDecimal(78); // BigDecimal | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
    String descending = "Y"; // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
    String qcolumns = "qcolumns_example"; // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
    try {
      CaseRestServicesGetQidGet200Response result = apiInstance.caseRestServicesGetQidPost(qid, output, pageno, paramCallback, newsort, descending, qcolumns);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CaseEnforcementApi#caseRestServicesGetQidPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **qid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | |
| **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] [enum: JSONP, JSON, XML] |
| **pageno** | **BigDecimal**| Indicates the number of the page to display. It is used only when the results are paginated. | [optional] [default to 1.0] |
| **paramCallback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] |
| **newsort** | **BigDecimal**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] |
| **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] [enum: Y, N] |
| **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] |

### Return type

[**CaseRestServicesGetQidGet200Response**](CaseRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results are an array (page)  of Cases from ICIS with the number of cases equal to the responseset (page size). |  -  |


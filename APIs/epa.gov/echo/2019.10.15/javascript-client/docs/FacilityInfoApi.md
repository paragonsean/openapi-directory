# USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echoRestServicesGetDownloadGet**](FacilityInfoApi.md#echoRestServicesGetDownloadGet) | **GET** /echo_rest_services.get_download | Combined ECHO Download Data Service
[**echoRestServicesGetDownloadPost**](FacilityInfoApi.md#echoRestServicesGetDownloadPost) | **POST** /echo_rest_services.get_download | Combined ECHO Download Data Service
[**echoRestServicesGetFacilitiesGet**](FacilityInfoApi.md#echoRestServicesGetFacilitiesGet) | **GET** /echo_rest_services.get_facilities | Combined ECHO Facility Search Service
[**echoRestServicesGetFacilitiesPost**](FacilityInfoApi.md#echoRestServicesGetFacilitiesPost) | **POST** /echo_rest_services.get_facilities | Combined ECHO Facility Search Service
[**echoRestServicesGetFacilityInfoGet**](FacilityInfoApi.md#echoRestServicesGetFacilityInfoGet) | **GET** /echo_rest_services.get_facility_info | Combined ECHO Facility Enhanced Search Service
[**echoRestServicesGetFacilityInfoPost**](FacilityInfoApi.md#echoRestServicesGetFacilityInfoPost) | **POST** /echo_rest_services.get_facility_info | Combined ECHO Facility Enhanced Search Service
[**echoRestServicesGetGeojsonGet**](FacilityInfoApi.md#echoRestServicesGetGeojsonGet) | **GET** /echo_rest_services.get_geojson | Combined ECHO GeoJSON Service
[**echoRestServicesGetGeojsonPost**](FacilityInfoApi.md#echoRestServicesGetGeojsonPost) | **POST** /echo_rest_services.get_geojson | Combined ECHO GeoJSON Service
[**echoRestServicesGetInfoClustersGet**](FacilityInfoApi.md#echoRestServicesGetInfoClustersGet) | **GET** /echo_rest_services.get_info_clusters | Combined ECHO Info Clusters Service
[**echoRestServicesGetInfoClustersPost**](FacilityInfoApi.md#echoRestServicesGetInfoClustersPost) | **POST** /echo_rest_services.get_info_clusters | Combined ECHO Info Clusters Service
[**echoRestServicesGetMapGet**](FacilityInfoApi.md#echoRestServicesGetMapGet) | **GET** /echo_rest_services.get_map | Combined ECHO Map Service
[**echoRestServicesGetMapPost**](FacilityInfoApi.md#echoRestServicesGetMapPost) | **POST** /echo_rest_services.get_map | Combined ECHO Map Service
[**echoRestServicesGetQidGet**](FacilityInfoApi.md#echoRestServicesGetQidGet) | **GET** /echo_rest_services.get_qid | Combined ECHO Paginated Results Service
[**echoRestServicesGetQidPost**](FacilityInfoApi.md#echoRestServicesGetQidPost) | **POST** /echo_rest_services.get_qid | Combined ECHO Paginated Results Service



## echoRestServicesGetDownloadGet

> File echoRestServicesGetDownloadGet(qid, opts)

Combined ECHO Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetDownloadGet(qid, opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesGetDownloadPost

> File echoRestServicesGetDownloadPost(qid, opts)

Combined ECHO Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetDownloadPost(qid, opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## echoRestServicesGetFacilitiesGet

> EchoRestServicesGetFacilitiesGet200Response echoRestServicesGetFacilitiesGet(opts)

Combined ECHO Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pZip': "pZip_example", // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
  'pFrs': "pFrs_example", // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
  'pReg': "pReg_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
  'pNcs': "pNcs_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pPen': "pPen_example", // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \"LE5\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
  'pC1lat': 3.4, // Number | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC1lon': 3.4, // Number | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lat': 3.4, // Number | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lon': 3.4, // Number | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pSic2': "pSic2_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \"22\" to match all SIC codes beginning with 22.  Use the \"%\" character within strings to match any SIC values with the pattern.  For example, \"2%21\" matches 2021, 2121, 2221, etc.
  'pSic4': "pSic4_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
  'pFa': "pFa_example", // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
  'pFf': "pFf_example", // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pMaj': "pMaj_example", // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
  'pMact': "pMact_example", // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pFeac': "pFeac_example", // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \"Y\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
  'pFea5yr': "pFea5yr_example", // String | A Y value identifies facilities that have had a formal enforcement action within the last 5 years.
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pIea5yr': "pIea5yr_example", // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
  'pCs': 3.4, // Number | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pNaa': "pNaa_example", // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOcr': "pOcr_example", // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
  'pIstatute': "pIstatute_example", // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pNeiu': "pNeiu_example", // String | 
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'maplist': "maplist_example", // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
  'summarylist': "summarylist_example", // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.echoRestServicesGetFacilitiesGet(opts, (error, data, response) => {
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
 **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] 
 **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] 
 **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] 
 **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] 
 **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] 
 **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] 
 **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] 
 **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] 
 **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] 
 **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] 
 **pC1lat** | **Number**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC1lon** | **Number**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lat** | **Number**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lon** | **Number**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc. | [optional] 
 **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] 
 **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] 
 **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] 
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] 
 **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \&quot;Y\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] 
 **pFea5yr** | **String**| A Y value identifies facilities that have had a formal enforcement action within the last 5 years. | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] 
 **pCs** | **Number**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] 
 **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pNeiu** | **String**|  | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] 
 **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**EchoRestServicesGetFacilitiesGet200Response**](EchoRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesGetFacilitiesPost

> EchoRestServicesGetFacilitiesGet200Response echoRestServicesGetFacilitiesPost(opts)

Combined ECHO Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pZip': "pZip_example", // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
  'pFrs': "pFrs_example", // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
  'pReg': "pReg_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
  'pNcs': "pNcs_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pPen': "pPen_example", // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\"LE5\\\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
  'pC1lat': 3.4, // Number | In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC1lon': 3.4, // Number | In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lat': 3.4, // Number | In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pC2lon': 3.4, // Number | In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pSic2': "pSic2_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\"22\\\" to match all SIC codes beginning with 22.  Use the \\\"%\\\" character within strings to match any SIC values with the pattern.  For example, \\\"2%21\\\" matches 2021, 2121, 2221, etc.
  'pSic4': "pSic4_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
  'pFa': "pFa_example", // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
  'pFf': "pFf_example", // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pMaj': "pMaj_example", // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
  'pMact': "pMact_example", // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pFeac': "pFeac_example", // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\"Y\\\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
  'pFea5yr': "pFea5yr_example", // String | A Y value identifies facilities that have had a formal enforcement action within the last 5 years.
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pIea5yr': "pIea5yr_example", // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
  'pCs': 3.4, // Number | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pNaa': "pNaa_example", // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOcr': "pOcr_example", // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
  'pIstatute': "pIstatute_example", // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pNeiu': "pNeiu_example", // String | 
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'maplist': "maplist_example", // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
  'summarylist': "summarylist_example", // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.echoRestServicesGetFacilitiesPost(opts, (error, data, response) => {
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
 **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] 
 **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] 
 **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] 
 **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] 
 **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] 
 **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] 
 **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] 
 **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] 
 **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] 
 **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] 
 **pC1lat** | **Number**| In decimal degrees.  Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC1lon** | **Number**| In decimal degrees.  Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lat** | **Number**| In decimal degrees.  Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pC2lon** | **Number**| In decimal degrees.  Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc. | [optional] 
 **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] 
 **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] 
 **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] 
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] 
 **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\&quot;Y\\\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] 
 **pFea5yr** | **String**| A Y value identifies facilities that have had a formal enforcement action within the last 5 years. | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] 
 **pCs** | **Number**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] 
 **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pNeiu** | **String**|  | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] 
 **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**EchoRestServicesGetFacilitiesGet200Response**](EchoRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## echoRestServicesGetFacilityInfoGet

> EchoRestServicesGetFacilityInfoGet200Response echoRestServicesGetFacilityInfoGet(opts)

Combined ECHO Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pZip': "pZip_example", // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
  'pFrs': "pFrs_example", // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
  'pReg': "pReg_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
  'pNcs': "pNcs_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pPen': "pPen_example", // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \"LE5\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
  'xmin': 3.4, // Number | Minimum longitude value in decimal degrees.
  'ymin': 3.4, // Number | Minimum latitude value in decimal degrees.
  'xmax': 3.4, // Number | Maximum longitude value in decimal degrees.
  'ymax': 3.4, // Number | Maximum latitude value in decimal degrees.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pSic2': "pSic2_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \"22\" to match all SIC codes beginning with 22.  Use the \"%\" character within strings to match any SIC values with the pattern.  For example, \"2%21\" matches 2021, 2121, 2221, etc.
  'pSic4': "pSic4_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
  'pFa': "pFa_example", // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
  'pFf': "pFf_example", // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pMaj': "pMaj_example", // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
  'pMact': "pMact_example", // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pFeac': "pFeac_example", // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \"Y\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
  'pFeac5yr': "pFeac5yr_example", // String | 
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pIea5yr': "pIea5yr_example", // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
  'pCs': 3.4, // Number | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pNaa': "pNaa_example", // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOcr': "pOcr_example", // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
  'pIstatute': "pIstatute_example", // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pNeiu': "pNeiu_example", // String | 
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetFacilityInfoGet(opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. - CSV &#x3D; Facility results formatted as comma delimited file download. - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection. - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] 
 **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] 
 **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] 
 **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] 
 **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] 
 **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] 
 **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] 
 **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] 
 **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] 
 **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \&quot;LE5\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] 
 **xmin** | **Number**| Minimum longitude value in decimal degrees. | [optional] 
 **ymin** | **Number**| Minimum latitude value in decimal degrees. | [optional] 
 **xmax** | **Number**| Maximum longitude value in decimal degrees. | [optional] 
 **ymax** | **Number**| Maximum latitude value in decimal degrees. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \&quot;22\&quot; to match all SIC codes beginning with 22.  Use the \&quot;%\&quot; character within strings to match any SIC values with the pattern.  For example, \&quot;2%21\&quot; matches 2021, 2121, 2221, etc. | [optional] 
 **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] 
 **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] 
 **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] 
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] 
 **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \&quot;Y\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] 
 **pFeac5yr** | **String**|  | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] 
 **pCs** | **Number**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] 
 **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pNeiu** | **String**|  | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

[**EchoRestServicesGetFacilityInfoGet200Response**](EchoRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesGetFacilityInfoPost

> EchoRestServicesGetFacilityInfoGet200Response echoRestServicesGetFacilityInfoPost(opts)

Combined ECHO Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pZip': "pZip_example", // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
  'pFrs': "pFrs_example", // String | Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results.
  'pReg': "pReg_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pSic': "pSic_example", // String | Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4.
  'pNcs': "pNcs_example", // String | North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values.
  'pPen': "pPen_example", // String | Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER = No Penalties - ANY = Any Penalty - LEXX = Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\"LE5\\\" for a facility with a penalty within previous 5 months. - GTXX = Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago.
  'xmin': 3.4, // Number | Minimum longitude value in decimal degrees.
  'ymin': 3.4, // Number | Minimum latitude value in decimal degrees.
  'xmax': 3.4, // Number | Maximum longitude value in decimal degrees.
  'ymax': 3.4, // Number | Maximum latitude value in decimal degrees.
  'pUsmex': "pUsmex_example", // String | US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border.
  'pSic2': "pSic2_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\"22\\\" to match all SIC codes beginning with 22.  Use the \\\"%\\\" character within strings to match any SIC values with the pattern.  For example, \\\"2%21\\\" matches 2021, 2121, 2221, etc.
  'pSic4': "pSic4_example", // String | Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker.
  'pFa': "pFa_example", // String | Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values.
  'pFf': "pFf_example", // String | Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities.
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pMaj': "pMaj_example", // String | Major Facility Flag.  Enter Y to restrict results to Major facilities only.
  'pMact': "pMact_example", // String | CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pFeac': "pFeac_example", // String | Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\"Y\\\" to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided.
  'pFeac5yr': "pFeac5yr_example", // String | 
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pIea5yr': "pIea5yr_example", // String | A Y value identifies facilities that have had an informal enforcement action within the last 5 years.
  'pCs': 3.4, // Number | Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 = Facilities in noncompliance. - 3 = Facilities having one or more programs reporting significant noncompliance. - 4 = Facilities having more than one program reporting significant noncompliance.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pNaa': "pNaa_example", // String | Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOcr': "pOcr_example", // String | Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media.- A = Air- C = CAMD (Clean Air Markets Division)- E = EIS (Emissions Inventory Systems)- G = GHG (Greenhouse Gases)- M = RMP (Risk Management Plan)- R = RCRA (Hazardous Waste)- S = SDWA (Public Drinking Water Systems)- T = TRI (Toxic Release Inventory)- TSCA = TSCA (Toxic Substances Control Act)- W = Water- ALL = Air and Water and RCRA
  'pIstatute': "pIstatute_example", // String | For use in identifying Facilities that have an inspection performed under the entered Statute.
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pNeiu': "pNeiu_example", // String | 
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetFacilityInfoPost(opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. - CSV &#x3D; Facility results formatted as comma delimited file download. - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection. - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **pFn** | **String**| Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers. | [optional] 
 **pSa** | **String**| Facility street address. Enter a complete or partial street address. | [optional] 
 **pSa1** | **String**| Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa. | [optional] 
 **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] 
 **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] 
 **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] 
 **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] 
 **pFrs** | **String**| Facility Registry Service ID Filter. Enter a single 12-digit FRS identifier to filter results. | [optional] 
 **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pSic** | **String**| Standard Industrial Classification (SIC) Code Filter.  Enter a single 4-digit SIC Code to filter results.  If more complex filtering is required, use p_sic2 and p_sic4. | [optional] 
 **pNcs** | **String**| North American Industry Classification System Filter. Enter two to six digits to filter results to facilities having matching NAICS codes.  Digits less than six will match to all codes beginning with the provided values. | [optional] 
 **pPen** | **String**| Last Penality Date Qualifier Filter.  Enter one of the following:    - NEVER &#x3D; No Penalties - ANY &#x3D; Any Penalty - LEXX &#x3D; Less than or equal to XX months.  Provide a number in place of XX, e.g. \\\&quot;LE5\\\&quot; for a facility with a penalty within previous 5 months. - GTXX &#x3D; Greater than XX months.  Provide a number in place of XX, eg. GT12, for a facility with the last penalty greater than 12 months ago. | [optional] 
 **xmin** | **Number**| Minimum longitude value in decimal degrees. | [optional] 
 **ymin** | **Number**| Minimum latitude value in decimal degrees. | [optional] 
 **xmax** | **Number**| Maximum longitude value in decimal degrees. | [optional] 
 **ymax** | **Number**| Maximum latitude value in decimal degrees. | [optional] 
 **pUsmex** | **String**| US-Mexico Border Flag.  Enter Y/N to restrict searches to facilities located within 100KM of the border. | [optional] 
 **pSic2** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 2. Enter a wild-card search against SIC codes.  A final wild-card is always present allowing \\\&quot;22\\\&quot; to match all SIC codes beginning with 22.  Use the \\\&quot;%\\\&quot; character within strings to match any SIC values with the pattern.  For example, \\\&quot;2%21\\\&quot; matches 2021, 2121, 2221, etc. | [optional] 
 **pSic4** | **String**| Standard Industrial Classification (SIC) Code Filter Alternate 3.  Enter the first 2, 3 or 4 SIC code digits to filter results to facilities having those code prefixes.  As this alternative does not utilize an index, p_sic2 will generally be quicker. | [optional] 
 **pFa** | **String**| Federal Agency. 1 character or 5-character values; may contain multiple comma-separated values. ALL will retrieve all facilities where the federal agency code is not null.  Use the Federal Agencies lookup service to obtain a list of values. | [optional] 
 **pFf** | **String**| Federal Facility Indicator Flag. Enter Y to restrict searches to federal facilities. | [optional] 
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pMaj** | **String**| Major Facility Flag.  Enter Y to restrict results to Major facilities only. | [optional] 
 **pMact** | **String**| CAA Maximum Achievable Control Technology (MACT) Subpart codes (alpha ID between 1 and 7 characters) applicable to the facility. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pFeac** | **String**| Formal Enforcment Action Last Case Date Limiter Flag.  Enter a value of \\\&quot;Y\\\&quot; to additionally apply the p_feay year filter to the last formal enforcement action case date.  Use the p_fea parameter to control if the filter is within or outside the date span provided. | [optional] 
 **pFeac5yr** | **String**|  | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pIea5yr** | **String**| A Y value identifies facilities that have had an informal enforcement action within the last 5 years. | [optional] 
 **pCs** | **Number**| Facility Compliance Limiter.  Enter 2, 3 or 4 to limit facilities returned. - 2 &#x3D; Facilities in noncompliance. - 3 &#x3D; Facilities having one or more programs reporting significant noncompliance. - 4 &#x3D; Facilities having more than one program reporting significant noncompliance. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pNaa** | **String**| Non-Attainment Area Flag.  Enter a Y or N to filter for or against facilities flagged as non-attainment areas. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOcr** | **String**| Toxics Release Inventory Pounds of On-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media.- A &#x3D; Air- C &#x3D; CAMD (Clean Air Markets Division)- E &#x3D; EIS (Emissions Inventory Systems)- G &#x3D; GHG (Greenhouse Gases)- M &#x3D; RMP (Risk Management Plan)- R &#x3D; RCRA (Hazardous Waste)- S &#x3D; SDWA (Public Drinking Water Systems)- T &#x3D; TRI (Toxic Release Inventory)- TSCA &#x3D; TSCA (Toxic Substances Control Act)- W &#x3D; Water- ALL &#x3D; Air and Water and RCRA | [optional] 
 **pIstatute** | **String**| For use in identifying Facilities that have an inspection performed under the entered Statute. | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pNeiu** | **String**|  | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

[**EchoRestServicesGetFacilityInfoGet200Response**](EchoRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## echoRestServicesGetGeojsonGet

> EchoRestServicesGetGeojsonGet200Response echoRestServicesGetGeojsonGet(qid, opts)

Combined ECHO GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetGeojsonGet(qid, opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection (default). - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **newsort** | **Number**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] 
 **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

[**EchoRestServicesGetGeojsonGet200Response**](EchoRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesGetGeojsonPost

> EchoRestServicesGetGeojsonGet200Response echoRestServicesGetGeojsonPost(qid, opts)

Combined ECHO GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetGeojsonPost(qid, opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - GEOJSON &#x3D; Facility results formatted as GeoJSON feature collection (default). - GEOJSONP &#x3D; Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **newsort** | **Number**| Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column. | [optional] 
 **descending** | **String**| Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

[**EchoRestServicesGetGeojsonGet200Response**](EchoRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## echoRestServicesGetInfoClustersGet

> File echoRestServicesGetInfoClustersGet(pQid, opts)

Combined ECHO Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetInfoClustersGet(pQid, opts, (error, data, response) => {
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
 **pQid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesGetInfoClustersPost

> File echoRestServicesGetInfoClustersPost(pQid, opts)

Combined ECHO Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.echoRestServicesGetInfoClustersPost(pQid, opts, (error, data, response) => {
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
 **pQid** | **String**| Query ID Selector.  Enter the QueryID number from a previously run query. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - CSV &#x3D; Facility results formatted as comma delimited file download (default). - GEOJSOND &#x3D; Facility results formatted as GeoJSON feature collection download. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## echoRestServicesGetMapGet

> EchoRestServicesGetMapGet200Response echoRestServicesGetMapGet(qid, pId, opts)

Combined ECHO Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'c1Lat': 3.4, // Number | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c1Long': 3.4, // Number | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Lat': 3.4, // Number | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Long': 3.4 // Number | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
};
apiInstance.echoRestServicesGetMapGet(qid, pId, opts, (error, data, response) => {
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
 **pId** | **String**| Identifier for the service. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **c1Lat** | **Number**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c1Long** | **Number**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Lat** | **Number**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Long** | **Number**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 

### Return type

[**EchoRestServicesGetMapGet200Response**](EchoRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesGetMapPost

> EchoRestServicesGetMapGet200Response echoRestServicesGetMapPost(qid, pId, opts)

Combined ECHO Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'c1Lat': 3.4, // Number | Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c1Long': 3.4, // Number | Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Lat': 3.4, // Number | Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
  'c2Long': 3.4 // Number | Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided.
};
apiInstance.echoRestServicesGetMapPost(qid, pId, opts, (error, data, response) => {
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
 **pId** | **String**| Identifier for the service. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **c1Lat** | **Number**| Latitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c1Long** | **Number**| Longitude of 1st corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Lat** | **Number**| Latitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 
 **c2Long** | **Number**| Longitude of 2nd corner of box that bounds the resulting facilities. The latitude and longitude of both corners of the bounding box must be provided. | [optional] 

### Return type

[**EchoRestServicesGetMapGet200Response**](EchoRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## echoRestServicesGetQidGet

> EchoRestServicesGetQidGet200Response echoRestServicesGetQidGet(qid, opts)

Combined ECHO Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.echoRestServicesGetQidGet(qid, opts, (error, data, response) => {
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

[**EchoRestServicesGetQidGet200Response**](EchoRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesGetQidPost

> EchoRestServicesGetQidGet200Response echoRestServicesGetQidPost(qid, opts)

Combined ECHO Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.FacilityInfoApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.echoRestServicesGetQidPost(qid, opts, (error, data, response) => {
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

[**EchoRestServicesGetQidGet200Response**](EchoRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


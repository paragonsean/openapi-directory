# USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rcraRestServicesGetDownloadGet**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetDownloadGet) | **GET** /rcra_rest_services.get_download | Resource Conservation and Recovery Act (RCRA) Download Data Service
[**rcraRestServicesGetDownloadPost**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetDownloadPost) | **POST** /rcra_rest_services.get_download | Resource Conservation and Recovery Act (RCRA) Download Data Service
[**rcraRestServicesGetFacilitiesGet**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetFacilitiesGet) | **GET** /rcra_rest_services.get_facilities | Resource Conservation and Recovery Act (RCRA) Facility Search Service
[**rcraRestServicesGetFacilitiesPost**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetFacilitiesPost) | **POST** /rcra_rest_services.get_facilities | Resource Conservation and Recovery Act (RCRA) Facility Search Service
[**rcraRestServicesGetFacilityInfoGet**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetFacilityInfoGet) | **GET** /rcra_rest_services.get_facility_info | Resource Conservation and Recovery Act (RCRA) Facility Enhanced Search Service
[**rcraRestServicesGetFacilityInfoPost**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetFacilityInfoPost) | **POST** /rcra_rest_services.get_facility_info | Resource Conservation and Recovery Act (RCRA) Facility Enhanced Search Service
[**rcraRestServicesGetGeojsonGet**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetGeojsonGet) | **GET** /rcra_rest_services.get_geojson | Resource Conservation and Recovery Act (RCRA) GeoJSON Service
[**rcraRestServicesGetGeojsonPost**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetGeojsonPost) | **POST** /rcra_rest_services.get_geojson | Resource Conservation and Recovery Act (RCRA) GeoJSON Service
[**rcraRestServicesGetInfoClustersGet**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetInfoClustersGet) | **GET** /rcra_rest_services.get_info_clusters | Resource Conservation and Recovery Act (RCRA) Info Clusters Service
[**rcraRestServicesGetInfoClustersPost**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetInfoClustersPost) | **POST** /rcra_rest_services.get_info_clusters | Resource Conservation and Recovery Act (RCRA) Info Clusters Service
[**rcraRestServicesGetMapGet**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetMapGet) | **GET** /rcra_rest_services.get_map | Resource Conservation and Recovery Act (RCRA) Map Service
[**rcraRestServicesGetMapPost**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetMapPost) | **POST** /rcra_rest_services.get_map | Resource Conservation and Recovery Act (RCRA) Map Service
[**rcraRestServicesGetQidGet**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetQidGet) | **GET** /rcra_rest_services.get_qid | Resource Conservation and Recovery Act (RCRA) Paginated Results Service
[**rcraRestServicesGetQidPost**](ResourceConservationAndRecoveryActApi.md#rcraRestServicesGetQidPost) | **POST** /rcra_rest_services.get_qid | Resource Conservation and Recovery Act (RCRA) Paginated Results Service



## rcraRestServicesGetDownloadGet

> File rcraRestServicesGetDownloadGet(qid, opts)

Resource Conservation and Recovery Act (RCRA) Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetDownloadGet(qid, opts, (error, data, response) => {
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


## rcraRestServicesGetDownloadPost

> File rcraRestServicesGetDownloadPost(qid, opts)

Resource Conservation and Recovery Act (RCRA) Download Data Service

Based on the QID obtained from a get_facilities or get_facility_info query, return a comma separated value (CSV) file of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetDownloadPost(qid, opts, (error, data, response) => {
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


## rcraRestServicesGetFacilitiesGet

> RcraRestServicesGetFacilitiesGet200Response rcraRestServicesGetFacilitiesGet(opts)

Resource Conservation and Recovery Act (RCRA) Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pStdist': "pStdist_example", // String | State District Filter.  Enter a single state district to restrict results.
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
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pCmps': "pCmps_example", // String | RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOlr': "pOlr_example", // String | Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of land releases. - GT0 = More than zero pounds of land releases. - GT1000 = More than one thousand pounds of land releases. - GT5000 = More than five thousand pounds of land releases. - GT10000 = More than ten thousand pounds of land releases. - GT20000 = More than twenty thousand pounds of land releases. - GT50000 = More than fifty thousand pounds of land releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pTrichem': "pTrichem_example", // String | 
  'pTriLrPol': "pTriLrPol_example", // String | 
  'pTriLrYr': "pTriLrYr_example", // String | 
  'pTriLrAmt': "pTriLrAmt_example", // String | 
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Air and Water and RCRA
  'pOwc': "pOwc_example", // String | 
  'pOwd': "pOwd_example", // String | 
  'pOpc': "pOpc_example", // String | 
  'pOpd': "pOpd_example", // String | 
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pOwop': "pOwop_example", // String | Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pIdt1': "pIdt1_example", // String | Beginning of date range of most recent facility inspection.
  'pIdt2': "pIdt2_example", // String | End of date range of most recent facility inspection.
  'pPityp': "pPityp_example", // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
  'pCifdi': "pCifdi_example", // String | Compliance issuess found during inspection.
  'pPfead1': "pPfead1_example", // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfead2': "pPfead2_example", // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfeat': "pPfeat_example", // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
  'pPsncq': "pPsncq_example", // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
  'pDwd': "pDwd_example", // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
  'pVioly': 3.4, // Number | Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
  'pNcv': "pNcv_example", // String | Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
  'pFcv': "pFcv_example", // String | Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
  'pViolt': "pViolt_example", // String | RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
  'pDes': "pDes_example", // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \"TSDF\" to return the full enforcement TSDF universe and \"Operating TSDF\" to return the operating TSDF universe.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pPidall': "pPidall_example", // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
  'pFacIco': "pFacIco_example", // String | FRS tribal land code flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land code.
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pDecouple': "pDecouple_example", // String | Decouple Inspection Code Search Flag.  Enter \"Y\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'maplist': "maplist_example", // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
  'summarylist': "summarylist_example", // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.rcraRestServicesGetFacilitiesGet(opts, (error, data, response) => {
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
 **pStdist** | **String**| State District Filter.  Enter a single state district to restrict results. | [optional] 
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
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pCmps** | **String**| RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOlr** | **String**| Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pTrichem** | **String**|  | [optional] 
 **pTriLrPol** | **String**|  | [optional] 
 **pTriLrYr** | **String**|  | [optional] 
 **pTriLrAmt** | **String**|  | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA | [optional] 
 **pOwc** | **String**|  | [optional] 
 **pOwd** | **String**|  | [optional] 
 **pOpc** | **String**|  | [optional] 
 **pOpd** | **String**|  | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] 
 **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] 
 **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] 
 **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] 
 **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] 
 **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] 
 **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] 
 **pVioly** | **Number**| Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation. | [optional] 
 **pNcv** | **String**| Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations. | [optional] 
 **pFcv** | **String**| Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation. | [optional] 
 **pViolt** | **String**| RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \&quot;TSDF\&quot; to return the full enforcement TSDF universe and \&quot;Operating TSDF\&quot; to return the operating TSDF universe. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] 
 **pFacIco** | **String**| FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \&quot;Y\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] 
 **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**RcraRestServicesGetFacilitiesGet200Response**](RcraRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## rcraRestServicesGetFacilitiesPost

> RcraRestServicesGetFacilitiesGet200Response rcraRestServicesGetFacilitiesPost(opts)

Resource Conservation and Recovery Act (RCRA) Facility Search Service

Validates query search parameters and returns query identifier.  Use the responseset parameter to set the page size

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pStdist': "pStdist_example", // String | State District Filter.  Enter a single state district to restrict results.
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
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pCmps': "pCmps_example", // String | RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOlr': "pOlr_example", // String | Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of land releases. - GT0 = More than zero pounds of land releases. - GT1000 = More than one thousand pounds of land releases. - GT5000 = More than five thousand pounds of land releases. - GT10000 = More than ten thousand pounds of land releases. - GT20000 = More than twenty thousand pounds of land releases. - GT50000 = More than fifty thousand pounds of land releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pTrichem': "pTrichem_example", // String | 
  'pTriLrPol': "pTriLrPol_example", // String | 
  'pTriLrYr': "pTriLrYr_example", // String | 
  'pTriLrAmt': "pTriLrAmt_example", // String | 
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Air and Water and RCRA
  'pOwc': "pOwc_example", // String | 
  'pOwd': "pOwd_example", // String | 
  'pOpc': "pOpc_example", // String | 
  'pOpd': "pOpd_example", // String | 
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pOwop': "pOwop_example", // String | Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pIdt1': "pIdt1_example", // String | Beginning of date range of most recent facility inspection.
  'pIdt2': "pIdt2_example", // String | End of date range of most recent facility inspection.
  'pPityp': "pPityp_example", // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
  'pCifdi': "pCifdi_example", // String | Compliance issuess found during inspection.
  'pPfead1': "pPfead1_example", // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfead2': "pPfead2_example", // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfeat': "pPfeat_example", // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
  'pPsncq': "pPsncq_example", // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
  'pDwd': "pDwd_example", // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
  'pVioly': 3.4, // Number | Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
  'pNcv': "pNcv_example", // String | Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
  'pFcv': "pFcv_example", // String | Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
  'pViolt': "pViolt_example", // String | RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
  'pDes': "pDes_example", // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\"TSDF\\\" to return the full enforcement TSDF universe and \\\"Operating TSDF\\\" to return the operating TSDF universe.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pPidall': "pPidall_example", // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
  'pFacIco': "pFacIco_example", // String | FRS tribal land code flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land code.
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pDecouple': "pDecouple_example", // String | Decouple Inspection Code Search Flag.  Enter \\\"Y\\\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'tablelist': "tablelist_example", // String | Table List Flag. Enter a Y to display the first page of facility results.
  'maplist': "maplist_example", // String | Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria).
  'summarylist': "summarylist_example", // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.rcraRestServicesGetFacilitiesPost(opts, (error, data, response) => {
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
 **pStdist** | **String**| State District Filter.  Enter a single state district to restrict results. | [optional] 
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
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pCmps** | **String**| RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOlr** | **String**| Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pTrichem** | **String**|  | [optional] 
 **pTriLrPol** | **String**|  | [optional] 
 **pTriLrYr** | **String**|  | [optional] 
 **pTriLrAmt** | **String**|  | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA | [optional] 
 **pOwc** | **String**|  | [optional] 
 **pOwd** | **String**|  | [optional] 
 **pOpc** | **String**|  | [optional] 
 **pOpd** | **String**|  | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] 
 **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] 
 **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] 
 **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] 
 **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] 
 **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] 
 **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] 
 **pVioly** | **Number**| Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation. | [optional] 
 **pNcv** | **String**| Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations. | [optional] 
 **pFcv** | **String**| Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation. | [optional] 
 **pViolt** | **String**| RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\&quot;TSDF\\\&quot; to return the full enforcement TSDF universe and \\\&quot;Operating TSDF\\\&quot; to return the operating TSDF universe. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] 
 **pFacIco** | **String**| FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \\\&quot;Y\\\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **tablelist** | **String**| Table List Flag. Enter a Y to display the first page of facility results. | [optional] 
 **maplist** | **String**| Map List Flag.  Provide a Y to return mappable coordinates representing the full geographic extent of the queryset (all facilities that met the selection criteria). | [optional] 
 **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**RcraRestServicesGetFacilitiesGet200Response**](RcraRestServicesGetFacilitiesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## rcraRestServicesGetFacilityInfoGet

> RcraRestServicesGetFacilityInfoGet200Response rcraRestServicesGetFacilityInfoGet(opts)

Resource Conservation and Recovery Act (RCRA) Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pStdist': "pStdist_example", // String | State District Filter.  Enter a single state district to restrict results.
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
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pCmps': "pCmps_example", // String | RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOlr': "pOlr_example", // String | Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of land releases. - GT0 = More than zero pounds of land releases. - GT1000 = More than one thousand pounds of land releases. - GT5000 = More than five thousand pounds of land releases. - GT10000 = More than ten thousand pounds of land releases. - GT20000 = More than twenty thousand pounds of land releases. - GT50000 = More than fifty thousand pounds of land releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pTrichem': "pTrichem_example", // String | 
  'pTriLrPol': "pTriLrPol_example", // String | 
  'pTriLrYr': "pTriLrYr_example", // String | 
  'pTriLrAmt': "pTriLrAmt_example", // String | 
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Air and Water and RCRA
  'pOwc': "pOwc_example", // String | 
  'pOwd': "pOwd_example", // String | 
  'pOpc': "pOpc_example", // String | 
  'pOpd': "pOpd_example", // String | 
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pOwop': "pOwop_example", // String | Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pIdt1': "pIdt1_example", // String | Beginning of date range of most recent facility inspection.
  'pIdt2': "pIdt2_example", // String | End of date range of most recent facility inspection.
  'pPityp': "pPityp_example", // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
  'pCifdi': "pCifdi_example", // String | Compliance issuess found during inspection.
  'pPfead1': "pPfead1_example", // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfead2': "pPfead2_example", // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfeat': "pPfeat_example", // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
  'pPsncq': "pPsncq_example", // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
  'pDwd': "pDwd_example", // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
  'pVioly': 3.4, // Number | Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
  'pNcv': "pNcv_example", // String | Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
  'pFcv': "pFcv_example", // String | Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
  'pViolt': "pViolt_example", // String | RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
  'pDes': "pDes_example", // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \"TSDF\" to return the full enforcement TSDF universe and \"Operating TSDF\" to return the operating TSDF universe.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pPidall': "pPidall_example", // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
  'pFacIco': "pFacIco_example", // String | FRS tribal land code flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land code.
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \"Y\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \"Y\" or \"N\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \"Y\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pDecouple': "pDecouple_example", // String | Decouple Inspection Code Search Flag.  Enter \"Y\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'summarylist': "summarylist_example", // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetFacilityInfoGet(opts, (error, data, response) => {
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
 **pStdist** | **String**| State District Filter.  Enter a single state district to restrict results. | [optional] 
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
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pCmps** | **String**| RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOlr** | **String**| Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pTrichem** | **String**|  | [optional] 
 **pTriLrPol** | **String**|  | [optional] 
 **pTriLrYr** | **String**|  | [optional] 
 **pTriLrAmt** | **String**|  | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA | [optional] 
 **pOwc** | **String**|  | [optional] 
 **pOwd** | **String**|  | [optional] 
 **pOpc** | **String**|  | [optional] 
 **pOpd** | **String**|  | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] 
 **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] 
 **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] 
 **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] 
 **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] 
 **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] 
 **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] 
 **pVioly** | **Number**| Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation. | [optional] 
 **pNcv** | **String**| Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations. | [optional] 
 **pFcv** | **String**| Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation. | [optional] 
 **pViolt** | **String**| RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \&quot;TSDF\&quot; to return the full enforcement TSDF universe and \&quot;Operating TSDF\&quot; to return the operating TSDF universe. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] 
 **pFacIco** | **String**| FRS tribal land code flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \&quot;Y\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \&quot;Y\&quot; or \&quot;N\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \&quot;Y\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \&quot;Y\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

[**RcraRestServicesGetFacilityInfoGet200Response**](RcraRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## rcraRestServicesGetFacilityInfoPost

> RcraRestServicesGetFacilityInfoGet200Response rcraRestServicesGetFacilityInfoPost(opts)

Resource Conservation and Recovery Act (RCRA) Facility Enhanced Search Service

Returns either an array of Facilities or an array of Clusters that meet the specified search criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language. - CSV = Facility results formatted as comma delimited file download. - GEOJSON = Facility results formatted as GeoJSON feature collection. - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pSa': "pSa_example", // String | Facility street address. Enter a complete or partial street address.
  'pSa1': "pSa1_example", // String | Facility street address. Enter a complete or partial street address.   Note that p_sa1 is culmulative with p_sa.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pStdist': "pStdist_example", // String | State District Filter.  Enter a single state district to restrict results.
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
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pCmps': "pCmps_example", // String | RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance
  'pLaw': "pLaw_example", // String | Law Statute Code Filter.  Enter a single statute code to limit results.
  'pSection': "pSection_example", // String | Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pImpw': "pImpw_example", // String | Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database.
  'pTrep': "pTrep_example", // String | Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR = Current TRI reporter. - NONCURR = Has reported to TRI in the past but not for the current reporting year.
  'pOlr': "pOlr_example", // String | Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of land releases. - GT0 = More than zero pounds of land releases. - GT1000 = More than one thousand pounds of land releases. - GT5000 = More than five thousand pounds of land releases. - GT10000 = More than ten thousand pounds of land releases. - GT20000 = More than twenty thousand pounds of land releases. - GT50000 = More than fifty thousand pounds of land releases.
  'pOct': "pOct_example", // String | Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z = Zero pounds of chemical releases. - GT0 = More than zero pounds of chemical releases. - GT1000 = More than one thousand pounds of chemical releases. - GT5000 = More than five thousand pounds of chemical releases. - GT10000 = More than ten thousand pounds of chemical releases. - GT20000 = More than twenty thousand pounds of chemical releases. - GT50000 = More than fifty thousand pounds of chemical releases.
  'pTrichem': "pTrichem_example", // String | 
  'pTriLrPol': "pTriLrPol_example", // String | 
  'pTriLrYr': "pTriLrYr_example", // String | 
  'pTriLrAmt': "pTriLrAmt_example", // String | 
  'pPm': "pPm_example", // String | Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE = 0% - GT5 = greater than 5% - GT10 = greater than 10% - GT25 = greater than 25% - GT50 = greater than 50% - GT75 = greater than 75%
  'pPd': "pPd_example", // String | Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE = 0 population density per square mile - GT100 = More than 100 population density per square mile - GT500 = More than 500 population density per square mile - GT1000 = More than 1000 population density per square mile - GT5000 = More than 5000 population density per square mile - GT10000 = More than 10000 population density per square mile - GT20000 = More than 20000 population density per square mile
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
  'pHuc': "pHuc_example", // String | 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values.
  'pWbd': "pWbd_example", // String | 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pMed': "pMed_example", // String | Filter Results by Media. - A = Air - M = RMP (Risk Management Plan) - R = RCRA (Hazardous Waste) - S = SDWA (Public Drinking Water Systems) - W = Water - ALL = Air and Water and RCRA
  'pOwc': "pOwc_example", // String | 
  'pOwd': "pOwd_example", // String | 
  'pOpc': "pOpc_example", // String | 
  'pOpd': "pOpd_example", // String | 
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': 3.4, // Number | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pTribeid': 3.4, // Number | Numeric code for tribe (or list of tribes).
  'pTribename': "pTribename_example", // String | Tribe Name Filter.  Enter a single tribe name to filter results.
  'pTribedist': 3.4, // Number | Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated.
  'pOwop': "pOwop_example", // String | Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL
  'pAgoo': "pAgoo_example", // String | Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters.
  'pIdt1': "pIdt1_example", // String | Beginning of date range of most recent facility inspection.
  'pIdt2': "pIdt2_example", // String | End of date range of most recent facility inspection.
  'pPityp': "pPityp_example", // String | Inspection Type: - CAC = Corrective Action Inspection - CAV = Compliance Assistance Visit - CDI = Case Development Inspection - CEI = Inspection Inspection - CSE = Compliance Schedule Evaluation - FCI = Focused Compliance - FRR = Financial Record Review - FSD = Facility Self Disclosure - FUI = Follow-Up Inspection - GME = Groundwater Monitoring Evaluation - NRR = Non-Financial Record Review - OAM = Operation and Maintenance Inspection May contain multiple comma-separated values.
  'pCifdi': "pCifdi_example", // String | Compliance issuess found during inspection.
  'pPfead1': "pPfead1_example", // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfead2': "pPfead2_example", // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfeat': "pPfeat_example", // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
  'pPsncq': "pPsncq_example", // String | Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z = Zero quarters in significant noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in significant noncompliance.
  'pDwd': "pDwd_example", // String | Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory.
  'pVioly': 3.4, // Number | Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation.
  'pNcv': "pNcv_example", // String | Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations.
  'pFcv': "pFcv_example", // String | Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation.
  'pViolt': "pViolt_example", // String | RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list.
  'pDes': "pDes_example", // String | Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\"TSDF\\\" to return the full enforcement TSDF universe and \\\"Operating TSDF\\\" to return the operating TSDF universe.
  'pFntype': "pFntype_example", // String | Controls type of text search performed on facility name with parameter p_fn. - EXACT = Find facilities having the exact provided name(s). - BEGINS = Find facilities with names starting with the provided term(s). - ALL = Find facilities using Oracle text search terms. - CONTAINS = 
  'pPidall': "pPidall_example", // String | Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc).
  'pFacIco': "pFacIco_example", // String | FRS tribal land code flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land code.
  'pIcoo': "pIcoo_example", // String | Indian country search and/or flag.  Enter \\\"Y\\\" to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned.
  'pFacIcos': "pFacIcos_example", // String | FRS tribal land spatial flag.  Enter \\\"Y\\\" or \\\"N\\\" to include or exclude facilities based on FRS tribal land spatial flag.
  'pEjscreen': "pEjscreen_example", // String | Enter \\\"Y\\\" to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile.
  'pLimitAddr': "pLimitAddr_example", // String | Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.  
  'pLat': 3.4, // Number | Latitude location in decimal degrees.
  'pLong': 3.4, // Number | Longitude location in decimal degrees.
  'pRadius': 3.4, // Number | Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities.
  'pDecouple': "pDecouple_example", // String | Decouple Inspection Code Search Flag.  Enter \\\"Y\\\" to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters.
  'pEjscreenOver80cnt': "pEjscreenOver80cnt_example", // String | The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11.
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'summarylist': "summarylist_example", // String | Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetFacilityInfoPost(opts, (error, data, response) => {
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
 **pStdist** | **String**| State District Filter.  Enter a single state district to restrict results. | [optional] 
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
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pCmps** | **String**| RCRA Current Compliance Status Limiter.  Enter one or more of the following keywords to limit results.  Enter multiple values as a comma-delimited list. - No Violation - In Violation - In Significant Noncompliance | [optional] 
 **pLaw** | **String**| Law Statute Code Filter.  Enter a single statute code to limit results. | [optional] 
 **pSection** | **String**| Law Section Code Filter. Enter one or more law section codes to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pImpw** | **String**| Discharging into Impaired Waters Flag. Enter Y to limit results to facilities with discharge to waterbodies listed as impaired in the ATTAINS database. | [optional] 
 **pTrep** | **String**| Current Toxics Release Inventory (TRI) Reporter Limiter.  Enter one of the following codes to limit results. - CURR &#x3D; Current TRI reporter. - NONCURR &#x3D; Has reported to TRI in the past but not for the current reporting year. | [optional] 
 **pOlr** | **String**| Toxics Release Inventory Pounds of Off-Site Land Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of land releases. - GT0 &#x3D; More than zero pounds of land releases. - GT1000 &#x3D; More than one thousand pounds of land releases. - GT5000 &#x3D; More than five thousand pounds of land releases. - GT10000 &#x3D; More than ten thousand pounds of land releases. - GT20000 &#x3D; More than twenty thousand pounds of land releases. - GT50000 &#x3D; More than fifty thousand pounds of land releases. | [optional] 
 **pOct** | **String**| Toxic Release Inventory Pounds of Off-Site Chemical Releases Limiter.  Enter a keyword to filter results. - Z &#x3D; Zero pounds of chemical releases. - GT0 &#x3D; More than zero pounds of chemical releases. - GT1000 &#x3D; More than one thousand pounds of chemical releases. - GT5000 &#x3D; More than five thousand pounds of chemical releases. - GT10000 &#x3D; More than ten thousand pounds of chemical releases. - GT20000 &#x3D; More than twenty thousand pounds of chemical releases. - GT50000 &#x3D; More than fifty thousand pounds of chemical releases. | [optional] 
 **pTrichem** | **String**|  | [optional] 
 **pTriLrPol** | **String**|  | [optional] 
 **pTriLrYr** | **String**|  | [optional] 
 **pTriLrAmt** | **String**|  | [optional] 
 **pPm** | **String**| Percent Minority Population Limiter.  Enter a value to restrict results to facilities with a given percentage of minority population within 3-mile radius. - NONE &#x3D; 0% - GT5 &#x3D; greater than 5% - GT10 &#x3D; greater than 10% - GT25 &#x3D; greater than 25% - GT50 &#x3D; greater than 50% - GT75 &#x3D; greater than 75% | [optional] 
 **pPd** | **String**| Population Density Limiter (per sq mile). Enter a value to limit results to facilities located in area of a given population density. - NONE &#x3D; 0 population density per square mile - GT100 &#x3D; More than 100 population density per square mile - GT500 &#x3D; More than 500 population density per square mile - GT1000 &#x3D; More than 1000 population density per square mile - GT5000 &#x3D; More than 5000 population density per square mile - GT10000 &#x3D; More than 10000 population density per square mile - GT20000 &#x3D; More than 20000 population density per square mile | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pHuc** | **String**| 2-, 4-, 6-, or 8-character watershed code. May contain multiple comma-separated values. | [optional] 
 **pWbd** | **String**| 2-, 4-, 6-, 8-, 10-, or 12-character watershed (WBD from the USGS Watershed Boundary Dataset). May contain multiple comma-separated values.  Uses the FRS Best Pick Coordinate to obtain the WBD12 Huc value. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pMed** | **String**| Filter Results by Media. - A &#x3D; Air - M &#x3D; RMP (Risk Management Plan) - R &#x3D; RCRA (Hazardous Waste) - S &#x3D; SDWA (Public Drinking Water Systems) - W &#x3D; Water - ALL &#x3D; Air and Water and RCRA | [optional] 
 **pOwc** | **String**|  | [optional] 
 **pOwd** | **String**|  | [optional] 
 **pOpc** | **String**|  | [optional] 
 **pOpd** | **String**|  | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **Number**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pTribeid** | **Number**| Numeric code for tribe (or list of tribes). | [optional] 
 **pTribename** | **String**| Tribe Name Filter.  Enter a single tribe name to filter results. | [optional] 
 **pTribedist** | **Number**| Proximity to tribal land limiter. Enter an amount of mile between 0 and 25 to filter results.  This parameter is only evaluated if p_tribeid is populated. | [optional] 
 **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following codes to filter results: - PUBLIC - PRIVATE - FEDERAL | [optional] 
 **pAgoo** | **String**| Indicates whether to AND or OR the Owner/Operator parameter (p_owop) and the federal agency code (p_fa) parameters. | [optional] 
 **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] 
 **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] 
 **pPityp** | **String**| Inspection Type: - CAC &#x3D; Corrective Action Inspection - CAV &#x3D; Compliance Assistance Visit - CDI &#x3D; Case Development Inspection - CEI &#x3D; Inspection Inspection - CSE &#x3D; Compliance Schedule Evaluation - FCI &#x3D; Focused Compliance - FRR &#x3D; Financial Record Review - FSD &#x3D; Facility Self Disclosure - FUI &#x3D; Follow-Up Inspection - GME &#x3D; Groundwater Monitoring Evaluation - NRR &#x3D; Non-Financial Record Review - OAM &#x3D; Operation and Maintenance Inspection May contain multiple comma-separated values. | [optional] 
 **pCifdi** | **String**| Compliance issuess found during inspection. | [optional] 
 **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] 
 **pPsncq** | **String**| Quarters in Significant Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of significant noncompliance. - Z &#x3D; Zero quarters in significant noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in significant noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in significant noncompliance. | [optional] 
 **pDwd** | **String**| Direct Water Discharges. Pounds of toxic chemicals released directly to surface water as reported to the Toxics Release Inventory. | [optional] 
 **pVioly** | **Number**| Years Since Last Violation Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years since the last violation. | [optional] 
 **pNcv** | **String**| Number of Current Violations Limiter.  Enter a value in the format GTXX replacing XX with a numeric value to select facilities with an equal to greater count of current violations.  Enter Z to select facilities with zero violations. | [optional] 
 **pFcv** | **String**| Years of Continuing Violations Limiter.  Enter a value in the format GTXX where XX is replaced by the number of years in continuing violation. | [optional] 
 **pViolt** | **String**| RCRA Violation Type.  Enter one or more Resource Conservation and Recovery Act violation types to limit results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pDes** | **String**| Universe Designation Limiter.  Enter one or more universe designation codes.  Provide multiple values as a comma-delimited list.  Use code \\\&quot;TSDF\\\&quot; to return the full enforcement TSDF universe and \\\&quot;Operating TSDF\\\&quot; to return the operating TSDF universe. | [optional] 
 **pFntype** | **String**| Controls type of text search performed on facility name with parameter p_fn. - EXACT &#x3D; Find facilities having the exact provided name(s). - BEGINS &#x3D; Find facilities with names starting with the provided term(s). - ALL &#x3D; Find facilities using Oracle text search terms. - CONTAINS &#x3D;  | [optional] 
 **pPidall** | **String**| Controls whether search is restricted to existing system. Y means the search will match the p_pid parameter against all associated permits (AIR, RCRA, SDWIS, etc). | [optional] 
 **pFacIco** | **String**| FRS tribal land code flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land code. | [optional] 
 **pIcoo** | **String**| Indian country search and/or flag.  Enter \\\&quot;Y\\\&quot; to set indian country search conditions to return any results found using p_ico, p_fac_ico or p_fac_icoo.  Otherwise only results matching all provided p_ico, p_fac_ico or p_fac_icoo conditions will be returned. | [optional] 
 **pFacIcos** | **String**| FRS tribal land spatial flag.  Enter \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to include or exclude facilities based on FRS tribal land spatial flag. | [optional] 
 **pEjscreen** | **String**| Enter \\\&quot;Y\\\&quot; to limit facilities to Census block groups where one of more Environmental Justice indexes above 80th percentile. | [optional] 
 **pLimitAddr** | **String**| Limit Address Search Flag.  Enter Y to restrict facility searches to native data source only.   | [optional] 
 **pLat** | **Number**| Latitude location in decimal degrees. | [optional] 
 **pLong** | **Number**| Longitude location in decimal degrees. | [optional] 
 **pRadius** | **Number**| Spatial Search Radius.  Enter a radius up to 100 miles in which to spatially search for facilities. | [optional] 
 **pDecouple** | **String**| Decouple Inspection Code Search Flag.  Enter \\\&quot;Y\\\&quot; to search for inspection code types with p_pityp without respect to the date range search provided with p_ysl* parameters. | [optional] 
 **pEjscreenOver80cnt** | **String**| The number of Environmenmt Justice Indicators above the 80th percentile.  Valid values are 1 through 11. | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **summarylist** | **String**| Summary List Flag.  Enter a Y to return a list of summary statistics based on the parameters submitted to the query service. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 
 **pPrettyPrint** | **Number**| Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost. | [optional] 

### Return type

[**RcraRestServicesGetFacilityInfoGet200Response**](RcraRestServicesGetFacilityInfoGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## rcraRestServicesGetGeojsonGet

> RcraRestServicesGetGeojsonGet200Response rcraRestServicesGetGeojsonGet(qid, opts)

Resource Conservation and Recovery Act (RCRA) GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetGeojsonGet(qid, opts, (error, data, response) => {
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

[**RcraRestServicesGetGeojsonGet200Response**](RcraRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## rcraRestServicesGetGeojsonPost

> RcraRestServicesGetGeojsonGet200Response rcraRestServicesGetGeojsonPost(qid, opts)

Resource Conservation and Recovery Act (RCRA) GeoJSON Service

Based on the QID obtained from a get_facilities or get_facility_info query, return GeoJSON of the facilities found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - GEOJSON = Facility results formatted as GeoJSON feature collection (default). - GEOJSONP = Facility results formatted as GeoJSON feature collection with Padding. - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example", // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetGeojsonPost(qid, opts, (error, data, response) => {
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

[**RcraRestServicesGetGeojsonGet200Response**](RcraRestServicesGetGeojsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## rcraRestServicesGetInfoClustersGet

> File rcraRestServicesGetInfoClustersGet(pQid, opts)

Resource Conservation and Recovery Act (RCRA) Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetInfoClustersGet(pQid, opts, (error, data, response) => {
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


## rcraRestServicesGetInfoClustersPost

> File rcraRestServicesGetInfoClustersPost(pQid, opts)

Resource Conservation and Recovery Act (RCRA) Info Clusters Service

Based on the QID obtained from a clustered get_facility_info query, download cluster facility information as either a CSV or GEOJSON file.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let pQid = "pQid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default). - GEOJSOND = Facility results formatted as GeoJSON feature collection download.
  'pPrettyPrint': 3.4 // Number | Optional flag to request GeoJSON formatted results to be pretty printed.  Only provide a numeric value when the output needs to be human readable as pretty printing has a performance cost.
};
apiInstance.rcraRestServicesGetInfoClustersPost(pQid, opts, (error, data, response) => {
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


## rcraRestServicesGetMapGet

> RcraRestServicesGetMapGet200Response rcraRestServicesGetMapGet(qid, pId, opts)

Resource Conservation and Recovery Act (RCRA) Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
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
apiInstance.rcraRestServicesGetMapGet(qid, pId, opts, (error, data, response) => {
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

[**RcraRestServicesGetMapGet200Response**](RcraRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## rcraRestServicesGetMapPost

> RcraRestServicesGetMapGet200Response rcraRestServicesGetMapPost(qid, pId, opts)

Resource Conservation and Recovery Act (RCRA) Map Service

The purpose of the GET_MAP service is to display facility coordinates and facility clusters related to a get_facilities facility query. Currently, the maximum number of coordinates returned is 500. GET_MAP performs automatic clustering at the state, county, and zip code levels to maximize the number of coordinates returned.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
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
apiInstance.rcraRestServicesGetMapPost(qid, pId, opts, (error, data, response) => {
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

[**RcraRestServicesGetMapGet200Response**](RcraRestServicesGetMapGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## rcraRestServicesGetQidGet

> RcraRestServicesGetQidGet200Response rcraRestServicesGetQidGet(qid, opts)

Resource Conservation and Recovery Act (RCRA) Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.rcraRestServicesGetQidGet(qid, opts, (error, data, response) => {
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

[**RcraRestServicesGetQidGet200Response**](RcraRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## rcraRestServicesGetQidPost

> RcraRestServicesGetQidGet200Response rcraRestServicesGetQidPost(qid, opts)

Resource Conservation and Recovery Act (RCRA) Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_facilities query. It then returns a Facility object containing all matching facilities. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_resource_conservation_and_recovery_act_';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoResourceConservationAndRecoveryAct.ResourceConservationAndRecoveryActApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.rcraRestServicesGetQidPost(qid, opts, (error, data, response) => {
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

[**RcraRestServicesGetQidGet200Response**](RcraRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


# USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.SafeDrinkingWaterApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sdwRestServicesGetDownloadGet**](SafeDrinkingWaterApi.md#sdwRestServicesGetDownloadGet) | **GET** /sdw_rest_services.get_download | Safe Drinking Water Act (SDWA) Download Data Service
[**sdwRestServicesGetDownloadPost**](SafeDrinkingWaterApi.md#sdwRestServicesGetDownloadPost) | **POST** /sdw_rest_services.get_download | Safe Drinking Water Act (SDWA) Download Data Service
[**sdwRestServicesGetQidGet**](SafeDrinkingWaterApi.md#sdwRestServicesGetQidGet) | **GET** /sdw_rest_services.get_qid | Safe Drinking Water Act (SDWA) Paginated Results Service
[**sdwRestServicesGetQidPost**](SafeDrinkingWaterApi.md#sdwRestServicesGetQidPost) | **POST** /sdw_rest_services.get_qid | Safe Drinking Water Act (SDWA) Paginated Results Service
[**sdwRestServicesGetSystemsGet**](SafeDrinkingWaterApi.md#sdwRestServicesGetSystemsGet) | **GET** /sdw_rest_services.get_systems | Safe Drinking Water Act (SDWA) Systems Search Service
[**sdwRestServicesGetSystemsPost**](SafeDrinkingWaterApi.md#sdwRestServicesGetSystemsPost) | **POST** /sdw_rest_services.get_systems | Safe Drinking Water Act (SDWA) Systems Search Service



## sdwRestServicesGetDownloadGet

> File sdwRestServicesGetDownloadGet(qid, opts)

Safe Drinking Water Act (SDWA) Download Data Service

Based on the QID obtained from a get_systems query, return a comma separated value (CSV) file of the water systems found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.SafeDrinkingWaterApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.sdwRestServicesGetDownloadGet(qid, opts, (error, data, response) => {
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


## sdwRestServicesGetDownloadPost

> File sdwRestServicesGetDownloadPost(qid, opts)

Safe Drinking Water Act (SDWA) Download Data Service

Based on the QID obtained from a get_systems query, return a comma separated value (CSV) file of the water systems found.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.SafeDrinkingWaterApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - CSV = Facility results formatted as comma delimited file download (default).
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.sdwRestServicesGetDownloadPost(qid, opts, (error, data, response) => {
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


## sdwRestServicesGetQidGet

> SdwRestServicesGetQidGet200Response sdwRestServicesGetQidGet(qid, opts)

Safe Drinking Water Act (SDWA) Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_systems query. It then returns a Systems object containing all matching water systems. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.SafeDrinkingWaterApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.sdwRestServicesGetQidGet(qid, opts, (error, data, response) => {
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

[**SdwRestServicesGetQidGet200Response**](SdwRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## sdwRestServicesGetQidPost

> SdwRestServicesGetQidGet200Response sdwRestServicesGetQidPost(qid, opts)

Safe Drinking Water Act (SDWA) Paginated Results Service

GET_QID is passed with a query ID corresponding to a previously run get_systems query. It then returns a Systems object containing all matching water systems. The main purpose of GET_QID is for large querysets that contain multiple pages (responsesets) of output. GET_QID allows for pagination and for the selection and sorting of columns. 

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.SafeDrinkingWaterApi();
let qid = "qid_example"; // String | Query ID Selector.  Enter the QueryID number from a previously run query.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pageno': 1.0, // Number | Indicates the number of the page to display. It is used only when the results are paginated.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'newsort': 3.4, // Number | Output Sort Column.  Enter the number of the column on which the data will be sorted. If unpopulated results will sort on the first column.
  'descending': "descending_example", // String | Output Sort Column Descending Flag.  Enter Y to column identified in the newsort parameter descending.  Enter N to use ascending sort order. Used only when newsort parameter is populated.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.sdwRestServicesGetQidPost(qid, opts, (error, data, response) => {
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

[**SdwRestServicesGetQidGet200Response**](SdwRestServicesGetQidGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## sdwRestServicesGetSystemsGet

> SdwRestServicesGetSystemsGet200Response sdwRestServicesGetSystemsGet(opts)

Safe Drinking Water Act (SDWA) Systems Search Service

Returns an array of public water systems that meet the specified search criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.SafeDrinkingWaterApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pZip': "pZip_example", // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
  'pReg': "pReg_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pTrb': "pTrb_example", // String | Tribe name
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \"Y\" or \"N\" to restrict searches to facilities inside or outside Indian Country.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pOwop': "pOwop_example", // String | Owner/Operator code filter.  Enter one of the following codes to filter results: - F = Federal Government - S = State Government - L = Local Government - M = Public/Private - N = Native American - P = Private
  'pSystyp': "pSystyp_example", // String | Type of public water system: - CWS=Community water system - NCWS=Non-community water system - NTCWS=Non-transient non-community water system - TNCWS=Transient non-community water system
  'pSwtyp': "pSwtyp_example", // String | Source Water Type: - SW = Surface water  - GW= Ground water - GU = Ground water under direct influence of (UDI) surface water - SWP = Purchased Surface water - GWP = Purchased Ground water - GUP = Purchased Ground water UDI surface water
  'pPopsv': "pPopsv_example", // String | Estimated average daily population served by a system: - LE500 = 500 or less - IN501_3K = 501-3,300 - IN3K_10K = 3,301-10,000 - IN10K_100K = 10,001-100,000 - IN100K_1M = 100,001-1,000,000 - GT1M = More than 1,000,000 May contain multiple comma-separated values.
  'pCntysv': "pCntysv_example", // String | 
  'pCs': "pCs_example", // String | Current violations: - M = Monitoring and Reporting Violations - H = Health-based Violations - O = Other Violations - P = Public Notice Violations - S = Serious Violator - N = No Violations May contain multiple comma-separated values.
  'pMr': "pMr_example", // String | Monitoring and Reporting Violations (failure to conduct regular monitoring of drinking water quality or submit monitoring results in a timely fashion).
  'pHealth': "pHealth_example", // String | Violations of health-based drinking water standards (maximum contaminant levels, maximum residual disinfectant levels, or treatment technique rules).
  'pOther': "pOther_example", // String | Other violations, such as failing to issue annual consumer confidence reports or maintain required records.
  'pPn': "pPn_example", // String | Public Notice Violations (failure to immediately alert consumers of serious problem with drinking water).
  'pSv': "pSv_example", // String | Serious Violator (unresolved serious, multiple, and/or continuing violations). A value of Y will return only SDWIS systems that are Serious Violators, while a value of N will only return SDWIS Systems that are not Serious Violators.
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pPswpol': "pPswpol_example", // String | For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
  'pPswvio': "pPswvio_example", // String | Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
  'pPbale': "pPbale_example", // String | Lead Action Level Exceedance.  A \"Y\" value will select water systems with at least 1 Lead Action Level Exceedance.
  'pCuale': "pCuale_example", // String | Copper Action Level Exceedance.  A \"Y\" value will select water systems with at least 1 Copper Action Level Exceedance.
  'pRc350v': "pRc350v_example", // String | Rule code 350 violation. A \"Y\" value will select water systems with at least one rule code 350 violation.
  'pPbv': "pPbv_example", // String | Lead Violations.  A \"Y\" value will select water systems with at least 1 Lead Violation.
  'pCuv': "pCuv_example", // String | Copper Violation.  A \"Y\" value will select water systems with at least 1 Copper Violation.
  'pLcrv': "pLcrv_example", // String | Lead or Copper rule violations.  A \"Y\" value will select water systems with at least 1 Lead or Copper Rule Violation.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pQis': "pQis_example", // String | Significant Quarters in Noncompliance Limiter.  Enter one of the following codes to limit results to facilities having given quarters of noncompliance. - Z = Zero quarters in noncompliance. - GE1 = One or more quarters in noncompliance. - GT1 = More than one quarters in noncompliance. - GE2 = Two or more quarters in noncompliance. - GT2 = More than two quarters in noncompliance. - GE4 = Four or more quarters in noncompliance. - GT4 = More than four quarters in noncompliance. - GE8 = Eight or more quarters in noncompliance. - GT8 = More than eight quarters in noncompliance. - GE12 = Twelve or more quarters in noncompliance. - GT12 = Twelve or more quarters in noncompliance. - 12 = Exactly twelve quarters in noncompliance. Note the seemingly incongruous of GT12 is deliberate.
  'pPfead1': "pPfead1_example", // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfead2': "pPfead2_example", // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfeat': "pPfeat_example", // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
  'pSs5yr': "pSs5yr_example", // String | Sanitary Surveys (in past 5 years) flag.  Values of visit_reason_code are either \"SNSV\" or \"SNSP\" in the past 5 years indicate a Sanitary Survey.    Enter \"Y\" to select facilities with Sanitary Surveys within the past 5 years.    Enter \"N\" to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for greater for facilities with a quantity than or equal to that value.   
  'pSdc': "pSdc_example", // String | Significant Deficiency Count (in past 5 years) flag.    Enter \"Y\" to select facilities with Sanitary Surveys within the past 5 years.    Enter \"N\" to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for facilities with a quantity greater than or equal to that value.
  'pSdcIls': "pSdcIls_example", // String | 
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': "pYsly_example", // String | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pIdt1': "pIdt1_example", // String | Beginning of date range of most recent facility inspection.
  'pIdt2': "pIdt2_example", // String | End of date range of most recent facility inspection.
  'pCmsFlag': "pCmsFlag_example", // String | 
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.sdwRestServicesGetSystemsGet(opts, (error, data, response) => {
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
 **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] 
 **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] 
 **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] 
 **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] 
 **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pTrb** | **String**| Tribe name | [optional] 
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \&quot;Y\&quot; or \&quot;N\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following codes to filter results: - F &#x3D; Federal Government - S &#x3D; State Government - L &#x3D; Local Government - M &#x3D; Public/Private - N &#x3D; Native American - P &#x3D; Private | [optional] 
 **pSystyp** | **String**| Type of public water system: - CWS&#x3D;Community water system - NCWS&#x3D;Non-community water system - NTCWS&#x3D;Non-transient non-community water system - TNCWS&#x3D;Transient non-community water system | [optional] 
 **pSwtyp** | **String**| Source Water Type: - SW &#x3D; Surface water  - GW&#x3D; Ground water - GU &#x3D; Ground water under direct influence of (UDI) surface water - SWP &#x3D; Purchased Surface water - GWP &#x3D; Purchased Ground water - GUP &#x3D; Purchased Ground water UDI surface water | [optional] 
 **pPopsv** | **String**| Estimated average daily population served by a system: - LE500 &#x3D; 500 or less - IN501_3K &#x3D; 501-3,300 - IN3K_10K &#x3D; 3,301-10,000 - IN10K_100K &#x3D; 10,001-100,000 - IN100K_1M &#x3D; 100,001-1,000,000 - GT1M &#x3D; More than 1,000,000 May contain multiple comma-separated values. | [optional] 
 **pCntysv** | **String**|  | [optional] 
 **pCs** | **String**| Current violations: - M &#x3D; Monitoring and Reporting Violations - H &#x3D; Health-based Violations - O &#x3D; Other Violations - P &#x3D; Public Notice Violations - S &#x3D; Serious Violator - N &#x3D; No Violations May contain multiple comma-separated values. | [optional] 
 **pMr** | **String**| Monitoring and Reporting Violations (failure to conduct regular monitoring of drinking water quality or submit monitoring results in a timely fashion). | [optional] 
 **pHealth** | **String**| Violations of health-based drinking water standards (maximum contaminant levels, maximum residual disinfectant levels, or treatment technique rules). | [optional] 
 **pOther** | **String**| Other violations, such as failing to issue annual consumer confidence reports or maintain required records. | [optional] 
 **pPn** | **String**| Public Notice Violations (failure to immediately alert consumers of serious problem with drinking water). | [optional] 
 **pSv** | **String**| Serious Violator (unresolved serious, multiple, and/or continuing violations). A value of Y will return only SDWIS systems that are Serious Violators, while a value of N will only return SDWIS Systems that are not Serious Violators. | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pPswpol** | **String**| For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values. | [optional] 
 **pPswvio** | **String**| Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations. | [optional] 
 **pPbale** | **String**| Lead Action Level Exceedance.  A \&quot;Y\&quot; value will select water systems with at least 1 Lead Action Level Exceedance. | [optional] 
 **pCuale** | **String**| Copper Action Level Exceedance.  A \&quot;Y\&quot; value will select water systems with at least 1 Copper Action Level Exceedance. | [optional] 
 **pRc350v** | **String**| Rule code 350 violation. A \&quot;Y\&quot; value will select water systems with at least one rule code 350 violation. | [optional] 
 **pPbv** | **String**| Lead Violations.  A \&quot;Y\&quot; value will select water systems with at least 1 Lead Violation. | [optional] 
 **pCuv** | **String**| Copper Violation.  A \&quot;Y\&quot; value will select water systems with at least 1 Copper Violation. | [optional] 
 **pLcrv** | **String**| Lead or Copper rule violations.  A \&quot;Y\&quot; value will select water systems with at least 1 Lead or Copper Rule Violation. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQis** | **String**| Significant Quarters in Noncompliance Limiter.  Enter one of the following codes to limit results to facilities having given quarters of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GE1 &#x3D; One or more quarters in noncompliance. - GT1 &#x3D; More than one quarters in noncompliance. - GE2 &#x3D; Two or more quarters in noncompliance. - GT2 &#x3D; More than two quarters in noncompliance. - GE4 &#x3D; Four or more quarters in noncompliance. - GT4 &#x3D; More than four quarters in noncompliance. - GE8 &#x3D; Eight or more quarters in noncompliance. - GT8 &#x3D; More than eight quarters in noncompliance. - GE12 &#x3D; Twelve or more quarters in noncompliance. - GT12 &#x3D; Twelve or more quarters in noncompliance. - 12 &#x3D; Exactly twelve quarters in noncompliance. Note the seemingly incongruous of GT12 is deliberate. | [optional] 
 **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] 
 **pSs5yr** | **String**| Sanitary Surveys (in past 5 years) flag.  Values of visit_reason_code are either \&quot;SNSV\&quot; or \&quot;SNSP\&quot; in the past 5 years indicate a Sanitary Survey.    Enter \&quot;Y\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \&quot;N\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for greater for facilities with a quantity than or equal to that value.    | [optional] 
 **pSdc** | **String**| Significant Deficiency Count (in past 5 years) flag.    Enter \&quot;Y\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \&quot;N\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for facilities with a quantity greater than or equal to that value. | [optional] 
 **pSdcIls** | **String**|  | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **String**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] 
 **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] 
 **pCmsFlag** | **String**|  | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**SdwRestServicesGetSystemsGet200Response**](SdwRestServicesGetSystemsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## sdwRestServicesGetSystemsPost

> SdwRestServicesGetSystemsGet200Response sdwRestServicesGetSystemsPost(opts)

Safe Drinking Water Act (SDWA) Systems Search Service

Returns an array of public water systems that meet the specified search criteria.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.SafeDrinkingWaterApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'pFn': "pFn_example", // String | Facility Name Filter. Enter one or more case-insensitive facility names to filter results.  Provide multiple values as a comma-delimited list.  See p_fntype for additional modifiers.
  'pCt': "pCt_example", // String | Facility City Filter. Enter a single case-insensitive city name to filter results.
  'pCo': "pCo_example", // String | Facility County Filter. Provide a single county name in combination with a state value provided via p_st.
  'pFips': "pFips_example", // String | FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059.
  'pSt': "pSt_example", // String | Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list.
  'pZip': "pZip_example", // String | 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values.
  'pReg': "pReg_example", // String | EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region.
  'pTrb': "pTrb_example", // String | Tribe name
  'pAct': "pAct_example", // String | Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits.
  'pQiv': "pQiv_example", // String | Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z = Zero quarters in noncompliance. - GEXX = Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX = Replacing XX with a numeric value, more than that number of quarters in noncompliance.
  'pIco': "pIco_example", // String | Indian Country Flag.  Enter a \\\"Y\\\" or \\\"N\\\" to restrict searches to facilities inside or outside Indian Country.
  'pPid': "pPid_example", // String | Nine-digit permit IDs. May contain up to 2000 comma-separated values.
  'pOwop': "pOwop_example", // String | Owner/Operator code filter.  Enter one of the following codes to filter results: - F = Federal Government - S = State Government - L = Local Government - M = Public/Private - N = Native American - P = Private
  'pSystyp': "pSystyp_example", // String | Type of public water system: - CWS=Community water system - NCWS=Non-community water system - NTCWS=Non-transient non-community water system - TNCWS=Transient non-community water system
  'pSwtyp': "pSwtyp_example", // String | Source Water Type: - SW = Surface water  - GW= Ground water - GU = Ground water under direct influence of (UDI) surface water - SWP = Purchased Surface water - GWP = Purchased Ground water - GUP = Purchased Ground water UDI surface water
  'pPopsv': "pPopsv_example", // String | Estimated average daily population served by a system: - LE500 = 500 or less - IN501_3K = 501-3,300 - IN3K_10K = 3,301-10,000 - IN10K_100K = 10,001-100,000 - IN100K_1M = 100,001-1,000,000 - GT1M = More than 1,000,000 May contain multiple comma-separated values.
  'pCntysv': "pCntysv_example", // String | 
  'pCs': "pCs_example", // String | Current violations: - M = Monitoring and Reporting Violations - H = Health-based Violations - O = Other Violations - P = Public Notice Violations - S = Serious Violator - N = No Violations May contain multiple comma-separated values.
  'pMr': "pMr_example", // String | Monitoring and Reporting Violations (failure to conduct regular monitoring of drinking water quality or submit monitoring results in a timely fashion).
  'pHealth': "pHealth_example", // String | Violations of health-based drinking water standards (maximum contaminant levels, maximum residual disinfectant levels, or treatment technique rules).
  'pOther': "pOther_example", // String | Other violations, such as failing to issue annual consumer confidence reports or maintain required records.
  'pPn': "pPn_example", // String | Public Notice Violations (failure to immediately alert consumers of serious problem with drinking water).
  'pSv': "pSv_example", // String | Serious Violator (unresolved serious, multiple, and/or continuing violations). A value of Y will return only SDWIS systems that are Serious Violators, while a value of N will only return SDWIS Systems that are not Serious Violators.
  'pQs': "pQs_example", // String | Quick Search. Allows entry for city, state, and/or zip code.
  'pSfs': "pSfs_example", // String | Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched.
  'pPswpol': "pPswpol_example", // String | For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values.
  'pPswvio': "pPswvio_example", // String | Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations.
  'pPbale': "pPbale_example", // String | Lead Action Level Exceedance.  A \\\"Y\\\" value will select water systems with at least 1 Lead Action Level Exceedance.
  'pCuale': "pCuale_example", // String | Copper Action Level Exceedance.  A \\\"Y\\\" value will select water systems with at least 1 Copper Action Level Exceedance.
  'pRc350v': "pRc350v_example", // String | Rule code 350 violation. A \\\"Y\\\" value will select water systems with at least one rule code 350 violation.
  'pPbv': "pPbv_example", // String | Lead Violations.  A \\\"Y\\\" value will select water systems with at least 1 Lead Violation.
  'pCuv': "pCuv_example", // String | Copper Violation.  A \\\"Y\\\" value will select water systems with at least 1 Copper Violation.
  'pLcrv': "pLcrv_example", // String | Lead or Copper rule violations.  A \\\"Y\\\" value will select water systems with at least 1 Lead or Copper Rule Violation.
  'pFea': "pFea_example", // String | Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W = within date range - N = not within date range
  'pFeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified.
  'pFeaa': "pFeaa_example", // String | Agency associated with Formal Enforcement Actions: - E = EPA - S = State - A = All
  'pIea': "pIea_example", // String | Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W = within date range - N = not within date range
  'pIeay': 3.4, // Number | Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified.
  'pIeaa': "pIeaa_example", // String | Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E = EPA - S = State
  'pQis': "pQis_example", // String | Significant Quarters in Noncompliance Limiter.  Enter one of the following codes to limit results to facilities having given quarters of noncompliance. - Z = Zero quarters in noncompliance. - GE1 = One or more quarters in noncompliance. - GT1 = More than one quarters in noncompliance. - GE2 = Two or more quarters in noncompliance. - GT2 = More than two quarters in noncompliance. - GE4 = Four or more quarters in noncompliance. - GT4 = More than four quarters in noncompliance. - GE8 = Eight or more quarters in noncompliance. - GT8 = More than eight quarters in noncompliance. - GE12 = Twelve or more quarters in noncompliance. - GT12 = Twelve or more quarters in noncompliance. - 12 = Exactly twelve quarters in noncompliance. Note the seemingly incongruous of GT12 is deliberate.
  'pPfead1': "pPfead1_example", // String | Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfead2': "pPfead2_example", // String | Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years.
  'pPfeat': "pPfeat_example", // String | Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list.
  'pSs5yr': "pSs5yr_example", // String | Sanitary Surveys (in past 5 years) flag.  Values of visit_reason_code are either \\\"SNSV\\\" or \\\"SNSP\\\" in the past 5 years indicate a Sanitary Survey.    Enter \\\"Y\\\" to select facilities with Sanitary Surveys within the past 5 years.    Enter \\\"N\\\" to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for greater for facilities with a quantity than or equal to that value.   
  'pSdc': "pSdc_example", // String | Significant Deficiency Count (in past 5 years) flag.    Enter \\\"Y\\\" to select facilities with Sanitary Surveys within the past 5 years.    Enter \\\"N\\\" to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for facilities with a quantity greater than or equal to that value.
  'pSdcIls': "pSdcIls_example", // String | 
  'pYsl': "pYsl_example", // String | Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W = within date range - N = not within date range
  'pYsly': "pYsly_example", // String | Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year.
  'pYsla': "pYsla_example", // String | Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E = EPA - S = State
  'pIdt1': "pIdt1_example", // String | Beginning of date range of most recent facility inspection.
  'pIdt2': "pIdt2_example", // String | End of date range of most recent facility inspection.
  'pCmsFlag': "pCmsFlag_example", // String | 
  'queryset': 3.4, // Number | Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000.
  'responseset': 3.4, // Number | Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'qcolumns': "qcolumns_example" // String | Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions.
};
apiInstance.sdwRestServicesGetSystemsPost(opts, (error, data, response) => {
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
 **pCt** | **String**| Facility City Filter. Enter a single case-insensitive city name to filter results. | [optional] 
 **pCo** | **String**| Facility County Filter. Provide a single county name in combination with a state value provided via p_st. | [optional] 
 **pFips** | **String**| FIPS Code Filter.  Enter a single 5-character Federal Information Processing Standards (FIPS) state + county value to restrict results.  E.g. to limit results to Kenosha County, Wisconsin, use 55059. | [optional] 
 **pSt** | **String**| Facility State and State-Equivalent Filter.  Provide one or more USPS postal abbreviations for states and state-equivalents to filter results.  Provide multiple values as a comma-delimited list. | [optional] 
 **pZip** | **String**| 5-Digit ZIP Code Filter. Provide one or more 5-digit postal zip codes to filter results.  May contain multiple comma-separated values. | [optional] 
 **pReg** | **String**| EPA Region Filter. Provide a single value of 01 thru 10 to restrict results to a single EPA region. | [optional] 
 **pTrb** | **String**| Tribe name | [optional] 
 **pAct** | **String**| Active Permits/Facilities Flag.  Provide Y or N to filter results to facilities with active permits. | [optional] 
 **pQiv** | **String**| Quarters in Noncompliance Limiter.  Enter a coded value to limit results to facilities with given quarter of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GEXX &#x3D; Replacing XX with a numeric value, that number of quarterd or more in noncompliance. - GTXX &#x3D; Replacing XX with a numeric value, more than that number of quarters in noncompliance. | [optional] 
 **pIco** | **String**| Indian Country Flag.  Enter a \\\&quot;Y\\\&quot; or \\\&quot;N\\\&quot; to restrict searches to facilities inside or outside Indian Country. | [optional] 
 **pPid** | **String**| Nine-digit permit IDs. May contain up to 2000 comma-separated values. | [optional] 
 **pOwop** | **String**| Owner/Operator code filter.  Enter one of the following codes to filter results: - F &#x3D; Federal Government - S &#x3D; State Government - L &#x3D; Local Government - M &#x3D; Public/Private - N &#x3D; Native American - P &#x3D; Private | [optional] 
 **pSystyp** | **String**| Type of public water system: - CWS&#x3D;Community water system - NCWS&#x3D;Non-community water system - NTCWS&#x3D;Non-transient non-community water system - TNCWS&#x3D;Transient non-community water system | [optional] 
 **pSwtyp** | **String**| Source Water Type: - SW &#x3D; Surface water  - GW&#x3D; Ground water - GU &#x3D; Ground water under direct influence of (UDI) surface water - SWP &#x3D; Purchased Surface water - GWP &#x3D; Purchased Ground water - GUP &#x3D; Purchased Ground water UDI surface water | [optional] 
 **pPopsv** | **String**| Estimated average daily population served by a system: - LE500 &#x3D; 500 or less - IN501_3K &#x3D; 501-3,300 - IN3K_10K &#x3D; 3,301-10,000 - IN10K_100K &#x3D; 10,001-100,000 - IN100K_1M &#x3D; 100,001-1,000,000 - GT1M &#x3D; More than 1,000,000 May contain multiple comma-separated values. | [optional] 
 **pCntysv** | **String**|  | [optional] 
 **pCs** | **String**| Current violations: - M &#x3D; Monitoring and Reporting Violations - H &#x3D; Health-based Violations - O &#x3D; Other Violations - P &#x3D; Public Notice Violations - S &#x3D; Serious Violator - N &#x3D; No Violations May contain multiple comma-separated values. | [optional] 
 **pMr** | **String**| Monitoring and Reporting Violations (failure to conduct regular monitoring of drinking water quality or submit monitoring results in a timely fashion). | [optional] 
 **pHealth** | **String**| Violations of health-based drinking water standards (maximum contaminant levels, maximum residual disinfectant levels, or treatment technique rules). | [optional] 
 **pOther** | **String**| Other violations, such as failing to issue annual consumer confidence reports or maintain required records. | [optional] 
 **pPn** | **String**| Public Notice Violations (failure to immediately alert consumers of serious problem with drinking water). | [optional] 
 **pSv** | **String**| Serious Violator (unresolved serious, multiple, and/or continuing violations). A value of Y will return only SDWIS systems that are Serious Violators, while a value of N will only return SDWIS Systems that are not Serious Violators. | [optional] 
 **pQs** | **String**| Quick Search. Allows entry for city, state, and/or zip code. | [optional] 
 **pSfs** | **String**| Single Facility Search Filter.  Provide a facility name or program system identifier to limit results.  For the all data search, the FRS registry identifier is also searched. | [optional] 
 **pPswpol** | **String**| For CWA, pollutant names for surface water discharges. for Drinking Water, SDWIS Violation contaminant codes for unaddressed violations that have occurred in the last 3 years. May contain multiple comma-separated values. | [optional] 
 **pPswvio** | **String**| Used in conjuction with parameters p_pswpol and p_pswparam, indicates whether search should only include pollutants with violations. | [optional] 
 **pPbale** | **String**| Lead Action Level Exceedance.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Lead Action Level Exceedance. | [optional] 
 **pCuale** | **String**| Copper Action Level Exceedance.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Copper Action Level Exceedance. | [optional] 
 **pRc350v** | **String**| Rule code 350 violation. A \\\&quot;Y\\\&quot; value will select water systems with at least one rule code 350 violation. | [optional] 
 **pPbv** | **String**| Lead Violations.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Lead Violation. | [optional] 
 **pCuv** | **String**| Copper Violation.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Copper Violation. | [optional] 
 **pLcrv** | **String**| Lead or Copper rule violations.  A \\\&quot;Y\\\&quot; value will select water systems with at least 1 Lead or Copper Rule Violation. | [optional] 
 **pFea** | **String**| Formal Enforcement Actions [within / not within] specified date range indicator. The date range is determined by parameters p_fead1 and p_fead2 or by parameter p_feay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pFeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Formal Enforcement Actions (FEA). Used along with p_fea (which indicates whether to look within or outside of the date range) to find FEAs within (or not within) the number of years specified. | [optional] 
 **pFeaa** | **String**| Agency associated with Formal Enforcement Actions: - E &#x3D; EPA - S &#x3D; State - A &#x3D; All | [optional] 
 **pIea** | **String**| Informal Enforcement Actions [within / not within] specified date range.  The date range is determined by parameters p_iead1 and p_iead2 or by parameter p_ieay. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pIeay** | **Number**| Years (1 to 5) Range.  This value is used to create a date range for Informal Enforcement Actions (IEA). Used along with p_iea (which indicates whether to look within or outside of the date range) to find IEAs within (or not within) the number of years specified. | [optional] 
 **pIeaa** | **String**| Agency associated with Informal Enforcement Actions. If left blank, both agencies are included. - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pQis** | **String**| Significant Quarters in Noncompliance Limiter.  Enter one of the following codes to limit results to facilities having given quarters of noncompliance. - Z &#x3D; Zero quarters in noncompliance. - GE1 &#x3D; One or more quarters in noncompliance. - GT1 &#x3D; More than one quarters in noncompliance. - GE2 &#x3D; Two or more quarters in noncompliance. - GT2 &#x3D; More than two quarters in noncompliance. - GE4 &#x3D; Four or more quarters in noncompliance. - GT4 &#x3D; More than four quarters in noncompliance. - GE8 &#x3D; Eight or more quarters in noncompliance. - GT8 &#x3D; More than eight quarters in noncompliance. - GE12 &#x3D; Twelve or more quarters in noncompliance. - GT12 &#x3D; Twelve or more quarters in noncompliance. - 12 &#x3D; Exactly twelve quarters in noncompliance. Note the seemingly incongruous of GT12 is deliberate. | [optional] 
 **pPfead1** | **String**| Formal Enforcement Action Date Range Start.  Enter a date in MM/DD/YYYY format to set the start of the range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfead2** | **String**| Formal Enforcement Action Date Range End.  Enter a date in MM/DD/YYYY format to set the end of the date range for filtering by recent Formal Enforcement Action (FEA) taken against the facility within the last five years. | [optional] 
 **pPfeat** | **String**| Formal Enforcement Action (FEA) Code Filter.  Enter one or more three-letter FEA codes to restrict results to facilities with these attributes.  Use p_fead1 and p_fead2 parameters to further restrict this filter by entering a date range.  Provide multiple codes as a comma-delimited list. | [optional] 
 **pSs5yr** | **String**| Sanitary Surveys (in past 5 years) flag.  Values of visit_reason_code are either \\\&quot;SNSV\\\&quot; or \\\&quot;SNSP\\\&quot; in the past 5 years indicate a Sanitary Survey.    Enter \\\&quot;Y\\\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \\\&quot;N\\\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for greater for facilities with a quantity than or equal to that value.    | [optional] 
 **pSdc** | **String**| Significant Deficiency Count (in past 5 years) flag.    Enter \\\&quot;Y\\\&quot; to select facilities with Sanitary Surveys within the past 5 years.    Enter \\\&quot;N\\\&quot; to select facilities without Sanitary Surveys in the past 5 years.  Enter a number to search for facilities with a quantity greater than or equal to that value. | [optional] 
 **pSdcIls** | **String**|  | [optional] 
 **pYsl** | **String**| Last Facility Inspection [within / not within] Specified Date Range Indicator. The date range is determined by parameters p_idt1 and p_idt2 or by parameter p_ysly. - W &#x3D; within date range - N &#x3D; not within date range | [optional] 
 **pYsly** | **String**| Number of years (1 to 5) since last facility inspection.  A value of 1 means that it has been inspected within the year. | [optional] 
 **pYsla** | **String**| Facility Last Inspection Code Filter.  If left blank, both agencies are included.  Enter a value to limit results: - E &#x3D; EPA - S &#x3D; State | [optional] 
 **pIdt1** | **String**| Beginning of date range of most recent facility inspection. | [optional] 
 **pIdt2** | **String**| End of date range of most recent facility inspection. | [optional] 
 **pCmsFlag** | **String**|  | [optional] 
 **queryset** | **Number**| Query Limiter.  Enter a value to limit the number of records returned for each query. Value cannot exceed 70,000. | [optional] 
 **responseset** | **Number**| Response Set Limiter. Enter a value to limit the number of records per page. Value cannot exceed 1,000. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **qcolumns** | **String**| Used to customize service output.  A list of comma-separated column IDs of output objects that will be returned in the service query object or download.  Use the metadata service endpoint for a complete list of Ids and definitions. | [optional] 

### Return type

[**SdwRestServicesGetSystemsGet200Response**](SdwRestServicesGetSystemsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


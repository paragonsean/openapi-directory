# USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.EffluentChartsApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**effRestServicesDownloadEffluentChartGet**](EffluentChartsApi.md#effRestServicesDownloadEffluentChartGet) | **GET** /eff_rest_services.download_effluent_chart | Effluent Charts Download Service
[**effRestServicesDownloadEffluentChartPost**](EffluentChartsApi.md#effRestServicesDownloadEffluentChartPost) | **POST** /eff_rest_services.download_effluent_chart | Effluent Charts Download Service
[**effRestServicesGetEffluentChartGet**](EffluentChartsApi.md#effRestServicesGetEffluentChartGet) | **GET** /eff_rest_services.get_effluent_chart | Detailed Effluent Chart Service
[**effRestServicesGetEffluentChartPost**](EffluentChartsApi.md#effRestServicesGetEffluentChartPost) | **POST** /eff_rest_services.get_effluent_chart | Detailed Effluent Chart Service
[**effRestServicesGetSummaryChartGet**](EffluentChartsApi.md#effRestServicesGetSummaryChartGet) | **GET** /eff_rest_services.get_summary_chart | Summary Effluent Chart Service
[**effRestServicesGetSummaryChartPost**](EffluentChartsApi.md#effRestServicesGetSummaryChartPost) | **POST** /eff_rest_services.get_summary_chart | Summary Effluent Chart Service



## effRestServicesDownloadEffluentChartGet

> File effRestServicesDownloadEffluentChartGet(pId, opts)

Effluent Charts Download Service

Downloads tabular Discharge Monitoring Report (DMR) and compliance data for one NPDES permit as a CSV.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.EffluentChartsApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'outfall': "outfall_example", // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
  'parameterCode': "parameterCode_example", // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
  'startDate': "startDate_example", // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'endDate': "endDate_example" // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
};
apiInstance.effRestServicesDownloadEffluentChartGet(pId, opts, (error, data, response) => {
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
 **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] 
 **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] 
 **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## effRestServicesDownloadEffluentChartPost

> File effRestServicesDownloadEffluentChartPost(pId, opts)

Effluent Charts Download Service

Downloads tabular Discharge Monitoring Report (DMR) and compliance data for one NPDES permit as a CSV.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.EffluentChartsApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'outfall': "outfall_example", // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
  'parameterCode': "parameterCode_example", // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
  'startDate': "startDate_example", // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'endDate': "endDate_example" // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
};
apiInstance.effRestServicesDownloadEffluentChartPost(pId, opts, (error, data, response) => {
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
 **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] 
 **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] 
 **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## effRestServicesGetEffluentChartGet

> EffRestServicesGetEffluentChartGet200Response effRestServicesGetEffluentChartGet(pId, opts)

Detailed Effluent Chart Service

Discharge Monitoring Report (DMR) data supporting each effluent chart for one NPDES permit. Includes Discharge Monitoring Reports and NPDES Violations.   

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.EffluentChartsApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'outfall': "outfall_example", // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
  'parameterCode': "parameterCode_example", // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
  'startDate': "startDate_example", // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'endDate': "endDate_example", // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.effRestServicesGetEffluentChartGet(pId, opts, (error, data, response) => {
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
 **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] 
 **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] 
 **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**EffRestServicesGetEffluentChartGet200Response**](EffRestServicesGetEffluentChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## effRestServicesGetEffluentChartPost

> EffRestServicesGetEffluentChartGet200Response effRestServicesGetEffluentChartPost(pId, opts)

Detailed Effluent Chart Service

Discharge Monitoring Report (DMR) data supporting each effluent chart for one NPDES permit. Includes Discharge Monitoring Reports and NPDES Violations.   

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.EffluentChartsApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'outfall': "outfall_example", // String | Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge.
  'parameterCode': "parameterCode_example", // String | Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes.
  'startDate': "startDate_example", // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'endDate': "endDate_example", // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.effRestServicesGetEffluentChartPost(pId, opts, (error, data, response) => {
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
 **outfall** | **String**| Three-character code that identifies the point of discharge (e.g., pipe or outfall) for a facility. A single NPDES ID may have multiple points of discharge. | [optional] 
 **parameterCode** | **String**| Five-digit numeric code identifying the parameter. See Parameter Lookup documentation for a complete list of codes. | [optional] 
 **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 

### Return type

[**EffRestServicesGetEffluentChartGet200Response**](EffRestServicesGetEffluentChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## effRestServicesGetSummaryChartGet

> EffRestServicesGetSummaryChartGet200Response effRestServicesGetSummaryChartGet(pId, opts)

Summary Effluent Chart Service

Summary of compliance status each outfall and parameter for one NPDES permit. Provides the current compliance status and overall compliance status for the date range of interest. This service supports the Summary Matrix on the Effluent Charts.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.EffluentChartsApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'startDate': "startDate_example", // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'endDate': "endDate_example" // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
};
apiInstance.effRestServicesGetSummaryChartGet(pId, opts, (error, data, response) => {
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
 **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 

### Return type

[**EffRestServicesGetSummaryChartGet200Response**](EffRestServicesGetSummaryChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## effRestServicesGetSummaryChartPost

> EffRestServicesGetSummaryChartGet200Response effRestServicesGetSummaryChartPost(pId, opts)

Summary Effluent Chart Service

Summary of compliance status each outfall and parameter for one NPDES permit. Provides the current compliance status and overall compliance status for the date range of interest. This service supports the Summary Matrix on the Effluent Charts.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.EffluentChartsApi();
let pId = "pId_example"; // String | Identifier for the service.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'startDate': "startDate_example", // String | The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data.
  'endDate': "endDate_example" // String | The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data.
};
apiInstance.effRestServicesGetSummaryChartPost(pId, opts, (error, data, response) => {
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
 **startDate** | **String**| The start date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with end_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 
 **endDate** | **String**| The end date (mm/dd/yyyy) for the date range of interest. Must be used in conjunction with start_date. If start_date and end_date are not specified, the service will return the last three years of data. | [optional] 

### Return type

[**EffRestServicesGetSummaryChartGet200Response**](EffRestServicesGetSummaryChartGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


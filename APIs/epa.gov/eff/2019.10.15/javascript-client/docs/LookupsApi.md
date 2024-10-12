# USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.LookupsApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restLookupsCwaParametersGet**](LookupsApi.md#restLookupsCwaParametersGet) | **GET** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service
[**restLookupsCwaParametersPost**](LookupsApi.md#restLookupsCwaParametersPost) | **POST** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service



## restLookupsCwaParametersGet

> RestLookupsCwaParametersGet200Response restLookupsCwaParametersGet(opts)

ECHO CWA Parameter Lookup Service

Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsCwaParametersGet(opts, (error, data, response) => {
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
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsCwaParametersGet200Response**](RestLookupsCwaParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsCwaParametersPost

> RestLookupsCwaParametersGet200Response restLookupsCwaParametersPost(opts)

ECHO CWA Parameter Lookup Service

Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting from 'u_s__epa_enforcement_and_compliance_history_online__echo_effluent_charting_and_reporting';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEffluentChartingAndReporting.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsCwaParametersPost(opts, (error, data, response) => {
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
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsCwaParametersGet200Response**](RestLookupsCwaParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


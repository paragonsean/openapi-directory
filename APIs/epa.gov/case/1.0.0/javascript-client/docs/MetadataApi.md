# USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.MetadataApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**caseRestServicesMetadataGet**](MetadataApi.md#caseRestServicesMetadataGet) | **GET** /case_rest_services.metadata | Enforcement Case Metadata Service
[**caseRestServicesMetadataPost**](MetadataApi.md#caseRestServicesMetadataPost) | **POST** /case_rest_services.metadata | Enforcement Case Metadata Service



## caseRestServicesMetadataGet

> CaseRestServicesMetadataGet200Response caseRestServicesMetadataGet(opts)

Enforcement Case Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_cases endpoint.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesMetadataGet(opts, (error, data, response) => {
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

### Return type

[**CaseRestServicesMetadataGet200Response**](CaseRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## caseRestServicesMetadataPost

> CaseRestServicesMetadataGet200Response caseRestServicesMetadataPost(opts)

Enforcement Case Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_cases endpoint.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.caseRestServicesMetadataPost(opts, (error, data, response) => {
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

### Return type

[**CaseRestServicesMetadataGet200Response**](CaseRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


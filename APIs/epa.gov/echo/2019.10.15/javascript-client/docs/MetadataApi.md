# USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.MetadataApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echoRestServicesMetadataGet**](MetadataApi.md#echoRestServicesMetadataGet) | **GET** /echo_rest_services.metadata | Combined ECHO Metadata Service
[**echoRestServicesMetadataPost**](MetadataApi.md#echoRestServicesMetadataPost) | **POST** /echo_rest_services.metadata | Combined ECHO Metadata Service



## echoRestServicesMetadataGet

> EchoRestServicesMetadataGet200Response echoRestServicesMetadataGet(opts)

Combined ECHO Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_qid, get_facility_info and other service endpoints.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.echoRestServicesMetadataGet(opts, (error, data, response) => {
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

[**EchoRestServicesMetadataGet200Response**](EchoRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## echoRestServicesMetadataPost

> EchoRestServicesMetadataGet200Response echoRestServicesMetadataPost(opts)

Combined ECHO Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_qid, get_facility_info and other service endpoints.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoAllData from 'u_s__epa_enforcement_and_compliance_history_online__echo_all_data';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoAllData.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.echoRestServicesMetadataPost(opts, (error, data, response) => {
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

[**EchoRestServicesMetadataGet200Response**](EchoRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


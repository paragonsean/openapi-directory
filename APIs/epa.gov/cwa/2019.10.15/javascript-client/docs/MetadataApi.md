# USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.MetadataApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cwaRestServicesMetadataGet**](MetadataApi.md#cwaRestServicesMetadataGet) | **GET** /cwa_rest_services.metadata | Clean Water Act (CWA) Metadata Service
[**cwaRestServicesMetadataPost**](MetadataApi.md#cwaRestServicesMetadataPost) | **POST** /cwa_rest_services.metadata | Clean Water Act (CWA) Metadata Service



## cwaRestServicesMetadataGet

> CwaRestServicesMetadataGet200Response cwaRestServicesMetadataGet(opts)

Clean Water Act (CWA) Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_qid, get_facility_info and other service endpoints.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.cwaRestServicesMetadataGet(opts, (error, data, response) => {
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

[**CwaRestServicesMetadataGet200Response**](CwaRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## cwaRestServicesMetadataPost

> CwaRestServicesMetadataGet200Response cwaRestServicesMetadataPost(opts)

Clean Water Act (CWA) Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_qid, get_facility_info and other service endpoints.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.cwaRestServicesMetadataPost(opts, (error, data, response) => {
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

[**CwaRestServicesMetadataGet200Response**](CwaRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


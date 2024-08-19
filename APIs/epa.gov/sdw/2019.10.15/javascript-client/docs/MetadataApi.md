# USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.MetadataApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sdwRestServicesMetadataGet**](MetadataApi.md#sdwRestServicesMetadataGet) | **GET** /sdw_rest_services.metadata | Safe Drinking Water Act (SDWA) Metadata Service
[**sdwRestServicesMetadataPost**](MetadataApi.md#sdwRestServicesMetadataPost) | **POST** /sdw_rest_services.metadata | Safe Drinking Water Act (SDWA) Metadata Service



## sdwRestServicesMetadataGet

> SdwRestServicesMetadataGet200Response sdwRestServicesMetadataGet(opts)

Safe Drinking Water Act (SDWA) Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_systems endpoint.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.sdwRestServicesMetadataGet(opts, (error, data, response) => {
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

[**SdwRestServicesMetadataGet200Response**](SdwRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## sdwRestServicesMetadataPost

> SdwRestServicesMetadataGet200Response sdwRestServicesMetadataPost(opts)

Safe Drinking Water Act (SDWA) Metadata Service

Returns the JSON Object Name and ColumnId for usage with the qcolumns parameter for get_systems endpoint.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct from 'u_s__epa_enforcement_and_compliance_history_online__echo_safe_drinking_water_act';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoSafeDrinkingWaterAct.MetadataApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example" // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
};
apiInstance.sdwRestServicesMetadataPost(opts, (error, data, response) => {
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

[**SdwRestServicesMetadataGet200Response**](SdwRestServicesMetadataGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


# OoxmlAutomation.SharedGradientStopsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedGradientstopsGetId**](SharedGradientStopsApi.md#sharedGradientstopsGetId) | **GET** /Shared/GradientStops/{id} | GradientStops: Get by Id



## sharedGradientstopsGetId

> SharedGradientStops sharedGradientstopsGetId(id)

GradientStops: Get by Id

Get by Id: Use this method to retrieve a GradientStops object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedGradientStopsApi();
let id = "id_example"; // String | 
apiInstance.sharedGradientstopsGetId(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**SharedGradientStops**](SharedGradientStops.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


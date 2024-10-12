# OoxmlAutomation.SharedGradientFillsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedGradientfillsGetId**](SharedGradientFillsApi.md#sharedGradientfillsGetId) | **GET** /Shared/GradientFills/{id} | GradientFills: Get by Id



## sharedGradientfillsGetId

> SharedGradientFills sharedGradientfillsGetId(id)

GradientFills: Get by Id

Get by Id: Use this method to retrieve a GradientFills object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedGradientFillsApi();
let id = "id_example"; // String | 
apiInstance.sharedGradientfillsGetId(id, (error, data, response) => {
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

[**SharedGradientFills**](SharedGradientFills.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OoxmlAutomation.SharedSolidFillsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedSolidfillsGetId**](SharedSolidFillsApi.md#sharedSolidfillsGetId) | **GET** /Shared/SolidFills/{id} | SolidFills: Get by Id



## sharedSolidfillsGetId

> SharedSolidFills sharedSolidfillsGetId(id)

SolidFills: Get by Id

Get by Id: Use this method to retrieve a SolidFills object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedSolidFillsApi();
let id = "id_example"; // String | 
apiInstance.sharedSolidfillsGetId(id, (error, data, response) => {
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

[**SharedSolidFills**](SharedSolidFills.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


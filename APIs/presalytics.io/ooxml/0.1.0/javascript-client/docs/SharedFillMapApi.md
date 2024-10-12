# OoxmlAutomation.SharedFillMapApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedFillmapGetId**](SharedFillMapApi.md#sharedFillmapGetId) | **GET** /Shared/FillMap/{id} | FillMap: Get by Id



## sharedFillmapGetId

> SharedFillMap sharedFillmapGetId(id)

FillMap: Get by Id

Get by Id: Use this method to retrieve a FillMap object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedFillMapApi();
let id = "id_example"; // String | 
apiInstance.sharedFillmapGetId(id, (error, data, response) => {
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

[**SharedFillMap**](SharedFillMap.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


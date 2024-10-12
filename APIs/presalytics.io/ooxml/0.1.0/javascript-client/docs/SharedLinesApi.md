# OoxmlAutomation.SharedLinesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedLinesGetId**](SharedLinesApi.md#sharedLinesGetId) | **GET** /Shared/Lines/{id} | Lines: Get by Id



## sharedLinesGetId

> SharedLines sharedLinesGetId(id)

Lines: Get by Id

Get by Id: Use this method to retrieve a Lines object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedLinesApi();
let id = "id_example"; // String | 
apiInstance.sharedLinesGetId(id, (error, data, response) => {
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

[**SharedLines**](SharedLines.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


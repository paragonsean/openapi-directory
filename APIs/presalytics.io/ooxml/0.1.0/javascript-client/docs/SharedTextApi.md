# OoxmlAutomation.SharedTextApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedTextGetId**](SharedTextApi.md#sharedTextGetId) | **GET** /Shared/Text/{id} | Text: Get by Id



## sharedTextGetId

> SharedText sharedTextGetId(id)

Text: Get by Id

Get by Id: Use this method to retrieve a Text object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedTextApi();
let id = "id_example"; // String | 
apiInstance.sharedTextGetId(id, (error, data, response) => {
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

[**SharedText**](SharedText.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


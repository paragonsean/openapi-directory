# OoxmlAutomation.SharedTextContainerApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedTextcontainerGetId**](SharedTextContainerApi.md#sharedTextcontainerGetId) | **GET** /Shared/TextContainer/{id} | TextContainer: Get by Id



## sharedTextcontainerGetId

> SharedTextContainer sharedTextcontainerGetId(id)

TextContainer: Get by Id

Get by Id: Use this method to retrieve a TextContainer object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedTextContainerApi();
let id = "id_example"; // String | 
apiInstance.sharedTextcontainerGetId(id, (error, data, response) => {
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

[**SharedTextContainer**](SharedTextContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OoxmlAutomation.SharedImageFillsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedImagefillsGetId**](SharedImageFillsApi.md#sharedImagefillsGetId) | **GET** /Shared/ImageFills/{id} | ImageFills: Get by Id



## sharedImagefillsGetId

> SharedImageFills sharedImagefillsGetId(id)

ImageFills: Get by Id

Get by Id: Use this method to retrieve a ImageFills object by its primary key (id)

### Example

```javascript
import OoxmlAutomation from 'ooxml_automation';

let apiInstance = new OoxmlAutomation.SharedImageFillsApi();
let id = "id_example"; // String | 
apiInstance.sharedImagefillsGetId(id, (error, data, response) => {
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

[**SharedImageFills**](SharedImageFills.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# SmartMe.FolderApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folderGet**](FolderApi.md#folderGet) | **GET** /api/Folder/{id} | Gets the Values for a folder or a meter



## folderGet

> FolderData folderGet(id)

Gets the Values for a folder or a meter

Gets the Values for a folder or a meter

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FolderApi();
let id = "id_example"; // String | 
apiInstance.folderGet(id, (error, data, response) => {
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

[**FolderData**](FolderData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


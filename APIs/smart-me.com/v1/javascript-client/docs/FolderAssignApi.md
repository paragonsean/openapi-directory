# SmartMe.FolderAssignApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folderAssignPost**](FolderAssignApi.md#folderAssignPost) | **POST** /api/folder/assign | Assign a folder (source) or meter to another folder (target). Can be used to create a folder structure.



## folderAssignPost

> folderAssignPost(source, target)

Assign a folder (source) or meter to another folder (target). Can be used to create a folder structure.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FolderAssignApi();
let source = "source_example"; // String | The ID of the meter or folder that should be assign
let target = "target_example"; // String | The ID of the meter or folder that should be the parent
apiInstance.folderAssignPost(source, target, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **String**| The ID of the meter or folder that should be assign | 
 **target** | **String**| The ID of the meter or folder that should be the parent | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


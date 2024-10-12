# SmartMe.UserToFolderAssignApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userToFolderAssignDelete**](UserToFolderAssignApi.md#userToFolderAssignDelete) | **DELETE** /api/folder/user/assign | Deletes a user to folder assignement
[**userToFolderAssignPost**](UserToFolderAssignApi.md#userToFolderAssignPost) | **POST** /api/folder/user/assign | Assign a user to a folder



## userToFolderAssignDelete

> userToFolderAssignDelete(source, target)

Deletes a user to folder assignement

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.UserToFolderAssignApi();
let source = "source_example"; // String | The ID of the user that should be de-assign
let target = "target_example"; // String | The ID of the folder
apiInstance.userToFolderAssignDelete(source, target, (error, data, response) => {
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
 **source** | **String**| The ID of the user that should be de-assign | 
 **target** | **String**| The ID of the folder | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## userToFolderAssignPost

> userToFolderAssignPost(source, target, oldFolder)

Assign a user to a folder

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.UserToFolderAssignApi();
let source = "source_example"; // String | The ID of the user that should be assign
let target = "target_example"; // String | The ID of the folder that should be the parent
let oldFolder = "oldFolder_example"; // String | The ID of the old folder (in case of a drag and drop to a new folder)
apiInstance.userToFolderAssignPost(source, target, oldFolder, (error, data, response) => {
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
 **source** | **String**| The ID of the user that should be assign | 
 **target** | **String**| The ID of the folder that should be the parent | 
 **oldFolder** | **String**| The ID of the old folder (in case of a drag and drop to a new folder) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


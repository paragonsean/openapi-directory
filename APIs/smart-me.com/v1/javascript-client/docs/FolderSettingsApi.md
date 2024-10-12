# SmartMe.FolderSettingsApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folderSettingsDelete**](FolderSettingsApi.md#folderSettingsDelete) | **DELETE** /api/folder/settings/{id} | Deletes a folder
[**folderSettingsGet**](FolderSettingsApi.md#folderSettingsGet) | **GET** /api/folder/settings/{id} | Gets the settings of a folder or meter
[**folderSettingsPost**](FolderSettingsApi.md#folderSettingsPost) | **POST** /api/folder/settings/{id} | Add or edit a folder or a meter. To add a new folder use and empty ID



## folderSettingsDelete

> folderSettingsDelete(id)

Deletes a folder

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FolderSettingsApi();
let id = "id_example"; // String | The ID of the folder
apiInstance.folderSettingsDelete(id, (error, data, response) => {
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
 **id** | **String**| The ID of the folder | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## folderSettingsGet

> FolderSettings folderSettingsGet(id)

Gets the settings of a folder or meter

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FolderSettingsApi();
let id = "id_example"; // String | 
apiInstance.folderSettingsGet(id, (error, data, response) => {
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

[**FolderSettings**](FolderSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## folderSettingsPost

> FolderMenuItem folderSettingsPost(id, folderSettings)

Add or edit a folder or a meter. To add a new folder use and empty ID

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FolderSettingsApi();
let id = "id_example"; // String | The ID of the folder or meter to edit. Use and empty ID to add a new folder
let folderSettings = new SmartMe.FolderSettings(); // FolderSettings | The folder or meter data
apiInstance.folderSettingsPost(id, folderSettings, (error, data, response) => {
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
 **id** | **String**| The ID of the folder or meter to edit. Use and empty ID to add a new folder | 
 **folderSettings** | [**FolderSettings**](FolderSettings.md)| The folder or meter data | 

### Return type

[**FolderMenuItem**](FolderMenuItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


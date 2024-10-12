# SmartMe.FolderMenuApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folderMenuGet**](FolderMenuApi.md#folderMenuGet) | **GET** /api/FolderMenu | Gets the folder menu items (each item might contain child items)
[**folderMenuPost**](FolderMenuApi.md#folderMenuPost) | **POST** /api/FolderMenu | Creates and updates the folder menu items



## folderMenuGet

> FolderMenuConfiguration folderMenuGet(opts)

Gets the folder menu items (each item might contain child items)

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FolderMenuApi();
let opts = {
  'filter': "filter_example" // String | (optional) Filter for the folders and meters:               all: load everything              assigned: load only folders and meters that are assigend to a folder              unassigend: load only meters that are not assigend to a folder              user: load only folder and all users assigned to this folders              subuserlist: load all subusers as a list
};
apiInstance.folderMenuGet(opts, (error, data, response) => {
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
 **filter** | **String**| (optional) Filter for the folders and meters:               all: load everything              assigned: load only folders and meters that are assigend to a folder              unassigend: load only meters that are not assigend to a folder              user: load only folder and all users assigned to this folders              subuserlist: load all subusers as a list | [optional] 

### Return type

[**FolderMenuConfiguration**](FolderMenuConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## folderMenuPost

> folderMenuPost(folderMenuConfiguration)

Creates and updates the folder menu items

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FolderMenuApi();
let folderMenuConfiguration = new SmartMe.FolderMenuConfiguration(); // FolderMenuConfiguration | 
apiInstance.folderMenuPost(folderMenuConfiguration, (error, data, response) => {
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
 **folderMenuConfiguration** | [**FolderMenuConfiguration**](FolderMenuConfiguration.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined


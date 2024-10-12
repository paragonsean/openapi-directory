# JellyfinApi.EnvironmentApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDefaultDirectoryBrowser**](EnvironmentApi.md#getDefaultDirectoryBrowser) | **GET** /Environment/DefaultDirectoryBrowser | Get Default directory browser.
[**getDirectoryContents**](EnvironmentApi.md#getDirectoryContents) | **GET** /Environment/DirectoryContents | Gets the contents of a given directory in the file system.
[**getDrives**](EnvironmentApi.md#getDrives) | **GET** /Environment/Drives | Gets available drives from the server&#39;s file system.
[**getNetworkShares**](EnvironmentApi.md#getNetworkShares) | **GET** /Environment/NetworkShares | Gets network paths.
[**getParentPath**](EnvironmentApi.md#getParentPath) | **GET** /Environment/ParentPath | Gets the parent path of a given path.
[**validatePath**](EnvironmentApi.md#validatePath) | **POST** /Environment/ValidatePath | Validates path.



## getDefaultDirectoryBrowser

> DefaultDirectoryBrowserInfoDto getDefaultDirectoryBrowser()

Get Default directory browser.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.EnvironmentApi();
apiInstance.getDefaultDirectoryBrowser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DefaultDirectoryBrowserInfoDto**](DefaultDirectoryBrowserInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getDirectoryContents

> [FileSystemEntryInfo] getDirectoryContents(path, opts)

Gets the contents of a given directory in the file system.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.EnvironmentApi();
let path = "path_example"; // String | The path.
let opts = {
  'includeFiles': false, // Boolean | An optional filter to include or exclude files from the results. true/false.
  'includeDirectories': false // Boolean | An optional filter to include or exclude folders from the results. true/false.
};
apiInstance.getDirectoryContents(path, opts, (error, data, response) => {
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
 **path** | **String**| The path. | 
 **includeFiles** | **Boolean**| An optional filter to include or exclude files from the results. true/false. | [optional] [default to false]
 **includeDirectories** | **Boolean**| An optional filter to include or exclude folders from the results. true/false. | [optional] [default to false]

### Return type

[**[FileSystemEntryInfo]**](FileSystemEntryInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getDrives

> [FileSystemEntryInfo] getDrives()

Gets available drives from the server&#39;s file system.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.EnvironmentApi();
apiInstance.getDrives((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[FileSystemEntryInfo]**](FileSystemEntryInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getNetworkShares

> [FileSystemEntryInfo] getNetworkShares()

Gets network paths.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.EnvironmentApi();
apiInstance.getNetworkShares((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[FileSystemEntryInfo]**](FileSystemEntryInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getParentPath

> String getParentPath(path)

Gets the parent path of a given path.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.EnvironmentApi();
let path = "path_example"; // String | The path.
apiInstance.getParentPath(path, (error, data, response) => {
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
 **path** | **String**| The path. | 

### Return type

**String**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## validatePath

> validatePath(validatePathDto)

Validates path.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.EnvironmentApi();
let validatePathDto = new JellyfinApi.ValidatePathDto(); // ValidatePathDto | Validate request object.
apiInstance.validatePath(validatePathDto, (error, data, response) => {
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
 **validatePathDto** | [**ValidatePathDto**](ValidatePathDto.md)| Validate request object. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


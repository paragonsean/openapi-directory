# NetlifysApiDocumentation.FileApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSiteFileByPathName**](FileApi.md#getSiteFileByPathName) | **GET** /sites/{site_id}/files/{file_path} | 
[**listSiteFiles**](FileApi.md#listSiteFiles) | **GET** /sites/{site_id}/files | 
[**uploadDeployFile**](FileApi.md#uploadDeployFile) | **PUT** /deploys/{deploy_id}/files/{path} | 



## getSiteFileByPathName

> File getSiteFileByPathName(siteId, filePath)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.FileApi();
let siteId = "siteId_example"; // String | 
let filePath = "filePath_example"; // String | 
apiInstance.getSiteFileByPathName(siteId, filePath, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **filePath** | **String**|  | 

### Return type

**File**

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSiteFiles

> [File] listSiteFiles(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.FileApi();
let siteId = "siteId_example"; // String | 
apiInstance.listSiteFiles(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

**[File]**

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadDeployFile

> File uploadDeployFile(deployId, path, fileBody, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.FileApi();
let deployId = "deployId_example"; // String | 
let path = "path_example"; // String | 
let fileBody = "/path/to/file"; // File | 
let opts = {
  'size': 56 // Number | 
};
apiInstance.uploadDeployFile(deployId, path, fileBody, opts, (error, data, response) => {
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
 **deployId** | **String**|  | 
 **path** | **String**|  | 
 **fileBody** | **File**|  | 
 **size** | **Number**|  | [optional] 

### Return type

**File**

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


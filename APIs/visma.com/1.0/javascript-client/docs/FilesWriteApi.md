# SeveraPublicRestApiDocumentation.FilesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywordsLinkKeywordToFile**](FilesWriteApi.md#keywordsLinkKeywordToFile) | **POST** /v1/files/{fileGuid}/keywords/{guid} | Link existing keyword to file



## keywordsLinkKeywordToFile

> FileKeywordModel keywordsLinkKeywordToFile(fileGuid, guid)

Link existing keyword to file

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.FilesWriteApi();
let fileGuid = "fileGuid_example"; // String | 
let guid = "guid_example"; // String | 
apiInstance.keywordsLinkKeywordToFile(fileGuid, guid, (error, data, response) => {
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
 **fileGuid** | **String**|  | 
 **guid** | **String**|  | 

### Return type

[**FileKeywordModel**](FileKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


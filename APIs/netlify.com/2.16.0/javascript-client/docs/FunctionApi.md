# NetlifysApiDocumentation.FunctionApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uploadDeployFunction**](FunctionApi.md#uploadDeployFunction) | **PUT** /deploys/{deploy_id}/functions/{name} | 



## uploadDeployFunction

> Function uploadDeployFunction(deployId, name, fileBody, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.FunctionApi();
let deployId = "deployId_example"; // String | 
let name = "name_example"; // String | 
let fileBody = "/path/to/file"; // File | 
let opts = {
  'runtime': "runtime_example", // String | 
  'size': 56, // Number | 
  'xNfRetryCount': 56 // Number | 
};
apiInstance.uploadDeployFunction(deployId, name, fileBody, opts, (error, data, response) => {
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
 **name** | **String**|  | 
 **fileBody** | **File**|  | 
 **runtime** | **String**|  | [optional] 
 **size** | **Number**|  | [optional] 
 **xNfRetryCount** | **Number**|  | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


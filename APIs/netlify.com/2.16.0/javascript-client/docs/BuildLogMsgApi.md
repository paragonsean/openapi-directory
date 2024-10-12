# NetlifysApiDocumentation.BuildLogMsgApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateSiteBuildLog**](BuildLogMsgApi.md#updateSiteBuildLog) | **POST** /builds/{build_id}/log | 



## updateSiteBuildLog

> updateSiteBuildLog(buildId, msg)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.BuildLogMsgApi();
let buildId = "buildId_example"; // String | 
let msg = new NetlifysApiDocumentation.BuildLogMsg(); // BuildLogMsg | 
apiInstance.updateSiteBuildLog(buildId, msg, (error, data, response) => {
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
 **buildId** | **String**|  | 
 **msg** | [**BuildLogMsg**](BuildLogMsg.md)|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


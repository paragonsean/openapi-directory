# NetlifysApiDocumentation.DeployedBranchApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listSiteDeployedBranches**](DeployedBranchApi.md#listSiteDeployedBranches) | **GET** /sites/{site_id}/deployed-branches | 



## listSiteDeployedBranches

> [DeployedBranch] listSiteDeployedBranches(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.DeployedBranchApi();
let siteId = "siteId_example"; // String | 
apiInstance.listSiteDeployedBranches(siteId, (error, data, response) => {
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

[**[DeployedBranch]**](DeployedBranch.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


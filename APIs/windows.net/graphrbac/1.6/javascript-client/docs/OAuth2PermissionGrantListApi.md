# GraphRbacManagementClient.OAuth2PermissionGrantListApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oAuth2PermissionGrantList**](OAuth2PermissionGrantListApi.md#oAuth2PermissionGrantList) | **GET** /{tenantID}/oauth2PermissionGrants | 



## oAuth2PermissionGrantList

> OAuth2PermissionGrantListResult oAuth2PermissionGrantList(apiVersion, tenantID, opts)



Queries OAuth2 permissions grants for the relevant SP ObjectId of an app.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.OAuth2PermissionGrantListApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let opts = {
  'filter': "clientId+eq+'61ed44c3-5a1d-4639-a215-07f25129c6c3" // String | This is the Service Principal ObjectId associated with the app
};
apiInstance.oAuth2PermissionGrantList(apiVersion, tenantID, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **filter** | **String**| This is the Service Principal ObjectId associated with the app | [optional] 

### Return type

[**OAuth2PermissionGrantListResult**](OAuth2PermissionGrantListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


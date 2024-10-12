# GraphRbacManagementClient.OAuth2PermissionGrantCreateApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oAuth2PermissionGrantCreate**](OAuth2PermissionGrantCreateApi.md#oAuth2PermissionGrantCreate) | **POST** /{tenantID}/oauth2PermissionGrants | 



## oAuth2PermissionGrantCreate

> OAuth2PermissionGrant oAuth2PermissionGrantCreate(apiVersion, tenantID, opts)



Grants OAuth2 permissions for the relevant resource Ids of an app.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.OAuth2PermissionGrantCreateApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let opts = {
  'oAuth2PermissionGrant': new GraphRbacManagementClient.OAuth2PermissionGrant() // OAuth2PermissionGrant | The relevant app Service Principal Object Id and the Service Principal Object Id you want to grant.
};
apiInstance.oAuth2PermissionGrantCreate(apiVersion, tenantID, opts, (error, data, response) => {
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
 **oAuth2PermissionGrant** | [**OAuth2PermissionGrant**](OAuth2PermissionGrant.md)| The relevant app Service Principal Object Id and the Service Principal Object Id you want to grant. | [optional] 

### Return type

[**OAuth2PermissionGrant**](OAuth2PermissionGrant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


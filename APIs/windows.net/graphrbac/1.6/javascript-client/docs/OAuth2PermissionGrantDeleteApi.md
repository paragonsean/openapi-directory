# GraphRbacManagementClient.OAuth2PermissionGrantDeleteApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oAuth2PermissionGrantDelete**](OAuth2PermissionGrantDeleteApi.md#oAuth2PermissionGrantDelete) | **DELETE** /{tenantID}/oauth2PermissionGrants/{objectId} | 



## oAuth2PermissionGrantDelete

> oAuth2PermissionGrantDelete(objectId, apiVersion, tenantID)



Delete a OAuth2 permission grant for the relevant resource Ids of an app.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.OAuth2PermissionGrantDeleteApi();
let objectId = "objectId_example"; // String | The object ID of a permission grant.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.oAuth2PermissionGrantDelete(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of a permission grant. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


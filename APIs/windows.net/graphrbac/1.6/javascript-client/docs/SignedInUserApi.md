# GraphRbacManagementClient.SignedInUserApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signedInUserGet**](SignedInUserApi.md#signedInUserGet) | **GET** /{tenantID}/me | 
[**signedInUserListOwnedObjects**](SignedInUserApi.md#signedInUserListOwnedObjects) | **GET** /{tenantID}/me/ownedObjects | 



## signedInUserGet

> User signedInUserGet(apiVersion, tenantID)



Gets the details for the currently logged-in user.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.SignedInUserApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.signedInUserGet(apiVersion, tenantID, (error, data, response) => {
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

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## signedInUserListOwnedObjects

> DirectoryObjectListResult signedInUserListOwnedObjects(apiVersion, tenantID)



Get the list of directory objects that are owned by the user.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.SignedInUserApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.signedInUserListOwnedObjects(apiVersion, tenantID, (error, data, response) => {
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

### Return type

[**DirectoryObjectListResult**](DirectoryObjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


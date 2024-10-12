# GraphRbacManagementClient.GroupOwnersApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsListOwners**](GroupOwnersApi.md#groupsListOwners) | **GET** /{tenantID}/groups/{objectId}/owners | Directory objects that are owners of the group.



## groupsListOwners

> DirectoryObjectListResult groupsListOwners(objectId, apiVersion, tenantID)

Directory objects that are owners of the group.

The owners are a set of non-admin users who are allowed to modify this object.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupOwnersApi();
let objectId = "objectId_example"; // String | The object ID of the group for which to get owners.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.groupsListOwners(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the group for which to get owners. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**DirectoryObjectListResult**](DirectoryObjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


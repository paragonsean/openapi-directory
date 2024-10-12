# GraphRbacManagementClient.GroupsOwnersApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsAddOwner**](GroupsOwnersApi.md#groupsAddOwner) | **POST** /{tenantID}/groups/{objectId}/$links/owners | 
[**groupsRemoveOwner**](GroupsOwnersApi.md#groupsRemoveOwner) | **DELETE** /{tenantID}/groups/{objectId}/$links/owners/{ownerObjectId} | 



## groupsAddOwner

> groupsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters)



Add an owner to a group.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupsOwnersApi();
let objectId = "objectId_example"; // String | The object ID of the application to which to add the owner.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let addOwnerParameters = new GraphRbacManagementClient.AddOwnerParameters(); // AddOwnerParameters | The URL of the owner object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
apiInstance.groupsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the application to which to add the owner. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **addOwnerParameters** | [**AddOwnerParameters**](AddOwnerParameters.md)| The URL of the owner object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## groupsRemoveOwner

> groupsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID)



Remove a member from owners.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.GroupsOwnersApi();
let objectId = "objectId_example"; // String | The object ID of the group from which to remove the owner.
let ownerObjectId = "ownerObjectId_example"; // String | Owner object id
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.groupsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the group from which to remove the owner. | 
 **ownerObjectId** | **String**| Owner object id | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


# GraphRbacManagementClient.ServicePrincipalOwnersApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicePrincipalsAddOwner**](ServicePrincipalOwnersApi.md#servicePrincipalsAddOwner) | **POST** /{tenantID}/servicePrincipals/{objectId}/$links/owners | 
[**servicePrincipalsListOwners**](ServicePrincipalOwnersApi.md#servicePrincipalsListOwners) | **GET** /{tenantID}/servicePrincipals/{objectId}/owners | Directory objects that are owners of this service principal.
[**servicePrincipalsRemoveOwner**](ServicePrincipalOwnersApi.md#servicePrincipalsRemoveOwner) | **DELETE** /{tenantID}/servicePrincipals/{objectId}/$links/owners/{ownerObjectId} | 



## servicePrincipalsAddOwner

> servicePrincipalsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters)



Add an owner to a service principal.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalOwnersApi();
let objectId = "objectId_example"; // String | The object ID of the service principal to which to add the owner.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let addOwnerParameters = new GraphRbacManagementClient.AddOwnerParameters(); // AddOwnerParameters | The URL of the owner object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
apiInstance.servicePrincipalsAddOwner(objectId, apiVersion, tenantID, addOwnerParameters, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal to which to add the owner. | 
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


## servicePrincipalsListOwners

> DirectoryObjectListResult servicePrincipalsListOwners(objectId, apiVersion, tenantID)

Directory objects that are owners of this service principal.

The owners are a set of non-admin users who are allowed to modify this object.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalOwnersApi();
let objectId = "objectId_example"; // String | The object ID of the service principal for which to get owners.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsListOwners(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal for which to get owners. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**DirectoryObjectListResult**](DirectoryObjectListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## servicePrincipalsRemoveOwner

> servicePrincipalsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID)



Remove a member from owners.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalOwnersApi();
let objectId = "objectId_example"; // String | The object ID of the service principal from which to remove the owner.
let ownerObjectId = "ownerObjectId_example"; // String | Owner object id
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsRemoveOwner(objectId, ownerObjectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal from which to remove the owner. | 
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


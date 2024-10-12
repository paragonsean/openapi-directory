# GraphRbacManagementClient.ServicePrincipalAppRoleAssignedToApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicePrincipalsListAppRoleAssignedTo**](ServicePrincipalAppRoleAssignedToApi.md#servicePrincipalsListAppRoleAssignedTo) | **GET** /{tenantID}/servicePrincipals/{objectId}/appRoleAssignedTo | Principals (users, groups, and service principals) that are assigned to this service principal.



## servicePrincipalsListAppRoleAssignedTo

> AppRoleAssignmentListResult servicePrincipalsListAppRoleAssignedTo(objectId, apiVersion, tenantID)

Principals (users, groups, and service principals) that are assigned to this service principal.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalAppRoleAssignedToApi();
let objectId = "objectId_example"; // String | The object ID of the service principal for which to get owners.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsListAppRoleAssignedTo(objectId, apiVersion, tenantID, (error, data, response) => {
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

[**AppRoleAssignmentListResult**](AppRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


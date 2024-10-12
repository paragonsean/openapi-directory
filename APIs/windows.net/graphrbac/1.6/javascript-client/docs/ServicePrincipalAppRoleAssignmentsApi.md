# GraphRbacManagementClient.ServicePrincipalAppRoleAssignmentsApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicePrincipalsListAppRoleAssignments**](ServicePrincipalAppRoleAssignmentsApi.md#servicePrincipalsListAppRoleAssignments) | **GET** /{tenantID}/servicePrincipals/{objectId}/appRoleAssignments | Applications that the service principal is assigned to.



## servicePrincipalsListAppRoleAssignments

> AppRoleAssignmentListResult servicePrincipalsListAppRoleAssignments(objectId, apiVersion, tenantID)

Applications that the service principal is assigned to.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalAppRoleAssignmentsApi();
let objectId = "objectId_example"; // String | The object ID of the service principal for which to get owners.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsListAppRoleAssignments(objectId, apiVersion, tenantID, (error, data, response) => {
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


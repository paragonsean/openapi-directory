# GraphRbacManagementClient.ServicePrincipalPasswordCredentialsApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicePrincipalsListPasswordCredentials**](ServicePrincipalPasswordCredentialsApi.md#servicePrincipalsListPasswordCredentials) | **GET** /{tenantID}/servicePrincipals/{objectId}/passwordCredentials | 
[**servicePrincipalsUpdatePasswordCredentials**](ServicePrincipalPasswordCredentialsApi.md#servicePrincipalsUpdatePasswordCredentials) | **PATCH** /{tenantID}/servicePrincipals/{objectId}/passwordCredentials | 



## servicePrincipalsListPasswordCredentials

> PasswordCredentialListResult servicePrincipalsListPasswordCredentials(objectId, apiVersion, tenantID)



Gets the passwordCredentials associated with a service principal.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalPasswordCredentialsApi();
let objectId = "objectId_example"; // String | The object ID of the service principal.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsListPasswordCredentials(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**PasswordCredentialListResult**](PasswordCredentialListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## servicePrincipalsUpdatePasswordCredentials

> servicePrincipalsUpdatePasswordCredentials(objectId, apiVersion, tenantID, passwordCredentialsUpdateParameters)



Updates the passwordCredentials associated with a service principal.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalPasswordCredentialsApi();
let objectId = "objectId_example"; // String | The object ID of the service principal.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let passwordCredentialsUpdateParameters = new GraphRbacManagementClient.PasswordCredentialsUpdateParameters(); // PasswordCredentialsUpdateParameters | Parameters to update the passwordCredentials of an existing service principal.
apiInstance.servicePrincipalsUpdatePasswordCredentials(objectId, apiVersion, tenantID, passwordCredentialsUpdateParameters, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **passwordCredentialsUpdateParameters** | [**PasswordCredentialsUpdateParameters**](PasswordCredentialsUpdateParameters.md)| Parameters to update the passwordCredentials of an existing service principal. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


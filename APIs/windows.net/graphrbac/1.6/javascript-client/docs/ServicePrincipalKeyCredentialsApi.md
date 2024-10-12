# GraphRbacManagementClient.ServicePrincipalKeyCredentialsApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicePrincipalsListKeyCredentials**](ServicePrincipalKeyCredentialsApi.md#servicePrincipalsListKeyCredentials) | **GET** /{tenantID}/servicePrincipals/{objectId}/keyCredentials | 
[**servicePrincipalsUpdateKeyCredentials**](ServicePrincipalKeyCredentialsApi.md#servicePrincipalsUpdateKeyCredentials) | **PATCH** /{tenantID}/servicePrincipals/{objectId}/keyCredentials | 



## servicePrincipalsListKeyCredentials

> KeyCredentialListResult servicePrincipalsListKeyCredentials(objectId, apiVersion, tenantID)



Get the keyCredentials associated with the specified service principal.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalKeyCredentialsApi();
let objectId = "objectId_example"; // String | The object ID of the service principal for which to get keyCredentials.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsListKeyCredentials(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal for which to get keyCredentials. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**KeyCredentialListResult**](KeyCredentialListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## servicePrincipalsUpdateKeyCredentials

> servicePrincipalsUpdateKeyCredentials(objectId, apiVersion, tenantID, keyCredentialsUpdateParameters)



Update the keyCredentials associated with a service principal.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalKeyCredentialsApi();
let objectId = "objectId_example"; // String | The object ID for which to get service principal information.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let keyCredentialsUpdateParameters = new GraphRbacManagementClient.KeyCredentialsUpdateParameters(); // KeyCredentialsUpdateParameters | Parameters to update the keyCredentials of an existing service principal.
apiInstance.servicePrincipalsUpdateKeyCredentials(objectId, apiVersion, tenantID, keyCredentialsUpdateParameters, (error, data, response) => {
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
 **objectId** | **String**| The object ID for which to get service principal information. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **keyCredentialsUpdateParameters** | [**KeyCredentialsUpdateParameters**](KeyCredentialsUpdateParameters.md)| Parameters to update the keyCredentials of an existing service principal. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


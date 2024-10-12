# GraphRbacManagementClient.ApplicationPasswordCredentialsApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationsListPasswordCredentials**](ApplicationPasswordCredentialsApi.md#applicationsListPasswordCredentials) | **GET** /{tenantID}/applications/{applicationObjectId}/passwordCredentials | 
[**applicationsUpdatePasswordCredentials**](ApplicationPasswordCredentialsApi.md#applicationsUpdatePasswordCredentials) | **PATCH** /{tenantID}/applications/{applicationObjectId}/passwordCredentials | 



## applicationsListPasswordCredentials

> PasswordCredentialListResult applicationsListPasswordCredentials(applicationObjectId, apiVersion, tenantID)



Get the passwordCredentials associated with an application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationPasswordCredentialsApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.applicationsListPasswordCredentials(applicationObjectId, apiVersion, tenantID, (error, data, response) => {
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
 **applicationObjectId** | **String**| Application object ID. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**PasswordCredentialListResult**](PasswordCredentialListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationsUpdatePasswordCredentials

> applicationsUpdatePasswordCredentials(applicationObjectId, apiVersion, tenantID, passwordCredentialsUpdateParameters)



Update passwordCredentials associated with an application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationPasswordCredentialsApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let passwordCredentialsUpdateParameters = new GraphRbacManagementClient.PasswordCredentialsUpdateParameters(); // PasswordCredentialsUpdateParameters | Parameters to update passwordCredentials of an existing application.
apiInstance.applicationsUpdatePasswordCredentials(applicationObjectId, apiVersion, tenantID, passwordCredentialsUpdateParameters, (error, data, response) => {
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
 **applicationObjectId** | **String**| Application object ID. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **passwordCredentialsUpdateParameters** | [**PasswordCredentialsUpdateParameters**](PasswordCredentialsUpdateParameters.md)| Parameters to update passwordCredentials of an existing application. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


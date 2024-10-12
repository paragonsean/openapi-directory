# GraphRbacManagementClient.ApplicationKeyCredentialsApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationsListKeyCredentials**](ApplicationKeyCredentialsApi.md#applicationsListKeyCredentials) | **GET** /{tenantID}/applications/{applicationObjectId}/keyCredentials | 
[**applicationsUpdateKeyCredentials**](ApplicationKeyCredentialsApi.md#applicationsUpdateKeyCredentials) | **PATCH** /{tenantID}/applications/{applicationObjectId}/keyCredentials | 



## applicationsListKeyCredentials

> KeyCredentialListResult applicationsListKeyCredentials(applicationObjectId, apiVersion, tenantID)



Get the keyCredentials associated with an application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationKeyCredentialsApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.applicationsListKeyCredentials(applicationObjectId, apiVersion, tenantID, (error, data, response) => {
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

[**KeyCredentialListResult**](KeyCredentialListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationsUpdateKeyCredentials

> applicationsUpdateKeyCredentials(applicationObjectId, apiVersion, tenantID, keyCredentialsUpdateParameters)



Update the keyCredentials associated with an application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationKeyCredentialsApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let keyCredentialsUpdateParameters = new GraphRbacManagementClient.KeyCredentialsUpdateParameters(); // KeyCredentialsUpdateParameters | Parameters to update the keyCredentials of an existing application.
apiInstance.applicationsUpdateKeyCredentials(applicationObjectId, apiVersion, tenantID, keyCredentialsUpdateParameters, (error, data, response) => {
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
 **keyCredentialsUpdateParameters** | [**KeyCredentialsUpdateParameters**](KeyCredentialsUpdateParameters.md)| Parameters to update the keyCredentials of an existing application. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


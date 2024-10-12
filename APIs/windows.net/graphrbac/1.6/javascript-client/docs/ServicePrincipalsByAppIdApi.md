# GraphRbacManagementClient.ServicePrincipalsByAppIdApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationsGetServicePrincipalsIdByAppId**](ServicePrincipalsByAppIdApi.md#applicationsGetServicePrincipalsIdByAppId) | **GET** /{tenantID}/servicePrincipalsByAppId/{applicationID}/objectId | 



## applicationsGetServicePrincipalsIdByAppId

> ServicePrincipalObjectResult applicationsGetServicePrincipalsIdByAppId(apiVersion, tenantID, applicationID)



Gets an object id for a given application id from the current tenant.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalsByAppIdApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let applicationID = "applicationID_example"; // String | The application ID.
apiInstance.applicationsGetServicePrincipalsIdByAppId(apiVersion, tenantID, applicationID, (error, data, response) => {
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
 **applicationID** | **String**| The application ID. | 

### Return type

[**ServicePrincipalObjectResult**](ServicePrincipalObjectResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


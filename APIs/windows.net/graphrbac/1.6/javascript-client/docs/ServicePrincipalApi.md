# GraphRbacManagementClient.ServicePrincipalApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicePrincipalsCreate**](ServicePrincipalApi.md#servicePrincipalsCreate) | **POST** /{tenantID}/servicePrincipals | 
[**servicePrincipalsDelete**](ServicePrincipalApi.md#servicePrincipalsDelete) | **DELETE** /{tenantID}/servicePrincipals/{objectId} | 
[**servicePrincipalsGet**](ServicePrincipalApi.md#servicePrincipalsGet) | **GET** /{tenantID}/servicePrincipals/{objectId} | 
[**servicePrincipalsList**](ServicePrincipalApi.md#servicePrincipalsList) | **GET** /{tenantID}/servicePrincipals | 
[**servicePrincipalsUpdate**](ServicePrincipalApi.md#servicePrincipalsUpdate) | **PATCH** /{tenantID}/servicePrincipals/{objectId} | 



## servicePrincipalsCreate

> ServicePrincipal servicePrincipalsCreate(apiVersion, tenantID, servicePrincipalCreateParameters)



Creates a service principal in the directory.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let servicePrincipalCreateParameters = new GraphRbacManagementClient.ServicePrincipalCreateParameters(); // ServicePrincipalCreateParameters | Parameters to create a service principal.
apiInstance.servicePrincipalsCreate(apiVersion, tenantID, servicePrincipalCreateParameters, (error, data, response) => {
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
 **servicePrincipalCreateParameters** | [**ServicePrincipalCreateParameters**](ServicePrincipalCreateParameters.md)| Parameters to create a service principal. | 

### Return type

[**ServicePrincipal**](ServicePrincipal.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## servicePrincipalsDelete

> servicePrincipalsDelete(objectId, apiVersion, tenantID)



Deletes a service principal from the directory.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalApi();
let objectId = "objectId_example"; // String | The object ID of the service principal to delete.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsDelete(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal to delete. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## servicePrincipalsGet

> ServicePrincipal servicePrincipalsGet(objectId, apiVersion, tenantID)



Gets service principal information from the directory. Query by objectId or pass a filter to query by appId

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalApi();
let objectId = "objectId_example"; // String | The object ID of the service principal to get.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.servicePrincipalsGet(objectId, apiVersion, tenantID, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal to get. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 

### Return type

[**ServicePrincipal**](ServicePrincipal.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## servicePrincipalsList

> ServicePrincipalListResult servicePrincipalsList(apiVersion, tenantID, opts)



Gets a list of service principals from the current tenant.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let opts = {
  'filter': "filter_example" // String | The filter to apply to the operation.
};
apiInstance.servicePrincipalsList(apiVersion, tenantID, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply to the operation. | [optional] 

### Return type

[**ServicePrincipalListResult**](ServicePrincipalListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## servicePrincipalsUpdate

> servicePrincipalsUpdate(objectId, apiVersion, tenantID, servicePrincipalUpdateParameters)



Updates a service principal in the directory.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ServicePrincipalApi();
let objectId = "objectId_example"; // String | The object ID of the service principal to delete.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let servicePrincipalUpdateParameters = new GraphRbacManagementClient.ServicePrincipalUpdateParameters(); // ServicePrincipalUpdateParameters | Parameters to update a service principal.
apiInstance.servicePrincipalsUpdate(objectId, apiVersion, tenantID, servicePrincipalUpdateParameters, (error, data, response) => {
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
 **objectId** | **String**| The object ID of the service principal to delete. | 
 **apiVersion** | **String**| Client API version. | 
 **tenantID** | **String**| The tenant ID. | 
 **servicePrincipalUpdateParameters** | [**ServicePrincipalUpdateParameters**](ServicePrincipalUpdateParameters.md)| Parameters to update a service principal. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


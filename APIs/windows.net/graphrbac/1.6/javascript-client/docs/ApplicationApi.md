# GraphRbacManagementClient.ApplicationApi

All URIs are relative to *https://graph.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationsCreate**](ApplicationApi.md#applicationsCreate) | **POST** /{tenantID}/applications | 
[**applicationsDelete**](ApplicationApi.md#applicationsDelete) | **DELETE** /{tenantID}/applications/{applicationObjectId} | 
[**applicationsGet**](ApplicationApi.md#applicationsGet) | **GET** /{tenantID}/applications/{applicationObjectId} | 
[**applicationsList**](ApplicationApi.md#applicationsList) | **GET** /{tenantID}/applications | 
[**applicationsPatch**](ApplicationApi.md#applicationsPatch) | **PATCH** /{tenantID}/applications/{applicationObjectId} | 
[**deletedApplicationsHardDelete**](ApplicationApi.md#deletedApplicationsHardDelete) | **DELETE** /{tenantID}/deletedApplications/{applicationObjectId} | 



## applicationsCreate

> Application applicationsCreate(apiVersion, tenantID, applicationCreateParameters)



Create a new application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let applicationCreateParameters = new GraphRbacManagementClient.ApplicationCreateParameters(); // ApplicationCreateParameters | The parameters for creating an application.
apiInstance.applicationsCreate(apiVersion, tenantID, applicationCreateParameters, (error, data, response) => {
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
 **applicationCreateParameters** | [**ApplicationCreateParameters**](ApplicationCreateParameters.md)| The parameters for creating an application. | 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## applicationsDelete

> applicationsDelete(applicationObjectId, apiVersion, tenantID)



Delete an application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.applicationsDelete(applicationObjectId, apiVersion, tenantID, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationsGet

> Application applicationsGet(applicationObjectId, apiVersion, tenantID)



Get an application by object ID.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.applicationsGet(applicationObjectId, apiVersion, tenantID, (error, data, response) => {
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

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationsList

> ApplicationListResult applicationsList(apiVersion, tenantID, opts)



Lists applications by filter parameters.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let opts = {
  'filter': "filter_example" // String | The filters to apply to the operation.
};
apiInstance.applicationsList(apiVersion, tenantID, opts, (error, data, response) => {
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
 **filter** | **String**| The filters to apply to the operation. | [optional] 

### Return type

[**ApplicationListResult**](ApplicationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationsPatch

> applicationsPatch(applicationObjectId, apiVersion, tenantID, applicationUpdateParameters)



Update an existing application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
let applicationUpdateParameters = new GraphRbacManagementClient.ApplicationUpdateParameters(); // ApplicationUpdateParameters | Parameters to update an existing application.
apiInstance.applicationsPatch(applicationObjectId, apiVersion, tenantID, applicationUpdateParameters, (error, data, response) => {
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
 **applicationUpdateParameters** | [**ApplicationUpdateParameters**](ApplicationUpdateParameters.md)| Parameters to update an existing application. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## deletedApplicationsHardDelete

> deletedApplicationsHardDelete(applicationObjectId, apiVersion, tenantID)



Hard-delete an application.

### Example

```javascript
import GraphRbacManagementClient from 'graph_rbac_management_client';
let defaultClient = GraphRbacManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GraphRbacManagementClient.ApplicationApi();
let applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let tenantID = "tenantID_example"; // String | The tenant ID.
apiInstance.deletedApplicationsHardDelete(applicationObjectId, apiVersion, tenantID, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


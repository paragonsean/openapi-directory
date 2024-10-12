# DeploymentAdminClient.FileContainersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileContainersCreate**](FileContainersApi.md#fileContainersCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{fileContainerId} | 
[**fileContainersDelete**](FileContainersApi.md#fileContainersDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{fileContainerId} | Deletes specified file container.
[**fileContainersGet**](FileContainersApi.md#fileContainersGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers/{fileContainerId} | 
[**fileContainersList**](FileContainersApi.md#fileContainersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/fileContainers | 



## fileContainersCreate

> FileContainer fileContainersCreate(subscriptionId, apiVersion, fileContainerId, fileContainerParameters)



Creates a new file container.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.FileContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
let fileContainerId = "fileContainerId_example"; // String | The file container identifier.
let fileContainerParameters = new DeploymentAdminClient.FileContainerParameters(); // FileContainerParameters | The parameters required to create a new file container.
apiInstance.fileContainersCreate(subscriptionId, apiVersion, fileContainerId, fileContainerParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]
 **fileContainerId** | **String**| The file container identifier. | 
 **fileContainerParameters** | [**FileContainerParameters**](FileContainerParameters.md)| The parameters required to create a new file container. | 

### Return type

[**FileContainer**](FileContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fileContainersDelete

> fileContainersDelete(subscriptionId, fileContainerId, apiVersion)

Deletes specified file container.

Delete an existing file container.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.FileContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let fileContainerId = "fileContainerId_example"; // String | The file container identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.fileContainersDelete(subscriptionId, fileContainerId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **fileContainerId** | **String**| The file container identifier. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fileContainersGet

> FileContainer fileContainersGet(subscriptionId, fileContainerId, apiVersion)



Retrieves the specific file container details.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.FileContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let fileContainerId = "fileContainerId_example"; // String | The file container identifier.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.fileContainersGet(subscriptionId, fileContainerId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **fileContainerId** | **String**| The file container identifier. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

[**FileContainer**](FileContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileContainersList

> FileContainersList fileContainersList(subscriptionId, apiVersion)



Returns an array of file containers.

### Example

```javascript
import DeploymentAdminClient from 'deployment_admin_client';
let defaultClient = DeploymentAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentAdminClient.FileContainersApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "'2019-01-01'"; // String | Client API Version.
apiInstance.fileContainersList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-01-01&#39;]

### Return type

[**FileContainersList**](FileContainersList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


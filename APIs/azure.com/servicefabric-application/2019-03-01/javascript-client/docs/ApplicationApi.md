# ServiceFabricManagementClient.ApplicationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationsCreateOrUpdate**](ApplicationApi.md#applicationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Creates or updates a Service Fabric application resource.
[**applicationsDelete**](ApplicationApi.md#applicationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Deletes a Service Fabric application resource.
[**applicationsGet**](ApplicationApi.md#applicationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Gets a Service Fabric application resource.
[**applicationsList**](ApplicationApi.md#applicationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications | Gets the list of application resources created in the specified Service Fabric cluster resource.
[**applicationsUpdate**](ApplicationApi.md#applicationsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Updates a Service Fabric application resource.



## applicationsCreateOrUpdate

> ApplicationResource applicationsCreateOrUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters)

Creates or updates a Service Fabric application resource.

Create or update a Service Fabric application resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let parameters = new ServiceFabricManagementClient.ApplicationResource(); // ApplicationResource | The application resource.
apiInstance.applicationsCreateOrUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationName** | **String**| The name of the application resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **parameters** | [**ApplicationResource**](ApplicationResource.md)| The application resource. | 

### Return type

[**ApplicationResource**](ApplicationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationsDelete

> applicationsDelete(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion)

Deletes a Service Fabric application resource.

Delete a Service Fabric application resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
apiInstance.applicationsDelete(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationName** | **String**| The name of the application resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsGet

> ApplicationResource applicationsGet(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion)

Gets a Service Fabric application resource.

Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
apiInstance.applicationsGet(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationName** | **String**| The name of the application resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]

### Return type

[**ApplicationResource**](ApplicationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsList

> ApplicationResourceList applicationsList(subscriptionId, resourceGroupName, clusterName, apiVersion)

Gets the list of application resources created in the specified Service Fabric cluster resource.

Gets all application resources created or in the process of being created in the Service Fabric cluster resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
apiInstance.applicationsList(subscriptionId, resourceGroupName, clusterName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]

### Return type

[**ApplicationResourceList**](ApplicationResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsUpdate

> ApplicationResource applicationsUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters)

Updates a Service Fabric application resource.

Update a Service Fabric application resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let parameters = new ServiceFabricManagementClient.ApplicationResourceUpdate(); // ApplicationResourceUpdate | The application resource for patch operations.
apiInstance.applicationsUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationName** | **String**| The name of the application resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **parameters** | [**ApplicationResourceUpdate**](ApplicationResourceUpdate.md)| The application resource for patch operations. | 

### Return type

[**ApplicationResource**](ApplicationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


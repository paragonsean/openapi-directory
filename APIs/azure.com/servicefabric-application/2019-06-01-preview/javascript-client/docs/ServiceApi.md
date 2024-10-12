# ServiceFabricManagementClient.ServiceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesCreate**](ServiceApi.md#servicesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Creates or updates a Service Fabric service resource.
[**servicesDelete**](ServiceApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Deletes a Service Fabric service resource.
[**servicesGet**](ServiceApi.md#servicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Gets a Service Fabric service resource.
[**servicesList**](ServiceApi.md#servicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services | Gets the list of service resources created in the specified Service Fabric application resource.
[**servicesUpdate**](ServiceApi.md#servicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Updates a Service Fabric service resource.



## servicesCreate

> ServiceResource servicesCreate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters)

Creates or updates a Service Fabric service resource.

Create or update a Service Fabric service resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
let parameters = new ServiceFabricManagementClient.ServiceResource(); // ServiceResource | The service resource.
apiInstance.servicesCreate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]
 **parameters** | [**ServiceResource**](ServiceResource.md)| The service resource. | 

### Return type

[**ServiceResource**](ServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesDelete

> servicesDelete(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion)

Deletes a Service Fabric service resource.

Delete a Service Fabric service resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
apiInstance.servicesDelete(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGet

> ServiceResource servicesGet(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion)

Gets a Service Fabric service resource.

Get a Service Fabric service resource created or in the process of being created in the Service Fabric application resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
apiInstance.servicesGet(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]

### Return type

[**ServiceResource**](ServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesList

> ServiceResourceList servicesList(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion)

Gets the list of service resources created in the specified Service Fabric application resource.

Gets all service resources created or in the process of being created in the Service Fabric application resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
apiInstance.servicesList(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]

### Return type

[**ServiceResourceList**](ServiceResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesUpdate

> ServiceResource servicesUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters)

Updates a Service Fabric service resource.

Update a Service Fabric service resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ServiceApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationName = "applicationName_example"; // String | The name of the application resource.
let serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
let apiVersion = "'2019-06-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
let parameters = new ServiceFabricManagementClient.ServiceResourceUpdate(); // ServiceResourceUpdate | The service resource for patch operations.
apiInstance.servicesUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to &#39;2019-06-01-preview&#39;]
 **parameters** | [**ServiceResourceUpdate**](ServiceResourceUpdate.md)| The service resource for patch operations. | 

### Return type

[**ServiceResource**](ServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


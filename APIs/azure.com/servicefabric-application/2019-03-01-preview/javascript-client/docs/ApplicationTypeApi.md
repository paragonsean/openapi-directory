# ServiceFabricManagementClient.ApplicationTypeApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationTypesCreate**](ApplicationTypeApi.md#applicationTypesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName} | Creates or updates a Service Fabric application type name resource.
[**applicationTypesDelete**](ApplicationTypeApi.md#applicationTypesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName} | Deletes a Service Fabric application type name resource.
[**applicationTypesGet**](ApplicationTypeApi.md#applicationTypesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName} | Gets a Service Fabric application type name resource.
[**applicationTypesList**](ApplicationTypeApi.md#applicationTypesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes | Gets the list of application type name resources created in the specified Service Fabric cluster resource.



## applicationTypesCreate

> ApplicationTypeResource applicationTypesCreate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion, parameters)

Creates or updates a Service Fabric application type name resource.

Create or update a Service Fabric application type name resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
let parameters = new ServiceFabricManagementClient.ApplicationTypeResource(); // ApplicationTypeResource | The application type name resource.
apiInstance.applicationTypesCreate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion, parameters, (error, data, response) => {
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
 **applicationTypeName** | **String**| The name of the application type name resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]
 **parameters** | [**ApplicationTypeResource**](ApplicationTypeResource.md)| The application type name resource. | 

### Return type

[**ApplicationTypeResource**](ApplicationTypeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationTypesDelete

> applicationTypesDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion)

Deletes a Service Fabric application type name resource.

Delete a Service Fabric application type name resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
apiInstance.applicationTypesDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion, (error, data, response) => {
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
 **applicationTypeName** | **String**| The name of the application type name resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypesGet

> ApplicationTypeResource applicationTypesGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion)

Gets a Service Fabric application type name resource.

Get a Service Fabric application type name resource created or in the process of being created in the Service Fabric cluster resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
apiInstance.applicationTypesGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion, (error, data, response) => {
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
 **applicationTypeName** | **String**| The name of the application type name resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]

### Return type

[**ApplicationTypeResource**](ApplicationTypeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypesList

> ApplicationTypeResourceList applicationTypesList(subscriptionId, resourceGroupName, clusterName, apiVersion)

Gets the list of application type name resources created in the specified Service Fabric cluster resource.

Gets all application type name resources created or in the process of being created in the Service Fabric cluster resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
apiInstance.applicationTypesList(subscriptionId, resourceGroupName, clusterName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]

### Return type

[**ApplicationTypeResourceList**](ApplicationTypeResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


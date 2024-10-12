# ServiceFabricManagementClient.ClusterApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersCreateOrUpdate**](ClusterApi.md#clustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName} | Creates or updates a Service Fabric cluster resource.
[**clustersDelete**](ClusterApi.md#clustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName} | Deletes a Service Fabric cluster resource.
[**clustersGet**](ClusterApi.md#clustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName} | Gets a Service Fabric cluster resource.
[**clustersList**](ClusterApi.md#clustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/clusters | Gets the list of Service Fabric cluster resources created in the specified subscription.
[**clustersListByResourceGroup**](ClusterApi.md#clustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters | Gets the list of Service Fabric cluster resources created in the specified resource group.
[**clustersUpdate**](ClusterApi.md#clustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName} | Updates the configuration of a Service Fabric cluster resource.



## clustersCreateOrUpdate

> Cluster clustersCreateOrUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)

Creates or updates a Service Fabric cluster resource.

Create or update a Service Fabric cluster resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let parameters = new ServiceFabricManagementClient.Cluster(); // Cluster | The cluster resource.
apiInstance.clustersCreateOrUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **parameters** | [**Cluster**](Cluster.md)| The cluster resource. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clustersDelete

> clustersDelete(resourceGroupName, clusterName, apiVersion, subscriptionId)

Deletes a Service Fabric cluster resource.

Delete a Service Fabric cluster resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
apiInstance.clustersDelete(resourceGroupName, clusterName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersGet

> Cluster clustersGet(resourceGroupName, clusterName, apiVersion, subscriptionId)

Gets a Service Fabric cluster resource.

Get a Service Fabric cluster resource created or in the process of being created in the specified resource group.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
apiInstance.clustersGet(resourceGroupName, clusterName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersList

> ClusterListResult clustersList(apiVersion, subscriptionId)

Gets the list of Service Fabric cluster resources created in the specified subscription.

Gets all Service Fabric cluster resources created or in the process of being created in the subscription.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterApi();
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
apiInstance.clustersList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersListByResourceGroup

> ClusterListResult clustersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)

Gets the list of Service Fabric cluster resources created in the specified resource group.

Gets all Service Fabric cluster resources created or in the process of being created in the resource group.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
apiInstance.clustersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersUpdate

> Cluster clustersUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)

Updates the configuration of a Service Fabric cluster resource.

Update the configuration of a Service Fabric cluster resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let apiVersion = "'2019-03-01'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let parameters = new ServiceFabricManagementClient.ClusterUpdateParameters(); // ClusterUpdateParameters | The parameters which contains the property value and property name which used to update the cluster configuration.
apiInstance.clustersUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to &#39;2019-03-01&#39;]
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **parameters** | [**ClusterUpdateParameters**](ClusterUpdateParameters.md)| The parameters which contains the property value and property name which used to update the cluster configuration. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# ContainerServiceClient.OpenShiftManagedClustersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openShiftManagedClustersCreateOrUpdate**](OpenShiftManagedClustersApi.md#openShiftManagedClustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Creates or updates an OpenShift managed cluster.
[**openShiftManagedClustersDelete**](OpenShiftManagedClustersApi.md#openShiftManagedClustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Deletes an OpenShift managed cluster.
[**openShiftManagedClustersGet**](OpenShiftManagedClustersApi.md#openShiftManagedClustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Gets a OpenShift managed cluster.
[**openShiftManagedClustersList**](OpenShiftManagedClustersApi.md#openShiftManagedClustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerService/openShiftManagedClusters | Gets a list of OpenShift managed clusters in the specified subscription.
[**openShiftManagedClustersListByResourceGroup**](OpenShiftManagedClustersApi.md#openShiftManagedClustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters | Lists OpenShift managed clusters in the specified subscription and resource group.
[**openShiftManagedClustersUpdateTags**](OpenShiftManagedClustersApi.md#openShiftManagedClustersUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resourceName} | Updates tags on an OpenShift managed cluster.



## openShiftManagedClustersCreateOrUpdate

> OpenShiftManagedCluster openShiftManagedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Creates or updates an OpenShift managed cluster.

Creates or updates a OpenShift managed cluster with the specified configuration for agents and OpenShift version.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.OpenShiftManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
let parameters = new ContainerServiceClient.OpenShiftManagedCluster(); // OpenShiftManagedCluster | Parameters supplied to the Create or Update an OpenShift Managed Cluster operation.
apiInstance.openShiftManagedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the OpenShift managed cluster resource. | 
 **parameters** | [**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)| Parameters supplied to the Create or Update an OpenShift Managed Cluster operation. | 

### Return type

[**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## openShiftManagedClustersDelete

> openShiftManagedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)

Deletes an OpenShift managed cluster.

Deletes the OpenShift managed cluster with a specified resource group and name.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.OpenShiftManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
apiInstance.openShiftManagedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the OpenShift managed cluster resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## openShiftManagedClustersGet

> OpenShiftManagedCluster openShiftManagedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets a OpenShift managed cluster.

Gets the details of the managed OpenShift cluster with a specified resource group and name.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.OpenShiftManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
apiInstance.openShiftManagedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the OpenShift managed cluster resource. | 

### Return type

[**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## openShiftManagedClustersList

> OpenShiftManagedClusterListResult openShiftManagedClustersList(apiVersion, subscriptionId)

Gets a list of OpenShift managed clusters in the specified subscription.

Gets a list of OpenShift managed clusters in the specified subscription. The operation returns properties of each OpenShift managed cluster.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.OpenShiftManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.openShiftManagedClustersList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**OpenShiftManagedClusterListResult**](OpenShiftManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## openShiftManagedClustersListByResourceGroup

> OpenShiftManagedClusterListResult openShiftManagedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Lists OpenShift managed clusters in the specified subscription and resource group.

Lists OpenShift managed clusters in the specified subscription and resource group. The operation returns properties of each OpenShift managed cluster.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.OpenShiftManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
apiInstance.openShiftManagedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 

### Return type

[**OpenShiftManagedClusterListResult**](OpenShiftManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## openShiftManagedClustersUpdateTags

> OpenShiftManagedCluster openShiftManagedClustersUpdateTags(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Updates tags on an OpenShift managed cluster.

Updates an OpenShift managed cluster with the specified tags.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.OpenShiftManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the OpenShift managed cluster resource.
let parameters = new ContainerServiceClient.TagsObject(); // TagsObject | Parameters supplied to the Update OpenShift Managed Cluster Tags operation.
apiInstance.openShiftManagedClustersUpdateTags(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **resourceName** | **String**| The name of the OpenShift managed cluster resource. | 
 **parameters** | [**TagsObject**](TagsObject.md)| Parameters supplied to the Update OpenShift Managed Cluster Tags operation. | 

### Return type

[**OpenShiftManagedCluster**](OpenShiftManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


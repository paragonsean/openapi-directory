# ContainerServiceClient.ManagedClustersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedClustersCreateOrUpdate**](ManagedClustersApi.md#managedClustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName} | Creates or updates a managed cluster.
[**managedClustersDelete**](ManagedClustersApi.md#managedClustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName} | Deletes a managed cluster.
[**managedClustersGet**](ManagedClustersApi.md#managedClustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName} | Gets a managed cluster.
[**managedClustersGetAccessProfile**](ManagedClustersApi.md#managedClustersGetAccessProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/accessProfiles/{roleName}/listCredential | Gets an access profile of a managed cluster.
[**managedClustersGetAccessProfiles**](ManagedClustersApi.md#managedClustersGetAccessProfiles) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/accessProfiles/{roleName} | Gets access profile of a managed cluster.
[**managedClustersGetUpgradeProfile**](ManagedClustersApi.md#managedClustersGetUpgradeProfile) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/upgradeProfiles/default | Gets upgrade profile for a managed cluster.
[**managedClustersList**](ManagedClustersApi.md#managedClustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerService/managedClusters | Gets a list of managed clusters in the specified subscription.
[**managedClustersListByResourceGroup**](ManagedClustersApi.md#managedClustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters | Lists managed clusters in the specified subscription and resource group.



## managedClustersCreateOrUpdate

> ManagedCluster managedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Creates or updates a managed cluster.

Creates or updates a managed cluster with the specified configuration for agents and Kubernetes version.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
let parameters = new ContainerServiceClient.ManagedCluster(); // ManagedCluster | Parameters supplied to the Create or Update a Managed Cluster operation.
apiInstance.managedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters, (error, data, response) => {
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
 **resourceName** | **String**| The name of the managed cluster resource. | 
 **parameters** | [**ManagedCluster**](ManagedCluster.md)| Parameters supplied to the Create or Update a Managed Cluster operation. | 

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managedClustersDelete

> managedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)

Deletes a managed cluster.

Deletes the managed cluster with a specified resource group and name.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
apiInstance.managedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the managed cluster resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managedClustersGet

> ManagedCluster managedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets a managed cluster.

Gets the details of the managed cluster with a specified resource group and name.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
apiInstance.managedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the managed cluster resource. | 

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedClustersGetAccessProfile

> ManagedClusterAccessProfile managedClustersGetAccessProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, roleName)

Gets an access profile of a managed cluster.

Gets the accessProfile for the specified role name of the managed cluster with a specified resource group and name.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
let roleName = "roleName_example"; // String | The name of the role for managed cluster accessProfile resource.
apiInstance.managedClustersGetAccessProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, roleName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the managed cluster resource. | 
 **roleName** | **String**| The name of the role for managed cluster accessProfile resource. | 

### Return type

[**ManagedClusterAccessProfile**](ManagedClusterAccessProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedClustersGetAccessProfiles

> ManagedClusterAccessProfile managedClustersGetAccessProfiles(apiVersion, subscriptionId, resourceGroupName, resourceName, roleName)

Gets access profile of a managed cluster.

Use ManagedClusters_GetAccessProfile instead.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
let roleName = "roleName_example"; // String | The name of the role for managed cluster accessProfile resource.
apiInstance.managedClustersGetAccessProfiles(apiVersion, subscriptionId, resourceGroupName, resourceName, roleName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the managed cluster resource. | 
 **roleName** | **String**| The name of the role for managed cluster accessProfile resource. | 

### Return type

[**ManagedClusterAccessProfile**](ManagedClusterAccessProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedClustersGetUpgradeProfile

> ManagedClusterUpgradeProfile managedClustersGetUpgradeProfile(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets upgrade profile for a managed cluster.

Gets the details of the upgrade profile for a managed cluster with a specified resource group and name.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
apiInstance.managedClustersGetUpgradeProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the managed cluster resource. | 

### Return type

[**ManagedClusterUpgradeProfile**](ManagedClusterUpgradeProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedClustersList

> ManagedClusterListResult managedClustersList(apiVersion, subscriptionId)

Gets a list of managed clusters in the specified subscription.

Gets a list of managed clusters in the specified subscription. The operation returns properties of each managed cluster.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.managedClustersList(apiVersion, subscriptionId, (error, data, response) => {
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

[**ManagedClusterListResult**](ManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedClustersListByResourceGroup

> ManagedClusterListResult managedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Lists managed clusters in the specified subscription and resource group.

Lists managed clusters in the specified subscription and resource group. The operation returns properties of each managed cluster.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ManagedClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
apiInstance.managedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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

[**ManagedClusterListResult**](ManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


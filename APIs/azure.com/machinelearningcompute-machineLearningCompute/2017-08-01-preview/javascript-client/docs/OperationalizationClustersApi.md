# MachineLearningComputeManagementClient.OperationalizationClustersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationalizationClustersCheckSystemServicesUpdatesAvailable**](OperationalizationClustersApi.md#operationalizationClustersCheckSystemServicesUpdatesAvailable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName}/checkSystemServicesUpdatesAvailable | 
[**operationalizationClustersCreateOrUpdate**](OperationalizationClustersApi.md#operationalizationClustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} | 
[**operationalizationClustersDelete**](OperationalizationClustersApi.md#operationalizationClustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} | 
[**operationalizationClustersGet**](OperationalizationClustersApi.md#operationalizationClustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} | 
[**operationalizationClustersListByResourceGroup**](OperationalizationClustersApi.md#operationalizationClustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters | 
[**operationalizationClustersListBySubscriptionId**](OperationalizationClustersApi.md#operationalizationClustersListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningCompute/operationalizationClusters | 
[**operationalizationClustersListKeys**](OperationalizationClustersApi.md#operationalizationClustersListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName}/listKeys | 
[**operationalizationClustersUpdate**](OperationalizationClustersApi.md#operationalizationClustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName} | 
[**operationalizationClustersUpdateSystemServices**](OperationalizationClustersApi.md#operationalizationClustersUpdateSystemServices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{clusterName}/updateSystemServices | 



## operationalizationClustersCheckSystemServicesUpdatesAvailable

> CheckSystemServicesUpdatesAvailableResponse operationalizationClustersCheckSystemServicesUpdatesAvailable(apiVersion, subscriptionId, resourceGroupName, clusterName)



Checks if updates are available for system services in the cluster.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let clusterName = "clusterName_example"; // String | The name of the cluster.
apiInstance.operationalizationClustersCheckSystemServicesUpdatesAvailable(apiVersion, subscriptionId, resourceGroupName, clusterName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **clusterName** | **String**| The name of the cluster. | 

### Return type

[**CheckSystemServicesUpdatesAvailableResponse**](CheckSystemServicesUpdatesAvailableResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationalizationClustersCreateOrUpdate

> OperationalizationCluster operationalizationClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters)



Create or update an operationalization cluster.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let parameters = new MachineLearningComputeManagementClient.OperationalizationCluster(); // OperationalizationCluster | Parameters supplied to create or update an Operationalization cluster.
apiInstance.operationalizationClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **clusterName** | **String**| The name of the cluster. | 
 **parameters** | [**OperationalizationCluster**](OperationalizationCluster.md)| Parameters supplied to create or update an Operationalization cluster. | 

### Return type

[**OperationalizationCluster**](OperationalizationCluster.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationalizationClustersDelete

> operationalizationClustersDelete(apiVersion, subscriptionId, resourceGroupName, clusterName, opts)



Deletes the specified cluster.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let opts = {
  'deleteAll': true // Boolean | If true, deletes all resources associated with this cluster.
};
apiInstance.operationalizationClustersDelete(apiVersion, subscriptionId, resourceGroupName, clusterName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **clusterName** | **String**| The name of the cluster. | 
 **deleteAll** | **Boolean**| If true, deletes all resources associated with this cluster. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationalizationClustersGet

> OperationalizationCluster operationalizationClustersGet(apiVersion, subscriptionId, resourceGroupName, clusterName)



Gets the operationalization cluster resource view. Note that the credentials are not returned by this call. Call ListKeys to get them.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let clusterName = "clusterName_example"; // String | The name of the cluster.
apiInstance.operationalizationClustersGet(apiVersion, subscriptionId, resourceGroupName, clusterName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **clusterName** | **String**| The name of the cluster. | 

### Return type

[**OperationalizationCluster**](OperationalizationCluster.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationalizationClustersListByResourceGroup

> PaginatedOperationalizationClustersList operationalizationClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, opts)



Gets the clusters in the specified resource group.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.operationalizationClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **skiptoken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**PaginatedOperationalizationClustersList**](PaginatedOperationalizationClustersList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationalizationClustersListBySubscriptionId

> PaginatedOperationalizationClustersList operationalizationClustersListBySubscriptionId(apiVersion, subscriptionId, opts)



Gets the operationalization clusters in the specified subscription.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.operationalizationClustersListBySubscriptionId(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **skiptoken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**PaginatedOperationalizationClustersList**](PaginatedOperationalizationClustersList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationalizationClustersListKeys

> OperationalizationClusterCredentials operationalizationClustersListKeys(apiVersion, subscriptionId, resourceGroupName, clusterName)



Gets the credentials for the specified cluster such as Storage, ACR and ACS credentials. This is a long running operation because it fetches keys from dependencies.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let clusterName = "clusterName_example"; // String | The name of the cluster.
apiInstance.operationalizationClustersListKeys(apiVersion, subscriptionId, resourceGroupName, clusterName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **clusterName** | **String**| The name of the cluster. | 

### Return type

[**OperationalizationClusterCredentials**](OperationalizationClusterCredentials.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationalizationClustersUpdate

> OperationalizationCluster operationalizationClustersUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters)



The PATCH operation can be used to update only the tags for a cluster. Use PUT operation to update other properties.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let parameters = new MachineLearningComputeManagementClient.OperationalizationClusterUpdateParameters(); // OperationalizationClusterUpdateParameters | The parameters supplied to patch the cluster.
apiInstance.operationalizationClustersUpdate(apiVersion, subscriptionId, resourceGroupName, clusterName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **clusterName** | **String**| The name of the cluster. | 
 **parameters** | [**OperationalizationClusterUpdateParameters**](OperationalizationClusterUpdateParameters.md)| The parameters supplied to patch the cluster. | 

### Return type

[**OperationalizationCluster**](OperationalizationCluster.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationalizationClustersUpdateSystemServices

> UpdateSystemServicesResponse operationalizationClustersUpdateSystemServices(apiVersion, subscriptionId, resourceGroupName, clusterName)



Updates system services in a cluster.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.OperationalizationClustersApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the cluster is located.
let clusterName = "clusterName_example"; // String | The name of the cluster.
apiInstance.operationalizationClustersUpdateSystemServices(apiVersion, subscriptionId, resourceGroupName, clusterName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of the resource group in which the cluster is located. | 
 **clusterName** | **String**| The name of the cluster. | 

### Return type

[**UpdateSystemServicesResponse**](UpdateSystemServicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


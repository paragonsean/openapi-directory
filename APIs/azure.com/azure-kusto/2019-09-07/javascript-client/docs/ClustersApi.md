# KustoManagementClient.ClustersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersCheckNameAvailability**](ClustersApi.md#clustersCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Kusto/locations/{location}/checkNameAvailability | 
[**clustersCreateOrUpdate**](ClustersApi.md#clustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} | 
[**clustersDelete**](ClustersApi.md#clustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} | 
[**clustersDetachFollowerDatabases**](ClustersApi.md#clustersDetachFollowerDatabases) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/detachFollowerDatabases | 
[**clustersGet**](ClustersApi.md#clustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} | 
[**clustersList**](ClustersApi.md#clustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Kusto/clusters | 
[**clustersListByResourceGroup**](ClustersApi.md#clustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters | 
[**clustersListFollowerDatabases**](ClustersApi.md#clustersListFollowerDatabases) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/listFollowerDatabases | 
[**clustersListSkusByResource**](ClustersApi.md#clustersListSkusByResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/skus | 
[**clustersStart**](ClustersApi.md#clustersStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/start | 
[**clustersStop**](ClustersApi.md#clustersStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/stop | 
[**clustersUpdate**](ClustersApi.md#clustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} | 



## clustersCheckNameAvailability

> CheckNameResult clustersCheckNameAvailability(apiVersion, subscriptionId, location, clusterName)



Checks that the cluster name is valid and is not already in use.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Azure location.
let clusterName = new KustoManagementClient.ClusterCheckNameRequest(); // ClusterCheckNameRequest | The name of the cluster.
apiInstance.clustersCheckNameAvailability(apiVersion, subscriptionId, location, clusterName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Azure location. | 
 **clusterName** | [**ClusterCheckNameRequest**](ClusterCheckNameRequest.md)| The name of the cluster. | 

### Return type

[**CheckNameResult**](CheckNameResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clustersCreateOrUpdate

> Cluster clustersCreateOrUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters)



Create or update a Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.Cluster(); // Cluster | The Kusto cluster parameters supplied to the CreateOrUpdate operation.
apiInstance.clustersCreateOrUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **parameters** | [**Cluster**](Cluster.md)| The Kusto cluster parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clustersDelete

> clustersDelete(resourceGroupName, clusterName, subscriptionId, apiVersion)



Deletes a Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.clustersDelete(resourceGroupName, clusterName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersDetachFollowerDatabases

> clustersDetachFollowerDatabases(resourceGroupName, clusterName, subscriptionId, apiVersion, followerDatabaseToRemove)



Detaches all followers of a database owned by this cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let followerDatabaseToRemove = new KustoManagementClient.FollowerDatabaseDefinition(); // FollowerDatabaseDefinition | The follower databases properties to remove.
apiInstance.clustersDetachFollowerDatabases(resourceGroupName, clusterName, subscriptionId, apiVersion, followerDatabaseToRemove, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **followerDatabaseToRemove** | [**FollowerDatabaseDefinition**](FollowerDatabaseDefinition.md)| The follower databases properties to remove. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clustersGet

> Cluster clustersGet(resourceGroupName, clusterName, subscriptionId, apiVersion)



Gets a Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.clustersGet(resourceGroupName, clusterName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersList

> ClusterListResult clustersList(subscriptionId, apiVersion)



Lists all Kusto clusters within a subscription.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.clustersList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersListByResourceGroup

> ClusterListResult clustersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Lists all Kusto clusters within a resource group.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.clustersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersListFollowerDatabases

> FollowerDatabaseListResult clustersListFollowerDatabases(resourceGroupName, clusterName, subscriptionId, apiVersion)



Returns a list of databases that are owned by this cluster and were followed by another cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.clustersListFollowerDatabases(resourceGroupName, clusterName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**FollowerDatabaseListResult**](FollowerDatabaseListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersListSkusByResource

> ListResourceSkusResult clustersListSkusByResource(resourceGroupName, clusterName, apiVersion, subscriptionId)



Returns the SKUs available for the provided resource.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.clustersListSkusByResource(resourceGroupName, clusterName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ListResourceSkusResult**](ListResourceSkusResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersStart

> clustersStart(resourceGroupName, clusterName, subscriptionId, apiVersion)



Starts a Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.clustersStart(resourceGroupName, clusterName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersStop

> clustersStop(resourceGroupName, clusterName, subscriptionId, apiVersion)



Stops a Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.clustersStop(resourceGroupName, clusterName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersUpdate

> Cluster clustersUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters)



Update a Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.ClusterUpdate(); // ClusterUpdate | The Kusto cluster parameters supplied to the Update operation.
apiInstance.clustersUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **parameters** | [**ClusterUpdate**](ClusterUpdate.md)| The Kusto cluster parameters supplied to the Update operation. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


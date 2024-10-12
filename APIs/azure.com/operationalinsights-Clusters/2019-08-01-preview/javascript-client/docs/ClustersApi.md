# AzureLogAnalytics.ClustersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersCreateOrUpdate**](ClustersApi.md#clustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} | 
[**clustersDelete**](ClustersApi.md#clustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} | 
[**clustersGet**](ClustersApi.md#clustersGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} | 
[**clustersList**](ClustersApi.md#clustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.OperationalInsights/clusters | 
[**clustersListByResourceGroup**](ClustersApi.md#clustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters | 
[**clustersUpdate**](ClustersApi.md#clustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/clusters/{clusterName} | 



## clustersCreateOrUpdate

> Cluster clustersCreateOrUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)



Create or update a Log Analytics cluster.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Log Analytics cluster.
let clusterName = "clusterName_example"; // String | The name of the Log Analytics cluster.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new AzureLogAnalytics.Cluster(); // Cluster | The parameters required to create or update a Log Analytics cluster.
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
 **resourceGroupName** | **String**| The resource group name of the Log Analytics cluster. | 
 **clusterName** | **String**| The name of the Log Analytics cluster. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Cluster**](Cluster.md)| The parameters required to create or update a Log Analytics cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## clustersDelete

> clustersDelete(resourceGroupName, clusterName, apiVersion, subscriptionId)



Deletes a cluster instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Log Analytics cluster.
let clusterName = "clusterName_example"; // String | Name of the Log Analytics Cluster.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The resource group name of the Log Analytics cluster. | 
 **clusterName** | **String**| Name of the Log Analytics Cluster. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersGet

> Cluster clustersGet(resourceGroupName, clusterName, apiVersion, subscriptionId)



Gets a Log Analytics cluster instance.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Log Analytics cluster.
let clusterName = "clusterName_example"; // String | Name of the Log Analytics Cluster.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The resource group name of the Log Analytics cluster. | 
 **clusterName** | **String**| Name of the Log Analytics Cluster. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersList

> ClusterListResult clustersList(apiVersion, subscriptionId)



Gets the Log Analytics clusters in a subscription.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.ClustersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersListByResourceGroup

> ClusterListResult clustersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets Log Analytics clusters in a resource group.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clustersUpdate

> Cluster clustersUpdate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)



Updates a Log Analytics cluster.

### Example

```javascript
import AzureLogAnalytics from 'azure_log_analytics';
let defaultClient = AzureLogAnalytics.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalytics.ClustersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the cluster.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new AzureLogAnalytics.ClusterPatch(); // ClusterPatch | The parameters required to patch a Log Analytics cluster.
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
 **resourceGroupName** | **String**| The resource group name of the cluster. | 
 **clusterName** | **String**| The name of the cluster. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ClusterPatch**](ClusterPatch.md)| The parameters required to patch a Log Analytics cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


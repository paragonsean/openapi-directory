# StorageManagementClient.QueueServicesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queueServicesGet**](QueueServicesApi.md#queueServicesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/queueservices/{serviceType} | 
[**queueServicesListMetricDefinitions**](QueueServicesApi.md#queueServicesListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/queueservices/{serviceType}/metricdefinitions | 
[**queueServicesListMetrics**](QueueServicesApi.md#queueServicesListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/queueservices/{serviceType}/metrics | 



## queueServicesGet

> QueueService queueServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns the queue service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.QueueServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.queueServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **serviceType** | **String**| The service type. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**QueueService**](QueueService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queueServicesListMetricDefinitions

> QueueServicesListMetricDefinitions200Response queueServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metric definitions for queue service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.QueueServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.queueServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **serviceType** | **String**| The service type. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**QueueServicesListMetricDefinitions200Response**](QueueServicesListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queueServicesListMetrics

> QueueServicesListMetrics200Response queueServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metrics for the queue service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.QueueServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.queueServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **farmId** | **String**| Farm Id. | 
 **serviceType** | **String**| The service type. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**QueueServicesListMetrics200Response**](QueueServicesListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


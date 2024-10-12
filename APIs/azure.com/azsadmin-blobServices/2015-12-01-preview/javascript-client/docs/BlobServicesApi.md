# StorageManagementClient.BlobServicesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobServicesGet**](BlobServicesApi.md#blobServicesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/blobservices/{serviceType} | 
[**blobServicesListMetricDefinitions**](BlobServicesApi.md#blobServicesListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/blobservices/{serviceType}/metricdefinitions | 
[**blobServicesListMetrics**](BlobServicesApi.md#blobServicesListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/blobservices/{serviceType}/metrics | 



## blobServicesGet

> BlobService blobServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns the BLOB service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.blobServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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

[**BlobService**](BlobService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobServicesListMetricDefinitions

> BlobServicesListMetricDefinitions200Response blobServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns the list of metric definitions for BLOB service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.blobServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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

[**BlobServicesListMetricDefinitions200Response**](BlobServicesListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobServicesListMetrics

> BlobServicesListMetrics200Response blobServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metrics for BLOB service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.blobServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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

[**BlobServicesListMetrics200Response**](BlobServicesListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


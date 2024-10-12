# StorageManagementClient.TableServicesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tableServicesGet**](TableServicesApi.md#tableServicesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/tableservices/{serviceType} | 
[**tableServicesListMetricDefinitions**](TableServicesApi.md#tableServicesListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/tableservices/{serviceType}/metricdefinitions | 
[**tableServicesListMetrics**](TableServicesApi.md#tableServicesListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/tableservices/{serviceType}/metrics | 



## tableServicesGet

> TableService tableServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns the table service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.TableServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.tableServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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

[**TableService**](TableService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tableServicesListMetricDefinitions

> TableServicesListMetricDefinitions200Response tableServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metric definitions for table service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.TableServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.tableServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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

[**TableServicesListMetricDefinitions200Response**](TableServicesListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tableServicesListMetrics

> TableServicesListMetrics200Response tableServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metrics for table service.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.TableServicesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let serviceType = "serviceType_example"; // String | The service type.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.tableServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion, (error, data, response) => {
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

[**TableServicesListMetrics200Response**](TableServicesListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# StorageManagementClient.SharesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharesGet**](SharesApi.md#sharesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName} | 
[**sharesList**](SharesApi.md#sharesList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares | 
[**sharesListMetricDefinitions**](SharesApi.md#sharesListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/metricdefinitions | 
[**sharesListMetrics**](SharesApi.md#sharesListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/shares/{shareName}/metrics | 



## sharesGet

> Share sharesGet(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a storage share.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.SharesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let shareName = "shareName_example"; // String | Share name.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.sharesGet(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| Share name. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesList

> [Share] sharesList(subscriptionId, resourceGroupName, farmId, apiVersion)



Returns a list of storage shares.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.SharesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.sharesList(subscriptionId, resourceGroupName, farmId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**[Share]**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesListMetricDefinitions

> SharesListMetricDefinitions200Response sharesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a list of metric definitions for a storage share.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.SharesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let shareName = "shareName_example"; // String | Share name.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.sharesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| Share name. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**SharesListMetricDefinitions200Response**](SharesListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesListMetrics

> SharesListMetrics200Response sharesListMetrics(subscriptionId, resourceGroupName, farmId, shareName, apiVersion)



Returns a list of metrics for a storage share.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.SharesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let farmId = "farmId_example"; // String | Farm Id.
let shareName = "shareName_example"; // String | Share name.
let apiVersion = "apiVersion_example"; // String | REST Api Version.
apiInstance.sharesListMetrics(subscriptionId, resourceGroupName, farmId, shareName, apiVersion, (error, data, response) => {
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
 **shareName** | **String**| Share name. | 
 **apiVersion** | **String**| REST Api Version. | 

### Return type

[**SharesListMetrics200Response**](SharesListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


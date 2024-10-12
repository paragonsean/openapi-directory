# MonitorManagementClient.AutoscaleSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoscaleSettingsCreateOrUpdate**](AutoscaleSettingsApi.md#autoscaleSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} | 
[**autoscaleSettingsDelete**](AutoscaleSettingsApi.md#autoscaleSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} | 
[**autoscaleSettingsGet**](AutoscaleSettingsApi.md#autoscaleSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} | 
[**autoscaleSettingsListByResourceGroup**](AutoscaleSettingsApi.md#autoscaleSettingsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings | 
[**autoscaleSettingsListBySubscription**](AutoscaleSettingsApi.md#autoscaleSettingsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/autoscalesettings | 



## autoscaleSettingsCreateOrUpdate

> AutoscaleSettingResource autoscaleSettingsCreateOrUpdate(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId, parameters)



Creates or updates an autoscale setting.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AutoscaleSettingsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let parameters = new MonitorManagementClient.AutoscaleSettingResource(); // AutoscaleSettingResource | Parameters supplied to the operation.
apiInstance.autoscaleSettingsCreateOrUpdate(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **autoscaleSettingName** | **String**| The autoscale setting name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **parameters** | [**AutoscaleSettingResource**](AutoscaleSettingResource.md)| Parameters supplied to the operation. | 

### Return type

[**AutoscaleSettingResource**](AutoscaleSettingResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## autoscaleSettingsDelete

> autoscaleSettingsDelete(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId)



Deletes and autoscale setting

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AutoscaleSettingsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.autoscaleSettingsDelete(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId, (error, data, response) => {
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
 **autoscaleSettingName** | **String**| The autoscale setting name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoscaleSettingsGet

> AutoscaleSettingResource autoscaleSettingsGet(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId)



Gets an autoscale setting

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AutoscaleSettingsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.autoscaleSettingsGet(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId, (error, data, response) => {
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
 **autoscaleSettingName** | **String**| The autoscale setting name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**AutoscaleSettingResource**](AutoscaleSettingResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoscaleSettingsListByResourceGroup

> AutoscaleSettingResourceCollection autoscaleSettingsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists the autoscale settings for a resource group

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AutoscaleSettingsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.autoscaleSettingsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**AutoscaleSettingResourceCollection**](AutoscaleSettingResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoscaleSettingsListBySubscription

> AutoscaleSettingResourceCollection autoscaleSettingsListBySubscription(apiVersion, subscriptionId)



Lists the autoscale settings for a subscription

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.AutoscaleSettingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
apiInstance.autoscaleSettingsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 

### Return type

[**AutoscaleSettingResourceCollection**](AutoscaleSettingResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


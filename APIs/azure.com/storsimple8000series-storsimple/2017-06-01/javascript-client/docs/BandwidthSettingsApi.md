# StorSimple8000SeriesManagementClient.BandwidthSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bandwidthSettingsCreateOrUpdate**](BandwidthSettingsApi.md#bandwidthSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/bandwidthSettings/{bandwidthSettingName} | 
[**bandwidthSettingsDelete**](BandwidthSettingsApi.md#bandwidthSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/bandwidthSettings/{bandwidthSettingName} | 
[**bandwidthSettingsGet**](BandwidthSettingsApi.md#bandwidthSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/bandwidthSettings/{bandwidthSettingName} | 
[**bandwidthSettingsListByManager**](BandwidthSettingsApi.md#bandwidthSettingsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/bandwidthSettings | 



## bandwidthSettingsCreateOrUpdate

> BandwidthSetting bandwidthSettingsCreateOrUpdate(bandwidthSettingName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters)



Creates or updates the bandwidth setting

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BandwidthSettingsApi();
let bandwidthSettingName = "bandwidthSettingName_example"; // String | The bandwidth setting name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let parameters = new StorSimple8000SeriesManagementClient.BandwidthSetting(); // BandwidthSetting | The bandwidth setting to be added or updated.
apiInstance.bandwidthSettingsCreateOrUpdate(bandwidthSettingName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters, (error, data, response) => {
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
 **bandwidthSettingName** | **String**| The bandwidth setting name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **parameters** | [**BandwidthSetting**](BandwidthSetting.md)| The bandwidth setting to be added or updated. | 

### Return type

[**BandwidthSetting**](BandwidthSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bandwidthSettingsDelete

> bandwidthSettingsDelete(bandwidthSettingName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the bandwidth setting

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BandwidthSettingsApi();
let bandwidthSettingName = "bandwidthSettingName_example"; // String | The name of the bandwidth setting.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.bandwidthSettingsDelete(bandwidthSettingName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **bandwidthSettingName** | **String**| The name of the bandwidth setting. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bandwidthSettingsGet

> BandwidthSetting bandwidthSettingsGet(bandwidthSettingName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified bandwidth setting name.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BandwidthSettingsApi();
let bandwidthSettingName = "bandwidthSettingName_example"; // String | The name of bandwidth setting to be fetched.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.bandwidthSettingsGet(bandwidthSettingName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **bandwidthSettingName** | **String**| The name of bandwidth setting to be fetched. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**BandwidthSetting**](BandwidthSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bandwidthSettingsListByManager

> BandwidthSettingList bandwidthSettingsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the bandwidth setting in a manager.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BandwidthSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.bandwidthSettingsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**BandwidthSettingList**](BandwidthSettingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


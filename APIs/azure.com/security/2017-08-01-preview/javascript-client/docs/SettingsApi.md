# SecurityCenter.SettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settingsGet**](SettingsApi.md#settingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/settings/{settingName} | 
[**settingsList**](SettingsApi.md#settingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/settings | 
[**settingsUpdate**](SettingsApi.md#settingsUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/settings/{settingName} | 



## settingsGet

> Setting settingsGet(apiVersion, subscriptionId, settingName)



Settings of different configurations in security center

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let settingName = "settingName_example"; // String | Name of setting: (MCAS/WDATP)
apiInstance.settingsGet(apiVersion, subscriptionId, settingName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **settingName** | **String**| Name of setting: (MCAS/WDATP) | 

### Return type

[**Setting**](Setting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsList

> SettingsList settingsList(apiVersion, subscriptionId)



Settings about different configurations in security center

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.settingsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 

### Return type

[**SettingsList**](SettingsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settingsUpdate

> Setting settingsUpdate(apiVersion, subscriptionId, settingName, setting)



updating settings about different configurations in security center

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.SettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let settingName = "settingName_example"; // String | Name of setting: (MCAS/WDATP)
let setting = new SecurityCenter.Setting(); // Setting | Setting object
apiInstance.settingsUpdate(apiVersion, subscriptionId, settingName, setting, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **settingName** | **String**| Name of setting: (MCAS/WDATP) | 
 **setting** | [**Setting**](Setting.md)| Setting object | 

### Return type

[**Setting**](Setting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


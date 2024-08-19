# SecurityCenter.AutoProvisioningSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoProvisioningSettingsCreate**](AutoProvisioningSettingsApi.md#autoProvisioningSettingsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/autoProvisioningSettings/{settingName} | 
[**autoProvisioningSettingsGet**](AutoProvisioningSettingsApi.md#autoProvisioningSettingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/autoProvisioningSettings/{settingName} | 
[**autoProvisioningSettingsList**](AutoProvisioningSettingsApi.md#autoProvisioningSettingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/autoProvisioningSettings | 



## autoProvisioningSettingsCreate

> AutoProvisioningSetting autoProvisioningSettingsCreate(apiVersion, subscriptionId, settingName, setting)



Details of a specific setting

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutoProvisioningSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let settingName = "settingName_example"; // String | Auto provisioning setting key
let setting = new SecurityCenter.AutoProvisioningSetting(); // AutoProvisioningSetting | Auto provisioning setting key
apiInstance.autoProvisioningSettingsCreate(apiVersion, subscriptionId, settingName, setting, (error, data, response) => {
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
 **settingName** | **String**| Auto provisioning setting key | 
 **setting** | [**AutoProvisioningSetting**](AutoProvisioningSetting.md)| Auto provisioning setting key | 

### Return type

[**AutoProvisioningSetting**](AutoProvisioningSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## autoProvisioningSettingsGet

> AutoProvisioningSetting autoProvisioningSettingsGet(apiVersion, subscriptionId, settingName)



Details of a specific setting

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutoProvisioningSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let settingName = "settingName_example"; // String | Auto provisioning setting key
apiInstance.autoProvisioningSettingsGet(apiVersion, subscriptionId, settingName, (error, data, response) => {
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
 **settingName** | **String**| Auto provisioning setting key | 

### Return type

[**AutoProvisioningSetting**](AutoProvisioningSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## autoProvisioningSettingsList

> AutoProvisioningSettingList autoProvisioningSettingsList(apiVersion, subscriptionId)



Exposes the auto provisioning settings of the subscriptions

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AutoProvisioningSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.autoProvisioningSettingsList(apiVersion, subscriptionId, (error, data, response) => {
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

[**AutoProvisioningSettingList**](AutoProvisioningSettingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# SecurityCenter.AdvancedThreatProtectionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advancedThreatProtectionCreate**](AdvancedThreatProtectionApi.md#advancedThreatProtectionCreate) | **PUT** /{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName} | 
[**advancedThreatProtectionGet**](AdvancedThreatProtectionApi.md#advancedThreatProtectionGet) | **GET** /{resourceId}/providers/Microsoft.Security/advancedThreatProtectionSettings/{settingName} | 



## advancedThreatProtectionCreate

> AdvancedThreatProtectionSetting advancedThreatProtectionCreate(apiVersion, resourceId, settingName, advancedThreatProtectionSetting)



Creates or updates the Advanced Threat Protection settings on a specified resource.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AdvancedThreatProtectionApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let resourceId = "resourceId_example"; // String | The identifier of the resource.
let settingName = "settingName_example"; // String | Advanced Threat Protection setting name.
let advancedThreatProtectionSetting = new SecurityCenter.AdvancedThreatProtectionSetting(); // AdvancedThreatProtectionSetting | Advanced Threat Protection Settings
apiInstance.advancedThreatProtectionCreate(apiVersion, resourceId, settingName, advancedThreatProtectionSetting, (error, data, response) => {
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
 **resourceId** | **String**| The identifier of the resource. | 
 **settingName** | **String**| Advanced Threat Protection setting name. | 
 **advancedThreatProtectionSetting** | [**AdvancedThreatProtectionSetting**](AdvancedThreatProtectionSetting.md)| Advanced Threat Protection Settings | 

### Return type

[**AdvancedThreatProtectionSetting**](AdvancedThreatProtectionSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## advancedThreatProtectionGet

> AdvancedThreatProtectionSetting advancedThreatProtectionGet(apiVersion, resourceId, settingName)



Gets the Advanced Threat Protection settings for the specified resource.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AdvancedThreatProtectionApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let resourceId = "resourceId_example"; // String | The identifier of the resource.
let settingName = "settingName_example"; // String | Advanced Threat Protection setting name.
apiInstance.advancedThreatProtectionGet(apiVersion, resourceId, settingName, (error, data, response) => {
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
 **resourceId** | **String**| The identifier of the resource. | 
 **settingName** | **String**| Advanced Threat Protection setting name. | 

### Return type

[**AdvancedThreatProtectionSetting**](AdvancedThreatProtectionSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


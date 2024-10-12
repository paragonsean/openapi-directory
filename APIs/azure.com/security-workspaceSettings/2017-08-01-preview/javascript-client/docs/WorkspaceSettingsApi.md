# SecurityCenter.WorkspaceSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSettingsCreate**](WorkspaceSettingsApi.md#workspaceSettingsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} | 
[**workspaceSettingsDelete**](WorkspaceSettingsApi.md#workspaceSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} | 
[**workspaceSettingsGet**](WorkspaceSettingsApi.md#workspaceSettingsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} | 
[**workspaceSettingsList**](WorkspaceSettingsApi.md#workspaceSettingsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings | 
[**workspaceSettingsUpdate**](WorkspaceSettingsApi.md#workspaceSettingsUpdate) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.Security/workspaceSettings/{workspaceSettingName} | 



## workspaceSettingsCreate

> WorkspaceSetting workspaceSettingsCreate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting)



creating settings about where we should store your security data and logs

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.WorkspaceSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
let workspaceSetting = new SecurityCenter.WorkspaceSetting(); // WorkspaceSetting | Security data setting object
apiInstance.workspaceSettingsCreate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting, (error, data, response) => {
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
 **workspaceSettingName** | **String**| Name of the security setting | 
 **workspaceSetting** | [**WorkspaceSetting**](WorkspaceSetting.md)| Security data setting object | 

### Return type

[**WorkspaceSetting**](WorkspaceSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workspaceSettingsDelete

> workspaceSettingsDelete(apiVersion, subscriptionId, workspaceSettingName)



Deletes the custom workspace settings for this subscription. new VMs will report to the default workspace

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.WorkspaceSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
apiInstance.workspaceSettingsDelete(apiVersion, subscriptionId, workspaceSettingName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **workspaceSettingName** | **String**| Name of the security setting | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSettingsGet

> WorkspaceSetting workspaceSettingsGet(apiVersion, subscriptionId, workspaceSettingName)



Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.WorkspaceSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
apiInstance.workspaceSettingsGet(apiVersion, subscriptionId, workspaceSettingName, (error, data, response) => {
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
 **workspaceSettingName** | **String**| Name of the security setting | 

### Return type

[**WorkspaceSetting**](WorkspaceSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSettingsList

> WorkspaceSettingList workspaceSettingsList(apiVersion, subscriptionId)



Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.WorkspaceSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.workspaceSettingsList(apiVersion, subscriptionId, (error, data, response) => {
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

[**WorkspaceSettingList**](WorkspaceSettingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workspaceSettingsUpdate

> WorkspaceSetting workspaceSettingsUpdate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting)



Settings about where we should store your security data and logs

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.WorkspaceSettingsApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let workspaceSettingName = "workspaceSettingName_example"; // String | Name of the security setting
let workspaceSetting = new SecurityCenter.WorkspaceSetting(); // WorkspaceSetting | Security data setting object
apiInstance.workspaceSettingsUpdate(apiVersion, subscriptionId, workspaceSettingName, workspaceSetting, (error, data, response) => {
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
 **workspaceSettingName** | **String**| Name of the security setting | 
 **workspaceSetting** | [**WorkspaceSetting**](WorkspaceSetting.md)| Security data setting object | 

### Return type

[**WorkspaceSetting**](WorkspaceSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


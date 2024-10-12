# MonitorManagementClient.SubscriptionDiagnosticSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionDiagnosticSettingsCreateOrUpdate**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings/{name} | 
[**subscriptionDiagnosticSettingsDelete**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings/{name} | 
[**subscriptionDiagnosticSettingsGet**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsGet) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings/{name} | 
[**subscriptionDiagnosticSettingsList**](SubscriptionDiagnosticSettingsApi.md#subscriptionDiagnosticSettingsList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/diagnosticSettings | 



## subscriptionDiagnosticSettingsCreateOrUpdate

> SubscriptionDiagnosticSettingsResource subscriptionDiagnosticSettingsCreateOrUpdate(subscriptionId, apiVersion, name, parameters)



Creates or updates subscription diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.SubscriptionDiagnosticSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
let parameters = new MonitorManagementClient.SubscriptionDiagnosticSettingsResource(); // SubscriptionDiagnosticSettingsResource | Parameters supplied to the operation.
apiInstance.subscriptionDiagnosticSettingsCreateOrUpdate(subscriptionId, apiVersion, name, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **name** | **String**| The name of the diagnostic setting. | 
 **parameters** | [**SubscriptionDiagnosticSettingsResource**](SubscriptionDiagnosticSettingsResource.md)| Parameters supplied to the operation. | 

### Return type

[**SubscriptionDiagnosticSettingsResource**](SubscriptionDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## subscriptionDiagnosticSettingsDelete

> subscriptionDiagnosticSettingsDelete(subscriptionId, apiVersion, name)



Deletes existing subscription diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.SubscriptionDiagnosticSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
apiInstance.subscriptionDiagnosticSettingsDelete(subscriptionId, apiVersion, name, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **name** | **String**| The name of the diagnostic setting. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionDiagnosticSettingsGet

> SubscriptionDiagnosticSettingsResource subscriptionDiagnosticSettingsGet(subscriptionId, apiVersion, name)



Gets the active subscription diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.SubscriptionDiagnosticSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
apiInstance.subscriptionDiagnosticSettingsGet(subscriptionId, apiVersion, name, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **name** | **String**| The name of the diagnostic setting. | 

### Return type

[**SubscriptionDiagnosticSettingsResource**](SubscriptionDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionDiagnosticSettingsList

> SubscriptionDiagnosticSettingsResourceCollection subscriptionDiagnosticSettingsList(subscriptionId, apiVersion)



Gets the active subscription diagnostic settings list for the specified subscriptionId.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.SubscriptionDiagnosticSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.subscriptionDiagnosticSettingsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**SubscriptionDiagnosticSettingsResourceCollection**](SubscriptionDiagnosticSettingsResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


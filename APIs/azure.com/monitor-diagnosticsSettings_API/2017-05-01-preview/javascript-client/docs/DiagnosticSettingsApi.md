# MonitorManagementClient.DiagnosticSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnosticSettingsCreateOrUpdate**](DiagnosticSettingsApi.md#diagnosticSettingsCreateOrUpdate) | **PUT** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/{name} | 
[**diagnosticSettingsDelete**](DiagnosticSettingsApi.md#diagnosticSettingsDelete) | **DELETE** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/{name} | 
[**diagnosticSettingsGet**](DiagnosticSettingsApi.md#diagnosticSettingsGet) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/{name} | 
[**diagnosticSettingsList**](DiagnosticSettingsApi.md#diagnosticSettingsList) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettings | 



## diagnosticSettingsCreateOrUpdate

> DiagnosticSettingsResource diagnosticSettingsCreateOrUpdate(resourceUri, apiVersion, name, parameters)



Creates or updates diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DiagnosticSettingsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
let parameters = new MonitorManagementClient.DiagnosticSettingsResource(); // DiagnosticSettingsResource | Parameters supplied to the operation.
apiInstance.diagnosticSettingsCreateOrUpdate(resourceUri, apiVersion, name, parameters, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. | 
 **apiVersion** | **String**| Client Api Version. | 
 **name** | **String**| The name of the diagnostic setting. | 
 **parameters** | [**DiagnosticSettingsResource**](DiagnosticSettingsResource.md)| Parameters supplied to the operation. | 

### Return type

[**DiagnosticSettingsResource**](DiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## diagnosticSettingsDelete

> diagnosticSettingsDelete(resourceUri, apiVersion, name)



Deletes existing diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DiagnosticSettingsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
apiInstance.diagnosticSettingsDelete(resourceUri, apiVersion, name, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. | 
 **apiVersion** | **String**| Client Api Version. | 
 **name** | **String**| The name of the diagnostic setting. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticSettingsGet

> DiagnosticSettingsResource diagnosticSettingsGet(resourceUri, apiVersion, name)



Gets the active diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DiagnosticSettingsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
apiInstance.diagnosticSettingsGet(resourceUri, apiVersion, name, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. | 
 **apiVersion** | **String**| Client Api Version. | 
 **name** | **String**| The name of the diagnostic setting. | 

### Return type

[**DiagnosticSettingsResource**](DiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticSettingsList

> DiagnosticSettingsResourceCollection diagnosticSettingsList(resourceUri, apiVersion)



Gets the active diagnostic settings list for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DiagnosticSettingsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diagnosticSettingsList(resourceUri, apiVersion, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DiagnosticSettingsResourceCollection**](DiagnosticSettingsResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


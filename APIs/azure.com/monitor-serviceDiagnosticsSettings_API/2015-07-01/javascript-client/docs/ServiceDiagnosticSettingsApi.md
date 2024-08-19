# MonitorManagementClient.ServiceDiagnosticSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceDiagnosticSettingsCreateOrUpdate**](ServiceDiagnosticSettingsApi.md#serviceDiagnosticSettingsCreateOrUpdate) | **PUT** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/service | 
[**serviceDiagnosticSettingsGet**](ServiceDiagnosticSettingsApi.md#serviceDiagnosticSettingsGet) | **GET** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/service | 



## serviceDiagnosticSettingsCreateOrUpdate

> ServiceDiagnosticSettingsResource serviceDiagnosticSettingsCreateOrUpdate(resourceUri, apiVersion, parameters)



Create or update new diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.ServiceDiagnosticSettingsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new MonitorManagementClient.ServiceDiagnosticSettingsResource(); // ServiceDiagnosticSettingsResource | Parameters supplied to the operation.
apiInstance.serviceDiagnosticSettingsCreateOrUpdate(resourceUri, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**ServiceDiagnosticSettingsResource**](ServiceDiagnosticSettingsResource.md)| Parameters supplied to the operation. | 

### Return type

[**ServiceDiagnosticSettingsResource**](ServiceDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceDiagnosticSettingsGet

> ServiceDiagnosticSettingsResource serviceDiagnosticSettingsGet(resourceUri, apiVersion)



Gets the active diagnostic settings for the specified resource.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.ServiceDiagnosticSettingsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.serviceDiagnosticSettingsGet(resourceUri, apiVersion, (error, data, response) => {
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

[**ServiceDiagnosticSettingsResource**](ServiceDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


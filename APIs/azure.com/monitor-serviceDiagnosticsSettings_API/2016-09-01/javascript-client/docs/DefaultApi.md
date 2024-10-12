# MonitorManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceDiagnosticSettingsUpdate**](DefaultApi.md#serviceDiagnosticSettingsUpdate) | **PATCH** /{resourceUri}/providers/microsoft.insights/diagnosticSettings/service | 



## serviceDiagnosticSettingsUpdate

> ServiceDiagnosticSettingsResource serviceDiagnosticSettingsUpdate(resourceUri, apiVersion, serviceDiagnosticSettingsResource)



Updates an existing ServiceDiagnosticSettingsResource. To update other fields use the CreateOrUpdate method. **WARNING**: This method will be deprecated in future releases.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DefaultApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let serviceDiagnosticSettingsResource = new MonitorManagementClient.ServiceDiagnosticSettingsResourcePatch(); // ServiceDiagnosticSettingsResourcePatch | Parameters supplied to the operation.
apiInstance.serviceDiagnosticSettingsUpdate(resourceUri, apiVersion, serviceDiagnosticSettingsResource, (error, data, response) => {
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
 **serviceDiagnosticSettingsResource** | [**ServiceDiagnosticSettingsResourcePatch**](ServiceDiagnosticSettingsResourcePatch.md)| Parameters supplied to the operation. | 

### Return type

[**ServiceDiagnosticSettingsResource**](ServiceDiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


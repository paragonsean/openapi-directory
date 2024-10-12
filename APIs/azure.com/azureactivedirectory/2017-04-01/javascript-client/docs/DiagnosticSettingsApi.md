# Azureactivedirectory.DiagnosticSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnosticSettingsCreateOrUpdate**](DiagnosticSettingsApi.md#diagnosticSettingsCreateOrUpdate) | **PUT** /providers/microsoft.aadiam/diagnosticSettings/{name} | 
[**diagnosticSettingsDelete**](DiagnosticSettingsApi.md#diagnosticSettingsDelete) | **DELETE** /providers/microsoft.aadiam/diagnosticSettings/{name} | 
[**diagnosticSettingsGet**](DiagnosticSettingsApi.md#diagnosticSettingsGet) | **GET** /providers/microsoft.aadiam/diagnosticSettings/{name} | 
[**diagnosticSettingsList**](DiagnosticSettingsApi.md#diagnosticSettingsList) | **GET** /providers/microsoft.aadiam/diagnosticSettings | 



## diagnosticSettingsCreateOrUpdate

> DiagnosticSettingsResource diagnosticSettingsCreateOrUpdate(apiVersion, name, parameters)



Creates or updates diagnostic settings for AadIam.

### Example

```javascript
import Azureactivedirectory from 'azureactivedirectory';
let defaultClient = Azureactivedirectory.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Azureactivedirectory.DiagnosticSettingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
let parameters = new Azureactivedirectory.DiagnosticSettingsResource(); // DiagnosticSettingsResource | Parameters supplied to the operation.
apiInstance.diagnosticSettingsCreateOrUpdate(apiVersion, name, parameters, (error, data, response) => {
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

> diagnosticSettingsDelete(apiVersion, name)



Deletes existing diagnostic setting for AadIam.

### Example

```javascript
import Azureactivedirectory from 'azureactivedirectory';
let defaultClient = Azureactivedirectory.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Azureactivedirectory.DiagnosticSettingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
apiInstance.diagnosticSettingsDelete(apiVersion, name, (error, data, response) => {
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

> DiagnosticSettingsResource diagnosticSettingsGet(apiVersion, name)



Gets the active diagnostic setting for AadIam.

### Example

```javascript
import Azureactivedirectory from 'azureactivedirectory';
let defaultClient = Azureactivedirectory.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Azureactivedirectory.DiagnosticSettingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let name = "name_example"; // String | The name of the diagnostic setting.
apiInstance.diagnosticSettingsGet(apiVersion, name, (error, data, response) => {
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
 **name** | **String**| The name of the diagnostic setting. | 

### Return type

[**DiagnosticSettingsResource**](DiagnosticSettingsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticSettingsList

> DiagnosticSettingsResourceCollection diagnosticSettingsList(apiVersion)



Gets the active diagnostic settings list for AadIam.

### Example

```javascript
import Azureactivedirectory from 'azureactivedirectory';
let defaultClient = Azureactivedirectory.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Azureactivedirectory.DiagnosticSettingsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diagnosticSettingsList(apiVersion, (error, data, response) => {
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

### Return type

[**DiagnosticSettingsResourceCollection**](DiagnosticSettingsResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# MicrosoftSerialConsoleClient.SerialConsoleApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disableConsole**](SerialConsoleApi.md#disableConsole) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/disableConsole | Disable Serial Console for a subscription
[**enableConsole**](SerialConsoleApi.md#enableConsole) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/enableConsole | Enable Serial Console for a subscription
[**getConsoleStatus**](SerialConsoleApi.md#getConsoleStatus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default} | Get the disabled status for a subscription
[**listOperations**](SerialConsoleApi.md#listOperations) | **GET** /providers/Microsoft.SerialConsole/operations | 



## disableConsole

> DisableSerialConsoleResult disableConsole(apiVersion, subscriptionId, _default)

Disable Serial Console for a subscription

Disables the Serial Console service for all VMs and VM scale sets in the provided subscription

### Example

```javascript
import MicrosoftSerialConsoleClient from 'microsoft_serial_console_client';
let defaultClient = MicrosoftSerialConsoleClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSerialConsoleClient.SerialConsoleApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
let _default = "_default_example"; // String | Default parameter. Leave the value as \"default\".
apiInstance.disableConsole(apiVersion, subscriptionId, _default, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it. | 
 **_default** | **String**| Default parameter. Leave the value as \&quot;default\&quot;. | 

### Return type

[**DisableSerialConsoleResult**](DisableSerialConsoleResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableConsole

> EnableSerialConsoleResult enableConsole(apiVersion, subscriptionId, _default)

Enable Serial Console for a subscription

Enables the Serial Console service for all VMs and VM scale sets in the provided subscription

### Example

```javascript
import MicrosoftSerialConsoleClient from 'microsoft_serial_console_client';
let defaultClient = MicrosoftSerialConsoleClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSerialConsoleClient.SerialConsoleApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
let _default = "_default_example"; // String | Default parameter. Leave the value as \"default\".
apiInstance.enableConsole(apiVersion, subscriptionId, _default, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it. | 
 **_default** | **String**| Default parameter. Leave the value as \&quot;default\&quot;. | 

### Return type

[**EnableSerialConsoleResult**](EnableSerialConsoleResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConsoleStatus

> SerialConsoleStatus getConsoleStatus(apiVersion, subscriptionId, _default)

Get the disabled status for a subscription

Gets whether or not Serial Console is disabled for a given subscription

### Example

```javascript
import MicrosoftSerialConsoleClient from 'microsoft_serial_console_client';
let defaultClient = MicrosoftSerialConsoleClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSerialConsoleClient.SerialConsoleApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it.
let _default = "_default_example"; // String | Default parameter. Leave the value as \"default\".
apiInstance.getConsoleStatus(apiVersion, subscriptionId, _default, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identifies the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call requiring it. | 
 **_default** | **String**| Default parameter. Leave the value as \&quot;default\&quot;. | 

### Return type

[**SerialConsoleStatus**](SerialConsoleStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOperations

> SerialConsoleOperations listOperations(apiVersion)



Gets a list of Serial Console API operations.

### Example

```javascript
import MicrosoftSerialConsoleClient from 'microsoft_serial_console_client';
let defaultClient = MicrosoftSerialConsoleClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftSerialConsoleClient.SerialConsoleApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.listOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**SerialConsoleOperations**](SerialConsoleOperations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


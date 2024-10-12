# ManagementApi.TerminalSettingsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTerminalsTerminalIdTerminalLogos**](TerminalSettingsTerminalLevelApi.md#getTerminalsTerminalIdTerminalLogos) | **GET** /terminals/{terminalId}/terminalLogos | Get the terminal logo
[**getTerminalsTerminalIdTerminalSettings**](TerminalSettingsTerminalLevelApi.md#getTerminalsTerminalIdTerminalSettings) | **GET** /terminals/{terminalId}/terminalSettings | Get terminal settings
[**patchTerminalsTerminalIdTerminalLogos**](TerminalSettingsTerminalLevelApi.md#patchTerminalsTerminalIdTerminalLogos) | **PATCH** /terminals/{terminalId}/terminalLogos | Update the logo
[**patchTerminalsTerminalIdTerminalSettings**](TerminalSettingsTerminalLevelApi.md#patchTerminalsTerminalIdTerminalSettings) | **PATCH** /terminals/{terminalId}/terminalSettings | Update terminal settings



## getTerminalsTerminalIdTerminalLogos

> Logo getTerminalsTerminalIdTerminalLogos(terminalId)

Get the terminal logo

Returns the logo that is configured for the payment terminal identified in the path. The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalSettingsTerminalLevelApi();
let terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
apiInstance.getTerminalsTerminalIdTerminalLogos(terminalId, (error, data, response) => {
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
 **terminalId** | **String**| The unique identifier of the payment terminal. | 

### Return type

[**Logo**](Logo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTerminalsTerminalIdTerminalSettings

> TerminalSettings getTerminalsTerminalIdTerminalSettings(terminalId)

Get terminal settings

Returns the settings that are configured for the payment terminal identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalSettingsTerminalLevelApi();
let terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
apiInstance.getTerminalsTerminalIdTerminalSettings(terminalId, (error, data, response) => {
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
 **terminalId** | **String**| The unique identifier of the payment terminal. | 

### Return type

[**TerminalSettings**](TerminalSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchTerminalsTerminalIdTerminalLogos

> Logo patchTerminalsTerminalIdTerminalLogos(terminalId, opts)

Update the logo

Updates the logo for the payment terminal identified in the path.  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from a higher level (store, merchant account, or company account), specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalSettingsTerminalLevelApi();
let terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
let opts = {
  'logo': new ManagementApi.Logo() // Logo | 
};
apiInstance.patchTerminalsTerminalIdTerminalLogos(terminalId, opts, (error, data, response) => {
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
 **terminalId** | **String**| The unique identifier of the payment terminal. | 
 **logo** | [**Logo**](Logo.md)|  | [optional] 

### Return type

[**Logo**](Logo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchTerminalsTerminalIdTerminalSettings

> TerminalSettings patchTerminalsTerminalIdTerminalSettings(terminalId, opts)

Update terminal settings

Updates the settings that are configured for the payment terminal identified in the path.  * To change a parameter value, include the full object that contains the parameter, even if you don&#39;t want to change all parameters in the object. * To restore a parameter value inherited from a higher level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalSettingsTerminalLevelApi();
let terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
let opts = {
  'terminalSettings': new ManagementApi.TerminalSettings() // TerminalSettings | 
};
apiInstance.patchTerminalsTerminalIdTerminalSettings(terminalId, opts, (error, data, response) => {
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
 **terminalId** | **String**| The unique identifier of the payment terminal. | 
 **terminalSettings** | [**TerminalSettings**](TerminalSettings.md)|  | [optional] 

### Return type

[**TerminalSettings**](TerminalSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


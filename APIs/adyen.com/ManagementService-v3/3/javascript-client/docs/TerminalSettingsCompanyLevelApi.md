# ManagementApi.TerminalSettingsCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompaniesCompanyIdTerminalLogos**](TerminalSettingsCompanyLevelApi.md#getCompaniesCompanyIdTerminalLogos) | **GET** /companies/{companyId}/terminalLogos | Get the terminal logo
[**getCompaniesCompanyIdTerminalSettings**](TerminalSettingsCompanyLevelApi.md#getCompaniesCompanyIdTerminalSettings) | **GET** /companies/{companyId}/terminalSettings | Get terminal settings
[**patchCompaniesCompanyIdTerminalLogos**](TerminalSettingsCompanyLevelApi.md#patchCompaniesCompanyIdTerminalLogos) | **PATCH** /companies/{companyId}/terminalLogos | Update the terminal logo
[**patchCompaniesCompanyIdTerminalSettings**](TerminalSettingsCompanyLevelApi.md#patchCompaniesCompanyIdTerminalSettings) | **PATCH** /companies/{companyId}/terminalSettings | Update terminal settings



## getCompaniesCompanyIdTerminalLogos

> Logo getCompaniesCompanyIdTerminalLogos(companyId, model)

Get the terminal logo

Returns the logo that is configured for a specific payment terminal model at the company identified in the path.   The logo is returned as a Base64-encoded string. You need to Base64-decode the string to get the actual image file.  This logo applies to all terminals of the specified model under the company, unless a different logo is configured at a lower level (merchant account, store, or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write

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

let apiInstance = new ManagementApi.TerminalSettingsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let model = "model_example"; // String | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
apiInstance.getCompaniesCompanyIdTerminalLogos(companyId, model, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **model** | **String**| The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. | 

### Return type

[**Logo**](Logo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdTerminalSettings

> TerminalSettings getCompaniesCompanyIdTerminalSettings(companyId)

Get terminal settings

Returns the payment terminal settings that are configured for the company identified in the path. These settings apply to all terminals under the company, unless different values are configured at a lower level (merchant account, store, or individual terminal).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

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

let apiInstance = new ManagementApi.TerminalSettingsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
apiInstance.getCompaniesCompanyIdTerminalSettings(companyId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 

### Return type

[**TerminalSettings**](TerminalSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchCompaniesCompanyIdTerminalLogos

> Logo patchCompaniesCompanyIdTerminalLogos(companyId, model, opts)

Update the terminal logo

Updates the logo that is configured for a specific payment terminal model at the company identified in the path. You can update the logo for only one terminal model at a time. This logo applies to all terminals of the specified model under the company, unless a different logo is configured at a lower level (merchant account, store, or individual terminal).  * To change the logo, specify the image file as a Base64-encoded string. * To restore the logo inherited from the Adyen PSP level, specify an empty logo value.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write

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

let apiInstance = new ManagementApi.TerminalSettingsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let model = "model_example"; // String | The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T.
let opts = {
  'logo': new ManagementApi.Logo() // Logo | 
};
apiInstance.patchCompaniesCompanyIdTerminalLogos(companyId, model, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **model** | **String**| The terminal model. Possible values: E355, VX675WIFIBT, VX680, VX690, VX700, VX820, M400, MX925, P400Plus, UX300, UX410, V200cPlus, V240mPlus, V400cPlus, V400m, e280, e285, e285p, S1E, S1EL, S1F2, S1L, S1U, S7T. | 
 **logo** | [**Logo**](Logo.md)|  | [optional] 

### Return type

[**Logo**](Logo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchCompaniesCompanyIdTerminalSettings

> TerminalSettings patchCompaniesCompanyIdTerminalSettings(companyId, opts)

Update terminal settings

Updates payment terminal settings for the company identified in the path. These settings apply to all terminals under the company, unless different values are configured at a lower level (merchant account, store, or individual terminal).  * To change a parameter value, include the full object that contains the parameter, even if you don&#39;t want to change all parameters in the object. * To restore a parameter value inherited from the Adyen PSP level, include the full object that contains the parameter, and specify an empty value for the parameter or omit the parameter. * Objects that are not included in the request are not updated.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal settings read and write  For [sensitive terminal settings](https://docs.adyen.com/point-of-sale/automating-terminal-management/configure-terminals-api#sensitive-terminal-settings), your API credential must have the following role: * Management API—Terminal settings Advanced read and write

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

let apiInstance = new ManagementApi.TerminalSettingsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'terminalSettings': new ManagementApi.TerminalSettings() // TerminalSettings | 
};
apiInstance.patchCompaniesCompanyIdTerminalSettings(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **terminalSettings** | [**TerminalSettings**](TerminalSettings.md)|  | [optional] 

### Return type

[**TerminalSettings**](TerminalSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


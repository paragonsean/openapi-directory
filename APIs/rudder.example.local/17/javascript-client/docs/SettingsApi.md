# RudderApi.SettingsApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllSettings**](SettingsApi.md#getAllSettings) | **GET** /settings | List all settings
[**getAllowedNetworks**](SettingsApi.md#getAllowedNetworks) | **GET** /settings/allowed_networks/{nodeId} | Get allowed networks for a policy server
[**getSetting**](SettingsApi.md#getSetting) | **GET** /settings/{settingId} | Get the value of a setting
[**modifyAllowedNetworks**](SettingsApi.md#modifyAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId}/diff | Modify allowed networks for a policy server
[**modifySetting**](SettingsApi.md#modifySetting) | **POST** /settings/{settingId} | Set the value of a setting
[**setAllowedNetworks**](SettingsApi.md#setAllowedNetworks) | **POST** /settings/allowed_networks/{nodeId} | Set allowed networks for a policy server



## getAllSettings

> GetAllSettings200Response getAllSettings()

List all settings

Get the current value of all the settings

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SettingsApi();
apiInstance.getAllSettings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllSettings200Response**](GetAllSettings200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllowedNetworks

> GetAllowedNetworks200Response getAllowedNetworks(nodeId)

Get allowed networks for a policy server

Get the list of allowed networks for a policy server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SettingsApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Policy server ID for which you want to manage allowed networks.
apiInstance.getAllowedNetworks(nodeId, (error, data, response) => {
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
 **nodeId** | **String**| Policy server ID for which you want to manage allowed networks. | 

### Return type

[**GetAllowedNetworks200Response**](GetAllowedNetworks200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSetting

> GetSetting200Response getSetting(settingId)

Get the value of a setting

Get the current value of a specific setting

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SettingsApi();
let settingId = "global_policy_mode"; // String | Id of the setting to set
apiInstance.getSetting(settingId, (error, data, response) => {
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
 **settingId** | **String**| Id of the setting to set | 

### Return type

[**GetSetting200Response**](GetSetting200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modifyAllowedNetworks

> ModifyAllowedNetworks200Response modifyAllowedNetworks(nodeId, modifyAllowedNetworksRequest)

Modify allowed networks for a policy server

Add or delete allowed networks for a policy server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SettingsApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Policy server ID for which you want to manage allowed networks.
let modifyAllowedNetworksRequest = new RudderApi.ModifyAllowedNetworksRequest(); // ModifyAllowedNetworksRequest | 
apiInstance.modifyAllowedNetworks(nodeId, modifyAllowedNetworksRequest, (error, data, response) => {
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
 **nodeId** | **String**| Policy server ID for which you want to manage allowed networks. | 
 **modifyAllowedNetworksRequest** | [**ModifyAllowedNetworksRequest**](ModifyAllowedNetworksRequest.md)|  | 

### Return type

[**ModifyAllowedNetworks200Response**](ModifyAllowedNetworks200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modifySetting

> ModifySetting200Response modifySetting(settingId, modifySettingRequest)

Set the value of a setting

Set the current value of a specific setting

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SettingsApi();
let settingId = "global_policy_mode"; // String | Id of the setting to set
let modifySettingRequest = new RudderApi.ModifySettingRequest(); // ModifySettingRequest | 
apiInstance.modifySetting(settingId, modifySettingRequest, (error, data, response) => {
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
 **settingId** | **String**| Id of the setting to set | 
 **modifySettingRequest** | [**ModifySettingRequest**](ModifySettingRequest.md)|  | 

### Return type

[**ModifySetting200Response**](ModifySetting200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setAllowedNetworks

> SetAllowedNetworks200Response setAllowedNetworks(nodeId, setAllowedNetworksRequest)

Set allowed networks for a policy server

Set the list of allowed networks for a policy server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SettingsApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Policy server ID for which you want to manage allowed networks.
let setAllowedNetworksRequest = new RudderApi.SetAllowedNetworksRequest(); // SetAllowedNetworksRequest | 
apiInstance.setAllowedNetworks(nodeId, setAllowedNetworksRequest, (error, data, response) => {
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
 **nodeId** | **String**| Policy server ID for which you want to manage allowed networks. | 
 **setAllowedNetworksRequest** | [**SetAllowedNetworksRequest**](SetAllowedNetworksRequest.md)|  | 

### Return type

[**SetAllowedNetworks200Response**](SetAllowedNetworks200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# JellyfinApi.PluginsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disablePlugin**](PluginsApi.md#disablePlugin) | **POST** /Plugins/{pluginId}/{version}/Disable | Disable a plugin.
[**enablePlugin**](PluginsApi.md#enablePlugin) | **POST** /Plugins/{pluginId}/{version}/Enable | Enables a disabled plugin.
[**getPluginConfiguration**](PluginsApi.md#getPluginConfiguration) | **GET** /Plugins/{pluginId}/Configuration | Gets plugin configuration.
[**getPluginImage**](PluginsApi.md#getPluginImage) | **GET** /Plugins/{pluginId}/{version}/Image | Gets a plugin&#39;s image.
[**getPluginManifest**](PluginsApi.md#getPluginManifest) | **POST** /Plugins/{pluginId}/Manifest | Gets a plugin&#39;s manifest.
[**getPlugins**](PluginsApi.md#getPlugins) | **GET** /Plugins | Gets a list of currently installed plugins.
[**uninstallPlugin**](PluginsApi.md#uninstallPlugin) | **DELETE** /Plugins/{pluginId} | Uninstalls a plugin.
[**uninstallPluginByVersion**](PluginsApi.md#uninstallPluginByVersion) | **DELETE** /Plugins/{pluginId}/{version} | Uninstalls a plugin by version.
[**updatePluginConfiguration**](PluginsApi.md#updatePluginConfiguration) | **POST** /Plugins/{pluginId}/Configuration | Updates plugin configuration.
[**updatePluginSecurityInfo**](PluginsApi.md#updatePluginSecurityInfo) | **POST** /Plugins/SecurityInfo | Updates plugin security info.



## disablePlugin

> disablePlugin(pluginId, version)

Disable a plugin.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
let version = new JellyfinApi.Version(); // Version | Plugin version.
apiInstance.disablePlugin(pluginId, version, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 
 **version** | [**Version**](.md)| Plugin version. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## enablePlugin

> enablePlugin(pluginId, version)

Enables a disabled plugin.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
let version = new JellyfinApi.Version(); // Version | Plugin version.
apiInstance.enablePlugin(pluginId, version, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 
 **version** | [**Version**](.md)| Plugin version. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPluginConfiguration

> Object getPluginConfiguration(pluginId)

Gets plugin configuration.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
apiInstance.getPluginConfiguration(pluginId, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 

### Return type

**Object**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPluginImage

> File getPluginImage(pluginId, version)

Gets a plugin&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
let version = new JellyfinApi.Version(); // Version | Plugin version.
apiInstance.getPluginImage(pluginId, version, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 
 **version** | [**Version**](.md)| Plugin version. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPluginManifest

> getPluginManifest(pluginId)

Gets a plugin&#39;s manifest.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
apiInstance.getPluginManifest(pluginId, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPlugins

> [PluginInfo] getPlugins()

Gets a list of currently installed plugins.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
apiInstance.getPlugins((error, data, response) => {
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

[**[PluginInfo]**](PluginInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## uninstallPlugin

> uninstallPlugin(pluginId)

Uninstalls a plugin.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
apiInstance.uninstallPlugin(pluginId, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## uninstallPluginByVersion

> uninstallPluginByVersion(pluginId, version)

Uninstalls a plugin by version.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
let version = new JellyfinApi.Version(); // Version | Plugin version.
apiInstance.uninstallPluginByVersion(pluginId, version, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 
 **version** | [**Version**](.md)| Plugin version. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## updatePluginConfiguration

> updatePluginConfiguration(pluginId)

Updates plugin configuration.

Accepts plugin configuration as JSON body.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginId = "pluginId_example"; // String | Plugin id.
apiInstance.updatePluginConfiguration(pluginId, (error, data, response) => {
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
 **pluginId** | **String**| Plugin id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## updatePluginSecurityInfo

> updatePluginSecurityInfo(pluginSecurityInfo)

Updates plugin security info.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PluginsApi();
let pluginSecurityInfo = new JellyfinApi.PluginSecurityInfo(); // PluginSecurityInfo | Plugin security info.
apiInstance.updatePluginSecurityInfo(pluginSecurityInfo, (error, data, response) => {
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
 **pluginSecurityInfo** | [**PluginSecurityInfo**](PluginSecurityInfo.md)| Plugin security info. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


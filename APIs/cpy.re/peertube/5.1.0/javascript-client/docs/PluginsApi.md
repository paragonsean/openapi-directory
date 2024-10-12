# PeerTube.PluginsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPlugin**](PluginsApi.md#addPlugin) | **POST** /api/v1/plugins/install | Install a plugin
[**apiV1PluginsNpmNamePublicSettingsGet**](PluginsApi.md#apiV1PluginsNpmNamePublicSettingsGet) | **GET** /api/v1/plugins/{npmName}/public-settings | Get a plugin&#39;s public settings
[**apiV1PluginsNpmNameRegisteredSettingsGet**](PluginsApi.md#apiV1PluginsNpmNameRegisteredSettingsGet) | **GET** /api/v1/plugins/{npmName}/registered-settings | Get a plugin&#39;s registered settings
[**apiV1PluginsNpmNameSettingsPut**](PluginsApi.md#apiV1PluginsNpmNameSettingsPut) | **PUT** /api/v1/plugins/{npmName}/settings | Set a plugin&#39;s settings
[**getAvailablePlugins**](PluginsApi.md#getAvailablePlugins) | **GET** /api/v1/plugins/available | List available plugins
[**getPlugin**](PluginsApi.md#getPlugin) | **GET** /api/v1/plugins/{npmName} | Get a plugin
[**getPlugins**](PluginsApi.md#getPlugins) | **GET** /api/v1/plugins | List plugins
[**uninstallPlugin**](PluginsApi.md#uninstallPlugin) | **POST** /api/v1/plugins/uninstall | Uninstall a plugin
[**updatePlugin**](PluginsApi.md#updatePlugin) | **POST** /api/v1/plugins/update | Update a plugin



## addPlugin

> addPlugin(opts)

Install a plugin

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let opts = {
  'addPluginRequest': new PeerTube.AddPluginRequest() // AddPluginRequest | 
};
apiInstance.addPlugin(opts, (error, data, response) => {
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
 **addPluginRequest** | [**AddPluginRequest**](AddPluginRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV1PluginsNpmNamePublicSettingsGet

> {String: Object} apiV1PluginsNpmNamePublicSettingsGet(npmName)

Get a plugin&#39;s public settings

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.PluginsApi();
let npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
apiInstance.apiV1PluginsNpmNamePublicSettingsGet(npmName, (error, data, response) => {
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
 **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1PluginsNpmNameRegisteredSettingsGet

> {String: Object} apiV1PluginsNpmNameRegisteredSettingsGet(npmName)

Get a plugin&#39;s registered settings

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
apiInstance.apiV1PluginsNpmNameRegisteredSettingsGet(npmName, (error, data, response) => {
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
 **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | 

### Return type

**{String: Object}**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1PluginsNpmNameSettingsPut

> apiV1PluginsNpmNameSettingsPut(npmName, opts)

Set a plugin&#39;s settings

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
let opts = {
  'apiV1PluginsNpmNameSettingsPutRequest': new PeerTube.ApiV1PluginsNpmNameSettingsPutRequest() // ApiV1PluginsNpmNameSettingsPutRequest | 
};
apiInstance.apiV1PluginsNpmNameSettingsPut(npmName, opts, (error, data, response) => {
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
 **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | 
 **apiV1PluginsNpmNameSettingsPutRequest** | [**ApiV1PluginsNpmNameSettingsPutRequest**](ApiV1PluginsNpmNameSettingsPutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getAvailablePlugins

> PluginResponse getAvailablePlugins(opts)

List available plugins

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let opts = {
  'search': "search_example", // String | 
  'pluginType': 56, // Number | 
  'currentPeerTubeEngine': "currentPeerTubeEngine_example", // String | 
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.getAvailablePlugins(opts, (error, data, response) => {
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
 **search** | **String**|  | [optional] 
 **pluginType** | **Number**|  | [optional] 
 **currentPeerTubeEngine** | **String**|  | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**PluginResponse**](PluginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlugin

> Plugin getPlugin(npmName)

Get a plugin

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
apiInstance.getPlugin(npmName, (error, data, response) => {
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
 **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlugins

> PluginResponse getPlugins(opts)

List plugins

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let opts = {
  'pluginType': 56, // Number | 
  'uninstalled': true, // Boolean | 
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.getPlugins(opts, (error, data, response) => {
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
 **pluginType** | **Number**|  | [optional] 
 **uninstalled** | **Boolean**|  | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**PluginResponse**](PluginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uninstallPlugin

> uninstallPlugin(opts)

Uninstall a plugin

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let opts = {
  'uninstallPluginRequest': new PeerTube.UninstallPluginRequest() // UninstallPluginRequest | 
};
apiInstance.uninstallPlugin(opts, (error, data, response) => {
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
 **uninstallPluginRequest** | [**UninstallPluginRequest**](UninstallPluginRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updatePlugin

> updatePlugin(opts)

Update a plugin

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.PluginsApi();
let opts = {
  'addPluginRequest': new PeerTube.AddPluginRequest() // AddPluginRequest | 
};
apiInstance.updatePlugin(opts, (error, data, response) => {
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
 **addPluginRequest** | [**AddPluginRequest**](AddPluginRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


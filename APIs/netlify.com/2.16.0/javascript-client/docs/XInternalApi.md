# NetlifysApiDocumentation.XInternalApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPluginRun**](XInternalApi.md#createPluginRun) | **POST** /deploys/{deploy_id}/plugin_runs | 
[**getLatestPluginRuns**](XInternalApi.md#getLatestPluginRuns) | **GET** /sites/{site_id}/plugin_runs/latest | 
[**updatePlugin**](XInternalApi.md#updatePlugin) | **PUT** /sites/{site_id}/plugins/{package} | 



## createPluginRun

> PluginRun createPluginRun(deployId, opts)



This is an internal-only endpoint.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.XInternalApi();
let deployId = "deployId_example"; // String | 
let opts = {
  'pluginRun': new NetlifysApiDocumentation.PluginRunData() // PluginRunData | 
};
apiInstance.createPluginRun(deployId, opts, (error, data, response) => {
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
 **deployId** | **String**|  | 
 **pluginRun** | [**PluginRunData**](PluginRunData.md)|  | [optional] 

### Return type

[**PluginRun**](PluginRun.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLatestPluginRuns

> [PluginRun] getLatestPluginRuns(siteId, packages, opts)



This is an internal-only endpoint.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.XInternalApi();
let siteId = "siteId_example"; // String | 
let packages = ["null"]; // [String] | 
let opts = {
  'state': "state_example" // String | 
};
apiInstance.getLatestPluginRuns(siteId, packages, opts, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **packages** | [**[String]**](String.md)|  | 
 **state** | **String**|  | [optional] 

### Return type

[**[PluginRun]**](PluginRun.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePlugin

> Plugin updatePlugin(siteId, _package, opts)



This is an internal-only endpoint.

### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.XInternalApi();
let siteId = "siteId_example"; // String | 
let _package = "_package_example"; // String | 
let opts = {
  'pluginParams': new NetlifysApiDocumentation.PluginParams() // PluginParams | 
};
apiInstance.updatePlugin(siteId, _package, opts, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **_package** | **String**|  | 
 **pluginParams** | [**PluginParams**](PluginParams.md)|  | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


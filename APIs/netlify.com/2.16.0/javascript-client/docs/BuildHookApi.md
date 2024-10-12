# NetlifysApiDocumentation.BuildHookApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSiteBuildHook**](BuildHookApi.md#createSiteBuildHook) | **POST** /sites/{site_id}/build_hooks | 
[**deleteSiteBuildHook**](BuildHookApi.md#deleteSiteBuildHook) | **DELETE** /sites/{site_id}/build_hooks/{id} | 
[**getSiteBuildHook**](BuildHookApi.md#getSiteBuildHook) | **GET** /sites/{site_id}/build_hooks/{id} | 
[**listSiteBuildHooks**](BuildHookApi.md#listSiteBuildHooks) | **GET** /sites/{site_id}/build_hooks | 
[**updateSiteBuildHook**](BuildHookApi.md#updateSiteBuildHook) | **PUT** /sites/{site_id}/build_hooks/{id} | 



## createSiteBuildHook

> BuildHook createSiteBuildHook(siteId, buildHook)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.BuildHookApi();
let siteId = "siteId_example"; // String | 
let buildHook = new NetlifysApiDocumentation.BuildHookSetup(); // BuildHookSetup | 
apiInstance.createSiteBuildHook(siteId, buildHook, (error, data, response) => {
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
 **buildHook** | [**BuildHookSetup**](BuildHookSetup.md)|  | 

### Return type

[**BuildHook**](BuildHook.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSiteBuildHook

> deleteSiteBuildHook(siteId, id)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.BuildHookApi();
let siteId = "siteId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteSiteBuildHook(siteId, id, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteBuildHook

> BuildHook getSiteBuildHook(siteId, id)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.BuildHookApi();
let siteId = "siteId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getSiteBuildHook(siteId, id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**BuildHook**](BuildHook.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSiteBuildHooks

> [BuildHook] listSiteBuildHooks(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.BuildHookApi();
let siteId = "siteId_example"; // String | 
apiInstance.listSiteBuildHooks(siteId, (error, data, response) => {
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

### Return type

[**[BuildHook]**](BuildHook.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSiteBuildHook

> updateSiteBuildHook(siteId, id, buildHook)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.BuildHookApi();
let siteId = "siteId_example"; // String | 
let id = "id_example"; // String | 
let buildHook = new NetlifysApiDocumentation.BuildHookSetup(); // BuildHookSetup | 
apiInstance.updateSiteBuildHook(siteId, id, buildHook, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **id** | **String**|  | 
 **buildHook** | [**BuildHookSetup**](BuildHookSetup.md)|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


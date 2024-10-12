# OtoroshiAdminApi.SnowmonkeyApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSnowMonkeyConfig**](SnowmonkeyApi.md#getSnowMonkeyConfig) | **GET** /api/snowmonkey/config | Get current Snow Monkey config
[**getSnowMonkeyOutages**](SnowmonkeyApi.md#getSnowMonkeyOutages) | **GET** /api/snowmonkey/outages | Get all current Snow Monkey ourages
[**patchSnowMonkey**](SnowmonkeyApi.md#patchSnowMonkey) | **PATCH** /api/snowmonkey/config | Update current Snow Monkey config
[**resetSnowMonkey**](SnowmonkeyApi.md#resetSnowMonkey) | **DELETE** /api/snowmonkey/outages | Reset Snow Monkey Outages for the day
[**startSnowMonkey**](SnowmonkeyApi.md#startSnowMonkey) | **POST** /api/snowmonkey/_start | Start the Snow Monkey
[**stopSnowMonkey**](SnowmonkeyApi.md#stopSnowMonkey) | **POST** /api/snowmonkey/_stop | Stop the Snow Monkey
[**updateSnowMonkey**](SnowmonkeyApi.md#updateSnowMonkey) | **PUT** /api/snowmonkey/config | Update current Snow Monkey config



## getSnowMonkeyConfig

> SnowMonkeyConfig getSnowMonkeyConfig()

Get current Snow Monkey config

Get current Snow Monkey config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.SnowmonkeyApi();
apiInstance.getSnowMonkeyConfig((error, data, response) => {
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

[**SnowMonkeyConfig**](SnowMonkeyConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSnowMonkeyOutages

> [Outage] getSnowMonkeyOutages()

Get all current Snow Monkey ourages

Get all current Snow Monkey ourages

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.SnowmonkeyApi();
apiInstance.getSnowMonkeyOutages((error, data, response) => {
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

[**[Outage]**](Outage.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSnowMonkey

> SnowMonkeyConfig patchSnowMonkey(opts)

Update current Snow Monkey config

Update current Snow Monkey config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.SnowmonkeyApi();
let opts = {
  'group': new OtoroshiAdminApi.Group() // Group | 
};
apiInstance.patchSnowMonkey(opts, (error, data, response) => {
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
 **group** | [**Group**](Group.md)|  | [optional] 

### Return type

[**SnowMonkeyConfig**](SnowMonkeyConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetSnowMonkey

> Done resetSnowMonkey()

Reset Snow Monkey Outages for the day

Reset Snow Monkey Outages for the day

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.SnowmonkeyApi();
apiInstance.resetSnowMonkey((error, data, response) => {
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

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startSnowMonkey

> Done startSnowMonkey()

Start the Snow Monkey

Start the Snow Monkey

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.SnowmonkeyApi();
apiInstance.startSnowMonkey((error, data, response) => {
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

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopSnowMonkey

> Done stopSnowMonkey()

Stop the Snow Monkey

Stop the Snow Monkey

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.SnowmonkeyApi();
apiInstance.stopSnowMonkey((error, data, response) => {
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

[**Done**](Done.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSnowMonkey

> SnowMonkeyConfig updateSnowMonkey(opts)

Update current Snow Monkey config

Update current Snow Monkey config

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.SnowmonkeyApi();
let opts = {
  'group': new OtoroshiAdminApi.Group() // Group | 
};
apiInstance.updateSnowMonkey(opts, (error, data, response) => {
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
 **group** | [**Group**](Group.md)|  | [optional] 

### Return type

[**SnowMonkeyConfig**](SnowMonkeyConfig.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


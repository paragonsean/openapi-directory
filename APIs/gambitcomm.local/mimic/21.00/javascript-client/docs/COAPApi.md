# MimicRestApi.COAPApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolCoapGetArgs**](COAPApi.md#protocolCoapGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/coap/get/args | Show the agent&#39;s COAP argument structure
[**protocolCoapGetConfig**](COAPApi.md#protocolCoapGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/coap/get/config | Show the agent&#39;s COAP configuration
[**protocolCoapGetStatistics**](COAPApi.md#protocolCoapGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/coap/get/statistics | Show the agent&#39;s COAP statistics
[**protocolCoapGetStatsHdr**](COAPApi.md#protocolCoapGetStatsHdr) | **GET** /mimic/protocol/msg/coap/get/stats_hdr | Show the COAP statistics headers
[**protocolCoapGetTrace**](COAPApi.md#protocolCoapGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/coap/get/trace | Show the agent&#39;s COAP traffic tracing
[**protocolCoapSetConfig**](COAPApi.md#protocolCoapSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/coap/set/config/{argument}/{value} | Set the agent&#39;s COAP configuration
[**protocolCoapSetTrace**](COAPApi.md#protocolCoapSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/coap/set/trace/{enableOrNot} | Set the agent&#39;s COAP traffic tracing



## protocolCoapGetArgs

> Object protocolCoapGetArgs(agentNum)

Show the agent&#39;s COAP argument structure

Agent&#39;s COAP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.COAPApi();
let agentNum = 56; // Number | Agent to show the COAP argument structure
apiInstance.protocolCoapGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the COAP argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolCoapGetConfig

> ConfigCOAP protocolCoapGetConfig(agentNum)

Show the agent&#39;s COAP configuration

Agent&#39;s COAP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.COAPApi();
let agentNum = 56; // Number | Agent to show the COAP configuration
apiInstance.protocolCoapGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the COAP configuration | 

### Return type

[**ConfigCOAP**](ConfigCOAP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolCoapGetStatistics

> [Number] protocolCoapGetStatistics(agentNum)

Show the agent&#39;s COAP statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.COAPApi();
let agentNum = 56; // Number | Agent to show COAP statistics
apiInstance.protocolCoapGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show COAP statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolCoapGetStatsHdr

> [String] protocolCoapGetStatsHdr()

Show the COAP statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.COAPApi();
apiInstance.protocolCoapGetStatsHdr((error, data, response) => {
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

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolCoapGetTrace

> ConfigCOAP protocolCoapGetTrace(agentNum)

Show the agent&#39;s COAP traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.COAPApi();
let agentNum = 56; // Number | Agent to show whether COAP tracing is enabled
apiInstance.protocolCoapGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether COAP tracing is enabled | 

### Return type

[**ConfigCOAP**](ConfigCOAP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolCoapSetConfig

> String protocolCoapSetConfig(agentNum, argument, value)

Set the agent&#39;s COAP configuration

Agent&#39;s COAP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.COAPApi();
let agentNum = 56; // Number | Agent to set the COAP configuration
let argument = "argument_example"; // String | Parameter to set the COAP configuration
let value = "value_example"; // String | Value to set the COAP configuration
apiInstance.protocolCoapSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the COAP configuration | 
 **argument** | **String**| Parameter to set the COAP configuration | 
 **value** | **String**| Value to set the COAP configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolCoapSetTrace

> String protocolCoapSetTrace(agentNum, enableOrNot)

Set the agent&#39;s COAP traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.COAPApi();
let agentNum = 56; // Number | Agent to set the COAP tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the COAP tracing
apiInstance.protocolCoapSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the COAP tracing | 
 **enableOrNot** | **String**| Value to set the COAP tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


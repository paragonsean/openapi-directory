# MimicRestApi.SFLOWApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolSflowGetArgs**](SFLOWApi.md#protocolSflowGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/args | Show the agent&#39;s SFLOW argument structure
[**protocolSflowGetConfig**](SFLOWApi.md#protocolSflowGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/config | Show the agent&#39;s SFLOW configuration
[**protocolSflowGetStatistics**](SFLOWApi.md#protocolSflowGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/statistics | Show the agent&#39;s SFLOW statistics
[**protocolSflowGetStatsHdr**](SFLOWApi.md#protocolSflowGetStatsHdr) | **GET** /mimic/protocol/msg/sflow/get/stats_hdr | Show the SFLOW statistics headers
[**protocolSflowGetTrace**](SFLOWApi.md#protocolSflowGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/trace | Show the agent&#39;s SFLOW traffic tracing
[**protocolSflowHalt**](SFLOWApi.md#protocolSflowHalt) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/halt | Halt SFLOW traffic
[**protocolSflowReload**](SFLOWApi.md#protocolSflowReload) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/reload | Reload SFLOW configuration before resuming traffic
[**protocolSflowResume**](SFLOWApi.md#protocolSflowResume) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/resume | Resuming traffic
[**protocolSflowSetConfig**](SFLOWApi.md#protocolSflowSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/set/config/{argument}/{value} | Set the agent&#39;s SFLOW configuration
[**protocolSflowSetTrace**](SFLOWApi.md#protocolSflowSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/set/trace/{enableOrNot} | Set the agent&#39;s SFLOW traffic tracing



## protocolSflowGetArgs

> Object protocolSflowGetArgs(agentNum)

Show the agent&#39;s SFLOW argument structure

Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to show the SFLOW argument structure
apiInstance.protocolSflowGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SFLOW argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowGetConfig

> ConfigSFLOW protocolSflowGetConfig(agentNum)

Show the agent&#39;s SFLOW configuration

Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to show the SFLOW configuration
apiInstance.protocolSflowGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SFLOW configuration | 

### Return type

[**ConfigSFLOW**](ConfigSFLOW.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowGetStatistics

> [Number] protocolSflowGetStatistics(agentNum)

Show the agent&#39;s SFLOW statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to show SFLOW statistics
apiInstance.protocolSflowGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show SFLOW statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowGetStatsHdr

> [String] protocolSflowGetStatsHdr()

Show the SFLOW statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
apiInstance.protocolSflowGetStatsHdr((error, data, response) => {
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


## protocolSflowGetTrace

> ConfigSFLOW protocolSflowGetTrace(agentNum)

Show the agent&#39;s SFLOW traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to show whether SFLOW tracing is enabled
apiInstance.protocolSflowGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether SFLOW tracing is enabled | 

### Return type

[**ConfigSFLOW**](ConfigSFLOW.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowHalt

> String protocolSflowHalt(agentNum)

Halt SFLOW traffic

Halt SFLOW traffic

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to set the SFLOW
apiInstance.protocolSflowHalt(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SFLOW | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowReload

> String protocolSflowReload(agentNum)

Reload SFLOW configuration before resuming traffic

Reload SFLOW configuration before resuming traffic

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to set the SFLOW
apiInstance.protocolSflowReload(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SFLOW | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowResume

> String protocolSflowResume(agentNum)

Resuming traffic

Resuming traffic

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to set the SFLOW
apiInstance.protocolSflowResume(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SFLOW | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowSetConfig

> String protocolSflowSetConfig(agentNum, argument, value)

Set the agent&#39;s SFLOW configuration

Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to set the SFLOW configuration
let argument = "argument_example"; // String | Parameter to set the SFLOW configuration
let value = "value_example"; // String | Value to set the SFLOW configuration
apiInstance.protocolSflowSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SFLOW configuration | 
 **argument** | **String**| Parameter to set the SFLOW configuration | 
 **value** | **String**| Value to set the SFLOW configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSflowSetTrace

> String protocolSflowSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SFLOW traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SFLOWApi();
let agentNum = 56; // Number | Agent to set the SFLOW tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the SFLOW tracing
apiInstance.protocolSflowSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SFLOW tracing | 
 **enableOrNot** | **String**| Value to set the SFLOW tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


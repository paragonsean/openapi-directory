# MimicRestApi.TODApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolTodGetArgs**](TODApi.md#protocolTodGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/args | Show the agent&#39;s TOD argument structure
[**protocolTodGetConfig**](TODApi.md#protocolTodGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/config | Show the agent&#39;s TOD configuration
[**protocolTodGetStatistics**](TODApi.md#protocolTodGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/statistics | Show the agent&#39;s TOD statistics
[**protocolTodGetStatsHdr**](TODApi.md#protocolTodGetStatsHdr) | **GET** /mimic/protocol/msg/tod/get/stats_hdr | Show the TOD statistics headers
[**protocolTodGetTrace**](TODApi.md#protocolTodGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/trace | Show the agent&#39;s TOD traffic tracing
[**protocolTodGettime**](TODApi.md#protocolTodGettime) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/gettime/server/{serverAddr}/port/{portNum}/script/{scriptName}/timeout/{timeSec}/retries/{numRetries} | Retrieve TOD time
[**protocolTodSetConfig**](TODApi.md#protocolTodSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tod/set/config/{argument}/{value} | Set the agent&#39;s TOD configuration
[**protocolTodSetTrace**](TODApi.md#protocolTodSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tod/set/trace/{enableOrNot} | Set the agent&#39;s TOD traffic tracing



## protocolTodGetArgs

> Object protocolTodGetArgs(agentNum)

Show the agent&#39;s TOD argument structure

Agent&#39;s TOD configuration

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
let agentNum = 56; // Number | Agent to show the TOD argument structure
apiInstance.protocolTodGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the TOD argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTodGetConfig

> ConfigTOD protocolTodGetConfig(agentNum)

Show the agent&#39;s TOD configuration

Agent&#39;s TOD configuration

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
let agentNum = 56; // Number | Agent to show the TOD configuration
apiInstance.protocolTodGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the TOD configuration | 

### Return type

[**ConfigTOD**](ConfigTOD.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTodGetStatistics

> [Number] protocolTodGetStatistics(agentNum)

Show the agent&#39;s TOD statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
let agentNum = 56; // Number | Agent to show TOD statistics
apiInstance.protocolTodGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TOD statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTodGetStatsHdr

> [String] protocolTodGetStatsHdr()

Show the TOD statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
apiInstance.protocolTodGetStatsHdr((error, data, response) => {
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


## protocolTodGetTrace

> ConfigTOD protocolTodGetTrace(agentNum)

Show the agent&#39;s TOD traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
let agentNum = 56; // Number | Agent to show whether TOD tracing is enabled
apiInstance.protocolTodGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether TOD tracing is enabled | 

### Return type

[**ConfigTOD**](ConfigTOD.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTodGettime

> [String] protocolTodGettime(agentNum, serverAddr, portNum, scriptName, timeSec, numRetries)

Retrieve TOD time

Retrive time from server

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
let agentNum = 56; // Number | Agent to show TOD return
let serverAddr = "serverAddr_example"; // String | serverAddr
let portNum = 56; // Number | portNum
let scriptName = "scriptName_example"; // String | scriptName
let timeSec = 56; // Number | timeSec
let numRetries = 56; // Number | numRetries
apiInstance.protocolTodGettime(agentNum, serverAddr, portNum, scriptName, timeSec, numRetries, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TOD return | 
 **serverAddr** | **String**| serverAddr | 
 **portNum** | **Number**| portNum | 
 **scriptName** | **String**| scriptName | 
 **timeSec** | **Number**| timeSec | 
 **numRetries** | **Number**| numRetries | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTodSetConfig

> String protocolTodSetConfig(agentNum, argument, value)

Set the agent&#39;s TOD configuration

Agent&#39;s TOD configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
let agentNum = 56; // Number | Agent to set the TOD configuration
let argument = "argument_example"; // String | Parameter to set the TOD configuration
let value = "value_example"; // String | Value to set the TOD configuration
apiInstance.protocolTodSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the TOD configuration | 
 **argument** | **String**| Parameter to set the TOD configuration | 
 **value** | **String**| Value to set the TOD configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTodSetTrace

> String protocolTodSetTrace(agentNum, enableOrNot)

Set the agent&#39;s TOD traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TODApi();
let agentNum = 56; // Number | Agent to set the TOD tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the TOD tracing
apiInstance.protocolTodSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the TOD tracing | 
 **enableOrNot** | **String**| Value to set the TOD tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# MimicRestApi.SYSLOGApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolSyslogGetArgs**](SYSLOGApi.md#protocolSyslogGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/args | Show the agent&#39;s SYSLOG argument structure
[**protocolSyslogGetAttr**](SYSLOGApi.md#protocolSyslogGetAttr) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/{attr} | Show the outgoing message&#39;s attributes
[**protocolSyslogGetConfig**](SYSLOGApi.md#protocolSyslogGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/config | Show the agent&#39;s SYSLOG configuration
[**protocolSyslogGetStatistics**](SYSLOGApi.md#protocolSyslogGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/statistics | Show the agent&#39;s SYSLOG statistics
[**protocolSyslogGetStatsHdr**](SYSLOGApi.md#protocolSyslogGetStatsHdr) | **GET** /mimic/protocol/msg/syslog/get/stats_hdr | Show the SYSLOG statistics headers
[**protocolSyslogGetTrace**](SYSLOGApi.md#protocolSyslogGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/trace | Show the agent&#39;s SYSLOG traffic tracing
[**protocolSyslogSend**](SYSLOGApi.md#protocolSyslogSend) | **POST** /mimic/agent/{agentNum}/protocol/msg/syslog/send/{pri} | Set the agent&#39;s SYSLOG traffic tracing
[**protocolSyslogSetAttr**](SYSLOGApi.md#protocolSyslogSetAttr) | **PUT** /mimic/agent/{agentNum}/protocol/msg/syslog/set/{attr}/{value} | Set the outgoing message&#39;s attributes
[**protocolSyslogSetConfig**](SYSLOGApi.md#protocolSyslogSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/syslog/set/config/{argument}/{value} | Set the agent&#39;s SYSLOG configuration
[**protocolSyslogSetTrace**](SYSLOGApi.md#protocolSyslogSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/syslog/set/trace/{enableOrNot} | Set the agent&#39;s SYSLOG traffic tracing



## protocolSyslogGetArgs

> Object protocolSyslogGetArgs(agentNum)

Show the agent&#39;s SYSLOG argument structure

Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to show the SYSLOG argument structure
apiInstance.protocolSyslogGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SYSLOG argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSyslogGetAttr

> String protocolSyslogGetAttr(agentNum, attr)

Show the outgoing message&#39;s attributes

Attribute can be server , sequence , separator , hostname , timestamp

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to set the SYSLOG tracing
let attr = "attr_example"; // String | Attribute
apiInstance.protocolSyslogGetAttr(agentNum, attr, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SYSLOG tracing | 
 **attr** | **String**| Attribute | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSyslogGetConfig

> ConfigSYSLOG protocolSyslogGetConfig(agentNum)

Show the agent&#39;s SYSLOG configuration

Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to show the SYSLOG configuration
apiInstance.protocolSyslogGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SYSLOG configuration | 

### Return type

[**ConfigSYSLOG**](ConfigSYSLOG.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSyslogGetStatistics

> [Number] protocolSyslogGetStatistics(agentNum)

Show the agent&#39;s SYSLOG statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to show SYSLOG statistics
apiInstance.protocolSyslogGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show SYSLOG statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSyslogGetStatsHdr

> [String] protocolSyslogGetStatsHdr()

Show the SYSLOG statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
apiInstance.protocolSyslogGetStatsHdr((error, data, response) => {
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


## protocolSyslogGetTrace

> ConfigSYSLOG protocolSyslogGetTrace(agentNum)

Show the agent&#39;s SYSLOG traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to show whether SYSLOG tracing is enabled
apiInstance.protocolSyslogGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether SYSLOG tracing is enabled | 

### Return type

[**ConfigSYSLOG**](ConfigSYSLOG.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSyslogSend

> String protocolSyslogSend(agentNum, pri, syslogMsg)

Set the agent&#39;s SYSLOG traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to set the SYSLOG tracing
let pri = 56; // Number | Message Priority
let syslogMsg = new MimicRestApi.SyslogMsg(); // SyslogMsg | 
apiInstance.protocolSyslogSend(agentNum, pri, syslogMsg, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SYSLOG tracing | 
 **pri** | **Number**| Message Priority | 
 **syslogMsg** | [**SyslogMsg**](SyslogMsg.md)|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## protocolSyslogSetAttr

> String protocolSyslogSetAttr(agentNum, attr, value)

Set the outgoing message&#39;s attributes

Attribute can be server , sequence , separator , hostname , timestamp

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to set the SYSLOG tracing
let attr = "attr_example"; // String | Attribute
let value = "value_example"; // String | 
apiInstance.protocolSyslogSetAttr(agentNum, attr, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SYSLOG tracing | 
 **attr** | **String**| Attribute | 
 **value** | **String**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSyslogSetConfig

> String protocolSyslogSetConfig(agentNum, argument, value)

Set the agent&#39;s SYSLOG configuration

Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to set the SYSLOG configuration
let argument = "argument_example"; // String | Parameter to set the SYSLOG configuration
let value = "value_example"; // String | Value to set the SYSLOG configuration
apiInstance.protocolSyslogSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SYSLOG configuration | 
 **argument** | **String**| Parameter to set the SYSLOG configuration | 
 **value** | **String**| Value to set the SYSLOG configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSyslogSetTrace

> String protocolSyslogSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SYSLOG traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SYSLOGApi();
let agentNum = 56; // Number | Agent to set the SYSLOG tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the SYSLOG tracing
apiInstance.protocolSyslogSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SYSLOG tracing | 
 **enableOrNot** | **String**| Value to set the SYSLOG tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


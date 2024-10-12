# MimicRestApi.PROXYApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolProxyGetArgs**](PROXYApi.md#protocolProxyGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/args | Show the agent&#39;s PROXY argument structure
[**protocolProxyGetConfig**](PROXYApi.md#protocolProxyGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/config | Show the agent&#39;s PROXY configuration
[**protocolProxyGetStatistics**](PROXYApi.md#protocolProxyGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/statistics | Show the agent&#39;s PROXY statistics
[**protocolProxyGetStatsHdr**](PROXYApi.md#protocolProxyGetStatsHdr) | **GET** /mimic/protocol/msg/proxy/get/stats_hdr | Show the PROXY statistics headers
[**protocolProxyGetTrace**](PROXYApi.md#protocolProxyGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/trace | Show the agent&#39;s PROXY traffic tracing
[**protocolProxyPortAdd**](PROXYApi.md#protocolProxyPortAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/proxy/port/add/{port}/{target}/{targetPort} | Add individual proxy target on the agent and the simulator host
[**protocolProxyPortIsstarted**](PROXYApi.md#protocolProxyPortIsstarted) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/port/isStarted/{port} | Check individual target
[**protocolProxyPortList**](PROXYApi.md#protocolProxyPortList) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/port/list | List all proxy targets
[**protocolProxyPortRemove**](PROXYApi.md#protocolProxyPortRemove) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/proxy/port/remove/{port} | Remove individual proxy target on the agent and the simulator host
[**protocolProxyPortStart**](PROXYApi.md#protocolProxyPortStart) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/port/start/{port} | Start additional target
[**protocolProxyPortStop**](PROXYApi.md#protocolProxyPortStop) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/port/stop/{port} | Stop additional target
[**protocolProxySetConfig**](PROXYApi.md#protocolProxySetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/set/config/{argument}/{value} | Set the agent&#39;s PROXY configuration
[**protocolProxySetTrace**](PROXYApi.md#protocolProxySetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/set/trace/{enableOrNot} | Set the agent&#39;s PROXY traffic tracing



## protocolProxyGetArgs

> Object protocolProxyGetArgs(agentNum)

Show the agent&#39;s PROXY argument structure

Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to show the PROXY argument structure
apiInstance.protocolProxyGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the PROXY argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyGetConfig

> ConfigPROXY protocolProxyGetConfig(agentNum)

Show the agent&#39;s PROXY configuration

Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to show the PROXY configuration
apiInstance.protocolProxyGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the PROXY configuration | 

### Return type

[**ConfigPROXY**](ConfigPROXY.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyGetStatistics

> [Number] protocolProxyGetStatistics(agentNum)

Show the agent&#39;s PROXY statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to show PROXY statistics
apiInstance.protocolProxyGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show PROXY statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyGetStatsHdr

> [String] protocolProxyGetStatsHdr()

Show the PROXY statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
apiInstance.protocolProxyGetStatsHdr((error, data, response) => {
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


## protocolProxyGetTrace

> ConfigPROXY protocolProxyGetTrace(agentNum)

Show the agent&#39;s PROXY traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to show whether PROXY tracing is enabled
apiInstance.protocolProxyGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether PROXY tracing is enabled | 

### Return type

[**ConfigPROXY**](ConfigPROXY.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyPortAdd

> String protocolProxyPortAdd(agentNum, port, target, targetPort)

Add individual proxy target on the agent and the simulator host

Additional proxy target

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to manipulate PROXY target
let port = 56; // Number | 
let target = "target_example"; // String | 
let targetPort = 56; // Number | 
apiInstance.protocolProxyPortAdd(agentNum, port, target, targetPort, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate PROXY target | 
 **port** | **Number**|  | 
 **target** | **String**|  | 
 **targetPort** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyPortIsstarted

> String protocolProxyPortIsstarted(agentNum, port)

Check individual target

Check individual target

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to manipulate PROXY target
let port = 56; // Number | 
apiInstance.protocolProxyPortIsstarted(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate PROXY target | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyPortList

> [Number] protocolProxyPortList(agentNum)

List all proxy targets

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to manipulate PROXY target
apiInstance.protocolProxyPortList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate PROXY target | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyPortRemove

> String protocolProxyPortRemove(agentNum, port)

Remove individual proxy target on the agent and the simulator host

Remove proxy target

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to manipulate PROXY target
let port = 56; // Number | 
apiInstance.protocolProxyPortRemove(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate PROXY target | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyPortStart

> String protocolProxyPortStart(agentNum, port)

Start additional target

Start additional target

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to manipulate PROXY target
let port = 56; // Number | 
apiInstance.protocolProxyPortStart(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate PROXY target | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxyPortStop

> String protocolProxyPortStop(agentNum, port)

Stop additional target

Stop additional target

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to manipulate PROXY target
let port = 56; // Number | 
apiInstance.protocolProxyPortStop(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate PROXY target | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxySetConfig

> String protocolProxySetConfig(agentNum, argument, value)

Set the agent&#39;s PROXY configuration

Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to set the PROXY configuration
let argument = "argument_example"; // String | Parameter to set the PROXY configuration
let value = "value_example"; // String | Value to set the PROXY configuration
apiInstance.protocolProxySetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the PROXY configuration | 
 **argument** | **String**| Parameter to set the PROXY configuration | 
 **value** | **String**| Value to set the PROXY configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolProxySetTrace

> String protocolProxySetTrace(agentNum, enableOrNot)

Set the agent&#39;s PROXY traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.PROXYApi();
let agentNum = 56; // Number | Agent to set the PROXY tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the PROXY tracing
apiInstance.protocolProxySetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the PROXY tracing | 
 **enableOrNot** | **String**| Value to set the PROXY tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


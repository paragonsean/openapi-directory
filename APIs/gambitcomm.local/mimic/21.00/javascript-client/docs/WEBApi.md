# MimicRestApi.WEBApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolWebGetArgs**](WEBApi.md#protocolWebGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/args | Show the agent&#39;s WEB argument structure
[**protocolWebGetConfig**](WEBApi.md#protocolWebGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/config | Show the agent&#39;s WEB configuration
[**protocolWebGetStatistics**](WEBApi.md#protocolWebGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/statistics | Show the agent&#39;s WEB statistics
[**protocolWebGetStatsHdr**](WEBApi.md#protocolWebGetStatsHdr) | **GET** /mimic/protocol/msg/web/get/stats_hdr | Show the WEB statistics headers
[**protocolWebGetTrace**](WEBApi.md#protocolWebGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/trace | Show the agent&#39;s WEB traffic tracing
[**protocolWebPortAdd**](WEBApi.md#protocolWebPortAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/web/port/add/{port} | Add the agent&#39;s WEB port
[**protocolWebPortExists**](WEBApi.md#protocolWebPortExists) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/port/exists/{port} | Show the agent&#39;s WEB port
[**protocolWebPortRemove**](WEBApi.md#protocolWebPortRemove) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/web/port/remove/{port} | Remove the agent&#39;s WEB port
[**protocolWebPortSet**](WEBApi.md#protocolWebPortSet) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/port/set/{port}/{protocol}/{version} | Set the agent&#39;s WEB port attribute
[**protocolWebPortStart**](WEBApi.md#protocolWebPortStart) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/port/start/{port} | Start the agent&#39;s WEB port
[**protocolWebPortStop**](WEBApi.md#protocolWebPortStop) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/port/stop/{port} | Stop the agent&#39;s WEB port
[**protocolWebSetConfig**](WEBApi.md#protocolWebSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/set/config/{argument}/{value} | Set the agent&#39;s WEB configuration
[**protocolWebSetTrace**](WEBApi.md#protocolWebSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/set/trace/{enableOrNot} | Set the agent&#39;s WEB traffic tracing



## protocolWebGetArgs

> Object protocolWebGetArgs(agentNum)

Show the agent&#39;s WEB argument structure

Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to show the WEB argument structure
apiInstance.protocolWebGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the WEB argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebGetConfig

> ConfigWEB protocolWebGetConfig(agentNum)

Show the agent&#39;s WEB configuration

Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to show the WEB configuration
apiInstance.protocolWebGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the WEB configuration | 

### Return type

[**ConfigWEB**](ConfigWEB.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebGetStatistics

> [Number] protocolWebGetStatistics(agentNum)

Show the agent&#39;s WEB statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to show WEB statistics
apiInstance.protocolWebGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show WEB statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebGetStatsHdr

> [String] protocolWebGetStatsHdr()

Show the WEB statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
apiInstance.protocolWebGetStatsHdr((error, data, response) => {
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


## protocolWebGetTrace

> ConfigWEB protocolWebGetTrace(agentNum)

Show the agent&#39;s WEB traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to show whether WEB tracing is enabled
apiInstance.protocolWebGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether WEB tracing is enabled | 

### Return type

[**ConfigWEB**](ConfigWEB.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebPortAdd

> String protocolWebPortAdd(agentNum, port)

Add the agent&#39;s WEB port

Add port

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to add WEB port
let port = 56; // Number | TCP port
apiInstance.protocolWebPortAdd(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add WEB port | 
 **port** | **Number**| TCP port | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebPortExists

> [String] protocolWebPortExists(agentNum, port)

Show the agent&#39;s WEB port

Check the port. 1 means existing, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to show WEB configuration
let port = 56; // Number | TCP port
apiInstance.protocolWebPortExists(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show WEB configuration | 
 **port** | **Number**| TCP port | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebPortRemove

> String protocolWebPortRemove(agentNum, port)

Remove the agent&#39;s WEB port

Remove port

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to remove WEB port
let port = 56; // Number | TCP port
apiInstance.protocolWebPortRemove(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to remove WEB port | 
 **port** | **Number**| TCP port | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebPortSet

> String protocolWebPortSet(agentNum, port, protocol, version)

Set the agent&#39;s WEB port attribute

Set port

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to set WEB port
let port = 56; // Number | TCP port
let protocol = "protocol_example"; // String | Encryption or related protocol
let version = "version_example"; // String | Encryption or related protocol version
apiInstance.protocolWebPortSet(agentNum, port, protocol, version, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set WEB port | 
 **port** | **Number**| TCP port | 
 **protocol** | **String**| Encryption or related protocol | 
 **version** | **String**| Encryption or related protocol version | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebPortStart

> String protocolWebPortStart(agentNum, port)

Start the agent&#39;s WEB port

Start port

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to start WEB port
let port = 56; // Number | TCP port
apiInstance.protocolWebPortStart(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to start WEB port | 
 **port** | **Number**| TCP port | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebPortStop

> String protocolWebPortStop(agentNum, port)

Stop the agent&#39;s WEB port

Stop port

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to stop WEB port
let port = 56; // Number | TCP port
apiInstance.protocolWebPortStop(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to stop WEB port | 
 **port** | **Number**| TCP port | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebSetConfig

> String protocolWebSetConfig(agentNum, argument, value)

Set the agent&#39;s WEB configuration

Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to set the WEB configuration
let argument = "argument_example"; // String | Parameter to set the WEB configuration
let value = "value_example"; // String | Value to set the WEB configuration
apiInstance.protocolWebSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the WEB configuration | 
 **argument** | **String**| Parameter to set the WEB configuration | 
 **value** | **String**| Value to set the WEB configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolWebSetTrace

> String protocolWebSetTrace(agentNum, enableOrNot)

Set the agent&#39;s WEB traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.WEBApi();
let agentNum = 56; // Number | Agent to set the WEB tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the WEB tracing
apiInstance.protocolWebSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the WEB tracing | 
 **enableOrNot** | **String**| Value to set the WEB tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


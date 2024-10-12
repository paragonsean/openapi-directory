# MimicRestApi.SSHApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolSshGetArgs**](SSHApi.md#protocolSshGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/args | Show the agent&#39;s SSH argument structure
[**protocolSshGetConfig**](SSHApi.md#protocolSshGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/config | Show the agent&#39;s SSH configuration
[**protocolSshGetStatistics**](SSHApi.md#protocolSshGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/statistics | Show the agent&#39;s SSH statistics
[**protocolSshGetStatsHdr**](SSHApi.md#protocolSshGetStatsHdr) | **GET** /mimic/protocol/msg/ssh/get/stats_hdr | Show the SSH statistics headers
[**protocolSshGetTrace**](SSHApi.md#protocolSshGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/trace | Show the agent&#39;s SSH traffic tracing
[**protocolSshIpaliasDisable**](SSHApi.md#protocolSshIpaliasDisable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/disable/{ipaddress}/{port} | Disable individual IP aliases on the agent and the simulator host
[**protocolSshIpaliasEnable**](SSHApi.md#protocolSshIpaliasEnable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/enable/{ipaddress}/{port} | Enable individual IP aliases on the agent and the simulator host
[**protocolSshIpaliasIsenabled**](SSHApi.md#protocolSshIpaliasIsenabled) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/isenabled/{ipaddress}/{port} | Check individual IP aliases on the agent and the simulator host
[**protocolSshIpaliasList**](SSHApi.md#protocolSshIpaliasList) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/list | List all IP aliases on the agent and the simulator host
[**protocolSshSetConfig**](SSHApi.md#protocolSshSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/set/config/{argument}/{value} | Set the agent&#39;s SSH configuration
[**protocolSshSetTrace**](SSHApi.md#protocolSshSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/set/trace/{enableOrNot} | Set the agent&#39;s SSH traffic tracing



## protocolSshGetArgs

> Object protocolSshGetArgs(agentNum)

Show the agent&#39;s SSH argument structure

Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to show the SSH argument structure
apiInstance.protocolSshGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SSH argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshGetConfig

> ConfigSSH protocolSshGetConfig(agentNum)

Show the agent&#39;s SSH configuration

Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to show the SSH configuration
apiInstance.protocolSshGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SSH configuration | 

### Return type

[**ConfigSSH**](ConfigSSH.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshGetStatistics

> [Number] protocolSshGetStatistics(agentNum)

Show the agent&#39;s SSH statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to show SSH statistics
apiInstance.protocolSshGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show SSH statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshGetStatsHdr

> [String] protocolSshGetStatsHdr()

Show the SSH statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
apiInstance.protocolSshGetStatsHdr((error, data, response) => {
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


## protocolSshGetTrace

> ConfigSSH protocolSshGetTrace(agentNum)

Show the agent&#39;s SSH traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to show whether SSH tracing is enabled
apiInstance.protocolSshGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether SSH tracing is enabled | 

### Return type

[**ConfigSSH**](ConfigSSH.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshIpaliasDisable

> String protocolSshIpaliasDisable(agentNum, ipaddress, port)

Disable individual IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to manipulate SSH IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolSshIpaliasDisable(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SSH IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshIpaliasEnable

> String protocolSshIpaliasEnable(agentNum, ipaddress, port)

Enable individual IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to manipulate SSH IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolSshIpaliasEnable(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SSH IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshIpaliasIsenabled

> String protocolSshIpaliasIsenabled(agentNum, ipaddress, port)

Check individual IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to manipulate SSH IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolSshIpaliasIsenabled(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SSH IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshIpaliasList

> [IPAlias] protocolSshIpaliasList(agentNum)

List all IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to manipulate SSH IP alias
apiInstance.protocolSshIpaliasList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SSH IP alias | 

### Return type

[**[IPAlias]**](IPAlias.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshSetConfig

> String protocolSshSetConfig(agentNum, argument, value)

Set the agent&#39;s SSH configuration

Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to set the SSH configuration
let argument = "argument_example"; // String | Parameter to set the SSH configuration
let value = "value_example"; // String | Value to set the SSH configuration
apiInstance.protocolSshSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SSH configuration | 
 **argument** | **String**| Parameter to set the SSH configuration | 
 **value** | **String**| Value to set the SSH configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSshSetTrace

> String protocolSshSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SSH traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SSHApi();
let agentNum = 56; // Number | Agent to set the SSH tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the SSH tracing
apiInstance.protocolSshSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SSH tracing | 
 **enableOrNot** | **String**| Value to set the SSH tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


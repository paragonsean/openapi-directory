# MimicRestApi.SNMPTCPApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolSnmptcpGetArgs**](SNMPTCPApi.md#protocolSnmptcpGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/args | Show the agent&#39;s SNMPTCP argument structure
[**protocolSnmptcpGetConfig**](SNMPTCPApi.md#protocolSnmptcpGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/config | Show the agent&#39;s SNMPTCP configuration
[**protocolSnmptcpGetStatistics**](SNMPTCPApi.md#protocolSnmptcpGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/statistics | Show the agent&#39;s SNMPTCP statistics
[**protocolSnmptcpGetStatsHdr**](SNMPTCPApi.md#protocolSnmptcpGetStatsHdr) | **GET** /mimic/protocol/msg/snmptcp/get/stats_hdr | Show the SNMPTCP statistics headers
[**protocolSnmptcpGetTrace**](SNMPTCPApi.md#protocolSnmptcpGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/trace | Show the agent&#39;s SNMPTCP traffic tracing
[**protocolSnmptcpIpaliasDisable**](SNMPTCPApi.md#protocolSnmptcpIpaliasDisable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/disable/{ipaddress}/{port} | Disable individual IP aliases on the agent and the simulator host
[**protocolSnmptcpIpaliasEnable**](SNMPTCPApi.md#protocolSnmptcpIpaliasEnable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/enable/{ipaddress}/{port} | Enable individual IP aliases on the agent and the simulator host
[**protocolSnmptcpIpaliasIsenabled**](SNMPTCPApi.md#protocolSnmptcpIpaliasIsenabled) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/isenabled/{ipaddress}/{port} | Check individual IP aliases on the agent and the simulator host
[**protocolSnmptcpIpaliasList**](SNMPTCPApi.md#protocolSnmptcpIpaliasList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/list | List all IP aliases on the agent and the simulator host
[**protocolSnmptcpSetConfig**](SNMPTCPApi.md#protocolSnmptcpSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/set/config/{argument}/{value} | Set the agent&#39;s SNMPTCP configuration
[**protocolSnmptcpSetTrace**](SNMPTCPApi.md#protocolSnmptcpSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/set/trace/{enableOrNot} | Set the agent&#39;s SNMPTCP traffic tracing



## protocolSnmptcpGetArgs

> Object protocolSnmptcpGetArgs(agentNum)

Show the agent&#39;s SNMPTCP argument structure

Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to show the SNMPTCP argument structure
apiInstance.protocolSnmptcpGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPTCP argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpGetConfig

> ConfigSNMPTCP protocolSnmptcpGetConfig(agentNum)

Show the agent&#39;s SNMPTCP configuration

Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to show the SNMPTCP configuration
apiInstance.protocolSnmptcpGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPTCP configuration | 

### Return type

[**ConfigSNMPTCP**](ConfigSNMPTCP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpGetStatistics

> [Number] protocolSnmptcpGetStatistics(agentNum)

Show the agent&#39;s SNMPTCP statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to show SNMPTCP statistics
apiInstance.protocolSnmptcpGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show SNMPTCP statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpGetStatsHdr

> [String] protocolSnmptcpGetStatsHdr()

Show the SNMPTCP statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
apiInstance.protocolSnmptcpGetStatsHdr((error, data, response) => {
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


## protocolSnmptcpGetTrace

> ConfigSNMPTCP protocolSnmptcpGetTrace(agentNum)

Show the agent&#39;s SNMPTCP traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to show whether SNMPTCP tracing is enabled
apiInstance.protocolSnmptcpGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether SNMPTCP tracing is enabled | 

### Return type

[**ConfigSNMPTCP**](ConfigSNMPTCP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpIpaliasDisable

> String protocolSnmptcpIpaliasDisable(agentNum, ipaddress, port)

Disable individual IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to manipulate SNMPTCP IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolSnmptcpIpaliasDisable(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SNMPTCP IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpIpaliasEnable

> String protocolSnmptcpIpaliasEnable(agentNum, ipaddress, port)

Enable individual IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to manipulate SNMPTCP IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolSnmptcpIpaliasEnable(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SNMPTCP IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpIpaliasIsenabled

> String protocolSnmptcpIpaliasIsenabled(agentNum, ipaddress, port)

Check individual IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to manipulate SNMPTCP IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolSnmptcpIpaliasIsenabled(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SNMPTCP IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpIpaliasList

> [IPAlias] protocolSnmptcpIpaliasList(agentNum)

List all IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to manipulate SNMPTCP IP alias
apiInstance.protocolSnmptcpIpaliasList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate SNMPTCP IP alias | 

### Return type

[**[IPAlias]**](IPAlias.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpSetConfig

> String protocolSnmptcpSetConfig(agentNum, argument, value)

Set the agent&#39;s SNMPTCP configuration

Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to set the SNMPTCP configuration
let argument = "argument_example"; // String | Parameter to set the SNMPTCP configuration
let value = "value_example"; // String | Value to set the SNMPTCP configuration
apiInstance.protocolSnmptcpSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SNMPTCP configuration | 
 **argument** | **String**| Parameter to set the SNMPTCP configuration | 
 **value** | **String**| Value to set the SNMPTCP configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmptcpSetTrace

> String protocolSnmptcpSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SNMPTCP traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPTCPApi();
let agentNum = 56; // Number | Agent to set the SNMPTCP tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the SNMPTCP tracing
apiInstance.protocolSnmptcpSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SNMPTCP tracing | 
 **enableOrNot** | **String**| Value to set the SNMPTCP tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


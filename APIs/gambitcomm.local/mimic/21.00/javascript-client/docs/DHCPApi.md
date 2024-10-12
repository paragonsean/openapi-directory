# MimicRestApi.DHCPApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolDhcpGetArgs**](DHCPApi.md#protocolDhcpGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/args | Show the agent&#39;s DHCP argument structure
[**protocolDhcpGetConfig**](DHCPApi.md#protocolDhcpGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/config | Show the agent&#39;s DHCP configuration
[**protocolDhcpGetStatistics**](DHCPApi.md#protocolDhcpGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/statistics | Show the agent&#39;s DHCP statistics
[**protocolDhcpGetStatsHdr**](DHCPApi.md#protocolDhcpGetStatsHdr) | **GET** /mimic/protocol/msg/dhcp/get/stats_hdr | Show the DHCP statistics headers
[**protocolDhcpGetTrace**](DHCPApi.md#protocolDhcpGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/trace | Show the agent&#39;s DHCP traffic tracing
[**protocolDhcpParams**](DHCPApi.md#protocolDhcpParams) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/params | Show the parameters configured by the server in its DHCP-OFFER message
[**protocolDhcpSetConfig**](DHCPApi.md#protocolDhcpSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/dhcp/set/config/{argument}/{value} | Set the agent&#39;s DHCP configuration
[**protocolDhcpSetTrace**](DHCPApi.md#protocolDhcpSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/dhcp/set/trace/{enableOrNot} | Set the agent&#39;s DHCP traffic tracing



## protocolDhcpGetArgs

> Object protocolDhcpGetArgs(agentNum)

Show the agent&#39;s DHCP argument structure

Agent&#39;s DHCP configuration particulars

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
let agentNum = 56; // Number | Agent to show the DHCP argument structure
apiInstance.protocolDhcpGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the DHCP argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolDhcpGetConfig

> ConfigDHCP protocolDhcpGetConfig(agentNum)

Show the agent&#39;s DHCP configuration

Agent&#39;s DHCP configuration hwaddr,classid,add_options,script

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
let agentNum = 56; // Number | Agent to show the DHCP configuration
apiInstance.protocolDhcpGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the DHCP configuration | 

### Return type

[**ConfigDHCP**](ConfigDHCP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolDhcpGetStatistics

> [Number] protocolDhcpGetStatistics(agentNum)

Show the agent&#39;s DHCP statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
let agentNum = 56; // Number | Agent to show DHCP statistics
apiInstance.protocolDhcpGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show DHCP statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolDhcpGetStatsHdr

> [String] protocolDhcpGetStatsHdr()

Show the DHCP statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
apiInstance.protocolDhcpGetStatsHdr((error, data, response) => {
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


## protocolDhcpGetTrace

> ConfigDHCP protocolDhcpGetTrace(agentNum)

Show the agent&#39;s DHCP traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
let agentNum = 56; // Number | Agent to show whether DHCP tracing is enabled
apiInstance.protocolDhcpGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether DHCP tracing is enabled | 

### Return type

[**ConfigDHCP**](ConfigDHCP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolDhcpParams

> [Object] protocolDhcpParams(agentNum)

Show the parameters configured by the server in its DHCP-OFFER message

DHCP-OFFER message parameters

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
let agentNum = 56; // Number | Agent to show DHCP DHCP-OFFER message
apiInstance.protocolDhcpParams(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show DHCP DHCP-OFFER message | 

### Return type

**[Object]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolDhcpSetConfig

> String protocolDhcpSetConfig(agentNum, argument, value)

Set the agent&#39;s DHCP configuration

Agent&#39;s DHCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
let agentNum = 56; // Number | Agent to set the DHCP configuration
let argument = "argument_example"; // String | Parameter to set the DHCP configuration
let value = "value_example"; // String | Value to set the DHCP configuration
apiInstance.protocolDhcpSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the DHCP configuration | 
 **argument** | **String**| Parameter to set the DHCP configuration | 
 **value** | **String**| Value to set the DHCP configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolDhcpSetTrace

> String protocolDhcpSetTrace(agentNum, enableOrNot)

Set the agent&#39;s DHCP traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DHCPApi();
let agentNum = 56; // Number | Agent to set the DHCP tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the DHCP tracing
apiInstance.protocolDhcpSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the DHCP tracing | 
 **enableOrNot** | **String**| Value to set the DHCP tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# MimicRestApi.IPMIApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolIpmiGetArgs**](IPMIApi.md#protocolIpmiGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/args | Show the agent&#39;s IPMI argument structure
[**protocolIpmiGetAttr**](IPMIApi.md#protocolIpmiGetAttr) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/{attr} | Show the outgoing message&#39;s attributes
[**protocolIpmiGetConfig**](IPMIApi.md#protocolIpmiGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/config | Show the agent&#39;s IPMI configuration
[**protocolIpmiGetStatistics**](IPMIApi.md#protocolIpmiGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/statistics | Show the agent&#39;s IPMI statistics
[**protocolIpmiGetStatsHdr**](IPMIApi.md#protocolIpmiGetStatsHdr) | **GET** /mimic/protocol/msg/ipmi/get/stats_hdr | Show the IPMI statistics headers
[**protocolIpmiGetTrace**](IPMIApi.md#protocolIpmiGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/trace | Show the agent&#39;s IPMI traffic tracing
[**protocolIpmiSetAttr**](IPMIApi.md#protocolIpmiSetAttr) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ipmi/set/{attr}/{value} | Set the outgoing message&#39;s attributes
[**protocolIpmiSetConfig**](IPMIApi.md#protocolIpmiSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ipmi/set/config/{argument}/{value} | Set the agent&#39;s IPMI configuration
[**protocolIpmiSetTrace**](IPMIApi.md#protocolIpmiSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ipmi/set/trace/{enableOrNot} | Set the agent&#39;s IPMI traffic tracing



## protocolIpmiGetArgs

> Object protocolIpmiGetArgs(agentNum)

Show the agent&#39;s IPMI argument structure

Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to show the IPMI argument structure
apiInstance.protocolIpmiGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the IPMI argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolIpmiGetAttr

> String protocolIpmiGetAttr(agentNum, attr)

Show the outgoing message&#39;s attributes

Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to set the IPMI tracing
let attr = "attr_example"; // String | Attribute
apiInstance.protocolIpmiGetAttr(agentNum, attr, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the IPMI tracing | 
 **attr** | **String**| Attribute | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolIpmiGetConfig

> ConfigIPMI protocolIpmiGetConfig(agentNum)

Show the agent&#39;s IPMI configuration

Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to show the IPMI configuration
apiInstance.protocolIpmiGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the IPMI configuration | 

### Return type

[**ConfigIPMI**](ConfigIPMI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolIpmiGetStatistics

> [Number] protocolIpmiGetStatistics(agentNum)

Show the agent&#39;s IPMI statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to show IPMI statistics
apiInstance.protocolIpmiGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show IPMI statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolIpmiGetStatsHdr

> [String] protocolIpmiGetStatsHdr()

Show the IPMI statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
apiInstance.protocolIpmiGetStatsHdr((error, data, response) => {
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


## protocolIpmiGetTrace

> ConfigIPMI protocolIpmiGetTrace(agentNum)

Show the agent&#39;s IPMI traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to show whether IPMI tracing is enabled
apiInstance.protocolIpmiGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether IPMI tracing is enabled | 

### Return type

[**ConfigIPMI**](ConfigIPMI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolIpmiSetAttr

> String protocolIpmiSetAttr(agentNum, attr, value)

Set the outgoing message&#39;s attributes

Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to set the IPMI tracing
let attr = "attr_example"; // String | Attribute
let value = "value_example"; // String | 
apiInstance.protocolIpmiSetAttr(agentNum, attr, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the IPMI tracing | 
 **attr** | **String**| Attribute | 
 **value** | **String**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolIpmiSetConfig

> String protocolIpmiSetConfig(agentNum, argument, value)

Set the agent&#39;s IPMI configuration

Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to set the IPMI configuration
let argument = "argument_example"; // String | Parameter to set the IPMI configuration
let value = "value_example"; // String | Value to set the IPMI configuration
apiInstance.protocolIpmiSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the IPMI configuration | 
 **argument** | **String**| Parameter to set the IPMI configuration | 
 **value** | **String**| Value to set the IPMI configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolIpmiSetTrace

> String protocolIpmiSetTrace(agentNum, enableOrNot)

Set the agent&#39;s IPMI traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.IPMIApi();
let agentNum = 56; // Number | Agent to set the IPMI tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the IPMI tracing
apiInstance.protocolIpmiSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the IPMI tracing | 
 **enableOrNot** | **String**| Value to set the IPMI tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


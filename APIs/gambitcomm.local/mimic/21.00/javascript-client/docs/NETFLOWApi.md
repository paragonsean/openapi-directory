# MimicRestApi.NETFLOWApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolNetflowChangeAttr**](NETFLOWApi.md#protocolNetflowChangeAttr) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/change/{flowset-uid}/{field-num}/{attr}/{value} | Change NETFLOW export attributes
[**protocolNetflowChangeDfs**](NETFLOWApi.md#protocolNetflowChangeDfs) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/change/dfs_interval/{interval} | Change NETFLOW data export interval
[**protocolNetflowChangeTfs**](NETFLOWApi.md#protocolNetflowChangeTfs) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/change/tfs_interval/{interval} | Change NETFLOW template export interval
[**protocolNetflowGetArgs**](NETFLOWApi.md#protocolNetflowGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/args | Show the agent&#39;s NETFLOW argument structure
[**protocolNetflowGetConfig**](NETFLOWApi.md#protocolNetflowGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/config | Show the agent&#39;s NETFLOW configuration
[**protocolNetflowGetStatistics**](NETFLOWApi.md#protocolNetflowGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/statistics | Show the agent&#39;s NETFLOW statistics
[**protocolNetflowGetStatsHdr**](NETFLOWApi.md#protocolNetflowGetStatsHdr) | **GET** /mimic/protocol/msg/netflow/get/stats_hdr | Show the NETFLOW statistics headers
[**protocolNetflowGetTrace**](NETFLOWApi.md#protocolNetflowGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/trace | Show the agent&#39;s NETFLOW traffic tracing
[**protocolNetflowHalt**](NETFLOWApi.md#protocolNetflowHalt) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/halt | Halt NETFLOW traffic
[**protocolNetflowList**](NETFLOWApi.md#protocolNetflowList) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/list | Show list of NETFLOW exports
[**protocolNetflowReload**](NETFLOWApi.md#protocolNetflowReload) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/reload | Reload NETFLOW configuration before resuming traffic
[**protocolNetflowResume**](NETFLOWApi.md#protocolNetflowResume) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/resume | Resuming traffic
[**protocolNetflowSetCollector**](NETFLOWApi.md#protocolNetflowSetCollector) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/collector/{collectorIP} | Swap NETFLOW collector
[**protocolNetflowSetConfig**](NETFLOWApi.md#protocolNetflowSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/config/{argument}/{value} | Set the agent&#39;s NETFLOW configuration
[**protocolNetflowSetFileName**](NETFLOWApi.md#protocolNetflowSetFileName) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/filename/{fileName} | Swap NETFLOW configuration file
[**protocolNetflowSetTrace**](NETFLOWApi.md#protocolNetflowSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/trace/{enableOrNot} | Set the agent&#39;s NETFLOW traffic tracing



## protocolNetflowChangeAttr

> String protocolNetflowChangeAttr(agentNum, flowsetUid, fieldNum, attr, value)

Change NETFLOW export attributes

Change attributes

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
let flowsetUid = 56; // Number | 
let fieldNum = 56; // Number | 
let attr = "attr_example"; // String | 
let value = "value_example"; // String | 
apiInstance.protocolNetflowChangeAttr(agentNum, flowsetUid, fieldNum, attr, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 
 **flowsetUid** | **Number**|  | 
 **fieldNum** | **Number**|  | 
 **attr** | **String**|  | 
 **value** | **String**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowChangeDfs

> String protocolNetflowChangeDfs(agentNum, interval)

Change NETFLOW data export interval

Interval in msec .

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
let interval = 56; // Number | NETFLOW export interval
apiInstance.protocolNetflowChangeDfs(agentNum, interval, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 
 **interval** | **Number**| NETFLOW export interval | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowChangeTfs

> String protocolNetflowChangeTfs(agentNum, interval)

Change NETFLOW template export interval

Interval in msec .

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
let interval = 56; // Number | NETFLOW export interval
apiInstance.protocolNetflowChangeTfs(agentNum, interval, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 
 **interval** | **Number**| NETFLOW export interval | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowGetArgs

> Object protocolNetflowGetArgs(agentNum)

Show the agent&#39;s NETFLOW argument structure

Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to show the NETFLOW argument structure
apiInstance.protocolNetflowGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the NETFLOW argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowGetConfig

> ConfigNETFLOW protocolNetflowGetConfig(agentNum)

Show the agent&#39;s NETFLOW configuration

Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to show the NETFLOW configuration
apiInstance.protocolNetflowGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the NETFLOW configuration | 

### Return type

[**ConfigNETFLOW**](ConfigNETFLOW.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowGetStatistics

> [Number] protocolNetflowGetStatistics(agentNum)

Show the agent&#39;s NETFLOW statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to show NETFLOW statistics
apiInstance.protocolNetflowGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show NETFLOW statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowGetStatsHdr

> [String] protocolNetflowGetStatsHdr()

Show the NETFLOW statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
apiInstance.protocolNetflowGetStatsHdr((error, data, response) => {
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


## protocolNetflowGetTrace

> ConfigNETFLOW protocolNetflowGetTrace(agentNum)

Show the agent&#39;s NETFLOW traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to show whether NETFLOW tracing is enabled
apiInstance.protocolNetflowGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether NETFLOW tracing is enabled | 

### Return type

[**ConfigNETFLOW**](ConfigNETFLOW.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowHalt

> String protocolNetflowHalt(agentNum)

Halt NETFLOW traffic

Halt NETFLOW traffic

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
apiInstance.protocolNetflowHalt(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowList

> [Object] protocolNetflowList(agentNum)

Show list of NETFLOW exports

Show list of NETFLOW exports

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to show NETFLOW statistics
apiInstance.protocolNetflowList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show NETFLOW statistics | 

### Return type

**[Object]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowReload

> String protocolNetflowReload(agentNum)

Reload NETFLOW configuration before resuming traffic

Reload NETFLOW configuration before resuming traffic

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
apiInstance.protocolNetflowReload(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowResume

> String protocolNetflowResume(agentNum)

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

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
apiInstance.protocolNetflowResume(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowSetCollector

> String protocolNetflowSetCollector(agentNum, collectorIP)

Swap NETFLOW collector

Allow changing collector without stopping agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
let collectorIP = "collectorIP_example"; // String | file name to load config
apiInstance.protocolNetflowSetCollector(agentNum, collectorIP, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 
 **collectorIP** | **String**| file name to load config | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowSetConfig

> String protocolNetflowSetConfig(agentNum, argument, value)

Set the agent&#39;s NETFLOW configuration

Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW configuration
let argument = "argument_example"; // String | Parameter to set the NETFLOW configuration
let value = "value_example"; // String | Value to set the NETFLOW configuration
apiInstance.protocolNetflowSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW configuration | 
 **argument** | **String**| Parameter to set the NETFLOW configuration | 
 **value** | **String**| Value to set the NETFLOW configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowSetFileName

> String protocolNetflowSetFileName(agentNum, fileName)

Swap NETFLOW configuration file

Allow reloading the configuration file for an agent without stopping agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW
let fileName = "fileName_example"; // String | file name to load config
apiInstance.protocolNetflowSetFileName(agentNum, fileName, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW | 
 **fileName** | **String**| file name to load config | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolNetflowSetTrace

> String protocolNetflowSetTrace(agentNum, enableOrNot)

Set the agent&#39;s NETFLOW traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.NETFLOWApi();
let agentNum = 56; // Number | Agent to set the NETFLOW tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the NETFLOW tracing
apiInstance.protocolNetflowSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the NETFLOW tracing | 
 **enableOrNot** | **String**| Value to set the NETFLOW tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


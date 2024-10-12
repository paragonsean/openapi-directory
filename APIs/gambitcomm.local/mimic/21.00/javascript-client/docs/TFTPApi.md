# MimicRestApi.TFTPApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolTftpGetArgs**](TFTPApi.md#protocolTftpGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/args | Show the agent&#39;s TFTP argument structure
[**protocolTftpGetConfig**](TFTPApi.md#protocolTftpGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/config | Show the agent&#39;s TFTP configuration
[**protocolTftpGetStatistics**](TFTPApi.md#protocolTftpGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/statistics | Show the agent&#39;s TFTP statistics
[**protocolTftpGetStatsHdr**](TFTPApi.md#protocolTftpGetStatsHdr) | **GET** /mimic/protocol/msg/tftp/get/stats_hdr | Show the TFTP statistics headers
[**protocolTftpGetTrace**](TFTPApi.md#protocolTftpGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/trace | Show the agent&#39;s TFTP traffic tracing
[**protocolTftpSessionGetParameter**](TFTPApi.md#protocolTftpSessionGetParameter) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/get/{parameter} | Show a parameter of a TFTP sesssion
[**protocolTftpSessionRead**](TFTPApi.md#protocolTftpSessionRead) | **POST** /mimic/agent/{agentNum}/protocol/msg/tftp/session/read/server/{srcfile} | Create a read session to download srcfile from server
[**protocolTftpSessionSetParameter**](TFTPApi.md#protocolTftpSessionSetParameter) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/set/{parameter}/{value} | Set a parameter of a TFTP sesssion
[**protocolTftpSessionStart**](TFTPApi.md#protocolTftpSessionStart) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/start | Start a TFTP sesssion
[**protocolTftpSessionStatus**](TFTPApi.md#protocolTftpSessionStatus) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/status | Check a TFTP sesssion&#39;s status
[**protocolTftpSessionStop**](TFTPApi.md#protocolTftpSessionStop) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/stop | Stop a TFTP sesssion
[**protocolTftpSessionWrite**](TFTPApi.md#protocolTftpSessionWrite) | **POST** /mimic/agent/{agentNum}/protocol/msg/tftp/session/write/server/{srcfile} | Create a read session to upload srcfile to server
[**protocolTftpSetConfig**](TFTPApi.md#protocolTftpSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/set/config/{argument}/{value} | Set the agent&#39;s TFTP configuration
[**protocolTftpSetTrace**](TFTPApi.md#protocolTftpSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/set/trace/{enableOrNot} | Set the agent&#39;s TFTP traffic tracing



## protocolTftpGetArgs

> Object protocolTftpGetArgs(agentNum)

Show the agent&#39;s TFTP argument structure

Agent&#39;s TFTP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show the TFTP argument structure
apiInstance.protocolTftpGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the TFTP argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpGetConfig

> ConfigTFTP protocolTftpGetConfig(agentNum)

Show the agent&#39;s TFTP configuration

Agent&#39;s TFTP configuration

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show the TFTP configuration
apiInstance.protocolTftpGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the TFTP configuration | 

### Return type

[**ConfigTFTP**](ConfigTFTP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpGetStatistics

> [Number] protocolTftpGetStatistics(agentNum)

Show the agent&#39;s TFTP statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show TFTP statistics
apiInstance.protocolTftpGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TFTP statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpGetStatsHdr

> [String] protocolTftpGetStatsHdr()

Show the TFTP statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
apiInstance.protocolTftpGetStatsHdr((error, data, response) => {
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


## protocolTftpGetTrace

> ConfigTFTP protocolTftpGetTrace(agentNum)

Show the agent&#39;s TFTP traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show whether TFTP tracing is enabled
apiInstance.protocolTftpGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether TFTP tracing is enabled | 

### Return type

[**ConfigTFTP**](ConfigTFTP.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSessionGetParameter

> String protocolTftpSessionGetParameter(agentNum, sessionID, parameter)

Show a parameter of a TFTP sesssion

Parameter is server , port , or dstfile

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show TFTP parameter
let sessionID = "sessionID_example"; // String | SessionID
let parameter = "parameter_example"; // String | Parameter to show
apiInstance.protocolTftpSessionGetParameter(agentNum, sessionID, parameter, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TFTP parameter | 
 **sessionID** | **String**| SessionID | 
 **parameter** | **String**| Parameter to show | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSessionRead

> [Number] protocolTftpSessionRead(agentNum, srcfile)

Create a read session to download srcfile from server

Session ID is returned

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show TFTP statistics
let srcfile = "srcfile_example"; // String | File name to retrieve from server
apiInstance.protocolTftpSessionRead(agentNum, srcfile, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TFTP statistics | 
 **srcfile** | **String**| File name to retrieve from server | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSessionSetParameter

> String protocolTftpSessionSetParameter(agentNum, sessionID, parameter, value)

Set a parameter of a TFTP sesssion

Parameter is server , port , or dstfile

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to set TFTP parameter
let sessionID = "sessionID_example"; // String | SessionID
let parameter = "parameter_example"; // String | Parameter to set
let value = "value_example"; // String | Value to set
apiInstance.protocolTftpSessionSetParameter(agentNum, sessionID, parameter, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set TFTP parameter | 
 **sessionID** | **String**| SessionID | 
 **parameter** | **String**| Parameter to set | 
 **value** | **String**| Value to set | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSessionStart

> String protocolTftpSessionStart(agentNum, sessionID)

Start a TFTP sesssion

Start uploading or downloading the file

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to start TFTP transaction
let sessionID = "sessionID_example"; // String | SessionID
apiInstance.protocolTftpSessionStart(agentNum, sessionID, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to start TFTP transaction | 
 **sessionID** | **String**| SessionID | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSessionStatus

> String protocolTftpSessionStatus(agentNum, sessionID)

Check a TFTP sesssion&#39;s status

Status includes running state, bytes transfered, and time elapsed

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show TFTP transaction
let sessionID = "sessionID_example"; // String | SessionID
apiInstance.protocolTftpSessionStatus(agentNum, sessionID, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TFTP transaction | 
 **sessionID** | **String**| SessionID | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSessionStop

> String protocolTftpSessionStop(agentNum, sessionID)

Stop a TFTP sesssion

Stop uploading or downloading the file

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to stop TFTP transaction
let sessionID = "sessionID_example"; // String | SessionID
apiInstance.protocolTftpSessionStop(agentNum, sessionID, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to stop TFTP transaction | 
 **sessionID** | **String**| SessionID | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSessionWrite

> [Number] protocolTftpSessionWrite(agentNum, srcfile)

Create a read session to upload srcfile to server

Session ID is returned

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to show TFTP statistics
let srcfile = "srcfile_example"; // String | File name to upload to server
apiInstance.protocolTftpSessionWrite(agentNum, srcfile, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TFTP statistics | 
 **srcfile** | **String**| File name to upload to server | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSetConfig

> String protocolTftpSetConfig(agentNum, argument, value)

Set the agent&#39;s TFTP configuration

Agent&#39;s TFTP configuration

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to set the TFTP configuration
let argument = "argument_example"; // String | Parameter to set the TFTP configuration
let value = "value_example"; // String | Value to set the TFTP configuration
apiInstance.protocolTftpSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the TFTP configuration | 
 **argument** | **String**| Parameter to set the TFTP configuration | 
 **value** | **String**| Value to set the TFTP configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTftpSetTrace

> String protocolTftpSetTrace(agentNum, enableOrNot)

Set the agent&#39;s TFTP traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TFTPApi();
let agentNum = 56; // Number | Agent to set the TFTP tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the TFTP tracing
apiInstance.protocolTftpSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the TFTP tracing | 
 **enableOrNot** | **String**| Value to set the TFTP tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


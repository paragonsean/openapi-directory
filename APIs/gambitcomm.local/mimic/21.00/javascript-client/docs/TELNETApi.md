# MimicRestApi.TELNETApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolTelnetConnectionLogon**](TELNETApi.md#protocolTelnetConnectionLogon) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/connection/logon/{connectionID}/{user}/{password} | Changes the connection&#39;s current logon.
[**protocolTelnetConnectionRequest**](TELNETApi.md#protocolTelnetConnectionRequest) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/connection/request/{connectionID}/{command} | Executes the command asynchronously .
[**protocolTelnetConnectionSignal**](TELNETApi.md#protocolTelnetConnectionSignal) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/connection/signal/{connectionID}/{signalName} | Triggers the asynchronous signal event with the specified signal name
[**protocolTelnetGetArgs**](TELNETApi.md#protocolTelnetGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/args | Show the agent&#39;s TELNET argument structure
[**protocolTelnetGetConfig**](TELNETApi.md#protocolTelnetGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/config | Show the agent&#39;s TELNET configuration
[**protocolTelnetGetStatistics**](TELNETApi.md#protocolTelnetGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/statistics | Show the agent&#39;s TELNET statistics
[**protocolTelnetGetStatsHdr**](TELNETApi.md#protocolTelnetGetStatsHdr) | **GET** /mimic/protocol/msg/telnet/get/stats_hdr | Show the TELNET statistics headers
[**protocolTelnetGetTrace**](TELNETApi.md#protocolTelnetGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/trace | Show the agent&#39;s TELNET traffic tracing
[**protocolTelnetIpaliasDisable**](TELNETApi.md#protocolTelnetIpaliasDisable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/disable/{ipaddress}/{port} | Disable individual IP aliases on the agent and the simulator host
[**protocolTelnetIpaliasEnable**](TELNETApi.md#protocolTelnetIpaliasEnable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/enable/{ipaddress}/{port} | Enable individual IP aliases on the agent and the simulator host
[**protocolTelnetIpaliasIsenabled**](TELNETApi.md#protocolTelnetIpaliasIsenabled) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/isenabled/{ipaddress}/{port} | Check individual IP aliases on the agent and the simulator host
[**protocolTelnetIpaliasList**](TELNETApi.md#protocolTelnetIpaliasList) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/list | List all IP aliases on the agent and the simulator host
[**protocolTelnetServerGetConnections**](TELNETApi.md#protocolTelnetServerGetConnections) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/connections | Show the agent&#39;s TELNET connections
[**protocolTelnetServerGetKeymap**](TELNETApi.md#protocolTelnetServerGetKeymap) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/keymap | Show the agent&#39;s TELNET keymap file name
[**protocolTelnetServerGetRulesdb**](TELNETApi.md#protocolTelnetServerGetRulesdb) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/rulesdb | Show the agent&#39;s TELNET rules db file name
[**protocolTelnetServerGetState**](TELNETApi.md#protocolTelnetServerGetState) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/state | Show the agent&#39;s TELNET server state
[**protocolTelnetServerGetUserdb**](TELNETApi.md#protocolTelnetServerGetUserdb) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/userdb | Show the agent&#39;s TELNET user db file name
[**protocolTelnetServerGetUsers**](TELNETApi.md#protocolTelnetServerGetUsers) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/users | Show the agent&#39;s TELNET users
[**protocolTelnetSetConfig**](TELNETApi.md#protocolTelnetSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/set/config/{argument}/{value} | Set the agent&#39;s TELNET configuration
[**protocolTelnetSetTrace**](TELNETApi.md#protocolTelnetSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/set/trace/{enableOrNot} | Set the agent&#39;s TELNET traffic tracing



## protocolTelnetConnectionLogon

> [String] protocolTelnetConnectionLogon(agentNum, connectionID, user, password)

Changes the connection&#39;s current logon.

Logon change allows (hidden) commands for a different access mode to run.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to manipulate TELNET connection
let connectionID = 56; // Number | 
let user = "user_example"; // String | 
let password = "password_example"; // String | 
apiInstance.protocolTelnetConnectionLogon(agentNum, connectionID, user, password, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate TELNET connection | 
 **connectionID** | **Number**|  | 
 **user** | **String**|  | 
 **password** | **String**|  | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetConnectionRequest

> [String] protocolTelnetConnectionRequest(agentNum, connectionID, command)

Executes the command asynchronously .

Equivalent of the command typed in by the user.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to manipulate TELNET connection
let connectionID = 56; // Number | 
let command = "command_example"; // String | 
apiInstance.protocolTelnetConnectionRequest(agentNum, connectionID, command, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate TELNET connection | 
 **connectionID** | **Number**|  | 
 **command** | **String**|  | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetConnectionSignal

> [String] protocolTelnetConnectionSignal(agentNum, connectionID, signalName)

Triggers the asynchronous signal event with the specified signal name

Signal name is either connect or idle

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to manipulate TELNET connection
let connectionID = 56; // Number | 
let signalName = "signalName_example"; // String | 
apiInstance.protocolTelnetConnectionSignal(agentNum, connectionID, signalName, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate TELNET connection | 
 **connectionID** | **Number**|  | 
 **signalName** | **String**|  | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetGetArgs

> Object protocolTelnetGetArgs(agentNum)

Show the agent&#39;s TELNET argument structure

Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show the TELNET argument structure
apiInstance.protocolTelnetGetArgs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the TELNET argument structure | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetGetConfig

> ConfigTELNET protocolTelnetGetConfig(agentNum)

Show the agent&#39;s TELNET configuration

Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show the TELNET configuration
apiInstance.protocolTelnetGetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the TELNET configuration | 

### Return type

[**ConfigTELNET**](ConfigTELNET.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetGetStatistics

> [Number] protocolTelnetGetStatistics(agentNum)

Show the agent&#39;s TELNET statistics

Statistics of fields indicated in the headers

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show TELNET statistics
apiInstance.protocolTelnetGetStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TELNET statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetGetStatsHdr

> [String] protocolTelnetGetStatsHdr()

Show the TELNET statistics headers

The headers of statistics fields

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
apiInstance.protocolTelnetGetStatsHdr((error, data, response) => {
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


## protocolTelnetGetTrace

> ConfigTELNET protocolTelnetGetTrace(agentNum)

Show the agent&#39;s TELNET traffic tracing

Trace 1 means enabled, 0 means not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show whether TELNET tracing is enabled
apiInstance.protocolTelnetGetTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show whether TELNET tracing is enabled | 

### Return type

[**ConfigTELNET**](ConfigTELNET.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetIpaliasDisable

> String protocolTelnetIpaliasDisable(agentNum, ipaddress, port)

Disable individual IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to manipulate TELNET IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolTelnetIpaliasDisable(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate TELNET IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetIpaliasEnable

> String protocolTelnetIpaliasEnable(agentNum, ipaddress, port)

Enable individual IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to manipulate TELNET IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolTelnetIpaliasEnable(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate TELNET IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetIpaliasIsenabled

> String protocolTelnetIpaliasIsenabled(agentNum, ipaddress, port)

Check individual IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to manipulate TELNET IP alias
let ipaddress = "ipaddress_example"; // String | 
let port = 56; // Number | 
apiInstance.protocolTelnetIpaliasIsenabled(agentNum, ipaddress, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate TELNET IP alias | 
 **ipaddress** | **String**|  | 
 **port** | **Number**|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetIpaliasList

> [IPAlias] protocolTelnetIpaliasList(agentNum)

List all IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to manipulate TELNET IP alias
apiInstance.protocolTelnetIpaliasList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to manipulate TELNET IP alias | 

### Return type

[**[IPAlias]**](IPAlias.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetServerGetConnections

> [Number] protocolTelnetServerGetConnections(agentNum)

Show the agent&#39;s TELNET connections

IDs of all connected connections

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show TELNET configuration
apiInstance.protocolTelnetServerGetConnections(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TELNET configuration | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetServerGetKeymap

> [String] protocolTelnetServerGetKeymap(agentNum)

Show the agent&#39;s TELNET keymap file name

Keymap file name

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show TELNET statistics
apiInstance.protocolTelnetServerGetKeymap(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TELNET statistics | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetServerGetRulesdb

> [String] protocolTelnetServerGetRulesdb(agentNum)

Show the agent&#39;s TELNET rules db file name

Rules db file name

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show TELNET statistics
apiInstance.protocolTelnetServerGetRulesdb(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TELNET statistics | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetServerGetState

> [Number] protocolTelnetServerGetState(agentNum)

Show the agent&#39;s TELNET server state

Return 1 means accepting connections, 0 not

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show TELNET statistics
apiInstance.protocolTelnetServerGetState(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TELNET statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetServerGetUserdb

> [String] protocolTelnetServerGetUserdb(agentNum)

Show the agent&#39;s TELNET user db file name

User db file name

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show TELNET statistics
apiInstance.protocolTelnetServerGetUserdb(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TELNET statistics | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetServerGetUsers

> [TelnetUser] protocolTelnetServerGetUsers(agentNum)

Show the agent&#39;s TELNET users

List of users

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to show TELNET configuration
apiInstance.protocolTelnetServerGetUsers(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show TELNET configuration | 

### Return type

[**[TelnetUser]**](TelnetUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetSetConfig

> String protocolTelnetSetConfig(agentNum, argument, value)

Set the agent&#39;s TELNET configuration

Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to set the TELNET configuration
let argument = "argument_example"; // String | Parameter to set the TELNET configuration
let value = "value_example"; // String | Value to set the TELNET configuration
apiInstance.protocolTelnetSetConfig(agentNum, argument, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the TELNET configuration | 
 **argument** | **String**| Parameter to set the TELNET configuration | 
 **value** | **String**| Value to set the TELNET configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolTelnetSetTrace

> String protocolTelnetSetTrace(agentNum, enableOrNot)

Set the agent&#39;s TELNET traffic tracing

1 to enable, 0 to disable

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.TELNETApi();
let agentNum = 56; // Number | Agent to set the TELNET tracing
let enableOrNot = "enableOrNot_example"; // String | Value to set the TELNET tracing
apiInstance.protocolTelnetSetTrace(agentNum, enableOrNot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the TELNET tracing | 
 **enableOrNot** | **String**| Value to set the TELNET tracing | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# MimicRestApi.SNMPv3Api

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protocolSnmpv3AccessAdd**](SNMPv3Api.md#protocolSnmpv3AccessAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/add/{groupName}/{prefix}/{securityModel}/{securityLevel}/{contextMatch}/{readView}/{writeView}/{notifyView} | Adds a new access entry with the specified parameters.
[**protocolSnmpv3AccessClear**](SNMPv3Api.md#protocolSnmpv3AccessClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/clear | Clears all access entries.
[**protocolSnmpv3AccessDel**](SNMPv3Api.md#protocolSnmpv3AccessDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/del/{accessName} | Deletes the specified access entry.
[**protocolSnmpv3AccessList**](SNMPv3Api.md#protocolSnmpv3AccessList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/access/list | Returns the current acccess entries as an array of strings.
[**protocolSnmpv3GetConfig**](SNMPv3Api.md#protocolSnmpv3GetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/config | Returns the SNMPv3 configuration.
[**protocolSnmpv3GetContextEngineid**](SNMPv3Api.md#protocolSnmpv3GetContextEngineid) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/context_engineid | Retrieves the contextEngineID for the agent instance.
[**protocolSnmpv3GetEngineboots**](SNMPv3Api.md#protocolSnmpv3GetEngineboots) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/engineboots | Retrieves the number of times the agent has been restarted.
[**protocolSnmpv3GetEngineid**](SNMPv3Api.md#protocolSnmpv3GetEngineid) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/engineid | For started agents, retrieves the current engineID in use by the snmpv3 module.
[**protocolSnmpv3GetEnginetime**](SNMPv3Api.md#protocolSnmpv3GetEnginetime) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/get/enginetime | Retrieves the time in seconds for which the agent has been running.
[**protocolSnmpv3GroupAdd**](SNMPv3Api.md#protocolSnmpv3GroupAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/add/{groupName}/{securityModel}/{securityName} | Adds a new group entry with the specified parameters.
[**protocolSnmpv3GroupClear**](SNMPv3Api.md#protocolSnmpv3GroupClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/clear | Clears all group entries.
[**protocolSnmpv3GroupDel**](SNMPv3Api.md#protocolSnmpv3GroupDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/del/{groupName} | Deletes the specified group entry.
[**protocolSnmpv3GroupList**](SNMPv3Api.md#protocolSnmpv3GroupList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/group/list | Returns the current group entries as an array of strings.
[**protocolSnmpv3SetConfig**](SNMPv3Api.md#protocolSnmpv3SetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/set/config/{parameter}/{value} | Changes the SNMPv3 configuration.
[**protocolSnmpv3UserAdd**](SNMPv3Api.md#protocolSnmpv3UserAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/add/{userName}/{securityName}/{authProtocol}/{authKey}/{privProtocol}/{privKey} | Adds a new user entry with the specified parameters.
[**protocolSnmpv3UserClear**](SNMPv3Api.md#protocolSnmpv3UserClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/clear | Clears all user entries.
[**protocolSnmpv3UserDel**](SNMPv3Api.md#protocolSnmpv3UserDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/del/{userName} | Deletes the specified user entry.
[**protocolSnmpv3UserList**](SNMPv3Api.md#protocolSnmpv3UserList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/user/list | Returns the current user entries as a Tcl list.
[**protocolSnmpv3UsmSave**](SNMPv3Api.md#protocolSnmpv3UsmSave) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/usm/save | Saves current user settings in the currently loaded USM config file.
[**protocolSnmpv3UsmSaveas**](SNMPv3Api.md#protocolSnmpv3UsmSaveas) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/usm/saveas/{filename} | Saves current user settings in the specified USM config file.
[**protocolSnmpv3VacmSave**](SNMPv3Api.md#protocolSnmpv3VacmSave) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/vacm/save | Saves current group, access, view settings in the currently loaded VACM config file.
[**protocolSnmpv3VacmSaveas**](SNMPv3Api.md#protocolSnmpv3VacmSaveas) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmpv3/vacm/saveas/{filename} | Saves current group, access, view settings in the specified VACM config file.
[**protocolSnmpv3ViewAdd**](SNMPv3Api.md#protocolSnmpv3ViewAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/add/{viewName}/{viewType}/{subtree}/{mask} | Adds a new view entry with the specified parameters.
[**protocolSnmpv3ViewClear**](SNMPv3Api.md#protocolSnmpv3ViewClear) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/clear | Clears all view entries.
[**protocolSnmpv3ViewDel**](SNMPv3Api.md#protocolSnmpv3ViewDel) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/del/{viewName} | Deletes the specified view entry.
[**protocolSnmpv3ViewList**](SNMPv3Api.md#protocolSnmpv3ViewList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmpv3/view/list | Returns the current view entries as an array of strings.



## protocolSnmpv3AccessAdd

> String protocolSnmpv3AccessAdd(agentNum, groupName, prefix, securityModel, securityLevel, contextMatch, readView, writeView, notifyView)

Adds a new access entry with the specified parameters.

Adds a new access entry with the specified parameters.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 access
let groupName = "groupName_example"; // String | SNMPv3 access name
let prefix = "prefix_example"; // String | SNMPv3 prefix
let securityModel = "securityModel_example"; // String | SNMPv3 access security model
let securityLevel = "securityLevel_example"; // String | SNMPv3 access security level
let contextMatch = "contextMatch_example"; // String | SNMPv3 access context match
let readView = "readView_example"; // String | SNMPv3 access read view
let writeView = "writeView_example"; // String | SNMPv3 access write view
let notifyView = "notifyView_example"; // String | SNMPv3 access notify view
apiInstance.protocolSnmpv3AccessAdd(agentNum, groupName, prefix, securityModel, securityLevel, contextMatch, readView, writeView, notifyView, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 access | 
 **groupName** | **String**| SNMPv3 access name | 
 **prefix** | **String**| SNMPv3 prefix | 
 **securityModel** | **String**| SNMPv3 access security model | 
 **securityLevel** | **String**| SNMPv3 access security level | 
 **contextMatch** | **String**| SNMPv3 access context match | 
 **readView** | **String**| SNMPv3 access read view | 
 **writeView** | **String**| SNMPv3 access write view | 
 **notifyView** | **String**| SNMPv3 access notify view | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3AccessClear

> String protocolSnmpv3AccessClear(agentNum)

Clears all access entries.

Clears all access entries.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 access
apiInstance.protocolSnmpv3AccessClear(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 access | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3AccessDel

> String protocolSnmpv3AccessDel(agentNum, accessName)

Deletes the specified access entry.

Deletes the specified access entry.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 access
let accessName = "accessName_example"; // String | SNMPv3 access name
apiInstance.protocolSnmpv3AccessDel(agentNum, accessName, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 access | 
 **accessName** | **String**| SNMPv3 access name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3AccessList

> [String] protocolSnmpv3AccessList(agentNum)

Returns the current acccess entries as an array of strings.

Returns the current acccess entries as an array of strings.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3AccessList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GetConfig

> ConfigSNMPv3 protocolSnmpv3GetConfig(agentNum)

Returns the SNMPv3 configuration.

Returns the SNMPv3 configuration.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3GetConfig(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

[**ConfigSNMPv3**](ConfigSNMPv3.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GetContextEngineid

> String protocolSnmpv3GetContextEngineid(agentNum)

Retrieves the contextEngineID for the agent instance.

Retrieves the contextEngineID for the agent instance.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 engine
apiInstance.protocolSnmpv3GetContextEngineid(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 engine | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GetEngineboots

> Number protocolSnmpv3GetEngineboots(agentNum)

Retrieves the number of times the agent has been restarted.

Retrieves the number of times the agent has been restarted.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 engine
apiInstance.protocolSnmpv3GetEngineboots(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 engine | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GetEngineid

> String protocolSnmpv3GetEngineid(agentNum)

For started agents, retrieves the current engineID in use by the snmpv3 module.

For stopped agents, this operation is meaningless. If not explicitly set by the user then the autogenerated engineID is returned. The format of the engineID is in the familiar hex format, eg. \\x01 23 45 67 89...

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3GetEngineid(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GetEnginetime

> Number protocolSnmpv3GetEnginetime(agentNum)

Retrieves the time in seconds for which the agent has been running.

Retrieves the time in seconds for which the agent has been running.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 engine
apiInstance.protocolSnmpv3GetEnginetime(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 engine | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GroupAdd

> String protocolSnmpv3GroupAdd(agentNum, groupName, securityModel, securityName)

Adds a new group entry with the specified parameters.

Adds a new group entry with the specified parameters.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 group
let groupName = "groupName_example"; // String | SNMPv3 group name
let securityModel = "securityModel_example"; // String | SNMPv3 group security model
let securityName = "securityName_example"; // String | SNMPv3 group security name
apiInstance.protocolSnmpv3GroupAdd(agentNum, groupName, securityModel, securityName, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 group | 
 **groupName** | **String**| SNMPv3 group name | 
 **securityModel** | **String**| SNMPv3 group security model | 
 **securityName** | **String**| SNMPv3 group security name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GroupClear

> String protocolSnmpv3GroupClear(agentNum)

Clears all group entries.

Clears all group entries.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 group
apiInstance.protocolSnmpv3GroupClear(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 group | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GroupDel

> String protocolSnmpv3GroupDel(agentNum, groupName)

Deletes the specified group entry.

Deletes the specified group entry.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 group
let groupName = "groupName_example"; // String | SNMPv3 group name
apiInstance.protocolSnmpv3GroupDel(agentNum, groupName, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 group | 
 **groupName** | **String**| SNMPv3 group name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3GroupList

> [String] protocolSnmpv3GroupList(agentNum)

Returns the current group entries as an array of strings.

Returns the current group entries as an array of strings.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3GroupList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3SetConfig

> String protocolSnmpv3SetConfig(agentNum, parameter, value)

Changes the SNMPv3 configuration.

Changes the SNMPv3 configuration.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
let parameter = "parameter_example"; // String | SNMPv3 configuration parameter
let value = "value_example"; // String | SNMPv3 parameter value
apiInstance.protocolSnmpv3SetConfig(agentNum, parameter, value, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 
 **parameter** | **String**| SNMPv3 configuration parameter | 
 **value** | **String**| SNMPv3 parameter value | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3UserAdd

> String protocolSnmpv3UserAdd(agentNum, userName, securityName, authProtocol, authKey, privProtocol, privKey)

Adds a new user entry with the specified parameters.

Adds a new user entry with the specified parameters.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 user
let userName = "userName_example"; // String | SNMPv3 user name
let securityName = "securityName_example"; // String | SNMPv3 user security name
let authProtocol = "authProtocol_example"; // String | SNMPv3 user authentication protocol
let authKey = "authKey_example"; // String | SNMPv3 user authentication key
let privProtocol = "privProtocol_example"; // String | SNMPv3 user privacy encryption protocol
let privKey = "privKey_example"; // String | SNMPv3 user privacy encryption key
apiInstance.protocolSnmpv3UserAdd(agentNum, userName, securityName, authProtocol, authKey, privProtocol, privKey, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 user | 
 **userName** | **String**| SNMPv3 user name | 
 **securityName** | **String**| SNMPv3 user security name | 
 **authProtocol** | **String**| SNMPv3 user authentication protocol | 
 **authKey** | **String**| SNMPv3 user authentication key | 
 **privProtocol** | **String**| SNMPv3 user privacy encryption protocol | 
 **privKey** | **String**| SNMPv3 user privacy encryption key | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3UserClear

> String protocolSnmpv3UserClear(agentNum)

Clears all user entries.

Clears all user entries.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 user
apiInstance.protocolSnmpv3UserClear(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 user | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3UserDel

> String protocolSnmpv3UserDel(agentNum, userName)

Deletes the specified user entry.

Deletes the specified user entry.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 user
let userName = "userName_example"; // String | SNMPv3 user name
apiInstance.protocolSnmpv3UserDel(agentNum, userName, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 user | 
 **userName** | **String**| SNMPv3 user name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3UserList

> [String] protocolSnmpv3UserList(agentNum)

Returns the current user entries as a Tcl list.

Returns the current user entries as a Tcl list.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3UserList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3UsmSave

> [String] protocolSnmpv3UsmSave(agentNum)

Saves current user settings in the currently loaded USM config file.

Saves current user settings in the currently loaded USM config file.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3UsmSave(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3UsmSaveas

> [String] protocolSnmpv3UsmSaveas(agentNum, filename)

Saves current user settings in the specified USM config file.

Saves current user settings in the specified USM config file.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
let filename = "filename_example"; // String | Filename to save
apiInstance.protocolSnmpv3UsmSaveas(agentNum, filename, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 
 **filename** | **String**| Filename to save | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3VacmSave

> [String] protocolSnmpv3VacmSave(agentNum)

Saves current group, access, view settings in the currently loaded VACM config file.

Saves current group, access, view settings in the currently loaded VACM config file.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3VacmSave(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3VacmSaveas

> [String] protocolSnmpv3VacmSaveas(agentNum, filename)

Saves current group, access, view settings in the specified VACM config file.

Saves current group, access, view settings in the specified VACM config file.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
let filename = "filename_example"; // String | Filename to save
apiInstance.protocolSnmpv3VacmSaveas(agentNum, filename, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 
 **filename** | **String**| Filename to save | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3ViewAdd

> String protocolSnmpv3ViewAdd(agentNum, viewName, viewType, subtree, mask)

Adds a new view entry with the specified parameters.

Adds a new view entry with the specified parameters.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 view
let viewName = "viewName_example"; // String | SNMPv3 view name
let viewType = "viewType_example"; // String | SNMPv3 view type
let subtree = "subtree_example"; // String | SNMPv3 view subtree
let mask = "mask_example"; // String | SNMPv3 view mask
apiInstance.protocolSnmpv3ViewAdd(agentNum, viewName, viewType, subtree, mask, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 view | 
 **viewName** | **String**| SNMPv3 view name | 
 **viewType** | **String**| SNMPv3 view type | 
 **subtree** | **String**| SNMPv3 view subtree | 
 **mask** | **String**| SNMPv3 view mask | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3ViewClear

> String protocolSnmpv3ViewClear(agentNum)

Clears all view entries.

Clears all view entries.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 view
apiInstance.protocolSnmpv3ViewClear(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 view | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3ViewDel

> String protocolSnmpv3ViewDel(agentNum, viewName)

Deletes the specified view entry.

Deletes the specified view entry.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to add the SNMPv3 view
let viewName = "viewName_example"; // String | SNMPv3 view name
apiInstance.protocolSnmpv3ViewDel(agentNum, viewName, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the SNMPv3 view | 
 **viewName** | **String**| SNMPv3 view name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolSnmpv3ViewList

> [String] protocolSnmpv3ViewList(agentNum)

Returns the current view entries as an array of strings.

Returns the current view entries as an array of strings.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.SNMPv3Api();
let agentNum = 56; // Number | Agent to show the SNMPv3 configuration
apiInstance.protocolSnmpv3ViewList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the SNMPv3 configuration | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


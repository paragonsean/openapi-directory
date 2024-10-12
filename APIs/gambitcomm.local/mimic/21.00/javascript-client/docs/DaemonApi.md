# MimicRestApi.DaemonApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addDaemonTimerScript**](DaemonApi.md#addDaemonTimerScript) | **POST** /mimic/timer/script/add/{script}/{interval}/{arg} | Add a new timer script to be executed at specified interval (in msec) with the specified argument.
[**cfgLoad**](DaemonApi.md#cfgLoad) | **PUT** /mimic/load/{cfgFile}/{firstAgentNum}/{lastAgentNum}/{startAgentNum} | Load the lab configuration file file.
[**cfgNew**](DaemonApi.md#cfgNew) | **PUT** /mimic/clear/{firstAgentNum}/{lastAgentNum} | Clear the lab configuration.
[**cfgSave**](DaemonApi.md#cfgSave) | **PUT** /mimic/save | Save the lab configuration.
[**cfgSaveas**](DaemonApi.md#cfgSaveas) | **PUT** /mimic/saveas/{cfgFile}/{firstAgentNum}/{lastAgentNum} | Save the lab configuration in file.
[**delDaemonTimerScript**](DaemonApi.md#delDaemonTimerScript) | **DELETE** /mimic/timer/script/delete/{script}/{interval}/{arg} | Remove a timer script from the execution list.
[**getActiveDataList**](DaemonApi.md#getActiveDataList) | **GET** /mimic/get/active_data_list | The list of {agentnum {statistics}} for agents that are currently active and whose statistics have changed since the last invocation of this command.
[**getActiveList**](DaemonApi.md#getActiveList) | **GET** /mimic/get/active_list | The list of {agentnum} that are currently active (running or paused).
[**getCfgFileChanged**](DaemonApi.md#getCfgFileChanged) | **GET** /mimic/get/cfgfile_changed | This predicate indicates if the currently loaded agent configuration file has changed.
[**getCfgfile**](DaemonApi.md#getCfgfile) | **GET** /mimic/get/cfgfile | The currently loaded lab configuration file for the particular user.
[**getChangedConfigList**](DaemonApi.md#getChangedConfigList) | **GET** /mimic/get/changed_config_list | The list of {agentnum} for which a configurable parameter changed.
[**getChangedStateList**](DaemonApi.md#getChangedStateList) | **GET** /mimic/get/changed_state_list | The list of {agentnum state} for which the state changed.
[**getClients**](DaemonApi.md#getClients) | **GET** /mimic/get/clients | The number of clients currently connected to the daemon.
[**getConfiguredList**](DaemonApi.md#getConfiguredList) | **GET** /mimic/get/configured_list | The list of {agentnum} that are currently configured.
[**getDaemonProtocols**](DaemonApi.md#getDaemonProtocols) | **GET** /mimic/get/protocols | The set of protocols supported by the Simulator.
[**getInterfaces**](DaemonApi.md#getInterfaces) | **GET** /mimic/get/interfaces | The set of network interfaces that can be used for simulations.
[**getLast**](DaemonApi.md#getLast) | **GET** /mimic/get/last | The last configured agent instance.
[**getLog**](DaemonApi.md#getLog) | **GET** /mimic/get/log | The current log file for the Simulator.
[**getMax**](DaemonApi.md#getMax) | **GET** /mimic/get/max | The maximum number of agent instances.
[**getNetaddr**](DaemonApi.md#getNetaddr) | **GET** /mimic/get/netaddr | The network address of the host where the MIMIC simulator is running.
[**getNetdev**](DaemonApi.md#getNetdev) | **GET** /mimic/get/netdev | The default network device to be used for agent addresses.
[**getProduct**](DaemonApi.md#getProduct) | **GET** /mimic/get/product | The product number that is licensed.
[**getReturn**](DaemonApi.md#getReturn) | **GET** /mimic/get/return | The return mode.
[**getVersion**](DaemonApi.md#getVersion) | **GET** /mimic/get/version | The version of the MIMIC command interface.
[**listDaemonTimerScripts**](DaemonApi.md#listDaemonTimerScripts) | **GET** /mimic/timer/script/list | List the timer scripts currently running along with the their intervals.
[**mgetInfo**](DaemonApi.md#mgetInfo) | **GET** /mimic/mget/{infoArray} | Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.
[**setLog**](DaemonApi.md#setLog) | **PUT** /mimic/set/log | The current log file for the Simulator.
[**setNetdev**](DaemonApi.md#setNetdev) | **PUT** /mimic/set/netdev | The network address of the host where the MIMIC simulator is running.
[**startAllAgents**](DaemonApi.md#startAllAgents) | **PUT** /mimic/start | Start MIMIC.
[**stopAllAgents**](DaemonApi.md#stopAllAgents) | **PUT** /mimic/stop | Stop MIMIC.
[**storeExists**](DaemonApi.md#storeExists) | **GET** /mimic/store/exists/{var} | This command can be used as a predicate to ascertain the existence of a given variable.
[**storeGet**](DaemonApi.md#storeGet) | **GET** /mimic/store/get/{var} | Fetches the value associated with a variable.
[**storeList**](DaemonApi.md#storeList) | **GET** /mimic/store/list | This command will return the list of variables in the said scope.
[**storeLreplace**](DaemonApi.md#storeLreplace) | **PUT** /mimic/store/lreplace/{var}/{index} | These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.
[**storePersists**](DaemonApi.md#storePersists) | **GET** /mimic/store/persists/{var} | This command can be used as a predicate to ascertain the persistence of a given variable.
[**storeSave**](DaemonApi.md#storeSave) | **PUT** /mimic/set/persistent | This operation flushes all global objects which need to be made persistent to disk.
[**storeSet**](DaemonApi.md#storeSet) | **PUT** /mimic/store/set/{var}/{persist} | Set the variable store for the global storage
[**storeUnset**](DaemonApi.md#storeUnset) | **PUT** /mimic/store/unset/{var} | Deletes a variable which is currently defined.
[**terminate**](DaemonApi.md#terminate) | **PUT** /mimic/terminate | Terminate the MIMIC daemon.



## addDaemonTimerScript

> String addDaemonTimerScript(script, interval, arg)

Add a new timer script to be executed at specified interval (in msec) with the specified argument.

Add a new timer script to be executed at specified interval (in msec) with the specified argument.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let script = "script_example"; // String | Script name
let interval = 56; // Number | Interval in msec
let arg = "arg_example"; // String | Arguments to the script
apiInstance.addDaemonTimerScript(script, interval, arg, (error, data, response) => {
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
 **script** | **String**| Script name | 
 **interval** | **Number**| Interval in msec | 
 **arg** | **String**| Arguments to the script | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cfgLoad

> {String: Number} cfgLoad(cfgFile, firstAgentNum, lastAgentNum, startAgentNum)

Load the lab configuration file file.

Load agents in cfgFile from firstAgentNum to lastAgentNum on startAgentNum of current configuration

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let cfgFile = "cfgFile_example"; // String | MIMIC agent configuration file to load
let firstAgentNum = 56; // Number | Agent number in cfgFile to start the loading
let lastAgentNum = 56; // Number | Agent number in cfgFile to end the loading
let startAgentNum = 56; // Number | Agent number in current configuration to start placing the new agents
apiInstance.cfgLoad(cfgFile, firstAgentNum, lastAgentNum, startAgentNum, (error, data, response) => {
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
 **cfgFile** | **String**| MIMIC agent configuration file to load | 
 **firstAgentNum** | **Number**| Agent number in cfgFile to start the loading | 
 **lastAgentNum** | **Number**| Agent number in cfgFile to end the loading | 
 **startAgentNum** | **Number**| Agent number in current configuration to start placing the new agents | 

### Return type

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cfgNew

> {String: Number} cfgNew(firstAgentNum, lastAgentNum)

Clear the lab configuration.

Clear the lab configuration.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let firstAgentNum = 56; // Number | Agent number to start clearing
let lastAgentNum = 56; // Number | Agent number to end the clearing
apiInstance.cfgNew(firstAgentNum, lastAgentNum, (error, data, response) => {
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
 **firstAgentNum** | **Number**| Agent number to start clearing | 
 **lastAgentNum** | **Number**| Agent number to end the clearing | 

### Return type

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cfgSave

> {String: Number} cfgSave()

Save the lab configuration.

Save the lab configuration.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.cfgSave((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cfgSaveas

> {String: Number} cfgSaveas(cfgFile, firstAgentNum, lastAgentNum)

Save the lab configuration in file.

Save the lab configuration in file.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let cfgFile = "cfgFile_example"; // String | MIMIC agent configuration file to save
let firstAgentNum = 56; // Number | Agent number in cfgFile to start the loading
let lastAgentNum = 56; // Number | Agent number in cfgFile to end the loading
apiInstance.cfgSaveas(cfgFile, firstAgentNum, lastAgentNum, (error, data, response) => {
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
 **cfgFile** | **String**| MIMIC agent configuration file to save | 
 **firstAgentNum** | **Number**| Agent number in cfgFile to start the loading | 
 **lastAgentNum** | **Number**| Agent number in cfgFile to end the loading | 

### Return type

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delDaemonTimerScript

> String delDaemonTimerScript(script, interval, arg)

Remove a timer script from the execution list.

The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let script = "script_example"; // String | Script name
let interval = 56; // Number | Interval in msec
let arg = "arg_example"; // String | Arguments to the script
apiInstance.delDaemonTimerScript(script, interval, arg, (error, data, response) => {
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
 **script** | **String**| Script name | 
 **interval** | **Number**| Interval in msec | 
 **arg** | **String**| Arguments to the script | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getActiveDataList

> [Number] getActiveDataList()

The list of {agentnum {statistics}} for agents that are currently active and whose statistics have changed since the last invocation of this command.

This list is guaranteed to be sorted into increasing order.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getActiveDataList((error, data, response) => {
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

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getActiveList

> [Number] getActiveList()

The list of {agentnum} that are currently active (running or paused).

This list is guaranteed to be sorted into increasing order.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getActiveList((error, data, response) => {
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

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCfgFileChanged

> {String: Number} getCfgFileChanged()

This predicate indicates if the currently loaded agent configuration file has changed.

Whether the loaded agent configuration file has changed since the last time this predicate was queried. This allows for a client to detect agent configuration changes and to synchronize those changes from the MIMIC daemon.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getCfgFileChanged((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCfgfile

> {String: Number} getCfgfile()

The currently loaded lab configuration file for the particular user.

In the case of multi-user access this command returns a different configuration file loaded for each user.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getCfgfile((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChangedConfigList

> [Number] getChangedConfigList()

The list of {agentnum} for which a configurable parameter changed.

This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getChangedConfigList((error, data, response) => {
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

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChangedStateList

> [AgentState] getChangedStateList()

The list of {agentnum state} for which the state changed.

This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getChangedStateList((error, data, response) => {
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

[**[AgentState]**](AgentState.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClients

> {String: Number} getClients()

The number of clients currently connected to the daemon.

The number of clients currently connected to the daemon.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getClients((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfiguredList

> [Number] getConfiguredList()

The list of {agentnum} that are currently configured.

This list is guaranteed to be sorted into increasing order.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getConfiguredList((error, data, response) => {
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

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDaemonProtocols

> {String: Number} getDaemonProtocols()

The set of protocols supported by the Simulator.

The set of protocols supported by the Simulator.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getDaemonProtocols((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInterfaces

> {String: Number} getInterfaces()

The set of network interfaces that can be used for simulations.

The set of network interfaces that can be used for simulations.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getInterfaces((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLast

> Number getLast()

The last configured agent instance.

The last configured agent instance.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getLast((error, data, response) => {
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

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLog

> {String: Number} getLog()

The current log file for the Simulator.

The current log file for the Simulator.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getLog((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMax

> Number getMax()

The maximum number of agent instances.

The maximum number of agent instances.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getMax((error, data, response) => {
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

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetaddr

> {String: Number} getNetaddr()

The network address of the host where the MIMIC simulator is running.

The network address of the host where the MIMIC simulator is running.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getNetaddr((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetdev

> {String: Number} getNetdev()

The default network device to be used for agent addresses.

The default network device to be used for agent addresses if the interface is not explicitly specified for an agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getNetdev((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProduct

> {String: Number} getProduct()

The product number that is licensed.

The product number that is licensed.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getProduct((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReturn

> {String: Number} getReturn()

The return mode.

The OpenAPI daemon operates in two modes, nocatch, where error returns from MIMIC operations return error; or catch, where the TCL catch semantics are used (these are similar to C++ exceptions)

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getReturn((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVersion

> String getVersion()

The version of the MIMIC command interface.

The version of the MIMIC command interface.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.getVersion((error, data, response) => {
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

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDaemonTimerScripts

> [TimerScript] listDaemonTimerScripts()

List the timer scripts currently running along with the their intervals.

The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.listDaemonTimerScripts((error, data, response) => {
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

[**[TimerScript]**](TimerScript.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mgetInfo

> [Object] mgetInfo(infoArray)

Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let infoArray = ["null"]; // [String] | Multiple strings of info.
apiInstance.mgetInfo(infoArray, (error, data, response) => {
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
 **infoArray** | [**[String]**](String.md)| Multiple strings of info. | 

### Return type

**[Object]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setLog

> String setLog(body)

The current log file for the Simulator.

The current log file for the Simulator.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let body = "body_example"; // String | The file name of the new log file
apiInstance.setLog(body, (error, data, response) => {
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
 **body** | **String**| The file name of the new log file | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setNetdev

> {String: Number} setNetdev()

The network address of the host where the MIMIC simulator is running.

The network address of the host where the MIMIC simulator is running.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.setNetdev((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startAllAgents

> {String: Number} startAllAgents()

Start MIMIC.

Start MIMIC.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.startAllAgents((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopAllAgents

> {String: Number} stopAllAgents()

Stop MIMIC.

Stop MIMIC.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.stopAllAgents((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeExists

> String storeExists(_var)

This command can be used as a predicate to ascertain the existence of a given variable.

It returns \&quot;1\&quot; if the variable exists, else \&quot;0\&quot;.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let _var = "_var_example"; // String | Variable name
apiInstance.storeExists(_var, (error, data, response) => {
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
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeGet

> String storeGet(_var)

Fetches the value associated with a variable.

The value will be returned as a string (like all Tcl values).

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let _var = "_var_example"; // String | Variable name
apiInstance.storeGet(_var, (error, data, response) => {
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
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeList

> [String] storeList()

This command will return the list of variables in the said scope.

The list will be a Tcl format list with curly braces \&quot;{}\&quot; around each list element. These elements in turn are space separated.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.storeList((error, data, response) => {
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


## storeLreplace

> String storeLreplace(_var, index, opts)

These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let _var = "_var_example"; // String | Variable name
let index = 56; // Number | Index
let opts = {
  'body': "body_example" // String | Value
};
apiInstance.storeLreplace(_var, index, opts, (error, data, response) => {
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
 **_var** | **String**| Variable name | 
 **index** | **Number**| Index | 
 **body** | **String**| Value | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storePersists

> String storePersists(_var)

This command can be used as a predicate to ascertain the persistence of a given variable.

It returns \&quot;1\&quot; if the variable is persistent, else \&quot;0\&quot;.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let _var = "_var_example"; // String | Variable name
apiInstance.storePersists(_var, (error, data, response) => {
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
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeSave

> {String: Number} storeSave()

This operation flushes all global objects which need to be made persistent to disk.

The MIMIC daemon caches persistent objects and their changes, and writes them to disk at program termination. If it were to crash, these changes would be lost. This operation allows to checkpoint the cache, ie. write changes to persistent objects to disk. To save the lab configuration with per-agent persistent information the mimic save operation needs to be used.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.storeSave((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeSet

> String storeSet(_var, persist, opts)

Set the variable store for the global storage

Persist 1 means persistent , 0 means non-persistent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let _var = "_var_example"; // String | Variable name
let persist = 56; // Number | Persistent setting
let opts = {
  'body': "body_example" // String | Value
};
apiInstance.storeSet(_var, persist, opts, (error, data, response) => {
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
 **_var** | **String**| Variable name | 
 **persist** | **Number**| Persistent setting | 
 **body** | **String**| Value | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storeUnset

> String storeUnset(_var)

Deletes a variable which is currently defined.

This will cleanup persistent variables if needed

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
let _var = "_var_example"; // String | Variable name
apiInstance.storeUnset(_var, (error, data, response) => {
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
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## terminate

> {String: Number} terminate()

Terminate the MIMIC daemon.

Terminate the MIMIC daemon.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.DaemonApi();
apiInstance.terminate((error, data, response) => {
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

**{String: Number}**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# MimicRestApi.AgentApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addIpalias**](AgentApi.md#addIpalias) | **POST** /mimic/agent/{agentNum}/ipalias/add/{IP}/{port}/{mask}/{interface} | Adds a new ipalias for the agent.
[**addTimerScript**](AgentApi.md#addTimerScript) | **POST** /mimic/agent/{agentNum}/timer/script/add/{script}/{interval}/{arg} | Add a new timer script to be executed at specified interval (in msec) with the specified argument.
[**agentRemove**](AgentApi.md#agentRemove) | **DELETE** /mimic/agent/{agentNum}/remove | Remove the current agent.
[**agentStoreCopy**](AgentApi.md#agentStoreCopy) | **PUT** /mimic/agent/{agentNum}/store/copy/{otherAgent} | This command copies the variable store from the other agent to this agent.
[**agentStoreExists**](AgentApi.md#agentStoreExists) | **GET** /mimic/agent/{agentNum}/store/exists/{var} | This command can be used as a predicate to ascertain the existence of a given variable.
[**agentStoreGet**](AgentApi.md#agentStoreGet) | **GET** /mimic/agent/{agentNum}/store/get/{var} | Fetches the value associated with a variable.
[**agentStoreList**](AgentApi.md#agentStoreList) | **GET** /mimic/agent/{agentNum}/store/list | This command will return the list of variables in the said scope.
[**agentStoreLreplace**](AgentApi.md#agentStoreLreplace) | **PUT** /mimic/agent/{agentNum}/store/lreplace/{var}/{index} | These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.
[**agentStorePersists**](AgentApi.md#agentStorePersists) | **GET** /mimic/agent/{agentNum}/store/persists/{var} | This command can be used as a predicate to ascertain the persistence of a given variable.
[**agentStoreSet**](AgentApi.md#agentStoreSet) | **PUT** /mimic/agent/{agentNum}/store/set/{var}/{persist} | These commands allow the creation of a new variable, or changing an existing value.
[**agentStoreUnset**](AgentApi.md#agentStoreUnset) | **PUT** /mimic/agent/{agentNum}/store/unset/{var} | Deletes a variable which is currently defined.
[**callNew**](AgentApi.md#callNew) | **POST** /mimic/agent/{agentNum}/add/{IP} | Add an agent.
[**delIpalias**](AgentApi.md#delIpalias) | **DELETE** /mimic/agent/{agentNum}/ipalias/delete/{IP}/{port} | Deletes an existing ipalias from the agent.
[**delTimerScript**](AgentApi.md#delTimerScript) | **DELETE** /mimic/agent/{agentNum}/timer/script/delete/{script}/{interval}/{arg} | Remove a timer script from the execution list.
[**fromAdd**](AgentApi.md#fromAdd) | **POST** /mimic/agent/{agentNum}/from/add/{IP}/{port} | Add a source address that the agent will accept messages from.
[**fromDel**](AgentApi.md#fromDel) | **DELETE** /mimic/agent/{agentNum}/from/delete/{IP}/{port} | delete a source address that the agent will accept messages from.
[**fromList**](AgentApi.md#fromList) | **GET** /mimic/agent/{agentNum}/from/list | List the source addresses that the agent will accept messages from.
[**getAgentState**](AgentApi.md#getAgentState) | **GET** /mimic/agent/{agentNum}/get/state | current running state of the agent
[**getChanged**](AgentApi.md#getChanged) | **GET** /mimic/agent/{agentNum}/get/changed | has the agent value space changed?
[**getConfigChanged**](AgentApi.md#getConfigChanged) | **GET** /mimic/agent/{agentNum}/get/config_changed | has the lab configuration changed?
[**getDelay**](AgentApi.md#getDelay) | **GET** /mimic/agent/{agentNum}/get/delay | one-way transit delay in msec.
[**getDrops**](AgentApi.md#getDrops) | **GET** /mimic/agent/{agentNum}/get/drops | drop rate (every N-th PDU). 0 means no drops.
[**getHost**](AgentApi.md#getHost) | **GET** /mimic/agent/{agentNum}/get/host | host address of the agent.
[**getInformTimeout**](AgentApi.md#getInformTimeout) | **GET** /mimic/agent/{agentNum}/get/inform_timeout | timeout in seconds for retransmitting INFORM PDUs.
[**getInterface**](AgentApi.md#getInterface) | **GET** /mimic/agent/{agentNum}/get/interface | network interface card for the agent.
[**getMask**](AgentApi.md#getMask) | **GET** /mimic/agent/{agentNum}/get/mask | subnet mask of the agent.
[**getMibs**](AgentApi.md#getMibs) | **GET** /mimic/agent/{agentNum}/get/mibs | set of MIBs, simulations and scenarios
[**getNumberStarts**](AgentApi.md#getNumberStarts) | **GET** /mimic/agent/{agentNum}/get/num_starts | number of starts for the agent.
[**getOiddir**](AgentApi.md#getOiddir) | **GET** /mimic/agent/{agentNum}/get/oiddir | MIB directory of the agent.
[**getOwner**](AgentApi.md#getOwner) | **GET** /mimic/agent/{agentNum}/get/owner | owner of the agent.
[**getPdusize**](AgentApi.md#getPdusize) | **GET** /mimic/agent/{agentNum}/get/pdusize | maximum PDU size.
[**getPort**](AgentApi.md#getPort) | **GET** /mimic/agent/{agentNum}/get/port | port number
[**getPrivdir**](AgentApi.md#getPrivdir) | **GET** /mimic/agent/{agentNum}/get/privdir | private directory of the agent.
[**getProtocols**](AgentApi.md#getProtocols) | **GET** /mimic/agent/{agentNum}/get/protocol | protocols supported by agent
[**getReadCommunity**](AgentApi.md#getReadCommunity) | **GET** /mimic/agent/{agentNum}/get/read | read community string
[**getScen**](AgentApi.md#getScen) | **GET** /mimic/agent/{agentNum}/get/scen | first scenario name
[**getSim**](AgentApi.md#getSim) | **GET** /mimic/agent/{agentNum}/get/sim | first simulation name
[**getStarttime**](AgentApi.md#getStarttime) | **GET** /mimic/agent/{agentNum}/get/start | relative start time
[**getStateChanged**](AgentApi.md#getStateChanged) | **GET** /mimic/agent/{agentNum}/get/state_changed | has the agent state changed?
[**getStatistics**](AgentApi.md#getStatistics) | **GET** /mimic/agent/{agentNum}/get/statistics | current statistics of the agent instance
[**getTrace**](AgentApi.md#getTrace) | **GET** /mimic/agent/{agentNum}/get/trace | SNMP PDU tracing
[**getValidate**](AgentApi.md#getValidate) | **GET** /mimic/agent/{agentNum}/get/validate | SNMP SET validation policy.
[**getWriteCommunity**](AgentApi.md#getWriteCommunity) | **GET** /mimic/agent/{agentNum}/get/write | write community string
[**halt**](AgentApi.md#halt) | **PUT** /mimic/agent/{agentNum}/halt | Halt the current agent.
[**listIpaliases**](AgentApi.md#listIpaliases) | **GET** /mimic/agent/{agentNum}/ipalias/list | Lists all the additional ipaliases configured for the agent.
[**listTimerScripts**](AgentApi.md#listTimerScripts) | **GET** /mimic/agent/{agentNum}/timer/script/list | List the timer scripts currently running along with the their intervals.
[**pauseNow**](AgentApi.md#pauseNow) | **PUT** /mimic/agent/{agentNum}/pause | Pause the current agent.
[**protocolGetConfig**](AgentApi.md#protocolGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/{prot}/get/config | Returns the protocol&#39;s configuration.
[**reload**](AgentApi.md#reload) | **PUT** /mimic/agent/{agentNum}/reload | Reload the current agent.
[**resume**](AgentApi.md#resume) | **PUT** /mimic/agent/{agentNum}/resume | Resume the current agent.
[**save**](AgentApi.md#save) | **PUT** /mimic/agent/{agentNum}/save | Save agent MIB values.
[**setDelay**](AgentApi.md#setDelay) | **PUT** /mimic/agent/{agentNum}/set/delay/{delay} | one-way transit delay in msec
[**setDrops**](AgentApi.md#setDrops) | **PUT** /mimic/agent/{agentNum}/set/drops/{drops} | drop rate (every N-th PDU)
[**setHost**](AgentApi.md#setHost) | **PUT** /mimic/agent/{agentNum}/set/host/{host} | host address of the agent.
[**setInformTimeout**](AgentApi.md#setInformTimeout) | **PUT** /mimic/agent/{agentNum}/set/inform_timeout/{inform_timeout} | timeout in seconds for retransmitting INFORM PDUs
[**setInterface**](AgentApi.md#setInterface) | **PUT** /mimic/agent/{agentNum}/set/interface/{interface} | network interface card for the agent
[**setMask**](AgentApi.md#setMask) | **PUT** /mimic/agent/{agentNum}/set/mask/{mask} | subnet mask of the agent.
[**setMibs**](AgentApi.md#setMibs) | **PUT** /mimic/agent/{agentNum}/set/mibs | set of MIBs, simulations and scenarios
[**setOiddir**](AgentApi.md#setOiddir) | **PUT** /mimic/agent/{agentNum}/set/oiddir/{oiddir} | MIB directory of the agent.
[**setOwner**](AgentApi.md#setOwner) | **PUT** /mimic/agent/{agentNum}/set/owner/{owner} | owner of the agent
[**setPdusize**](AgentApi.md#setPdusize) | **PUT** /mimic/agent/{agentNum}/set/pdusize/{pdusize} | maximum PDU size
[**setPort**](AgentApi.md#setPort) | **PUT** /mimic/agent/{agentNum}/set/port/{port} | port number
[**setPrivdir**](AgentApi.md#setPrivdir) | **PUT** /mimic/agent/{agentNum}/set/privdir/{privdir} | private directory of the agent.
[**setProtocols**](AgentApi.md#setProtocols) | **PUT** /mimic/agent/{agentNum}/set/protocol | protocols supported by agent as a comma-separated list
[**setReadCommunity**](AgentApi.md#setReadCommunity) | **PUT** /mimic/agent/{agentNum}/set/read/{read} | read community string
[**setStarttime**](AgentApi.md#setStarttime) | **PUT** /mimic/agent/{agentNum}/set/start/{start} | relative start time
[**setTrace**](AgentApi.md#setTrace) | **PUT** /mimic/agent/{agentNum}/set/trace/{trace} | SNMP PDU tracing
[**setValidate**](AgentApi.md#setValidate) | **PUT** /mimic/agent/{agentNum}/set/validate/{validate} | SNMP SET validation policy
[**setWriteCommunity**](AgentApi.md#setWriteCommunity) | **PUT** /mimic/agent/{agentNum}/set/write/{write} | write community string
[**start**](AgentApi.md#start) | **PUT** /mimic/agent/{agentNum}/start | Start the current agent.
[**startIpalias**](AgentApi.md#startIpalias) | **PUT** /mimic/agent/{agentNum}/ipalias/start/{IP}/{port} | Starts an existing ipalias for the agent.
[**statusIpalias**](AgentApi.md#statusIpalias) | **GET** /mimic/agent/{agentNum}/ipalias/status/{IP}/{port} | Returns the status (0&#x3D;down, 1&#x3D;up) of an existing ipalias for the agent.
[**stop**](AgentApi.md#stop) | **PUT** /mimic/agent/{agentNum}/stop | Show the agent&#39;s primary IP address
[**stopIpalias**](AgentApi.md#stopIpalias) | **PUT** /mimic/agent/{agentNum}/ipalias/stop/{IP}/{port} | Stops an existing ipalias for the agent.
[**trapConfigAdd**](AgentApi.md#trapConfigAdd) | **POST** /mimic/agent/{agentNum}/trap/config/add/{IP}/{port} | Add a trap destination to the set of destinations.
[**trapConfigDel**](AgentApi.md#trapConfigDel) | **DELETE** /mimic/agent/{agentNum}/trap/config/delete/{IP}/{port} | Remove a trap destination from the set of destinations.
[**trapConfigList**](AgentApi.md#trapConfigList) | **GET** /mimic/agent/{agentNum}/trap/config/list | List the set of trap destinations for this agent instance.
[**trapList**](AgentApi.md#trapList) | **GET** /mimic/agent/{agentNum}/trap/list | List the outstanding asynchronous traps for this agent instance.



## addIpalias

> String addIpalias(agentNum, IP, port, mask, _interface)

Adds a new ipalias for the agent.

port defaults to 161 if not specified. mask defaults to the class-based network mask for the address. interface defaults to the default network interface.  If port is set to 0, the system will automatically select a port number. This is useful for client-mode protocols, such as TFTP or TOD. Upon start of an IP alias with a 0 (auto-assigned) port number, its port will change to contain the value of the selected system port.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to add the IP alias
let IP = "IP_example"; // String | IP address , IPv4 or IPv6
let port = 56; // Number | SNMP port , 0 or empty for default
let mask = "mask_example"; // String | Netmask, empty for default
let _interface = "_interface_example"; // String | Interface. Empty for default
apiInstance.addIpalias(agentNum, IP, port, mask, _interface, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the IP alias | 
 **IP** | **String**| IP address , IPv4 or IPv6 | 
 **port** | **Number**| SNMP port , 0 or empty for default | 
 **mask** | **String**| Netmask, empty for default | 
 **_interface** | **String**| Interface. Empty for default | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addTimerScript

> String addTimerScript(agentNum, script, interval, arg)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the timer script list
let script = "script_example"; // String | Script name
let interval = 56; // Number | Interval in msec
let arg = "arg_example"; // String | Arguments to the script
apiInstance.addTimerScript(agentNum, script, interval, arg, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the timer script list | 
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


## agentRemove

> String agentRemove(agentNum)

Remove the current agent.

For speed, this operation will complete asynchronously. The same synchronization considerations apply as in /mimic/agent/start.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.agentRemove(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentStoreCopy

> String agentStoreCopy(agentNum, otherAgent)

This command copies the variable store from the other agent to this agent.

This command copies the variable store from the other agent to this agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
let otherAgent = 56; // Number | Agent of the value space
apiInstance.agentStoreCopy(agentNum, otherAgent, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **otherAgent** | **Number**| Agent of the value space | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentStoreExists

> String agentStoreExists(agentNum, _var)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
let _var = "_var_example"; // String | Variable name
apiInstance.agentStoreExists(agentNum, _var, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentStoreGet

> String agentStoreGet(agentNum, _var)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
let _var = "_var_example"; // String | Variable name
apiInstance.agentStoreGet(agentNum, _var, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentStoreList

> [String] agentStoreList(agentNum)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
apiInstance.agentStoreList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentStoreLreplace

> String agentStoreLreplace(agentNum, _var, index, opts)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
let _var = "_var_example"; // String | Variable name
let index = 56; // Number | Index
let opts = {
  'body': "body_example" // String | Value
};
apiInstance.agentStoreLreplace(agentNum, _var, index, opts, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
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


## agentStorePersists

> String agentStorePersists(agentNum, _var)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
let _var = "_var_example"; // String | Variable name
apiInstance.agentStorePersists(agentNum, _var, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agentStoreSet

> String agentStoreSet(agentNum, _var, persist, opts)

These commands allow the creation of a new variable, or changing an existing value.

The append sub-command will append the value to an existing variable, or create a new one. The set sub-command will overwrite an existing variable, or create a new one. The optional persist flag can be used to indicate if the variable is to be persistent as described above. By default a value of &#39;0&#39; will be implied for the persist flag. To avoid mistakes, for existing variables the persist flag can only be set. If you want to reset it, you first need to unset the variable.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
let _var = "_var_example"; // String | Variable name
let persist = 56; // Number | Persistent setting
let opts = {
  'body': "body_example" // String | Value
};
apiInstance.agentStoreSet(agentNum, _var, persist, opts, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
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


## agentStoreUnset

> String agentStoreUnset(agentNum, _var)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent of the value space
let _var = "_var_example"; // String | Variable name
apiInstance.agentStoreUnset(agentNum, _var, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **_var** | **String**| Variable name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## callNew

> String callNew(agentNum, IP, triplet)

Add an agent.

Add an agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
let IP = "IP_example"; // String | Primary IP
let triplet = [new MimicRestApi.Triplet()]; // [Triplet] | Created agent object
apiInstance.callNew(agentNum, IP, triplet, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 
 **IP** | **String**| Primary IP | 
 **triplet** | [**[Triplet]**](Triplet.md)| Created agent object | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delIpalias

> String delIpalias(agentNum, IP, port)

Deletes an existing ipalias from the agent.

port defaults to 161 if not specified.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to delete the IP alias
let IP = "IP_example"; // String | IP address , IPv4 or IPv6
let port = 56; // Number | SNMP port , 0 or empty for default
apiInstance.delIpalias(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to delete the IP alias | 
 **IP** | **String**| IP address , IPv4 or IPv6 | 
 **port** | **Number**| SNMP port , 0 or empty for default | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delTimerScript

> String delTimerScript(agentNum, script, interval, arg)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the timer script list
let script = "script_example"; // String | Script name
let interval = 56; // Number | Interval in msec
let arg = "arg_example"; // String | Arguments to the script
apiInstance.delTimerScript(agentNum, script, interval, arg, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the timer script list | 
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


## fromAdd

> String fromAdd(agentNum, IP, port)

Add a source address that the agent will accept messages from.

An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to add the IP source
let IP = "IP_example"; // String | IP of the port, 0.0.0.0 for any
let port = 56; // Number | port of the source, 0 for any
apiInstance.fromAdd(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the IP source | 
 **IP** | **String**| IP of the port, 0.0.0.0 for any | 
 **port** | **Number**| port of the source, 0 for any | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fromDel

> String fromDel(agentNum, IP, port)

delete a source address that the agent will accept messages from.

An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to delete the IP source
let IP = "IP_example"; // String | IP of the source
let port = 56; // Number | port of the source
apiInstance.fromDel(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to delete the IP source | 
 **IP** | **String**| IP of the source | 
 **port** | **Number**| port of the source | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fromList

> [IPSource] fromList(agentNum)

List the source addresses that the agent will accept messages from.

This in effect implements source-address-indexing, where 2 agents with the same address can be configured, each accepting messages from different management stations.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to show the IP sources
apiInstance.fromList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the IP sources | 

### Return type

[**[IPSource]**](IPSource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAgentState

> Number getAgentState(agentNum)

current running state of the agent

0-Unknown 1-Running 2-Stopped 3-Halted 4-Paused 5-Deleted 6-Stopping

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the state
apiInstance.getAgentState(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the state | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChanged

> Number getChanged(agentNum)

has the agent value space changed?

has the agent value space changed?

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the indicator
apiInstance.getChanged(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the indicator | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfigChanged

> Number getConfigChanged(agentNum)

has the lab configuration changed?

has the lab configuration changed?

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the indicator
apiInstance.getConfigChanged(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the indicator | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDelay

> Number getDelay(agentNum)

one-way transit delay in msec.

The minimum granularity is 10 msec.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the delay time
apiInstance.getDelay(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the delay time | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDrops

> Number getDrops(agentNum)

drop rate (every N-th PDU). 0 means no drops.

drop rate (every N-th PDU). 0 means no drops.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the drop rate
apiInstance.getDrops(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the drop rate | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHost

> String getHost(agentNum)

host address of the agent.

Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.getHost(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInformTimeout

> Number getInformTimeout(agentNum)

timeout in seconds for retransmitting INFORM PDUs.

The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the timeout setting
apiInstance.getInformTimeout(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the timeout setting | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInterface

> String getInterface(agentNum)

network interface card for the agent.

network interface card for the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary interface
apiInstance.getInterface(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary interface | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMask

> String getMask(agentNum)

subnet mask of the agent.

subnet mask of the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary interface
apiInstance.getMask(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary interface | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMibs

> [Triplet] getMibs(agentNum)

set of MIBs, simulations and scenarios

set of MIBs, simulations and scenarios

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the MIB triplets
apiInstance.getMibs(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the MIB triplets | 

### Return type

[**[Triplet]**](Triplet.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumberStarts

> Number getNumberStarts(agentNum)

number of starts for the agent.

This count is incremented each time an agent starts. It affects the SNMPv3 EngineBoots parameter.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the count
apiInstance.getNumberStarts(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the count | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOiddir

> String getOiddir(agentNum)

MIB directory of the agent.

MIB directory of the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the directory path
apiInstance.getOiddir(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the directory path | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOwner

> String getOwner(agentNum)

owner of the agent.

owner of the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the owner
apiInstance.getOwner(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the owner | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPdusize

> Number getPdusize(agentNum)

maximum PDU size.

The limit for this configurable is 65536.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the PDU size
apiInstance.getPdusize(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the PDU size | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPort

> String getPort(agentNum)

port number

port number

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary SNMP port
apiInstance.getPort(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary SNMP port | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPrivdir

> String getPrivdir(agentNum)

private directory of the agent.

private directory of the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the directory path
apiInstance.getPrivdir(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the directory path | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProtocols

> [String] getProtocols(agentNum)

protocols supported by agent

protocols supported by agent as an array of strings

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the protocols arrary
apiInstance.getProtocols(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the protocols arrary | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadCommunity

> String getReadCommunity(agentNum)

read community string

read community string

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the SNMP read community string
apiInstance.getReadCommunity(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the SNMP read community string | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScen

> Number getScen(agentNum)

first scenario name

first scenario name

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the first scenario number
apiInstance.getScen(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the first scenario number | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSim

> String getSim(agentNum)

first simulation name

first simulation name

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the first simulation name
apiInstance.getSim(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the first simulation name | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStarttime

> String getStarttime(agentNum)

relative start time

relative start time

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the relative start time
apiInstance.getStarttime(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the relative start time | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStateChanged

> Number getStateChanged(agentNum)

has the agent state changed?

has the agent state changed?

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the indicator
apiInstance.getStateChanged(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the indicator | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatistics

> [Number] getStatistics(agentNum)

current statistics of the agent instance

The statistics are returned as 64-bit decimal numbers for the following statistics, total, discarded, error, GET, GETNEXT, SET, GETBULK, trap, GET variables, GETNEXT variables, SET variables, GETBULK variables, INFORM sent, INFORM re-sent, INFORM timed out, INFORM acked, INFORM REPORT

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the statistics
apiInstance.getStatistics(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the statistics | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrace

> Number getTrace(agentNum)

SNMP PDU tracing

SNMP PDU tracing

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the indicator
apiInstance.getTrace(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the indicator | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getValidate

> Number getValidate(agentNum)

SNMP SET validation policy.

Is a bitmask in which with the following bits (from LSB) check for type, length, range, access

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the bitmask integer
apiInstance.getValidate(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the bitmask integer | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWriteCommunity

> String getWriteCommunity(agentNum)

write community string

write community string

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the SNMP write community string
apiInstance.getWriteCommunity(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the SNMP write community string | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## halt

> String halt(agentNum)

Halt the current agent.

Halt the current agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.halt(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIpaliases

> [IPAlias] listIpaliases(agentNum)

Lists all the additional ipaliases configured for the agent.

The agent host address (set with mimic agent set host) is not in this list, since it is already accessible separately with mimic agent get host.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to show the IP alias list
apiInstance.listIpaliases(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the IP alias list | 

### Return type

[**[IPAlias]**](IPAlias.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTimerScripts

> [TimerScript] listTimerScripts(agentNum)

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

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the timer script list
apiInstance.listTimerScripts(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the timer script list | 

### Return type

[**[TimerScript]**](TimerScript.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pauseNow

> String pauseNow(agentNum)

Pause the current agent.

Pause the current agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.pauseNow(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protocolGetConfig

> Object protocolGetConfig(agentNum, prot)

Returns the protocol&#39;s configuration.

Returns the protocol&#39;s configuration.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to show the protocol configuration
let prot = "prot_example"; // String | Protocol to show configuration
apiInstance.protocolGetConfig(agentNum, prot, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the protocol configuration | 
 **prot** | **String**| Protocol to show configuration | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reload

> String reload(agentNum)

Reload the current agent.

This only works for halted agents. The net effect is the same as restarting an agent (ie. stop, start, halt), but without disconnecting the network (and thus existing connections).

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.reload(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resume

> String resume(agentNum)

Resume the current agent.

Resume the current agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.resume(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## save

> String save(agentNum)

Save agent MIB values.

Save agent MIB values.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to save
apiInstance.save(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to save | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setDelay

> Number setDelay(agentNum, delay)

one-way transit delay in msec

The minimum granularity is 10 msec.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the delay time
let delay = 56; // Number | Delay time of the agent
apiInstance.setDelay(agentNum, delay, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the delay time | 
 **delay** | **Number**| Delay time of the agent | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setDrops

> Number setDrops(agentNum, drops)

drop rate (every N-th PDU)

0 means no drops

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the drop rate
let drops = 56; // Number | Drop rate of the agent
apiInstance.setDrops(agentNum, drops, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the drop rate | 
 **drops** | **Number**| Drop rate of the agent | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setHost

> String setHost(agentNum, host)

host address of the agent.

Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the primary IP
let host = "host_example"; // String | Primary IP of the agent
apiInstance.setHost(agentNum, host, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the primary IP | 
 **host** | **String**| Primary IP of the agent | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setInformTimeout

> Number setInformTimeout(agentNum, informTimeout)

timeout in seconds for retransmitting INFORM PDUs

The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the timeout setting
let informTimeout = 56; // Number | Tmeout setting
apiInstance.setInformTimeout(agentNum, informTimeout, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the timeout setting | 
 **informTimeout** | **Number**| Tmeout setting | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setInterface

> String setInterface(agentNum, _interface)

network interface card for the agent

network interface card for the agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the primary interface
let _interface = "_interface_example"; // String | Primary interface of the agent
apiInstance.setInterface(agentNum, _interface, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the primary interface | 
 **_interface** | **String**| Primary interface of the agent | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setMask

> String setMask(agentNum, mask)

subnet mask of the agent.

subnet mask of the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the primary IP address mask
let mask = "mask_example"; // String | Mask to set for the agent primary IP address
apiInstance.setMask(agentNum, mask, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the primary IP address mask | 
 **mask** | **String**| Mask to set for the agent primary IP address | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setMibs

> String setMibs(agentNum, triplet)

set of MIBs, simulations and scenarios

set of MIBs, simulations and scenarios

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the MIB triplets
let triplet = [new MimicRestApi.Triplet()]; // [Triplet] | 
apiInstance.setMibs(agentNum, triplet, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the MIB triplets | 
 **triplet** | [**[Triplet]**](Triplet.md)|  | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setOiddir

> String setOiddir(agentNum, oiddir)

MIB directory of the agent.

MIB directory of the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the directory path
let oiddir = "oiddir_example"; // String | Directory path for the agent
apiInstance.setOiddir(agentNum, oiddir, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the directory path | 
 **oiddir** | **String**| Directory path for the agent | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setOwner

> String setOwner(agentNum, owner)

owner of the agent

owner of the agent

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the owner
let owner = "owner_example"; // String | Owner of the agent
apiInstance.setOwner(agentNum, owner, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the owner | 
 **owner** | **String**| Owner of the agent | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setPdusize

> Number setPdusize(agentNum, pdusize)

maximum PDU size

The limit for this configurable is 65536

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the PDU size
let pdusize = 56; // Number | PDU size setting for the agent
apiInstance.setPdusize(agentNum, pdusize, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the PDU size | 
 **pdusize** | **Number**| PDU size setting for the agent | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setPort

> String setPort(agentNum, port)

port number

port number

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the primary SNMP port
let port = 56; // Number | Primary SNMP port of the agent
apiInstance.setPort(agentNum, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the primary SNMP port | 
 **port** | **Number**| Primary SNMP port of the agent | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setPrivdir

> String setPrivdir(agentNum, privdir)

private directory of the agent.

private directory of the agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the directory path
let privdir = "privdir_example"; // String | Directory path for the agent
apiInstance.setPrivdir(agentNum, privdir, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the directory path | 
 **privdir** | **String**| Directory path for the agent | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setProtocols

> [Number] setProtocols(agentNum, requestBody)

protocols supported by agent as a comma-separated list

protocols supported by agent as a comma-separated list

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the protocols arrary
let requestBody = ["null"]; // [String] | Created agent object
apiInstance.setProtocols(agentNum, requestBody, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the protocols arrary | 
 **requestBody** | [**[String]**](String.md)| Created agent object | 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setReadCommunity

> String setReadCommunity(agentNum, read)

read community string

read community string

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the SNMP read community string
let read = "read_example"; // String | SNMP read community string
apiInstance.setReadCommunity(agentNum, read, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the SNMP read community string | 
 **read** | **String**| SNMP read community string | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setStarttime

> String setStarttime(agentNum, start)

relative start time

relative start time

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the relative start time
let start = 56; // Number | Relative start time of the agent
apiInstance.setStarttime(agentNum, start, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the relative start time | 
 **start** | **Number**| Relative start time of the agent | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setTrace

> Number setTrace(agentNum, trace)

SNMP PDU tracing

SNMP PDU tracing

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set trace setting
let trace = 56; // Number | Trace setting for the agent
apiInstance.setTrace(agentNum, trace, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set trace setting | 
 **trace** | **Number**| Trace setting for the agent | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setValidate

> Number setValidate(agentNum, validate)

SNMP SET validation policy

Is a bitmask in which with the following bits (from LSB) check for type, length, range, access. A default value of 65535 does all validation checking.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the bitmask integer
let validate = 56; // Number | Bitmask integer to set
apiInstance.setValidate(agentNum, validate, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the bitmask integer | 
 **validate** | **Number**| Bitmask integer to set | 

### Return type

**Number**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setWriteCommunity

> String setWriteCommunity(agentNum, write)

write community string

write community string

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to set the SNMP write community string
let write = "write_example"; // String | SNMP write community string
apiInstance.setWriteCommunity(agentNum, write, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to set the SNMP write community string | 
 **write** | **String**| SNMP write community string | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## start

> String start(agentNum)

Start the current agent.

For speed, this operation will complete asynchronously. A successful return from this command means the starting of the agent is in progress. If you need to rely on the agent to have completed startup, you should wait for it&#39;s state to become RUNNING.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.start(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startIpalias

> String startIpalias(agentNum, IP, port)

Starts an existing ipalias for the agent.

port defaults to 161 if not specified.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to start the IP alias
let IP = "IP_example"; // String | IP address , IPv4 or IPv6
let port = 56; // Number | SNMP port , 0 or empty for default
apiInstance.startIpalias(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to start the IP alias | 
 **IP** | **String**| IP address , IPv4 or IPv6 | 
 **port** | **Number**| SNMP port , 0 or empty for default | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## statusIpalias

> String statusIpalias(agentNum, IP, port)

Returns the status (0&#x3D;down, 1&#x3D;up) of an existing ipalias for the agent.

port defaults to 161 if not specified.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to show status of the IP alias
let IP = "IP_example"; // String | IP address , IPv4 or IPv6
let port = 56; // Number | SNMP port , 0 or empty for default
apiInstance.statusIpalias(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show status of the IP alias | 
 **IP** | **String**| IP address , IPv4 or IPv6 | 
 **port** | **Number**| SNMP port , 0 or empty for default | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stop

> String stop(agentNum)

Show the agent&#39;s primary IP address

Agent primary IP address

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to return the primary IP
apiInstance.stop(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to return the primary IP | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopIpalias

> String stopIpalias(agentNum, IP, port)

Stops an existing ipalias for the agent.

port defaults to 161 if not specified.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to stop the IP alias
let IP = "IP_example"; // String | IP address , IPv4 or IPv6
let port = 56; // Number | SNMP port , 0 or empty for default
apiInstance.stopIpalias(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to stop the IP alias | 
 **IP** | **String**| IP address , IPv4 or IPv6 | 
 **port** | **Number**| SNMP port , 0 or empty for default | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trapConfigAdd

> String trapConfigAdd(agentNum, IP, port)

Add a trap destination to the set of destinations.

Add a trap destination to the set of destinations.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to add the destination
let IP = "IP_example"; // String | IP of the destination
let port = 56; // Number | port of the destination
apiInstance.trapConfigAdd(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to add the destination | 
 **IP** | **String**| IP of the destination | 
 **port** | **Number**| port of the destination | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trapConfigDel

> String trapConfigDel(agentNum, IP, port)

Remove a trap destination from the set of destinations.

Remove a trap destination from the set of destinations.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to delete the destination
let IP = "IP_example"; // String | IP of the destination
let port = 56; // Number | port of the destination
apiInstance.trapConfigDel(agentNum, IP, port, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to delete the destination | 
 **IP** | **String**| IP of the destination | 
 **port** | **Number**| port of the destination | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trapConfigList

> [TrapDest] trapConfigList(agentNum)

List the set of trap destinations for this agent instance.

Each trap destination is identified with an IP address and a port number. The default port number is the standard SNMP trap port 162.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to show the IP alias list
apiInstance.trapConfigList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the IP alias list | 

### Return type

[**[TrapDest]**](TrapDest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trapList

> [String] trapList(agentNum)

List the outstanding asynchronous traps for this agent instance.

List the outstanding asynchronous traps for this agent instance.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AgentApi();
let agentNum = 56; // Number | Agent to list the traps
apiInstance.trapList(agentNum, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to list the traps | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


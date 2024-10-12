# AgentApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addIpalias**](AgentApi.md#addIpalias) | **POST** /mimic/agent/{agentNum}/ipalias/add/{IP}/{port}/{mask}/{interface} | Adds a new ipalias for the agent. |
| [**addTimerScript**](AgentApi.md#addTimerScript) | **POST** /mimic/agent/{agentNum}/timer/script/add/{script}/{interval}/{arg} | Add a new timer script to be executed at specified interval (in msec) with the specified argument. |
| [**agentRemove**](AgentApi.md#agentRemove) | **DELETE** /mimic/agent/{agentNum}/remove | Remove the current agent. |
| [**agentStoreCopy**](AgentApi.md#agentStoreCopy) | **PUT** /mimic/agent/{agentNum}/store/copy/{otherAgent} | This command copies the variable store from the other agent to this agent. |
| [**agentStoreExists**](AgentApi.md#agentStoreExists) | **GET** /mimic/agent/{agentNum}/store/exists/{var} | This command can be used as a predicate to ascertain the existence of a given variable. |
| [**agentStoreGet**](AgentApi.md#agentStoreGet) | **GET** /mimic/agent/{agentNum}/store/get/{var} | Fetches the value associated with a variable. |
| [**agentStoreList**](AgentApi.md#agentStoreList) | **GET** /mimic/agent/{agentNum}/store/list | This command will return the list of variables in the said scope. |
| [**agentStoreLreplace**](AgentApi.md#agentStoreLreplace) | **PUT** /mimic/agent/{agentNum}/store/lreplace/{var}/{index} | These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist. |
| [**agentStorePersists**](AgentApi.md#agentStorePersists) | **GET** /mimic/agent/{agentNum}/store/persists/{var} | This command can be used as a predicate to ascertain the persistence of a given variable. |
| [**agentStoreSet**](AgentApi.md#agentStoreSet) | **PUT** /mimic/agent/{agentNum}/store/set/{var}/{persist} | These commands allow the creation of a new variable, or changing an existing value. |
| [**agentStoreUnset**](AgentApi.md#agentStoreUnset) | **PUT** /mimic/agent/{agentNum}/store/unset/{var} | Deletes a variable which is currently defined. |
| [**callNew**](AgentApi.md#callNew) | **POST** /mimic/agent/{agentNum}/add/{IP} | Add an agent. |
| [**delIpalias**](AgentApi.md#delIpalias) | **DELETE** /mimic/agent/{agentNum}/ipalias/delete/{IP}/{port} | Deletes an existing ipalias from the agent. |
| [**delTimerScript**](AgentApi.md#delTimerScript) | **DELETE** /mimic/agent/{agentNum}/timer/script/delete/{script}/{interval}/{arg} | Remove a timer script from the execution list. |
| [**fromAdd**](AgentApi.md#fromAdd) | **POST** /mimic/agent/{agentNum}/from/add/{IP}/{port} | Add a source address that the agent will accept messages from. |
| [**fromDel**](AgentApi.md#fromDel) | **DELETE** /mimic/agent/{agentNum}/from/delete/{IP}/{port} | delete a source address that the agent will accept messages from. |
| [**fromList**](AgentApi.md#fromList) | **GET** /mimic/agent/{agentNum}/from/list | List the source addresses that the agent will accept messages from. |
| [**getAgentState**](AgentApi.md#getAgentState) | **GET** /mimic/agent/{agentNum}/get/state | current running state of the agent |
| [**getChanged**](AgentApi.md#getChanged) | **GET** /mimic/agent/{agentNum}/get/changed | has the agent value space changed? |
| [**getConfigChanged**](AgentApi.md#getConfigChanged) | **GET** /mimic/agent/{agentNum}/get/config_changed | has the lab configuration changed? |
| [**getDelay**](AgentApi.md#getDelay) | **GET** /mimic/agent/{agentNum}/get/delay | one-way transit delay in msec. |
| [**getDrops**](AgentApi.md#getDrops) | **GET** /mimic/agent/{agentNum}/get/drops | drop rate (every N-th PDU). 0 means no drops. |
| [**getHost**](AgentApi.md#getHost) | **GET** /mimic/agent/{agentNum}/get/host | host address of the agent. |
| [**getInformTimeout**](AgentApi.md#getInformTimeout) | **GET** /mimic/agent/{agentNum}/get/inform_timeout | timeout in seconds for retransmitting INFORM PDUs. |
| [**getInterface**](AgentApi.md#getInterface) | **GET** /mimic/agent/{agentNum}/get/interface | network interface card for the agent. |
| [**getMask**](AgentApi.md#getMask) | **GET** /mimic/agent/{agentNum}/get/mask | subnet mask of the agent. |
| [**getMibs**](AgentApi.md#getMibs) | **GET** /mimic/agent/{agentNum}/get/mibs | set of MIBs, simulations and scenarios |
| [**getNumberStarts**](AgentApi.md#getNumberStarts) | **GET** /mimic/agent/{agentNum}/get/num_starts | number of starts for the agent. |
| [**getOiddir**](AgentApi.md#getOiddir) | **GET** /mimic/agent/{agentNum}/get/oiddir | MIB directory of the agent. |
| [**getOwner**](AgentApi.md#getOwner) | **GET** /mimic/agent/{agentNum}/get/owner | owner of the agent. |
| [**getPdusize**](AgentApi.md#getPdusize) | **GET** /mimic/agent/{agentNum}/get/pdusize | maximum PDU size. |
| [**getPort**](AgentApi.md#getPort) | **GET** /mimic/agent/{agentNum}/get/port | port number |
| [**getPrivdir**](AgentApi.md#getPrivdir) | **GET** /mimic/agent/{agentNum}/get/privdir | private directory of the agent. |
| [**getProtocols**](AgentApi.md#getProtocols) | **GET** /mimic/agent/{agentNum}/get/protocol | protocols supported by agent |
| [**getReadCommunity**](AgentApi.md#getReadCommunity) | **GET** /mimic/agent/{agentNum}/get/read | read community string |
| [**getScen**](AgentApi.md#getScen) | **GET** /mimic/agent/{agentNum}/get/scen | first scenario name |
| [**getSim**](AgentApi.md#getSim) | **GET** /mimic/agent/{agentNum}/get/sim | first simulation name |
| [**getStarttime**](AgentApi.md#getStarttime) | **GET** /mimic/agent/{agentNum}/get/start | relative start time |
| [**getStateChanged**](AgentApi.md#getStateChanged) | **GET** /mimic/agent/{agentNum}/get/state_changed | has the agent state changed? |
| [**getStatistics**](AgentApi.md#getStatistics) | **GET** /mimic/agent/{agentNum}/get/statistics | current statistics of the agent instance |
| [**getTrace**](AgentApi.md#getTrace) | **GET** /mimic/agent/{agentNum}/get/trace | SNMP PDU tracing |
| [**getValidate**](AgentApi.md#getValidate) | **GET** /mimic/agent/{agentNum}/get/validate | SNMP SET validation policy. |
| [**getWriteCommunity**](AgentApi.md#getWriteCommunity) | **GET** /mimic/agent/{agentNum}/get/write | write community string |
| [**halt**](AgentApi.md#halt) | **PUT** /mimic/agent/{agentNum}/halt | Halt the current agent. |
| [**listIpaliases**](AgentApi.md#listIpaliases) | **GET** /mimic/agent/{agentNum}/ipalias/list | Lists all the additional ipaliases configured for the agent. |
| [**listTimerScripts**](AgentApi.md#listTimerScripts) | **GET** /mimic/agent/{agentNum}/timer/script/list | List the timer scripts currently running along with the their intervals. |
| [**pauseNow**](AgentApi.md#pauseNow) | **PUT** /mimic/agent/{agentNum}/pause | Pause the current agent. |
| [**protocolGetConfig**](AgentApi.md#protocolGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/{prot}/get/config | Returns the protocol&#39;s configuration. |
| [**reload**](AgentApi.md#reload) | **PUT** /mimic/agent/{agentNum}/reload | Reload the current agent. |
| [**resume**](AgentApi.md#resume) | **PUT** /mimic/agent/{agentNum}/resume | Resume the current agent. |
| [**save**](AgentApi.md#save) | **PUT** /mimic/agent/{agentNum}/save | Save agent MIB values. |
| [**setDelay**](AgentApi.md#setDelay) | **PUT** /mimic/agent/{agentNum}/set/delay/{delay} | one-way transit delay in msec |
| [**setDrops**](AgentApi.md#setDrops) | **PUT** /mimic/agent/{agentNum}/set/drops/{drops} | drop rate (every N-th PDU) |
| [**setHost**](AgentApi.md#setHost) | **PUT** /mimic/agent/{agentNum}/set/host/{host} | host address of the agent. |
| [**setInformTimeout**](AgentApi.md#setInformTimeout) | **PUT** /mimic/agent/{agentNum}/set/inform_timeout/{inform_timeout} | timeout in seconds for retransmitting INFORM PDUs |
| [**setInterface**](AgentApi.md#setInterface) | **PUT** /mimic/agent/{agentNum}/set/interface/{interface} | network interface card for the agent |
| [**setMask**](AgentApi.md#setMask) | **PUT** /mimic/agent/{agentNum}/set/mask/{mask} | subnet mask of the agent. |
| [**setMibs**](AgentApi.md#setMibs) | **PUT** /mimic/agent/{agentNum}/set/mibs | set of MIBs, simulations and scenarios |
| [**setOiddir**](AgentApi.md#setOiddir) | **PUT** /mimic/agent/{agentNum}/set/oiddir/{oiddir} | MIB directory of the agent. |
| [**setOwner**](AgentApi.md#setOwner) | **PUT** /mimic/agent/{agentNum}/set/owner/{owner} | owner of the agent |
| [**setPdusize**](AgentApi.md#setPdusize) | **PUT** /mimic/agent/{agentNum}/set/pdusize/{pdusize} | maximum PDU size |
| [**setPort**](AgentApi.md#setPort) | **PUT** /mimic/agent/{agentNum}/set/port/{port} | port number |
| [**setPrivdir**](AgentApi.md#setPrivdir) | **PUT** /mimic/agent/{agentNum}/set/privdir/{privdir} | private directory of the agent. |
| [**setProtocols**](AgentApi.md#setProtocols) | **PUT** /mimic/agent/{agentNum}/set/protocol | protocols supported by agent as a comma-separated list |
| [**setReadCommunity**](AgentApi.md#setReadCommunity) | **PUT** /mimic/agent/{agentNum}/set/read/{read} | read community string |
| [**setStarttime**](AgentApi.md#setStarttime) | **PUT** /mimic/agent/{agentNum}/set/start/{start} | relative start time |
| [**setTrace**](AgentApi.md#setTrace) | **PUT** /mimic/agent/{agentNum}/set/trace/{trace} | SNMP PDU tracing |
| [**setValidate**](AgentApi.md#setValidate) | **PUT** /mimic/agent/{agentNum}/set/validate/{validate} | SNMP SET validation policy |
| [**setWriteCommunity**](AgentApi.md#setWriteCommunity) | **PUT** /mimic/agent/{agentNum}/set/write/{write} | write community string |
| [**start**](AgentApi.md#start) | **PUT** /mimic/agent/{agentNum}/start | Start the current agent. |
| [**startIpalias**](AgentApi.md#startIpalias) | **PUT** /mimic/agent/{agentNum}/ipalias/start/{IP}/{port} | Starts an existing ipalias for the agent. |
| [**statusIpalias**](AgentApi.md#statusIpalias) | **GET** /mimic/agent/{agentNum}/ipalias/status/{IP}/{port} | Returns the status (0&#x3D;down, 1&#x3D;up) of an existing ipalias for the agent. |
| [**stop**](AgentApi.md#stop) | **PUT** /mimic/agent/{agentNum}/stop | Show the agent&#39;s primary IP address |
| [**stopIpalias**](AgentApi.md#stopIpalias) | **PUT** /mimic/agent/{agentNum}/ipalias/stop/{IP}/{port} | Stops an existing ipalias for the agent. |
| [**trapConfigAdd**](AgentApi.md#trapConfigAdd) | **POST** /mimic/agent/{agentNum}/trap/config/add/{IP}/{port} | Add a trap destination to the set of destinations. |
| [**trapConfigDel**](AgentApi.md#trapConfigDel) | **DELETE** /mimic/agent/{agentNum}/trap/config/delete/{IP}/{port} | Remove a trap destination from the set of destinations. |
| [**trapConfigList**](AgentApi.md#trapConfigList) | **GET** /mimic/agent/{agentNum}/trap/config/list | List the set of trap destinations for this agent instance. |
| [**trapList**](AgentApi.md#trapList) | **GET** /mimic/agent/{agentNum}/trap/list | List the outstanding asynchronous traps for this agent instance. |


<a id="addIpalias"></a>
# **addIpalias**
> String addIpalias(agentNum, IP, port, mask, _interface)

Adds a new ipalias for the agent.

port defaults to 161 if not specified. mask defaults to the class-based network mask for the address. interface defaults to the default network interface.  If port is set to 0, the system will automatically select a port number. This is useful for client-mode protocols, such as TFTP or TOD. Upon start of an IP alias with a 0 (auto-assigned) port number, its port will change to contain the value of the selected system port.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the IP alias
    String IP = "IP_example"; // String | IP address , IPv4 or IPv6
    Integer port = 56; // Integer | SNMP port , 0 or empty for default
    String mask = "mask_example"; // String | Netmask, empty for default
    String _interface = "_interface_example"; // String | Interface. Empty for default
    try {
      String result = apiInstance.addIpalias(agentNum, IP, port, mask, _interface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#addIpalias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to add the IP alias | |
| **IP** | **String**| IP address , IPv4 or IPv6 | |
| **port** | **Integer**| SNMP port , 0 or empty for default | |
| **mask** | **String**| Netmask, empty for default | |
| **_interface** | **String**| Interface. Empty for default | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="addTimerScript"></a>
# **addTimerScript**
> String addTimerScript(agentNum, script, interval, arg)

Add a new timer script to be executed at specified interval (in msec) with the specified argument.

Add a new timer script to be executed at specified interval (in msec) with the specified argument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the timer script list
    String script = "script_example"; // String | Script name
    Integer interval = 56; // Integer | Interval in msec
    String arg = "arg_example"; // String | Arguments to the script
    try {
      String result = apiInstance.addTimerScript(agentNum, script, interval, arg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#addTimerScript");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the timer script list | |
| **script** | **String**| Script name | |
| **interval** | **Integer**| Interval in msec | |
| **arg** | **String**| Arguments to the script | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentRemove"></a>
# **agentRemove**
> String agentRemove(agentNum)

Remove the current agent.

For speed, this operation will complete asynchronously. The same synchronization considerations apply as in /mimic/agent/start.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.agentRemove(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentRemove");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStoreCopy"></a>
# **agentStoreCopy**
> String agentStoreCopy(agentNum, otherAgent)

This command copies the variable store from the other agent to this agent.

This command copies the variable store from the other agent to this agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    Integer otherAgent = 56; // Integer | Agent of the value space
    try {
      String result = apiInstance.agentStoreCopy(agentNum, otherAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStoreCopy");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |
| **otherAgent** | **Integer**| Agent of the value space | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStoreExists"></a>
# **agentStoreExists**
> String agentStoreExists(agentNum, var)

This command can be used as a predicate to ascertain the existence of a given variable.

It returns \&quot;1\&quot; if the variable exists, else \&quot;0\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.agentStoreExists(agentNum, var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStoreExists");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |
| **var** | **String**| Variable name | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStoreGet"></a>
# **agentStoreGet**
> String agentStoreGet(agentNum, var)

Fetches the value associated with a variable.

The value will be returned as a string (like all Tcl values).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.agentStoreGet(agentNum, var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStoreGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |
| **var** | **String**| Variable name | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStoreList"></a>
# **agentStoreList**
> List&lt;String&gt; agentStoreList(agentNum)

This command will return the list of variables in the said scope.

The list will be a Tcl format list with curly braces \&quot;{}\&quot; around each list element. These elements in turn are space separated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    try {
      List<String> result = apiInstance.agentStoreList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStoreList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStoreLreplace"></a>
# **agentStoreLreplace**
> String agentStoreLreplace(agentNum, var, index, body)

These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String var = "var_example"; // String | Variable name
    Integer index = 56; // Integer | Index
    String body = "body_example"; // String | Value
    try {
      String result = apiInstance.agentStoreLreplace(agentNum, var, index, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStoreLreplace");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |
| **var** | **String**| Variable name | |
| **index** | **Integer**| Index | |
| **body** | **String**| Value | [optional] |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStorePersists"></a>
# **agentStorePersists**
> String agentStorePersists(agentNum, var)

This command can be used as a predicate to ascertain the persistence of a given variable.

It returns \&quot;1\&quot; if the variable is persistent, else \&quot;0\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.agentStorePersists(agentNum, var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStorePersists");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |
| **var** | **String**| Variable name | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStoreSet"></a>
# **agentStoreSet**
> String agentStoreSet(agentNum, var, persist, body)

These commands allow the creation of a new variable, or changing an existing value.

The append sub-command will append the value to an existing variable, or create a new one. The set sub-command will overwrite an existing variable, or create a new one. The optional persist flag can be used to indicate if the variable is to be persistent as described above. By default a value of &#39;0&#39; will be implied for the persist flag. To avoid mistakes, for existing variables the persist flag can only be set. If you want to reset it, you first need to unset the variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String var = "var_example"; // String | Variable name
    Integer persist = 56; // Integer | Persistent setting
    String body = "body_example"; // String | Value
    try {
      String result = apiInstance.agentStoreSet(agentNum, var, persist, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStoreSet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |
| **var** | **String**| Variable name | |
| **persist** | **Integer**| Persistent setting | |
| **body** | **String**| Value | [optional] |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="agentStoreUnset"></a>
# **agentStoreUnset**
> String agentStoreUnset(agentNum, var)

Deletes a variable which is currently defined.

This will cleanup persistent variables if needed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent of the value space
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.agentStoreUnset(agentNum, var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#agentStoreUnset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent of the value space | |
| **var** | **String**| Variable name | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="callNew"></a>
# **callNew**
> String callNew(agentNum, IP, triplet)

Add an agent.

Add an agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    String IP = "IP_example"; // String | Primary IP
    List<Triplet> triplet = Arrays.asList(); // List<Triplet> | Created agent object
    try {
      String result = apiInstance.callNew(agentNum, IP, triplet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#callNew");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |
| **IP** | **String**| Primary IP | |
| **triplet** | [**List&lt;Triplet&gt;**](Triplet.md)| Created agent object | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="delIpalias"></a>
# **delIpalias**
> String delIpalias(agentNum, IP, port)

Deletes an existing ipalias from the agent.

port defaults to 161 if not specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to delete the IP alias
    String IP = "IP_example"; // String | IP address , IPv4 or IPv6
    Integer port = 56; // Integer | SNMP port , 0 or empty for default
    try {
      String result = apiInstance.delIpalias(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#delIpalias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to delete the IP alias | |
| **IP** | **String**| IP address , IPv4 or IPv6 | |
| **port** | **Integer**| SNMP port , 0 or empty for default | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="delTimerScript"></a>
# **delTimerScript**
> String delTimerScript(agentNum, script, interval, arg)

Remove a timer script from the execution list.

The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the timer script list
    String script = "script_example"; // String | Script name
    Integer interval = 56; // Integer | Interval in msec
    String arg = "arg_example"; // String | Arguments to the script
    try {
      String result = apiInstance.delTimerScript(agentNum, script, interval, arg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#delTimerScript");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the timer script list | |
| **script** | **String**| Script name | |
| **interval** | **Integer**| Interval in msec | |
| **arg** | **String**| Arguments to the script | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="fromAdd"></a>
# **fromAdd**
> String fromAdd(agentNum, IP, port)

Add a source address that the agent will accept messages from.

An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the IP source
    String IP = "IP_example"; // String | IP of the port, 0.0.0.0 for any
    Integer port = 56; // Integer | port of the source, 0 for any
    try {
      String result = apiInstance.fromAdd(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#fromAdd");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to add the IP source | |
| **IP** | **String**| IP of the port, 0.0.0.0 for any | |
| **port** | **Integer**| port of the source, 0 for any | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="fromDel"></a>
# **fromDel**
> String fromDel(agentNum, IP, port)

delete a source address that the agent will accept messages from.

An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to delete the IP source
    String IP = "IP_example"; // String | IP of the source
    Integer port = 56; // Integer | port of the source
    try {
      String result = apiInstance.fromDel(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#fromDel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to delete the IP source | |
| **IP** | **String**| IP of the source | |
| **port** | **Integer**| port of the source | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="fromList"></a>
# **fromList**
> List&lt;IPSource&gt; fromList(agentNum)

List the source addresses that the agent will accept messages from.

This in effect implements source-address-indexing, where 2 agents with the same address can be configured, each accepting messages from different management stations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the IP sources
    try {
      List<IPSource> result = apiInstance.fromList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#fromList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to show the IP sources | |

### Return type

[**List&lt;IPSource&gt;**](IPSource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getAgentState"></a>
# **getAgentState**
> Integer getAgentState(agentNum)

current running state of the agent

0-Unknown 1-Running 2-Stopped 3-Halted 4-Paused 5-Deleted 6-Stopping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the state
    try {
      Integer result = apiInstance.getAgentState(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getAgentState");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the state | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getChanged"></a>
# **getChanged**
> Integer getChanged(agentNum)

has the agent value space changed?

has the agent value space changed?

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the indicator
    try {
      Integer result = apiInstance.getChanged(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getChanged");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the indicator | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getConfigChanged"></a>
# **getConfigChanged**
> Integer getConfigChanged(agentNum)

has the lab configuration changed?

has the lab configuration changed?

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the indicator
    try {
      Integer result = apiInstance.getConfigChanged(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getConfigChanged");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the indicator | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getDelay"></a>
# **getDelay**
> Integer getDelay(agentNum)

one-way transit delay in msec.

The minimum granularity is 10 msec.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the delay time
    try {
      Integer result = apiInstance.getDelay(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getDelay");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the delay time | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getDrops"></a>
# **getDrops**
> Integer getDrops(agentNum)

drop rate (every N-th PDU). 0 means no drops.

drop rate (every N-th PDU). 0 means no drops.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the drop rate
    try {
      Integer result = apiInstance.getDrops(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getDrops");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the drop rate | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getHost"></a>
# **getHost**
> String getHost(agentNum)

host address of the agent.

Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.getHost(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getHost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getInformTimeout"></a>
# **getInformTimeout**
> Integer getInformTimeout(agentNum)

timeout in seconds for retransmitting INFORM PDUs.

The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the timeout setting
    try {
      Integer result = apiInstance.getInformTimeout(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getInformTimeout");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the timeout setting | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getInterface"></a>
# **getInterface**
> String getInterface(agentNum)

network interface card for the agent.

network interface card for the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary interface
    try {
      String result = apiInstance.getInterface(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getInterface");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary interface | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getMask"></a>
# **getMask**
> String getMask(agentNum)

subnet mask of the agent.

subnet mask of the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary interface
    try {
      String result = apiInstance.getMask(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getMask");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary interface | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getMibs"></a>
# **getMibs**
> List&lt;Triplet&gt; getMibs(agentNum)

set of MIBs, simulations and scenarios

set of MIBs, simulations and scenarios

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the MIB triplets
    try {
      List<Triplet> result = apiInstance.getMibs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getMibs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the MIB triplets | |

### Return type

[**List&lt;Triplet&gt;**](Triplet.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getNumberStarts"></a>
# **getNumberStarts**
> Integer getNumberStarts(agentNum)

number of starts for the agent.

This count is incremented each time an agent starts. It affects the SNMPv3 EngineBoots parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the count
    try {
      Integer result = apiInstance.getNumberStarts(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getNumberStarts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the count | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getOiddir"></a>
# **getOiddir**
> String getOiddir(agentNum)

MIB directory of the agent.

MIB directory of the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the directory path
    try {
      String result = apiInstance.getOiddir(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getOiddir");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the directory path | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getOwner"></a>
# **getOwner**
> String getOwner(agentNum)

owner of the agent.

owner of the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the owner
    try {
      String result = apiInstance.getOwner(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getOwner");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the owner | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getPdusize"></a>
# **getPdusize**
> Integer getPdusize(agentNum)

maximum PDU size.

The limit for this configurable is 65536.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the PDU size
    try {
      Integer result = apiInstance.getPdusize(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getPdusize");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the PDU size | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getPort"></a>
# **getPort**
> String getPort(agentNum)

port number

port number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary SNMP port
    try {
      String result = apiInstance.getPort(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getPort");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary SNMP port | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getPrivdir"></a>
# **getPrivdir**
> String getPrivdir(agentNum)

private directory of the agent.

private directory of the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the directory path
    try {
      String result = apiInstance.getPrivdir(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getPrivdir");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the directory path | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getProtocols"></a>
# **getProtocols**
> List&lt;String&gt; getProtocols(agentNum)

protocols supported by agent

protocols supported by agent as an array of strings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the protocols arrary
    try {
      List<String> result = apiInstance.getProtocols(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getProtocols");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the protocols arrary | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getReadCommunity"></a>
# **getReadCommunity**
> String getReadCommunity(agentNum)

read community string

read community string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the SNMP read community string
    try {
      String result = apiInstance.getReadCommunity(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getReadCommunity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the SNMP read community string | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getScen"></a>
# **getScen**
> Integer getScen(agentNum)

first scenario name

first scenario name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the first scenario number
    try {
      Integer result = apiInstance.getScen(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getScen");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the first scenario number | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getSim"></a>
# **getSim**
> String getSim(agentNum)

first simulation name

first simulation name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the first simulation name
    try {
      String result = apiInstance.getSim(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getSim");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the first simulation name | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getStarttime"></a>
# **getStarttime**
> String getStarttime(agentNum)

relative start time

relative start time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the relative start time
    try {
      String result = apiInstance.getStarttime(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getStarttime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the relative start time | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getStateChanged"></a>
# **getStateChanged**
> Integer getStateChanged(agentNum)

has the agent state changed?

has the agent state changed?

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the indicator
    try {
      Integer result = apiInstance.getStateChanged(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getStateChanged");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the indicator | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getStatistics"></a>
# **getStatistics**
> List&lt;Integer&gt; getStatistics(agentNum)

current statistics of the agent instance

The statistics are returned as 64-bit decimal numbers for the following statistics, total, discarded, error, GET, GETNEXT, SET, GETBULK, trap, GET variables, GETNEXT variables, SET variables, GETBULK variables, INFORM sent, INFORM re-sent, INFORM timed out, INFORM acked, INFORM REPORT

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the statistics
    try {
      List<Integer> result = apiInstance.getStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getStatistics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the statistics | |

### Return type

**List&lt;Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getTrace"></a>
# **getTrace**
> Integer getTrace(agentNum)

SNMP PDU tracing

SNMP PDU tracing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the indicator
    try {
      Integer result = apiInstance.getTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getTrace");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the indicator | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getValidate"></a>
# **getValidate**
> Integer getValidate(agentNum)

SNMP SET validation policy.

Is a bitmask in which with the following bits (from LSB) check for type, length, range, access

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the bitmask integer
    try {
      Integer result = apiInstance.getValidate(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getValidate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the bitmask integer | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="getWriteCommunity"></a>
# **getWriteCommunity**
> String getWriteCommunity(agentNum)

write community string

write community string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the SNMP write community string
    try {
      String result = apiInstance.getWriteCommunity(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#getWriteCommunity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the SNMP write community string | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="halt"></a>
# **halt**
> String halt(agentNum)

Halt the current agent.

Halt the current agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.halt(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#halt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="listIpaliases"></a>
# **listIpaliases**
> List&lt;IPAlias&gt; listIpaliases(agentNum)

Lists all the additional ipaliases configured for the agent.

The agent host address (set with mimic agent set host) is not in this list, since it is already accessible separately with mimic agent get host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the IP alias list
    try {
      List<IPAlias> result = apiInstance.listIpaliases(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#listIpaliases");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to show the IP alias list | |

### Return type

[**List&lt;IPAlias&gt;**](IPAlias.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="listTimerScripts"></a>
# **listTimerScripts**
> List&lt;TimerScript&gt; listTimerScripts(agentNum)

List the timer scripts currently running along with the their intervals.

The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the timer script list
    try {
      List<TimerScript> result = apiInstance.listTimerScripts(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#listTimerScripts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the timer script list | |

### Return type

[**List&lt;TimerScript&gt;**](TimerScript.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="pauseNow"></a>
# **pauseNow**
> String pauseNow(agentNum)

Pause the current agent.

Pause the current agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.pauseNow(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#pauseNow");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="protocolGetConfig"></a>
# **protocolGetConfig**
> Object protocolGetConfig(agentNum, prot)

Returns the protocol&#39;s configuration.

Returns the protocol&#39;s configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the protocol configuration
    String prot = "prot_example"; // String | Protocol to show configuration
    try {
      Object result = apiInstance.protocolGetConfig(agentNum, prot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#protocolGetConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to show the protocol configuration | |
| **prot** | **String**| Protocol to show configuration | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="reload"></a>
# **reload**
> String reload(agentNum)

Reload the current agent.

This only works for halted agents. The net effect is the same as restarting an agent (ie. stop, start, halt), but without disconnecting the network (and thus existing connections).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.reload(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#reload");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="resume"></a>
# **resume**
> String resume(agentNum)

Resume the current agent.

Resume the current agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.resume(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#resume");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="save"></a>
# **save**
> String save(agentNum)

Save agent MIB values.

Save agent MIB values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to save
    try {
      String result = apiInstance.save(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#save");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to save | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setDelay"></a>
# **setDelay**
> Integer setDelay(agentNum, delay)

one-way transit delay in msec

The minimum granularity is 10 msec.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the delay time
    Integer delay = 56; // Integer | Delay time of the agent
    try {
      Integer result = apiInstance.setDelay(agentNum, delay);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setDelay");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the delay time | |
| **delay** | **Integer**| Delay time of the agent | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setDrops"></a>
# **setDrops**
> Integer setDrops(agentNum, drops)

drop rate (every N-th PDU)

0 means no drops

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the drop rate
    Integer drops = 56; // Integer | Drop rate of the agent
    try {
      Integer result = apiInstance.setDrops(agentNum, drops);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setDrops");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the drop rate | |
| **drops** | **Integer**| Drop rate of the agent | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setHost"></a>
# **setHost**
> String setHost(agentNum, host)

host address of the agent.

Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the primary IP
    String host = "host_example"; // String | Primary IP of the agent
    try {
      String result = apiInstance.setHost(agentNum, host);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setHost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the primary IP | |
| **host** | **String**| Primary IP of the agent | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setInformTimeout"></a>
# **setInformTimeout**
> Integer setInformTimeout(agentNum, informTimeout)

timeout in seconds for retransmitting INFORM PDUs

The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the timeout setting
    Integer informTimeout = 56; // Integer | Tmeout setting
    try {
      Integer result = apiInstance.setInformTimeout(agentNum, informTimeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setInformTimeout");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the timeout setting | |
| **informTimeout** | **Integer**| Tmeout setting | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setInterface"></a>
# **setInterface**
> String setInterface(agentNum, _interface)

network interface card for the agent

network interface card for the agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the primary interface
    String _interface = "_interface_example"; // String | Primary interface of the agent
    try {
      String result = apiInstance.setInterface(agentNum, _interface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setInterface");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the primary interface | |
| **_interface** | **String**| Primary interface of the agent | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setMask"></a>
# **setMask**
> String setMask(agentNum, mask)

subnet mask of the agent.

subnet mask of the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the primary IP address mask
    String mask = "mask_example"; // String | Mask to set for the agent primary IP address
    try {
      String result = apiInstance.setMask(agentNum, mask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setMask");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the primary IP address mask | |
| **mask** | **String**| Mask to set for the agent primary IP address | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setMibs"></a>
# **setMibs**
> String setMibs(agentNum, triplet)

set of MIBs, simulations and scenarios

set of MIBs, simulations and scenarios

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the MIB triplets
    List<Triplet> triplet = Arrays.asList(); // List<Triplet> | 
    try {
      String result = apiInstance.setMibs(agentNum, triplet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setMibs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the MIB triplets | |
| **triplet** | [**List&lt;Triplet&gt;**](Triplet.md)|  | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setOiddir"></a>
# **setOiddir**
> String setOiddir(agentNum, oiddir)

MIB directory of the agent.

MIB directory of the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the directory path
    String oiddir = "oiddir_example"; // String | Directory path for the agent
    try {
      String result = apiInstance.setOiddir(agentNum, oiddir);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setOiddir");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the directory path | |
| **oiddir** | **String**| Directory path for the agent | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setOwner"></a>
# **setOwner**
> String setOwner(agentNum, owner)

owner of the agent

owner of the agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the owner
    String owner = "owner_example"; // String | Owner of the agent
    try {
      String result = apiInstance.setOwner(agentNum, owner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setOwner");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the owner | |
| **owner** | **String**| Owner of the agent | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setPdusize"></a>
# **setPdusize**
> Integer setPdusize(agentNum, pdusize)

maximum PDU size

The limit for this configurable is 65536

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the PDU size
    Integer pdusize = 56; // Integer | PDU size setting for the agent
    try {
      Integer result = apiInstance.setPdusize(agentNum, pdusize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setPdusize");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the PDU size | |
| **pdusize** | **Integer**| PDU size setting for the agent | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setPort"></a>
# **setPort**
> String setPort(agentNum, port)

port number

port number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the primary SNMP port
    Integer port = 56; // Integer | Primary SNMP port of the agent
    try {
      String result = apiInstance.setPort(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setPort");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the primary SNMP port | |
| **port** | **Integer**| Primary SNMP port of the agent | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setPrivdir"></a>
# **setPrivdir**
> String setPrivdir(agentNum, privdir)

private directory of the agent.

private directory of the agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the directory path
    String privdir = "privdir_example"; // String | Directory path for the agent
    try {
      String result = apiInstance.setPrivdir(agentNum, privdir);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setPrivdir");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the directory path | |
| **privdir** | **String**| Directory path for the agent | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setProtocols"></a>
# **setProtocols**
> List&lt;Integer&gt; setProtocols(agentNum, requestBody)

protocols supported by agent as a comma-separated list

protocols supported by agent as a comma-separated list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the protocols arrary
    List<String> requestBody = Arrays.asList(); // List<String> | Created agent object
    try {
      List<Integer> result = apiInstance.setProtocols(agentNum, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setProtocols");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the protocols arrary | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| Created agent object | |

### Return type

**List&lt;Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setReadCommunity"></a>
# **setReadCommunity**
> String setReadCommunity(agentNum, read)

read community string

read community string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the SNMP read community string
    String read = "read_example"; // String | SNMP read community string
    try {
      String result = apiInstance.setReadCommunity(agentNum, read);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setReadCommunity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the SNMP read community string | |
| **read** | **String**| SNMP read community string | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setStarttime"></a>
# **setStarttime**
> String setStarttime(agentNum, start)

relative start time

relative start time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the relative start time
    Integer start = 56; // Integer | Relative start time of the agent
    try {
      String result = apiInstance.setStarttime(agentNum, start);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setStarttime");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the relative start time | |
| **start** | **Integer**| Relative start time of the agent | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setTrace"></a>
# **setTrace**
> Integer setTrace(agentNum, trace)

SNMP PDU tracing

SNMP PDU tracing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set trace setting
    Integer trace = 56; // Integer | Trace setting for the agent
    try {
      Integer result = apiInstance.setTrace(agentNum, trace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setTrace");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set trace setting | |
| **trace** | **Integer**| Trace setting for the agent | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setValidate"></a>
# **setValidate**
> Integer setValidate(agentNum, validate)

SNMP SET validation policy

Is a bitmask in which with the following bits (from LSB) check for type, length, range, access. A default value of 65535 does all validation checking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the bitmask integer
    Integer validate = 56; // Integer | Bitmask integer to set
    try {
      Integer result = apiInstance.setValidate(agentNum, validate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setValidate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the bitmask integer | |
| **validate** | **Integer**| Bitmask integer to set | |

### Return type

**Integer**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="setWriteCommunity"></a>
# **setWriteCommunity**
> String setWriteCommunity(agentNum, write)

write community string

write community string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SNMP write community string
    String write = "write_example"; // String | SNMP write community string
    try {
      String result = apiInstance.setWriteCommunity(agentNum, write);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#setWriteCommunity");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to set the SNMP write community string | |
| **write** | **String**| SNMP write community string | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="start"></a>
# **start**
> String start(agentNum)

Start the current agent.

For speed, this operation will complete asynchronously. A successful return from this command means the starting of the agent is in progress. If you need to rely on the agent to have completed startup, you should wait for it&#39;s state to become RUNNING.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.start(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#start");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="startIpalias"></a>
# **startIpalias**
> String startIpalias(agentNum, IP, port)

Starts an existing ipalias for the agent.

port defaults to 161 if not specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to start the IP alias
    String IP = "IP_example"; // String | IP address , IPv4 or IPv6
    Integer port = 56; // Integer | SNMP port , 0 or empty for default
    try {
      String result = apiInstance.startIpalias(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#startIpalias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to start the IP alias | |
| **IP** | **String**| IP address , IPv4 or IPv6 | |
| **port** | **Integer**| SNMP port , 0 or empty for default | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="statusIpalias"></a>
# **statusIpalias**
> String statusIpalias(agentNum, IP, port)

Returns the status (0&#x3D;down, 1&#x3D;up) of an existing ipalias for the agent.

port defaults to 161 if not specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show status of the IP alias
    String IP = "IP_example"; // String | IP address , IPv4 or IPv6
    Integer port = 56; // Integer | SNMP port , 0 or empty for default
    try {
      String result = apiInstance.statusIpalias(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#statusIpalias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to show status of the IP alias | |
| **IP** | **String**| IP address , IPv4 or IPv6 | |
| **port** | **Integer**| SNMP port , 0 or empty for default | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="stop"></a>
# **stop**
> String stop(agentNum)

Show the agent&#39;s primary IP address

Agent primary IP address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to return the primary IP
    try {
      String result = apiInstance.stop(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#stop");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to return the primary IP | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="stopIpalias"></a>
# **stopIpalias**
> String stopIpalias(agentNum, IP, port)

Stops an existing ipalias for the agent.

port defaults to 161 if not specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to stop the IP alias
    String IP = "IP_example"; // String | IP address , IPv4 or IPv6
    Integer port = 56; // Integer | SNMP port , 0 or empty for default
    try {
      String result = apiInstance.stopIpalias(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#stopIpalias");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to stop the IP alias | |
| **IP** | **String**| IP address , IPv4 or IPv6 | |
| **port** | **Integer**| SNMP port , 0 or empty for default | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="trapConfigAdd"></a>
# **trapConfigAdd**
> String trapConfigAdd(agentNum, IP, port)

Add a trap destination to the set of destinations.

Add a trap destination to the set of destinations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add the destination
    String IP = "IP_example"; // String | IP of the destination
    Integer port = 56; // Integer | port of the destination
    try {
      String result = apiInstance.trapConfigAdd(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#trapConfigAdd");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to add the destination | |
| **IP** | **String**| IP of the destination | |
| **port** | **Integer**| port of the destination | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="trapConfigDel"></a>
# **trapConfigDel**
> String trapConfigDel(agentNum, IP, port)

Remove a trap destination from the set of destinations.

Remove a trap destination from the set of destinations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to delete the destination
    String IP = "IP_example"; // String | IP of the destination
    Integer port = 56; // Integer | port of the destination
    try {
      String result = apiInstance.trapConfigDel(agentNum, IP, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#trapConfigDel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to delete the destination | |
| **IP** | **String**| IP of the destination | |
| **port** | **Integer**| port of the destination | |

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="trapConfigList"></a>
# **trapConfigList**
> List&lt;TrapDest&gt; trapConfigList(agentNum)

List the set of trap destinations for this agent instance.

Each trap destination is identified with an IP address and a port number. The default port number is the standard SNMP trap port 162.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the IP alias list
    try {
      List<TrapDest> result = apiInstance.trapConfigList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#trapConfigList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to show the IP alias list | |

### Return type

[**List&lt;TrapDest&gt;**](TrapDest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid agent number value |  -  |

<a id="trapList"></a>
# **trapList**
> List&lt;String&gt; trapList(agentNum)

List the outstanding asynchronous traps for this agent instance.

List the outstanding asynchronous traps for this agent instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AgentApi apiInstance = new AgentApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to list the traps
    try {
      List<String> result = apiInstance.trapList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgentApi#trapList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agentNum** | **Integer**| Agent to list the traps | |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


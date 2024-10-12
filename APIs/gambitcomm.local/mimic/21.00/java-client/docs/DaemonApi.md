# DaemonApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addDaemonTimerScript**](DaemonApi.md#addDaemonTimerScript) | **POST** /mimic/timer/script/add/{script}/{interval}/{arg} | Add a new timer script to be executed at specified interval (in msec) with the specified argument. |
| [**cfgLoad**](DaemonApi.md#cfgLoad) | **PUT** /mimic/load/{cfgFile}/{firstAgentNum}/{lastAgentNum}/{startAgentNum} | Load the lab configuration file file. |
| [**cfgNew**](DaemonApi.md#cfgNew) | **PUT** /mimic/clear/{firstAgentNum}/{lastAgentNum} | Clear the lab configuration. |
| [**cfgSave**](DaemonApi.md#cfgSave) | **PUT** /mimic/save | Save the lab configuration. |
| [**cfgSaveas**](DaemonApi.md#cfgSaveas) | **PUT** /mimic/saveas/{cfgFile}/{firstAgentNum}/{lastAgentNum} | Save the lab configuration in file. |
| [**delDaemonTimerScript**](DaemonApi.md#delDaemonTimerScript) | **DELETE** /mimic/timer/script/delete/{script}/{interval}/{arg} | Remove a timer script from the execution list. |
| [**getActiveDataList**](DaemonApi.md#getActiveDataList) | **GET** /mimic/get/active_data_list | The list of {agentnum {statistics}} for agents that are currently active and whose statistics have changed since the last invocation of this command. |
| [**getActiveList**](DaemonApi.md#getActiveList) | **GET** /mimic/get/active_list | The list of {agentnum} that are currently active (running or paused). |
| [**getCfgFileChanged**](DaemonApi.md#getCfgFileChanged) | **GET** /mimic/get/cfgfile_changed | This predicate indicates if the currently loaded agent configuration file has changed. |
| [**getCfgfile**](DaemonApi.md#getCfgfile) | **GET** /mimic/get/cfgfile | The currently loaded lab configuration file for the particular user. |
| [**getChangedConfigList**](DaemonApi.md#getChangedConfigList) | **GET** /mimic/get/changed_config_list | The list of {agentnum} for which a configurable parameter changed. |
| [**getChangedStateList**](DaemonApi.md#getChangedStateList) | **GET** /mimic/get/changed_state_list | The list of {agentnum state} for which the state changed. |
| [**getClients**](DaemonApi.md#getClients) | **GET** /mimic/get/clients | The number of clients currently connected to the daemon. |
| [**getConfiguredList**](DaemonApi.md#getConfiguredList) | **GET** /mimic/get/configured_list | The list of {agentnum} that are currently configured. |
| [**getDaemonProtocols**](DaemonApi.md#getDaemonProtocols) | **GET** /mimic/get/protocols | The set of protocols supported by the Simulator. |
| [**getInterfaces**](DaemonApi.md#getInterfaces) | **GET** /mimic/get/interfaces | The set of network interfaces that can be used for simulations. |
| [**getLast**](DaemonApi.md#getLast) | **GET** /mimic/get/last | The last configured agent instance. |
| [**getLog**](DaemonApi.md#getLog) | **GET** /mimic/get/log | The current log file for the Simulator. |
| [**getMax**](DaemonApi.md#getMax) | **GET** /mimic/get/max | The maximum number of agent instances. |
| [**getNetaddr**](DaemonApi.md#getNetaddr) | **GET** /mimic/get/netaddr | The network address of the host where the MIMIC simulator is running. |
| [**getNetdev**](DaemonApi.md#getNetdev) | **GET** /mimic/get/netdev | The default network device to be used for agent addresses. |
| [**getProduct**](DaemonApi.md#getProduct) | **GET** /mimic/get/product | The product number that is licensed. |
| [**getReturn**](DaemonApi.md#getReturn) | **GET** /mimic/get/return | The return mode. |
| [**getVersion**](DaemonApi.md#getVersion) | **GET** /mimic/get/version | The version of the MIMIC command interface. |
| [**listDaemonTimerScripts**](DaemonApi.md#listDaemonTimerScripts) | **GET** /mimic/timer/script/list | List the timer scripts currently running along with the their intervals. |
| [**mgetInfo**](DaemonApi.md#mgetInfo) | **GET** /mimic/mget/{infoArray} | Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command. |
| [**setLog**](DaemonApi.md#setLog) | **PUT** /mimic/set/log | The current log file for the Simulator. |
| [**setNetdev**](DaemonApi.md#setNetdev) | **PUT** /mimic/set/netdev | The network address of the host where the MIMIC simulator is running. |
| [**startAllAgents**](DaemonApi.md#startAllAgents) | **PUT** /mimic/start | Start MIMIC. |
| [**stopAllAgents**](DaemonApi.md#stopAllAgents) | **PUT** /mimic/stop | Stop MIMIC. |
| [**storeExists**](DaemonApi.md#storeExists) | **GET** /mimic/store/exists/{var} | This command can be used as a predicate to ascertain the existence of a given variable. |
| [**storeGet**](DaemonApi.md#storeGet) | **GET** /mimic/store/get/{var} | Fetches the value associated with a variable. |
| [**storeList**](DaemonApi.md#storeList) | **GET** /mimic/store/list | This command will return the list of variables in the said scope. |
| [**storeLreplace**](DaemonApi.md#storeLreplace) | **PUT** /mimic/store/lreplace/{var}/{index} | These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist. |
| [**storePersists**](DaemonApi.md#storePersists) | **GET** /mimic/store/persists/{var} | This command can be used as a predicate to ascertain the persistence of a given variable. |
| [**storeSave**](DaemonApi.md#storeSave) | **PUT** /mimic/set/persistent | This operation flushes all global objects which need to be made persistent to disk. |
| [**storeSet**](DaemonApi.md#storeSet) | **PUT** /mimic/store/set/{var}/{persist} | Set the variable store for the global storage |
| [**storeUnset**](DaemonApi.md#storeUnset) | **PUT** /mimic/store/unset/{var} | Deletes a variable which is currently defined. |
| [**terminate**](DaemonApi.md#terminate) | **PUT** /mimic/terminate | Terminate the MIMIC daemon. |


<a id="addDaemonTimerScript"></a>
# **addDaemonTimerScript**
> String addDaemonTimerScript(script, interval, arg)

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String script = "script_example"; // String | Script name
    Integer interval = 56; // Integer | Interval in msec
    String arg = "arg_example"; // String | Arguments to the script
    try {
      String result = apiInstance.addDaemonTimerScript(script, interval, arg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#addDaemonTimerScript");
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

<a id="cfgLoad"></a>
# **cfgLoad**
> Map&lt;String, Integer&gt; cfgLoad(cfgFile, firstAgentNum, lastAgentNum, startAgentNum)

Load the lab configuration file file.

Load agents in cfgFile from firstAgentNum to lastAgentNum on startAgentNum of current configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String cfgFile = "cfgFile_example"; // String | MIMIC agent configuration file to load
    Integer firstAgentNum = 56; // Integer | Agent number in cfgFile to start the loading
    Integer lastAgentNum = 56; // Integer | Agent number in cfgFile to end the loading
    Integer startAgentNum = 56; // Integer | Agent number in current configuration to start placing the new agents
    try {
      Map<String, Integer> result = apiInstance.cfgLoad(cfgFile, firstAgentNum, lastAgentNum, startAgentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#cfgLoad");
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
| **cfgFile** | **String**| MIMIC agent configuration file to load | |
| **firstAgentNum** | **Integer**| Agent number in cfgFile to start the loading | |
| **lastAgentNum** | **Integer**| Agent number in cfgFile to end the loading | |
| **startAgentNum** | **Integer**| Agent number in current configuration to start placing the new agents | |

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cfgNew"></a>
# **cfgNew**
> Map&lt;String, Integer&gt; cfgNew(firstAgentNum, lastAgentNum)

Clear the lab configuration.

Clear the lab configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    Integer firstAgentNum = 56; // Integer | Agent number to start clearing
    Integer lastAgentNum = 56; // Integer | Agent number to end the clearing
    try {
      Map<String, Integer> result = apiInstance.cfgNew(firstAgentNum, lastAgentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#cfgNew");
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
| **firstAgentNum** | **Integer**| Agent number to start clearing | |
| **lastAgentNum** | **Integer**| Agent number to end the clearing | |

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cfgSave"></a>
# **cfgSave**
> Map&lt;String, Integer&gt; cfgSave()

Save the lab configuration.

Save the lab configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.cfgSave();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#cfgSave");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="cfgSaveas"></a>
# **cfgSaveas**
> Map&lt;String, Integer&gt; cfgSaveas(cfgFile, firstAgentNum, lastAgentNum)

Save the lab configuration in file.

Save the lab configuration in file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String cfgFile = "cfgFile_example"; // String | MIMIC agent configuration file to save
    Integer firstAgentNum = 56; // Integer | Agent number in cfgFile to start the loading
    Integer lastAgentNum = 56; // Integer | Agent number in cfgFile to end the loading
    try {
      Map<String, Integer> result = apiInstance.cfgSaveas(cfgFile, firstAgentNum, lastAgentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#cfgSaveas");
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
| **cfgFile** | **String**| MIMIC agent configuration file to save | |
| **firstAgentNum** | **Integer**| Agent number in cfgFile to start the loading | |
| **lastAgentNum** | **Integer**| Agent number in cfgFile to end the loading | |

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="delDaemonTimerScript"></a>
# **delDaemonTimerScript**
> String delDaemonTimerScript(script, interval, arg)

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String script = "script_example"; // String | Script name
    Integer interval = 56; // Integer | Interval in msec
    String arg = "arg_example"; // String | Arguments to the script
    try {
      String result = apiInstance.delDaemonTimerScript(script, interval, arg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#delDaemonTimerScript");
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

<a id="getActiveDataList"></a>
# **getActiveDataList**
> List&lt;Integer&gt; getActiveDataList()

The list of {agentnum {statistics}} for agents that are currently active and whose statistics have changed since the last invocation of this command.

This list is guaranteed to be sorted into increasing order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      List<Integer> result = apiInstance.getActiveDataList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getActiveDataList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getActiveList"></a>
# **getActiveList**
> List&lt;Integer&gt; getActiveList()

The list of {agentnum} that are currently active (running or paused).

This list is guaranteed to be sorted into increasing order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      List<Integer> result = apiInstance.getActiveList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getActiveList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getCfgFileChanged"></a>
# **getCfgFileChanged**
> Map&lt;String, Integer&gt; getCfgFileChanged()

This predicate indicates if the currently loaded agent configuration file has changed.

Whether the loaded agent configuration file has changed since the last time this predicate was queried. This allows for a client to detect agent configuration changes and to synchronize those changes from the MIMIC daemon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getCfgFileChanged();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getCfgFileChanged");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getCfgfile"></a>
# **getCfgfile**
> Map&lt;String, Integer&gt; getCfgfile()

The currently loaded lab configuration file for the particular user.

In the case of multi-user access this command returns a different configuration file loaded for each user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getCfgfile();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getCfgfile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getChangedConfigList"></a>
# **getChangedConfigList**
> List&lt;Integer&gt; getChangedConfigList()

The list of {agentnum} for which a configurable parameter changed.

This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      List<Integer> result = apiInstance.getChangedConfigList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getChangedConfigList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getChangedStateList"></a>
# **getChangedStateList**
> List&lt;AgentState&gt; getChangedStateList()

The list of {agentnum state} for which the state changed.

This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      List<AgentState> result = apiInstance.getChangedStateList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getChangedStateList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;AgentState&gt;**](AgentState.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getClients"></a>
# **getClients**
> Map&lt;String, Integer&gt; getClients()

The number of clients currently connected to the daemon.

The number of clients currently connected to the daemon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getClients();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getClients");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getConfiguredList"></a>
# **getConfiguredList**
> List&lt;Integer&gt; getConfiguredList()

The list of {agentnum} that are currently configured.

This list is guaranteed to be sorted into increasing order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      List<Integer> result = apiInstance.getConfiguredList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getConfiguredList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getDaemonProtocols"></a>
# **getDaemonProtocols**
> Map&lt;String, Integer&gt; getDaemonProtocols()

The set of protocols supported by the Simulator.

The set of protocols supported by the Simulator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getDaemonProtocols();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getDaemonProtocols");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getInterfaces"></a>
# **getInterfaces**
> Map&lt;String, Integer&gt; getInterfaces()

The set of network interfaces that can be used for simulations.

The set of network interfaces that can be used for simulations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getInterfaces();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getInterfaces");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getLast"></a>
# **getLast**
> Integer getLast()

The last configured agent instance.

The last configured agent instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Integer result = apiInstance.getLast();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getLast");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getLog"></a>
# **getLog**
> Map&lt;String, Integer&gt; getLog()

The current log file for the Simulator.

The current log file for the Simulator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getLog();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getLog");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getMax"></a>
# **getMax**
> Integer getMax()

The maximum number of agent instances.

The maximum number of agent instances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Integer result = apiInstance.getMax();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getMax");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="getNetaddr"></a>
# **getNetaddr**
> Map&lt;String, Integer&gt; getNetaddr()

The network address of the host where the MIMIC simulator is running.

The network address of the host where the MIMIC simulator is running.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getNetaddr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getNetaddr");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getNetdev"></a>
# **getNetdev**
> Map&lt;String, Integer&gt; getNetdev()

The default network device to be used for agent addresses.

The default network device to be used for agent addresses if the interface is not explicitly specified for an agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getNetdev();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getNetdev");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getProduct"></a>
# **getProduct**
> Map&lt;String, Integer&gt; getProduct()

The product number that is licensed.

The product number that is licensed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getProduct();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getProduct");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getReturn"></a>
# **getReturn**
> Map&lt;String, Integer&gt; getReturn()

The return mode.

The OpenAPI daemon operates in two modes, nocatch, where error returns from MIMIC operations return error; or catch, where the TCL catch semantics are used (these are similar to C++ exceptions)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.getReturn();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getReturn");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getVersion"></a>
# **getVersion**
> String getVersion()

The version of the MIMIC command interface.

The version of the MIMIC command interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      String result = apiInstance.getVersion();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getVersion");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="listDaemonTimerScripts"></a>
# **listDaemonTimerScripts**
> List&lt;TimerScript&gt; listDaemonTimerScripts()

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      List<TimerScript> result = apiInstance.listDaemonTimerScripts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#listDaemonTimerScripts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="mgetInfo"></a>
# **mgetInfo**
> List&lt;Object&gt; mgetInfo(infoArray)

Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    List<String> infoArray = Arrays.asList(); // List<String> | Multiple strings of info.
    try {
      List<Object> result = apiInstance.mgetInfo(infoArray);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#mgetInfo");
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
| **infoArray** | [**List&lt;String&gt;**](String.md)| Multiple strings of info. | |

### Return type

**List&lt;Object&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid info string |  -  |

<a id="setLog"></a>
# **setLog**
> String setLog(body)

The current log file for the Simulator.

The current log file for the Simulator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String body = "body_example"; // String | The file name of the new log file
    try {
      String result = apiInstance.setLog(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#setLog");
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
| **body** | **String**| The file name of the new log file | |

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

<a id="setNetdev"></a>
# **setNetdev**
> Map&lt;String, Integer&gt; setNetdev()

The network address of the host where the MIMIC simulator is running.

The network address of the host where the MIMIC simulator is running.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.setNetdev();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#setNetdev");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="startAllAgents"></a>
# **startAllAgents**
> Map&lt;String, Integer&gt; startAllAgents()

Start MIMIC.

Start MIMIC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.startAllAgents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#startAllAgents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="stopAllAgents"></a>
# **stopAllAgents**
> Map&lt;String, Integer&gt; stopAllAgents()

Stop MIMIC.

Stop MIMIC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.stopAllAgents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#stopAllAgents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="storeExists"></a>
# **storeExists**
> String storeExists(var)

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.storeExists(var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storeExists");
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

<a id="storeGet"></a>
# **storeGet**
> String storeGet(var)

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.storeGet(var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storeGet");
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

<a id="storeList"></a>
# **storeList**
> List&lt;String&gt; storeList()

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      List<String> result = apiInstance.storeList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storeList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

<a id="storeLreplace"></a>
# **storeLreplace**
> String storeLreplace(var, index, body)

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String var = "var_example"; // String | Variable name
    Integer index = 56; // Integer | Index
    String body = "body_example"; // String | Value
    try {
      String result = apiInstance.storeLreplace(var, index, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storeLreplace");
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

<a id="storePersists"></a>
# **storePersists**
> String storePersists(var)

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.storePersists(var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storePersists");
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

<a id="storeSave"></a>
# **storeSave**
> Map&lt;String, Integer&gt; storeSave()

This operation flushes all global objects which need to be made persistent to disk.

The MIMIC daemon caches persistent objects and their changes, and writes them to disk at program termination. If it were to crash, these changes would be lost. This operation allows to checkpoint the cache, ie. write changes to persistent objects to disk. To save the lab configuration with per-agent persistent information the mimic save operation needs to be used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.storeSave();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storeSave");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="storeSet"></a>
# **storeSet**
> String storeSet(var, persist, body)

Set the variable store for the global storage

Persist 1 means persistent , 0 means non-persistent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String var = "var_example"; // String | Variable name
    Integer persist = 56; // Integer | Persistent setting
    String body = "body_example"; // String | Value
    try {
      String result = apiInstance.storeSet(var, persist, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storeSet");
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

<a id="storeUnset"></a>
# **storeUnset**
> String storeUnset(var)

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
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String var = "var_example"; // String | Variable name
    try {
      String result = apiInstance.storeUnset(var);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#storeUnset");
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

<a id="terminate"></a>
# **terminate**
> Map&lt;String, Integer&gt; terminate()

Terminate the MIMIC daemon.

Terminate the MIMIC daemon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    try {
      Map<String, Integer> result = apiInstance.terminate();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#terminate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


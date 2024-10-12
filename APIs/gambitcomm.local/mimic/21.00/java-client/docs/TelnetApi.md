# TelnetApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolTelnetConnectionLogon**](TelnetApi.md#protocolTelnetConnectionLogon) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/connection/logon/{connectionID}/{user}/{password} | Changes the connection&#39;s current logon. |
| [**protocolTelnetConnectionRequest**](TelnetApi.md#protocolTelnetConnectionRequest) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/connection/request/{connectionID}/{command} | Executes the command asynchronously . |
| [**protocolTelnetConnectionSignal**](TelnetApi.md#protocolTelnetConnectionSignal) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/connection/signal/{connectionID}/{signalName} | Triggers the asynchronous signal event with the specified signal name |
| [**protocolTelnetGetArgs**](TelnetApi.md#protocolTelnetGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/args | Show the agent&#39;s TELNET argument structure |
| [**protocolTelnetGetConfig**](TelnetApi.md#protocolTelnetGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/config | Show the agent&#39;s TELNET configuration |
| [**protocolTelnetGetStatistics**](TelnetApi.md#protocolTelnetGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/statistics | Show the agent&#39;s TELNET statistics |
| [**protocolTelnetGetStatsHdr**](TelnetApi.md#protocolTelnetGetStatsHdr) | **GET** /mimic/protocol/msg/telnet/get/stats_hdr | Show the TELNET statistics headers |
| [**protocolTelnetGetTrace**](TelnetApi.md#protocolTelnetGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/get/trace | Show the agent&#39;s TELNET traffic tracing |
| [**protocolTelnetIpaliasDisable**](TelnetApi.md#protocolTelnetIpaliasDisable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/disable/{ipaddress}/{port} | Disable individual IP aliases on the agent and the simulator host |
| [**protocolTelnetIpaliasEnable**](TelnetApi.md#protocolTelnetIpaliasEnable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/enable/{ipaddress}/{port} | Enable individual IP aliases on the agent and the simulator host |
| [**protocolTelnetIpaliasIsenabled**](TelnetApi.md#protocolTelnetIpaliasIsenabled) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/isenabled/{ipaddress}/{port} | Check individual IP aliases on the agent and the simulator host |
| [**protocolTelnetIpaliasList**](TelnetApi.md#protocolTelnetIpaliasList) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/ipalias/list | List all IP aliases on the agent and the simulator host |
| [**protocolTelnetServerGetConnections**](TelnetApi.md#protocolTelnetServerGetConnections) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/connections | Show the agent&#39;s TELNET connections |
| [**protocolTelnetServerGetKeymap**](TelnetApi.md#protocolTelnetServerGetKeymap) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/keymap | Show the agent&#39;s TELNET keymap file name |
| [**protocolTelnetServerGetRulesdb**](TelnetApi.md#protocolTelnetServerGetRulesdb) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/rulesdb | Show the agent&#39;s TELNET rules db file name |
| [**protocolTelnetServerGetState**](TelnetApi.md#protocolTelnetServerGetState) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/state | Show the agent&#39;s TELNET server state |
| [**protocolTelnetServerGetUserdb**](TelnetApi.md#protocolTelnetServerGetUserdb) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/userdb | Show the agent&#39;s TELNET user db file name |
| [**protocolTelnetServerGetUsers**](TelnetApi.md#protocolTelnetServerGetUsers) | **GET** /mimic/agent/{agentNum}/protocol/msg/telnet/server/get/users | Show the agent&#39;s TELNET users |
| [**protocolTelnetSetConfig**](TelnetApi.md#protocolTelnetSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/set/config/{argument}/{value} | Set the agent&#39;s TELNET configuration |
| [**protocolTelnetSetTrace**](TelnetApi.md#protocolTelnetSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/telnet/set/trace/{enableOrNot} | Set the agent&#39;s TELNET traffic tracing |


<a id="protocolTelnetConnectionLogon"></a>
# **protocolTelnetConnectionLogon**
> List&lt;String&gt; protocolTelnetConnectionLogon(agentNum, connectionID, user, password)

Changes the connection&#39;s current logon.

Logon change allows (hidden) commands for a different access mode to run.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate TELNET connection
    Integer connectionID = 56; // Integer | 
    String user = "user_example"; // String | 
    String password = "password_example"; // String | 
    try {
      List<String> result = apiInstance.protocolTelnetConnectionLogon(agentNum, connectionID, user, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetConnectionLogon");
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
| **agentNum** | **Integer**| Agent to manipulate TELNET connection | |
| **connectionID** | **Integer**|  | |
| **user** | **String**|  | |
| **password** | **String**|  | |

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

<a id="protocolTelnetConnectionRequest"></a>
# **protocolTelnetConnectionRequest**
> List&lt;String&gt; protocolTelnetConnectionRequest(agentNum, connectionID, command)

Executes the command asynchronously .

Equivalent of the command typed in by the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate TELNET connection
    Integer connectionID = 56; // Integer | 
    String command = "command_example"; // String | 
    try {
      List<String> result = apiInstance.protocolTelnetConnectionRequest(agentNum, connectionID, command);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetConnectionRequest");
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
| **agentNum** | **Integer**| Agent to manipulate TELNET connection | |
| **connectionID** | **Integer**|  | |
| **command** | **String**|  | |

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

<a id="protocolTelnetConnectionSignal"></a>
# **protocolTelnetConnectionSignal**
> List&lt;String&gt; protocolTelnetConnectionSignal(agentNum, connectionID, signalName)

Triggers the asynchronous signal event with the specified signal name

Signal name is either connect or idle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate TELNET connection
    Integer connectionID = 56; // Integer | 
    String signalName = "signalName_example"; // String | 
    try {
      List<String> result = apiInstance.protocolTelnetConnectionSignal(agentNum, connectionID, signalName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetConnectionSignal");
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
| **agentNum** | **Integer**| Agent to manipulate TELNET connection | |
| **connectionID** | **Integer**|  | |
| **signalName** | **String**|  | |

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

<a id="protocolTelnetGetArgs"></a>
# **protocolTelnetGetArgs**
> Object protocolTelnetGetArgs(agentNum)

Show the agent&#39;s TELNET argument structure

Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the TELNET argument structure
    try {
      Object result = apiInstance.protocolTelnetGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetGetArgs");
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
| **agentNum** | **Integer**| Agent to show the TELNET argument structure | |

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

<a id="protocolTelnetGetConfig"></a>
# **protocolTelnetGetConfig**
> ConfigTELNET protocolTelnetGetConfig(agentNum)

Show the agent&#39;s TELNET configuration

Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the TELNET configuration
    try {
      ConfigTELNET result = apiInstance.protocolTelnetGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetGetConfig");
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
| **agentNum** | **Integer**| Agent to show the TELNET configuration | |

### Return type

[**ConfigTELNET**](ConfigTELNET.md)

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

<a id="protocolTelnetGetStatistics"></a>
# **protocolTelnetGetStatistics**
> List&lt;Integer&gt; protocolTelnetGetStatistics(agentNum)

Show the agent&#39;s TELNET statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TELNET statistics
    try {
      List<Integer> result = apiInstance.protocolTelnetGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetGetStatistics");
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
| **agentNum** | **Integer**| Agent to show TELNET statistics | |

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

<a id="protocolTelnetGetStatsHdr"></a>
# **protocolTelnetGetStatsHdr**
> List&lt;String&gt; protocolTelnetGetStatsHdr()

Show the TELNET statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolTelnetGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetGetStatsHdr");
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

<a id="protocolTelnetGetTrace"></a>
# **protocolTelnetGetTrace**
> ConfigTELNET protocolTelnetGetTrace(agentNum)

Show the agent&#39;s TELNET traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether TELNET tracing is enabled
    try {
      ConfigTELNET result = apiInstance.protocolTelnetGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether TELNET tracing is enabled | |

### Return type

[**ConfigTELNET**](ConfigTELNET.md)

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

<a id="protocolTelnetIpaliasDisable"></a>
# **protocolTelnetIpaliasDisable**
> String protocolTelnetIpaliasDisable(agentNum, ipaddress, port)

Disable individual IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate TELNET IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolTelnetIpaliasDisable(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetIpaliasDisable");
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
| **agentNum** | **Integer**| Agent to manipulate TELNET IP alias | |
| **ipaddress** | **String**|  | |
| **port** | **Integer**|  | |

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

<a id="protocolTelnetIpaliasEnable"></a>
# **protocolTelnetIpaliasEnable**
> String protocolTelnetIpaliasEnable(agentNum, ipaddress, port)

Enable individual IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate TELNET IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolTelnetIpaliasEnable(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetIpaliasEnable");
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
| **agentNum** | **Integer**| Agent to manipulate TELNET IP alias | |
| **ipaddress** | **String**|  | |
| **port** | **Integer**|  | |

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

<a id="protocolTelnetIpaliasIsenabled"></a>
# **protocolTelnetIpaliasIsenabled**
> String protocolTelnetIpaliasIsenabled(agentNum, ipaddress, port)

Check individual IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate TELNET IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolTelnetIpaliasIsenabled(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetIpaliasIsenabled");
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
| **agentNum** | **Integer**| Agent to manipulate TELNET IP alias | |
| **ipaddress** | **String**|  | |
| **port** | **Integer**|  | |

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

<a id="protocolTelnetIpaliasList"></a>
# **protocolTelnetIpaliasList**
> List&lt;IPAlias&gt; protocolTelnetIpaliasList(agentNum)

List all IP aliases on the agent and the simulator host

By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate TELNET IP alias
    try {
      List<IPAlias> result = apiInstance.protocolTelnetIpaliasList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetIpaliasList");
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
| **agentNum** | **Integer**| Agent to manipulate TELNET IP alias | |

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

<a id="protocolTelnetServerGetConnections"></a>
# **protocolTelnetServerGetConnections**
> List&lt;Integer&gt; protocolTelnetServerGetConnections(agentNum)

Show the agent&#39;s TELNET connections

IDs of all connected connections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TELNET configuration
    try {
      List<Integer> result = apiInstance.protocolTelnetServerGetConnections(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetServerGetConnections");
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
| **agentNum** | **Integer**| Agent to show TELNET configuration | |

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

<a id="protocolTelnetServerGetKeymap"></a>
# **protocolTelnetServerGetKeymap**
> List&lt;String&gt; protocolTelnetServerGetKeymap(agentNum)

Show the agent&#39;s TELNET keymap file name

Keymap file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TELNET statistics
    try {
      List<String> result = apiInstance.protocolTelnetServerGetKeymap(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetServerGetKeymap");
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
| **agentNum** | **Integer**| Agent to show TELNET statistics | |

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

<a id="protocolTelnetServerGetRulesdb"></a>
# **protocolTelnetServerGetRulesdb**
> List&lt;String&gt; protocolTelnetServerGetRulesdb(agentNum)

Show the agent&#39;s TELNET rules db file name

Rules db file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TELNET statistics
    try {
      List<String> result = apiInstance.protocolTelnetServerGetRulesdb(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetServerGetRulesdb");
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
| **agentNum** | **Integer**| Agent to show TELNET statistics | |

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

<a id="protocolTelnetServerGetState"></a>
# **protocolTelnetServerGetState**
> List&lt;Integer&gt; protocolTelnetServerGetState(agentNum)

Show the agent&#39;s TELNET server state

Return 1 means accepting connections, 0 not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TELNET statistics
    try {
      List<Integer> result = apiInstance.protocolTelnetServerGetState(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetServerGetState");
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
| **agentNum** | **Integer**| Agent to show TELNET statistics | |

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

<a id="protocolTelnetServerGetUserdb"></a>
# **protocolTelnetServerGetUserdb**
> List&lt;String&gt; protocolTelnetServerGetUserdb(agentNum)

Show the agent&#39;s TELNET user db file name

User db file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TELNET statistics
    try {
      List<String> result = apiInstance.protocolTelnetServerGetUserdb(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetServerGetUserdb");
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
| **agentNum** | **Integer**| Agent to show TELNET statistics | |

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

<a id="protocolTelnetServerGetUsers"></a>
# **protocolTelnetServerGetUsers**
> List&lt;TelnetUser&gt; protocolTelnetServerGetUsers(agentNum)

Show the agent&#39;s TELNET users

List of users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TELNET configuration
    try {
      List<TelnetUser> result = apiInstance.protocolTelnetServerGetUsers(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetServerGetUsers");
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
| **agentNum** | **Integer**| Agent to show TELNET configuration | |

### Return type

[**List&lt;TelnetUser&gt;**](TelnetUser.md)

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

<a id="protocolTelnetSetConfig"></a>
# **protocolTelnetSetConfig**
> String protocolTelnetSetConfig(agentNum, argument, value)

Set the agent&#39;s TELNET configuration

Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the TELNET configuration
    String argument = "argument_example"; // String | Parameter to set the TELNET configuration
    String value = "value_example"; // String | Value to set the TELNET configuration
    try {
      String result = apiInstance.protocolTelnetSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetSetConfig");
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
| **agentNum** | **Integer**| Agent to set the TELNET configuration | |
| **argument** | **String**| Parameter to set the TELNET configuration | |
| **value** | **String**| Value to set the TELNET configuration | |

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

<a id="protocolTelnetSetTrace"></a>
# **protocolTelnetSetTrace**
> String protocolTelnetSetTrace(agentNum, enableOrNot)

Set the agent&#39;s TELNET traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TelnetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TelnetApi apiInstance = new TelnetApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the TELNET tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the TELNET tracing
    try {
      String result = apiInstance.protocolTelnetSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TelnetApi#protocolTelnetSetTrace");
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
| **agentNum** | **Integer**| Agent to set the TELNET tracing | |
| **enableOrNot** | **String**| Value to set the TELNET tracing | |

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


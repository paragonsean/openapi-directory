# SnmptcpApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolSnmptcpGetArgs**](SnmptcpApi.md#protocolSnmptcpGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/args | Show the agent&#39;s SNMPTCP argument structure |
| [**protocolSnmptcpGetConfig**](SnmptcpApi.md#protocolSnmptcpGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/config | Show the agent&#39;s SNMPTCP configuration |
| [**protocolSnmptcpGetStatistics**](SnmptcpApi.md#protocolSnmptcpGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/statistics | Show the agent&#39;s SNMPTCP statistics |
| [**protocolSnmptcpGetStatsHdr**](SnmptcpApi.md#protocolSnmptcpGetStatsHdr) | **GET** /mimic/protocol/msg/snmptcp/get/stats_hdr | Show the SNMPTCP statistics headers |
| [**protocolSnmptcpGetTrace**](SnmptcpApi.md#protocolSnmptcpGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/get/trace | Show the agent&#39;s SNMPTCP traffic tracing |
| [**protocolSnmptcpIpaliasDisable**](SnmptcpApi.md#protocolSnmptcpIpaliasDisable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/disable/{ipaddress}/{port} | Disable individual IP aliases on the agent and the simulator host |
| [**protocolSnmptcpIpaliasEnable**](SnmptcpApi.md#protocolSnmptcpIpaliasEnable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/enable/{ipaddress}/{port} | Enable individual IP aliases on the agent and the simulator host |
| [**protocolSnmptcpIpaliasIsenabled**](SnmptcpApi.md#protocolSnmptcpIpaliasIsenabled) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/isenabled/{ipaddress}/{port} | Check individual IP aliases on the agent and the simulator host |
| [**protocolSnmptcpIpaliasList**](SnmptcpApi.md#protocolSnmptcpIpaliasList) | **GET** /mimic/agent/{agentNum}/protocol/msg/snmptcp/ipalias/list | List all IP aliases on the agent and the simulator host |
| [**protocolSnmptcpSetConfig**](SnmptcpApi.md#protocolSnmptcpSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/set/config/{argument}/{value} | Set the agent&#39;s SNMPTCP configuration |
| [**protocolSnmptcpSetTrace**](SnmptcpApi.md#protocolSnmptcpSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/snmptcp/set/trace/{enableOrNot} | Set the agent&#39;s SNMPTCP traffic tracing |


<a id="protocolSnmptcpGetArgs"></a>
# **protocolSnmptcpGetArgs**
> Object protocolSnmptcpGetArgs(agentNum)

Show the agent&#39;s SNMPTCP argument structure

Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPTCP argument structure
    try {
      Object result = apiInstance.protocolSnmptcpGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpGetArgs");
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
| **agentNum** | **Integer**| Agent to show the SNMPTCP argument structure | |

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

<a id="protocolSnmptcpGetConfig"></a>
# **protocolSnmptcpGetConfig**
> ConfigSNMPTCP protocolSnmptcpGetConfig(agentNum)

Show the agent&#39;s SNMPTCP configuration

Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SNMPTCP configuration
    try {
      ConfigSNMPTCP result = apiInstance.protocolSnmptcpGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpGetConfig");
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
| **agentNum** | **Integer**| Agent to show the SNMPTCP configuration | |

### Return type

[**ConfigSNMPTCP**](ConfigSNMPTCP.md)

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

<a id="protocolSnmptcpGetStatistics"></a>
# **protocolSnmptcpGetStatistics**
> List&lt;Integer&gt; protocolSnmptcpGetStatistics(agentNum)

Show the agent&#39;s SNMPTCP statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show SNMPTCP statistics
    try {
      List<Integer> result = apiInstance.protocolSnmptcpGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpGetStatistics");
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
| **agentNum** | **Integer**| Agent to show SNMPTCP statistics | |

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

<a id="protocolSnmptcpGetStatsHdr"></a>
# **protocolSnmptcpGetStatsHdr**
> List&lt;String&gt; protocolSnmptcpGetStatsHdr()

Show the SNMPTCP statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolSnmptcpGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpGetStatsHdr");
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

<a id="protocolSnmptcpGetTrace"></a>
# **protocolSnmptcpGetTrace**
> ConfigSNMPTCP protocolSnmptcpGetTrace(agentNum)

Show the agent&#39;s SNMPTCP traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether SNMPTCP tracing is enabled
    try {
      ConfigSNMPTCP result = apiInstance.protocolSnmptcpGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether SNMPTCP tracing is enabled | |

### Return type

[**ConfigSNMPTCP**](ConfigSNMPTCP.md)

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

<a id="protocolSnmptcpIpaliasDisable"></a>
# **protocolSnmptcpIpaliasDisable**
> String protocolSnmptcpIpaliasDisable(agentNum, ipaddress, port)

Disable individual IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SNMPTCP IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolSnmptcpIpaliasDisable(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpIpaliasDisable");
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
| **agentNum** | **Integer**| Agent to manipulate SNMPTCP IP alias | |
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

<a id="protocolSnmptcpIpaliasEnable"></a>
# **protocolSnmptcpIpaliasEnable**
> String protocolSnmptcpIpaliasEnable(agentNum, ipaddress, port)

Enable individual IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SNMPTCP IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolSnmptcpIpaliasEnable(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpIpaliasEnable");
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
| **agentNum** | **Integer**| Agent to manipulate SNMPTCP IP alias | |
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

<a id="protocolSnmptcpIpaliasIsenabled"></a>
# **protocolSnmptcpIpaliasIsenabled**
> String protocolSnmptcpIpaliasIsenabled(agentNum, ipaddress, port)

Check individual IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SNMPTCP IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolSnmptcpIpaliasIsenabled(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpIpaliasIsenabled");
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
| **agentNum** | **Integer**| Agent to manipulate SNMPTCP IP alias | |
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

<a id="protocolSnmptcpIpaliasList"></a>
# **protocolSnmptcpIpaliasList**
> List&lt;IPAlias&gt; protocolSnmptcpIpaliasList(agentNum)

List all IP aliases on the agent and the simulator host

By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SNMPTCP IP alias
    try {
      List<IPAlias> result = apiInstance.protocolSnmptcpIpaliasList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpIpaliasList");
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
| **agentNum** | **Integer**| Agent to manipulate SNMPTCP IP alias | |

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

<a id="protocolSnmptcpSetConfig"></a>
# **protocolSnmptcpSetConfig**
> String protocolSnmptcpSetConfig(agentNum, argument, value)

Set the agent&#39;s SNMPTCP configuration

Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SNMPTCP configuration
    String argument = "argument_example"; // String | Parameter to set the SNMPTCP configuration
    String value = "value_example"; // String | Value to set the SNMPTCP configuration
    try {
      String result = apiInstance.protocolSnmptcpSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpSetConfig");
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
| **agentNum** | **Integer**| Agent to set the SNMPTCP configuration | |
| **argument** | **String**| Parameter to set the SNMPTCP configuration | |
| **value** | **String**| Value to set the SNMPTCP configuration | |

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

<a id="protocolSnmptcpSetTrace"></a>
# **protocolSnmptcpSetTrace**
> String protocolSnmptcpSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SNMPTCP traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnmptcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SnmptcpApi apiInstance = new SnmptcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SNMPTCP tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the SNMPTCP tracing
    try {
      String result = apiInstance.protocolSnmptcpSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnmptcpApi#protocolSnmptcpSetTrace");
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
| **agentNum** | **Integer**| Agent to set the SNMPTCP tracing | |
| **enableOrNot** | **String**| Value to set the SNMPTCP tracing | |

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


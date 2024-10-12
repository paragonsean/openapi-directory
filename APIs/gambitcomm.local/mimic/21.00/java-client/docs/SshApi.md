# SshApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolSshGetArgs**](SshApi.md#protocolSshGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/args | Show the agent&#39;s SSH argument structure |
| [**protocolSshGetConfig**](SshApi.md#protocolSshGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/config | Show the agent&#39;s SSH configuration |
| [**protocolSshGetStatistics**](SshApi.md#protocolSshGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/statistics | Show the agent&#39;s SSH statistics |
| [**protocolSshGetStatsHdr**](SshApi.md#protocolSshGetStatsHdr) | **GET** /mimic/protocol/msg/ssh/get/stats_hdr | Show the SSH statistics headers |
| [**protocolSshGetTrace**](SshApi.md#protocolSshGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/get/trace | Show the agent&#39;s SSH traffic tracing |
| [**protocolSshIpaliasDisable**](SshApi.md#protocolSshIpaliasDisable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/disable/{ipaddress}/{port} | Disable individual IP aliases on the agent and the simulator host |
| [**protocolSshIpaliasEnable**](SshApi.md#protocolSshIpaliasEnable) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/enable/{ipaddress}/{port} | Enable individual IP aliases on the agent and the simulator host |
| [**protocolSshIpaliasIsenabled**](SshApi.md#protocolSshIpaliasIsenabled) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/isenabled/{ipaddress}/{port} | Check individual IP aliases on the agent and the simulator host |
| [**protocolSshIpaliasList**](SshApi.md#protocolSshIpaliasList) | **GET** /mimic/agent/{agentNum}/protocol/msg/ssh/ipalias/list | List all IP aliases on the agent and the simulator host |
| [**protocolSshSetConfig**](SshApi.md#protocolSshSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/set/config/{argument}/{value} | Set the agent&#39;s SSH configuration |
| [**protocolSshSetTrace**](SshApi.md#protocolSshSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ssh/set/trace/{enableOrNot} | Set the agent&#39;s SSH traffic tracing |


<a id="protocolSshGetArgs"></a>
# **protocolSshGetArgs**
> Object protocolSshGetArgs(agentNum)

Show the agent&#39;s SSH argument structure

Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SSH argument structure
    try {
      Object result = apiInstance.protocolSshGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshGetArgs");
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
| **agentNum** | **Integer**| Agent to show the SSH argument structure | |

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

<a id="protocolSshGetConfig"></a>
# **protocolSshGetConfig**
> ConfigSSH protocolSshGetConfig(agentNum)

Show the agent&#39;s SSH configuration

Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SSH configuration
    try {
      ConfigSSH result = apiInstance.protocolSshGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshGetConfig");
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
| **agentNum** | **Integer**| Agent to show the SSH configuration | |

### Return type

[**ConfigSSH**](ConfigSSH.md)

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

<a id="protocolSshGetStatistics"></a>
# **protocolSshGetStatistics**
> List&lt;Integer&gt; protocolSshGetStatistics(agentNum)

Show the agent&#39;s SSH statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show SSH statistics
    try {
      List<Integer> result = apiInstance.protocolSshGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshGetStatistics");
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
| **agentNum** | **Integer**| Agent to show SSH statistics | |

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

<a id="protocolSshGetStatsHdr"></a>
# **protocolSshGetStatsHdr**
> List&lt;String&gt; protocolSshGetStatsHdr()

Show the SSH statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolSshGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshGetStatsHdr");
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

<a id="protocolSshGetTrace"></a>
# **protocolSshGetTrace**
> ConfigSSH protocolSshGetTrace(agentNum)

Show the agent&#39;s SSH traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether SSH tracing is enabled
    try {
      ConfigSSH result = apiInstance.protocolSshGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether SSH tracing is enabled | |

### Return type

[**ConfigSSH**](ConfigSSH.md)

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

<a id="protocolSshIpaliasDisable"></a>
# **protocolSshIpaliasDisable**
> String protocolSshIpaliasDisable(agentNum, ipaddress, port)

Disable individual IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SSH IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolSshIpaliasDisable(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshIpaliasDisable");
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
| **agentNum** | **Integer**| Agent to manipulate SSH IP alias | |
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

<a id="protocolSshIpaliasEnable"></a>
# **protocolSshIpaliasEnable**
> String protocolSshIpaliasEnable(agentNum, ipaddress, port)

Enable individual IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SSH IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolSshIpaliasEnable(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshIpaliasEnable");
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
| **agentNum** | **Integer**| Agent to manipulate SSH IP alias | |
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

<a id="protocolSshIpaliasIsenabled"></a>
# **protocolSshIpaliasIsenabled**
> String protocolSshIpaliasIsenabled(agentNum, ipaddress, port)

Check individual IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SSH IP alias
    String ipaddress = "ipaddress_example"; // String | 
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolSshIpaliasIsenabled(agentNum, ipaddress, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshIpaliasIsenabled");
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
| **agentNum** | **Integer**| Agent to manipulate SSH IP alias | |
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

<a id="protocolSshIpaliasList"></a>
# **protocolSshIpaliasList**
> List&lt;IPAlias&gt; protocolSshIpaliasList(agentNum)

List all IP aliases on the agent and the simulator host

By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate SSH IP alias
    try {
      List<IPAlias> result = apiInstance.protocolSshIpaliasList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshIpaliasList");
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
| **agentNum** | **Integer**| Agent to manipulate SSH IP alias | |

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

<a id="protocolSshSetConfig"></a>
# **protocolSshSetConfig**
> String protocolSshSetConfig(agentNum, argument, value)

Set the agent&#39;s SSH configuration

Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SSH configuration
    String argument = "argument_example"; // String | Parameter to set the SSH configuration
    String value = "value_example"; // String | Value to set the SSH configuration
    try {
      String result = apiInstance.protocolSshSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshSetConfig");
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
| **agentNum** | **Integer**| Agent to set the SSH configuration | |
| **argument** | **String**| Parameter to set the SSH configuration | |
| **value** | **String**| Value to set the SSH configuration | |

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

<a id="protocolSshSetTrace"></a>
# **protocolSshSetTrace**
> String protocolSshSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SSH traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SshApi apiInstance = new SshApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SSH tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the SSH tracing
    try {
      String result = apiInstance.protocolSshSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshApi#protocolSshSetTrace");
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
| **agentNum** | **Integer**| Agent to set the SSH tracing | |
| **enableOrNot** | **String**| Value to set the SSH tracing | |

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


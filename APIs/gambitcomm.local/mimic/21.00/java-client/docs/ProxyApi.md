# ProxyApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolProxyGetArgs**](ProxyApi.md#protocolProxyGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/args | Show the agent&#39;s PROXY argument structure |
| [**protocolProxyGetConfig**](ProxyApi.md#protocolProxyGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/config | Show the agent&#39;s PROXY configuration |
| [**protocolProxyGetStatistics**](ProxyApi.md#protocolProxyGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/statistics | Show the agent&#39;s PROXY statistics |
| [**protocolProxyGetStatsHdr**](ProxyApi.md#protocolProxyGetStatsHdr) | **GET** /mimic/protocol/msg/proxy/get/stats_hdr | Show the PROXY statistics headers |
| [**protocolProxyGetTrace**](ProxyApi.md#protocolProxyGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/get/trace | Show the agent&#39;s PROXY traffic tracing |
| [**protocolProxyPortAdd**](ProxyApi.md#protocolProxyPortAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/proxy/port/add/{port}/{target}/{targetPort} | Add individual proxy target on the agent and the simulator host |
| [**protocolProxyPortIsstarted**](ProxyApi.md#protocolProxyPortIsstarted) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/port/isStarted/{port} | Check individual target |
| [**protocolProxyPortList**](ProxyApi.md#protocolProxyPortList) | **GET** /mimic/agent/{agentNum}/protocol/msg/proxy/port/list | List all proxy targets |
| [**protocolProxyPortRemove**](ProxyApi.md#protocolProxyPortRemove) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/proxy/port/remove/{port} | Remove individual proxy target on the agent and the simulator host |
| [**protocolProxyPortStart**](ProxyApi.md#protocolProxyPortStart) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/port/start/{port} | Start additional target |
| [**protocolProxyPortStop**](ProxyApi.md#protocolProxyPortStop) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/port/stop/{port} | Stop additional target |
| [**protocolProxySetConfig**](ProxyApi.md#protocolProxySetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/set/config/{argument}/{value} | Set the agent&#39;s PROXY configuration |
| [**protocolProxySetTrace**](ProxyApi.md#protocolProxySetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/proxy/set/trace/{enableOrNot} | Set the agent&#39;s PROXY traffic tracing |


<a id="protocolProxyGetArgs"></a>
# **protocolProxyGetArgs**
> Object protocolProxyGetArgs(agentNum)

Show the agent&#39;s PROXY argument structure

Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the PROXY argument structure
    try {
      Object result = apiInstance.protocolProxyGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyGetArgs");
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
| **agentNum** | **Integer**| Agent to show the PROXY argument structure | |

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

<a id="protocolProxyGetConfig"></a>
# **protocolProxyGetConfig**
> ConfigPROXY protocolProxyGetConfig(agentNum)

Show the agent&#39;s PROXY configuration

Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the PROXY configuration
    try {
      ConfigPROXY result = apiInstance.protocolProxyGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyGetConfig");
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
| **agentNum** | **Integer**| Agent to show the PROXY configuration | |

### Return type

[**ConfigPROXY**](ConfigPROXY.md)

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

<a id="protocolProxyGetStatistics"></a>
# **protocolProxyGetStatistics**
> List&lt;Integer&gt; protocolProxyGetStatistics(agentNum)

Show the agent&#39;s PROXY statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show PROXY statistics
    try {
      List<Integer> result = apiInstance.protocolProxyGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyGetStatistics");
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
| **agentNum** | **Integer**| Agent to show PROXY statistics | |

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

<a id="protocolProxyGetStatsHdr"></a>
# **protocolProxyGetStatsHdr**
> List&lt;String&gt; protocolProxyGetStatsHdr()

Show the PROXY statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolProxyGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyGetStatsHdr");
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

<a id="protocolProxyGetTrace"></a>
# **protocolProxyGetTrace**
> ConfigPROXY protocolProxyGetTrace(agentNum)

Show the agent&#39;s PROXY traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether PROXY tracing is enabled
    try {
      ConfigPROXY result = apiInstance.protocolProxyGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether PROXY tracing is enabled | |

### Return type

[**ConfigPROXY**](ConfigPROXY.md)

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

<a id="protocolProxyPortAdd"></a>
# **protocolProxyPortAdd**
> String protocolProxyPortAdd(agentNum, port, target, targetPort)

Add individual proxy target on the agent and the simulator host

Additional proxy target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate PROXY target
    Integer port = 56; // Integer | 
    String target = "target_example"; // String | 
    Integer targetPort = 56; // Integer | 
    try {
      String result = apiInstance.protocolProxyPortAdd(agentNum, port, target, targetPort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyPortAdd");
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
| **agentNum** | **Integer**| Agent to manipulate PROXY target | |
| **port** | **Integer**|  | |
| **target** | **String**|  | |
| **targetPort** | **Integer**|  | |

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

<a id="protocolProxyPortIsstarted"></a>
# **protocolProxyPortIsstarted**
> String protocolProxyPortIsstarted(agentNum, port)

Check individual target

Check individual target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate PROXY target
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolProxyPortIsstarted(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyPortIsstarted");
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
| **agentNum** | **Integer**| Agent to manipulate PROXY target | |
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

<a id="protocolProxyPortList"></a>
# **protocolProxyPortList**
> List&lt;Integer&gt; protocolProxyPortList(agentNum)

List all proxy targets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate PROXY target
    try {
      List<Integer> result = apiInstance.protocolProxyPortList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyPortList");
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
| **agentNum** | **Integer**| Agent to manipulate PROXY target | |

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

<a id="protocolProxyPortRemove"></a>
# **protocolProxyPortRemove**
> String protocolProxyPortRemove(agentNum, port)

Remove individual proxy target on the agent and the simulator host

Remove proxy target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate PROXY target
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolProxyPortRemove(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyPortRemove");
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
| **agentNum** | **Integer**| Agent to manipulate PROXY target | |
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

<a id="protocolProxyPortStart"></a>
# **protocolProxyPortStart**
> String protocolProxyPortStart(agentNum, port)

Start additional target

Start additional target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate PROXY target
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolProxyPortStart(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyPortStart");
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
| **agentNum** | **Integer**| Agent to manipulate PROXY target | |
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

<a id="protocolProxyPortStop"></a>
# **protocolProxyPortStop**
> String protocolProxyPortStop(agentNum, port)

Stop additional target

Stop additional target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to manipulate PROXY target
    Integer port = 56; // Integer | 
    try {
      String result = apiInstance.protocolProxyPortStop(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxyPortStop");
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
| **agentNum** | **Integer**| Agent to manipulate PROXY target | |
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

<a id="protocolProxySetConfig"></a>
# **protocolProxySetConfig**
> String protocolProxySetConfig(agentNum, argument, value)

Set the agent&#39;s PROXY configuration

Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the PROXY configuration
    String argument = "argument_example"; // String | Parameter to set the PROXY configuration
    String value = "value_example"; // String | Value to set the PROXY configuration
    try {
      String result = apiInstance.protocolProxySetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxySetConfig");
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
| **agentNum** | **Integer**| Agent to set the PROXY configuration | |
| **argument** | **String**| Parameter to set the PROXY configuration | |
| **value** | **String**| Value to set the PROXY configuration | |

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

<a id="protocolProxySetTrace"></a>
# **protocolProxySetTrace**
> String protocolProxySetTrace(agentNum, enableOrNot)

Set the agent&#39;s PROXY traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the PROXY tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the PROXY tracing
    try {
      String result = apiInstance.protocolProxySetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#protocolProxySetTrace");
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
| **agentNum** | **Integer**| Agent to set the PROXY tracing | |
| **enableOrNot** | **String**| Value to set the PROXY tracing | |

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


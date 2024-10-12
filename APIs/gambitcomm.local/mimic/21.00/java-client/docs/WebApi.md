# WebApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolWebGetArgs**](WebApi.md#protocolWebGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/args | Show the agent&#39;s WEB argument structure |
| [**protocolWebGetConfig**](WebApi.md#protocolWebGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/config | Show the agent&#39;s WEB configuration |
| [**protocolWebGetStatistics**](WebApi.md#protocolWebGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/statistics | Show the agent&#39;s WEB statistics |
| [**protocolWebGetStatsHdr**](WebApi.md#protocolWebGetStatsHdr) | **GET** /mimic/protocol/msg/web/get/stats_hdr | Show the WEB statistics headers |
| [**protocolWebGetTrace**](WebApi.md#protocolWebGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/get/trace | Show the agent&#39;s WEB traffic tracing |
| [**protocolWebPortAdd**](WebApi.md#protocolWebPortAdd) | **POST** /mimic/agent/{agentNum}/protocol/msg/web/port/add/{port} | Add the agent&#39;s WEB port |
| [**protocolWebPortExists**](WebApi.md#protocolWebPortExists) | **GET** /mimic/agent/{agentNum}/protocol/msg/web/port/exists/{port} | Show the agent&#39;s WEB port |
| [**protocolWebPortRemove**](WebApi.md#protocolWebPortRemove) | **DELETE** /mimic/agent/{agentNum}/protocol/msg/web/port/remove/{port} | Remove the agent&#39;s WEB port |
| [**protocolWebPortSet**](WebApi.md#protocolWebPortSet) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/port/set/{port}/{protocol}/{version} | Set the agent&#39;s WEB port attribute |
| [**protocolWebPortStart**](WebApi.md#protocolWebPortStart) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/port/start/{port} | Start the agent&#39;s WEB port |
| [**protocolWebPortStop**](WebApi.md#protocolWebPortStop) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/port/stop/{port} | Stop the agent&#39;s WEB port |
| [**protocolWebSetConfig**](WebApi.md#protocolWebSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/set/config/{argument}/{value} | Set the agent&#39;s WEB configuration |
| [**protocolWebSetTrace**](WebApi.md#protocolWebSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/web/set/trace/{enableOrNot} | Set the agent&#39;s WEB traffic tracing |


<a id="protocolWebGetArgs"></a>
# **protocolWebGetArgs**
> Object protocolWebGetArgs(agentNum)

Show the agent&#39;s WEB argument structure

Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the WEB argument structure
    try {
      Object result = apiInstance.protocolWebGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebGetArgs");
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
| **agentNum** | **Integer**| Agent to show the WEB argument structure | |

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

<a id="protocolWebGetConfig"></a>
# **protocolWebGetConfig**
> ConfigWEB protocolWebGetConfig(agentNum)

Show the agent&#39;s WEB configuration

Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the WEB configuration
    try {
      ConfigWEB result = apiInstance.protocolWebGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebGetConfig");
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
| **agentNum** | **Integer**| Agent to show the WEB configuration | |

### Return type

[**ConfigWEB**](ConfigWEB.md)

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

<a id="protocolWebGetStatistics"></a>
# **protocolWebGetStatistics**
> List&lt;Integer&gt; protocolWebGetStatistics(agentNum)

Show the agent&#39;s WEB statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show WEB statistics
    try {
      List<Integer> result = apiInstance.protocolWebGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebGetStatistics");
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
| **agentNum** | **Integer**| Agent to show WEB statistics | |

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

<a id="protocolWebGetStatsHdr"></a>
# **protocolWebGetStatsHdr**
> List&lt;String&gt; protocolWebGetStatsHdr()

Show the WEB statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolWebGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebGetStatsHdr");
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

<a id="protocolWebGetTrace"></a>
# **protocolWebGetTrace**
> ConfigWEB protocolWebGetTrace(agentNum)

Show the agent&#39;s WEB traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether WEB tracing is enabled
    try {
      ConfigWEB result = apiInstance.protocolWebGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether WEB tracing is enabled | |

### Return type

[**ConfigWEB**](ConfigWEB.md)

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

<a id="protocolWebPortAdd"></a>
# **protocolWebPortAdd**
> String protocolWebPortAdd(agentNum, port)

Add the agent&#39;s WEB port

Add port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to add WEB port
    Integer port = 56; // Integer | TCP port
    try {
      String result = apiInstance.protocolWebPortAdd(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebPortAdd");
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
| **agentNum** | **Integer**| Agent to add WEB port | |
| **port** | **Integer**| TCP port | |

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

<a id="protocolWebPortExists"></a>
# **protocolWebPortExists**
> List&lt;String&gt; protocolWebPortExists(agentNum, port)

Show the agent&#39;s WEB port

Check the port. 1 means existing, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show WEB configuration
    Integer port = 56; // Integer | TCP port
    try {
      List<String> result = apiInstance.protocolWebPortExists(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebPortExists");
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
| **agentNum** | **Integer**| Agent to show WEB configuration | |
| **port** | **Integer**| TCP port | |

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

<a id="protocolWebPortRemove"></a>
# **protocolWebPortRemove**
> String protocolWebPortRemove(agentNum, port)

Remove the agent&#39;s WEB port

Remove port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to remove WEB port
    Integer port = 56; // Integer | TCP port
    try {
      String result = apiInstance.protocolWebPortRemove(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebPortRemove");
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
| **agentNum** | **Integer**| Agent to remove WEB port | |
| **port** | **Integer**| TCP port | |

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

<a id="protocolWebPortSet"></a>
# **protocolWebPortSet**
> String protocolWebPortSet(agentNum, port, protocol, version)

Set the agent&#39;s WEB port attribute

Set port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set WEB port
    Integer port = 56; // Integer | TCP port
    String protocol = "protocol_example"; // String | Encryption or related protocol
    String version = "version_example"; // String | Encryption or related protocol version
    try {
      String result = apiInstance.protocolWebPortSet(agentNum, port, protocol, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebPortSet");
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
| **agentNum** | **Integer**| Agent to set WEB port | |
| **port** | **Integer**| TCP port | |
| **protocol** | **String**| Encryption or related protocol | |
| **version** | **String**| Encryption or related protocol version | |

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

<a id="protocolWebPortStart"></a>
# **protocolWebPortStart**
> String protocolWebPortStart(agentNum, port)

Start the agent&#39;s WEB port

Start port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to start WEB port
    Integer port = 56; // Integer | TCP port
    try {
      String result = apiInstance.protocolWebPortStart(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebPortStart");
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
| **agentNum** | **Integer**| Agent to start WEB port | |
| **port** | **Integer**| TCP port | |

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

<a id="protocolWebPortStop"></a>
# **protocolWebPortStop**
> String protocolWebPortStop(agentNum, port)

Stop the agent&#39;s WEB port

Stop port

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to stop WEB port
    Integer port = 56; // Integer | TCP port
    try {
      String result = apiInstance.protocolWebPortStop(agentNum, port);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebPortStop");
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
| **agentNum** | **Integer**| Agent to stop WEB port | |
| **port** | **Integer**| TCP port | |

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

<a id="protocolWebSetConfig"></a>
# **protocolWebSetConfig**
> String protocolWebSetConfig(agentNum, argument, value)

Set the agent&#39;s WEB configuration

Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the WEB configuration
    String argument = "argument_example"; // String | Parameter to set the WEB configuration
    String value = "value_example"; // String | Value to set the WEB configuration
    try {
      String result = apiInstance.protocolWebSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebSetConfig");
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
| **agentNum** | **Integer**| Agent to set the WEB configuration | |
| **argument** | **String**| Parameter to set the WEB configuration | |
| **value** | **String**| Value to set the WEB configuration | |

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

<a id="protocolWebSetTrace"></a>
# **protocolWebSetTrace**
> String protocolWebSetTrace(agentNum, enableOrNot)

Set the agent&#39;s WEB traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebApi apiInstance = new WebApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the WEB tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the WEB tracing
    try {
      String result = apiInstance.protocolWebSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApi#protocolWebSetTrace");
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
| **agentNum** | **Integer**| Agent to set the WEB tracing | |
| **enableOrNot** | **String**| Value to set the WEB tracing | |

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


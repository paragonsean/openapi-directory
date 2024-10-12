# SyslogApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolSyslogGetArgs**](SyslogApi.md#protocolSyslogGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/args | Show the agent&#39;s SYSLOG argument structure |
| [**protocolSyslogGetAttr**](SyslogApi.md#protocolSyslogGetAttr) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/{attr} | Show the outgoing message&#39;s attributes |
| [**protocolSyslogGetConfig**](SyslogApi.md#protocolSyslogGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/config | Show the agent&#39;s SYSLOG configuration |
| [**protocolSyslogGetStatistics**](SyslogApi.md#protocolSyslogGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/statistics | Show the agent&#39;s SYSLOG statistics |
| [**protocolSyslogGetStatsHdr**](SyslogApi.md#protocolSyslogGetStatsHdr) | **GET** /mimic/protocol/msg/syslog/get/stats_hdr | Show the SYSLOG statistics headers |
| [**protocolSyslogGetTrace**](SyslogApi.md#protocolSyslogGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/syslog/get/trace | Show the agent&#39;s SYSLOG traffic tracing |
| [**protocolSyslogSend**](SyslogApi.md#protocolSyslogSend) | **POST** /mimic/agent/{agentNum}/protocol/msg/syslog/send/{pri} | Set the agent&#39;s SYSLOG traffic tracing |
| [**protocolSyslogSetAttr**](SyslogApi.md#protocolSyslogSetAttr) | **PUT** /mimic/agent/{agentNum}/protocol/msg/syslog/set/{attr}/{value} | Set the outgoing message&#39;s attributes |
| [**protocolSyslogSetConfig**](SyslogApi.md#protocolSyslogSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/syslog/set/config/{argument}/{value} | Set the agent&#39;s SYSLOG configuration |
| [**protocolSyslogSetTrace**](SyslogApi.md#protocolSyslogSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/syslog/set/trace/{enableOrNot} | Set the agent&#39;s SYSLOG traffic tracing |


<a id="protocolSyslogGetArgs"></a>
# **protocolSyslogGetArgs**
> Object protocolSyslogGetArgs(agentNum)

Show the agent&#39;s SYSLOG argument structure

Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SYSLOG argument structure
    try {
      Object result = apiInstance.protocolSyslogGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogGetArgs");
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
| **agentNum** | **Integer**| Agent to show the SYSLOG argument structure | |

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

<a id="protocolSyslogGetAttr"></a>
# **protocolSyslogGetAttr**
> String protocolSyslogGetAttr(agentNum, attr)

Show the outgoing message&#39;s attributes

Attribute can be server , sequence , separator , hostname , timestamp

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SYSLOG tracing
    String attr = "attr_example"; // String | Attribute
    try {
      String result = apiInstance.protocolSyslogGetAttr(agentNum, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogGetAttr");
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
| **agentNum** | **Integer**| Agent to set the SYSLOG tracing | |
| **attr** | **String**| Attribute | |

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

<a id="protocolSyslogGetConfig"></a>
# **protocolSyslogGetConfig**
> ConfigSYSLOG protocolSyslogGetConfig(agentNum)

Show the agent&#39;s SYSLOG configuration

Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SYSLOG configuration
    try {
      ConfigSYSLOG result = apiInstance.protocolSyslogGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogGetConfig");
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
| **agentNum** | **Integer**| Agent to show the SYSLOG configuration | |

### Return type

[**ConfigSYSLOG**](ConfigSYSLOG.md)

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

<a id="protocolSyslogGetStatistics"></a>
# **protocolSyslogGetStatistics**
> List&lt;Integer&gt; protocolSyslogGetStatistics(agentNum)

Show the agent&#39;s SYSLOG statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show SYSLOG statistics
    try {
      List<Integer> result = apiInstance.protocolSyslogGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogGetStatistics");
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
| **agentNum** | **Integer**| Agent to show SYSLOG statistics | |

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

<a id="protocolSyslogGetStatsHdr"></a>
# **protocolSyslogGetStatsHdr**
> List&lt;String&gt; protocolSyslogGetStatsHdr()

Show the SYSLOG statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolSyslogGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogGetStatsHdr");
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

<a id="protocolSyslogGetTrace"></a>
# **protocolSyslogGetTrace**
> ConfigSYSLOG protocolSyslogGetTrace(agentNum)

Show the agent&#39;s SYSLOG traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether SYSLOG tracing is enabled
    try {
      ConfigSYSLOG result = apiInstance.protocolSyslogGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether SYSLOG tracing is enabled | |

### Return type

[**ConfigSYSLOG**](ConfigSYSLOG.md)

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

<a id="protocolSyslogSend"></a>
# **protocolSyslogSend**
> String protocolSyslogSend(agentNum, pri, syslogMsg)

Set the agent&#39;s SYSLOG traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SYSLOG tracing
    Integer pri = 56; // Integer | Message Priority
    SyslogMsg syslogMsg = new SyslogMsg(); // SyslogMsg | 
    try {
      String result = apiInstance.protocolSyslogSend(agentNum, pri, syslogMsg);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogSend");
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
| **agentNum** | **Integer**| Agent to set the SYSLOG tracing | |
| **pri** | **Integer**| Message Priority | |
| **syslogMsg** | [**SyslogMsg**](SyslogMsg.md)|  | |

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

<a id="protocolSyslogSetAttr"></a>
# **protocolSyslogSetAttr**
> String protocolSyslogSetAttr(agentNum, attr, value)

Set the outgoing message&#39;s attributes

Attribute can be server , sequence , separator , hostname , timestamp

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SYSLOG tracing
    String attr = "attr_example"; // String | Attribute
    String value = "value_example"; // String | 
    try {
      String result = apiInstance.protocolSyslogSetAttr(agentNum, attr, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogSetAttr");
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
| **agentNum** | **Integer**| Agent to set the SYSLOG tracing | |
| **attr** | **String**| Attribute | |
| **value** | **String**|  | |

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

<a id="protocolSyslogSetConfig"></a>
# **protocolSyslogSetConfig**
> String protocolSyslogSetConfig(agentNum, argument, value)

Set the agent&#39;s SYSLOG configuration

Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SYSLOG configuration
    String argument = "argument_example"; // String | Parameter to set the SYSLOG configuration
    String value = "value_example"; // String | Value to set the SYSLOG configuration
    try {
      String result = apiInstance.protocolSyslogSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogSetConfig");
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
| **agentNum** | **Integer**| Agent to set the SYSLOG configuration | |
| **argument** | **String**| Parameter to set the SYSLOG configuration | |
| **value** | **String**| Value to set the SYSLOG configuration | |

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

<a id="protocolSyslogSetTrace"></a>
# **protocolSyslogSetTrace**
> String protocolSyslogSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SYSLOG traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SyslogApi apiInstance = new SyslogApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SYSLOG tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the SYSLOG tracing
    try {
      String result = apiInstance.protocolSyslogSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogApi#protocolSyslogSetTrace");
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
| **agentNum** | **Integer**| Agent to set the SYSLOG tracing | |
| **enableOrNot** | **String**| Value to set the SYSLOG tracing | |

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


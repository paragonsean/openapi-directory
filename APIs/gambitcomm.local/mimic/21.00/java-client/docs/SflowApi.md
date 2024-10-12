# SflowApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolSflowGetArgs**](SflowApi.md#protocolSflowGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/args | Show the agent&#39;s SFLOW argument structure |
| [**protocolSflowGetConfig**](SflowApi.md#protocolSflowGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/config | Show the agent&#39;s SFLOW configuration |
| [**protocolSflowGetStatistics**](SflowApi.md#protocolSflowGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/statistics | Show the agent&#39;s SFLOW statistics |
| [**protocolSflowGetStatsHdr**](SflowApi.md#protocolSflowGetStatsHdr) | **GET** /mimic/protocol/msg/sflow/get/stats_hdr | Show the SFLOW statistics headers |
| [**protocolSflowGetTrace**](SflowApi.md#protocolSflowGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/sflow/get/trace | Show the agent&#39;s SFLOW traffic tracing |
| [**protocolSflowHalt**](SflowApi.md#protocolSflowHalt) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/halt | Halt SFLOW traffic |
| [**protocolSflowReload**](SflowApi.md#protocolSflowReload) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/reload | Reload SFLOW configuration before resuming traffic |
| [**protocolSflowResume**](SflowApi.md#protocolSflowResume) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/resume | Resuming traffic |
| [**protocolSflowSetConfig**](SflowApi.md#protocolSflowSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/set/config/{argument}/{value} | Set the agent&#39;s SFLOW configuration |
| [**protocolSflowSetTrace**](SflowApi.md#protocolSflowSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/sflow/set/trace/{enableOrNot} | Set the agent&#39;s SFLOW traffic tracing |


<a id="protocolSflowGetArgs"></a>
# **protocolSflowGetArgs**
> Object protocolSflowGetArgs(agentNum)

Show the agent&#39;s SFLOW argument structure

Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SFLOW argument structure
    try {
      Object result = apiInstance.protocolSflowGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowGetArgs");
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
| **agentNum** | **Integer**| Agent to show the SFLOW argument structure | |

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

<a id="protocolSflowGetConfig"></a>
# **protocolSflowGetConfig**
> ConfigSFLOW protocolSflowGetConfig(agentNum)

Show the agent&#39;s SFLOW configuration

Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the SFLOW configuration
    try {
      ConfigSFLOW result = apiInstance.protocolSflowGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowGetConfig");
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
| **agentNum** | **Integer**| Agent to show the SFLOW configuration | |

### Return type

[**ConfigSFLOW**](ConfigSFLOW.md)

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

<a id="protocolSflowGetStatistics"></a>
# **protocolSflowGetStatistics**
> List&lt;Integer&gt; protocolSflowGetStatistics(agentNum)

Show the agent&#39;s SFLOW statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show SFLOW statistics
    try {
      List<Integer> result = apiInstance.protocolSflowGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowGetStatistics");
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
| **agentNum** | **Integer**| Agent to show SFLOW statistics | |

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

<a id="protocolSflowGetStatsHdr"></a>
# **protocolSflowGetStatsHdr**
> List&lt;String&gt; protocolSflowGetStatsHdr()

Show the SFLOW statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolSflowGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowGetStatsHdr");
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

<a id="protocolSflowGetTrace"></a>
# **protocolSflowGetTrace**
> ConfigSFLOW protocolSflowGetTrace(agentNum)

Show the agent&#39;s SFLOW traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether SFLOW tracing is enabled
    try {
      ConfigSFLOW result = apiInstance.protocolSflowGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether SFLOW tracing is enabled | |

### Return type

[**ConfigSFLOW**](ConfigSFLOW.md)

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

<a id="protocolSflowHalt"></a>
# **protocolSflowHalt**
> String protocolSflowHalt(agentNum)

Halt SFLOW traffic

Halt SFLOW traffic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SFLOW
    try {
      String result = apiInstance.protocolSflowHalt(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowHalt");
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
| **agentNum** | **Integer**| Agent to set the SFLOW | |

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

<a id="protocolSflowReload"></a>
# **protocolSflowReload**
> String protocolSflowReload(agentNum)

Reload SFLOW configuration before resuming traffic

Reload SFLOW configuration before resuming traffic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SFLOW
    try {
      String result = apiInstance.protocolSflowReload(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowReload");
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
| **agentNum** | **Integer**| Agent to set the SFLOW | |

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

<a id="protocolSflowResume"></a>
# **protocolSflowResume**
> String protocolSflowResume(agentNum)

Resuming traffic

Resuming traffic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SFLOW
    try {
      String result = apiInstance.protocolSflowResume(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowResume");
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
| **agentNum** | **Integer**| Agent to set the SFLOW | |

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

<a id="protocolSflowSetConfig"></a>
# **protocolSflowSetConfig**
> String protocolSflowSetConfig(agentNum, argument, value)

Set the agent&#39;s SFLOW configuration

Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SFLOW configuration
    String argument = "argument_example"; // String | Parameter to set the SFLOW configuration
    String value = "value_example"; // String | Value to set the SFLOW configuration
    try {
      String result = apiInstance.protocolSflowSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowSetConfig");
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
| **agentNum** | **Integer**| Agent to set the SFLOW configuration | |
| **argument** | **String**| Parameter to set the SFLOW configuration | |
| **value** | **String**| Value to set the SFLOW configuration | |

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

<a id="protocolSflowSetTrace"></a>
# **protocolSflowSetTrace**
> String protocolSflowSetTrace(agentNum, enableOrNot)

Set the agent&#39;s SFLOW traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SflowApi apiInstance = new SflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the SFLOW tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the SFLOW tracing
    try {
      String result = apiInstance.protocolSflowSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SflowApi#protocolSflowSetTrace");
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
| **agentNum** | **Integer**| Agent to set the SFLOW tracing | |
| **enableOrNot** | **String**| Value to set the SFLOW tracing | |

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


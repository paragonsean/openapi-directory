# TodApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolTodGetArgs**](TodApi.md#protocolTodGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/args | Show the agent&#39;s TOD argument structure |
| [**protocolTodGetConfig**](TodApi.md#protocolTodGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/config | Show the agent&#39;s TOD configuration |
| [**protocolTodGetStatistics**](TodApi.md#protocolTodGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/statistics | Show the agent&#39;s TOD statistics |
| [**protocolTodGetStatsHdr**](TodApi.md#protocolTodGetStatsHdr) | **GET** /mimic/protocol/msg/tod/get/stats_hdr | Show the TOD statistics headers |
| [**protocolTodGetTrace**](TodApi.md#protocolTodGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/get/trace | Show the agent&#39;s TOD traffic tracing |
| [**protocolTodGettime**](TodApi.md#protocolTodGettime) | **GET** /mimic/agent/{agentNum}/protocol/msg/tod/gettime/server/{serverAddr}/port/{portNum}/script/{scriptName}/timeout/{timeSec}/retries/{numRetries} | Retrieve TOD time |
| [**protocolTodSetConfig**](TodApi.md#protocolTodSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tod/set/config/{argument}/{value} | Set the agent&#39;s TOD configuration |
| [**protocolTodSetTrace**](TodApi.md#protocolTodSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tod/set/trace/{enableOrNot} | Set the agent&#39;s TOD traffic tracing |


<a id="protocolTodGetArgs"></a>
# **protocolTodGetArgs**
> Object protocolTodGetArgs(agentNum)

Show the agent&#39;s TOD argument structure

Agent&#39;s TOD configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the TOD argument structure
    try {
      Object result = apiInstance.protocolTodGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodGetArgs");
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
| **agentNum** | **Integer**| Agent to show the TOD argument structure | |

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

<a id="protocolTodGetConfig"></a>
# **protocolTodGetConfig**
> ConfigTOD protocolTodGetConfig(agentNum)

Show the agent&#39;s TOD configuration

Agent&#39;s TOD configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the TOD configuration
    try {
      ConfigTOD result = apiInstance.protocolTodGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodGetConfig");
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
| **agentNum** | **Integer**| Agent to show the TOD configuration | |

### Return type

[**ConfigTOD**](ConfigTOD.md)

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

<a id="protocolTodGetStatistics"></a>
# **protocolTodGetStatistics**
> List&lt;Integer&gt; protocolTodGetStatistics(agentNum)

Show the agent&#39;s TOD statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TOD statistics
    try {
      List<Integer> result = apiInstance.protocolTodGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodGetStatistics");
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
| **agentNum** | **Integer**| Agent to show TOD statistics | |

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

<a id="protocolTodGetStatsHdr"></a>
# **protocolTodGetStatsHdr**
> List&lt;String&gt; protocolTodGetStatsHdr()

Show the TOD statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolTodGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodGetStatsHdr");
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

<a id="protocolTodGetTrace"></a>
# **protocolTodGetTrace**
> ConfigTOD protocolTodGetTrace(agentNum)

Show the agent&#39;s TOD traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether TOD tracing is enabled
    try {
      ConfigTOD result = apiInstance.protocolTodGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether TOD tracing is enabled | |

### Return type

[**ConfigTOD**](ConfigTOD.md)

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

<a id="protocolTodGettime"></a>
# **protocolTodGettime**
> List&lt;String&gt; protocolTodGettime(agentNum, serverAddr, portNum, scriptName, timeSec, numRetries)

Retrieve TOD time

Retrive time from server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TOD return
    String serverAddr = "serverAddr_example"; // String | serverAddr
    Integer portNum = 56; // Integer | portNum
    String scriptName = "scriptName_example"; // String | scriptName
    Integer timeSec = 56; // Integer | timeSec
    Integer numRetries = 56; // Integer | numRetries
    try {
      List<String> result = apiInstance.protocolTodGettime(agentNum, serverAddr, portNum, scriptName, timeSec, numRetries);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodGettime");
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
| **agentNum** | **Integer**| Agent to show TOD return | |
| **serverAddr** | **String**| serverAddr | |
| **portNum** | **Integer**| portNum | |
| **scriptName** | **String**| scriptName | |
| **timeSec** | **Integer**| timeSec | |
| **numRetries** | **Integer**| numRetries | |

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

<a id="protocolTodSetConfig"></a>
# **protocolTodSetConfig**
> String protocolTodSetConfig(agentNum, argument, value)

Set the agent&#39;s TOD configuration

Agent&#39;s TOD configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the TOD configuration
    String argument = "argument_example"; // String | Parameter to set the TOD configuration
    String value = "value_example"; // String | Value to set the TOD configuration
    try {
      String result = apiInstance.protocolTodSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodSetConfig");
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
| **agentNum** | **Integer**| Agent to set the TOD configuration | |
| **argument** | **String**| Parameter to set the TOD configuration | |
| **value** | **String**| Value to set the TOD configuration | |

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

<a id="protocolTodSetTrace"></a>
# **protocolTodSetTrace**
> String protocolTodSetTrace(agentNum, enableOrNot)

Set the agent&#39;s TOD traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TodApi apiInstance = new TodApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the TOD tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the TOD tracing
    try {
      String result = apiInstance.protocolTodSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodApi#protocolTodSetTrace");
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
| **agentNum** | **Integer**| Agent to set the TOD tracing | |
| **enableOrNot** | **String**| Value to set the TOD tracing | |

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


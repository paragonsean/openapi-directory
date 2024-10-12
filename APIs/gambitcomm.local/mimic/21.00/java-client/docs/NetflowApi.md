# NetflowApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolNetflowChangeAttr**](NetflowApi.md#protocolNetflowChangeAttr) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/change/{flowset-uid}/{field-num}/{attr}/{value} | Change NETFLOW export attributes |
| [**protocolNetflowChangeDfs**](NetflowApi.md#protocolNetflowChangeDfs) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/change/dfs_interval/{interval} | Change NETFLOW data export interval |
| [**protocolNetflowChangeTfs**](NetflowApi.md#protocolNetflowChangeTfs) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/change/tfs_interval/{interval} | Change NETFLOW template export interval |
| [**protocolNetflowGetArgs**](NetflowApi.md#protocolNetflowGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/args | Show the agent&#39;s NETFLOW argument structure |
| [**protocolNetflowGetConfig**](NetflowApi.md#protocolNetflowGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/config | Show the agent&#39;s NETFLOW configuration |
| [**protocolNetflowGetStatistics**](NetflowApi.md#protocolNetflowGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/statistics | Show the agent&#39;s NETFLOW statistics |
| [**protocolNetflowGetStatsHdr**](NetflowApi.md#protocolNetflowGetStatsHdr) | **GET** /mimic/protocol/msg/netflow/get/stats_hdr | Show the NETFLOW statistics headers |
| [**protocolNetflowGetTrace**](NetflowApi.md#protocolNetflowGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/get/trace | Show the agent&#39;s NETFLOW traffic tracing |
| [**protocolNetflowHalt**](NetflowApi.md#protocolNetflowHalt) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/halt | Halt NETFLOW traffic |
| [**protocolNetflowList**](NetflowApi.md#protocolNetflowList) | **GET** /mimic/agent/{agentNum}/protocol/msg/netflow/flow/list | Show list of NETFLOW exports |
| [**protocolNetflowReload**](NetflowApi.md#protocolNetflowReload) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/reload | Reload NETFLOW configuration before resuming traffic |
| [**protocolNetflowResume**](NetflowApi.md#protocolNetflowResume) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/resume | Resuming traffic |
| [**protocolNetflowSetCollector**](NetflowApi.md#protocolNetflowSetCollector) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/collector/{collectorIP} | Swap NETFLOW collector |
| [**protocolNetflowSetConfig**](NetflowApi.md#protocolNetflowSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/config/{argument}/{value} | Set the agent&#39;s NETFLOW configuration |
| [**protocolNetflowSetFileName**](NetflowApi.md#protocolNetflowSetFileName) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/filename/{fileName} | Swap NETFLOW configuration file |
| [**protocolNetflowSetTrace**](NetflowApi.md#protocolNetflowSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/netflow/set/trace/{enableOrNot} | Set the agent&#39;s NETFLOW traffic tracing |


<a id="protocolNetflowChangeAttr"></a>
# **protocolNetflowChangeAttr**
> String protocolNetflowChangeAttr(agentNum, flowsetUid, fieldNum, attr, value)

Change NETFLOW export attributes

Change attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    Integer flowsetUid = 56; // Integer | 
    Integer fieldNum = 56; // Integer | 
    String attr = "attr_example"; // String | 
    String value = "value_example"; // String | 
    try {
      String result = apiInstance.protocolNetflowChangeAttr(agentNum, flowsetUid, fieldNum, attr, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowChangeAttr");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |
| **flowsetUid** | **Integer**|  | |
| **fieldNum** | **Integer**|  | |
| **attr** | **String**|  | |
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

<a id="protocolNetflowChangeDfs"></a>
# **protocolNetflowChangeDfs**
> String protocolNetflowChangeDfs(agentNum, interval)

Change NETFLOW data export interval

Interval in msec .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    Integer interval = 56; // Integer | NETFLOW export interval
    try {
      String result = apiInstance.protocolNetflowChangeDfs(agentNum, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowChangeDfs");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |
| **interval** | **Integer**| NETFLOW export interval | |

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

<a id="protocolNetflowChangeTfs"></a>
# **protocolNetflowChangeTfs**
> String protocolNetflowChangeTfs(agentNum, interval)

Change NETFLOW template export interval

Interval in msec .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    Integer interval = 56; // Integer | NETFLOW export interval
    try {
      String result = apiInstance.protocolNetflowChangeTfs(agentNum, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowChangeTfs");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |
| **interval** | **Integer**| NETFLOW export interval | |

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

<a id="protocolNetflowGetArgs"></a>
# **protocolNetflowGetArgs**
> Object protocolNetflowGetArgs(agentNum)

Show the agent&#39;s NETFLOW argument structure

Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the NETFLOW argument structure
    try {
      Object result = apiInstance.protocolNetflowGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowGetArgs");
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
| **agentNum** | **Integer**| Agent to show the NETFLOW argument structure | |

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

<a id="protocolNetflowGetConfig"></a>
# **protocolNetflowGetConfig**
> ConfigNETFLOW protocolNetflowGetConfig(agentNum)

Show the agent&#39;s NETFLOW configuration

Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the NETFLOW configuration
    try {
      ConfigNETFLOW result = apiInstance.protocolNetflowGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowGetConfig");
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
| **agentNum** | **Integer**| Agent to show the NETFLOW configuration | |

### Return type

[**ConfigNETFLOW**](ConfigNETFLOW.md)

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

<a id="protocolNetflowGetStatistics"></a>
# **protocolNetflowGetStatistics**
> List&lt;Integer&gt; protocolNetflowGetStatistics(agentNum)

Show the agent&#39;s NETFLOW statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show NETFLOW statistics
    try {
      List<Integer> result = apiInstance.protocolNetflowGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowGetStatistics");
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
| **agentNum** | **Integer**| Agent to show NETFLOW statistics | |

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

<a id="protocolNetflowGetStatsHdr"></a>
# **protocolNetflowGetStatsHdr**
> List&lt;String&gt; protocolNetflowGetStatsHdr()

Show the NETFLOW statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolNetflowGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowGetStatsHdr");
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

<a id="protocolNetflowGetTrace"></a>
# **protocolNetflowGetTrace**
> ConfigNETFLOW protocolNetflowGetTrace(agentNum)

Show the agent&#39;s NETFLOW traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether NETFLOW tracing is enabled
    try {
      ConfigNETFLOW result = apiInstance.protocolNetflowGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether NETFLOW tracing is enabled | |

### Return type

[**ConfigNETFLOW**](ConfigNETFLOW.md)

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

<a id="protocolNetflowHalt"></a>
# **protocolNetflowHalt**
> String protocolNetflowHalt(agentNum)

Halt NETFLOW traffic

Halt NETFLOW traffic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    try {
      String result = apiInstance.protocolNetflowHalt(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowHalt");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |

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

<a id="protocolNetflowList"></a>
# **protocolNetflowList**
> List&lt;Object&gt; protocolNetflowList(agentNum)

Show list of NETFLOW exports

Show list of NETFLOW exports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show NETFLOW statistics
    try {
      List<Object> result = apiInstance.protocolNetflowList(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowList");
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
| **agentNum** | **Integer**| Agent to show NETFLOW statistics | |

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
| **400** | Invalid agent number value |  -  |

<a id="protocolNetflowReload"></a>
# **protocolNetflowReload**
> String protocolNetflowReload(agentNum)

Reload NETFLOW configuration before resuming traffic

Reload NETFLOW configuration before resuming traffic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    try {
      String result = apiInstance.protocolNetflowReload(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowReload");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |

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

<a id="protocolNetflowResume"></a>
# **protocolNetflowResume**
> String protocolNetflowResume(agentNum)

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
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    try {
      String result = apiInstance.protocolNetflowResume(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowResume");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |

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

<a id="protocolNetflowSetCollector"></a>
# **protocolNetflowSetCollector**
> String protocolNetflowSetCollector(agentNum, collectorIP)

Swap NETFLOW collector

Allow changing collector without stopping agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    String collectorIP = "collectorIP_example"; // String | file name to load config
    try {
      String result = apiInstance.protocolNetflowSetCollector(agentNum, collectorIP);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowSetCollector");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |
| **collectorIP** | **String**| file name to load config | |

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

<a id="protocolNetflowSetConfig"></a>
# **protocolNetflowSetConfig**
> String protocolNetflowSetConfig(agentNum, argument, value)

Set the agent&#39;s NETFLOW configuration

Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW configuration
    String argument = "argument_example"; // String | Parameter to set the NETFLOW configuration
    String value = "value_example"; // String | Value to set the NETFLOW configuration
    try {
      String result = apiInstance.protocolNetflowSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowSetConfig");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW configuration | |
| **argument** | **String**| Parameter to set the NETFLOW configuration | |
| **value** | **String**| Value to set the NETFLOW configuration | |

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

<a id="protocolNetflowSetFileName"></a>
# **protocolNetflowSetFileName**
> String protocolNetflowSetFileName(agentNum, fileName)

Swap NETFLOW configuration file

Allow reloading the configuration file for an agent without stopping agent

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW
    String fileName = "fileName_example"; // String | file name to load config
    try {
      String result = apiInstance.protocolNetflowSetFileName(agentNum, fileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowSetFileName");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW | |
| **fileName** | **String**| file name to load config | |

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

<a id="protocolNetflowSetTrace"></a>
# **protocolNetflowSetTrace**
> String protocolNetflowSetTrace(agentNum, enableOrNot)

Set the agent&#39;s NETFLOW traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    NetflowApi apiInstance = new NetflowApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the NETFLOW tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the NETFLOW tracing
    try {
      String result = apiInstance.protocolNetflowSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetflowApi#protocolNetflowSetTrace");
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
| **agentNum** | **Integer**| Agent to set the NETFLOW tracing | |
| **enableOrNot** | **String**| Value to set the NETFLOW tracing | |

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


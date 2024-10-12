# IpmiApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolIpmiGetArgs**](IpmiApi.md#protocolIpmiGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/args | Show the agent&#39;s IPMI argument structure |
| [**protocolIpmiGetAttr**](IpmiApi.md#protocolIpmiGetAttr) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/{attr} | Show the outgoing message&#39;s attributes |
| [**protocolIpmiGetConfig**](IpmiApi.md#protocolIpmiGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/config | Show the agent&#39;s IPMI configuration |
| [**protocolIpmiGetStatistics**](IpmiApi.md#protocolIpmiGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/statistics | Show the agent&#39;s IPMI statistics |
| [**protocolIpmiGetStatsHdr**](IpmiApi.md#protocolIpmiGetStatsHdr) | **GET** /mimic/protocol/msg/ipmi/get/stats_hdr | Show the IPMI statistics headers |
| [**protocolIpmiGetTrace**](IpmiApi.md#protocolIpmiGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/ipmi/get/trace | Show the agent&#39;s IPMI traffic tracing |
| [**protocolIpmiSetAttr**](IpmiApi.md#protocolIpmiSetAttr) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ipmi/set/{attr}/{value} | Set the outgoing message&#39;s attributes |
| [**protocolIpmiSetConfig**](IpmiApi.md#protocolIpmiSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ipmi/set/config/{argument}/{value} | Set the agent&#39;s IPMI configuration |
| [**protocolIpmiSetTrace**](IpmiApi.md#protocolIpmiSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/ipmi/set/trace/{enableOrNot} | Set the agent&#39;s IPMI traffic tracing |


<a id="protocolIpmiGetArgs"></a>
# **protocolIpmiGetArgs**
> Object protocolIpmiGetArgs(agentNum)

Show the agent&#39;s IPMI argument structure

Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the IPMI argument structure
    try {
      Object result = apiInstance.protocolIpmiGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiGetArgs");
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
| **agentNum** | **Integer**| Agent to show the IPMI argument structure | |

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

<a id="protocolIpmiGetAttr"></a>
# **protocolIpmiGetAttr**
> String protocolIpmiGetAttr(agentNum, attr)

Show the outgoing message&#39;s attributes

Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the IPMI tracing
    String attr = "attr_example"; // String | Attribute
    try {
      String result = apiInstance.protocolIpmiGetAttr(agentNum, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiGetAttr");
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
| **agentNum** | **Integer**| Agent to set the IPMI tracing | |
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

<a id="protocolIpmiGetConfig"></a>
# **protocolIpmiGetConfig**
> ConfigIPMI protocolIpmiGetConfig(agentNum)

Show the agent&#39;s IPMI configuration

Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the IPMI configuration
    try {
      ConfigIPMI result = apiInstance.protocolIpmiGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiGetConfig");
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
| **agentNum** | **Integer**| Agent to show the IPMI configuration | |

### Return type

[**ConfigIPMI**](ConfigIPMI.md)

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

<a id="protocolIpmiGetStatistics"></a>
# **protocolIpmiGetStatistics**
> List&lt;Integer&gt; protocolIpmiGetStatistics(agentNum)

Show the agent&#39;s IPMI statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show IPMI statistics
    try {
      List<Integer> result = apiInstance.protocolIpmiGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiGetStatistics");
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
| **agentNum** | **Integer**| Agent to show IPMI statistics | |

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

<a id="protocolIpmiGetStatsHdr"></a>
# **protocolIpmiGetStatsHdr**
> List&lt;String&gt; protocolIpmiGetStatsHdr()

Show the IPMI statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolIpmiGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiGetStatsHdr");
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

<a id="protocolIpmiGetTrace"></a>
# **protocolIpmiGetTrace**
> ConfigIPMI protocolIpmiGetTrace(agentNum)

Show the agent&#39;s IPMI traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether IPMI tracing is enabled
    try {
      ConfigIPMI result = apiInstance.protocolIpmiGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether IPMI tracing is enabled | |

### Return type

[**ConfigIPMI**](ConfigIPMI.md)

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

<a id="protocolIpmiSetAttr"></a>
# **protocolIpmiSetAttr**
> String protocolIpmiSetAttr(agentNum, attr, value)

Set the outgoing message&#39;s attributes

Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the IPMI tracing
    String attr = "attr_example"; // String | Attribute
    String value = "value_example"; // String | 
    try {
      String result = apiInstance.protocolIpmiSetAttr(agentNum, attr, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiSetAttr");
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
| **agentNum** | **Integer**| Agent to set the IPMI tracing | |
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

<a id="protocolIpmiSetConfig"></a>
# **protocolIpmiSetConfig**
> String protocolIpmiSetConfig(agentNum, argument, value)

Set the agent&#39;s IPMI configuration

Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the IPMI configuration
    String argument = "argument_example"; // String | Parameter to set the IPMI configuration
    String value = "value_example"; // String | Value to set the IPMI configuration
    try {
      String result = apiInstance.protocolIpmiSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiSetConfig");
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
| **agentNum** | **Integer**| Agent to set the IPMI configuration | |
| **argument** | **String**| Parameter to set the IPMI configuration | |
| **value** | **String**| Value to set the IPMI configuration | |

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

<a id="protocolIpmiSetTrace"></a>
# **protocolIpmiSetTrace**
> String protocolIpmiSetTrace(agentNum, enableOrNot)

Set the agent&#39;s IPMI traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpmiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IpmiApi apiInstance = new IpmiApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the IPMI tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the IPMI tracing
    try {
      String result = apiInstance.protocolIpmiSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpmiApi#protocolIpmiSetTrace");
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
| **agentNum** | **Integer**| Agent to set the IPMI tracing | |
| **enableOrNot** | **String**| Value to set the IPMI tracing | |

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


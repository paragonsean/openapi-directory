# DhcpApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolDhcpGetArgs**](DhcpApi.md#protocolDhcpGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/args | Show the agent&#39;s DHCP argument structure |
| [**protocolDhcpGetConfig**](DhcpApi.md#protocolDhcpGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/config | Show the agent&#39;s DHCP configuration |
| [**protocolDhcpGetStatistics**](DhcpApi.md#protocolDhcpGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/statistics | Show the agent&#39;s DHCP statistics |
| [**protocolDhcpGetStatsHdr**](DhcpApi.md#protocolDhcpGetStatsHdr) | **GET** /mimic/protocol/msg/dhcp/get/stats_hdr | Show the DHCP statistics headers |
| [**protocolDhcpGetTrace**](DhcpApi.md#protocolDhcpGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/get/trace | Show the agent&#39;s DHCP traffic tracing |
| [**protocolDhcpParams**](DhcpApi.md#protocolDhcpParams) | **GET** /mimic/agent/{agentNum}/protocol/msg/dhcp/params | Show the parameters configured by the server in its DHCP-OFFER message |
| [**protocolDhcpSetConfig**](DhcpApi.md#protocolDhcpSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/dhcp/set/config/{argument}/{value} | Set the agent&#39;s DHCP configuration |
| [**protocolDhcpSetTrace**](DhcpApi.md#protocolDhcpSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/dhcp/set/trace/{enableOrNot} | Set the agent&#39;s DHCP traffic tracing |


<a id="protocolDhcpGetArgs"></a>
# **protocolDhcpGetArgs**
> Object protocolDhcpGetArgs(agentNum)

Show the agent&#39;s DHCP argument structure

Agent&#39;s DHCP configuration particulars

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the DHCP argument structure
    try {
      Object result = apiInstance.protocolDhcpGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpGetArgs");
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
| **agentNum** | **Integer**| Agent to show the DHCP argument structure | |

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

<a id="protocolDhcpGetConfig"></a>
# **protocolDhcpGetConfig**
> ConfigDHCP protocolDhcpGetConfig(agentNum)

Show the agent&#39;s DHCP configuration

Agent&#39;s DHCP configuration hwaddr,classid,add_options,script

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the DHCP configuration
    try {
      ConfigDHCP result = apiInstance.protocolDhcpGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpGetConfig");
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
| **agentNum** | **Integer**| Agent to show the DHCP configuration | |

### Return type

[**ConfigDHCP**](ConfigDHCP.md)

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

<a id="protocolDhcpGetStatistics"></a>
# **protocolDhcpGetStatistics**
> List&lt;Integer&gt; protocolDhcpGetStatistics(agentNum)

Show the agent&#39;s DHCP statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show DHCP statistics
    try {
      List<Integer> result = apiInstance.protocolDhcpGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpGetStatistics");
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
| **agentNum** | **Integer**| Agent to show DHCP statistics | |

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

<a id="protocolDhcpGetStatsHdr"></a>
# **protocolDhcpGetStatsHdr**
> List&lt;String&gt; protocolDhcpGetStatsHdr()

Show the DHCP statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolDhcpGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpGetStatsHdr");
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

<a id="protocolDhcpGetTrace"></a>
# **protocolDhcpGetTrace**
> ConfigDHCP protocolDhcpGetTrace(agentNum)

Show the agent&#39;s DHCP traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether DHCP tracing is enabled
    try {
      ConfigDHCP result = apiInstance.protocolDhcpGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether DHCP tracing is enabled | |

### Return type

[**ConfigDHCP**](ConfigDHCP.md)

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

<a id="protocolDhcpParams"></a>
# **protocolDhcpParams**
> List&lt;Object&gt; protocolDhcpParams(agentNum)

Show the parameters configured by the server in its DHCP-OFFER message

DHCP-OFFER message parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show DHCP DHCP-OFFER message
    try {
      List<Object> result = apiInstance.protocolDhcpParams(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpParams");
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
| **agentNum** | **Integer**| Agent to show DHCP DHCP-OFFER message | |

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

<a id="protocolDhcpSetConfig"></a>
# **protocolDhcpSetConfig**
> String protocolDhcpSetConfig(agentNum, argument, value)

Set the agent&#39;s DHCP configuration

Agent&#39;s DHCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the DHCP configuration
    String argument = "argument_example"; // String | Parameter to set the DHCP configuration
    String value = "value_example"; // String | Value to set the DHCP configuration
    try {
      String result = apiInstance.protocolDhcpSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpSetConfig");
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
| **agentNum** | **Integer**| Agent to set the DHCP configuration | |
| **argument** | **String**| Parameter to set the DHCP configuration | |
| **value** | **String**| Value to set the DHCP configuration | |

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

<a id="protocolDhcpSetTrace"></a>
# **protocolDhcpSetTrace**
> String protocolDhcpSetTrace(agentNum, enableOrNot)

Set the agent&#39;s DHCP traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the DHCP tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the DHCP tracing
    try {
      String result = apiInstance.protocolDhcpSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#protocolDhcpSetTrace");
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
| **agentNum** | **Integer**| Agent to set the DHCP tracing | |
| **enableOrNot** | **String**| Value to set the DHCP tracing | |

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


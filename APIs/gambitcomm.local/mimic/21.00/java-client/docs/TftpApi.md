# TftpApi

All URIs are relative to *http://gambitcomm.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**protocolTftpGetArgs**](TftpApi.md#protocolTftpGetArgs) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/args | Show the agent&#39;s TFTP argument structure |
| [**protocolTftpGetConfig**](TftpApi.md#protocolTftpGetConfig) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/config | Show the agent&#39;s TFTP configuration |
| [**protocolTftpGetStatistics**](TftpApi.md#protocolTftpGetStatistics) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/statistics | Show the agent&#39;s TFTP statistics |
| [**protocolTftpGetStatsHdr**](TftpApi.md#protocolTftpGetStatsHdr) | **GET** /mimic/protocol/msg/tftp/get/stats_hdr | Show the TFTP statistics headers |
| [**protocolTftpGetTrace**](TftpApi.md#protocolTftpGetTrace) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/get/trace | Show the agent&#39;s TFTP traffic tracing |
| [**protocolTftpSessionGetParameter**](TftpApi.md#protocolTftpSessionGetParameter) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/get/{parameter} | Show a parameter of a TFTP sesssion |
| [**protocolTftpSessionRead**](TftpApi.md#protocolTftpSessionRead) | **POST** /mimic/agent/{agentNum}/protocol/msg/tftp/session/read/server/{srcfile} | Create a read session to download srcfile from server |
| [**protocolTftpSessionSetParameter**](TftpApi.md#protocolTftpSessionSetParameter) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/set/{parameter}/{value} | Set a parameter of a TFTP sesssion |
| [**protocolTftpSessionStart**](TftpApi.md#protocolTftpSessionStart) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/start | Start a TFTP sesssion |
| [**protocolTftpSessionStatus**](TftpApi.md#protocolTftpSessionStatus) | **GET** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/status | Check a TFTP sesssion&#39;s status |
| [**protocolTftpSessionStop**](TftpApi.md#protocolTftpSessionStop) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/{sessionID}/stop | Stop a TFTP sesssion |
| [**protocolTftpSessionWrite**](TftpApi.md#protocolTftpSessionWrite) | **POST** /mimic/agent/{agentNum}/protocol/msg/tftp/session/write/server/{srcfile} | Create a read session to upload srcfile to server |
| [**protocolTftpSetConfig**](TftpApi.md#protocolTftpSetConfig) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/set/config/{argument}/{value} | Set the agent&#39;s TFTP configuration |
| [**protocolTftpSetTrace**](TftpApi.md#protocolTftpSetTrace) | **PUT** /mimic/agent/{agentNum}/protocol/msg/tftp/set/trace/{enableOrNot} | Set the agent&#39;s TFTP traffic tracing |


<a id="protocolTftpGetArgs"></a>
# **protocolTftpGetArgs**
> Object protocolTftpGetArgs(agentNum)

Show the agent&#39;s TFTP argument structure

Agent&#39;s TFTP configuration with port,rule,prompt,paging_prompt,userdb,keymap

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the TFTP argument structure
    try {
      Object result = apiInstance.protocolTftpGetArgs(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpGetArgs");
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
| **agentNum** | **Integer**| Agent to show the TFTP argument structure | |

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

<a id="protocolTftpGetConfig"></a>
# **protocolTftpGetConfig**
> ConfigTFTP protocolTftpGetConfig(agentNum)

Show the agent&#39;s TFTP configuration

Agent&#39;s TFTP configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show the TFTP configuration
    try {
      ConfigTFTP result = apiInstance.protocolTftpGetConfig(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpGetConfig");
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
| **agentNum** | **Integer**| Agent to show the TFTP configuration | |

### Return type

[**ConfigTFTP**](ConfigTFTP.md)

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

<a id="protocolTftpGetStatistics"></a>
# **protocolTftpGetStatistics**
> List&lt;Integer&gt; protocolTftpGetStatistics(agentNum)

Show the agent&#39;s TFTP statistics

Statistics of fields indicated in the headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TFTP statistics
    try {
      List<Integer> result = apiInstance.protocolTftpGetStatistics(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpGetStatistics");
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
| **agentNum** | **Integer**| Agent to show TFTP statistics | |

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

<a id="protocolTftpGetStatsHdr"></a>
# **protocolTftpGetStatsHdr**
> List&lt;String&gt; protocolTftpGetStatsHdr()

Show the TFTP statistics headers

The headers of statistics fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    try {
      List<String> result = apiInstance.protocolTftpGetStatsHdr();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpGetStatsHdr");
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

<a id="protocolTftpGetTrace"></a>
# **protocolTftpGetTrace**
> ConfigTFTP protocolTftpGetTrace(agentNum)

Show the agent&#39;s TFTP traffic tracing

Trace 1 means enabled, 0 means not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show whether TFTP tracing is enabled
    try {
      ConfigTFTP result = apiInstance.protocolTftpGetTrace(agentNum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpGetTrace");
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
| **agentNum** | **Integer**| Agent to show whether TFTP tracing is enabled | |

### Return type

[**ConfigTFTP**](ConfigTFTP.md)

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

<a id="protocolTftpSessionGetParameter"></a>
# **protocolTftpSessionGetParameter**
> String protocolTftpSessionGetParameter(agentNum, sessionID, parameter)

Show a parameter of a TFTP sesssion

Parameter is server , port , or dstfile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TFTP parameter
    String sessionID = "sessionID_example"; // String | SessionID
    String parameter = "parameter_example"; // String | Parameter to show
    try {
      String result = apiInstance.protocolTftpSessionGetParameter(agentNum, sessionID, parameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSessionGetParameter");
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
| **agentNum** | **Integer**| Agent to show TFTP parameter | |
| **sessionID** | **String**| SessionID | |
| **parameter** | **String**| Parameter to show | |

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

<a id="protocolTftpSessionRead"></a>
# **protocolTftpSessionRead**
> List&lt;Integer&gt; protocolTftpSessionRead(agentNum, srcfile)

Create a read session to download srcfile from server

Session ID is returned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TFTP statistics
    String srcfile = "srcfile_example"; // String | File name to retrieve from server
    try {
      List<Integer> result = apiInstance.protocolTftpSessionRead(agentNum, srcfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSessionRead");
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
| **agentNum** | **Integer**| Agent to show TFTP statistics | |
| **srcfile** | **String**| File name to retrieve from server | |

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

<a id="protocolTftpSessionSetParameter"></a>
# **protocolTftpSessionSetParameter**
> String protocolTftpSessionSetParameter(agentNum, sessionID, parameter, value)

Set a parameter of a TFTP sesssion

Parameter is server , port , or dstfile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set TFTP parameter
    String sessionID = "sessionID_example"; // String | SessionID
    String parameter = "parameter_example"; // String | Parameter to set
    String value = "value_example"; // String | Value to set
    try {
      String result = apiInstance.protocolTftpSessionSetParameter(agentNum, sessionID, parameter, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSessionSetParameter");
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
| **agentNum** | **Integer**| Agent to set TFTP parameter | |
| **sessionID** | **String**| SessionID | |
| **parameter** | **String**| Parameter to set | |
| **value** | **String**| Value to set | |

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

<a id="protocolTftpSessionStart"></a>
# **protocolTftpSessionStart**
> String protocolTftpSessionStart(agentNum, sessionID)

Start a TFTP sesssion

Start uploading or downloading the file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to start TFTP transaction
    String sessionID = "sessionID_example"; // String | SessionID
    try {
      String result = apiInstance.protocolTftpSessionStart(agentNum, sessionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSessionStart");
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
| **agentNum** | **Integer**| Agent to start TFTP transaction | |
| **sessionID** | **String**| SessionID | |

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

<a id="protocolTftpSessionStatus"></a>
# **protocolTftpSessionStatus**
> String protocolTftpSessionStatus(agentNum, sessionID)

Check a TFTP sesssion&#39;s status

Status includes running state, bytes transfered, and time elapsed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TFTP transaction
    String sessionID = "sessionID_example"; // String | SessionID
    try {
      String result = apiInstance.protocolTftpSessionStatus(agentNum, sessionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSessionStatus");
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
| **agentNum** | **Integer**| Agent to show TFTP transaction | |
| **sessionID** | **String**| SessionID | |

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

<a id="protocolTftpSessionStop"></a>
# **protocolTftpSessionStop**
> String protocolTftpSessionStop(agentNum, sessionID)

Stop a TFTP sesssion

Stop uploading or downloading the file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to stop TFTP transaction
    String sessionID = "sessionID_example"; // String | SessionID
    try {
      String result = apiInstance.protocolTftpSessionStop(agentNum, sessionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSessionStop");
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
| **agentNum** | **Integer**| Agent to stop TFTP transaction | |
| **sessionID** | **String**| SessionID | |

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

<a id="protocolTftpSessionWrite"></a>
# **protocolTftpSessionWrite**
> List&lt;Integer&gt; protocolTftpSessionWrite(agentNum, srcfile)

Create a read session to upload srcfile to server

Session ID is returned

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to show TFTP statistics
    String srcfile = "srcfile_example"; // String | File name to upload to server
    try {
      List<Integer> result = apiInstance.protocolTftpSessionWrite(agentNum, srcfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSessionWrite");
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
| **agentNum** | **Integer**| Agent to show TFTP statistics | |
| **srcfile** | **String**| File name to upload to server | |

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

<a id="protocolTftpSetConfig"></a>
# **protocolTftpSetConfig**
> String protocolTftpSetConfig(agentNum, argument, value)

Set the agent&#39;s TFTP configuration

Agent&#39;s TFTP configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the TFTP configuration
    String argument = "argument_example"; // String | Parameter to set the TFTP configuration
    String value = "value_example"; // String | Value to set the TFTP configuration
    try {
      String result = apiInstance.protocolTftpSetConfig(agentNum, argument, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSetConfig");
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
| **agentNum** | **Integer**| Agent to set the TFTP configuration | |
| **argument** | **String**| Parameter to set the TFTP configuration | |
| **value** | **String**| Value to set the TFTP configuration | |

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

<a id="protocolTftpSetTrace"></a>
# **protocolTftpSetTrace**
> String protocolTftpSetTrace(agentNum, enableOrNot)

Set the agent&#39;s TFTP traffic tracing

1 to enable, 0 to disable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TftpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://gambitcomm.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TftpApi apiInstance = new TftpApi(defaultClient);
    Integer agentNum = 56; // Integer | Agent to set the TFTP tracing
    String enableOrNot = "enableOrNot_example"; // String | Value to set the TFTP tracing
    try {
      String result = apiInstance.protocolTftpSetTrace(agentNum, enableOrNot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TftpApi#protocolTftpSetTrace");
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
| **agentNum** | **Integer**| Agent to set the TFTP tracing | |
| **enableOrNot** | **String**| Value to set the TFTP tracing | |

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


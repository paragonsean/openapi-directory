# LogsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logsAppIdDrainsGet_0**](LogsApi.md#logsAppIdDrainsGet_0) | **GET** /logs/{appId}/drains |  |
| [**logsAppIdDrainsIdOrUrlDelete_0**](LogsApi.md#logsAppIdDrainsIdOrUrlDelete_0) | **DELETE** /logs/{appId}/drains/:idOrUrl |  |
| [**logsAppIdDrainsIdOrUrlGet_0**](LogsApi.md#logsAppIdDrainsIdOrUrlGet_0) | **GET** /logs/{appId}/drains/:idOrUrl |  |
| [**logsAppIdDrainsPost_0**](LogsApi.md#logsAppIdDrainsPost_0) | **POST** /logs/{appId}/drains |  |
| [**logsAppIdGet_0**](LogsApi.md#logsAppIdGet_0) | **GET** /logs/{appId} |  |
| [**logsAppIdSseGet_0**](LogsApi.md#logsAppIdSseGet_0) | **GET** /logs/{appId}/sse |  |
| [**logsDrainsDrainIdPut_0**](LogsApi.md#logsDrainsDrainIdPut_0) | **PUT** /logs/drains/{drainId} |  |
| [**logsDrainsGet_0**](LogsApi.md#logsDrainsGet_0) | **GET** /logs/drains |  |
| [**logsLogsChunkedAppIdGet_0**](LogsApi.md#logsLogsChunkedAppIdGet_0) | **GET** /logs/logs-chunked/{appId} |  |
| [**logsLogsSocketAppIdGet_0**](LogsApi.md#logsLogsSocketAppIdGet_0) | **GET** /logs/logs-socket/{appId} |  |
| [**v3LogsAppIdDrainsGet_0**](LogsApi.md#v3LogsAppIdDrainsGet_0) | **GET** /v3/logs/{appId}/drains |  |
| [**v3LogsAppIdDrainsIdOrUrlDelete_0**](LogsApi.md#v3LogsAppIdDrainsIdOrUrlDelete_0) | **DELETE** /v3/logs/{appId}/drains/:idOrUrl |  |
| [**v3LogsAppIdDrainsIdOrUrlGet_0**](LogsApi.md#v3LogsAppIdDrainsIdOrUrlGet_0) | **GET** /v3/logs/{appId}/drains/:idOrUrl |  |
| [**v3LogsAppIdDrainsPost_0**](LogsApi.md#v3LogsAppIdDrainsPost_0) | **POST** /v3/logs/{appId}/drains |  |
| [**v3LogsAppIdGet_0**](LogsApi.md#v3LogsAppIdGet_0) | **GET** /v3/logs/{appId} |  |
| [**v3LogsAppIdLogsChunkedGet_0**](LogsApi.md#v3LogsAppIdLogsChunkedGet_0) | **GET** /v3/logs/{appId}/logs-chunked |  |
| [**v3LogsAppIdLogsSocketGet_0**](LogsApi.md#v3LogsAppIdLogsSocketGet_0) | **GET** /v3/logs/{appId}/logs-socket |  |


<a id="logsAppIdDrainsGet_0"></a>
# **logsAppIdDrainsGet_0**
> logsAppIdDrainsGet_0(appId)



Fetch the logs drains for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsAppIdDrainsGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdDrainsIdOrUrlDelete_0"></a>
# **logsAppIdDrainsIdOrUrlDelete_0**
> logsAppIdDrainsIdOrUrlDelete_0(appId)



Delete the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsIdOrUrlDelete_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsAppIdDrainsIdOrUrlDelete_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdDrainsIdOrUrlGet_0"></a>
# **logsAppIdDrainsIdOrUrlGet_0**
> logsAppIdDrainsIdOrUrlGet_0(appId)



Fetch the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsIdOrUrlGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsAppIdDrainsIdOrUrlGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdDrainsPost_0"></a>
# **logsAppIdDrainsPost_0**
> logsAppIdDrainsPost_0(appId)



Add a log drain for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdDrainsPost_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsAppIdDrainsPost_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdGet_0"></a>
# **logsAppIdGet_0**
> logsAppIdGet_0(appId, limit, order, after, before, filter, deploymentId)



Fetch the logs for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Application Id
    Integer limit = 56; // Integer | Number of lines to return
    String order = "asc"; // String | Logs order
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | Lowest bound for logs date, ISO 8601
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Highest bounds for logs date, ISO 8601
    String filter = "filter_example"; // String | A pattern to filter with
    String deploymentId = "deploymentId_example"; // String | Only fetch logs emitted by this deployment
    try {
      apiInstance.logsAppIdGet_0(appId, limit, order, after, before, filter, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsAppIdGet_0");
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
| **appId** | **String**| Application Id | |
| **limit** | **Integer**| Number of lines to return | [optional] |
| **order** | **String**| Logs order | [optional] [default to desc] [enum: asc, desc] |
| **after** | **OffsetDateTime**| Lowest bound for logs date, ISO 8601 | [optional] |
| **before** | **OffsetDateTime**| Highest bounds for logs date, ISO 8601 | [optional] |
| **filter** | **String**| A pattern to filter with | [optional] |
| **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsAppIdSseGet_0"></a>
# **logsAppIdSseGet_0**
> logsAppIdSseGet_0(appId)



Retrieve logs as they come through a sse connection. To have authorization, you have to add &#x60;authorization&#x3D;oAuthAuthorizationString&#x60; as query param.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.logsAppIdSseGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsAppIdSseGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsDrainsDrainIdPut_0"></a>
# **logsDrainsDrainIdPut_0**
> logsDrainsDrainIdPut_0(drainId)



Fetch all the logs drains (ccadmin dedicated route)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String drainId = "drainId_example"; // String | Automatically added
    try {
      apiInstance.logsDrainsDrainIdPut_0(drainId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsDrainsDrainIdPut_0");
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
| **drainId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsDrainsGet_0"></a>
# **logsDrainsGet_0**
> logsDrainsGet_0()



Fetch all the logs drains (ccadmin dedicated route)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    try {
      apiInstance.logsDrainsGet_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsDrainsGet_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsLogsChunkedAppIdGet_0"></a>
# **logsLogsChunkedAppIdGet_0**
> logsLogsChunkedAppIdGet_0(appId, download)



Retrieve logs as they come through a chunked, never-ending response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Application Id
    Boolean download = true; // Boolean | Tell the user-agent to download the body as a file
    try {
      apiInstance.logsLogsChunkedAppIdGet_0(appId, download);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsLogsChunkedAppIdGet_0");
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
| **appId** | **String**| Application Id | |
| **download** | **Boolean**| Tell the user-agent to download the body as a file | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="logsLogsSocketAppIdGet_0"></a>
# **logsLogsSocketAppIdGet_0**
> logsLogsSocketAppIdGet_0(appId, since, filter, deploymentId)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Application Id
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only fetch logs newer than this (ISO-8601 formatted) date
    String filter = "filter_example"; // String | A pattern to filter with
    String deploymentId = "deploymentId_example"; // String | Only fetch logs emitted by this deployment
    try {
      apiInstance.logsLogsSocketAppIdGet_0(appId, since, filter, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsLogsSocketAppIdGet_0");
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
| **appId** | **String**| Application Id | |
| **since** | **OffsetDateTime**| Only fetch logs newer than this (ISO-8601 formatted) date | [optional] |
| **filter** | **String**| A pattern to filter with | [optional] |
| **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdDrainsGet_0"></a>
# **v3LogsAppIdDrainsGet_0**
> v3LogsAppIdDrainsGet_0(appId)



Fetch the logs drains for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#v3LogsAppIdDrainsGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdDrainsIdOrUrlDelete_0"></a>
# **v3LogsAppIdDrainsIdOrUrlDelete_0**
> v3LogsAppIdDrainsIdOrUrlDelete_0(appId)



Delete the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsIdOrUrlDelete_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#v3LogsAppIdDrainsIdOrUrlDelete_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdDrainsIdOrUrlGet_0"></a>
# **v3LogsAppIdDrainsIdOrUrlGet_0**
> v3LogsAppIdDrainsIdOrUrlGet_0(appId)



Fetch the logs drain by id or url for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsIdOrUrlGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#v3LogsAppIdDrainsIdOrUrlGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdDrainsPost_0"></a>
# **v3LogsAppIdDrainsPost_0**
> v3LogsAppIdDrainsPost_0(appId)



Add a log drain for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdDrainsPost_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#v3LogsAppIdDrainsPost_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdGet_0"></a>
# **v3LogsAppIdGet_0**
> v3LogsAppIdGet_0(appId)



Fetch the logs for a given application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#v3LogsAppIdGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdLogsChunkedGet_0"></a>
# **v3LogsAppIdLogsChunkedGet_0**
> v3LogsAppIdLogsChunkedGet_0(appId)



Retrieve logs as they come through a chunked, never-ending response

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdLogsChunkedGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#v3LogsAppIdLogsChunkedGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |

<a id="v3LogsAppIdLogsSocketGet_0"></a>
# **v3LogsAppIdLogsSocketGet_0**
> v3LogsAppIdLogsSocketGet_0(appId)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String appId = "appId_example"; // String | Automatically added
    try {
      apiInstance.v3LogsAppIdLogsSocketGet_0(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#v3LogsAppIdLogsSocketGet_0");
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
| **appId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | &lt;No description&gt; |  -  |


# UtilitiesApi

All URIs are relative to *https://firefox.settings.services.mozilla.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contribute**](UtilitiesApi.md#contribute) | **GET** /contribute.json |  |
| [**getOpenapiSpec**](UtilitiesApi.md#getOpenapiSpec) | **GET** /__api__ |  |
| [**heartbeat**](UtilitiesApi.md#heartbeat) | **GET** /__heartbeat__ |  |
| [**lbheartbeat**](UtilitiesApi.md#lbheartbeat) | **GET** /__lbheartbeat__ |  |
| [**serverInfo**](UtilitiesApi.md#serverInfo) | **GET** / |  |
| [**version**](UtilitiesApi.md#version) | **GET** /__version__ |  |


<a id="contribute"></a>
# **contribute**
> Map&lt;String, Object&gt; contribute()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.contribute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#contribute");
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

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return open source contributing information. |  -  |

<a id="getOpenapiSpec"></a>
# **getOpenapiSpec**
> Map&lt;String, Object&gt; getOpenapiSpec()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.getOpenapiSpec();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#getOpenapiSpec");
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

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return an OpenAPI description of the running instance. |  -  |

<a id="heartbeat"></a>
# **heartbeat**
> Map&lt;String, Object&gt; heartbeat()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.heartbeat();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#heartbeat");
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

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server is working properly. |  -  |
| **503** | One or more subsystems failing. |  -  |

<a id="lbheartbeat"></a>
# **lbheartbeat**
> Object lbheartbeat()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    try {
      Object result = apiInstance.lbheartbeat();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#lbheartbeat");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if server is reachable. |  -  |

<a id="serverInfo"></a>
# **serverInfo**
> Map&lt;String, Object&gt; serverInfo()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.serverInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#serverInfo");
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

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return information about the running Instance. |  -  |

<a id="version"></a>
# **version**
> Map&lt;String, Object&gt; version()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://firefox.settings.services.mozilla.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    try {
      Map<String, Object> result = apiInstance.version();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#version");
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

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the running Instance version information. |  -  |


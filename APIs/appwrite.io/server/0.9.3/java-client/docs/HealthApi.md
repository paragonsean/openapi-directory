# HealthApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthGet**](HealthApi.md#healthGet) | **GET** /health | Get HTTP |
| [**healthGetAntiVirus**](HealthApi.md#healthGetAntiVirus) | **GET** /health/anti-virus | Get Anti virus |
| [**healthGetCache**](HealthApi.md#healthGetCache) | **GET** /health/cache | Get Cache |
| [**healthGetDB**](HealthApi.md#healthGetDB) | **GET** /health/db | Get DB |
| [**healthGetQueueCertificates**](HealthApi.md#healthGetQueueCertificates) | **GET** /health/queue/certificates | Get Certificate Queue |
| [**healthGetQueueFunctions**](HealthApi.md#healthGetQueueFunctions) | **GET** /health/queue/functions | Get Functions Queue |
| [**healthGetQueueLogs**](HealthApi.md#healthGetQueueLogs) | **GET** /health/queue/logs | Get Logs Queue |
| [**healthGetQueueTasks**](HealthApi.md#healthGetQueueTasks) | **GET** /health/queue/tasks | Get Tasks Queue |
| [**healthGetQueueUsage**](HealthApi.md#healthGetQueueUsage) | **GET** /health/queue/usage | Get Usage Queue |
| [**healthGetQueueWebhooks**](HealthApi.md#healthGetQueueWebhooks) | **GET** /health/queue/webhooks | Get Webhooks Queue |
| [**healthGetStorageLocal**](HealthApi.md#healthGetStorageLocal) | **GET** /health/storage/local | Get Local Storage |
| [**healthGetTime**](HealthApi.md#healthGetTime) | **GET** /health/time | Get Time |


<a id="healthGet"></a>
# **healthGet**
> healthGet()

Get HTTP

Check the Appwrite HTTP server is up and responsive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGet");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetAntiVirus"></a>
# **healthGetAntiVirus**
> healthGetAntiVirus()

Get Anti virus

Check the Appwrite Anti Virus server is up and connection is successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetAntiVirus();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetAntiVirus");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetCache"></a>
# **healthGetCache**
> healthGetCache()

Get Cache

Check the Appwrite in-memory cache server is up and connection is successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetCache();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetCache");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetDB"></a>
# **healthGetDB**
> healthGetDB()

Get DB

Check the Appwrite database server is up and connection is successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetDB();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetDB");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetQueueCertificates"></a>
# **healthGetQueueCertificates**
> healthGetQueueCertificates()

Get Certificate Queue

Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetQueueCertificates();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetQueueCertificates");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetQueueFunctions"></a>
# **healthGetQueueFunctions**
> healthGetQueueFunctions()

Get Functions Queue



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetQueueFunctions();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetQueueFunctions");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetQueueLogs"></a>
# **healthGetQueueLogs**
> healthGetQueueLogs()

Get Logs Queue

Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetQueueLogs();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetQueueLogs");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetQueueTasks"></a>
# **healthGetQueueTasks**
> healthGetQueueTasks()

Get Tasks Queue

Get the number of tasks that are waiting to be processed in the Appwrite internal queue server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetQueueTasks();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetQueueTasks");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetQueueUsage"></a>
# **healthGetQueueUsage**
> healthGetQueueUsage()

Get Usage Queue

Get the number of usage stats that are waiting to be processed in the Appwrite internal queue server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetQueueUsage();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetQueueUsage");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetQueueWebhooks"></a>
# **healthGetQueueWebhooks**
> healthGetQueueWebhooks()

Get Webhooks Queue

Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetQueueWebhooks();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetQueueWebhooks");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetStorageLocal"></a>
# **healthGetStorageLocal**
> healthGetStorageLocal()

Get Local Storage

Check the Appwrite local storage device is up and connection is successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetStorageLocal();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetStorageLocal");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |

<a id="healthGetTime"></a>
# **healthGetTime**
> healthGetTime()

Get Time

Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.healthGetTime();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#healthGetTime");
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | File |  -  |


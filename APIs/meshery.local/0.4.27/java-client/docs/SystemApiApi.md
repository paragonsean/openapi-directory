# SystemApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeleteAdapterConfig**](SystemApiApi.md#idDeleteAdapterConfig) | **DELETE** /api/system/adapter/manage | Handle DELETE requests to delete adapter config |
| [**idDeleteK8SConfig**](SystemApiApi.md#idDeleteK8SConfig) | **DELETE** /api/system/kubernetes | Handle DELETE request for Kubernetes Config |
| [**idGetKubernetesPing**](SystemApiApi.md#idGetKubernetesPing) | **GET** /api/system/kubernetes/ping | Handle GET request for Kubernetes ping |
| [**idGetSystemAdapters**](SystemApiApi.md#idGetSystemAdapters) | **GET** /api/system/adapters | Handle GET request for adapters |
| [**idGetSystemVersion**](SystemApiApi.md#idGetSystemVersion) | **GET** /api/system/version | Handle GET request for system/server version |
| [**idMeshSyncGrafana**](SystemApiApi.md#idMeshSyncGrafana) | **GET** /api/system/meshsync/grafana | Handle GET request for mesh-sync grafana |
| [**idMeshSyncPrometheus**](SystemApiApi.md#idMeshSyncPrometheus) | **GET** /api/system/meshsync/prometheus | Handle GET request for fetching prometheus |
| [**idPostAdapterConfig**](SystemApiApi.md#idPostAdapterConfig) | **POST** /api/system/adapter/manage | Handle POST requests to persist adapter config |
| [**idPostAdapterOperation**](SystemApiApi.md#idPostAdapterOperation) | **POST** /api/system/adapter/operation | Handle POST requests for Adapter Operations |
| [**idPostK8SConfig**](SystemApiApi.md#idPostK8SConfig) | **POST** /api/system/kubernetes | Handle POST request for Kubernetes Config |
| [**idPostK8SContexts**](SystemApiApi.md#idPostK8SContexts) | **POST** /api/system/kubernetes/contexts | Handle POST requests for Kubernetes Context list |
| [**idSystemSync**](SystemApiApi.md#idSystemSync) | **GET** /api/system/sync | Handle GET request for config sync |


<a id="idDeleteAdapterConfig"></a>
# **idDeleteAdapterConfig**
> idDeleteAdapterConfig(adapter)

Handle DELETE requests to delete adapter config

Used to delete adapter configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    String adapter = "adapter_example"; // String | 
    try {
      apiInstance.idDeleteAdapterConfig(adapter);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idDeleteAdapterConfig");
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
| **adapter** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idDeleteK8SConfig"></a>
# **idDeleteK8SConfig**
> idDeleteK8SConfig()

Handle DELETE request for Kubernetes Config

Used to delete kubernetes config to System

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      apiInstance.idDeleteK8SConfig();
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idDeleteK8SConfig");
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

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGetKubernetesPing"></a>
# **idGetKubernetesPing**
> idGetKubernetesPing()

Handle GET request for Kubernetes ping

Fetches server version to simulate ping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      apiInstance.idGetKubernetesPing();
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idGetKubernetesPing");
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

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGetSystemAdapters"></a>
# **idGetSystemAdapters**
> List&lt;Adapter&gt; idGetSystemAdapters(adapter)

Handle GET request for adapters

Fetches and returns all the adapters and ping adapters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    String adapter = "adapter_example"; // String | 
    try {
      List<Adapter> result = apiInstance.idGetSystemAdapters(adapter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idGetSystemAdapters");
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
| **adapter** | **String**|  | [optional] |

### Return type

[**List&lt;Adapter&gt;**](Adapter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return all the adapters |  -  |

<a id="idGetSystemVersion"></a>
# **idGetSystemVersion**
> Version idGetSystemVersion()

Handle GET request for system/server version

Returns the running Meshery version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      Version result = apiInstance.idGetSystemVersion();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idGetSystemVersion");
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

[**Version**](Version.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns Meshery version |  -  |

<a id="idMeshSyncGrafana"></a>
# **idMeshSyncGrafana**
> Map&lt;String, List&lt;Service&gt;&gt; idMeshSyncGrafana()

Handle GET request for mesh-sync grafana

Fetches Prometheus and Grafana

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      Map<String, List<Service>> result = apiInstance.idMeshSyncGrafana();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idMeshSyncGrafana");
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

[**Map&lt;String, List&lt;Service&gt;&gt;**](List.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a map for v1 services |  -  |

<a id="idMeshSyncPrometheus"></a>
# **idMeshSyncPrometheus**
> Map&lt;String, List&lt;Service&gt;&gt; idMeshSyncPrometheus()

Handle GET request for fetching prometheus

Fetches Prometheus

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      Map<String, List<Service>> result = apiInstance.idMeshSyncPrometheus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idMeshSyncPrometheus");
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

[**Map&lt;String, List&lt;Service&gt;&gt;**](List.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a map for v1 services |  -  |

<a id="idPostAdapterConfig"></a>
# **idPostAdapterConfig**
> List&lt;Adapter&gt; idPostAdapterConfig(body)

Handle POST requests to persist adapter config

Used to persist adapter config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    String body = "body_example"; // String | 
    try {
      List<Adapter> result = apiInstance.idPostAdapterConfig(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idPostAdapterConfig");
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
| **body** | **String**|  | [optional] |

### Return type

[**List&lt;Adapter&gt;**](Adapter.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all the meshery adapters |  -  |

<a id="idPostAdapterOperation"></a>
# **idPostAdapterOperation**
> idPostAdapterOperation(adapter, query, customBody, namespace, deleteOp)

Handle POST requests for Adapter Operations

Used to send operations to the adapters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    String adapter = "adapter_example"; // String | 
    String query = "query_example"; // String | 
    String customBody = "customBody_example"; // String | 
    String namespace = "namespace_example"; // String | 
    String deleteOp = "deleteOp_example"; // String | 
    try {
      apiInstance.idPostAdapterOperation(adapter, query, customBody, namespace, deleteOp);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idPostAdapterOperation");
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
| **adapter** | **String**|  | [optional] |
| **query** | **String**|  | [optional] |
| **customBody** | **String**|  | [optional] |
| **namespace** | **String**|  | [optional] |
| **deleteOp** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idPostK8SConfig"></a>
# **idPostK8SConfig**
> K8SConfig idPostK8SConfig()

Handle POST request for Kubernetes Config

Used to add kubernetes config to System

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      K8SConfig result = apiInstance.idPostK8SConfig();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idPostK8SConfig");
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

[**K8SConfig**](K8SConfig.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns saved kubernetes config |  -  |

<a id="idPostK8SContexts"></a>
# **idPostK8SContexts**
> List&lt;K8SContext&gt; idPostK8SContexts()

Handle POST requests for Kubernetes Context list

Returns the context list for a given k8s config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      List<K8SContext> result = apiInstance.idPostK8SContexts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idPostK8SContexts");
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

[**List&lt;K8SContext&gt;**](K8SContext.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns kubernetes context list |  -  |

<a id="idSystemSync"></a>
# **idSystemSync**
> Preference idSystemSync()

Handle GET request for config sync

Used to send session data to the UI for initial sync

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    SystemApiApi apiInstance = new SystemApiApi(defaultClient);
    try {
      Preference result = apiInstance.idSystemSync();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApiApi#idSystemSync");
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

[**Preference**](Preference.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns User Load Test Preferencee |  -  |


# GrafanaApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeleteGrafanaConfig**](GrafanaApiApi.md#idDeleteGrafanaConfig) | **DELETE** /api/telemetry/metrics/grafana/config | Handle DELETE request for Grafana configuration |
| [**idGetGrafana**](GrafanaApiApi.md#idGetGrafana) | **GET** /api/telemetry/metrics/grafana/scan | Handle GET request for Grafana |
| [**idGetGrafanaBoards**](GrafanaApiApi.md#idGetGrafanaBoards) | **GET** /api/telemetry/metrics/grafana/boards | Handle GET request for Grafana boards |
| [**idGetGrafanaConfig**](GrafanaApiApi.md#idGetGrafanaConfig) | **GET** /api/telemetry/metrics/grafana/config | Handle GET request for Grafana configuration |
| [**idGetGrafanaPing**](GrafanaApiApi.md#idGetGrafanaPing) | **GET** /api/telemetry/metrics/grafana/ping | Handle GET request for Grafana ping |
| [**idGetGrafanaQuery**](GrafanaApiApi.md#idGetGrafanaQuery) | **GET** /api/telemetry/metrics/grafana/query | Handle GET request for Grafana queries |
| [**idPostGrafanaBoards**](GrafanaApiApi.md#idPostGrafanaBoards) | **POST** /api/telemetry/metrics/grafana/boards | Handle POST request for Grafana boards |
| [**idPostGrafanaConfig**](GrafanaApiApi.md#idPostGrafanaConfig) | **POST** /api/telemetry/metrics/grafana/config | Handle POST request for Grafana configuration |


<a id="idDeleteGrafanaConfig"></a>
# **idDeleteGrafanaConfig**
> idDeleteGrafanaConfig()

Handle DELETE request for Grafana configuration

Used for Delete Grafana configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    try {
      apiInstance.idDeleteGrafanaConfig();
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idDeleteGrafanaConfig");
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

<a id="idGetGrafana"></a>
# **idGetGrafana**
> Map&lt;String, List&lt;Service&gt;&gt; idGetGrafana()

Handle GET request for Grafana

Fetches and returns Grafana

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    try {
      Map<String, List<Service>> result = apiInstance.idGetGrafana();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idGetGrafana");
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

<a id="idGetGrafanaBoards"></a>
# **idGetGrafanaBoards**
> List&lt;GrafanaBoard&gt; idGetGrafanaBoards(dashboardSearch)

Handle GET request for Grafana boards

Used for fetching Grafana boards and panels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    String dashboardSearch = "dashboardSearch_example"; // String | 
    try {
      List<GrafanaBoard> result = apiInstance.idGetGrafanaBoards(dashboardSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idGetGrafanaBoards");
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
| **dashboardSearch** | **String**|  | [optional] |

### Return type

[**List&lt;GrafanaBoard&gt;**](GrafanaBoard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns Grafana boards and panels |  -  |

<a id="idGetGrafanaConfig"></a>
# **idGetGrafanaConfig**
> Grafana idGetGrafanaConfig()

Handle GET request for Grafana configuration

Used for fetching Grafana configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    try {
      Grafana result = apiInstance.idGetGrafanaConfig();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idGetGrafanaConfig");
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

[**Grafana**](Grafana.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns Grafana configs |  -  |

<a id="idGetGrafanaPing"></a>
# **idGetGrafanaPing**
> idGetGrafanaPing()

Handle GET request for Grafana ping

Used to initiate a Grafana ping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    try {
      apiInstance.idGetGrafanaPing();
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idGetGrafanaPing");
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

<a id="idGetGrafanaQuery"></a>
# **idGetGrafanaQuery**
> idGetGrafanaQuery()

Handle GET request for Grafana queries

Used for handling Grafana queries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    try {
      apiInstance.idGetGrafanaQuery();
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idGetGrafanaQuery");
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

<a id="idPostGrafanaBoards"></a>
# **idPostGrafanaBoards**
> idPostGrafanaBoards()

Handle POST request for Grafana boards

Used for persist Grafana boards and panel selections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    try {
      apiInstance.idPostGrafanaBoards();
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idPostGrafanaBoards");
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

<a id="idPostGrafanaConfig"></a>
# **idPostGrafanaConfig**
> idPostGrafanaConfig(grafanaConfigParams)

Handle POST request for Grafana configuration

Used for persisting Grafana configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GrafanaApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    GrafanaApiApi apiInstance = new GrafanaApiApi(defaultClient);
    GrafanaConfigParams grafanaConfigParams = new GrafanaConfigParams(); // GrafanaConfigParams | 
    try {
      apiInstance.idPostGrafanaConfig(grafanaConfigParams);
    } catch (ApiException e) {
      System.err.println("Exception when calling GrafanaApiApi#idPostGrafanaConfig");
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
| **grafanaConfigParams** | [**GrafanaConfigParams**](GrafanaConfigParams.md)|  | |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |


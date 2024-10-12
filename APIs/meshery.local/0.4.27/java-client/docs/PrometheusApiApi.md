# PrometheusApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeletePrometheusConfig**](PrometheusApiApi.md#idDeletePrometheusConfig) | **DELETE** /api/telemetry/metrics/config | Handle DELETE for Prometheus configuration |
| [**idGetPrometheusConfig**](PrometheusApiApi.md#idGetPrometheusConfig) | **GET** /api/telemetry/metrics/config | Handle GET for Prometheus configuration |
| [**idGetPrometheusPing**](PrometheusApiApi.md#idGetPrometheusPing) | **GET** /api/telemetry/metrics/ping | Handle GET request for Prometheus Ping |
| [**idGetPrometheusQuery**](PrometheusApiApi.md#idGetPrometheusQuery) | **GET** /api/telemetry/metrics/query | Handle GET request for Prometheus Query |
| [**idGetPrometheusStaticBoard**](PrometheusApiApi.md#idGetPrometheusStaticBoard) | **GET** /api/telemetry/metrics/static-board | Handle GET request for Prometheus static board |
| [**idPostPrometheusBoard**](PrometheusApiApi.md#idPostPrometheusBoard) | **POST** /api/telemetry/metrics/boards | Handle POST request for Prometheus board |
| [**idPostPrometheusBoardImport**](PrometheusApiApi.md#idPostPrometheusBoardImport) | **POST** /api/telemetry/metrics/board_import | Handle POST request for Prometheus board import |
| [**idPostPrometheusConfig**](PrometheusApiApi.md#idPostPrometheusConfig) | **POST** /api/telemetry/metrics/config | Handle POST for Prometheus configuration |


<a id="idDeletePrometheusConfig"></a>
# **idDeletePrometheusConfig**
> idDeletePrometheusConfig()

Handle DELETE for Prometheus configuration

Used for deleting Prometheus configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    try {
      apiInstance.idDeletePrometheusConfig();
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idDeletePrometheusConfig");
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

<a id="idGetPrometheusConfig"></a>
# **idGetPrometheusConfig**
> Prometheus idGetPrometheusConfig()

Handle GET for Prometheus configuration

Used for fetching Prometheus configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    try {
      Prometheus result = apiInstance.idGetPrometheusConfig();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idGetPrometheusConfig");
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

[**Prometheus**](Prometheus.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns prometheus configuration |  -  |

<a id="idGetPrometheusPing"></a>
# **idGetPrometheusPing**
> idGetPrometheusPing()

Handle GET request for Prometheus Ping

Used to ping prometheus

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    try {
      apiInstance.idGetPrometheusPing();
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idGetPrometheusPing");
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

<a id="idGetPrometheusQuery"></a>
# **idGetPrometheusQuery**
> idGetPrometheusQuery()

Handle GET request for Prometheus Query

Used to prometheus queries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    try {
      apiInstance.idGetPrometheusQuery();
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idGetPrometheusQuery");
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

<a id="idGetPrometheusStaticBoard"></a>
# **idGetPrometheusStaticBoard**
> Map&lt;String, GrafanaBoard&gt; idGetPrometheusStaticBoard()

Handle GET request for Prometheus static board

Used to fetch the static board

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    try {
      Map<String, GrafanaBoard> result = apiInstance.idGetPrometheusStaticBoard();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idGetPrometheusStaticBoard");
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

[**Map&lt;String, GrafanaBoard&gt;**](GrafanaBoard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns Prometheus static board |  -  |

<a id="idPostPrometheusBoard"></a>
# **idPostPrometheusBoard**
> idPostPrometheusBoard(selectedGrafanaConfig)

Handle POST request for Prometheus board

Used to persist selected board and panels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    List<SelectedGrafanaConfig> selectedGrafanaConfig = Arrays.asList(); // List<SelectedGrafanaConfig> | 
    try {
      apiInstance.idPostPrometheusBoard(selectedGrafanaConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idPostPrometheusBoard");
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
| **selectedGrafanaConfig** | [**List&lt;SelectedGrafanaConfig&gt;**](SelectedGrafanaConfig.md)|  | |

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

<a id="idPostPrometheusBoardImport"></a>
# **idPostPrometheusBoardImport**
> GrafanaBoard idPostPrometheusBoardImport()

Handle POST request for Prometheus board import

Used for importing Grafana board for Prometheus

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    try {
      GrafanaBoard result = apiInstance.idPostPrometheusBoardImport();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idPostPrometheusBoardImport");
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

[**GrafanaBoard**](GrafanaBoard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for prometheus board import |  -  |

<a id="idPostPrometheusConfig"></a>
# **idPostPrometheusConfig**
> idPostPrometheusConfig(body)

Handle POST for Prometheus configuration

Used for persisting Prometheus configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrometheusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PrometheusApiApi apiInstance = new PrometheusApiApi(defaultClient);
    String body = "body_example"; // String | 
    try {
      apiInstance.idPostPrometheusConfig(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrometheusApiApi#idPostPrometheusConfig");
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


# UtilsApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDataMetrics_0**](UtilsApi.md#getDataMetrics_0) | **GET** /platform/public/utils/metrics | Get metrics about the current data release |
| [**getDataStats_0**](UtilsApi.md#getDataStats_0) | **GET** /platform/public/utils/stats | Get statistics about the current data release |
| [**getPing_0**](UtilsApi.md#getPing_0) | **GET** /platform/public/utils/ping | Ping service |
| [**getTherapeuticAreas_0**](UtilsApi.md#getTherapeuticAreas_0) | **GET** /platform/public/utils/therapeuticareas | Get the list of therapeutic areas about the current data release |
| [**getVersion_0**](UtilsApi.md#getVersion_0) | **GET** /platform/public/utils/version | Get API version |


<a id="getDataMetrics_0"></a>
# **getDataMetrics_0**
> getDataMetrics_0()

Get metrics about the current data release

Returns the metrics about associations and evidences, divided by datasource, genes and so on. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    UtilsApi apiInstance = new UtilsApi(defaultClient);
    try {
      apiInstance.getDataMetrics_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilsApi#getDataMetrics_0");
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
| **200** | Successful response |  -  |

<a id="getDataStats_0"></a>
# **getDataStats_0**
> getDataStats_0()

Get statistics about the current data release

Returns the number of associations and evidences, divided by datasource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    UtilsApi apiInstance = new UtilsApi(defaultClient);
    try {
      apiInstance.getDataStats_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilsApi#getDataStats_0");
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
| **200** | Successful response |  -  |

<a id="getPing_0"></a>
# **getPing_0**
> getPing_0()

Ping service

Check if the API is up 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    UtilsApi apiInstance = new UtilsApi(defaultClient);
    try {
      apiInstance.getPing_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilsApi#getPing_0");
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
| **200** | Successful response |  -  |

<a id="getTherapeuticAreas_0"></a>
# **getTherapeuticAreas_0**
> getTherapeuticAreas_0()

Get the list of therapeutic areas about the current data release

Returns the list of therapeutic areas for the current data release 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    UtilsApi apiInstance = new UtilsApi(defaultClient);
    try {
      apiInstance.getTherapeuticAreas_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilsApi#getTherapeuticAreas_0");
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
| **200** | Successful response |  -  |

<a id="getVersion_0"></a>
# **getVersion_0**
> getVersion_0()

Get API version

Returns current API version. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    UtilsApi apiInstance = new UtilsApi(defaultClient);
    try {
      apiInstance.getVersion_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilsApi#getVersion_0");
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
| **200** | Successful response |  -  |


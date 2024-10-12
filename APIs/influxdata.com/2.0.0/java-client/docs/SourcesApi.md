# SourcesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSourcesID**](SourcesApi.md#deleteSourcesID) | **DELETE** /sources/{sourceID} | Delete a source |
| [**getSources**](SourcesApi.md#getSources) | **GET** /sources | List all sources |
| [**getSourcesID**](SourcesApi.md#getSourcesID) | **GET** /sources/{sourceID} | Retrieve a source |
| [**getSourcesIDBuckets**](SourcesApi.md#getSourcesIDBuckets) | **GET** /sources/{sourceID}/buckets | Get buckets in a source |
| [**getSourcesIDHealth**](SourcesApi.md#getSourcesIDHealth) | **GET** /sources/{sourceID}/health | Get the health of a source |
| [**patchSourcesID**](SourcesApi.md#patchSourcesID) | **PATCH** /sources/{sourceID} | Update a Source |
| [**postSources**](SourcesApi.md#postSources) | **POST** /sources | Create a source |


<a id="deleteSourcesID"></a>
# **deleteSourcesID**
> deleteSourcesID(sourceID, zapTraceSpan)

Delete a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String sourceID = "sourceID_example"; // String | The source ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteSourcesID(sourceID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#deleteSourcesID");
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
| **sourceID** | **String**| The source ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | View not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getSources"></a>
# **getSources**
> Sources getSources(zapTraceSpan, org)

List all sources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String org = "org_example"; // String | The name of the organization.
    try {
      Sources result = apiInstance.getSources(zapTraceSpan, org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#getSources");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **org** | **String**| The name of the organization. | [optional] |

### Return type

[**Sources**](Sources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of sources |  -  |
| **0** | Unexpected error |  -  |

<a id="getSourcesID"></a>
# **getSourcesID**
> Source getSourcesID(sourceID, zapTraceSpan)

Retrieve a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String sourceID = "sourceID_example"; // String | The source ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Source result = apiInstance.getSourcesID(sourceID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#getSourcesID");
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
| **sourceID** | **String**| The source ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A source |  -  |
| **404** | Source not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getSourcesIDBuckets"></a>
# **getSourcesIDBuckets**
> Buckets getSourcesIDBuckets(sourceID, zapTraceSpan, org)

Get buckets in a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String sourceID = "sourceID_example"; // String | The source ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String org = "org_example"; // String | The name of the organization.
    try {
      Buckets result = apiInstance.getSourcesIDBuckets(sourceID, zapTraceSpan, org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#getSourcesIDBuckets");
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
| **sourceID** | **String**| The source ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **org** | **String**| The name of the organization. | [optional] |

### Return type

[**Buckets**](Buckets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A source |  -  |
| **404** | Source not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getSourcesIDHealth"></a>
# **getSourcesIDHealth**
> HealthCheck getSourcesIDHealth(sourceID, zapTraceSpan)

Get the health of a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String sourceID = "sourceID_example"; // String | The source ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      HealthCheck result = apiInstance.getSourcesIDHealth(sourceID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#getSourcesIDHealth");
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
| **sourceID** | **String**| The source ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**HealthCheck**](HealthCheck.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The source is healthy |  -  |
| **503** | The source is not healthy |  -  |
| **0** | Unexpected error |  -  |

<a id="patchSourcesID"></a>
# **patchSourcesID**
> Source patchSourcesID(sourceID, source, zapTraceSpan)

Update a Source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String sourceID = "sourceID_example"; // String | The source ID.
    Source source = new Source(); // Source | Source update
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Source result = apiInstance.patchSourcesID(sourceID, source, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#patchSourcesID");
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
| **sourceID** | **String**| The source ID. | |
| **source** | [**Source**](Source.md)| Source update | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created Source |  -  |
| **404** | Source not found |  -  |
| **0** | Unexpected error |  -  |

<a id="postSources"></a>
# **postSources**
> Source postSources(source, zapTraceSpan)

Create a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    Source source = new Source(); // Source | Source to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Source result = apiInstance.postSources(source, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#postSources");
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
| **source** | [**Source**](Source.md)| Source to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created Source |  -  |
| **0** | Unexpected error |  -  |


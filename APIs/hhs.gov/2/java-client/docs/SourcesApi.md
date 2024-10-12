# SourcesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesSourcesIdJsonGet**](SourcesApi.md#resourcesSourcesIdJsonGet) | **GET** /resources/sources/{id}.json | Get Source by ID |
| [**resourcesSourcesIdSyndicateFormatGet**](SourcesApi.md#resourcesSourcesIdSyndicateFormatGet) | **GET** /resources/sources/{id}/syndicate.{format} | Get MediaItems for Source |
| [**resourcesSourcesJsonGet**](SourcesApi.md#resourcesSourcesJsonGet) | **GET** /resources/sources.json | Get Sources |


<a id="resourcesSourcesIdJsonGet"></a>
# **resourcesSourcesIdJsonGet**
> List&lt;SourceWrapped&gt; resourcesSourcesIdJsonGet(id)

Get Source by ID

Information about a specific source.

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
    Long id = 56L; // Long | The id of the source to look up
    try {
      List<SourceWrapped> result = apiInstance.resourcesSourcesIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#resourcesSourcesIdJsonGet");
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
| **id** | **Long**| The id of the source to look up | |

### Return type

[**List&lt;SourceWrapped&gt;**](SourceWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Source identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesSourcesIdSyndicateFormatGet"></a>
# **resourcesSourcesIdSyndicateFormatGet**
> List&lt;MediaItemWrapped&gt; resourcesSourcesIdSyndicateFormatGet(id, format, displayMethod)

Get MediaItems for Source

MediaItem

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
    Long id = 56L; // Long | The id of the record to look up
    String format = "format_example"; // String | Automatically added
    String displayMethod = "displayMethod_example"; // String | Method used to render an html request. Accepts one: [mv, list, feed]
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesSourcesIdSyndicateFormatGet(id, format, displayMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#resourcesSourcesIdSyndicateFormatGet");
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
| **id** | **Long**| The id of the record to look up | |
| **format** | **String**| Automatically added | |
| **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Renders the list of MediaItems associated with the Source identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesSourcesJsonGet"></a>
# **resourcesSourcesJsonGet**
> List&lt;SourceWrapped&gt; resourcesSourcesJsonGet(max, offset, sort)

Get Sources

Source Listings

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
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | Return records starting at the offset index.
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    try {
      List<SourceWrapped> result = apiInstance.resourcesSourcesJsonGet(max, offset, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#resourcesSourcesJsonGet");
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
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| Return records starting at the offset index. | [optional] |
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |

### Return type

[**List&lt;SourceWrapped&gt;**](SourceWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of Sources. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |


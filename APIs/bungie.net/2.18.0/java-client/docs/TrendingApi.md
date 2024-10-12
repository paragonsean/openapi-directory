# TrendingApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**trendingGetTrendingCategories**](TrendingApi.md#trendingGetTrendingCategories) | **GET** /Trending/Categories/ |  |
| [**trendingGetTrendingCategory**](TrendingApi.md#trendingGetTrendingCategory) | **GET** /Trending/Categories/{categoryId}/{pageNumber}/ |  |
| [**trendingGetTrendingEntryDetail**](TrendingApi.md#trendingGetTrendingEntryDetail) | **GET** /Trending/Details/{trendingEntryType}/{identifier}/ |  |


<a id="trendingGetTrendingCategories"></a>
# **trendingGetTrendingCategories**
> TrendingGetTrendingCategories200Response trendingGetTrendingCategories()



Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrendingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    TrendingApi apiInstance = new TrendingApi(defaultClient);
    try {
      TrendingGetTrendingCategories200Response result = apiInstance.trendingGetTrendingCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrendingApi#trendingGetTrendingCategories");
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

[**TrendingGetTrendingCategories200Response**](TrendingGetTrendingCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="trendingGetTrendingCategory"></a>
# **trendingGetTrendingCategory**
> TrendingGetTrendingCategory200Response trendingGetTrendingCategory(categoryId, pageNumber)



Returns paginated lists of trending items for a category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrendingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    TrendingApi apiInstance = new TrendingApi(defaultClient);
    String categoryId = "categoryId_example"; // String | The ID of the category for whom you want additional results.
    Integer pageNumber = 56; // Integer | The page # of results to return.
    try {
      TrendingGetTrendingCategory200Response result = apiInstance.trendingGetTrendingCategory(categoryId, pageNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrendingApi#trendingGetTrendingCategory");
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
| **categoryId** | **String**| The ID of the category for whom you want additional results. | |
| **pageNumber** | **Integer**| The page # of results to return. | |

### Return type

[**TrendingGetTrendingCategory200Response**](TrendingGetTrendingCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="trendingGetTrendingEntryDetail"></a>
# **trendingGetTrendingEntryDetail**
> TrendingGetTrendingEntryDetail200Response trendingGetTrendingEntryDetail(identifier, trendingEntryType)



Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrendingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    TrendingApi apiInstance = new TrendingApi(defaultClient);
    String identifier = "identifier_example"; // String | The identifier for the entity to be returned.
    Integer trendingEntryType = 56; // Integer | The type of entity to be returned.
    try {
      TrendingGetTrendingEntryDetail200Response result = apiInstance.trendingGetTrendingEntryDetail(identifier, trendingEntryType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrendingApi#trendingGetTrendingEntryDetail");
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
| **identifier** | **String**| The identifier for the entity to be returned. | |
| **trendingEntryType** | **Integer**| The type of entity to be returned. | |

### Return type

[**TrendingGetTrendingEntryDetail200Response**](TrendingGetTrendingEntryDetail200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |


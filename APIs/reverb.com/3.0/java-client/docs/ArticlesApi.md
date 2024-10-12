# ArticlesApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**articlesCategoriesGet**](ArticlesApi.md#articlesCategoriesGet) | **GET** /articles/categories | List of all article categories |
| [**articlesGet**](ArticlesApi.md#articlesGet) | **GET** /articles |  |


<a id="articlesCategoriesGet"></a>
# **articlesCategoriesGet**
> articlesCategoriesGet()

List of all article categories

List of all article categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    try {
      apiInstance.articlesCategoriesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesCategoriesGet");
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
| **0** | Unexpected error |  -  |

<a id="articlesGet"></a>
# **articlesGet**
> articlesGet(page, perPage, offset, query, excludeFeatured)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    String query = "query_example"; // String | What's being searched for
    Integer excludeFeatured = 56; // Integer | Number of featured articles to exclude
    try {
      apiInstance.articlesGet(page, perPage, offset, query, excludeFeatured);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesGet");
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
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |
| **query** | **String**| What&#39;s being searched for | [optional] |
| **excludeFeatured** | **Integer**| Number of featured articles to exclude | [optional] |

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
| **0** | Unexpected error |  -  |


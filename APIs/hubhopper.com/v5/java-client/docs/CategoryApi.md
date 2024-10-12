# CategoryApi

All URIs are relative to *https://apis.hubhopper.com/partner*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesCategoryIdGet**](CategoryApi.md#categoriesCategoryIdGet) | **GET** /categories/{categoryId} |  |
| [**categoriesCategoryIdPodcastsGet**](CategoryApi.md#categoriesCategoryIdPodcastsGet) | **GET** /categories/{categoryId}/podcasts |  |
| [**categoriesGet**](CategoryApi.md#categoriesGet) | **GET** /categories |  |


<a id="categoriesCategoryIdGet"></a>
# **categoriesCategoryIdGet**
> SingleCategory categoriesCategoryIdGet(categoryId)



Get specific content category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.hubhopper.com/partner");
    
    // Configure API key authorization: partner_id
    ApiKeyAuth partner_id = (ApiKeyAuth) defaultClient.getAuthentication("partner_id");
    partner_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //partner_id.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String categoryId = "categoryId_example"; // String | Unique qualifier for a category.
    try {
      SingleCategory result = apiInstance.categoriesCategoryIdGet(categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoriesCategoryIdGet");
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
| **categoryId** | **String**| Unique qualifier for a category. | |

### Return type

[**SingleCategory**](SingleCategory.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
| **404** | 404 response |  -  |
| **500** | 500 response |  -  |

<a id="categoriesCategoryIdPodcastsGet"></a>
# **categoriesCategoryIdPodcastsGet**
> PodcastList categoriesCategoryIdPodcastsGet(categoryId, page, pageSize, order, filters)



Get a list of all podcasts under a category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.hubhopper.com/partner");
    
    // Configure API key authorization: partner_id
    ApiKeyAuth partner_id = (ApiKeyAuth) defaultClient.getAuthentication("partner_id");
    partner_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //partner_id.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String categoryId = "categoryId_example"; // String | Unique qualifier for a category.
    String page = "page_example"; // String | Provide the page number to fetch.
    String pageSize = "pageSize_example"; // String | Provide the size of the page to fetch.
    String order = "order_example"; // String | Order the items by 'newest' | 'random'
    String filters = "filters_example"; // String | Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
    try {
      PodcastList result = apiInstance.categoriesCategoryIdPodcastsGet(categoryId, page, pageSize, order, filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoriesCategoryIdPodcastsGet");
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
| **categoryId** | **String**| Unique qualifier for a category. | |
| **page** | **String**| Provide the page number to fetch. | [optional] |
| **pageSize** | **String**| Provide the size of the page to fetch. | [optional] |
| **order** | **String**| Order the items by &#39;newest&#39; | &#39;random&#39; | [optional] |
| **filters** | **String**| Takes filters like &#39;lang&#39; in a url encoded json.  Example: 1)Single -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); 2)Multiple -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;,\&quot;hi\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); | [optional] |

### Return type

[**PodcastList**](PodcastList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
| **404** | 404 response |  -  |
| **500** | 500 response |  -  |

<a id="categoriesGet"></a>
# **categoriesGet**
> CategoryList categoriesGet(pageSize, page)



Get the list of all content categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.hubhopper.com/partner");
    
    // Configure API key authorization: partner_id
    ApiKeyAuth partner_id = (ApiKeyAuth) defaultClient.getAuthentication("partner_id");
    partner_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //partner_id.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String pageSize = "pageSize_example"; // String | Provide the size of the page to fetch.
    String page = "page_example"; // String | Provide the page number to fetch.
    try {
      CategoryList result = apiInstance.categoriesGet(pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoriesGet");
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
| **pageSize** | **String**| Provide the size of the page to fetch. | [optional] |
| **page** | **String**| Provide the page number to fetch. | [optional] |

### Return type

[**CategoryList**](CategoryList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 response |  * Access-Control-Allow-Origin -  <br>  |
| **404** | 404 response |  -  |
| **500** | 500 response |  -  |


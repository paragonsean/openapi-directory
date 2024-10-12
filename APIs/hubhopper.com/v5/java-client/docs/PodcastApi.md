# PodcastApi

All URIs are relative to *https://apis.hubhopper.com/partner*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**podcastsGet**](PodcastApi.md#podcastsGet) | **GET** /podcasts |  |
| [**podcastsPodcastIdEpisodesGet**](PodcastApi.md#podcastsPodcastIdEpisodesGet) | **GET** /podcasts/{podcastId}/episodes |  |
| [**podcastsPodcastIdGet**](PodcastApi.md#podcastsPodcastIdGet) | **GET** /podcasts/{podcastId} |  |


<a id="podcastsGet"></a>
# **podcastsGet**
> PodcastList podcastsGet(page, pageSize, order, filters)



Get the list of all podcasts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastApi;

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

    PodcastApi apiInstance = new PodcastApi(defaultClient);
    String page = "page_example"; // String | Provide the page number to fetch.
    String pageSize = "pageSize_example"; // String | Provide the size of the page to fetch.
    String order = "order_example"; // String | Order the items by 'newest' | 'random'
    String filters = "filters_example"; // String | Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
    try {
      PodcastList result = apiInstance.podcastsGet(page, pageSize, order, filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastApi#podcastsGet");
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

<a id="podcastsPodcastIdEpisodesGet"></a>
# **podcastsPodcastIdEpisodesGet**
> PodcastEpisodeList podcastsPodcastIdEpisodesGet(podcastId, page, pageSize, order, filters)



Get a list of all episodes under a podcast.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastApi;

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

    PodcastApi apiInstance = new PodcastApi(defaultClient);
    String podcastId = "podcastId_example"; // String | Unique qualifier for a podcast.
    String page = "page_example"; // String | Provide the page number to fetch.
    String pageSize = "pageSize_example"; // String | Provide the size of the page to fetch.
    String order = "order_example"; // String | Order the items by 'newest' | 'random'
    String filters = "filters_example"; // String | Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
    try {
      PodcastEpisodeList result = apiInstance.podcastsPodcastIdEpisodesGet(podcastId, page, pageSize, order, filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastApi#podcastsPodcastIdEpisodesGet");
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
| **podcastId** | **String**| Unique qualifier for a podcast. | |
| **page** | **String**| Provide the page number to fetch. | [optional] |
| **pageSize** | **String**| Provide the size of the page to fetch. | [optional] |
| **order** | **String**| Order the items by &#39;newest&#39; | &#39;random&#39; | [optional] |
| **filters** | **String**| Takes filters like &#39;lang&#39; in a url encoded json.  Example: 1)Single -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); 2)Multiple -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;,\&quot;hi\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); | [optional] |

### Return type

[**PodcastEpisodeList**](PodcastEpisodeList.md)

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

<a id="podcastsPodcastIdGet"></a>
# **podcastsPodcastIdGet**
> SinglePodcast podcastsPodcastIdGet(podcastId)



Get a single Podcast.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastApi;

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

    PodcastApi apiInstance = new PodcastApi(defaultClient);
    String podcastId = "podcastId_example"; // String | Unique qualifier for a podcast.
    try {
      SinglePodcast result = apiInstance.podcastsPodcastIdGet(podcastId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastApi#podcastsPodcastIdGet");
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
| **podcastId** | **String**| Unique qualifier for a podcast. | |

### Return type

[**SinglePodcast**](SinglePodcast.md)

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


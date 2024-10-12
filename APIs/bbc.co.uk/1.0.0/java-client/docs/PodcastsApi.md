# PodcastsApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPodcastByPid**](PodcastsApi.md#getPodcastByPid) | **GET** /podcasts/{pid} | Podcast |
| [**getPodcastEpisodes**](PodcastsApi.md#getPodcastEpisodes) | **GET** /podcasts/{pid}/episodes | Podcast Episodes |
| [**getPodcasts**](PodcastsApi.md#getPodcasts) | **GET** /podcasts | All Podcasts |
| [**getPodcastsFeatured**](PodcastsApi.md#getPodcastsFeatured) | **GET** /podcasts/featured | Featured Podcasts |


<a id="getPodcastByPid"></a>
# **getPodcastByPid**
> PodcastsResponse getPodcastByPid(xAPIKey, pid, offset, limit)

Podcast

Retrieve data about the podcast with the supplied PID 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PodcastsApi apiInstance = new PodcastsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String pid = "pid_example"; // String | pid
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PodcastsResponse result = apiInstance.getPodcastByPid(xAPIKey, pid, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastsApi#getPodcastByPid");
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
| **xAPIKey** | **String**| API_KEY | |
| **pid** | **String**| pid | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**PodcastsResponse**](PodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPodcastEpisodes"></a>
# **getPodcastEpisodes**
> PodcastEpisodesResponse getPodcastEpisodes(xAPIKey, pid, offset, limit)

Podcast Episodes

Retrieve all episodes for a specific podcast 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PodcastsApi apiInstance = new PodcastsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String pid = "pid_example"; // String | pid
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PodcastEpisodesResponse result = apiInstance.getPodcastEpisodes(xAPIKey, pid, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastsApi#getPodcastEpisodes");
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
| **xAPIKey** | **String**| API_KEY | |
| **pid** | **String**| pid | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**PodcastEpisodesResponse**](PodcastEpisodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPodcasts"></a>
# **getPodcasts**
> PodcastsResponse getPodcasts(xAPIKey, offset, limit, sort, network, networkUrlKey, category, q, coverage)

All Podcasts

Retrieve all Podcasts 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PodcastsApi apiInstance = new PodcastsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String sort = "title"; // String | Sort order for Podcasts results
    String network = "network_example"; // String | Network Master Brand ID (mid)
    String networkUrlKey = "networkUrlKey_example"; // String | Network URL key
    String category = "category_example"; // String | Category ID
    String q = "q_example"; // String | Search query String
    String coverage = "local"; // String | Local, National or Regional Coverage
    try {
      PodcastsResponse result = apiInstance.getPodcasts(xAPIKey, offset, limit, sort, network, networkUrlKey, category, q, coverage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastsApi#getPodcasts");
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
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **sort** | **String**| Sort order for Podcasts results | [optional] [enum: title, -title, available_from_date, -available_from_date] |
| **network** | **String**| Network Master Brand ID (mid) | [optional] |
| **networkUrlKey** | **String**| Network URL key | [optional] |
| **category** | **String**| Category ID | [optional] |
| **q** | **String**| Search query String | [optional] |
| **coverage** | **String**| Local, National or Regional Coverage | [optional] [enum: local, national, regional] |

### Return type

[**PodcastsResponse**](PodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="getPodcastsFeatured"></a>
# **getPodcastsFeatured**
> PodcastsFeaturedResponse getPodcastsFeatured(xAPIKey)

Featured Podcasts

Retrieve featured podcasts 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcastsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PodcastsApi apiInstance = new PodcastsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    try {
      PodcastsFeaturedResponse result = apiInstance.getPodcastsFeatured(xAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcastsApi#getPodcastsFeatured");
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
| **xAPIKey** | **String**| API_KEY | |

### Return type

[**PodcastsFeaturedResponse**](PodcastsFeaturedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |


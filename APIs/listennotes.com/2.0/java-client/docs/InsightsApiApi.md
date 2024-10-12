# InsightsApiApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPodcastAudience**](InsightsApiApi.md#getPodcastAudience) | **GET** /podcasts/{id}/audience | Fetch audience demographics for a podcast |
| [**getPodcastsByDomainName**](InsightsApiApi.md#getPodcastsByDomainName) | **GET** /podcasts/domains/{domain_name} | Fetch podcasts by a publisher&#39;s domain name |


<a id="getPodcastAudience"></a>
# **getPodcastAudience**
> PodcastAudienceResponse getPodcastAudience(xListenAPIKey, id)

Fetch audience demographics for a podcast

Fetch audience demographics for a podcast - 1) directly measured on the Listen Notes platform; 2) only supports audience breakdown by regions for now; 3) not every podcast has data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    InsightsApiApi apiInstance = new InsightsApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "25212ac3c53240a880dd5032e547047b"; // String | Podcast id.
    try {
      PodcastAudienceResponse result = apiInstance.getPodcastAudience(xListenAPIKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsApiApi#getPodcastAudience");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **id** | **String**| Podcast id. | |

### Return type

[**PodcastAudienceResponse**](PodcastAudienceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getPodcastsByDomainName"></a>
# **getPodcastsByDomainName**
> PodcastDomainResponse getPodcastsByDomainName(xListenAPIKey, domainName, page)

Fetch podcasts by a publisher&#39;s domain name

Fetch podcasts by a publisher&#39;s domain name, e.g., nytimes.com, wondery.com, npr.org... Each request will return up to 10 podcasts. You can use the &#x60;page&#x60; parameter to paginate. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    InsightsApiApi apiInstance = new InsightsApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String domainName = "nytimes.com"; // String | A publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...
    Integer page = 1; // Integer | Page number of the podcasts from this domain name
    try {
      PodcastDomainResponse result = apiInstance.getPodcastsByDomainName(xListenAPIKey, domainName, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsApiApi#getPodcastsByDomainName");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **domainName** | **String**| A publisher&#39;s domain name, e.g., nytimes.com, wondery.com, npr.org... | |
| **page** | **Integer**| Page number of the podcasts from this domain name | [optional] [default to 1] |

### Return type

[**PodcastDomainResponse**](PodcastDomainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |


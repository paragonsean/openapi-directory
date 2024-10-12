# PodcasterApiApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePodcastById**](PodcasterApiApi.md#deletePodcastById) | **DELETE** /podcasts/{id} | Request to delete a podcast |
| [**submitPodcast**](PodcasterApiApi.md#submitPodcast) | **POST** /podcasts/submit | Submit a podcast to Listen Notes database |


<a id="deletePodcastById"></a>
# **deletePodcastById**
> DeletePodcastResponse deletePodcastById(xListenAPIKey, id, reason)

Request to delete a podcast

Podcast hosting services can use this endpoint to streamline the process of podcast deletion on behave of their users (podcasters). We will review the deletion request within 12 hours. If the podcast is already deleted, the \&quot;status\&quot; field in the response will be \&quot;deleted\&quot;. Otherwise, the status field will be \&quot;in review\&quot;. If you want to get a notification once the podcast is deleted, you can configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcasterApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    PodcasterApiApi apiInstance = new PodcasterApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "4d3fe717742d4963a85562e9f84d8c79"; // String | Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...
    String reason = "the podcaster wants to delete it"; // String | The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put \"testing\" here to indicate that you are testing this endpoint, so we will not actually delete the podcast.
    try {
      DeletePodcastResponse result = apiInstance.deletePodcastById(xListenAPIKey, id, reason);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcasterApiApi#deletePodcastById");
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
| **id** | **String**| Podcast id. You can get podcast id from using other endpoints, e.g., &#x60;GET /search&#x60;, &#x60;GET /best_podcasts&#x60;... | |
| **reason** | **String**| The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put \&quot;testing\&quot; here to indicate that you are testing this endpoint, so we will not actually delete the podcast. | [optional] |

### Return type

[**DeletePodcastResponse**](DeletePodcastResponse.md)

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

<a id="submitPodcast"></a>
# **submitPodcast**
> SubmitPodcastResponse submitPodcast(xListenAPIKey, rss, email)

Submit a podcast to Listen Notes database

Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn&#39;t exist in the database, \&quot;status\&quot; in the response will be \&quot;in review\&quot;, and we&#39;ll review it within 12 hours. If the podcast exists, \&quot;status\&quot; in the response will be \&quot;found\&quot;. If this submission is rejected, \&quot;status\&quot; in the response will be \&quot;rejected\&quot;. You can use &#x60;POST /podcasts&#x60; to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the \&quot;email\&quot; parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodcasterApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    PodcasterApiApi apiInstance = new PodcasterApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String rss = "rss_example"; // String | A valid podcast rss url.
    String email = "email_example"; // String | A valid email address. If **email** is specified, then we'll notify this email address once the podcast is accepted.
    try {
      SubmitPodcastResponse result = apiInstance.submitPodcast(xListenAPIKey, rss, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodcasterApiApi#submitPodcast");
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
| **rss** | **String**| A valid podcast rss url. | |
| **email** | **String**| A valid email address. If **email** is specified, then we&#39;ll notify this email address once the podcast is accepted. | [optional] |

### Return type

[**SubmitPodcastResponse**](SubmitPodcastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **400** |  |  -  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |


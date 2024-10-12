# DefaultApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**podcastDeletedPost**](DefaultApi.md#podcastDeletedPost) | **POST** /podcastDeleted |  |
| [**podcastsSubmitAcceptedPost**](DefaultApi.md#podcastsSubmitAcceptedPost) | **POST** /podcastsSubmitAccepted |  |
| [**podcastsSubmitRejectedPost**](DefaultApi.md#podcastsSubmitRejectedPost) | **POST** /podcastsSubmitRejected |  |


<a id="podcastDeletedPost"></a>
# **podcastDeletedPost**
> podcastDeletedPost(podcastMinimumRss)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PodcastMinimumRss podcastMinimumRss = new PodcastMinimumRss(); // PodcastMinimumRss | Triggered by your request to DELETE /podcasts/{id}, if the podcast is actually deleted.
    try {
      apiInstance.podcastDeletedPost(podcastMinimumRss);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#podcastDeletedPost");
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
| **podcastMinimumRss** | [**PodcastMinimumRss**](PodcastMinimumRss.md)| Triggered by your request to DELETE /podcasts/{id}, if the podcast is actually deleted. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a 200 status to indicate that the data was received successfully |  -  |

<a id="podcastsSubmitAcceptedPost"></a>
# **podcastsSubmitAcceptedPost**
> podcastsSubmitAcceptedPost(podcastMinimumRss)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    PodcastMinimumRss podcastMinimumRss = new PodcastMinimumRss(); // PodcastMinimumRss | Triggered by your request to POST /podcasts/submit, if the podcast submission is accepted.
    try {
      apiInstance.podcastsSubmitAcceptedPost(podcastMinimumRss);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#podcastsSubmitAcceptedPost");
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
| **podcastMinimumRss** | [**PodcastMinimumRss**](PodcastMinimumRss.md)| Triggered by your request to POST /podcasts/submit, if the podcast submission is accepted. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a 200 status to indicate that the data was received successfully |  -  |

<a id="podcastsSubmitRejectedPost"></a>
# **podcastsSubmitRejectedPost**
> podcastsSubmitRejectedPost(UNKNOWN_BASE_TYPE)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE = new UNKNOWN_BASE_TYPE(); // UNKNOWN_BASE_TYPE | Triggered by your request to POST /podcasts/submit, if the podcast submission is rejected.
    try {
      apiInstance.podcastsSubmitRejectedPost(UNKNOWN_BASE_TYPE);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#podcastsSubmitRejectedPost");
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
| **UNKNOWN_BASE_TYPE** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Triggered by your request to POST /podcasts/submit, if the podcast submission is rejected. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a 200 status to indicate that the data was received successfully |  -  |


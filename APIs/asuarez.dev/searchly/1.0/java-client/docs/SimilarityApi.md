# SimilarityApi

All URIs are relative to *https://searchly.asuarez.dev/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**srcSearchlyApiV1ControllersSimilarityByContent**](SimilarityApi.md#srcSearchlyApiV1ControllersSimilarityByContent) | **POST** /similarity/by_content | API endpoint to search similarity using content |
| [**srcSearchlyApiV1ControllersSimilarityBySong**](SimilarityApi.md#srcSearchlyApiV1ControllersSimilarityBySong) | **GET** /similarity/by_song | API endpoint to search similarity using a song identifier |


<a id="srcSearchlyApiV1ControllersSimilarityByContent"></a>
# **srcSearchlyApiV1ControllersSimilarityByContent**
> APIResponseSimilarity srcSearchlyApiV1ControllersSimilarityByContent(srcSearchlyApiV1ControllersSimilarityByContentRequest)

API endpoint to search similarity using content

Endpoint for an end-user client to search similarity by content.  If you want to run the /similarity/by_content operation, you can do so via an HTTP POST command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/similarity/by_content &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://searchly.asuarez.dev/api/v1");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    SrcSearchlyApiV1ControllersSimilarityByContentRequest srcSearchlyApiV1ControllersSimilarityByContentRequest = new SrcSearchlyApiV1ControllersSimilarityByContentRequest(); // SrcSearchlyApiV1ControllersSimilarityByContentRequest | Body wrapper for the request.
    try {
      APIResponseSimilarity result = apiInstance.srcSearchlyApiV1ControllersSimilarityByContent(srcSearchlyApiV1ControllersSimilarityByContentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#srcSearchlyApiV1ControllersSimilarityByContent");
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
| **srcSearchlyApiV1ControllersSimilarityByContentRequest** | [**SrcSearchlyApiV1ControllersSimilarityByContentRequest**](SrcSearchlyApiV1ControllersSimilarityByContentRequest.md)| Body wrapper for the request. | |

### Return type

[**APIResponseSimilarity**](APIResponseSimilarity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/text

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard SearchLy API v1 JSON response. You should check the &#x60;error&#x60; attribute to determine if there was an error. |  -  |
| **0** | Unexpected error. |  -  |

<a id="srcSearchlyApiV1ControllersSimilarityBySong"></a>
# **srcSearchlyApiV1ControllersSimilarityBySong**
> APIResponseSimilarity srcSearchlyApiV1ControllersSimilarityBySong(songId)

API endpoint to search similarity using a song identifier

Endpoint for an end-user client to search similarity by song identifier.  If you want to run the /similarity/by_song operation, you can do so via an HTTP GET command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/similarity/by_song &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://searchly.asuarez.dev/api/v1");

    SimilarityApi apiInstance = new SimilarityApi(defaultClient);
    Integer songId = 234; // Integer | Song identifier.
    try {
      APIResponseSimilarity result = apiInstance.srcSearchlyApiV1ControllersSimilarityBySong(songId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarityApi#srcSearchlyApiV1ControllersSimilarityBySong");
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
| **songId** | **Integer**| Song identifier. | |

### Return type

[**APIResponseSimilarity**](APIResponseSimilarity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/text

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard SearchLy API v1 JSON response. You should check the &#x60;error&#x60; attribute to determine if there was an error. |  -  |
| **0** | Unexpected error. |  -  |


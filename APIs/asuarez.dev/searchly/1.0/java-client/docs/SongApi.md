# SongApi

All URIs are relative to *https://searchly.asuarez.dev/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**srcSearchlyApiV1ControllersSongSearch**](SongApi.md#srcSearchlyApiV1ControllersSongSearch) | **GET** /song/search | API endpoint to search songs from the database given a query |


<a id="srcSearchlyApiV1ControllersSongSearch"></a>
# **srcSearchlyApiV1ControllersSongSearch**
> APIResponseSong srcSearchlyApiV1ControllersSongSearch(query)

API endpoint to search songs from the database given a query

Endpoint for an end-user client to search songs from the database given a String query.  If you want to run the /song/search operation, you can do so via an HTTP GET command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/song/search &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SongApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://searchly.asuarez.dev/api/v1");

    SongApi apiInstance = new SongApi(defaultClient);
    String query = "Miley Cyrus"; // String | Query.
    try {
      APIResponseSong result = apiInstance.srcSearchlyApiV1ControllersSongSearch(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SongApi#srcSearchlyApiV1ControllersSongSearch");
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
| **query** | **String**| Query. | |

### Return type

[**APIResponseSong**](APIResponseSong.md)

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


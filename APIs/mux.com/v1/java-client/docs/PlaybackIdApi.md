# PlaybackIdApi

All URIs are relative to *https://api.mux.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssetOrLivestreamId**](PlaybackIdApi.md#getAssetOrLivestreamId) | **GET** /video/v1/playback-ids/{PLAYBACK_ID} | Retrieve an Asset or Live Stream ID |


<a id="getAssetOrLivestreamId"></a>
# **getAssetOrLivestreamId**
> GetAssetOrLiveStreamIdResponse getAssetOrLivestreamId(PLAYBACK_ID).execute();

Retrieve an Asset or Live Stream ID

Retrieves the Identifier of the Asset or Live Stream associated with the Playback ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaybackIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mux.com");
    
    // Configure HTTP basic authorization: accessToken
    HttpBasicAuth accessToken = (HttpBasicAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setUsername("YOUR USERNAME");
    accessToken.setPassword("YOUR PASSWORD");

    PlaybackIdApi apiInstance = new PlaybackIdApi(defaultClient);
    String PLAYBACK_ID = "PLAYBACK_ID_example"; // String | The live stream's playback ID.
    try {
      GetAssetOrLiveStreamIdResponse result = apiInstance.getAssetOrLivestreamId(PLAYBACK_ID)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaybackIdApi#getAssetOrLivestreamId");
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
| **PLAYBACK_ID** | **String**| The live stream&#39;s playback ID. | |

### Return type

[**GetAssetOrLiveStreamIdResponse**](GetAssetOrLiveStreamIdResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


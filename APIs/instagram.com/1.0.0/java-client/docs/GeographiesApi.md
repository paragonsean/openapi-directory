# GeographiesApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geographiesGeoIdMediaRecentGet**](GeographiesApi.md#geographiesGeoIdMediaRecentGet) | **GET** /geographies/{geo-id}/media/recent | Get recent media from a custom geo-id. |


<a id="geographiesGeoIdMediaRecentGet"></a>
# **geographiesGeoIdMediaRecentGet**
> MediaListResponse geographiesGeoIdMediaRecentGet(geoId, count, minId)

Get recent media from a custom geo-id.

Get recent media from a geography subscription that you created.  **Note:** You can only access Geographies that were explicitly created by your OAuth client. Check the Geography Subscriptions section of the [real-time updates page](https://instagram.com/developer/realtime/). When you create a subscription to some geography that you define, you will be returned a unique &#x60;geo-id&#x60; that can be used in this query. To backfill photos from the location covered by this geography, use the [media search endpoint](https://instagram.com/developer/endpoints/media/).  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    GeographiesApi apiInstance = new GeographiesApi(defaultClient);
    String geoId = "geoId_example"; // String | The geography ID.
    Integer count = 56; // Integer | Max number of media to return.
    String minId = "minId_example"; // String | Return media before this `min_id`.
    try {
      MediaListResponse result = apiInstance.geographiesGeoIdMediaRecentGet(geoId, count, minId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographiesApi#geographiesGeoIdMediaRecentGet");
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
| **geoId** | **String**| The geography ID. | |
| **count** | **Integer**| Max number of media to return. | [optional] |
| **minId** | **String**| Return media before this &#x60;min_id&#x60;. | [optional] |

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of recent media entries from a geography subscription. |  -  |


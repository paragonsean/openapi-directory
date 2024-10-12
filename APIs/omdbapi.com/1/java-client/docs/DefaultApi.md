# DefaultApi

All URIs are relative to *http://www.omdbapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOMDbSearch**](DefaultApi.md#getOMDbSearch) | **GET** / | OMDb Search |


<a id="getOMDbSearch"></a>
# **getOMDbSearch**
> CombinedResult getOMDbSearch(r, t, i, s, y, type, plot, tomatoes, v, page, paramCallback)

OMDb Search

Find a movie, series or episode from the OMDb by title, IMDb-id or by free-text search

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
    defaultClient.setBasePath("http://www.omdbapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String r = "json"; // String | The data type to return.
    String t = "t_example"; // String | Movie title to search for. One of t, i or s is required.
    String i = "i_example"; // String | A valid IMDb ID (e.g. tt1285016). One of t, i or s is required.
    String s = "s_example"; // String | Movie title to search for. One of t, i or s is required.
    Integer y = 56; // Integer | Year of release.
    String type = "movie"; // String | Type of result to return.
    String plot = "short"; // String | Return short or full plot.
    Boolean tomatoes = false; // Boolean | Include Rotten Tomatoes ratings.
    Integer v = 1; // Integer | API version (reserved for future use).
    Integer page = 1; // Integer | Page number to return.
    String paramCallback = "paramCallback_example"; // String | JSONP callback name.
    try {
      CombinedResult result = apiInstance.getOMDbSearch(r, t, i, s, y, type, plot, tomatoes, v, page, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOMDbSearch");
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
| **r** | **String**| The data type to return. | [default to json] [enum: json, xml] |
| **t** | **String**| Movie title to search for. One of t, i or s is required. | [optional] |
| **i** | **String**| A valid IMDb ID (e.g. tt1285016). One of t, i or s is required. | [optional] |
| **s** | **String**| Movie title to search for. One of t, i or s is required. | [optional] |
| **y** | **Integer**| Year of release. | [optional] |
| **type** | **String**| Type of result to return. | [optional] [enum: movie, series, episode] |
| **plot** | **String**| Return short or full plot. | [optional] [default to short] [enum: short, full] |
| **tomatoes** | **Boolean**| Include Rotten Tomatoes ratings. | [optional] [default to false] |
| **v** | **Integer**| API version (reserved for future use). | [optional] [default to 1] |
| **page** | **Integer**| Page number to return. | [optional] [default to 1] |
| **paramCallback** | **String**| JSONP callback name. | [optional] |

### Return type

[**CombinedResult**](CombinedResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |


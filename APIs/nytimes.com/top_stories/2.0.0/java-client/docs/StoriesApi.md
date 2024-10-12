# StoriesApi

All URIs are relative to *http://api.nytimes.com/svc/topstories/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sectionFormatGet**](StoriesApi.md#sectionFormatGet) | **GET** /{section}.{format} | Top Stories |


<a id="sectionFormatGet"></a>
# **sectionFormatGet**
> SectionFormatGet200Response sectionFormatGet(section, format, paramCallback)

Top Stories

The Top Stories API returns a list of articles and associated images currently on the specified section.  Support JSON and JSONP. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/topstories/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    StoriesApi apiInstance = new StoriesApi(defaultClient);
    String section = "home"; // String | The section the story appears in.
    String format = "json"; // String | if this is JSONP or JSON
    String paramCallback = "paramCallback_example"; // String | The name of the function the API call results will be passed to. Required when using JSONP. This parameter has only one valid value per section. The format is {section_name}TopStoriesCallback. 
    try {
      SectionFormatGet200Response result = apiInstance.sectionFormatGet(section, format, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoriesApi#sectionFormatGet");
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
| **section** | **String**| The section the story appears in. | [enum: home, opinion, world, national, politics, upshot, nyregion, business, technology, science, health, sports, arts, books, movies, theater, sundayreview, fashion, tmagazine, food, travel, magazine, realestate, automobiles, obituaries, insider] |
| **format** | **String**| if this is JSONP or JSON | [enum: json, jsonp] |
| **paramCallback** | **String**| The name of the function the API call results will be passed to. Required when using JSONP. This parameter has only one valid value per section. The format is {section_name}TopStoriesCallback.  | [optional] |

### Return type

[**SectionFormatGet200Response**](SectionFormatGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of articles |  -  |


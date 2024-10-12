# DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/suggest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timestagsGet**](DefaultApi.md#timestagsGet) | **GET** /timestags |  |


<a id="timestagsGet"></a>
# **timestagsGet**
> List&lt;List&lt;String&gt;&gt; timestagsGet(query, filter, max)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/suggest/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | Your search query
    String filter = "Des"; // String | If you do not specify a value for filter (see the Optional Parameters), your query will be matched to tags in all four Times dictionaries: subject, geographic location, organization and person. To use more than one, separate with commas. 
    Integer max = 10; // Integer | Sets the maximum number of results
    try {
      List<List<String>> result = apiInstance.timestagsGet(query, filter, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#timestagsGet");
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
| **query** | **String**| Your search query | |
| **filter** | **String**| If you do not specify a value for filter (see the Optional Parameters), your query will be matched to tags in all four Times dictionaries: subject, geographic location, organization and person. To use more than one, separate with commas.  | [optional] [enum: Des, Geo, Org, Per] |
| **max** | **Integer**| Sets the maximum number of results | [optional] [default to 10] |

### Return type

[**List&lt;List&lt;String&gt;&gt;**](List.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of tags |  -  |


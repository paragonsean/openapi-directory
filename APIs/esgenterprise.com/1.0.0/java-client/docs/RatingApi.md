# RatingApi

All URIs are relative to *https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchGet**](RatingApi.md#searchGet) | **GET** /search | List all company ESG Ratings |


<a id="searchGet"></a>
# **searchGet**
> SearchGet200Response searchGet(q)

List all company ESG Ratings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RatingApi apiInstance = new RatingApi(defaultClient);
    String q = "q_example"; // String | Company name or stock symbol
    try {
      SearchGet200Response result = apiInstance.searchGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatingApi#searchGet");
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
| **q** | **String**| Company name or stock symbol | |

### Return type

[**SearchGet200Response**](SearchGet200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of ESG Ratings |  * x-next - ESG ratings <br>  |


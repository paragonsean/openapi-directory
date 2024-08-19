# PathfinderApi

All URIs are relative to *https://api.breadcrumbs.one*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pathfinderPost**](PathfinderApi.md#pathfinderPost) | **POST** /pathfinder | Automatically find path between crypto addresses |


<a id="pathfinderPost"></a>
# **pathfinderPost**
> BreadcrumbsAPIModelsPathfinderPathfinderResponse pathfinderPost(breadcrumbsAPIModelsPathfinderPathfinderRequest)

Automatically find path between crypto addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PathfinderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.breadcrumbs.one");
    
    // Configure API key authorization: X-API-KEY
    ApiKeyAuth X-API-KEY = (ApiKeyAuth) defaultClient.getAuthentication("X-API-KEY");
    X-API-KEY.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-KEY.setApiKeyPrefix("Token");

    PathfinderApi apiInstance = new PathfinderApi(defaultClient);
    BreadcrumbsAPIModelsPathfinderPathfinderRequest breadcrumbsAPIModelsPathfinderPathfinderRequest = new BreadcrumbsAPIModelsPathfinderPathfinderRequest(); // BreadcrumbsAPIModelsPathfinderPathfinderRequest | 
    try {
      BreadcrumbsAPIModelsPathfinderPathfinderResponse result = apiInstance.pathfinderPost(breadcrumbsAPIModelsPathfinderPathfinderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PathfinderApi#pathfinderPost");
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
| **breadcrumbsAPIModelsPathfinderPathfinderRequest** | [**BreadcrumbsAPIModelsPathfinderPathfinderRequest**](BreadcrumbsAPIModelsPathfinderPathfinderRequest.md)|  | [optional] |

### Return type

[**BreadcrumbsAPIModelsPathfinderPathfinderResponse**](BreadcrumbsAPIModelsPathfinderPathfinderResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Client Error |  -  |


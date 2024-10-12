# ClickApi

All URIs are relative to *https://api.shorten.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getClicks**](ClickApi.md#getClicks) | **GET** /clicks | Get clicks |


<a id="getClicks"></a>
# **getClicks**
> GetClicksModel getClicks(continueFrom, limit)

Get clicks

Retrieve the raw click data for your account. Clicks are retrieved by creation date in descending order.    If there are more results than the limit for the request the response will return you a value in lastId property you can specify it in the continueFrom query parameter to get the next batch of records.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClickApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shorten.rest");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ClickApi apiInstance = new ClickApi(defaultClient);
    String continueFrom = "1588788835614657618"; // String | An ID returned by a previous query to continue clicks retrieval (see lastId in response)
    Integer limit = 1000; // Integer | Number of results to return per request
    try {
      GetClicksModel result = apiInstance.getClicks(continueFrom, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClickApi#getClicks");
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
| **continueFrom** | **String**| An ID returned by a previous query to continue clicks retrieval (see lastId in response) | [optional] |
| **limit** | **Integer**| Number of results to return per request | [optional] [default to 1000] |

### Return type

[**GetClicksModel**](GetClicksModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns Array of Click models, also returns lastId |  -  |


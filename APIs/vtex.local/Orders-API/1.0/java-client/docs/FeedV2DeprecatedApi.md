# FeedV2DeprecatedApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getfeedorderstatus**](FeedV2DeprecatedApi.md#getfeedorderstatus) | **GET** /api/oms/pvt/feed/orders/status | Get feed order status |


<a id="getfeedorderstatus"></a>
# **getfeedorderstatus**
> getfeedorderstatus(maxLot, accept, contentType)

Get feed order status

Get feed order status (deprecated)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedV2DeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    FeedV2DeprecatedApi apiInstance = new FeedV2DeprecatedApi(defaultClient);
    String maxLot = "{{maxLot}}"; // String | 
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String contentType = "application/json"; // String | Type of the content being sent
    try {
      apiInstance.getfeedorderstatus(maxLot, accept, contentType);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedV2DeprecatedApi#getfeedorderstatus");
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
| **maxLot** | **String**|  | [default to {{maxLot}}] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **contentType** | **String**| Type of the content being sent | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


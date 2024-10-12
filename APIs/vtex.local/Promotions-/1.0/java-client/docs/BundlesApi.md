# BundlesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**calculatediscountsandtaxesBundles**](BundlesApi.md#calculatediscountsandtaxesBundles) | **POST** /pub/bundles | Calculate discounts and taxes (Bundles) |


<a id="calculatediscountsandtaxesBundles"></a>
# **calculatediscountsandtaxesBundles**
> calculatediscountsandtaxesBundles(contentType, accept, calculatediscountsandtaxesBundlesRequest)

Calculate discounts and taxes (Bundles)

Calculate discounts and taxes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

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

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    CalculatediscountsandtaxesBundlesRequest calculatediscountsandtaxesBundlesRequest = new CalculatediscountsandtaxesBundlesRequest(); // CalculatediscountsandtaxesBundlesRequest | 
    try {
      apiInstance.calculatediscountsandtaxesBundles(contentType, accept, calculatediscountsandtaxesBundlesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#calculatediscountsandtaxesBundles");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **calculatediscountsandtaxesBundlesRequest** | [**CalculatediscountsandtaxesBundlesRequest**](CalculatediscountsandtaxesBundlesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


# AutocompleteApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoComplete**](AutocompleteApi.md#autoComplete) | **GET** /buscaautocomplete | Product Search Autocomplete |


<a id="autoComplete"></a>
# **autoComplete**
> TheRootSchema autoComplete(contentType, accept, productNameContains)

Product Search Autocomplete

Retrieves product&#39;s information related to the searched string.  &#x60;{{searchString}} is the part of string the user is looking for.  E.g.: &#x60;ref&#x60; | &#x60;refrig&#x60; | &#x60;refrigerator&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutocompleteApi;

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

    AutocompleteApi apiInstance = new AutocompleteApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String productNameContains = "jeans"; // String | Part of the string that will be searched.
    try {
      TheRootSchema result = apiInstance.autoComplete(contentType, accept, productNameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutocompleteApi#autoComplete");
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
| **contentType** | **String**| Type of the content being sent | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | |
| **productNameContains** | **String**| Part of the string that will be searched. | |

### Return type

[**TheRootSchema**](TheRootSchema.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |


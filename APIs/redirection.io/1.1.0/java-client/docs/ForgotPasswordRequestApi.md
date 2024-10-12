# ForgotPasswordRequestApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postForgotPasswordRequestCollection**](ForgotPasswordRequestApi.md#postForgotPasswordRequestCollection) | **POST** /users/forgot-password-request | Creates a ForgotPasswordRequest resource. |


<a id="postForgotPasswordRequestCollection"></a>
# **postForgotPasswordRequestCollection**
> ForgotPasswordRequest postForgotPasswordRequestCollection(forgotPasswordRequest)

Creates a ForgotPasswordRequest resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ForgotPasswordRequestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ForgotPasswordRequestApi apiInstance = new ForgotPasswordRequestApi(defaultClient);
    ForgotPasswordRequest forgotPasswordRequest = new ForgotPasswordRequest(); // ForgotPasswordRequest | The new ForgotPasswordRequest resource
    try {
      ForgotPasswordRequest result = apiInstance.postForgotPasswordRequestCollection(forgotPasswordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ForgotPasswordRequestApi#postForgotPasswordRequestCollection");
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
| **forgotPasswordRequest** | [**ForgotPasswordRequest**](ForgotPasswordRequest.md)| The new ForgotPasswordRequest resource | [optional] |

### Return type

[**ForgotPasswordRequest**](ForgotPasswordRequest.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ForgotPasswordRequest resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |


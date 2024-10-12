# HooksApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hooksPost**](HooksApi.md#hooksPost) | **POST** /hooks | Subscribe to webhooks |
| [**hooksUnsubscribePost**](HooksApi.md#hooksUnsubscribePost) | **POST** /hooks/unsubscribe | Unsubscribe from webhooks |


<a id="hooksPost"></a>
# **hooksPost**
> hooksPost(data)

Subscribe to webhooks

Use this endpoint to subscribe to webhooks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    HooksPostRequest data = new HooksPostRequest(); // HooksPostRequest | 
    try {
      apiInstance.hooksPost(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#hooksPost");
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
| **data** | [**HooksPostRequest**](HooksPostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully subscribed to the weebhooks |  -  |

<a id="hooksUnsubscribePost"></a>
# **hooksUnsubscribePost**
> hooksUnsubscribePost(data)

Unsubscribe from webhooks

Use this endpoint to unsubscribe from a webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    HooksUnsubscribePostRequest data = new HooksUnsubscribePostRequest(); // HooksUnsubscribePostRequest | 
    try {
      apiInstance.hooksUnsubscribePost(data);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#hooksUnsubscribePost");
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
| **data** | [**HooksUnsubscribePostRequest**](HooksUnsubscribePostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully unsubscribed from the weebhooks |  -  |


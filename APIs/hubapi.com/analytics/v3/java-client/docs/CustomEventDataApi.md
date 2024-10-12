# CustomEventDataApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postEventsV3SendSend**](CustomEventDataApi.md#postEventsV3SendSend) | **POST** /events/v3/send | Send custom event completion |


<a id="postEventsV3SendSend"></a>
# **postEventsV3SendSend**
> postEventsV3SendSend(behavioralEventHttpCompletionRequest)

Send custom event completion

Endpoint to send an instance of a custom event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomEventDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    CustomEventDataApi apiInstance = new CustomEventDataApi(defaultClient);
    BehavioralEventHttpCompletionRequest behavioralEventHttpCompletionRequest = new BehavioralEventHttpCompletionRequest(); // BehavioralEventHttpCompletionRequest | 
    try {
      apiInstance.postEventsV3SendSend(behavioralEventHttpCompletionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomEventDataApi#postEventsV3SendSend");
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
| **behavioralEventHttpCompletionRequest** | [**BehavioralEventHttpCompletionRequest**](BehavioralEventHttpCompletionRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | An error occurred. |  -  |


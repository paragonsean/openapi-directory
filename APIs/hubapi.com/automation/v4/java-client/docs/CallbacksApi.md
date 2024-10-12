# CallbacksApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postAutomationV4ActionsCallbacksCallbackIdCompleteComplete**](CallbacksApi.md#postAutomationV4ActionsCallbacksCallbackIdCompleteComplete) | **POST** /automation/v4/actions/callbacks/{callbackId}/complete | Completes a single callback |
| [**postAutomationV4ActionsCallbacksCompleteCompleteBatch**](CallbacksApi.md#postAutomationV4ActionsCallbacksCompleteCompleteBatch) | **POST** /automation/v4/actions/callbacks/complete | Completes a batch of callbacks |


<a id="postAutomationV4ActionsCallbacksCallbackIdCompleteComplete"></a>
# **postAutomationV4ActionsCallbacksCallbackIdCompleteComplete**
> postAutomationV4ActionsCallbacksCallbackIdCompleteComplete(callbackId, callbackCompletionRequest)

Completes a single callback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallbacksApi;

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

    CallbacksApi apiInstance = new CallbacksApi(defaultClient);
    String callbackId = "callbackId_example"; // String | 
    CallbackCompletionRequest callbackCompletionRequest = new CallbackCompletionRequest(); // CallbackCompletionRequest | 
    try {
      apiInstance.postAutomationV4ActionsCallbacksCallbackIdCompleteComplete(callbackId, callbackCompletionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallbacksApi#postAutomationV4ActionsCallbacksCallbackIdCompleteComplete");
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
| **callbackId** | **String**|  | |
| **callbackCompletionRequest** | [**CallbackCompletionRequest**](CallbackCompletionRequest.md)|  | |

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

<a id="postAutomationV4ActionsCallbacksCompleteCompleteBatch"></a>
# **postAutomationV4ActionsCallbacksCompleteCompleteBatch**
> postAutomationV4ActionsCallbacksCompleteCompleteBatch(batchInputCallbackCompletionBatchRequest)

Completes a batch of callbacks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallbacksApi;

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

    CallbacksApi apiInstance = new CallbacksApi(defaultClient);
    BatchInputCallbackCompletionBatchRequest batchInputCallbackCompletionBatchRequest = new BatchInputCallbackCompletionBatchRequest(); // BatchInputCallbackCompletionBatchRequest | 
    try {
      apiInstance.postAutomationV4ActionsCallbacksCompleteCompleteBatch(batchInputCallbackCompletionBatchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallbacksApi#postAutomationV4ActionsCallbacksCompleteCompleteBatch");
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
| **batchInputCallbackCompletionBatchRequest** | [**BatchInputCallbackCompletionBatchRequest**](BatchInputCallbackCompletionBatchRequest.md)|  | |

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


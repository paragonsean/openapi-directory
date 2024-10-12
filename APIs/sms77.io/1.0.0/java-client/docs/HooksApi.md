# HooksApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hooksGet**](HooksApi.md#hooksGet) | **GET** /hooks |  |
| [**hooksPOST**](HooksApi.md#hooksPOST) | **POST** /hooks |  |


<a id="hooksGet"></a>
# **hooksGet**
> HooksGet200Response hooksGet(action)



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
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    String action = "read"; // String | Determines the action to execute.
    try {
      HooksGet200Response result = apiInstance.hooksGet(action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#hooksGet");
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
| **action** | **String**| Determines the action to execute. | [enum: read] |

### Return type

[**HooksGet200Response**](HooksGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hooksPOST"></a>
# **hooksPOST**
> HooksPOST200Response hooksPOST(action, id, targetUrl, eventType, requestMethod)



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
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    String action = "subscribe"; // String | Determines the action to execute.
    Integer id = 56; // Integer | The Webhook ID you wish to unsubscribe.
    String targetUrl = "targetUrl_example"; // String | Target URL of your Webhook.
    String eventType = "all"; // String | Type of event for which you would like to receive a webhook.
    String requestMethod = "POST"; // String | Request method in which you want to receive the webhook.
    try {
      HooksPOST200Response result = apiInstance.hooksPOST(action, id, targetUrl, eventType, requestMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#hooksPOST");
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
| **action** | **String**| Determines the action to execute. | [enum: subscribe, unsubscribe] |
| **id** | **Integer**| The Webhook ID you wish to unsubscribe. | [optional] |
| **targetUrl** | **String**| Target URL of your Webhook. | [optional] |
| **eventType** | **String**| Type of event for which you would like to receive a webhook. | [optional] [enum: all, sms_mo, dlr, voice_status] |
| **requestMethod** | **String**| Request method in which you want to receive the webhook. | [optional] [default to POST] [enum: POST, JSON, GET] |

### Return type

[**HooksPOST200Response**](HooksPOST200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hook subscribed |  -  |


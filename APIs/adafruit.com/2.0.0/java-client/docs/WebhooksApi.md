# WebhooksApi

All URIs are relative to *https://io.adafruit.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRawWebhookFeedData**](WebhooksApi.md#createRawWebhookFeedData) | **POST** /webhooks/feed/:token/raw | Send arbitrary data to a feed via webhook URL. |
| [**createWebhookFeedData**](WebhooksApi.md#createWebhookFeedData) | **POST** /webhooks/feed/:token | Send data to a feed via webhook URL. |


<a id="createRawWebhookFeedData"></a>
# **createRawWebhookFeedData**
> Data createRawWebhookFeedData()

Send arbitrary data to a feed via webhook URL.

The raw data webhook receiver accepts POST requests and stores the raw request body on your feed. This is useful when you don&#39;t have control of the webhook sender. If feed history is turned on, payloads will be truncated at 1024 bytes. If feed history is turned off, payloads will be truncated at 100KB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      Data result = apiInstance.createRawWebhookFeedData();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createRawWebhookFeedData");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New feed data record |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="createWebhookFeedData"></a>
# **createWebhookFeedData**
> Data createWebhookFeedData(payload)

Send data to a feed via webhook URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://io.adafruit.com/api/v2");
    
    // Configure API key authorization: HeaderSignature
    ApiKeyAuth HeaderSignature = (ApiKeyAuth) defaultClient.getAuthentication("HeaderSignature");
    HeaderSignature.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderSignature.setApiKeyPrefix("Token");

    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    // Configure API key authorization: HeaderKey
    ApiKeyAuth HeaderKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderKey");
    HeaderKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderKey.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    CreateWebhookFeedDataRequest payload = new CreateWebhookFeedDataRequest(); // CreateWebhookFeedDataRequest | Webhook payload containing data `value` parameter.
    try {
      Data result = apiInstance.createWebhookFeedData(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createWebhookFeedData");
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
| **payload** | [**CreateWebhookFeedDataRequest**](CreateWebhookFeedDataRequest.md)| Webhook payload containing data &#x60;value&#x60; parameter. | |

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New feed data record |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |


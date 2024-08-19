# WebhooksApi

All URIs are relative to *https://api.sakari.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webhooksFetchAll**](WebhooksApi.md#webhooksFetchAll) | **GET** /v1/accounts/{accountId}/webhooks | Fetch active webhooks |
| [**webhooksSubscribe**](WebhooksApi.md#webhooksSubscribe) | **POST** /v1/accounts/{accountId}/webhooks | Subscribe to message events |
| [**webhooksUnsubscribe**](WebhooksApi.md#webhooksUnsubscribe) | **DELETE** /v1/accounts/{accountId}/webhooks/{url} | Unsubscribe to message events |


<a id="webhooksFetchAll"></a>
# **webhooksFetchAll**
> WebhooksResponse webhooksFetchAll(accountId)

Fetch active webhooks

When messages are acknowledge by carriers, a notification is sent to the specified URL

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    try {
      WebhooksResponse result = apiInstance.webhooksFetchAll(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksFetchAll");
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
| **accountId** | **String**| Account to apply operations to | |

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="webhooksSubscribe"></a>
# **webhooksSubscribe**
> WebhookResponse webhooksSubscribe(accountId, webhooksSubscribeRequest)

Subscribe to message events

When messages are acknowledge by carriers, a notification is sent to the specified URL

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    WebhooksSubscribeRequest webhooksSubscribeRequest = new WebhooksSubscribeRequest(); // WebhooksSubscribeRequest | 
    try {
      WebhookResponse result = apiInstance.webhooksSubscribe(accountId, webhooksSubscribeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksSubscribe");
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
| **accountId** | **String**| Account to apply operations to | |
| **webhooksSubscribeRequest** | [**WebhooksSubscribeRequest**](WebhooksSubscribeRequest.md)|  | |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="webhooksUnsubscribe"></a>
# **webhooksUnsubscribe**
> webhooksUnsubscribe(accountId, url)

Unsubscribe to message events

Delete subscription for receiving notifications

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
    defaultClient.setBasePath("https://api.sakari.io");
    
    // Configure OAuth2 access token for authorization: sakari_auth
    OAuth sakari_auth = (OAuth) defaultClient.getAuthentication("sakari_auth");
    sakari_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String accountId = "accountId_example"; // String | Account to apply operations to
    String url = "url_example"; // String | Account to apply operations to
    try {
      apiInstance.webhooksUnsubscribe(accountId, url);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksUnsubscribe");
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
| **accountId** | **String**| Account to apply operations to | |
| **url** | **String**| Account to apply operations to | |

### Return type

null (empty response body)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |


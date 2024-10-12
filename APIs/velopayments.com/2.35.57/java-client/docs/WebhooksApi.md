# WebhooksApi

All URIs are relative to *https://api.sandbox.velopayments.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebhookV1**](WebhooksApi.md#createWebhookV1) | **POST** /v1/webhooks | Create Webhook |
| [**getWebhookV1**](WebhooksApi.md#getWebhookV1) | **GET** /v1/webhooks/{webhookId} | Get details about the given webhook. |
| [**listWebhooksV1**](WebhooksApi.md#listWebhooksV1) | **GET** /v1/webhooks | List the details about the webhooks for the given payor. |
| [**pingWebhookV1**](WebhooksApi.md#pingWebhookV1) | **POST** /v1/webhooks/{webhookId}/ping |  |
| [**updateWebhookV1**](WebhooksApi.md#updateWebhookV1) | **POST** /v1/webhooks/{webhookId} | Update Webhook |


<a id="createWebhookV1"></a>
# **createWebhookV1**
> createWebhookV1(createWebhookRequest)

Create Webhook

Create Webhook

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    CreateWebhookRequest createWebhookRequest = new CreateWebhookRequest(); // CreateWebhookRequest | 
    try {
      apiInstance.createWebhookV1(createWebhookRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createWebhookV1");
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
| **createWebhookRequest** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Webhook Created |  * Location - Reference to Webhook object <br>  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="getWebhookV1"></a>
# **getWebhookV1**
> WebhookResponse getWebhookV1(webhookId)

Get details about the given webhook.

Get details about the given webhook.

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    UUID webhookId = UUID.randomUUID(); // UUID | Webhook id
    try {
      WebhookResponse result = apiInstance.getWebhookV1(webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getWebhookV1");
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
| **webhookId** | **UUID**| Webhook id | |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook response |  -  |
| **400** | Bad Request, Invalid path parameter |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="listWebhooksV1"></a>
# **listWebhooksV1**
> WebhooksResponse listWebhooksV1(payorId, page, pageSize)

List the details about the webhooks for the given payor.

List the details about the webhooks for the given payor.

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    UUID payorId = UUID.randomUUID(); // UUID | The Payor ID
    Integer page = 1; // Integer | Page number. Default is 1.
    Integer pageSize = 25; // Integer | The number of results to return in a page
    try {
      WebhooksResponse result = apiInstance.listWebhooksV1(payorId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#listWebhooksV1");
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
| **payorId** | **UUID**| The Payor ID | |
| **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return in a page | [optional] [default to 25] |

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook response |  -  |
| **400** | Invalid Request Parameters |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

<a id="pingWebhookV1"></a>
# **pingWebhookV1**
> PingResponse pingWebhookV1(webhookId)



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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    UUID webhookId = UUID.randomUUID(); // UUID | Webhook id
    try {
      PingResponse result = apiInstance.pingWebhookV1(webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#pingWebhookV1");
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
| **webhookId** | **UUID**| Webhook id | |

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Send ping |  -  |
| **400** | Bad Request, Invalid path parameter |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |

<a id="updateWebhookV1"></a>
# **updateWebhookV1**
> updateWebhookV1(webhookId, updateWebhookRequest)

Update Webhook

Update Webhook

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
    defaultClient.setBasePath("https://api.sandbox.velopayments.com");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    UUID webhookId = UUID.randomUUID(); // UUID | Webhook id
    UpdateWebhookRequest updateWebhookRequest = new UpdateWebhookRequest(); // UpdateWebhookRequest | 
    try {
      apiInstance.updateWebhookV1(webhookId, updateWebhookRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#updateWebhookV1");
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
| **webhookId** | **UUID**| Webhook id | |
| **updateWebhookRequest** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Webhook Updated |  -  |
| **400** | Invalid request. See Error message payload for details of failure |  -  |
| **401** | Invalid access token. May be expired or invalid |  -  |
| **403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
| **404** | The resource was not found or is no longer available  |  -  |


# WebhooksApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebhook**](WebhooksApi.md#createWebhook) | **POST** /self/webhooks | Create a new webhook subscription |
| [**destroyWebhook**](WebhooksApi.md#destroyWebhook) | **DELETE** /self/webhooks/{id} | Remove a web hook |
| [**listWebhooks**](WebhooksApi.md#listWebhooks) | **GET** /self/webhooks | List web hooks |
| [**renewWebhook**](WebhooksApi.md#renewWebhook) | **PUT** /self/webhooks/{id}/renew | Renews a web hook |
| [**viewWebhook**](WebhooksApi.md#viewWebhook) | **GET** /self/webhooks/{id} | Get web hook details |


<a id="createWebhook"></a>
# **createWebhook**
> Webhook createWebhook(webhookCreate)

Create a new webhook subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    WebhookCreate webhookCreate = new WebhookCreate(); // WebhookCreate | Webhook create parameters
    try {
      Webhook result = apiInstance.createWebhook(webhookCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createWebhook");
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
| **webhookCreate** | [**WebhookCreate**](WebhookCreate.md)| Webhook create parameters | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="destroyWebhook"></a>
# **destroyWebhook**
> destroyWebhook(id)

Remove a web hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the webhook
    try {
      apiInstance.destroyWebhook(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#destroyWebhook");
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
| **id** | **String**| Unique identifier of the webhook | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="listWebhooks"></a>
# **listWebhooks**
> List&lt;Webhook&gt; listWebhooks()

List web hooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      List<Webhook> result = apiInstance.listWebhooks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#listWebhooks");
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

[**List&lt;Webhook&gt;**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="renewWebhook"></a>
# **renewWebhook**
> Webhook renewWebhook(id)

Renews a web hook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | Webhook ID
    try {
      Webhook result = apiInstance.renewWebhook(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#renewWebhook");
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
| **id** | **String**| Webhook ID | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

<a id="viewWebhook"></a>
# **viewWebhook**
> Webhook viewWebhook(id)

Get web hook details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of the webhook
    try {
      Webhook result = apiInstance.viewWebhook(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#viewWebhook");
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
| **id** | **String**| Unique identifier of the webhook | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |


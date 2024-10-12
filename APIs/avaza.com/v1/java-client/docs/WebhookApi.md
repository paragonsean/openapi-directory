# WebhookApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webhookDelete**](WebhookApi.md#webhookDelete) | **DELETE** /api/Webhook/{id} | Delete Webhook Subscription by ID |
| [**webhookDeleteByUrl**](WebhookApi.md#webhookDeleteByUrl) | **DELETE** /api/Webhook | Delete webhook subscription by URL |
| [**webhookGet**](WebhookApi.md#webhookGet) | **GET** /api/Webhook | Get list of Webhook Subscriptions |
| [**webhookGetByID**](WebhookApi.md#webhookGetByID) | **GET** /api/Webhook/{id} | Get Webhook Subscription by SubscriptionID |
| [**webhookPost**](WebhookApi.md#webhookPost) | **POST** /api/Webhook | Subscribe to Webhook. On success, returns ID of webhook subscription. |


<a id="webhookDelete"></a>
# **webhookDelete**
> Object webhookDelete(id)

Delete Webhook Subscription by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    Integer id = 56; // Integer | Subscription id to be deleted
    try {
      Object result = apiInstance.webhookDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookDelete");
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
| **id** | **Integer**| Subscription id to be deleted | |

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription deleted ok |  -  |
| **401** | Unauthorized |  -  |

<a id="webhookDeleteByUrl"></a>
# **webhookDeleteByUrl**
> Object webhookDeleteByUrl(targetUrl)

Delete webhook subscription by URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String targetUrl = "targetUrl_example"; // String | Target URL that should be used to delete subscriptions
    try {
      Object result = apiInstance.webhookDeleteByUrl(targetUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookDeleteByUrl");
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
| **targetUrl** | **String**| Target URL that should be used to delete subscriptions | |

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Subscription Deleted OK |  -  |
| **401** | Unauthorized |  -  |

<a id="webhookGet"></a>
# **webhookGet**
> WebhookList webhookGet()

Get list of Webhook Subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    try {
      WebhookList result = apiInstance.webhookGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookGet");
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

[**WebhookList**](WebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webhookGetByID"></a>
# **webhookGetByID**
> WebhookList webhookGetByID(id)

Get Webhook Subscription by SubscriptionID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      WebhookList result = apiInstance.webhookGetByID(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookGetByID");
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
| **id** | **Integer**|  | |

### Return type

[**WebhookList**](WebhookList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webhookPost"></a>
# **webhookPost**
> SubscribeResult webhookPost(model)

Subscribe to Webhook. On success, returns ID of webhook subscription.

When you receive a webhook, you should respond with Http 200 OK Status Code, otherwise we will retry. To create a webhook, you need both the webhook_notifications scope, as well as the scope for the required entity being monitored.  Event values are: \&quot;company_created\&quot;, \&quot;company_deleted\&quot;, \&quot;company_updated\&quot;, \&quot;contact_created\&quot;, \&quot;contact_deleted\&quot;, \&quot;contact_updated\&quot;, \&quot;invoice_created\&quot;, \&quot;invoice_sent\&quot;,\&quot;invoice_updated\&quot;,\&quot;invoice_deleted\&quot;, \&quot;project_created\&quot;, \&quot;project_deleted\&quot;, \&quot;project_updated\&quot;, \&quot;task_created\&quot;, \&quot;task_updated\&quot;,\&quot;task_deleted\&quot;, \&quot;timesheet_created\&quot;, \&quot;timesheet_deleted\&quot;, \&quot;timesheet_updated, \&quot;bill_created\&quot;, \&quot;bill_updated\&quot;.  You can subscribe to any webhook, but you will only receive notifications for data appropriate to the roles of your user account. There is an optional  Secret parameter (string 255 char max). This allows for webhook authentication. If provided, the Secret will be BASE 64 encoded and passed with notications as a basic authentication http header. i.e. Authorization Basic [BASE64 of Secret]\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    CreateSubscription model = new CreateSubscription(); // CreateSubscription | 
    try {
      SubscribeResult result = apiInstance.webhookPost(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookPost");
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
| **model** | [**CreateSubscription**](CreateSubscription.md)|  | |

### Return type

[**SubscribeResult**](SubscribeResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Subscription created |  -  |
| **401** | Unauthorized |  -  |
| **409** | Duplicate subscription already exists |  -  |


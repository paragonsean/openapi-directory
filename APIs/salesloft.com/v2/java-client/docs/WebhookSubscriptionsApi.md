# WebhookSubscriptionsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2WebhookSubscriptionsGet**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsGet) | **GET** /v2/webhook_subscriptions | List webhook subscriptions |
| [**v2WebhookSubscriptionsIdDelete**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsIdDelete) | **DELETE** /v2/webhook_subscriptions/{id} | Delete a webhook subscription |
| [**v2WebhookSubscriptionsIdGet**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsIdGet) | **GET** /v2/webhook_subscriptions/{id} | Fetch a webhook subscription |
| [**v2WebhookSubscriptionsIdPut**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsIdPut) | **PUT** /v2/webhook_subscriptions/{id} | Update a webhook subscription |
| [**v2WebhookSubscriptionsPost**](WebhookSubscriptionsApi.md#v2WebhookSubscriptionsPost) | **POST** /v2/webhook_subscriptions | Create a webhook subscription |


<a id="v2WebhookSubscriptionsGet"></a>
# **v2WebhookSubscriptionsGet**
> List&lt;Subscription&gt; v2WebhookSubscriptionsGet(enabled)

List webhook subscriptions

Fetches all of the customer&#39;s webhook subscriptions for your application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    WebhookSubscriptionsApi apiInstance = new WebhookSubscriptionsApi(defaultClient);
    Boolean enabled = true; // Boolean | Filters webhook subscriptions by whether is enabled or not.
    try {
      List<Subscription> result = apiInstance.v2WebhookSubscriptionsGet(enabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookSubscriptionsApi#v2WebhookSubscriptionsGet");
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
| **enabled** | **Boolean**| Filters webhook subscriptions by whether is enabled or not. | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2WebhookSubscriptionsIdDelete"></a>
# **v2WebhookSubscriptionsIdDelete**
> v2WebhookSubscriptionsIdDelete(id)

Delete a webhook subscription

Deletes a webhook subscription. This operation is not reversible without contacting support. This operation can be called multiple times successfully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    WebhookSubscriptionsApi apiInstance = new WebhookSubscriptionsApi(defaultClient);
    Integer id = 56; // Integer | The id of the Webhook Subscription to delete
    try {
      apiInstance.v2WebhookSubscriptionsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookSubscriptionsApi#v2WebhookSubscriptionsIdDelete");
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
| **id** | **Integer**| The id of the Webhook Subscription to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | This webhook subscription has been deleted successfully |  -  |

<a id="v2WebhookSubscriptionsIdGet"></a>
# **v2WebhookSubscriptionsIdGet**
> Subscription v2WebhookSubscriptionsIdGet(id)

Fetch a webhook subscription

Fetches a webhook subscription, by ID only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    WebhookSubscriptionsApi apiInstance = new WebhookSubscriptionsApi(defaultClient);
    Integer id = 56; // Integer | The id for the Webhook Subscription
    try {
      Subscription result = apiInstance.v2WebhookSubscriptionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookSubscriptionsApi#v2WebhookSubscriptionsIdGet");
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
| **id** | **Integer**| The id for the Webhook Subscription | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2WebhookSubscriptionsIdPut"></a>
# **v2WebhookSubscriptionsIdPut**
> Subscription v2WebhookSubscriptionsIdPut(id, enabled)

Update a webhook subscription

Updates a webhook subscription. Request must be made with a valid Oauth token or API key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    WebhookSubscriptionsApi apiInstance = new WebhookSubscriptionsApi(defaultClient);
    Integer id = 56; // Integer | The Webhook Suscription id to update
    Boolean enabled = true; // Boolean | Enable or disable the webhook subscription
    try {
      Subscription result = apiInstance.v2WebhookSubscriptionsIdPut(id, enabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookSubscriptionsApi#v2WebhookSubscriptionsIdPut");
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
| **id** | **Integer**| The Webhook Suscription id to update | |
| **enabled** | **Boolean**| Enable or disable the webhook subscription | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2WebhookSubscriptionsPost"></a>
# **v2WebhookSubscriptionsPost**
> Subscription v2WebhookSubscriptionsPost(callbackToken, callbackUrl, eventType)

Create a webhook subscription

Creates a webhook subscription. Visit the &lt;a href&#x3D;\&quot;/webhooks.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;webhooks page&lt;/a&gt; for additional details and a list of available webhooks. Request must be made with a valid Oauth token or API key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    WebhookSubscriptionsApi apiInstance = new WebhookSubscriptionsApi(defaultClient);
    String callbackToken = "callbackToken_example"; // String | Any string to be used as a shared secret when subscription events are published. SalesLoft will send the value of this callback_token in the payload of each event so the receiver may verify it matches the original value. This ensures webhook events are being delivered by SalesLoft.
    String callbackUrl = "callbackUrl_example"; // String | URL for your callback handler
    String eventType = "eventType_example"; // String | Type of event the subscription is for. Visit the \\\"Event Types\\\" section of the webhooks page to find a list of supported event types.
    try {
      Subscription result = apiInstance.v2WebhookSubscriptionsPost(callbackToken, callbackUrl, eventType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookSubscriptionsApi#v2WebhookSubscriptionsPost");
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
| **callbackToken** | **String**| Any string to be used as a shared secret when subscription events are published. SalesLoft will send the value of this callback_token in the payload of each event so the receiver may verify it matches the original value. This ensures webhook events are being delivered by SalesLoft. | |
| **callbackUrl** | **String**| URL for your callback handler | |
| **eventType** | **String**| Type of event the subscription is for. Visit the \\\&quot;Event Types\\\&quot; section of the webhooks page to find a list of supported event types. | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


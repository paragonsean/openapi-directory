# WebhooksApi

All URIs are relative to *https://api.up.com.au/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webhooksGet**](WebhooksApi.md#webhooksGet) | **GET** /webhooks | List webhooks |
| [**webhooksIdDelete**](WebhooksApi.md#webhooksIdDelete) | **DELETE** /webhooks/{id} | Delete webhook |
| [**webhooksIdGet**](WebhooksApi.md#webhooksIdGet) | **GET** /webhooks/{id} | Retrieve webhook |
| [**webhooksPost**](WebhooksApi.md#webhooksPost) | **POST** /webhooks | Create webhook |
| [**webhooksWebhookIdLogsGet**](WebhooksApi.md#webhooksWebhookIdLogsGet) | **GET** /webhooks/{webhookId}/logs | List webhook logs |
| [**webhooksWebhookIdPingPost**](WebhooksApi.md#webhooksWebhookIdPingPost) | **POST** /webhooks/{webhookId}/ping | Ping webhook |


<a id="webhooksGet"></a>
# **webhooksGet**
> ListWebhooksResponse webhooksGet(pageSize)

List webhooks

Retrieve a list of configured webhooks. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered oldest first to newest last. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Integer pageSize = 30; // Integer | The number of records to return in each page. 
    try {
      ListWebhooksResponse result = apiInstance.webhooksGet(pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksGet");
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
| **pageSize** | **Integer**| The number of records to return in each page.  | [optional] |

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="webhooksIdDelete"></a>
# **webhooksIdDelete**
> webhooksIdDelete(id)

Delete webhook

Delete a specific webhook by providing its unique identifier. Once deleted, webhook events will no longer be sent to the configured URL. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "a940825b-80b6-4798-b378-c6284259b4c5"; // String | The unique identifier for the webhook. 
    try {
      apiInstance.webhooksIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksIdDelete");
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
| **id** | **String**| The unique identifier for the webhook.  | |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |

<a id="webhooksIdGet"></a>
# **webhooksIdGet**
> GetWebhookResponse webhooksIdGet(id)

Retrieve webhook

Retrieve a specific webhook by providing its unique identifier. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "c8283a72-24b0-4fd8-9b13-fccccab371e5"; // String | The unique identifier for the webhook. 
    try {
      GetWebhookResponse result = apiInstance.webhooksIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksIdGet");
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
| **id** | **String**| The unique identifier for the webhook.  | |

### Return type

[**GetWebhookResponse**](GetWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="webhooksPost"></a>
# **webhooksPost**
> CreateWebhookResponse webhooksPost(createWebhookRequest)

Create webhook

Create a new webhook with a given URL. The URL will receive webhook events as JSON-encoded &#x60;POST&#x60; requests. The URL must respond with a HTTP &#x60;200&#x60; status on success.  There is currently a limit of 10 webhooks at any given time. Once this limit is reached, existing webhooks will need to be deleted before new webhooks can be created.  Event delivery is retried with exponential backoff if the URL is unreachable or it does not respond with a &#x60;200&#x60; status. The response includes a &#x60;secretKey&#x60; attribute, which is used to sign requests sent to the webhook URL. It will not be returned from any other endpoints within the Up API. If the &#x60;secretKey&#x60; is lost, simply create a new webhook with the same URL, capture its &#x60;secretKey&#x60; and then delete the original webhook. See [Handling webhook events](#callback_post_webhookURL) for details on how to process webhook events.  It is probably a good idea to test the webhook by [sending it a &#x60;PING&#x60; event](#post_webhooks_webhookId_ping) after creating it. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    CreateWebhookRequest createWebhookRequest = new CreateWebhookRequest(); // CreateWebhookRequest | 
    try {
      CreateWebhookResponse result = apiInstance.webhooksPost(createWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksPost");
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

[**CreateWebhookResponse**](CreateWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="webhooksWebhookIdLogsGet"></a>
# **webhooksWebhookIdLogsGet**
> ListWebhookDeliveryLogsResponse webhooksWebhookIdLogsGet(webhookId, pageSize)

List webhook logs

Retrieve a list of delivery logs for a webhook by providing its unique identifier. This is useful for analysis and debugging purposes. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered newest first to oldest last. Logs may be automatically purged after a period of time. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String webhookId = "7104f5df-4993-495f-9d29-2b4d062c03a9"; // String | The unique identifier for the webhook. 
    Integer pageSize = 30; // Integer | The number of records to return in each page. 
    try {
      ListWebhookDeliveryLogsResponse result = apiInstance.webhooksWebhookIdLogsGet(webhookId, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksWebhookIdLogsGet");
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
| **webhookId** | **String**| The unique identifier for the webhook.  | |
| **pageSize** | **Integer**| The number of records to return in each page.  | [optional] |

### Return type

[**ListWebhookDeliveryLogsResponse**](ListWebhookDeliveryLogsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="webhooksWebhookIdPingPost"></a>
# **webhooksWebhookIdPingPost**
> WebhookEventCallback webhooksWebhookIdPingPost(webhookId)

Ping webhook

Send a &#x60;PING&#x60; event to a webhook by providing its unique identifier. This is useful for testing and debugging purposes. The event is delivered asynchronously and its data is returned in the response to this request. 

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
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String webhookId = "830e127d-fb89-4400-92bb-f3f48289dcba"; // String | The unique identifier for the webhook. 
    try {
      WebhookEventCallback result = apiInstance.webhooksWebhookIdPingPost(webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksWebhookIdPingPost");
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
| **webhookId** | **String**| The unique identifier for the webhook.  | |

### Return type

[**WebhookEventCallback**](WebhookEventCallback.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |


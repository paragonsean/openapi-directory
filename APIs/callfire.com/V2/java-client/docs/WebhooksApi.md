# WebhooksApi

All URIs are relative to *https://api.callfire.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebhook**](WebhooksApi.md#createWebhook) | **POST** /webhooks | Create a webhook |
| [**deleteWebhook**](WebhooksApi.md#deleteWebhook) | **DELETE** /webhooks/{id} | Delete a webhook |
| [**findWebhookResources**](WebhooksApi.md#findWebhookResources) | **GET** /webhooks/resources | Find webhook resources |
| [**findWebhooks**](WebhooksApi.md#findWebhooks) | **GET** /webhooks | Find webhooks |
| [**getWebhook**](WebhooksApi.md#getWebhook) | **GET** /webhooks/{id} | Find a specific webhook |
| [**getWebhookResource**](WebhooksApi.md#getWebhookResource) | **GET** /webhooks/resources/{resource} | Find specific webhook resource |
| [**updateWebhook**](WebhooksApi.md#updateWebhook) | **PUT** /webhooks/{id} | Update a webhook |


<a id="createWebhook"></a>
# **createWebhook**
> ResourceId createWebhook(webhook)

Create a webhook

Create a Webhook for notification in the CallFire system. Use the webhooks API to receive notifications of important CallFire events. Select the resource to listen to, and then choose the resource events to receive notifications on. When an event triggers, a POST will be made to the callback URL with a payload of notification information. Available resources and their events include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;]. Webhooks support secret token which is used as signing key to HmacSHA1 hash of json payload which is returned in &#39;X-CallFire-Signature&#39; header. This header can be used to verify callback POST is coming from CallFire. See [security guide](https://developers.callfire.com/security-guide.html)

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Webhook webhook = new Webhook(); // Webhook | A webhook object
    try {
      ResourceId result = apiInstance.createWebhook(webhook);
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
| **webhook** | [**Webhook**](Webhook.md)| A webhook object | [optional] |

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="deleteWebhook"></a>
# **deleteWebhook**
> deleteWebhook(id)

Delete a webhook

Deletes a webhook instance. Will be removed permanently

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Long id = 56L; // Long | An Id of a webhook
    try {
      apiInstance.deleteWebhook(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#deleteWebhook");
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
| **id** | **Long**| An Id of a webhook | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findWebhookResources"></a>
# **findWebhookResources**
> ItemListWebhookResource findWebhookResources(fields)

Find webhook resources

Searches for webhook resources. Available resources include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;]

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      ItemListWebhookResource result = apiInstance.findWebhookResources(fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#findWebhookResources");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**ItemListWebhookResource**](ItemListWebhookResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="findWebhooks"></a>
# **findWebhooks**
> WebhookPage findWebhooks(fields, limit, offset, name, resource, event, paramCallback, enabled)

Find webhooks

Searches all webhooks available for a current user. Searches by name, resource, event, callback URL, or whether they are enabled. Returns a paged list of Webhooks

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    Integer limit = 100; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String name = "name_example"; // String | A name of a webhook
    String resource = "resource_example"; // String | A name of a resource, available values: 'CccCampaign', 'CallBroadcast', 'TextBroadcast',  'OutboundCall', 'OutboundText', 'InboundCall', 'InboundText', 'ContactList'
    String event = "event_example"; // String | A name of event, available values: 'started', 'stopped', 'finished'
    String paramCallback = "paramCallback_example"; // String | A callback URL
    Boolean enabled = true; // Boolean | Specifies whether webhook is enabled
    try {
      WebhookPage result = apiInstance.findWebhooks(fields, limit, offset, name, resource, event, paramCallback, enabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#findWebhooks");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **name** | **String**| A name of a webhook | [optional] |
| **resource** | **String**| A name of a resource, available values: &#39;CccCampaign&#39;, &#39;CallBroadcast&#39;, &#39;TextBroadcast&#39;,  &#39;OutboundCall&#39;, &#39;OutboundText&#39;, &#39;InboundCall&#39;, &#39;InboundText&#39;, &#39;ContactList&#39; | [optional] |
| **event** | **String**| A name of event, available values: &#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39; | [optional] |
| **paramCallback** | **String**| A callback URL | [optional] |
| **enabled** | **Boolean**| Specifies whether webhook is enabled | [optional] |

### Return type

[**WebhookPage**](WebhookPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getWebhook"></a>
# **getWebhook**
> Webhook getWebhook(id, fields)

Find a specific webhook

Returns a single Webhook instance for a given webhook id

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Long id = 56L; // Long | An id of a webhook
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      Webhook result = apiInstance.getWebhook(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getWebhook");
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
| **id** | **Long**| An id of a webhook | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getWebhookResource"></a>
# **getWebhookResource**
> WebhookResource getWebhookResource(resource, fields)

Find specific webhook resource

Returns information about supported events for a given webhook resource

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String resource = "resource_example"; // String | A name of a webhook resource. Available resources include 'CccCampaign': ['started', 'stopped', 'finished'], 'CallBroadcast': ['started', 'stopped', 'finished'], 'TextBroadcast': ['started', 'stopped', 'finished'], 'OutboundCall': ['finished'], 'InboundCall': ['finished'], 'OutboundText': ['finished'], 'InboundText': ['finished'], 'ContactList': ['validationFinished', 'validationFailed'], 'MonthlyRenewal': ['failed', 'finished'], 'LowBalance': ['failed', 'finished']
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      WebhookResource result = apiInstance.getWebhookResource(resource, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getWebhookResource");
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
| **resource** | **String**| A name of a webhook resource. Available resources include &#39;CccCampaign&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;CallBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;TextBroadcast&#39;: [&#39;started&#39;, &#39;stopped&#39;, &#39;finished&#39;], &#39;OutboundCall&#39;: [&#39;finished&#39;], &#39;InboundCall&#39;: [&#39;finished&#39;], &#39;OutboundText&#39;: [&#39;finished&#39;], &#39;InboundText&#39;: [&#39;finished&#39;], &#39;ContactList&#39;: [&#39;validationFinished&#39;, &#39;validationFailed&#39;], &#39;MonthlyRenewal&#39;: [&#39;failed&#39;, &#39;finished&#39;], &#39;LowBalance&#39;: [&#39;failed&#39;, &#39;finished&#39;] | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**WebhookResource**](WebhookResource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateWebhook"></a>
# **updateWebhook**
> updateWebhook(id, webhook)

Update a webhook

Updates the information in existing webhook

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Long id = 56L; // Long | An id of a webhook
    Webhook webhook = new Webhook(); // Webhook | A webhook object
    try {
      apiInstance.updateWebhook(id, webhook);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#updateWebhook");
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
| **id** | **Long**| An id of a webhook | |
| **webhook** | [**Webhook**](Webhook.md)| A webhook object | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |


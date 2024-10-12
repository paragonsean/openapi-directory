# WebhooksApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWebhookById**](WebhooksApi.md#getWebhookById) | **GET** /webhooks/{webhookId} | Get Webhook by Id |
| [**webhooksGet**](WebhooksApi.md#webhooksGet) | **GET** /webhooks | Get Webhooks |
| [**webhooksPost**](WebhooksApi.md#webhooksPost) | **POST** /webhooks | Create Webhook |
| [**webhooksWebhookIdDelete**](WebhooksApi.md#webhooksWebhookIdDelete) | **DELETE** /webhooks/{webhookId} | Delete Webhook by Id |
| [**webhooksWebhookIdDisablePost**](WebhooksApi.md#webhooksWebhookIdDisablePost) | **POST** /webhooks/{webhookId}/disable | Ability to enable a webHook. |
| [**webhooksWebhookIdEnablePost**](WebhooksApi.md#webhooksWebhookIdEnablePost) | **POST** /webhooks/{webhookId}/enable | Ability to disable a webHook. |
| [**webhooksWebhookIdPut**](WebhooksApi.md#webhooksWebhookIdPut) | **PUT** /webhooks/{webhookId} | Update Webhook by Id |


<a id="getWebhookById"></a>
# **getWebhookById**
> String getWebhookById(webhookId)

Get Webhook by Id

Returns information of the webhook specified by the passed id.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String webhookId = "webhookId_example"; // String | Id of the outbound webhook to be retrieved.
    try {
      String result = apiInstance.getWebhookById(webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getWebhookById");
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
| **webhookId** | **String**| Id of the outbound webhook to be retrieved. | |

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful and response body contains information about the requested webhook. |  -  |
| **400** | The passed webhook id was either empty or null. |  -  |
| **404** | The webhook was not found. |  -  |
| **500** | Internal has occured. The response body may contain more information. |  -  |

<a id="webhooksGet"></a>
# **webhooksGet**
> List&lt;WebhookInfo&gt; webhooksGet(teamId)

Get Webhooks

Returns a collection of defined outbound webhooks in the system.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String teamId = "teamId_example"; // String | 
    try {
      List<WebhookInfo> result = apiInstance.webhooksGet(teamId);
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
| **teamId** | **String**|  | [optional] |

### Return type

[**List&lt;WebhookInfo&gt;**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful and response body contains information about all outbound webhooks in the subscription. |  -  |
| **404** | The subscription does not have any outbound webhooks. |  -  |
| **500** | Internal has occured. The response body may contain more information. |  -  |

<a id="webhooksPost"></a>
# **webhooksPost**
> String webhooksPost(webhookBaseInfo)

Create Webhook

Creates a new outbound webhook that will be notified when certain events occur.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    WebhookBaseInfo webhookBaseInfo = new WebhookBaseInfo(); // WebhookBaseInfo | Json object that contains the external URL of the webhook.
    try {
      String result = apiInstance.webhooksPost(webhookBaseInfo);
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
| **webhookBaseInfo** | [**WebhookBaseInfo**](WebhookBaseInfo.md)| Json object that contains the external URL of the webhook. | [optional] |

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Action was successful and response contains the id of the newly created webhook. |  -  |
| **400** | Either the webhook object or a necessary property was invalid or empty. |  -  |
| **500** | Internal has occured. The response body may contain more information. |  -  |

<a id="webhooksWebhookIdDelete"></a>
# **webhooksWebhookIdDelete**
> webhooksWebhookIdDelete(webhookId)

Delete Webhook by Id

Deletes the specified webhook so that it will no longer be notified.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String webhookId = "webhookId_example"; // String | Id of the outbound webhook that will be deleted.
    try {
      apiInstance.webhooksWebhookIdDelete(webhookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksWebhookIdDelete");
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
| **webhookId** | **String**| Id of the outbound webhook that will be deleted. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook was successfully deleted. |  -  |
| **400** | The passed webhook id was invalid or empty. |  -  |
| **404** | Webhook with specified id was not found. |  -  |
| **500** | Internal has occured. The response body may contain more information. |  -  |

<a id="webhooksWebhookIdDisablePost"></a>
# **webhooksWebhookIdDisablePost**
> WebhookInfo webhooksWebhookIdDisablePost(webhookId)

Ability to enable a webHook.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String webhookId = "webhookId_example"; // String | Webhook ID for webhook which should be disabled.
    try {
      WebhookInfo result = apiInstance.webhooksWebhookIdDisablePost(webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksWebhookIdDisablePost");
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
| **webhookId** | **String**| Webhook ID for webhook which should be disabled. | |

### Return type

[**WebhookInfo**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disable was successful and response body contains the webhook details. |  -  |
| **400** | A passed parameter was either empty or null. |  -  |
| **404** | Webhook with specified id was not found. |  -  |
| **500** | Internal has occured. The response body may contain more information. |  -  |

<a id="webhooksWebhookIdEnablePost"></a>
# **webhooksWebhookIdEnablePost**
> WebhookInfo webhooksWebhookIdEnablePost(webhookId)

Ability to disable a webHook.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String webhookId = "webhookId_example"; // String | Webhook ID for webhook which should be enabled.
    try {
      WebhookInfo result = apiInstance.webhooksWebhookIdEnablePost(webhookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksWebhookIdEnablePost");
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
| **webhookId** | **String**| Webhook ID for webhook which should be enabled. | |

### Return type

[**WebhookInfo**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="webhooksWebhookIdPut"></a>
# **webhooksWebhookIdPut**
> WebhookInfo webhooksWebhookIdPut(webhookId, webhookBaseInfo)

Update Webhook by Id

Updates the specified webhook.

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
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String webhookId = "webhookId_example"; // String | Id of the outbound webhook to be updated.
    WebhookBaseInfo webhookBaseInfo = new WebhookBaseInfo(); // WebhookBaseInfo | Json object containing the updated URL of the webhook.
    try {
      WebhookInfo result = apiInstance.webhooksWebhookIdPut(webhookId, webhookBaseInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksWebhookIdPut");
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
| **webhookId** | **String**| Id of the outbound webhook to be updated. | |
| **webhookBaseInfo** | [**WebhookBaseInfo**](WebhookBaseInfo.md)| Json object containing the updated URL of the webhook. | [optional] |

### Return type

[**WebhookInfo**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update was successful and response body contains the updated webhook details. |  -  |
| **400** | A passed parameter was either empty or null. |  -  |
| **404** | Webhook with specified id was not found. |  -  |
| **500** | Internal has occured. The response body may contain more information. |  -  |


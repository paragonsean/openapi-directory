# IncomingWebhooksApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIncomingWebhook**](IncomingWebhooksApi.md#createIncomingWebhook) | **POST** /webhooks/incoming/create/{conversationId} | Create a new webhook for existing conversation. |
| [**deleteIncomingWebhook**](IncomingWebhooksApi.md#deleteIncomingWebhook) | **DELETE** /webhooks/incoming/{webhookId} | Delete an existing webhook |
| [**getIncomingWebhookByUser**](IncomingWebhooksApi.md#getIncomingWebhookByUser) | **GET** /webhooks/incoming/user/{userId} | Get all webhooks of a special user. |
| [**postWebhookAsSlackMessage**](IncomingWebhooksApi.md#postWebhookAsSlackMessage) | **POST** /webhooks/incoming/{webhookId} | Post text item for conversation via webhook. |


<a id="createIncomingWebhook"></a>
# **createIncomingWebhook**
> IncomingWebhook createIncomingWebhook(conversationId, name, userId, description)

Create a new webhook for existing conversation.

Create a new webhook. Conversation must exist and creater has to be participant. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    IncomingWebhooksApi apiInstance = new IncomingWebhooksApi(defaultClient);
    String conversationId = "conversationId_example"; // String | The id of the conversation.
    String name = "name_example"; // String | The name of the webhook
    String userId = "userId_example"; // String | The id of the user of the webhook
    String description = "description_example"; // String | A short description of the webhook
    try {
      IncomingWebhook result = apiInstance.createIncomingWebhook(conversationId, name, userId, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomingWebhooksApi#createIncomingWebhook");
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
| **conversationId** | **String**| The id of the conversation. | |
| **name** | **String**| The name of the webhook | [optional] |
| **userId** | **String**| The id of the user of the webhook | [optional] |
| **description** | **String**| A short description of the webhook | [optional] |

### Return type

[**IncomingWebhook**](IncomingWebhook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created webhook object as JSON string. |  -  |
| **400** | Could not create webhook. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="deleteIncomingWebhook"></a>
# **deleteIncomingWebhook**
> deleteIncomingWebhook(webhookId)

Delete an existing webhook

Delete a new webhook. Webhook must exist OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    IncomingWebhooksApi apiInstance = new IncomingWebhooksApi(defaultClient);
    String webhookId = "webhookId_example"; // String | The id of the webhook
    try {
      apiInstance.deleteIncomingWebhook(webhookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomingWebhooksApi#deleteIncomingWebhook");
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
| **webhookId** | **String**| The id of the webhook | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webhook was deleted |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | Could not find webhook |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getIncomingWebhookByUser"></a>
# **getIncomingWebhookByUser**
> List&lt;IncomingWebhook&gt; getIncomingWebhookByUser(userId, pagesize, searchpointer)

Get all webhooks of a special user.

Get all webhooks of a special user. OauthScopes: READ_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    IncomingWebhooksApi apiInstance = new IncomingWebhooksApi(defaultClient);
    String userId = "userId_example"; // String | The id of the user.
    BigDecimal pagesize = new BigDecimal("25"); // BigDecimal | Max number of hooks per request. Default is 25
    String searchpointer = "searchpointer_example"; // String | Start of search if consequtive call.
    try {
      List<IncomingWebhook> result = apiInstance.getIncomingWebhookByUser(userId, pagesize, searchpointer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomingWebhooksApi#getIncomingWebhookByUser");
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
| **userId** | **String**| The id of the user. | |
| **pagesize** | **BigDecimal**| Max number of hooks per request. Default is 25 | [optional] [default to 25] |
| **searchpointer** | **String**| Start of search if consequtive call. | [optional] |

### Return type

[**List&lt;IncomingWebhook&gt;**](IncomingWebhook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result successful |  -  |
| **400** | The request cannot be fulfilled due to bad syntax |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="postWebhookAsSlackMessage"></a>
# **postWebhookAsSlackMessage**
> postWebhookAsSlackMessage(webhookId, fileURL, filename, markdown, subject, text)

Post text item for conversation via webhook.

Post text items to conversations via slack apps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IncomingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");

    IncomingWebhooksApi apiInstance = new IncomingWebhooksApi(defaultClient);
    String webhookId = "webhookId_example"; // String | The id of the webhook.
    String fileURL = "fileURL_example"; // String | missing documentation
    String filename = "filename_example"; // String | missing documentation
    Boolean markdown = true; // Boolean | missing documentation
    String subject = "subject_example"; // String | missing documentation
    String text = "text_example"; // String | The text which will occur in the conversation. May contain formats like *bold* or _italic_
    try {
      apiInstance.postWebhookAsSlackMessage(webhookId, fileURL, filename, markdown, subject, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling IncomingWebhooksApi#postWebhookAsSlackMessage");
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
| **webhookId** | **String**| The id of the webhook. | |
| **fileURL** | **String**| missing documentation | [optional] |
| **filename** | **String**| missing documentation | [optional] |
| **markdown** | **Boolean**| missing documentation | [optional] |
| **subject** | **String**| missing documentation | [optional] |
| **text** | **String**| The text which will occur in the conversation. May contain formats like *bold* or _italic_ | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Message was posted to conversation |  -  |
| **400** | The request cannot be fulfilled due to bad syntax |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |


# MessagesApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMessageById**](MessagesApi.md#deleteMessageById) | **DELETE** /messages/{messageId} | delete a message |
| [**getMessageById**](MessagesApi.md#getMessageById) | **GET** /messages/{messageId} | fetch a specific message |
| [**getMessages**](MessagesApi.md#getMessages) | **GET** /messages | fetch all sent/received messages |
| [**sendMessages**](MessagesApi.md#sendMessages) | **POST** /messages | send messages |
| [**updateMessageById**](MessagesApi.md#updateMessageById) | **PUT** /messages/{messageId} | update a message |
| [**updateMessageTags**](MessagesApi.md#updateMessageTags) | **PATCH** /messages/{messageId} | update message tags |


<a id="deleteMessageById"></a>
# **deleteMessageById**
> deleteMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, telstraApiVersion)

delete a message

Use this endpoint to delete a message that&#39;s been scheduled for sending, but hasn&#39;t yet sent. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    UUID messageId = UUID.randomUUID(); // UUID | When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints. 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      apiInstance.deleteMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, telstraApiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#deleteMessageById");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **messageId** | **UUID**| When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints.  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | A 204 response means your message has been deleted.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | DELETE_INVALID_MSG_SENT | The message can&#39;t be deleted because it&#39;s already been sent. | | ID_NOT_ASSIGNED | Ensure the messageId corresponds to a message that has been sent from/to this account. | | TIMEFRAME_ERR | Ensure the messageId corresponds to a message that is not more than 30 days old. | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is DELETE. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="getMessageById"></a>
# **getMessageById**
> MessageGet getMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, telstraApiVersion)

fetch a specific message

Use the **messageId** to fetch a message that&#39;s been sent from/to your account within the last 30 days. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    UUID messageId = UUID.randomUUID(); // UUID | When you sent the original message, this is the UUID that was returned in the response. Use this ID to fetch, update or delete a message with the appropriate endpoints.   Incoming messages are also assigned a messageId. Use this ID with GET/ messages/{messageId} to fetch the message later. 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      MessageGet result = apiInstance.getMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#getMessageById");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **messageId** | **UUID**| When you sent the original message, this is the UUID that was returned in the response. Use this ID to fetch, update or delete a message with the appropriate endpoints.   Incoming messages are also assigned a messageId. Use this ID with GET/ messages/{messageId} to fetch the message later.  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**MessageGet**](MessageGet.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 response means the call has been successful.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | ID_NOT_ASSIGNED | Ensure the messageId corresponds to a message that has been sent from/to this account. | | FIELD_INVALID | Check the field and the field formatting are correct. | | TIMEFRAME_ERR | Ensure the messageId corresponds to a message that is not more than 30 days old. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **406** | Media type invalid  | code | suggested_action | | :--- | :--- | | MEDIA_TYPE_INVALID | Check the media type in the Accept header. It should be application/json. |  |  * Content-Language -  <br>  |
| **415** | Payload media type error  | code | suggested_action | | :--- | :--- | | PAYLOAD_MEDIA_TYPE_ERR | Check the media type in the Accept header. It should be application/json. |  |  * Content-Language -  <br>  |
| **422** | Logic error  | code | suggested_action | | :--- | :--- | | LOGIC_ERR | Check the logic of the request and try again. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="getMessages"></a>
# **getMessages**
> GetMessages200Response getMessages(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion, limit, offset, direction, status, filter)

fetch all sent/received messages

Fetch messages that have been sent from/to your account in the last 30 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    String telstraApiVersion = "3.1.0"; // String | 
    Integer limit = 10; // Integer | Tell us how many results you want us to return, up to a maximum of 50. 
    Integer offset = 0; // Integer | Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on. 
    String direction = "outgoing"; // String | Filter your messages by direction: * **outgoing** – messages sent from your account. * **incoming** – messages sent to your account. 
    String status = "queued"; // String | Filter your messages by one of the statuses below:  * **queued** – messages queued for sending or still in transit. * **sent** – messages that have been sent from the server. * **delivered** – messages successful delivered to the recipient's device. Note that we will only be able to return this status if you set deliveryNotification to **true** (paid feature).  * **expired** – message that couldn't be sent within the **retryTimeout** timeframe. 
    String filter = "filter_example"; // String | Filter your messages by:  * tag - use one of the tags assigned to your message(s) * number - either the Virtual Number used to send the message, or the Recipient Number the message was sent to. 
    try {
      GetMessages200Response result = apiInstance.getMessages(contentLanguage, authorization, accept, acceptCharset, contentType, telstraApiVersion, limit, offset, direction, status, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#getMessages");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **telstraApiVersion** | **String**|  | [optional] |
| **limit** | **Integer**| Tell us how many results you want us to return, up to a maximum of 50.  | [optional] [default to 10] |
| **offset** | **Integer**| Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on.  | [optional] [default to 0] |
| **direction** | **String**| Filter your messages by direction: * **outgoing** – messages sent from your account. * **incoming** – messages sent to your account.  | [optional] [enum: outgoing, incoming] |
| **status** | **String**| Filter your messages by one of the statuses below:  * **queued** – messages queued for sending or still in transit. * **sent** – messages that have been sent from the server. * **delivered** – messages successful delivered to the recipient&#39;s device. Note that we will only be able to return this status if you set deliveryNotification to **true** (paid feature).  * **expired** – message that couldn&#39;t be sent within the **retryTimeout** timeframe.  | [optional] [enum: queued, sent, delivered, expired] |
| **filter** | **String**| Filter your messages by:  * tag - use one of the tags assigned to your message(s) * number - either the Virtual Number used to send the message, or the Recipient Number the message was sent to.  | [optional] |

### Return type

[**GetMessages200Response**](GetMessages200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 response means the call has been successful.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is GET. |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="sendMessages"></a>
# **sendMessages**
> MessageSent sendMessages(contentLanguage, authorization, accept, acceptCharset, contentType, sendMessagesRequest, telstraApiVersion)

send messages

Send an SMS/MMS to a mobile number, or to multiple mobile numbers.  Free Trial users can message to up to 10 unique recipient numbers for free. The first five recipients will be automatically added to your Free Trial Numbers list. Need more? Just use the POST /free-trial-numbers call to add another five. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    SendMessagesRequest sendMessagesRequest = new SendMessagesRequest(); // SendMessagesRequest | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      MessageSent result = apiInstance.sendMessages(contentLanguage, authorization, accept, acceptCharset, contentType, sendMessagesRequest, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#sendMessages");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **sendMessagesRequest** | [**SendMessagesRequest**](SendMessagesRequest.md)|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**MessageSent**](MessageSent.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A 201 Created response means your message has sent.  |  * Content-Language -  <br>  * Location -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | RECIPIENT_OPTOUT | Use GET/recipient-optouts/{number} to check which numbers have opted out of receiving messages from a Virtual Number. | | TAGS_ERR | Ensure you&#39;ve assigned no more than 10 tags, using up to 64 characters for each. | | SENDERNAME_ERR | Email telstradev@team.telstra.com to request approval for this senderName. | | MODERATION_ERR | Please remove any swear words or offensive language. | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_LENGTH_ERR | Check the field is within character limits. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. | | MULTIMEDIA_TOO_LARGE | Reduce the multimedia file size and try again. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). | | ACCOUNT_LIMIT_ERROR | Check the credit and limits on your account [here](https://dev.telstra.com). | | FREE_TRIAL_INTERNATIONAL_ERR | Move to a paid plan to send a message to an international destination. |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is POST. |  |  * Content-Language -  <br>  |
| **413** | Payload Too Large  | code | suggested_action | | :--- | :--- | | MULTIMEDIA_TOO_LARGE | Reduce multimedia size | | PAYLOAD_TOO_LARGE | Reduce body payload size |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="updateMessageById"></a>
# **updateMessageById**
> MessageUpdate updateMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageByIdRequest, telstraApiVersion)

update a message

Need to update a message that&#39;s scheduled for sending? You can change any of the below parameters, as long as the message hasn&#39;t been sent yet. This request body will override the original POST/ messages call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    UUID messageId = UUID.randomUUID(); // UUID | When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints. 
    UpdateMessageByIdRequest updateMessageByIdRequest = new UpdateMessageByIdRequest(); // UpdateMessageByIdRequest | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      MessageUpdate result = apiInstance.updateMessageById(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageByIdRequest, telstraApiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#updateMessageById");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **messageId** | **UUID**| When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints.  | |
| **updateMessageByIdRequest** | [**UpdateMessageByIdRequest**](UpdateMessageByIdRequest.md)|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

[**MessageUpdate**](MessageUpdate.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 response means the call has been successful.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | UPDATE_INVALID_MSG_SENT | The message can&#39;t be updated because it&#39;s already been sent. | | ID_INVALID | Ensure the messageId corresponds to an outgoing message. | | ID_NOT_ASSIGNED | Ensure the messageId corresponds to a message that has been sent from this account. | | RECIPIENT_OPTOUT | The recipient has opted out of receiving messages from this Virtual Number.  | | TAGS_ERR | Ensure you&#39;ve assigned no more than 10 tags, using up to 64 characters for each. | | SENDERNAME_ERR | Email (telstradev@team.telstra.com) to request approval for this senderName.| | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_LENGTH_ERR | Check the field is within character limits. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. | | MULTIMEDIA_TOO_LARGE | Reduce the multimedia file size and try again. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). | | FREE_TRIAL_INTERNATIONAL_ERR | Move to a paid plan to send a message to an international destination. |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is PUT. |  |  * Content-Language -  <br>  |
| **413** | Payload Too Large  | code | suggested_action | | :--- | :--- | | MULTIMEDIA_TOO_LARGE | Reduce multimedia size | | PAYLOAD_TOO_LARGE | Reduce body payload size |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |

<a id="updateMessageTags"></a>
# **updateMessageTags**
> updateMessageTags(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageTagsRequest, telstraApiVersion)

update message tags

Use the **messageId** to update the tag(s) assigned to a message. You can use this endpoint any time, even after your message has been delivered. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://products.api.telstra.com/messaging/v3");
    
    // Configure OAuth2 access token for authorization: bearer_auth
    OAuth bearer_auth = (OAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String contentLanguage = "en-au"; // String | 
    String authorization = "Bearer <access_token>"; // String | 
    String accept = "application/json"; // String | 
    String acceptCharset = "utf-8"; // String | 
    String contentType = "application/json"; // String | 
    UUID messageId = UUID.randomUUID(); // UUID | When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints. 
    UpdateMessageTagsRequest updateMessageTagsRequest = new UpdateMessageTagsRequest(); // UpdateMessageTagsRequest | 
    String telstraApiVersion = "3.1.0"; // String | 
    try {
      apiInstance.updateMessageTags(contentLanguage, authorization, accept, acceptCharset, contentType, messageId, updateMessageTagsRequest, telstraApiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#updateMessageTags");
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
| **contentLanguage** | **String**|  | |
| **authorization** | **String**|  | |
| **accept** | **String**|  | |
| **acceptCharset** | **String**|  | |
| **contentType** | **String**|  | |
| **messageId** | **UUID**| When you sent the original message, this is the UUID that was returned in the call response. Use this ID to fetch, update or delete a message with the appropriate endpoints.  | |
| **updateMessageTagsRequest** | [**UpdateMessageTagsRequest**](UpdateMessageTagsRequest.md)|  | |
| **telstraApiVersion** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | A 204 No Content response means your tag(s) have been successfully updated.  |  * Content-Language -  <br>  |
| **400** | Bad Request  | code | suggested_action | | :--- | :--- | | ID_INVALID | Ensure the messageId corresponds to an outgoing message. | | ID_NOT_ASSIGNED | Ensure the messageId corresponds to a message that has been sent from this account. | | TAGS_ERR | Ensure you&#39;ve assigned no more than 10 tags, using up to 64 characters for each. | | FIELD_INVALID | Check the field and the field formatting are correct. | | FIELD_MISSING | Ensure you&#39;ve supplied all the required fields. |  |  * Content-Language -  <br>  |
| **401** | Unauthorized  | code | suggested_action | | :--- | :--- | | TOKEN_INVALID | Check the access token. | | TOKEN_EXPIRED | Please refresh the token. |  |  * Content-Language -  <br>  |
| **402** | Payment Required  | code | suggested_action | | :--- | :--- | | ACCOUNT_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | RATE_PLAN_ERR | Contact [support](mailto:telstradev@team.telstra.com) for help with your account. | | ACCOUNT_NOT_LINKED | Check you&#39;ve registered for the Messaging API [here](https://dev.telstra.com). |  |  * Content-Language -  <br>  |
| **403** | Forbidden  | code | suggested_action | | :--- | :--- | | RESOURCE_AUTH_ERR | Check the permissions associated with your account. | | INSUFFICIENT_SCOPE | The access token you generated does not have sufficient permissions for this request. |  |  * Content-Language -  <br>  |
| **404** | Not Found  | code | suggested_action | | :--- | :--- | | RESOURCE_TEMP_ERR | Check the API status page to see if an active incident is causing a temporary issue with the resource. | | RESOURCE_NOT_FOUND | Check the endpoint is correct. |  |  * Content-Language -  <br>  |
| **405** | Method Not Allowed  | code | suggested_action | | :--- | :--- | | METHOD_INVALID | Ensure the method is PATCH. |  |  * Content-Language -  <br>  |
| **413** | Payload Too Large  | code | suggested_action | | :--- | :--- | | PAYLOAD_TOO_LARGE | Reduce body payload size |  |  * Content-Language -  <br>  |
| **429** | Too Many Requests  | code | suggested_action | | :--- | :--- | | TOO_MANY_REQUESTS | Reduce the number of concurrent calls. |  |  * Content-Language -  <br>  * Retry-After -  <br>  |
| **500** | Internal Server Error  | code | suggested_action | | :--- | :--- | | INTERNAL_TIMEOUT | Try the call again. If the issue persists, check the API [status page](https://dev.telstra.com/api/status) to see if there&#39;s an active incident. | | INTERNAL_SERVER_ERR | Check the API [status page](https://dev.telstra.com/api/status) to see if an active incident is causing the internal error. | | NETWORK_ERR | Please try again later. |  |  * Content-Language -  <br>  |
| **0** | Unexpected  |  * Content-Language -  <br>  |


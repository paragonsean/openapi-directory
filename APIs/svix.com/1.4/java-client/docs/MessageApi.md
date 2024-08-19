# MessageApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMessageApiV1AppAppIdMsgPost**](MessageApi.md#createMessageApiV1AppAppIdMsgPost) | **POST** /api/v1/app/{app_id}/msg/ | Create Message |
| [**expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete**](MessageApi.md#expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete) | **DELETE** /api/v1/app/{app_id}/msg/{msg_id}/content/ | Delete message payload |
| [**getMessageApiV1AppAppIdMsgMsgIdGet**](MessageApi.md#getMessageApiV1AppAppIdMsgMsgIdGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/ | Get Message |
| [**listMessagesApiV1AppAppIdMsgGet**](MessageApi.md#listMessagesApiV1AppAppIdMsgGet) | **GET** /api/v1/app/{app_id}/msg/ | List Messages |


<a id="createMessageApiV1AppAppIdMsgPost"></a>
# **createMessageApiV1AppAppIdMsgPost**
> MessageOut createMessageApiV1AppAppIdMsgPost(appId, messageIn, withContent, idempotencyKey)

Create Message

Creates a new message and dispatches it to all of the application&#39;s endpoints.  The &#x60;eventId&#x60; is an optional custom unique ID. It&#39;s verified to be unique only up to a day, after that no verification will be made. If a message with the same &#x60;eventId&#x60; already exists for any application in your environment, a 409 conflict error will be returned.  The &#x60;eventType&#x60; indicates the type and schema of the event. All messages of a certain &#x60;eventType&#x60; are expected to have the same schema. Endpoints can choose to only listen to specific event types. Messages can also have &#x60;channels&#x60;, which similar to event types let endpoints filter by them. Unlike event types, messages can have multiple channels, and channels don&#39;t imply a specific message content or schema.  The &#x60;payload&#x60; property is the webhook&#39;s body (the actual webhook message). Svix supports payload sizes of up to ~350kb, though it&#39;s generally a good idea to keep webhook payloads small, probably no larger than 40kb.  The optional &#x60;application&#x60; property will be used to create an application if the application referenced in the path does not exist. If it does then this property is ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageApi apiInstance = new MessageApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    MessageIn messageIn = new MessageIn(); // MessageIn | 
    Boolean withContent = true; // Boolean | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      MessageOut result = apiInstance.createMessageApiV1AppAppIdMsgPost(appId, messageIn, withContent, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageApi#createMessageApiV1AppAppIdMsgPost");
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
| **appId** | **String**|  | |
| **messageIn** | [**MessageIn**](MessageIn.md)|  | |
| **withContent** | **Boolean**|  | [optional] [default to true] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**MessageOut**](MessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **413** | Request Entity Too Large |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete"></a>
# **expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete**
> expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete(msgId, appId, idempotencyKey)

Delete message payload

Delete the given message&#39;s payload. Useful in cases when a message was accidentally sent with sensitive content.  The message can&#39;t be replayed or resent once its payload has been deleted or expired.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageApi apiInstance = new MessageApi(defaultClient);
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete(msgId, appId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageApi#expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete");
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
| **msgId** | **String**|  | |
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="getMessageApiV1AppAppIdMsgMsgIdGet"></a>
# **getMessageApiV1AppAppIdMsgMsgIdGet**
> MessageOut getMessageApiV1AppAppIdMsgMsgIdGet(msgId, appId, idempotencyKey)

Get Message

Get a message by its ID or eventID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageApi apiInstance = new MessageApi(defaultClient);
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      MessageOut result = apiInstance.getMessageApiV1AppAppIdMsgMsgIdGet(msgId, appId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageApi#getMessageApiV1AppAppIdMsgMsgIdGet");
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
| **msgId** | **String**|  | |
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**MessageOut**](MessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="listMessagesApiV1AppAppIdMsgGet"></a>
# **listMessagesApiV1AppAppIdMsgGet**
> ListResponseMessageOut listMessagesApiV1AppAppIdMsgGet(appId, iterator, limit, eventTypes, channel, before, after, idempotencyKey)

List Messages

List all of the application&#39;s messages.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed. The &#x60;after&#x60; parameter lets you filter all items created after a certain date and is ignored if an iterator is passed. &#x60;before&#x60; and &#x60;after&#x60; cannot be used simultaneously.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageApi apiInstance = new MessageApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    List<String> eventTypes = Arrays.asList(); // List<String> | 
    String channel = "project_1337"; // String | 
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseMessageOut result = apiInstance.listMessagesApiV1AppAppIdMsgGet(appId, iterator, limit, eventTypes, channel, before, after, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageApi#listMessagesApiV1AppAppIdMsgGet");
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
| **appId** | **String**|  | |
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **eventTypes** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **channel** | **String**|  | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseMessageOut**](ListResponseMessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |


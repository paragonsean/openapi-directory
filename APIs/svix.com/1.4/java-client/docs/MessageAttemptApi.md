# MessageAttemptApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete**](MessageAttemptApi.md#expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete) | **DELETE** /api/v1/app/{app_id}/msg/{msg_id}/attempt/{attempt_id}/content/ | Delete attempt response body |
| [**getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet**](MessageAttemptApi.md#getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/attempt/{attempt_id}/ | Get Attempt |
| [**listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet**](MessageAttemptApi.md#listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/endpoint/ | List Attempted Destinations |
| [**listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet**](MessageAttemptApi.md#listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet) | **GET** /api/v1/app/{app_id}/endpoint/{endpoint_id}/msg/ | List Attempted Messages |
| [**listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet**](MessageAttemptApi.md#listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/attempt/ | List Attempts |
| [**listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet**](MessageAttemptApi.md#listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet) | **GET** /api/v1/app/{app_id}/attempt/endpoint/{endpoint_id}/ | List Attempts By Endpoint |
| [**listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet**](MessageAttemptApi.md#listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet) | **GET** /api/v1/app/{app_id}/attempt/msg/{msg_id}/ | List Attempts By Msg |
| [**listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet**](MessageAttemptApi.md#listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/attempt/ | List Attempts For Endpoint |
| [**resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost**](MessageAttemptApi.md#resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost) | **POST** /api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/resend/ | Resend Webhook |


<a id="expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete"></a>
# **expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete**
> expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete(attemptId, msgId, appId, idempotencyKey)

Delete attempt response body

Deletes the given attempt&#39;s response body. Useful when an endpoint accidentally returned sensitive content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String attemptId = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete(attemptId, msgId, appId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete");
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
| **attemptId** | **String**|  | |
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

<a id="getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet"></a>
# **getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet**
> MessageAttemptOut getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet(attemptId, msgId, appId, idempotencyKey)

Get Attempt

&#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String attemptId = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      MessageAttemptOut result = apiInstance.getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet(attemptId, msgId, appId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet");
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
| **attemptId** | **String**|  | |
| **msgId** | **String**|  | |
| **appId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**MessageAttemptOut**](MessageAttemptOut.md)

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

<a id="listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet"></a>
# **listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet**
> ListResponseMessageEndpointOut listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet(msgId, appId, iterator, limit, idempotencyKey)

List Attempted Destinations

&#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "msgep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseMessageEndpointOut result = apiInstance.listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet(msgId, appId, iterator, limit, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet");
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
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseMessageEndpointOut**](ListResponseMessageEndpointOut.md)

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

<a id="listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet"></a>
# **listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet**
> ListResponseEndpointMessageOut listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet(endpointId, appId, iterator, limit, channel, status, before, after, idempotencyKey)

List Attempted Messages

List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    String channel = "project_1337"; // String | 
    MessageStatus status = MessageStatus.fromValue("0"); // MessageStatus | 
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseEndpointMessageOut result = apiInstance.listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet(endpointId, appId, iterator, limit, channel, status, before, after, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet");
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
| **endpointId** | **String**|  | |
| **appId** | **String**|  | |
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **channel** | **String**|  | [optional] |
| **status** | [**MessageStatus**](.md)|  | [optional] [enum: 0, 1, 2, 3] |
| **before** | **OffsetDateTime**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseEndpointMessageOut**](ListResponseEndpointMessageOut.md)

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

<a id="listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet"></a>
# **listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet**
> ListResponseMessageAttemptOut listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet(appId, msgId, iterator, limit, endpointId, eventTypes, channel, status, before, after, idempotencyKey)

List Attempts

Deprecated: Please use \&quot;List Attempts by Endpoint\&quot; and \&quot;List Attempts by Msg\&quot; instead.  &#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    String endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    List<String> eventTypes = Arrays.asList(); // List<String> | 
    String channel = "project_1337"; // String | 
    MessageStatus status = MessageStatus.fromValue("0"); // MessageStatus | 
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseMessageAttemptOut result = apiInstance.listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet(appId, msgId, iterator, limit, endpointId, eventTypes, channel, status, before, after, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet");
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
| **msgId** | **String**|  | |
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **endpointId** | **String**|  | [optional] |
| **eventTypes** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **channel** | **String**|  | [optional] |
| **status** | [**MessageStatus**](.md)|  | [optional] [enum: 0, 1, 2, 3] |
| **before** | **OffsetDateTime**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseMessageAttemptOut**](ListResponseMessageAttemptOut.md)

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

<a id="listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet"></a>
# **listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet**
> ListResponseMessageAttemptOut listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet(appId, endpointId, iterator, limit, status, statusCodeClass, eventTypes, channel, before, after, idempotencyKey)

List Attempts By Endpoint

List attempts by endpoint id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    MessageStatus status = MessageStatus.fromValue("0"); // MessageStatus | 
    StatusCodeClass statusCodeClass = StatusCodeClass.fromValue("0"); // StatusCodeClass | 
    List<String> eventTypes = Arrays.asList(); // List<String> | 
    String channel = "project_1337"; // String | 
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseMessageAttemptOut result = apiInstance.listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet(appId, endpointId, iterator, limit, status, statusCodeClass, eventTypes, channel, before, after, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet");
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
| **endpointId** | **String**|  | |
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **status** | [**MessageStatus**](.md)|  | [optional] [enum: 0, 1, 2, 3] |
| **statusCodeClass** | [**StatusCodeClass**](.md)|  | [optional] [enum: 0, 100, 200, 300, 400, 500] |
| **eventTypes** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **channel** | **String**|  | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseMessageAttemptOut**](ListResponseMessageAttemptOut.md)

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

<a id="listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet"></a>
# **listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet**
> ListResponseMessageAttemptOut listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet(appId, msgId, endpointId, iterator, limit, status, statusCodeClass, eventTypes, channel, before, after, idempotencyKey)

List Attempts By Msg

List attempts by message id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    MessageStatus status = MessageStatus.fromValue("0"); // MessageStatus | 
    StatusCodeClass statusCodeClass = StatusCodeClass.fromValue("0"); // StatusCodeClass | 
    List<String> eventTypes = Arrays.asList(); // List<String> | 
    String channel = "project_1337"; // String | 
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseMessageAttemptOut result = apiInstance.listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet(appId, msgId, endpointId, iterator, limit, status, statusCodeClass, eventTypes, channel, before, after, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet");
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
| **msgId** | **String**|  | |
| **endpointId** | **String**|  | [optional] |
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **status** | [**MessageStatus**](.md)|  | [optional] [enum: 0, 1, 2, 3] |
| **statusCodeClass** | [**StatusCodeClass**](.md)|  | [optional] [enum: 0, 100, 200, 300, 400, 500] |
| **eventTypes** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **channel** | **String**|  | [optional] |
| **before** | **OffsetDateTime**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseMessageAttemptOut**](ListResponseMessageAttemptOut.md)

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

<a id="listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet"></a>
# **listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet**
> ListResponseMessageAttemptEndpointOut listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet(msgId, appId, endpointId, iterator, limit, eventTypes, channel, status, before, after, idempotencyKey)

List Attempts For Endpoint

DEPRECATED: please use list_attempts with endpoint_id as a query parameter instead.  List the message attempts for a particular endpoint.  Returning the endpoint.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String iterator = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    List<String> eventTypes = Arrays.asList(); // List<String> | 
    String channel = "project_1337"; // String | 
    MessageStatus status = MessageStatus.fromValue("0"); // MessageStatus | 
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime after = OffsetDateTime.now(); // OffsetDateTime | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseMessageAttemptEndpointOut result = apiInstance.listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet(msgId, appId, endpointId, iterator, limit, eventTypes, channel, status, before, after, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet");
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
| **endpointId** | **String**|  | |
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **eventTypes** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **channel** | **String**|  | [optional] |
| **status** | [**MessageStatus**](.md)|  | [optional] [enum: 0, 1, 2, 3] |
| **before** | **OffsetDateTime**|  | [optional] |
| **after** | **OffsetDateTime**|  | [optional] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseMessageAttemptEndpointOut**](ListResponseMessageAttemptEndpointOut.md)

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

<a id="resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost"></a>
# **resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost**
> resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost(endpointId, msgId, appId, idempotencyKey)

Resend Webhook

Resend a message to the specified endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageAttemptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    MessageAttemptApi apiInstance = new MessageAttemptApi(defaultClient);
    String endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost(endpointId, msgId, appId, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageAttemptApi#resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost");
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
| **endpointId** | **String**|  | |
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
| **202** | Successful Response |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |


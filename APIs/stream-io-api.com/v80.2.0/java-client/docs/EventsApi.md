# EventsApi

All URIs are relative to *https://chat.stream-io-api.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendEvent**](EventsApi.md#sendEvent) | **POST** /channels/{type}/{id}/event | Send event |
| [**sendUserCustomEvent**](EventsApi.md#sendUserCustomEvent) | **POST** /users/{user_id}/event | Send user event |
| [**sync_0**](EventsApi.md#sync_0) | **POST** /sync | Sync |


<a id="sendEvent"></a>
# **sendEvent**
> EventResponse sendEvent(type, id, sendEventRequest)

Send event

Sends event to the channel  Sends events: - any  Required permissions: - SendCustomEvent 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String type = "type_example"; // String | 
    String id = "id_example"; // String | 
    SendEventRequest sendEventRequest = new SendEventRequest(); // SendEventRequest | 
    try {
      EventResponse result = apiInstance.sendEvent(type, id, sendEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#sendEvent");
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
| **type** | **String**|  | |
| **id** | **String**|  | |
| **sendEventRequest** | [**SendEventRequest**](SendEventRequest.md)|  | |

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="sendUserCustomEvent"></a>
# **sendUserCustomEvent**
> Response sendUserCustomEvent(userId, sendUserCustomEventRequest)

Send user event

Sends a custom event to a user  Sends events: - custom 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String userId = "userId_example"; // String | 
    SendUserCustomEventRequest sendUserCustomEventRequest = new SendUserCustomEventRequest(); // SendUserCustomEventRequest | 
    try {
      Response result = apiInstance.sendUserCustomEvent(userId, sendUserCustomEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#sendUserCustomEvent");
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
| **userId** | **String**|  | |
| **sendUserCustomEventRequest** | [**SendUserCustomEventRequest**](SendUserCustomEventRequest.md)|  | |

### Return type

[**Response**](Response.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |

<a id="sync_0"></a>
# **sync_0**
> SyncResponse sync_0(syncRequest, withInaccessibleCids, watch, clientId, connectionId)

Sync

Returns all events happened since client disconnect in specified channels  Required permissions: - ReadChannel 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.stream-io-api.com");
    
    // Configure API key authorization: stream-auth-type
    ApiKeyAuth stream-auth-type = (ApiKeyAuth) defaultClient.getAuthentication("stream-auth-type");
    stream-auth-type.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //stream-auth-type.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    SyncRequest syncRequest = new SyncRequest(); // SyncRequest | 
    Boolean withInaccessibleCids = true; // Boolean | 
    Boolean watch = true; // Boolean | 
    String clientId = "clientId_example"; // String | 
    String connectionId = "connectionId_example"; // String | 
    try {
      SyncResponse result = apiInstance.sync_0(syncRequest, withInaccessibleCids, watch, clientId, connectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#sync_0");
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
| **syncRequest** | [**SyncRequest**](SyncRequest.md)|  | |
| **withInaccessibleCids** | **Boolean**|  | [optional] |
| **watch** | **Boolean**|  | [optional] |
| **clientId** | **String**|  | [optional] |
| **connectionId** | **String**|  | [optional] |

### Return type

[**SyncResponse**](SyncResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **400** | Bad request |  -  |
| **429** | Too many requests |  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - Timestamp when number of requests will be reset <br>  |


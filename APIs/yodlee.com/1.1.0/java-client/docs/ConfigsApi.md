# ConfigsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSubscriptionNotificationEvent**](ConfigsApi.md#createSubscriptionNotificationEvent) | **POST** /configs/notifications/events/{eventName} | Subscribe For Notification Event |
| [**deleteSubscribedNotificationEvent**](ConfigsApi.md#deleteSubscribedNotificationEvent) | **DELETE** /configs/notifications/events/{eventName} | Delete Notification Subscription |
| [**getPublicEncryptionKey**](ConfigsApi.md#getPublicEncryptionKey) | **GET** /configs/publicKey | Get Public Key |
| [**getSubscribedNotificationEvents**](ConfigsApi.md#getSubscribedNotificationEvents) | **GET** /configs/notifications/events | Get Subscribed Notification Events |
| [**updateSubscribedNotificationEvent**](ConfigsApi.md#updateSubscribedNotificationEvent) | **PUT** /configs/notifications/events/{eventName} | Update Notification Subscription |


<a id="createSubscriptionNotificationEvent"></a>
# **createSubscriptionNotificationEvent**
> createSubscriptionNotificationEvent(eventName, createConfigsNotificationEventRequest)

Subscribe For Notification Event

The subscribe events service is used to subscribe to an event for receiving notifications.&lt;br&gt;The callback URL, where the notification will be posted should be provided to this service.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;Customers can subscribe to REFRESH,DATA_UPDATES and AUTO_REFRESH_UPDATES event.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;This service is not available in developer sandbox/test environment and will be made available for testing in your dedicated environment, once the contract is signed.&lt;li&gt;The content type has to be passed as application/json for the body parameter.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigsApi apiInstance = new ConfigsApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    CreateConfigsNotificationEventRequest createConfigsNotificationEventRequest = new CreateConfigsNotificationEventRequest(); // CreateConfigsNotificationEventRequest | eventRequest
    try {
      apiInstance.createSubscriptionNotificationEvent(eventName, createConfigsNotificationEventRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigsApi#createSubscriptionNotificationEvent");
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
| **eventName** | **String**| eventName | [enum: REFRESH, DATA_UPDATES, AUTO_REFRESH_UPDATES] |
| **createConfigsNotificationEventRequest** | [**CreateConfigsNotificationEventRequest**](CreateConfigsNotificationEventRequest.md)| eventRequest | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Y803 : eventName required&lt;br&gt;Y803 : callbackUrl required&lt;br&gt;Y800 : Invalid value for callbackUrl |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="deleteSubscribedNotificationEvent"></a>
# **deleteSubscribedNotificationEvent**
> deleteSubscribedNotificationEvent(eventName)

Delete Notification Subscription

The delete events service is used to unsubscribe from an events service.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigsApi apiInstance = new ConfigsApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    try {
      apiInstance.deleteSubscribedNotificationEvent(eventName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigsApi#deleteSubscribedNotificationEvent");
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
| **eventName** | **String**| eventName | [enum: REFRESH, DATA_UPDATES, AUTO_REFRESH_UPDATES] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Y803 : eventName required |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getPublicEncryptionKey"></a>
# **getPublicEncryptionKey**
> ConfigsPublicKeyResponse getPublicEncryptionKey()

Get Public Key

The get public key service provides the public key that should be used to encrypt user credentials while invoking POST /providerAccounts and PUT /providerAccounts endpoints.&lt;br&gt;This service will only work if the PKI (public key infrastructure) feature is enabled for the customer.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt; The key in the response is a string in PEM format.&lt;/li&gt;&lt;li&gt;This endpoint is not available in the Sandbox environment and it is useful only if the PKI feature is enabled.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigsApi apiInstance = new ConfigsApi(defaultClient);
    try {
      ConfigsPublicKeyResponse result = apiInstance.getPublicEncryptionKey();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigsApi#getPublicEncryptionKey");
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

[**ConfigsPublicKeyResponse**](ConfigsPublicKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getSubscribedNotificationEvents"></a>
# **getSubscribedNotificationEvents**
> ConfigsNotificationResponse getSubscribedNotificationEvents(eventName)

Get Subscribed Notification Events

The get events service provides the list of events for which consumers subscribed to receive notifications. &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigsApi apiInstance = new ConfigsApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    try {
      ConfigsNotificationResponse result = apiInstance.getSubscribedNotificationEvents(eventName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigsApi#getSubscribedNotificationEvents");
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
| **eventName** | **String**| eventName | [optional] [enum: REFRESH, DATA_UPDATES, AUTO_REFRESH_UPDATES] |

### Return type

[**ConfigsNotificationResponse**](ConfigsNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="updateSubscribedNotificationEvent"></a>
# **updateSubscribedNotificationEvent**
> updateSubscribedNotificationEvent(eventName, updateConfigsNotificationEventRequest)

Update Notification Subscription

The update events service is used to update the callback URL.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;The content type has to be passed as application/json for the body parameter. &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ConfigsApi apiInstance = new ConfigsApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    UpdateConfigsNotificationEventRequest updateConfigsNotificationEventRequest = new UpdateConfigsNotificationEventRequest(); // UpdateConfigsNotificationEventRequest | eventRequest
    try {
      apiInstance.updateSubscribedNotificationEvent(eventName, updateConfigsNotificationEventRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigsApi#updateSubscribedNotificationEvent");
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
| **eventName** | **String**| eventName | [enum: REFRESH, DATA_UPDATES, AUTO_REFRESH_UPDATES] |
| **updateConfigsNotificationEventRequest** | [**UpdateConfigsNotificationEventRequest**](UpdateConfigsNotificationEventRequest.md)| eventRequest | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Y803 : eventName required&lt;br&gt;Y803 : callbackUrl required&lt;br&gt;Y800 : Invalid value for callbackUrl |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |


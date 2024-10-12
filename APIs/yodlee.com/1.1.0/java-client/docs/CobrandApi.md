# CobrandApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cobrandLogin**](CobrandApi.md#cobrandLogin) | **POST** /cobrand/login | Cobrand Login |
| [**cobrandLogout**](CobrandApi.md#cobrandLogout) | **POST** /cobrand/logout | Cobrand Logout |
| [**createSubscriptionEvent**](CobrandApi.md#createSubscriptionEvent) | **POST** /cobrand/config/notifications/events/{eventName} | Subscribe Event |
| [**deleteSubscribedEvent**](CobrandApi.md#deleteSubscribedEvent) | **DELETE** /cobrand/config/notifications/events/{eventName} | Delete Subscription |
| [**getPublicKey**](CobrandApi.md#getPublicKey) | **GET** /cobrand/publicKey | Get Public Key |
| [**getSubscribedEvents**](CobrandApi.md#getSubscribedEvents) | **GET** /cobrand/config/notifications/events | Get Subscribed Events |
| [**updateSubscribedEvent**](CobrandApi.md#updateSubscribedEvent) | **PUT** /cobrand/config/notifications/events/{eventName} | Update Subscription |


<a id="cobrandLogin"></a>
# **cobrandLogin**
> CobrandLoginResponse cobrandLogin(cobrandLoginRequest)

Cobrand Login

The cobrand login service authenticates a cobrand.&lt;br&gt;Cobrand session in the response includes the cobrand session token (cobSession) &lt;br&gt;which is used in subsequent API calls like registering or signing in the user. &lt;br&gt;The idle timeout for a cobrand session is 2 hours and the absolute timeout is 24 hours. This service can be &lt;br&gt;invoked to create a new cobrand session token. &lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.&lt;br&gt;The content type has to be passed as application/json for the body parameter. &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CobrandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CobrandApi apiInstance = new CobrandApi(defaultClient);
    CobrandLoginRequest cobrandLoginRequest = new CobrandLoginRequest(); // CobrandLoginRequest | cobrandLoginRequest
    try {
      CobrandLoginResponse result = apiInstance.cobrandLogin(cobrandLoginRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CobrandApi#cobrandLogin");
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
| **cobrandLoginRequest** | [**CobrandLoginRequest**](CobrandLoginRequest.md)| cobrandLoginRequest | |

### Return type

[**CobrandLoginResponse**](CobrandLoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for cobrandParam |  -  |
| **401** | Y003 : Account is locked, contact Yodlee customer care&lt;br&gt;Y001 : User name and password required |  -  |
| **404** | Not Found |  -  |

<a id="cobrandLogout"></a>
# **cobrandLogout**
> cobrandLogout()

Cobrand Logout

The cobrand logout service is used to log out the cobrand.&lt;br&gt;This service does not return a response. The HTTP response code is 204 (Success with no content).&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CobrandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CobrandApi apiInstance = new CobrandApi(defaultClient);
    try {
      apiInstance.cobrandLogout();
    } catch (ApiException e) {
      System.err.println("Exception when calling CobrandApi#cobrandLogout");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Logout successful |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="createSubscriptionEvent"></a>
# **createSubscriptionEvent**
> createSubscriptionEvent(eventName, createCobrandNotificationEventRequest)

Subscribe Event

&lt;b&gt;Refer POST /configs/notifications/events/{eventName}.&lt;/b&gt;&lt;br&gt;The subscribe events service is used to subscribe to an event for receiving notifications.&lt;br&gt;The callback URL, where the notification will be posted should be provided to this service.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;Customers can subscribe to REFRESH,DATA_UPDATES and AUTO_REFRESH_UPDATES event.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes&lt;/b&gt;:&lt;br&gt;This service is not available in developer sandbox/test environment and will be made available for testing in your dedicated environment, once the contract is signed.&lt;br&gt;The content type has to be passed as application/json for the body parameter.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CobrandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CobrandApi apiInstance = new CobrandApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    CreateCobrandNotificationEventRequest createCobrandNotificationEventRequest = new CreateCobrandNotificationEventRequest(); // CreateCobrandNotificationEventRequest | eventRequest
    try {
      apiInstance.createSubscriptionEvent(eventName, createCobrandNotificationEventRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CobrandApi#createSubscriptionEvent");
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
| **createCobrandNotificationEventRequest** | [**CreateCobrandNotificationEventRequest**](CreateCobrandNotificationEventRequest.md)| eventRequest | |

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

<a id="deleteSubscribedEvent"></a>
# **deleteSubscribedEvent**
> deleteSubscribedEvent(eventName)

Delete Subscription

&lt;b&gt;Refer DELETE /configs/notifications/events/{eventName}.&lt;/b&gt;&lt;br&gt;The delete events service is used to unsubscribe from an events service.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CobrandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CobrandApi apiInstance = new CobrandApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    try {
      apiInstance.deleteSubscribedEvent(eventName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CobrandApi#deleteSubscribedEvent");
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

<a id="getPublicKey"></a>
# **getPublicKey**
> CobrandPublicKeyResponse getPublicKey()

Get Public Key

&lt;b&gt;Refer GET /configs/publicKey.&lt;/b&gt;&lt;br&gt;The get public key service provides the customer the public key that should be used to encrypt the user credentials before sending it to Yodlee.&lt;br&gt;This endpoint is useful only for PKI enabled.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CobrandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CobrandApi apiInstance = new CobrandApi(defaultClient);
    try {
      CobrandPublicKeyResponse result = apiInstance.getPublicKey();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CobrandApi#getPublicKey");
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

[**CobrandPublicKeyResponse**](CobrandPublicKeyResponse.md)

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

<a id="getSubscribedEvents"></a>
# **getSubscribedEvents**
> CobrandNotificationResponse getSubscribedEvents(eventName)

Get Subscribed Events

&lt;b&gt;Refer GET /configs/notifications/events.&lt;/b&gt;&lt;br&gt;The get events service provides the list of events for which consumers subscribed &lt;br&gt;to receive notifications. &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CobrandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CobrandApi apiInstance = new CobrandApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    try {
      CobrandNotificationResponse result = apiInstance.getSubscribedEvents(eventName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CobrandApi#getSubscribedEvents");
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

[**CobrandNotificationResponse**](CobrandNotificationResponse.md)

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

<a id="updateSubscribedEvent"></a>
# **updateSubscribedEvent**
> updateSubscribedEvent(eventName, updateCobrandNotificationEventRequest)

Update Subscription

&lt;b&gt;Refer PUT /configs/notifications/events/{eventName}.&lt;/b&gt;&lt;br&gt;The update events service is used to update the callback URL.&lt;br&gt;If the callback URL is invalid or inaccessible, the subscription will be unsuccessful, and an error will be thrown.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; The content type has to be passed as application/json for the body parameter. &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CobrandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CobrandApi apiInstance = new CobrandApi(defaultClient);
    String eventName = "REFRESH"; // String | eventName
    UpdateCobrandNotificationEventRequest updateCobrandNotificationEventRequest = new UpdateCobrandNotificationEventRequest(); // UpdateCobrandNotificationEventRequest | eventRequest
    try {
      apiInstance.updateSubscribedEvent(eventName, updateCobrandNotificationEventRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CobrandApi#updateSubscribedEvent");
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
| **updateCobrandNotificationEventRequest** | [**UpdateCobrandNotificationEventRequest**](UpdateCobrandNotificationEventRequest.md)| eventRequest | |

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


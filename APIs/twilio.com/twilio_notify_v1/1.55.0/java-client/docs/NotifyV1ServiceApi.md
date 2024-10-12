# NotifyV1ServiceApi

All URIs are relative to *https://notify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](NotifyV1ServiceApi.md#createService) | **POST** /v1/Services |  |
| [**deleteService**](NotifyV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} |  |
| [**fetchService**](NotifyV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} |  |
| [**listService**](NotifyV1ServiceApi.md#listService) | **GET** /v1/Services |  |
| [**updateService**](NotifyV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> NotifyV1Service createService(alexaSkillId, apnCredentialSid, defaultAlexaNotificationProtocolVersion, defaultApnNotificationProtocolVersion, defaultFcmNotificationProtocolVersion, defaultGcmNotificationProtocolVersion, deliveryCallbackEnabled, deliveryCallbackUrl, facebookMessengerPageId, fcmCredentialSid, friendlyName, gcmCredentialSid, logEnabled, messagingServiceSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1ServiceApi apiInstance = new NotifyV1ServiceApi(defaultClient);
    String alexaSkillId = "alexaSkillId_example"; // String | Deprecated.
    String apnCredentialSid = "apnCredentialSid_example"; // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings.
    String defaultAlexaNotificationProtocolVersion = "defaultAlexaNotificationProtocolVersion_example"; // String | Deprecated.
    String defaultApnNotificationProtocolVersion = "defaultApnNotificationProtocolVersion_example"; // String | The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
    String defaultFcmNotificationProtocolVersion = "defaultFcmNotificationProtocolVersion_example"; // String | The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
    String defaultGcmNotificationProtocolVersion = "defaultGcmNotificationProtocolVersion_example"; // String | The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
    Boolean deliveryCallbackEnabled = true; // Boolean | Callback configuration that enables delivery callbacks, default false
    String deliveryCallbackUrl = "deliveryCallbackUrl_example"; // String | URL to send delivery status callback.
    String facebookMessengerPageId = "facebookMessengerPageId_example"; // String | Deprecated.
    String fcmCredentialSid = "fcmCredentialSid_example"; // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    String gcmCredentialSid = "gcmCredentialSid_example"; // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings.
    Boolean logEnabled = true; // Boolean | Whether to log notifications. Can be: `true` or `false` and the default is `true`.
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications.
    try {
      NotifyV1Service result = apiInstance.createService(alexaSkillId, apnCredentialSid, defaultAlexaNotificationProtocolVersion, defaultApnNotificationProtocolVersion, defaultFcmNotificationProtocolVersion, defaultGcmNotificationProtocolVersion, deliveryCallbackEnabled, deliveryCallbackUrl, facebookMessengerPageId, fcmCredentialSid, friendlyName, gcmCredentialSid, logEnabled, messagingServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1ServiceApi#createService");
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
| **alexaSkillId** | **String**| Deprecated. | [optional] |
| **apnCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings. | [optional] |
| **defaultAlexaNotificationProtocolVersion** | **String**| Deprecated. | [optional] |
| **defaultApnNotificationProtocolVersion** | **String**| The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] |
| **defaultFcmNotificationProtocolVersion** | **String**| The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] |
| **defaultGcmNotificationProtocolVersion** | **String**| The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] |
| **deliveryCallbackEnabled** | **Boolean**| Callback configuration that enables delivery callbacks, default false | [optional] |
| **deliveryCallbackUrl** | **String**| URL to send delivery status callback. | [optional] |
| **facebookMessengerPageId** | **String**| Deprecated. | [optional] |
| **fcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **gcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings. | [optional] |
| **logEnabled** | **Boolean**| Whether to log notifications. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] |
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications. | [optional] |

### Return type

[**NotifyV1Service**](NotifyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1ServiceApi apiInstance = new NotifyV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to delete.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1ServiceApi#deleteService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchService"></a>
# **fetchService**
> NotifyV1Service fetchService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1ServiceApi apiInstance = new NotifyV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to fetch.
    try {
      NotifyV1Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1ServiceApi#fetchService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to fetch. | |

### Return type

[**NotifyV1Service**](NotifyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(friendlyName, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1ServiceApi apiInstance = new NotifyV1ServiceApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | The string that identifies the Service resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(friendlyName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1ServiceApi#listService");
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
| **friendlyName** | **String**| The string that identifies the Service resources to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> NotifyV1Service updateService(sid, alexaSkillId, apnCredentialSid, defaultAlexaNotificationProtocolVersion, defaultApnNotificationProtocolVersion, defaultFcmNotificationProtocolVersion, defaultGcmNotificationProtocolVersion, deliveryCallbackEnabled, deliveryCallbackUrl, facebookMessengerPageId, fcmCredentialSid, friendlyName, gcmCredentialSid, logEnabled, messagingServiceSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1ServiceApi apiInstance = new NotifyV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
    String alexaSkillId = "alexaSkillId_example"; // String | Deprecated.
    String apnCredentialSid = "apnCredentialSid_example"; // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings.
    String defaultAlexaNotificationProtocolVersion = "defaultAlexaNotificationProtocolVersion_example"; // String | Deprecated.
    String defaultApnNotificationProtocolVersion = "defaultApnNotificationProtocolVersion_example"; // String | The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
    String defaultFcmNotificationProtocolVersion = "defaultFcmNotificationProtocolVersion_example"; // String | The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
    String defaultGcmNotificationProtocolVersion = "defaultGcmNotificationProtocolVersion_example"; // String | The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
    Boolean deliveryCallbackEnabled = true; // Boolean | Callback configuration that enables delivery callbacks, default false
    String deliveryCallbackUrl = "deliveryCallbackUrl_example"; // String | URL to send delivery status callback.
    String facebookMessengerPageId = "facebookMessengerPageId_example"; // String | Deprecated.
    String fcmCredentialSid = "fcmCredentialSid_example"; // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    String gcmCredentialSid = "gcmCredentialSid_example"; // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings.
    Boolean logEnabled = true; // Boolean | Whether to log notifications. Can be: `true` or `false` and the default is `true`.
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications.
    try {
      NotifyV1Service result = apiInstance.updateService(sid, alexaSkillId, apnCredentialSid, defaultAlexaNotificationProtocolVersion, defaultApnNotificationProtocolVersion, defaultFcmNotificationProtocolVersion, defaultGcmNotificationProtocolVersion, deliveryCallbackEnabled, deliveryCallbackUrl, facebookMessengerPageId, fcmCredentialSid, friendlyName, gcmCredentialSid, logEnabled, messagingServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1ServiceApi#updateService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | |
| **alexaSkillId** | **String**| Deprecated. | [optional] |
| **apnCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings. | [optional] |
| **defaultAlexaNotificationProtocolVersion** | **String**| Deprecated. | [optional] |
| **defaultApnNotificationProtocolVersion** | **String**| The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] |
| **defaultFcmNotificationProtocolVersion** | **String**| The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] |
| **defaultGcmNotificationProtocolVersion** | **String**| The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] |
| **deliveryCallbackEnabled** | **Boolean**| Callback configuration that enables delivery callbacks, default false | [optional] |
| **deliveryCallbackUrl** | **String**| URL to send delivery status callback. | [optional] |
| **facebookMessengerPageId** | **String**| Deprecated. | [optional] |
| **fcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **gcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings. | [optional] |
| **logEnabled** | **Boolean**| Whether to log notifications. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] |
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications. | [optional] |

### Return type

[**NotifyV1Service**](NotifyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


# Api20100401UserDefinedMessageSubscriptionApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUserDefinedMessageSubscription**](Api20100401UserDefinedMessageSubscriptionApi.md#createUserDefinedMessageSubscription) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json |  |
| [**deleteUserDefinedMessageSubscription**](Api20100401UserDefinedMessageSubscriptionApi.md#deleteUserDefinedMessageSubscription) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions/{Sid}.json |  |


<a id="createUserDefinedMessageSubscription"></a>
# **createUserDefinedMessageSubscription**
> ApiV2010AccountCallUserDefinedMessageSubscription createUserDefinedMessageSubscription(accountSid, callSid, callback, idempotencyKey, method)



Subscribe to User Defined Messages for a given Call SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401UserDefinedMessageSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401UserDefinedMessageSubscriptionApi apiInstance = new Api20100401UserDefinedMessageSubscriptionApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
    String callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages.
    URI callback = new URI(); // URI | The URL we should call using the `method` to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted).
    String idempotencyKey = "idempotencyKey_example"; // String | A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
    String method = "HEAD"; // String | The HTTP method Twilio will use when requesting the above `Url`. Either `GET` or `POST`. Default is `POST`.
    try {
      ApiV2010AccountCallUserDefinedMessageSubscription result = apiInstance.createUserDefinedMessageSubscription(accountSid, callSid, callback, idempotencyKey, method);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401UserDefinedMessageSubscriptionApi#createUserDefinedMessageSubscription");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages. | |
| **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages. | |
| **callback** | **URI**| The URL we should call using the &#x60;method&#x60; to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted). | |
| **idempotencyKey** | **String**| A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated. | [optional] |
| **method** | **String**| The HTTP method Twilio will use when requesting the above &#x60;Url&#x60;. Either &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |

### Return type

[**ApiV2010AccountCallUserDefinedMessageSubscription**](ApiV2010AccountCallUserDefinedMessageSubscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteUserDefinedMessageSubscription"></a>
# **deleteUserDefinedMessageSubscription**
> deleteUserDefinedMessageSubscription(accountSid, callSid, sid)



Delete a specific User Defined Message Subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401UserDefinedMessageSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401UserDefinedMessageSubscriptionApi apiInstance = new Api20100401UserDefinedMessageSubscriptionApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
    String callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.
    String sid = "sid_example"; // String | The SID that uniquely identifies this User Defined Message Subscription.
    try {
      apiInstance.deleteUserDefinedMessageSubscription(accountSid, callSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401UserDefinedMessageSubscriptionApi#deleteUserDefinedMessageSubscription");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages. | |
| **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages. | |
| **sid** | **String**| The SID that uniquely identifies this User Defined Message Subscription. | |

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


# SubscriptionsApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05SubscriptionRequestsCmInitPost**](SubscriptionsApi.md#v05SubscriptionRequestsCmInitPost) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription |
| [**v05SubscriptionRequestsCmOnInitPost**](SubscriptionsApi.md#v05SubscriptionRequestsCmOnInitPost) | **POST** /v0.5/subscription-requests/cm/on-init | callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription. |
| [**v05SubscriptionRequestsHiuNotifyPost**](SubscriptionsApi.md#v05SubscriptionRequestsHiuNotifyPost) | **POST** /v0.5/subscription-requests/hiu/notify | Notification for subscription grant/deny/revoke |
| [**v05SubscriptionRequestsHiuOnNotifyPost**](SubscriptionsApi.md#v05SubscriptionRequestsHiuOnNotifyPost) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification. |
| [**v05SubscriptionsHiuNotifyPost**](SubscriptionsApi.md#v05SubscriptionsHiuNotifyPost) | **POST** /v0.5/subscriptions/hiu/notify | Notification to HIU on basis of a granted subscription |
| [**v05SubscriptionsHiuOnNotifyPost**](SubscriptionsApi.md#v05SubscriptionsHiuOnNotifyPost) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification. |


<a id="v05SubscriptionRequestsCmInitPost"></a>
# **v05SubscriptionRequestsCmInitPost**
> v05SubscriptionRequestsCmInitPost(authorization, X_CM_ID, subscriptionRequest)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    SubscriptionRequest subscriptionRequest = new SubscriptionRequest(); // SubscriptionRequest | 
    try {
      apiInstance.v05SubscriptionRequestsCmInitPost(authorization, X_CM_ID, subscriptionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#v05SubscriptionRequestsCmInitPost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | |
| **subscriptionRequest** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request Accepted |  -  |
| **400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
| **401** | **Causes:**   * Expired/Invalid token.  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05SubscriptionRequestsCmOnInitPost"></a>
# **v05SubscriptionRequestsCmOnInitPost**
> v05SubscriptionRequestsCmOnInitPost(authorization, X_HIU_ID, hiUSubscriptionRequestReceipt)

callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

This callback API acknowledges the request for subscription from a HIU, and sends back a \&quot;id\&quot; that will be used when the patient/user approves or denies the subscription.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    HIUSubscriptionRequestReceipt hiUSubscriptionRequestReceipt = new HIUSubscriptionRequestReceipt(); // HIUSubscriptionRequestReceipt | 
    try {
      apiInstance.v05SubscriptionRequestsCmOnInitPost(authorization, X_HIU_ID, hiUSubscriptionRequestReceipt);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#v05SubscriptionRequestsCmOnInitPost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | |
| **hiUSubscriptionRequestReceipt** | [**HIUSubscriptionRequestReceipt**](HIUSubscriptionRequestReceipt.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request Accepted. |  -  |
| **401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
| **500** | **Causes:**   * Downstream services are down  |  -  |

<a id="v05SubscriptionRequestsHiuNotifyPost"></a>
# **v05SubscriptionRequestsHiuNotifyPost**
> v05SubscriptionRequestsHiuNotifyPost(authorization, X_HIU_ID, subscriptionApprovalNotification)

Notification for subscription grant/deny/revoke

This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    SubscriptionApprovalNotification subscriptionApprovalNotification = new SubscriptionApprovalNotification(); // SubscriptionApprovalNotification | 
    try {
      apiInstance.v05SubscriptionRequestsHiuNotifyPost(authorization, X_HIU_ID, subscriptionApprovalNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#v05SubscriptionRequestsHiuNotifyPost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | |
| **subscriptionApprovalNotification** | [**SubscriptionApprovalNotification**](SubscriptionApprovalNotification.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request Accepted |  -  |
| **400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
| **401** | **Causes:**   * Expired/Invalid token.  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05SubscriptionRequestsHiuOnNotifyPost"></a>
# **v05SubscriptionRequestsHiuOnNotifyPost**
> v05SubscriptionRequestsHiuOnNotifyPost(authorization, X_CM_ID, hiUSubscriptionRequestNotificationAcknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIUSubscriptionRequestNotificationAcknowledgement hiUSubscriptionRequestNotificationAcknowledgement = new HIUSubscriptionRequestNotificationAcknowledgement(); // HIUSubscriptionRequestNotificationAcknowledgement | 
    try {
      apiInstance.v05SubscriptionRequestsHiuOnNotifyPost(authorization, X_CM_ID, hiUSubscriptionRequestNotificationAcknowledgement);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#v05SubscriptionRequestsHiuOnNotifyPost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | |
| **hiUSubscriptionRequestNotificationAcknowledgement** | [**HIUSubscriptionRequestNotificationAcknowledgement**](HIUSubscriptionRequestNotificationAcknowledgement.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request Accepted. |  -  |
| **401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
| **500** | **Causes:**   * Downstream services are down  |  -  |

<a id="v05SubscriptionsHiuNotifyPost"></a>
# **v05SubscriptionsHiuNotifyPost**
> v05SubscriptionsHiuNotifyPost(authorization, X_HIU_ID, hiUSubscriptionNotification)

Notification to HIU on basis of a granted subscription

This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category &#x3D; LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category &#x3D; DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    HIUSubscriptionNotification hiUSubscriptionNotification = new HIUSubscriptionNotification(); // HIUSubscriptionNotification | 
    try {
      apiInstance.v05SubscriptionsHiuNotifyPost(authorization, X_HIU_ID, hiUSubscriptionNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#v05SubscriptionsHiuNotifyPost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **X_HIU_ID** | **String**| Identifier of the health information user to which the request was intended. | |
| **hiUSubscriptionNotification** | [**HIUSubscriptionNotification**](HIUSubscriptionNotification.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request Accepted |  -  |
| **400** | **Causes:**   * Invalid data sent    * Required attributes not mentioned  |  -  |
| **401** | **Causes:**   * Expired/Invalid token.  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05SubscriptionsHiuOnNotifyPost"></a>
# **v05SubscriptionsHiuOnNotifyPost**
> v05SubscriptionsHiuOnNotifyPost(authorization, X_CM_ID, hiUSubscriptionNotificationAcknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    SubscriptionsApi apiInstance = new SubscriptionsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIUSubscriptionNotificationAcknowledgment hiUSubscriptionNotificationAcknowledgment = new HIUSubscriptionNotificationAcknowledgment(); // HIUSubscriptionNotificationAcknowledgment | 
    try {
      apiInstance.v05SubscriptionsHiuOnNotifyPost(authorization, X_CM_ID, hiUSubscriptionNotificationAcknowledgment);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApi#v05SubscriptionsHiuOnNotifyPost");
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | |
| **X_CM_ID** | **String**| Suffix of the consent manager to which the request was intended. | |
| **hiUSubscriptionNotificationAcknowledgment** | [**HIUSubscriptionNotificationAcknowledgment**](HIUSubscriptionNotificationAcknowledgment.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request Accepted. |  -  |
| **401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
| **500** | **Causes:**   * Downstream services are down  |  -  |


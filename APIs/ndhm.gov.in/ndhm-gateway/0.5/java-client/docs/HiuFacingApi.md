# HiuFacingApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05ConsentRequestsInitPost_0**](HiuFacingApi.md#v05ConsentRequestsInitPost_0) | **POST** /v0.5/consent-requests/init | Create consent request |
| [**v05ConsentRequestsStatusPost_0**](HiuFacingApi.md#v05ConsentRequestsStatusPost_0) | **POST** /v0.5/consent-requests/status | Get consent request status |
| [**v05ConsentsFetchPost_0**](HiuFacingApi.md#v05ConsentsFetchPost_0) | **POST** /v0.5/consents/fetch | Get consent artefact |
| [**v05ConsentsHiuOnNotifyPost_0**](HiuFacingApi.md#v05ConsentsHiuOnNotifyPost_0) | **POST** /v0.5/consents/hiu/on-notify | Consent notification |
| [**v05HealthInformationCmRequestPost_0**](HiuFacingApi.md#v05HealthInformationCmRequestPost_0) | **POST** /v0.5/health-information/cm/request | Health information data request |
| [**v05HealthInformationNotifyPost_1**](HiuFacingApi.md#v05HealthInformationNotifyPost_1) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow |
| [**v05PatientsFindPost_0**](HiuFacingApi.md#v05PatientsFindPost_0) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id |
| [**v05SubscriptionRequestsCmInitPost_0**](HiuFacingApi.md#v05SubscriptionRequestsCmInitPost_0) | **POST** /v0.5/subscription-requests/cm/init | Request for subscription |
| [**v05SubscriptionRequestsHiuOnNotifyPost_0**](HiuFacingApi.md#v05SubscriptionRequestsHiuOnNotifyPost_0) | **POST** /v0.5/subscription-requests/hiu/on-notify | Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification. |
| [**v05SubscriptionsHiuOnNotifyPost_0**](HiuFacingApi.md#v05SubscriptionsHiuOnNotifyPost_0) | **POST** /v0.5/subscriptions/hiu/on-notify | Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification. |
| [**v05UsersAuthConfirmPost_1**](HiuFacingApi.md#v05UsersAuthConfirmPost_1) | **POST** /v0.5/users/auth/confirm | Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation |
| [**v05UsersAuthFetchModesPost_1**](HiuFacingApi.md#v05UsersAuthFetchModesPost_1) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose |
| [**v05UsersAuthInitPost_1**](HiuFacingApi.md#v05UsersAuthInitPost_1) | **POST** /v0.5/users/auth/init | Initialize authentication from HIP |
| [**v05UsersAuthOnNotifyPost_1**](HiuFacingApi.md#v05UsersAuthOnNotifyPost_1) | **POST** /v0.5/users/auth/on-notify | callback API by HIU/HIPs as acknowledgement of auth notification |


<a id="v05ConsentRequestsInitPost_0"></a>
# **v05ConsentRequestsInitPost_0**
> v05ConsentRequestsInitPost_0(authorization, X_CM_ID, consentRequest)

Create consent request

Creates a consent request to get data about a patient by HIU user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    ConsentRequest consentRequest = new ConsentRequest(); // ConsentRequest | 
    try {
      apiInstance.v05ConsentRequestsInitPost_0(authorization, X_CM_ID, consentRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05ConsentRequestsInitPost_0");
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
| **consentRequest** | [**ConsentRequest**](ConsentRequest.md)|  | |

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

<a id="v05ConsentRequestsStatusPost_0"></a>
# **v05ConsentRequestsStatusPost_0**
> v05ConsentRequestsStatusPost_0(authorization, X_CM_ID, consentRequestStatusRequest)

Get consent request status

Get status of consent request done previously

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    ConsentRequestStatusRequest consentRequestStatusRequest = new ConsentRequestStatusRequest(); // ConsentRequestStatusRequest | 
    try {
      apiInstance.v05ConsentRequestsStatusPost_0(authorization, X_CM_ID, consentRequestStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05ConsentRequestsStatusPost_0");
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
| **consentRequestStatusRequest** | [**ConsentRequestStatusRequest**](ConsentRequestStatusRequest.md)|  | |

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
| **400** | **Causes:**   * Invalid data sent  |  -  |
| **401** | **Causes:**   * Expired/Invalid token.  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05ConsentsFetchPost_0"></a>
# **v05ConsentsFetchPost_0**
> v05ConsentsFetchPost_0(authorization, X_CM_ID, consentFetchRequest)

Get consent artefact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    ConsentFetchRequest consentFetchRequest = new ConsentFetchRequest(); // ConsentFetchRequest | 
    try {
      apiInstance.v05ConsentsFetchPost_0(authorization, X_CM_ID, consentFetchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05ConsentsFetchPost_0");
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
| **consentFetchRequest** | [**ConsentFetchRequest**](ConsentFetchRequest.md)|  | |

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
| **202** | Request Accepted |  -  |
| **400** | **Causes:**   * Invalid data sent  |  -  |
| **401** | **Causes:**   * Expired/Invalid token.  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05ConsentsHiuOnNotifyPost_0"></a>
# **v05ConsentsHiuOnNotifyPost_0**
> v05ConsentsHiuOnNotifyPost_0(authorization, X_CM_ID, hiUConsentNotificationResponse)

Consent notification

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIUConsentNotificationResponse hiUConsentNotificationResponse = new HIUConsentNotificationResponse(); // HIUConsentNotificationResponse | 
    try {
      apiInstance.v05ConsentsHiuOnNotifyPost_0(authorization, X_CM_ID, hiUConsentNotificationResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05ConsentsHiuOnNotifyPost_0");
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
| **hiUConsentNotificationResponse** | [**HIUConsentNotificationResponse**](HIUConsentNotificationResponse.md)|  | |

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

<a id="v05HealthInformationCmRequestPost_0"></a>
# **v05HealthInformationCmRequestPost_0**
> v05HealthInformationCmRequestPost_0(authorization, X_CM_ID, hiRequest)

Health information data request

Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIRequest hiRequest = new HIRequest(); // HIRequest | 
    try {
      apiInstance.v05HealthInformationCmRequestPost_0(authorization, X_CM_ID, hiRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05HealthInformationCmRequestPost_0");
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
| **hiRequest** | [**HIRequest**](HIRequest.md)|  | |

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
| **400** | **Causes:**   * Bad request  |  -  |
| **401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05HealthInformationNotifyPost_1"></a>
# **v05HealthInformationNotifyPost_1**
> v05HealthInformationNotifyPost_1(authorization, X_CM_ID, healthInformationNotification)

Notifications corresponding to events during data flow

API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HealthInformationNotification healthInformationNotification = new HealthInformationNotification(); // HealthInformationNotification | 
    try {
      apiInstance.v05HealthInformationNotifyPost_1(authorization, X_CM_ID, healthInformationNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05HealthInformationNotifyPost_1");
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
| **healthInformationNotification** | [**HealthInformationNotification**](HealthInformationNotification.md)|  | |

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
| **204** | Notification is Accepted |  -  |
| **400** | **Causes:**   * Invalid Request  |  -  |
| **401** | **Causes:**   * Expired/Invalid token.  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05PatientsFindPost_0"></a>
# **v05PatientsFindPost_0**
> v05PatientsFindPost_0(authorization, X_CM_ID, patientIdentificationRequest)

Identify a patient by her consent-manager user-id

This API is meant for identify to patient given her consent-manager-user-id 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientIdentificationRequest patientIdentificationRequest = new PatientIdentificationRequest(); // PatientIdentificationRequest | 
    try {
      apiInstance.v05PatientsFindPost_0(authorization, X_CM_ID, patientIdentificationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05PatientsFindPost_0");
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
| **patientIdentificationRequest** | [**PatientIdentificationRequest**](PatientIdentificationRequest.md)|  | |

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
| **400** | Invalid request, required attributes not provided  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05SubscriptionRequestsCmInitPost_0"></a>
# **v05SubscriptionRequestsCmInitPost_0**
> v05SubscriptionRequestsCmInitPost_0(authorization, X_CM_ID, subscriptionRequest)

Request for subscription

creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    SubscriptionRequest subscriptionRequest = new SubscriptionRequest(); // SubscriptionRequest | 
    try {
      apiInstance.v05SubscriptionRequestsCmInitPost_0(authorization, X_CM_ID, subscriptionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05SubscriptionRequestsCmInitPost_0");
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

<a id="v05SubscriptionRequestsHiuOnNotifyPost_0"></a>
# **v05SubscriptionRequestsHiuOnNotifyPost_0**
> v05SubscriptionRequestsHiuOnNotifyPost_0(authorization, X_CM_ID, hiUSubscriptionRequestNotificationAcknowledgement)

Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to subscription request relevant notifications.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIUSubscriptionRequestNotificationAcknowledgement hiUSubscriptionRequestNotificationAcknowledgement = new HIUSubscriptionRequestNotificationAcknowledgement(); // HIUSubscriptionRequestNotificationAcknowledgement | 
    try {
      apiInstance.v05SubscriptionRequestsHiuOnNotifyPost_0(authorization, X_CM_ID, hiUSubscriptionRequestNotificationAcknowledgement);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05SubscriptionRequestsHiuOnNotifyPost_0");
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

<a id="v05SubscriptionsHiuOnNotifyPost_0"></a>
# **v05SubscriptionsHiuOnNotifyPost_0**
> v05SubscriptionsHiuOnNotifyPost_0(authorization, X_CM_ID, hiUSubscriptionNotificationAcknowledgment)

Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIUSubscriptionNotificationAcknowledgment hiUSubscriptionNotificationAcknowledgment = new HIUSubscriptionNotificationAcknowledgment(); // HIUSubscriptionNotificationAcknowledgment | 
    try {
      apiInstance.v05SubscriptionsHiuOnNotifyPost_0(authorization, X_CM_ID, hiUSubscriptionNotificationAcknowledgment);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05SubscriptionsHiuOnNotifyPost_0");
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

<a id="v05UsersAuthConfirmPost_1"></a>
# **v05UsersAuthConfirmPost_1**
> v05UsersAuthConfirmPost_1(authorization, X_CM_ID, patientAuthConfirmRequest)

Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientAuthConfirmRequest patientAuthConfirmRequest = new PatientAuthConfirmRequest(); // PatientAuthConfirmRequest | 
    try {
      apiInstance.v05UsersAuthConfirmPost_1(authorization, X_CM_ID, patientAuthConfirmRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05UsersAuthConfirmPost_1");
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
| **patientAuthConfirmRequest** | [**PatientAuthConfirmRequest**](PatientAuthConfirmRequest.md)|  | |

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
| **202** | Request accepted |  -  |
| **400** | **Causes:**   * transaction id is not provided or invalid   * token or other auth confirmation details not provided or invalid  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05UsersAuthFetchModesPost_1"></a>
# **v05UsersAuthFetchModesPost_1**
> v05UsersAuthFetchModesPost_1(authorization, X_CM_ID, patientAuthModeQueryRequest)

Get a patient&#39;s authentication modes relevant to specified purpose

This API is meant for identify supported authentication modes for a patient given a specific purpose 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientAuthModeQueryRequest patientAuthModeQueryRequest = new PatientAuthModeQueryRequest(); // PatientAuthModeQueryRequest | 
    try {
      apiInstance.v05UsersAuthFetchModesPost_1(authorization, X_CM_ID, patientAuthModeQueryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05UsersAuthFetchModesPost_1");
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
| **patientAuthModeQueryRequest** | [**PatientAuthModeQueryRequest**](PatientAuthModeQueryRequest.md)|  | |

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
| **400** | Invalid request, required attributes not provided  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05UsersAuthInitPost_1"></a>
# **v05UsersAuthInitPost_1**
> v05UsersAuthInitPost_1(authorization, X_CM_ID, patientAuthInitRequest)

Initialize authentication from HIP

This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientAuthInitRequest patientAuthInitRequest = new PatientAuthInitRequest(); // PatientAuthInitRequest | 
    try {
      apiInstance.v05UsersAuthInitPost_1(authorization, X_CM_ID, patientAuthInitRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05UsersAuthInitPost_1");
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
| **patientAuthInitRequest** | [**PatientAuthInitRequest**](PatientAuthInitRequest.md)|  | |

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
| **202** | Request accepted |  -  |
| **400** | **Causes:**   * patient id is not provided  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05UsersAuthOnNotifyPost_1"></a>
# **v05UsersAuthOnNotifyPost_1**
> v05UsersAuthOnNotifyPost_1(authorization, X_CM_ID, patientAuthNotificationAcknowledgement)

callback API by HIU/HIPs as acknowledgement of auth notification

This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HiuFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    HiuFacingApi apiInstance = new HiuFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientAuthNotificationAcknowledgement patientAuthNotificationAcknowledgement = new PatientAuthNotificationAcknowledgement(); // PatientAuthNotificationAcknowledgement | 
    try {
      apiInstance.v05UsersAuthOnNotifyPost_1(authorization, X_CM_ID, patientAuthNotificationAcknowledgement);
    } catch (ApiException e) {
      System.err.println("Exception when calling HiuFacingApi#v05UsersAuthOnNotifyPost_1");
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
| **patientAuthNotificationAcknowledgement** | [**PatientAuthNotificationAcknowledgement**](PatientAuthNotificationAcknowledgement.md)|  | |

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
| **202** | Request accepted |  -  |
| **400** | **Causes:**   * required details not provided   * neither auth nor error specified   |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |


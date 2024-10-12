# ConsentFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05ConsentRequestsInitPost**](ConsentFlowApi.md#v05ConsentRequestsInitPost) | **POST** /v0.5/consent-requests/init | Create consent request |
| [**v05ConsentRequestsOnInitPost**](ConsentFlowApi.md#v05ConsentRequestsOnInitPost) | **POST** /v0.5/consent-requests/on-init | Response to consent request |
| [**v05ConsentRequestsOnStatusPost**](ConsentFlowApi.md#v05ConsentRequestsOnStatusPost) | **POST** /v0.5/consent-requests/on-status | Result of consent request status |
| [**v05ConsentRequestsStatusPost**](ConsentFlowApi.md#v05ConsentRequestsStatusPost) | **POST** /v0.5/consent-requests/status | Get consent request status |
| [**v05ConsentsFetchPost**](ConsentFlowApi.md#v05ConsentsFetchPost) | **POST** /v0.5/consents/fetch | Get consent artefact |
| [**v05ConsentsHipNotifyPost**](ConsentFlowApi.md#v05ConsentsHipNotifyPost) | **POST** /v0.5/consents/hip/notify | Consent notification |
| [**v05ConsentsHipOnNotifyPost**](ConsentFlowApi.md#v05ConsentsHipOnNotifyPost) | **POST** /v0.5/consents/hip/on-notify | Consent notification |
| [**v05ConsentsHiuNotifyPost**](ConsentFlowApi.md#v05ConsentsHiuNotifyPost) | **POST** /v0.5/consents/hiu/notify | Consent notification |
| [**v05ConsentsHiuOnNotifyPost**](ConsentFlowApi.md#v05ConsentsHiuOnNotifyPost) | **POST** /v0.5/consents/hiu/on-notify | Consent notification |
| [**v05ConsentsOnFetchPost**](ConsentFlowApi.md#v05ConsentsOnFetchPost) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact |


<a id="v05ConsentRequestsInitPost"></a>
# **v05ConsentRequestsInitPost**
> v05ConsentRequestsInitPost(authorization, X_CM_ID, consentRequest)

Create consent request

Creates a consent request to get data about a patient by HIU user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    ConsentRequest consentRequest = new ConsentRequest(); // ConsentRequest | 
    try {
      apiInstance.v05ConsentRequestsInitPost(authorization, X_CM_ID, consentRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentRequestsInitPost");
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

<a id="v05ConsentRequestsOnInitPost"></a>
# **v05ConsentRequestsOnInitPost**
> v05ConsentRequestsOnInitPost(authorization, X_HIU_ID, consentRequestInitResponse)

Response to consent request

Result of consent request creation for a patient. **consentRequest.id** represents the consentrequest id created by CM. The result must contain either **consentRequest** or the **error** caused. &lt;br/&gt;   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    ConsentRequestInitResponse consentRequestInitResponse = new ConsentRequestInitResponse(); // ConsentRequestInitResponse | 
    try {
      apiInstance.v05ConsentRequestsOnInitPost(authorization, X_HIU_ID, consentRequestInitResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentRequestsOnInitPost");
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
| **consentRequestInitResponse** | [**ConsentRequestInitResponse**](ConsentRequestInitResponse.md)|  | |

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

<a id="v05ConsentRequestsOnStatusPost"></a>
# **v05ConsentRequestsOnStatusPost**
> v05ConsentRequestsOnStatusPost(authorization, X_HIU_ID, hiUConsentRequestStatus)

Result of consent request status

Result of consent request done previously. Status of request can be GRANTED,  DENIED, EXPIRED. If the request was GRANTED, then  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    HIUConsentRequestStatus hiUConsentRequestStatus = new HIUConsentRequestStatus(); // HIUConsentRequestStatus | 
    try {
      apiInstance.v05ConsentRequestsOnStatusPost(authorization, X_HIU_ID, hiUConsentRequestStatus);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentRequestsOnStatusPost");
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
| **hiUConsentRequestStatus** | [**HIUConsentRequestStatus**](HIUConsentRequestStatus.md)|  | |

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

<a id="v05ConsentRequestsStatusPost"></a>
# **v05ConsentRequestsStatusPost**
> v05ConsentRequestsStatusPost(authorization, X_CM_ID, consentRequestStatusRequest)

Get consent request status

Get status of consent request done previously

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    ConsentRequestStatusRequest consentRequestStatusRequest = new ConsentRequestStatusRequest(); // ConsentRequestStatusRequest | 
    try {
      apiInstance.v05ConsentRequestsStatusPost(authorization, X_CM_ID, consentRequestStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentRequestsStatusPost");
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

<a id="v05ConsentsFetchPost"></a>
# **v05ConsentsFetchPost**
> v05ConsentsFetchPost(authorization, X_CM_ID, consentFetchRequest)

Get consent artefact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    ConsentFetchRequest consentFetchRequest = new ConsentFetchRequest(); // ConsentFetchRequest | 
    try {
      apiInstance.v05ConsentsFetchPost(authorization, X_CM_ID, consentFetchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentsFetchPost");
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

<a id="v05ConsentsHipNotifyPost"></a>
# **v05ConsentsHipNotifyPost**
> v05ConsentsHipNotifyPost(authorization, X_HIP_ID, hiPConsentNotification)

Consent notification

Notification of consents to health information providers consent request granted, consent revoked, consent expired. Only the GRANTED, REVOKED and EXPIRED status notifications will be sent to HIP.   1. If consent is granted, status&#x3D;GRANTED, then consentDetail contains the consent artefact details and signature is available.    2. If consent is revoked, then status&#x3D;REVOKED, and consentId specifes which consent artefact is revoked.    3. If the consent has expired, then status&#x3D;EXPIRED, and consentId specifies which consent artefact has expired. Note, this is also responsibility of the HIP to keep track of consent expiry. Any data request on expired consent artefact must not be done.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    HIPConsentNotification hiPConsentNotification = new HIPConsentNotification(); // HIPConsentNotification | 
    try {
      apiInstance.v05ConsentsHipNotifyPost(authorization, X_HIP_ID, hiPConsentNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentsHipNotifyPost");
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
| **X_HIP_ID** | **String**| Identifier of the health information provider to which the request was intended. | |
| **hiPConsentNotification** | [**HIPConsentNotification**](HIPConsentNotification.md)|  | |

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
| **401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
| **500** | **Causes:**   * Downstream services are down  |  -  |

<a id="v05ConsentsHipOnNotifyPost"></a>
# **v05ConsentsHipOnNotifyPost**
> v05ConsentsHipOnNotifyPost(authorization, X_CM_ID, hiPConsentNotificationResponse)

Consent notification

This API is called by HIP as acknowledgement to notification of consents, in cases of consent revocation and expiration.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIPConsentNotificationResponse hiPConsentNotificationResponse = new HIPConsentNotificationResponse(); // HIPConsentNotificationResponse | 
    try {
      apiInstance.v05ConsentsHipOnNotifyPost(authorization, X_CM_ID, hiPConsentNotificationResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentsHipOnNotifyPost");
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
| **hiPConsentNotificationResponse** | [**HIPConsentNotificationResponse**](HIPConsentNotificationResponse.md)|  | |

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
| **401** | **Causes:**   * Invalid/Expired/Empty token.  |  -  |
| **500** | **Causes:**   * Downstream services are down  |  -  |

<a id="v05ConsentsHiuNotifyPost"></a>
# **v05ConsentsHiuNotifyPost**
> v05ConsentsHiuNotifyPost(authorization, X_HIU_ID, hiUConsentNotificationEvent)

Consent notification

Health information user will get notified about the consent request granted or denied, consent revoked, consent expired.  1. For consent request grant, status&#x3D;GRANTED, consentRequestId&#x3D;&lt;consent-request-id&gt;, and consentArtefacts is an array of generated consent artefact Ids. 2. For consent request expiry, status&#x3D;EXPIRED, consentRequestId&#x3D;&lt;consent-request-id&gt; 3. For consent request denied, status&#x3D;DENIED, consentRequestId&#x3D;&lt;consent-request-id&gt; 4. For consent revocation, status&#x3D;REVOKED, consentArtefacts is an array of revoked consent artefact ids 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    HIUConsentNotificationEvent hiUConsentNotificationEvent = new HIUConsentNotificationEvent(); // HIUConsentNotificationEvent | 
    try {
      apiInstance.v05ConsentsHiuNotifyPost(authorization, X_HIU_ID, hiUConsentNotificationEvent);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentsHiuNotifyPost");
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
| **hiUConsentNotificationEvent** | [**HIUConsentNotificationEvent**](HIUConsentNotificationEvent.md)|  | |

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

<a id="v05ConsentsHiuOnNotifyPost"></a>
# **v05ConsentsHiuOnNotifyPost**
> v05ConsentsHiuOnNotifyPost(authorization, X_CM_ID, hiUConsentNotificationResponse)

Consent notification

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIUConsentNotificationResponse hiUConsentNotificationResponse = new HIUConsentNotificationResponse(); // HIUConsentNotificationResponse | 
    try {
      apiInstance.v05ConsentsHiuOnNotifyPost(authorization, X_CM_ID, hiUConsentNotificationResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentsHiuOnNotifyPost");
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

<a id="v05ConsentsOnFetchPost"></a>
# **v05ConsentsOnFetchPost**
> v05ConsentsOnFetchPost(authorization, X_HIU_ID, consentArtefactResponse)

Result of fetch request for a consent artefact

Must contain either consentDetail or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    ConsentFlowApi apiInstance = new ConsentFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    ConsentArtefactResponse consentArtefactResponse = new ConsentArtefactResponse(); // ConsentArtefactResponse | 
    try {
      apiInstance.v05ConsentsOnFetchPost(authorization, X_HIU_ID, consentArtefactResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentFlowApi#v05ConsentsOnFetchPost");
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
| **consentArtefactResponse** | [**ConsentArtefactResponse**](ConsentArtefactResponse.md)|  | |

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


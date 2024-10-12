# ConsentFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05ConsentRequestsOnInitPost**](ConsentFlowApi.md#v05ConsentRequestsOnInitPost) | **POST** /v0.5/consent-requests/on-init | Response to consent request |
| [**v05ConsentRequestsOnStatusPost**](ConsentFlowApi.md#v05ConsentRequestsOnStatusPost) | **POST** /v0.5/consent-requests/on-status | Result of consent request status |
| [**v05ConsentsHiuNotifyPost**](ConsentFlowApi.md#v05ConsentsHiuNotifyPost) | **POST** /v0.5/consents/hiu/notify | Consent notification |
| [**v05ConsentsOnFetchPost**](ConsentFlowApi.md#v05ConsentsOnFetchPost) | **POST** /v0.5/consents/on-fetch | Result of fetch request for a consent artefact |


<a id="v05ConsentRequestsOnInitPost"></a>
# **v05ConsentRequestsOnInitPost**
> v05ConsentRequestsOnInitPost(authorization, X_HIU_ID, consentRequestInitResponse)

Response to consent request

Result of consent request creation for a patient. **id** represents the consentrequest id created by CM. The result must contain either **id** or the **error** caused. &lt;br/&gt;   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

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
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | |
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
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | |
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
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | |
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

<a id="v05ConsentsOnFetchPost"></a>
# **v05ConsentsOnFetchPost**
> v05ConsentsOnFetchPost(authorization, X_HIU_ID, consentArtefactResponse)

Result of fetch request for a consent artefact

Must contain either consent or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

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
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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
| **authorization** | **String**| Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge. | |
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


# ConsentApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05ConsentRequestsInitPost**](ConsentApi.md#v05ConsentRequestsInitPost) | **POST** /v0.5/consent-requests/init | Create consent request |
| [**v05ConsentRequestsStatusPost**](ConsentApi.md#v05ConsentRequestsStatusPost) | **POST** /v0.5/consent-requests/status | Get consent request status |
| [**v05ConsentsFetchPost**](ConsentApi.md#v05ConsentsFetchPost) | **POST** /v0.5/consents/fetch | Get consent artefact |
| [**v05ConsentsHipOnNotifyPost**](ConsentApi.md#v05ConsentsHipOnNotifyPost) | **POST** /v0.5/consents/hip/on-notify | Consent notification |
| [**v05ConsentsHiuOnNotifyPost**](ConsentApi.md#v05ConsentsHiuOnNotifyPost) | **POST** /v0.5/consents/hiu/on-notify | Consent notification |


<a id="v05ConsentRequestsInitPost"></a>
# **v05ConsentRequestsInitPost**
> v05ConsentRequestsInitPost(authorization, consentRequest)

Create consent request

Creates a consent request to get data about a patient by HIU user. CM should call Gateway - ***_/v0.5/consent-requests/on-init*** API with the consent-request-id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    ConsentApi apiInstance = new ConsentApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    ConsentRequest consentRequest = new ConsentRequest(); // ConsentRequest | 
    try {
      apiInstance.v05ConsentRequestsInitPost(authorization, consentRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentApi#v05ConsentRequestsInitPost");
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

<a id="v05ConsentRequestsStatusPost"></a>
# **v05ConsentRequestsStatusPost**
> v05ConsentRequestsStatusPost(authorization, consentRequestStatusRequest)

Get consent request status

Get status of consent request done previously. CM responds by calling Gateway API - ***_/v0.5/consent-requests/on-status***

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    ConsentApi apiInstance = new ConsentApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    ConsentRequestStatusRequest consentRequestStatusRequest = new ConsentRequestStatusRequest(); // ConsentRequestStatusRequest | 
    try {
      apiInstance.v05ConsentRequestsStatusPost(authorization, consentRequestStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentApi#v05ConsentRequestsStatusPost");
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
> v05ConsentsFetchPost(authorization, consentFetchRequest)

Get consent artefact

This API is called when a HIU makes a request to get a consent artefact. For response please refer to the Gateway ***_/v0.5/consents/on-fetch***

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    ConsentApi apiInstance = new ConsentApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    ConsentFetchRequest consentFetchRequest = new ConsentFetchRequest(); // ConsentFetchRequest | 
    try {
      apiInstance.v05ConsentsFetchPost(authorization, consentFetchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentApi#v05ConsentsFetchPost");
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

<a id="v05ConsentsHipOnNotifyPost"></a>
# **v05ConsentsHipOnNotifyPost**
> v05ConsentsHipOnNotifyPost(authorization, hiPConsentNotificationResponse)

Consent notification

This API is called by HIP as acknowledgement to notification of consents, in cases of consent revocation and expiration, notified by CM earlier via Gateway API - ***_/v0.5/consents/hip/notify***.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    ConsentApi apiInstance = new ConsentApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    HIPConsentNotificationResponse hiPConsentNotificationResponse = new HIPConsentNotificationResponse(); // HIPConsentNotificationResponse | 
    try {
      apiInstance.v05ConsentsHipOnNotifyPost(authorization, hiPConsentNotificationResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentApi#v05ConsentsHipOnNotifyPost");
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

<a id="v05ConsentsHiuOnNotifyPost"></a>
# **v05ConsentsHiuOnNotifyPost**
> v05ConsentsHiuOnNotifyPost(authorization, hiUConsentNotificationResponse)

Consent notification

This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED, notified by CM earlier via Gateway API - ***_/v0.5/consents/hiu/notify***. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    ConsentApi apiInstance = new ConsentApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    HIUConsentNotificationResponse hiUConsentNotificationResponse = new HIUConsentNotificationResponse(); // HIUConsentNotificationResponse | 
    try {
      apiInstance.v05ConsentsHiuOnNotifyPost(authorization, hiUConsentNotificationResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsentApi#v05ConsentsHiuOnNotifyPost");
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


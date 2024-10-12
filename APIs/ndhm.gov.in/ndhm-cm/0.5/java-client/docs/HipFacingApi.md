# HipFacingApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05UsersAuthFetchModesPost_0**](HipFacingApi.md#v05UsersAuthFetchModesPost_0) | **POST** /v0.5/users/auth/fetch-modes | Get a patient&#39;s authentication modes relevant to specified purpose |
| [**v05UsersAuthOnNotifyPost_0**](HipFacingApi.md#v05UsersAuthOnNotifyPost_0) | **POST** /v0.5/users/auth/on-notify | callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth) |


<a id="v05UsersAuthFetchModesPost_0"></a>
# **v05UsersAuthFetchModesPost_0**
> v05UsersAuthFetchModesPost_0(authorization, patientAuthModeQueryRequest)

Get a patient&#39;s authentication modes relevant to specified purpose

This API is meant for identify supported authentication modes for a patient given a specific purpose 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HipFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    HipFacingApi apiInstance = new HipFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    PatientAuthModeQueryRequest patientAuthModeQueryRequest = new PatientAuthModeQueryRequest(); // PatientAuthModeQueryRequest | 
    try {
      apiInstance.v05UsersAuthFetchModesPost_0(authorization, patientAuthModeQueryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling HipFacingApi#v05UsersAuthFetchModesPost_0");
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

<a id="v05UsersAuthOnNotifyPost_0"></a>
# **v05UsersAuthOnNotifyPost_0**
> v05UsersAuthOnNotifyPost_0(authorization, patientAuthNotificationAcknowledgement)

callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)

This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HipFacingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    HipFacingApi apiInstance = new HipFacingApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    PatientAuthNotificationAcknowledgement patientAuthNotificationAcknowledgement = new PatientAuthNotificationAcknowledgement(); // PatientAuthNotificationAcknowledgement | 
    try {
      apiInstance.v05UsersAuthOnNotifyPost_0(authorization, patientAuthNotificationAcknowledgement);
    } catch (ApiException e) {
      System.err.println("Exception when calling HipFacingApi#v05UsersAuthOnNotifyPost_0");
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


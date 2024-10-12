# PatientNotificationApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05PatientsSmsNotifyPost_0**](PatientNotificationApi.md#v05PatientsSmsNotifyPost_0) | **POST** /v0.5/patients/sms/notify | API for HIP to send SMS notifications to patients |
| [**v05PatientsSmsOnNotifyPost_0**](PatientNotificationApi.md#v05PatientsSmsOnNotifyPost_0) | **POST** /v0.5/patients/sms/on-notify | Acknowledgment response for SMS notification sent to patient by HIP |


<a id="v05PatientsSmsNotifyPost_0"></a>
# **v05PatientsSmsNotifyPost_0**
> v05PatientsSmsNotifyPost_0(authorization, X_CM_ID, patientSMSNotifcationRequest)

API for HIP to send SMS notifications to patients

API to send SMS notifications to patient with custom deeplink. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientNotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    PatientNotificationApi apiInstance = new PatientNotificationApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientSMSNotifcationRequest patientSMSNotifcationRequest = new PatientSMSNotifcationRequest(); // PatientSMSNotifcationRequest | 
    try {
      apiInstance.v05PatientsSmsNotifyPost_0(authorization, X_CM_ID, patientSMSNotifcationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientNotificationApi#v05PatientsSmsNotifyPost_0");
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
| **patientSMSNotifcationRequest** | [**PatientSMSNotifcationRequest**](PatientSMSNotifcationRequest.md)|  | |

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
| **202** | accepted |  -  |
| **400** | **Causes:**   * required information not provided  |  -  |
| **401** | **Causes:**   * Unauthorized request  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05PatientsSmsOnNotifyPost_0"></a>
# **v05PatientsSmsOnNotifyPost_0**
> v05PatientsSmsOnNotifyPost_0(authorization, X_HIP_ID, patientSMSNotifcationResponse)

Acknowledgment response for SMS notification sent to patient by HIP

If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientNotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    PatientNotificationApi apiInstance = new PatientNotificationApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    PatientSMSNotifcationResponse patientSMSNotifcationResponse = new PatientSMSNotifcationResponse(); // PatientSMSNotifcationResponse | 
    try {
      apiInstance.v05PatientsSmsOnNotifyPost_0(authorization, X_HIP_ID, patientSMSNotifcationResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientNotificationApi#v05PatientsSmsOnNotifyPost_0");
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
| **patientSMSNotifcationResponse** | [**PatientSMSNotifcationResponse**](PatientSMSNotifcationResponse.md)|  | |

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


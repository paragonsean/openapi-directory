# DataFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05HealthInformationNotifyPost**](DataFlowApi.md#v05HealthInformationNotifyPost) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow |
| [**v05HealthInformationOnRequestPost**](DataFlowApi.md#v05HealthInformationOnRequestPost) | **POST** /v0.5/health-information/on-request | Health information data request acknowledgement from HIP |
| [**v05HealthInformationRequestPost**](DataFlowApi.md#v05HealthInformationRequestPost) | **POST** /v0.5/health-information/request | Health information data request from HIU |


<a id="v05HealthInformationNotifyPost"></a>
# **v05HealthInformationNotifyPost**
> v05HealthInformationNotifyPost(authorization, healthInformationNotification)

Notifications corresponding to events during data flow

API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    HealthInformationNotification healthInformationNotification = new HealthInformationNotification(); // HealthInformationNotification | 
    try {
      apiInstance.v05HealthInformationNotifyPost(authorization, healthInformationNotification);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationNotifyPost");
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

<a id="v05HealthInformationOnRequestPost"></a>
# **v05HealthInformationOnRequestPost**
> v05HealthInformationOnRequestPost(authorization, hiPHealthInformationRequestAcknowledgement)

Health information data request acknowledgement from HIP

This API is called by HIP to acknowledge Health information request receipt. When HIU requests health information, CM generates a transactionId and makes a health information request to the HIP(s). HIPs acknowledgement to the health-information request is coveyed by this API. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged.   

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    HIPHealthInformationRequestAcknowledgement hiPHealthInformationRequestAcknowledgement = new HIPHealthInformationRequestAcknowledgement(); // HIPHealthInformationRequestAcknowledgement | 
    try {
      apiInstance.v05HealthInformationOnRequestPost(authorization, hiPHealthInformationRequestAcknowledgement);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationOnRequestPost");
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
| **hiPHealthInformationRequestAcknowledgement** | [**HIPHealthInformationRequestAcknowledgement**](HIPHealthInformationRequestAcknowledgement.md)|  | |

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
| **202** | Request accepted. |  -  |
| **400** | **Causes:**   * Bad request  |  -  |
| **401** | **Causes:**   * Token is invalid or Link has expired  |  -  |
| **500** | **Causes:**   * Downstream system(s) is down.   * Unhandled exceptions.  |  -  |

<a id="v05HealthInformationRequestPost"></a>
# **v05HealthInformationRequestPost**
> v05HealthInformationRequestPost(authorization, hiRequest)

Health information data request from HIU

HIU request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via Gateway API - ***_/v0.5/health-information/cm/on-request***.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    HIRequest hiRequest = new HIRequest(); // HIRequest | 
    try {
      apiInstance.v05HealthInformationRequestPost(authorization, hiRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationRequestPost");
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


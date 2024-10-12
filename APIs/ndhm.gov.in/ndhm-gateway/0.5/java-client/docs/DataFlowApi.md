# DataFlowApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05HealthInformationCmOnRequestPost**](DataFlowApi.md#v05HealthInformationCmOnRequestPost) | **POST** /v0.5/health-information/cm/on-request | Health information data request |
| [**v05HealthInformationCmRequestPost**](DataFlowApi.md#v05HealthInformationCmRequestPost) | **POST** /v0.5/health-information/cm/request | Health information data request |
| [**v05HealthInformationHipOnRequestPost**](DataFlowApi.md#v05HealthInformationHipOnRequestPost) | **POST** /v0.5/health-information/hip/on-request | Health information data request |
| [**v05HealthInformationHipRequestPost**](DataFlowApi.md#v05HealthInformationHipRequestPost) | **POST** /v0.5/health-information/hip/request | Health information data request |
| [**v05HealthInformationNotifyPost**](DataFlowApi.md#v05HealthInformationNotifyPost) | **POST** /v0.5/health-information/notify | Notifications corresponding to events during data flow |


<a id="v05HealthInformationCmOnRequestPost"></a>
# **v05HealthInformationCmOnRequestPost**
> v05HealthInformationCmOnRequestPost(authorization, X_HIU_ID, hiUHealthInformationRequestResponse)

Health information data request

Callback API for acknowledgement of Health information request of HIU. CM calls this API when it has validated the Health Information request given the consent id. Either the **hiRequest** or **error** would need to be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIU_ID = "X_HIU_ID_example"; // String | Identifier of the health information user to which the request was intended.
    HIUHealthInformationRequestResponse hiUHealthInformationRequestResponse = new HIUHealthInformationRequestResponse(); // HIUHealthInformationRequestResponse | 
    try {
      apiInstance.v05HealthInformationCmOnRequestPost(authorization, X_HIU_ID, hiUHealthInformationRequestResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationCmOnRequestPost");
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
| **hiUHealthInformationRequestResponse** | [**HIUHealthInformationRequestResponse**](HIUHealthInformationRequestResponse.md)|  | |

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

<a id="v05HealthInformationCmRequestPost"></a>
# **v05HealthInformationCmRequestPost**
> v05HealthInformationCmRequestPost(authorization, X_CM_ID, hiRequest)

Health information data request

Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIRequest hiRequest = new HIRequest(); // HIRequest | 
    try {
      apiInstance.v05HealthInformationCmRequestPost(authorization, X_CM_ID, hiRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationCmRequestPost");
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

<a id="v05HealthInformationHipOnRequestPost"></a>
# **v05HealthInformationHipOnRequestPost**
> v05HealthInformationHipOnRequestPost(authorization, X_CM_ID, hiPHealthInformationRequestAcknowledgement)

Health information data request

API called by HIP to acknowledge Health information request receipt. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged.   

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HIPHealthInformationRequestAcknowledgement hiPHealthInformationRequestAcknowledgement = new HIPHealthInformationRequestAcknowledgement(); // HIPHealthInformationRequestAcknowledgement | 
    try {
      apiInstance.v05HealthInformationHipOnRequestPost(authorization, X_CM_ID, hiPHealthInformationRequestAcknowledgement);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationHipOnRequestPost");
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

<a id="v05HealthInformationHipRequestPost"></a>
# **v05HealthInformationHipRequestPost**
> v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hiPHIRequest)

Health information data request

API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_HIP_ID = "X_HIP_ID_example"; // String | Identifier of the health information provider to which the request was intended.
    HIPHIRequest hiPHIRequest = new HIPHIRequest(); // HIPHIRequest | 
    try {
      apiInstance.v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hiPHIRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowApi#v05HealthInformationHipRequestPost");
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
| **hiPHIRequest** | [**HIPHIRequest**](HIPHIRequest.md)|  | |

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

<a id="v05HealthInformationNotifyPost"></a>
# **v05HealthInformationNotifyPost**
> v05HealthInformationNotifyPost(authorization, X_CM_ID, healthInformationNotification)

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    DataFlowApi apiInstance = new DataFlowApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    HealthInformationNotification healthInformationNotification = new HealthInformationNotification(); // HealthInformationNotification | 
    try {
      apiInstance.v05HealthInformationNotifyPost(authorization, X_CM_ID, healthInformationNotification);
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


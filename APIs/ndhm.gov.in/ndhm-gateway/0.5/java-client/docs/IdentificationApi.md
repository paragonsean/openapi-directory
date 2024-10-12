# IdentificationApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05PatientsFindPost**](IdentificationApi.md#v05PatientsFindPost) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id |
| [**v05PatientsOnFindPost**](IdentificationApi.md#v05PatientsOnFindPost) | **POST** /v0.5/patients/on-find | Identification result for a consent-manager user-id |


<a id="v05PatientsFindPost"></a>
# **v05PatientsFindPost**
> v05PatientsFindPost(authorization, X_CM_ID, patientIdentificationRequest)

Identify a patient by her consent-manager user-id

This API is meant for identify to patient given her consent-manager-user-id 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    IdentificationApi apiInstance = new IdentificationApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    String X_CM_ID = "X_CM_ID_example"; // String | Suffix of the consent manager to which the request was intended.
    PatientIdentificationRequest patientIdentificationRequest = new PatientIdentificationRequest(); // PatientIdentificationRequest | 
    try {
      apiInstance.v05PatientsFindPost(authorization, X_CM_ID, patientIdentificationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentificationApi#v05PatientsFindPost");
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

<a id="v05PatientsOnFindPost"></a>
# **v05PatientsOnFindPost**
> v05PatientsOnFindPost(authorization, patientIdentificationResponse)

Identification result for a consent-manager user-id

If a patient is found then patient.name contains the patients name.  Otherwise, patient is not provided, and possibly error is raised for invalid requests Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. specify **X-HIU-ID** if the requester is HIU (identified from /find requester.id) 2. specify **X-HIP-ID** if the requester is HIP (identified from /find requester.id) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.ndhm.gov.in/gateway");

    IdentificationApi apiInstance = new IdentificationApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    PatientIdentificationResponse patientIdentificationResponse = new PatientIdentificationResponse(); // PatientIdentificationResponse | 
    try {
      apiInstance.v05PatientsOnFindPost(authorization, patientIdentificationResponse);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentificationApi#v05PatientsOnFindPost");
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
| **patientIdentificationResponse** | [**PatientIdentificationResponse**](PatientIdentificationResponse.md)|  | |

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


# IdentificationApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v05PatientsFindPost**](IdentificationApi.md#v05PatientsFindPost) | **POST** /v0.5/patients/find | Identify a patient by her consent-manager user-id |


<a id="v05PatientsFindPost"></a>
# **v05PatientsFindPost**
> v05PatientsFindPost(authorization, patientIdentificationRequest)

Identify a patient by her consent-manager user-id

This API is meant for identify to patient given her consent-manager-user-id. CM subsequently makes the /on-find Gateway API call with results.  

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
    defaultClient.setBasePath("https://dev.ndhm.gov.in/cm");

    IdentificationApi apiInstance = new IdentificationApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
    PatientIdentificationRequest patientIdentificationRequest = new PatientIdentificationRequest(); // PatientIdentificationRequest | 
    try {
      apiInstance.v05PatientsFindPost(authorization, patientIdentificationRequest);
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


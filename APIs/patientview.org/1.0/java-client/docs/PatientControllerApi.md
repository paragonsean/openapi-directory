# PatientControllerApi

All URIs are relative to *https://www.patientview.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBasicPatientDetails**](PatientControllerApi.md#getBasicPatientDetails) | **GET** /patient/{userId}/basic | Get Basic Patient Information |


<a id="getBasicPatientDetails"></a>
# **getBasicPatientDetails**
> List&lt;Patient&gt; getBasicPatientDetails(userId)

Get Basic Patient Information

Given a User ID, get basic patient information for a user from clinical data stored in FHIR

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    PatientControllerApi apiInstance = new PatientControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    try {
      List<Patient> result = apiInstance.getBasicPatientDetails(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientControllerApi#getBasicPatientDetails");
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
| **userId** | **Long**| userId | |

### Return type

[**List&lt;Patient&gt;**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |


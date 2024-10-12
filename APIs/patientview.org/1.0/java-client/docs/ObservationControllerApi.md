# ObservationControllerApi

All URIs are relative to *https://www.patientview.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getObservationsByCode**](ObservationControllerApi.md#getObservationsByCode) | **GET** /user/{userId}/observations/{code} | Get Observations of a Certain Type For a User |
| [**getObservationsByCodes**](ObservationControllerApi.md#getObservationsByCodes) | **GET** /user/{userId}/observations | Get Observations of Multiple Types For a User |
| [**getPatientEnteredObservationsByCode**](ObservationControllerApi.md#getPatientEnteredObservationsByCode) | **GET** /user/{userId}/observations/{code}/patiententered | Get patient entered Observations of a Certain Type For a User |


<a id="getObservationsByCode"></a>
# **getObservationsByCode**
> List&lt;FhirObservation&gt; getObservationsByCode(userId, code)

Get Observations of a Certain Type For a User

Given a User ID and observation code, retrieve all observations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObservationControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    ObservationControllerApi apiInstance = new ObservationControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    String code = "code_example"; // String | code
    try {
      List<FhirObservation> result = apiInstance.getObservationsByCode(userId, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservationControllerApi#getObservationsByCode");
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
| **code** | **String**| code | |

### Return type

[**List&lt;FhirObservation&gt;**](FhirObservation.md)

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

<a id="getObservationsByCodes"></a>
# **getObservationsByCodes**
> FhirObservationPage getObservationsByCodes(userId, code, limit, offset, orderDirection)

Get Observations of Multiple Types For a User

Given a User ID and search parameters, retrieve a page of observations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObservationControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    ObservationControllerApi apiInstance = new ObservationControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    List<String> code = Arrays.asList(); // List<String> | code
    Long limit = 56L; // Long | limit
    Long offset = 56L; // Long | offset
    String orderDirection = "orderDirection_example"; // String | orderDirection
    try {
      FhirObservationPage result = apiInstance.getObservationsByCodes(userId, code, limit, offset, orderDirection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservationControllerApi#getObservationsByCodes");
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
| **code** | [**List&lt;String&gt;**](String.md)| code | |
| **limit** | **Long**| limit | |
| **offset** | **Long**| offset | |
| **orderDirection** | **String**| orderDirection | |

### Return type

[**FhirObservationPage**](FhirObservationPage.md)

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

<a id="getPatientEnteredObservationsByCode"></a>
# **getPatientEnteredObservationsByCode**
> List&lt;FhirObservation&gt; getPatientEnteredObservationsByCode(userId, code)

Get patient entered Observations of a Certain Type For a User

Given a User ID and observation code, retrieve patient entered observations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObservationControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    ObservationControllerApi apiInstance = new ObservationControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    String code = "code_example"; // String | code
    try {
      List<FhirObservation> result = apiInstance.getPatientEnteredObservationsByCode(userId, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservationControllerApi#getPatientEnteredObservationsByCode");
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
| **code** | **String**| code | |

### Return type

[**List&lt;FhirObservation&gt;**](FhirObservation.md)

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


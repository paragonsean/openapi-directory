# ObservationHeadingControllerApi

All URIs are relative to *https://www.patientview.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAvailableObservationHeadings**](ObservationHeadingControllerApi.md#getAvailableObservationHeadings) | **GET** /user/{userId}/availableobservationheadings | Get Available Observations Types For a User |
| [**getPatientEnteredObservationHeadings**](ObservationHeadingControllerApi.md#getPatientEnteredObservationHeadings) | **GET** /user/{userId}/patiententeredobservationheadings | Get Available Patient Entered Observations Types For a User |


<a id="getAvailableObservationHeadings"></a>
# **getAvailableObservationHeadings**
> List&lt;ObservationHeading&gt; getAvailableObservationHeadings(userId)

Get Available Observations Types For a User

Given a User ID retrieve a list of available observation types for that user (where they have observation data).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObservationHeadingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    ObservationHeadingControllerApi apiInstance = new ObservationHeadingControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    try {
      List<ObservationHeading> result = apiInstance.getAvailableObservationHeadings(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservationHeadingControllerApi#getAvailableObservationHeadings");
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

[**List&lt;ObservationHeading&gt;**](ObservationHeading.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getPatientEnteredObservationHeadings"></a>
# **getPatientEnteredObservationHeadings**
> List&lt;ObservationHeading&gt; getPatientEnteredObservationHeadings(userId)

Get Available Patient Entered Observations Types For a User

Given a User ID retrieve a list of available observation types for that user (where they have patient entered observation data).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ObservationHeadingControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    ObservationHeadingControllerApi apiInstance = new ObservationHeadingControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    try {
      List<ObservationHeading> result = apiInstance.getPatientEnteredObservationHeadings(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ObservationHeadingControllerApi#getPatientEnteredObservationHeadings");
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

[**List&lt;ObservationHeading&gt;**](ObservationHeading.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |


# AeAssessmentApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAEAssessment**](AeAssessmentApi.md#deleteAEAssessment) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessment/{AEAssessmentId} | Delete auto enrolment assessment |
| [**getAEAssessmentFromEmployee**](AeAssessmentApi.md#getAEAssessmentFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessment/{AEAssessmentId} | Get the auto enrolment assessment |
| [**getAEAssessmentsFromEmployee**](AeAssessmentApi.md#getAEAssessmentsFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessments | Get the auto enrolment assessments |
| [**getAEAssessmentsFromPayRun**](AeAssessmentApi.md#getAEAssessmentsFromPayRun) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/AEAssessments | Get the auto enrolment assessments |
| [**postNewAEAssessment**](AeAssessmentApi.md#postNewAEAssessment) | **POST** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessments | Insert new auto enrolment assessment |
| [**putNewAEAssessment**](AeAssessmentApi.md#putNewAEAssessment) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessment/{AEAssessmentId} | Insert new auto enrolment assessment |


<a id="deleteAEAssessment"></a>
# **deleteAEAssessment**
> deleteAEAssessment(employerId, employeeId, aeAssessmentId, authorization, apiVersion)

Delete auto enrolment assessment

Deletes an existing auto enrolment assessment for the employee. Used to remove historical assessments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AeAssessmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    AeAssessmentApi apiInstance = new AeAssessmentApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String aeAssessmentId = "aeAssessmentId_example"; // String | The auto enrolment assessment unique identifier. E.g. AE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteAEAssessment(employerId, employeeId, aeAssessmentId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AeAssessmentApi#deleteAEAssessment");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | |
| **aeAssessmentId** | **String**| The auto enrolment assessment unique identifier. E.g. AE001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAEAssessmentFromEmployee"></a>
# **getAEAssessmentFromEmployee**
> AEAssessment getAEAssessmentFromEmployee(employerId, employeeId, aeAssessmentId, authorization, apiVersion)

Get the auto enrolment assessment

Gets the auto enrolment assessment from the specified employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AeAssessmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    AeAssessmentApi apiInstance = new AeAssessmentApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String aeAssessmentId = "aeAssessmentId_example"; // String | The auto enrolment assessment unique identifier. E.g. AE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      AEAssessment result = apiInstance.getAEAssessmentFromEmployee(employerId, employeeId, aeAssessmentId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AeAssessmentApi#getAEAssessmentFromEmployee");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | |
| **aeAssessmentId** | **String**| The auto enrolment assessment unique identifier. E.g. AE001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**AEAssessment**](AEAssessment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The a e assessment object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAEAssessmentsFromEmployee"></a>
# **getAEAssessmentsFromEmployee**
> LinkCollection getAEAssessmentsFromEmployee(employerId, employeeId, authorization, apiVersion)

Get the auto enrolment assessments

Gets all auto enrolment assessments from the specified employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AeAssessmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    AeAssessmentApi apiInstance = new AeAssessmentApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAEAssessmentsFromEmployee(employerId, employeeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AeAssessmentApi#getAEAssessmentsFromEmployee");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link collection object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getAEAssessmentsFromPayRun"></a>
# **getAEAssessmentsFromPayRun**
> LinkCollection getAEAssessmentsFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion)

Get the auto enrolment assessments

Gets all auto enrolment assessments from the specified pay run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AeAssessmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    AeAssessmentApi apiInstance = new AeAssessmentApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAEAssessmentsFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AeAssessmentApi#getAEAssessmentsFromPayRun");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **payScheduleId** | **String**| The pay schedules&#39; unique identifier. E.g SCH001 | |
| **payRunId** | **String**| The pay runs&#39; unique identifier. E.g. PR001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link collection object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postNewAEAssessment"></a>
# **postNewAEAssessment**
> Link postNewAEAssessment(employerId, employeeId, authorization, apiVersion, aeAssessment)

Insert new auto enrolment assessment

Creates a new auto enrolment assessment for the employee. Used to insert historical assessments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AeAssessmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    AeAssessmentApi apiInstance = new AeAssessmentApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    AEAssessment aeAssessment = new AEAssessment(); // AEAssessment | The auto enrolment assessment object.
    try {
      Link result = apiInstance.postNewAEAssessment(employerId, employeeId, authorization, apiVersion, aeAssessment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AeAssessmentApi#postNewAEAssessment");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **aeAssessment** | [**AEAssessment**](AEAssessment.md)| The auto enrolment assessment object. | |

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The link object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putNewAEAssessment"></a>
# **putNewAEAssessment**
> AEAssessment putNewAEAssessment(employerId, employeeId, aeAssessmentId, authorization, apiVersion, aeAssessment)

Insert new auto enrolment assessment

Creates a new auto enrolment assessment for the employee. Used to insert historical assessments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AeAssessmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    AeAssessmentApi apiInstance = new AeAssessmentApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String aeAssessmentId = "aeAssessmentId_example"; // String | The auto enrolment assessment unique identifier. E.g. AE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    AEAssessment aeAssessment = new AEAssessment(); // AEAssessment | The auto enrolment assessment object.
    try {
      AEAssessment result = apiInstance.putNewAEAssessment(employerId, employeeId, aeAssessmentId, authorization, apiVersion, aeAssessment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AeAssessmentApi#putNewAEAssessment");
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
| **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | |
| **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | |
| **aeAssessmentId** | **String**| The auto enrolment assessment unique identifier. E.g. AE001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **aeAssessment** | [**AEAssessment**](AEAssessment.md)| The auto enrolment assessment object. | |

### Return type

[**AEAssessment**](AEAssessment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The a e assessment object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |


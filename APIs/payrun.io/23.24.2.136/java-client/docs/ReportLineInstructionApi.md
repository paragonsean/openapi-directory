# ReportLineInstructionApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteReportingInstruction**](ReportLineInstructionApi.md#deleteReportingInstruction) | **DELETE** /Employer/{EmployerId}/ReportingInstruction/{ReportingInstructionId} | Deletes a reporting instruction |
| [**getReportingInstructionFromEmployer**](ReportLineInstructionApi.md#getReportingInstructionFromEmployer) | **GET** /Employer/{EmployerId}/ReportingInstruction/{ReportingInstructionId} | Gets the specified reporting instruction from the employer |
| [**getReportingInstructionsFromEmployer**](ReportLineInstructionApi.md#getReportingInstructionsFromEmployer) | **GET** /Employer/{EmployerId}/ReportingInstructions | Gets the reporting instructions from the specified employer |
| [**postReportingInstruction**](ReportLineInstructionApi.md#postReportingInstruction) | **POST** /Employer/{EmployerId}/ReportingInstructions | Creates a new Reporting Instruction |
| [**putReportingInstruction**](ReportLineInstructionApi.md#putReportingInstruction) | **PUT** /Employer/{EmployerId}/ReportingInstruction/{ReportingInstructionId} | Update a reporting Instruction |


<a id="deleteReportingInstruction"></a>
# **deleteReportingInstruction**
> deleteReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion)

Deletes a reporting instruction

Delete the specified reporting instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportLineInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportLineInstructionApi apiInstance = new ReportLineInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String reportingInstructionId = "reportingInstructionId_example"; // String | The reporting instruction unique identifier. E.g. SERRPT001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportLineInstructionApi#deleteReportingInstruction");
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
| **reportingInstructionId** | **String**| The reporting instruction unique identifier. E.g. SERRPT001 | |
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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getReportingInstructionFromEmployer"></a>
# **getReportingInstructionFromEmployer**
> ReportingInstruction getReportingInstructionFromEmployer(employerId, reportingInstructionId, authorization, apiVersion)

Gets the specified reporting instruction from the employer

Returns the specified pay instruction from employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportLineInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportLineInstructionApi apiInstance = new ReportLineInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String reportingInstructionId = "reportingInstructionId_example"; // String | The reporting instruction unique identifier. E.g. SERRPT001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      ReportingInstruction result = apiInstance.getReportingInstructionFromEmployer(employerId, reportingInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportLineInstructionApi#getReportingInstructionFromEmployer");
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
| **reportingInstructionId** | **String**| The reporting instruction unique identifier. E.g. SERRPT001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**ReportingInstruction**](ReportingInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reporting instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getReportingInstructionsFromEmployer"></a>
# **getReportingInstructionsFromEmployer**
> LinkCollection getReportingInstructionsFromEmployer(employerId, authorization, apiVersion)

Gets the reporting instructions from the specified employer

Get links to all pay instructions for the specified employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportLineInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportLineInstructionApi apiInstance = new ReportLineInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getReportingInstructionsFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportLineInstructionApi#getReportingInstructionsFromEmployer");
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

<a id="postReportingInstruction"></a>
# **postReportingInstruction**
> Link postReportingInstruction(employerId, authorization, apiVersion, reportingInstruction)

Creates a new Reporting Instruction

Creates a new reporting instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportLineInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportLineInstructionApi apiInstance = new ReportLineInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    ReportingInstruction reportingInstruction = new ReportingInstruction(); // ReportingInstruction | The reporting instruction object.
    try {
      Link result = apiInstance.postReportingInstruction(employerId, authorization, apiVersion, reportingInstruction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportLineInstructionApi#postReportingInstruction");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **reportingInstruction** | [**ReportingInstruction**](ReportingInstruction.md)| The reporting instruction object. | |

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
| **201** | The link object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putReportingInstruction"></a>
# **putReportingInstruction**
> ReportingInstruction putReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion, reportingInstruction)

Update a reporting Instruction

Updates the existing specified reporting instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportLineInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    ReportLineInstructionApi apiInstance = new ReportLineInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String reportingInstructionId = "reportingInstructionId_example"; // String | The reporting instruction unique identifier. E.g. SERRPT001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    ReportingInstruction reportingInstruction = new ReportingInstruction(); // ReportingInstruction | The reporting instruction object.
    try {
      ReportingInstruction result = apiInstance.putReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion, reportingInstruction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportLineInstructionApi#putReportingInstruction");
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
| **reportingInstructionId** | **String**| The reporting instruction unique identifier. E.g. SERRPT001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **reportingInstruction** | [**ReportingInstruction**](ReportingInstruction.md)| The reporting instruction object. | |

### Return type

[**ReportingInstruction**](ReportingInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reporting instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |


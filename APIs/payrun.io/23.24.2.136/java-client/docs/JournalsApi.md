# JournalsApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteJournalInstruction**](JournalsApi.md#deleteJournalInstruction) | **DELETE** /Employer/{EmployerId}/JournalInstruction/{JournalInstructionId} | Deletes a Journal instruction |
| [**deleteJournalInstructionTemplate**](JournalsApi.md#deleteJournalInstructionTemplate) | **DELETE** /JournalInstruction/{JournalInstructionId} | Deletes a Journal instruction template |
| [**getJournalInstructionFromEmployer**](JournalsApi.md#getJournalInstructionFromEmployer) | **GET** /Employer/{EmployerId}/JournalInstruction/{JournalInstructionId} | Gets the specified journal instruction from the employer |
| [**getJournalInstructionTemplate**](JournalsApi.md#getJournalInstructionTemplate) | **GET** /JournalInstruction/{JournalInstructionId} | Gets the Journal instructions template for the application |
| [**getJournalInstructionTemplates**](JournalsApi.md#getJournalInstructionTemplates) | **GET** /JournalInstructions | Gets the Journal instructions templates for the application |
| [**getJournalInstructionsFromEmployer**](JournalsApi.md#getJournalInstructionsFromEmployer) | **GET** /Employer/{EmployerId}/JournalInstructions | Gets the Journal instructions from the specified employer |
| [**getJournalLineFromEmployer**](JournalsApi.md#getJournalLineFromEmployer) | **GET** /Employer/{EmployerId}/JournalLine/{JournalLineId} | Gets the specified journal Line from the employer |
| [**getJournalLinesFromEmployee**](JournalsApi.md#getJournalLinesFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/JournalLines | Gets the journal Lines from the specified employee |
| [**getJournalLinesFromEmployer**](JournalsApi.md#getJournalLinesFromEmployer) | **GET** /Employer/{EmployerId}/JournalLines | Gets the Journal Lines from the specified employer |
| [**getJournalLinesFromPayRun**](JournalsApi.md#getJournalLinesFromPayRun) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/JournalLines | Gets the journal Lines from the specified pay run |
| [**getJournalLinesFromSubContractor**](JournalsApi.md#getJournalLinesFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/JournalLines | Gets the journal Lines from the specified sub contractor |
| [**postJournalInstruction**](JournalsApi.md#postJournalInstruction) | **POST** /Employer/{EmployerId}/JournalInstructions | Creates a new Journal Instruction |
| [**postJournalInstructionTemplate**](JournalsApi.md#postJournalInstructionTemplate) | **POST** /JournalInstructions | Creates a new Journal Instruction template |
| [**putJournalInstruction**](JournalsApi.md#putJournalInstruction) | **PUT** /Employer/{EmployerId}/JournalInstruction/{JournalInstructionId} | Update a Journal Instruction |
| [**putJournalInstructionTemplate**](JournalsApi.md#putJournalInstructionTemplate) | **PUT** /JournalInstruction/{JournalInstructionId} | Update a Journal Instruction template |


<a id="deleteJournalInstruction"></a>
# **deleteJournalInstruction**
> deleteJournalInstruction(employerId, journalInstructionId, authorization, apiVersion)

Deletes a Journal instruction

Delete the specified Journal instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteJournalInstruction(employerId, journalInstructionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#deleteJournalInstruction");
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
| **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | |
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

<a id="deleteJournalInstructionTemplate"></a>
# **deleteJournalInstructionTemplate**
> deleteJournalInstructionTemplate(journalInstructionId, authorization, apiVersion)

Deletes a Journal instruction template

Delete the specified Journal instruction template object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteJournalInstructionTemplate(journalInstructionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#deleteJournalInstructionTemplate");
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
| **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | |
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

<a id="getJournalInstructionFromEmployer"></a>
# **getJournalInstructionFromEmployer**
> JournalInstruction getJournalInstructionFromEmployer(employerId, journalInstructionId, authorization, apiVersion)

Gets the specified journal instruction from the employer

Returns the specified journal instruction from employer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      JournalInstruction result = apiInstance.getJournalInstructionFromEmployer(employerId, journalInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalInstructionFromEmployer");
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
| **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The journal instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getJournalInstructionTemplate"></a>
# **getJournalInstructionTemplate**
> JournalInstruction getJournalInstructionTemplate(journalInstructionId, authorization, apiVersion)

Gets the Journal instructions template for the application

Retrurns the specified journal instruction from the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      JournalInstruction result = apiInstance.getJournalInstructionTemplate(journalInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalInstructionTemplate");
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
| **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The journal instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getJournalInstructionTemplates"></a>
# **getJournalInstructionTemplates**
> LinkCollection getJournalInstructionTemplates(authorization, apiVersion)

Gets the Journal instructions templates for the application

Get links to all journal instruction templates for the application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getJournalInstructionTemplates(authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalInstructionTemplates");
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

<a id="getJournalInstructionsFromEmployer"></a>
# **getJournalInstructionsFromEmployer**
> LinkCollection getJournalInstructionsFromEmployer(employerId, authorization, apiVersion)

Gets the Journal instructions from the specified employer

Get links to all journal instructions for the specified employer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getJournalInstructionsFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalInstructionsFromEmployer");
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

<a id="getJournalLineFromEmployer"></a>
# **getJournalLineFromEmployer**
> JournalLine getJournalLineFromEmployer(employerId, journalLineId, authorization, apiVersion)

Gets the specified journal Line from the employer

Returns the specified journal Line from employer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      JournalLine result = apiInstance.getJournalLineFromEmployer(employerId, journalLineId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalLineFromEmployer");
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
| **journalLineId** | **String**| The journal line unique identifier. E.g JL001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**JournalLine**](JournalLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The journal line object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getJournalLinesFromEmployee"></a>
# **getJournalLinesFromEmployee**
> LinkCollection getJournalLinesFromEmployee(employerId, employeeId, authorization, apiVersion)

Gets the journal Lines from the specified employee

Get links to all journal lines for the specified employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getJournalLinesFromEmployee(employerId, employeeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalLinesFromEmployee");
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

<a id="getJournalLinesFromEmployer"></a>
# **getJournalLinesFromEmployer**
> LinkCollection getJournalLinesFromEmployer(employerId, authorization, apiVersion)

Gets the Journal Lines from the specified employer

Get links to all journal Lines for the specified employer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getJournalLinesFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalLinesFromEmployer");
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

<a id="getJournalLinesFromPayRun"></a>
# **getJournalLinesFromPayRun**
> LinkCollection getJournalLinesFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion)

Gets the journal Lines from the specified pay run

Get links to all journal lines for the specified pay run

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getJournalLinesFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalLinesFromPayRun");
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

<a id="getJournalLinesFromSubContractor"></a>
# **getJournalLinesFromSubContractor**
> LinkCollection getJournalLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion)

Gets the journal Lines from the specified sub contractor

Get links to all journal lines for the specified sub contractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getJournalLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalLinesFromSubContractor");
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
| **subContractorId** | **String**| The sub contractors&#39; unique identifier. E.g SUB001 | |
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

<a id="postJournalInstruction"></a>
# **postJournalInstruction**
> Link postJournalInstruction(employerId, authorization, apiVersion)

Creates a new Journal Instruction

Creates a new Journal instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Link result = apiInstance.postJournalInstruction(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#postJournalInstruction");
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

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The link object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postJournalInstructionTemplate"></a>
# **postJournalInstructionTemplate**
> Link postJournalInstructionTemplate(authorization, apiVersion)

Creates a new Journal Instruction template

Creates a new Journal instruction teamplte object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Link result = apiInstance.postJournalInstructionTemplate(authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#postJournalInstructionTemplate");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The link object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putJournalInstruction"></a>
# **putJournalInstruction**
> JournalInstruction putJournalInstruction(employerId, journalInstructionId, authorization, apiVersion)

Update a Journal Instruction

Updates the existing specified Journal instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      JournalInstruction result = apiInstance.putJournalInstruction(employerId, journalInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#putJournalInstruction");
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
| **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The journal instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putJournalInstructionTemplate"></a>
# **putJournalInstructionTemplate**
> JournalInstruction putJournalInstructionTemplate(journalInstructionId, authorization, apiVersion)

Update a Journal Instruction template

Updates the existing specified Journal instruction template object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      JournalInstruction result = apiInstance.putJournalInstructionTemplate(journalInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#putJournalInstructionTemplate");
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
| **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The journal instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |


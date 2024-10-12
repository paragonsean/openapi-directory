# PayScheduleApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePaySchedule**](PayScheduleApi.md#deletePaySchedule) | **DELETE** /Employer/{EmployerId}/PaySchedule/{PayScheduleId} | Deletes a pay schedule |
| [**getAllPayScheduleTags_0**](PayScheduleApi.md#getAllPayScheduleTags_0) | **GET** /Employer/{EmployerId}/PaySchedules/Tags | Get all pay schedule tags |
| [**getEmployeesFromPayScheduleOnEffectiveDate_0**](PayScheduleApi.md#getEmployeesFromPayScheduleOnEffectiveDate_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Employees/{EffectiveDate} | Get employees from a pay schedule on effective date. |
| [**getEmployeesFromPaySchedule_0**](PayScheduleApi.md#getEmployeesFromPaySchedule_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Employees | Get all employees revisions from a pay schedule. |
| [**getPayRunFromPaySchedule_0**](PayScheduleApi.md#getPayRunFromPaySchedule_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId} | Gets the pay run from the pay schedule |
| [**getPayRunsFromPaySchedule_0**](PayScheduleApi.md#getPayRunsFromPaySchedule_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRuns | Gets the pay runs from the pay schedule |
| [**getPayScheduleFromEmployer**](PayScheduleApi.md#getPayScheduleFromEmployer) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId} | Gets the specified pay schedule from the employer |
| [**getPaySchedulesFromEmployer**](PayScheduleApi.md#getPaySchedulesFromEmployer) | **GET** /Employer/{EmployerId}/PaySchedules | Gets the pay schedule from the specified employer |
| [**getPaySchedulesWithTag_0**](PayScheduleApi.md#getPaySchedulesWithTag_0) | **GET** /Employer/{EmployerId}/PaySchedules/Tag/{TagId} | Get pay schedule with tag |
| [**postPaySchedule**](PayScheduleApi.md#postPaySchedule) | **POST** /Employer/{EmployerId}/PaySchedules | Create a new pay schedule |
| [**putPaySchedule**](PayScheduleApi.md#putPaySchedule) | **PUT** /Employer/{EmployerId}/PaySchedule/{PayScheduleId} | Updates a pay schedule |


<a id="deletePaySchedule"></a>
# **deletePaySchedule**
> deletePaySchedule(employerId, payScheduleId, authorization, apiVersion)

Deletes a pay schedule

Delete the specified pay schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deletePaySchedule(employerId, payScheduleId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#deletePaySchedule");
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

<a id="getAllPayScheduleTags_0"></a>
# **getAllPayScheduleTags_0**
> LinkCollection getAllPayScheduleTags_0(employerId, authorization, apiVersion)

Get all pay schedule tags

Gets all the pay schedule tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAllPayScheduleTags_0(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getAllPayScheduleTags_0");
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

<a id="getEmployeesFromPayScheduleOnEffectiveDate_0"></a>
# **getEmployeesFromPayScheduleOnEffectiveDate_0**
> LinkCollection getEmployeesFromPayScheduleOnEffectiveDate_0(employerId, payScheduleId, effectiveDate, authorization, apiVersion)

Get employees from a pay schedule on effective date.

Gets links to all employee revisions in the specified pay schedule for the given effective date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getEmployeesFromPayScheduleOnEffectiveDate_0(employerId, payScheduleId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getEmployeesFromPayScheduleOnEffectiveDate_0");
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
| **effectiveDate** | **LocalDate**| The effective date to be applied. E.g 2016-04-06 | |
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

<a id="getEmployeesFromPaySchedule_0"></a>
# **getEmployeesFromPaySchedule_0**
> LinkCollection getEmployeesFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion)

Get all employees revisions from a pay schedule.

Gets links to all employee revisions that have ever existed in the specified pay schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getEmployeesFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getEmployeesFromPaySchedule_0");
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

<a id="getPayRunFromPaySchedule_0"></a>
# **getPayRunFromPaySchedule_0**
> PayRun getPayRunFromPaySchedule_0(employerId, payScheduleId, payRunId, authorization, apiVersion)

Gets the pay run from the pay schedule

Returns the pay run from the pay schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      PayRun result = apiInstance.getPayRunFromPaySchedule_0(employerId, payScheduleId, payRunId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getPayRunFromPaySchedule_0");
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

[**PayRun**](PayRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pay run object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPayRunsFromPaySchedule_0"></a>
# **getPayRunsFromPaySchedule_0**
> LinkCollection getPayRunsFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion)

Gets the pay runs from the pay schedule

Get links to all pay runs for the specified pay schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getPayRunsFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getPayRunsFromPaySchedule_0");
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

<a id="getPayScheduleFromEmployer"></a>
# **getPayScheduleFromEmployer**
> PaySchedule getPayScheduleFromEmployer(employerId, payScheduleId, authorization, apiVersion)

Gets the specified pay schedule from the employer

Returns the specified pay schedule object from employer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      PaySchedule result = apiInstance.getPayScheduleFromEmployer(employerId, payScheduleId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getPayScheduleFromEmployer");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**PaySchedule**](PaySchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pay schedule object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPaySchedulesFromEmployer"></a>
# **getPaySchedulesFromEmployer**
> LinkCollection getPaySchedulesFromEmployer(employerId, authorization, apiVersion)

Gets the pay schedule from the specified employer

Get links to all pay schedules for the specified employer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getPaySchedulesFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getPaySchedulesFromEmployer");
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

<a id="getPaySchedulesWithTag_0"></a>
# **getPaySchedulesWithTag_0**
> LinkCollection getPaySchedulesWithTag_0(employerId, tagId, authorization, apiVersion)

Get pay schedule with tag

Gets the pay schedules with the tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getPaySchedulesWithTag_0(employerId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#getPaySchedulesWithTag_0");
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
| **tagId** | **String**| The tag unique identifier. E.g. MyTag | |
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

<a id="postPaySchedule"></a>
# **postPaySchedule**
> Link postPaySchedule(employerId, authorization, apiVersion, paySchedule)

Create a new pay schedule

Create a new pay schedule object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    PaySchedule paySchedule = new PaySchedule(); // PaySchedule | The pay schedule object.
    try {
      Link result = apiInstance.postPaySchedule(employerId, authorization, apiVersion, paySchedule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#postPaySchedule");
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
| **paySchedule** | [**PaySchedule**](PaySchedule.md)| The pay schedule object. | |

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

<a id="putPaySchedule"></a>
# **putPaySchedule**
> PaySchedule putPaySchedule(employerId, payScheduleId, authorization, apiVersion, paySchedule)

Updates a pay schedule

Updates the existing specified pay schedule object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayScheduleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayScheduleApi apiInstance = new PayScheduleApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    PaySchedule paySchedule = new PaySchedule(); // PaySchedule | The pay schedule object.
    try {
      PaySchedule result = apiInstance.putPaySchedule(employerId, payScheduleId, authorization, apiVersion, paySchedule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayScheduleApi#putPaySchedule");
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
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **paySchedule** | [**PaySchedule**](PaySchedule.md)| The pay schedule object. | |

### Return type

[**PaySchedule**](PaySchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pay schedule object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |


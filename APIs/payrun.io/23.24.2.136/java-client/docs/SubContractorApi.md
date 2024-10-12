# SubContractorApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSubContractor**](SubContractorApi.md#deleteSubContractor) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Delete an sub contractor |
| [**deleteSubContractorRevision**](SubContractorApi.md#deleteSubContractorRevision) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/{EffectiveDate} | Delete an sub contractor revision matching the specified revision date. |
| [**deleteSubContractorRevisionByNumber**](SubContractorApi.md#deleteSubContractorRevisionByNumber) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Revision/{RevisionNumber} | Delete an SubContractor revision matching the specified revision number. |
| [**getSubContractorByEffectiveDate**](SubContractorApi.md#getSubContractorByEffectiveDate) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/{EffectiveDate} | Get sub contractor by effective date. |
| [**getSubContractorFromEmployer**](SubContractorApi.md#getSubContractorFromEmployer) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Get sub contractor from employer |
| [**getSubContractorRevisionByNumber**](SubContractorApi.md#getSubContractorRevisionByNumber) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Revision/{RevisionNumber} | Gets the sub contractor by revision number |
| [**getSubContractorRevisions**](SubContractorApi.md#getSubContractorRevisions) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Revisions | Get all sub contractor revisions |
| [**getSubContractorsByEffectiveDate**](SubContractorApi.md#getSubContractorsByEffectiveDate) | **GET** /Employer/{EmployerId}/SubContractors/{EffectiveDate} | Get sub contractors from employer at a given effective date. |
| [**getSubContractorsFromEmployer**](SubContractorApi.md#getSubContractorsFromEmployer) | **GET** /Employer/{EmployerId}/SubContractors | Get sub contractors from employer. |
| [**patchSubContractor**](SubContractorApi.md#patchSubContractor) | **PATCH** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Patches the sub contractor |
| [**postSubContractorIntoEmployer**](SubContractorApi.md#postSubContractorIntoEmployer) | **POST** /Employer/{EmployerId}/SubContractors | Create a new sub contractor |
| [**putSubContractorIntoEmployer**](SubContractorApi.md#putSubContractorIntoEmployer) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Updates the sub contractor |


<a id="deleteSubContractor"></a>
# **deleteSubContractor**
> deleteSubContractor(employerId, subContractorId, authorization, apiVersion)

Delete an sub contractor

Delete the specified sub contractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteSubContractor(employerId, subContractorId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#deleteSubContractor");
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

<a id="deleteSubContractorRevision"></a>
# **deleteSubContractorRevision**
> deleteSubContractorRevision(employerId, subContractorId, effectiveDate, authorization, apiVersion)

Delete an sub contractor revision matching the specified revision date.

Deletes the specified sub contractor revision for the matching revision date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteSubContractorRevision(employerId, subContractorId, effectiveDate, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#deleteSubContractorRevision");
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
| **effectiveDate** | **LocalDate**| The effective date to be applied. E.g 2016-04-06 | |
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

<a id="deleteSubContractorRevisionByNumber"></a>
# **deleteSubContractorRevisionByNumber**
> deleteSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion)

Delete an SubContractor revision matching the specified revision number.

Deletes the specified sub contractor revision for the matching revision number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#deleteSubContractorRevisionByNumber");
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
| **revisionNumber** | **String**| The revision number. E.g. 1 | |
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

<a id="getSubContractorByEffectiveDate"></a>
# **getSubContractorByEffectiveDate**
> SubContractor getSubContractorByEffectiveDate(employerId, subContractorId, effectiveDate, authorization, apiVersion)

Get sub contractor by effective date.

Returns the sub contractor&#39;s state at the specified effective date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      SubContractor result = apiInstance.getSubContractorByEffectiveDate(employerId, subContractorId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#getSubContractorByEffectiveDate");
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
| **effectiveDate** | **LocalDate**| The effective date to be applied. E.g 2016-04-06 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The sub contractor object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getSubContractorFromEmployer"></a>
# **getSubContractorFromEmployer**
> SubContractor getSubContractorFromEmployer(employerId, subContractorId, authorization, apiVersion)

Get sub contractor from employer

Gets the specified sub contractor from employer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      SubContractor result = apiInstance.getSubContractorFromEmployer(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#getSubContractorFromEmployer");
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

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The sub contractor object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getSubContractorRevisionByNumber"></a>
# **getSubContractorRevisionByNumber**
> SubContractor getSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion)

Gets the sub contractor by revision number

Get the sub contractor revision matching the specified revision number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      SubContractor result = apiInstance.getSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#getSubContractorRevisionByNumber");
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
| **revisionNumber** | **String**| The revision number. E.g. 1 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The sub contractor object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getSubContractorRevisions"></a>
# **getSubContractorRevisions**
> LinkCollection getSubContractorRevisions(employerId, subContractorId, authorization, apiVersion)

Get all sub contractor revisions

Gets links to all the sub contractor revisions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getSubContractorRevisions(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#getSubContractorRevisions");
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

<a id="getSubContractorsByEffectiveDate"></a>
# **getSubContractorsByEffectiveDate**
> LinkCollection getSubContractorsByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get sub contractors from employer at a given effective date.

Get links to all sub contractors for the employer on specified effective date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getSubContractorsByEffectiveDate(employerId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#getSubContractorsByEffectiveDate");
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

<a id="getSubContractorsFromEmployer"></a>
# **getSubContractorsFromEmployer**
> LinkCollection getSubContractorsFromEmployer(employerId, authorization, apiVersion)

Get sub contractors from employer.

Get links to all sub contractors for the specified employer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getSubContractorsFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#getSubContractorsFromEmployer");
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

<a id="patchSubContractor"></a>
# **patchSubContractor**
> SubContractor patchSubContractor(employerId, subContractorId, authorization, apiVersion, subContractor)

Patches the sub contractor

Patches the specified sub contractor with the supplied values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    SubContractor subContractor = new SubContractor(); // SubContractor | The sub contractor object.
    try {
      SubContractor result = apiInstance.patchSubContractor(employerId, subContractorId, authorization, apiVersion, subContractor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#patchSubContractor");
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
| **subContractor** | [**SubContractor**](SubContractor.md)| The sub contractor object. | |

### Return type

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The sub contractor object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postSubContractorIntoEmployer"></a>
# **postSubContractorIntoEmployer**
> Link postSubContractorIntoEmployer(employerId, authorization, apiVersion, subContractor)

Create a new sub contractor

Create a new sub contractor object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    SubContractor subContractor = new SubContractor(); // SubContractor | The sub contractor object.
    try {
      Link result = apiInstance.postSubContractorIntoEmployer(employerId, authorization, apiVersion, subContractor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#postSubContractorIntoEmployer");
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
| **subContractor** | [**SubContractor**](SubContractor.md)| The sub contractor object. | |

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

<a id="putSubContractorIntoEmployer"></a>
# **putSubContractorIntoEmployer**
> SubContractor putSubContractorIntoEmployer(employerId, subContractorId, authorization, apiVersion, subContractor)

Updates the sub contractor

Updates the existing specified sub contractor object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubContractorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    SubContractorApi apiInstance = new SubContractorApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    SubContractor subContractor = new SubContractor(); // SubContractor | The sub contractor object.
    try {
      SubContractor result = apiInstance.putSubContractorIntoEmployer(employerId, subContractorId, authorization, apiVersion, subContractor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubContractorApi#putSubContractorIntoEmployer");
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
| **subContractor** | [**SubContractor**](SubContractor.md)| The sub contractor object. | |

### Return type

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The sub contractor object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |


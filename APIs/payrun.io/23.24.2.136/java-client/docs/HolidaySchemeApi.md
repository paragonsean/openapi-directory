# HolidaySchemeApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteHolidayScheme**](HolidaySchemeApi.md#deleteHolidayScheme) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Delete an holiday scheme |
| [**deleteHolidaySchemeRevision**](HolidaySchemeApi.md#deleteHolidaySchemeRevision) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/{EffectiveDate} | Delete an holiday scheme revision matching the specified revision date. |
| [**deleteHolidaySchemeRevisionByNumber**](HolidaySchemeApi.md#deleteHolidaySchemeRevisionByNumber) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Revision/{RevisionNumber} | Delete an HolidayScheme revision matching the specified revision number. |
| [**deleteHolidaySchemeTag_0**](HolidaySchemeApi.md#deleteHolidaySchemeTag_0) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Delete holiday scheme tag |
| [**getAllHolidaySchemeTags_0**](HolidaySchemeApi.md#getAllHolidaySchemeTags_0) | **GET** /Employer/{EmployerId}/HolidaySchemes/Tags | Get all holiday scheme tags |
| [**getHolidaySchemeByEffectiveDate**](HolidaySchemeApi.md#getHolidaySchemeByEffectiveDate) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/{EffectiveDate} | Get holiday scheme by effective date. |
| [**getHolidaySchemeFromEmployer**](HolidaySchemeApi.md#getHolidaySchemeFromEmployer) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Get holiday scheme from employer |
| [**getHolidaySchemeRevisionByNumber**](HolidaySchemeApi.md#getHolidaySchemeRevisionByNumber) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Revision/{RevisionNumber} | Gets the holiday scheme revision by revision number |
| [**getHolidaySchemeRevisions**](HolidaySchemeApi.md#getHolidaySchemeRevisions) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Revisions | Get all holiday scheme revisions |
| [**getHolidaySchemesByEffectiveDate**](HolidaySchemeApi.md#getHolidaySchemesByEffectiveDate) | **GET** /Employer/{EmployerId}/HolidaySchemes/{EffectiveDate} | Get holiday schemes from employer at a given effective date. |
| [**getHolidaySchemesFromEmployer**](HolidaySchemeApi.md#getHolidaySchemesFromEmployer) | **GET** /Employer/{EmployerId}/HolidaySchemes | Get holiday schemes from employer. |
| [**getHolidaySchemesWithTag_0**](HolidaySchemeApi.md#getHolidaySchemesWithTag_0) | **GET** /Employer/{EmployerId}/HolidaySchemes/Tag/{TagId} | Get holiday schemes with tag |
| [**getTagFromHolidaySchemeRevision_0**](HolidaySchemeApi.md#getTagFromHolidaySchemeRevision_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId}/{EffectiveDate} | Get holiday scheme revision tag |
| [**getTagFromHolidayScheme_0**](HolidaySchemeApi.md#getTagFromHolidayScheme_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Get holiday scheme tag |
| [**getTagsFromHolidaySchemeRevision_0**](HolidaySchemeApi.md#getTagsFromHolidaySchemeRevision_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tags/{EffectiveDate} | Get all holiday scheme revision tags |
| [**getTagsFromHolidayScheme_0**](HolidaySchemeApi.md#getTagsFromHolidayScheme_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tags | Get all tags from the holiday scheme |
| [**patchHolidayScheme**](HolidaySchemeApi.md#patchHolidayScheme) | **PATCH** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Patches the holiday scheme |
| [**postHolidaySchemeIntoEmployer**](HolidaySchemeApi.md#postHolidaySchemeIntoEmployer) | **POST** /Employer/{EmployerId}/HolidaySchemes | Create a new holiday scheme |
| [**putHolidaySchemeIntoEmployer**](HolidaySchemeApi.md#putHolidaySchemeIntoEmployer) | **PUT** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Updates the holiday scheme |
| [**putHolidaySchemeTag_0**](HolidaySchemeApi.md#putHolidaySchemeTag_0) | **PUT** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Insert holiday scheme tag |


<a id="deleteHolidayScheme"></a>
# **deleteHolidayScheme**
> deleteHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion)

Delete an holiday scheme

Delete the specified holiday scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#deleteHolidayScheme");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
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

<a id="deleteHolidaySchemeRevision"></a>
# **deleteHolidaySchemeRevision**
> deleteHolidaySchemeRevision(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion)

Delete an holiday scheme revision matching the specified revision date.

Deletes the specified holiday scheme revision for the matching revision date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteHolidaySchemeRevision(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#deleteHolidaySchemeRevision");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
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

<a id="deleteHolidaySchemeRevisionByNumber"></a>
# **deleteHolidaySchemeRevisionByNumber**
> deleteHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion)

Delete an HolidayScheme revision matching the specified revision number.

Deletes the specified holiday scheme revision for the matching revision number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#deleteHolidaySchemeRevisionByNumber");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
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

<a id="deleteHolidaySchemeTag_0"></a>
# **deleteHolidaySchemeTag_0**
> deleteHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Delete holiday scheme tag

Deletes a tag from the holiday scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#deleteHolidaySchemeTag_0");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **tagId** | **String**| The tag unique identifier. E.g. MyTag | |
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

<a id="getAllHolidaySchemeTags_0"></a>
# **getAllHolidaySchemeTags_0**
> LinkCollection getAllHolidaySchemeTags_0(employerId, authorization, apiVersion)

Get all holiday scheme tags

Gets all the holiday scheme tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAllHolidaySchemeTags_0(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getAllHolidaySchemeTags_0");
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

<a id="getHolidaySchemeByEffectiveDate"></a>
# **getHolidaySchemeByEffectiveDate**
> HolidayScheme getHolidaySchemeByEffectiveDate(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion)

Get holiday scheme by effective date.

Returns the holiday scheme&#39;s state at the specified effective date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      HolidayScheme result = apiInstance.getHolidaySchemeByEffectiveDate(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getHolidaySchemeByEffectiveDate");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **effectiveDate** | **LocalDate**| The effective date to be applied. E.g 2016-04-06 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The holiday scheme object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getHolidaySchemeFromEmployer"></a>
# **getHolidaySchemeFromEmployer**
> HolidayScheme getHolidaySchemeFromEmployer(employerId, holidaySchemeId, authorization, apiVersion)

Get holiday scheme from employer

Gets the specified holiday scheme from employer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      HolidayScheme result = apiInstance.getHolidaySchemeFromEmployer(employerId, holidaySchemeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getHolidaySchemeFromEmployer");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The holiday scheme object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getHolidaySchemeRevisionByNumber"></a>
# **getHolidaySchemeRevisionByNumber**
> HolidayScheme getHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion)

Gets the holiday scheme revision by revision number

Get the holiday scheme revision matching the specified revision number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      HolidayScheme result = apiInstance.getHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getHolidaySchemeRevisionByNumber");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **revisionNumber** | **String**| The revision number. E.g. 1 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The holiday scheme object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getHolidaySchemeRevisions"></a>
# **getHolidaySchemeRevisions**
> LinkCollection getHolidaySchemeRevisions(employerId, holidaySchemeId, authorization, apiVersion)

Get all holiday scheme revisions

Gets links to all the holiday scheme revisions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getHolidaySchemeRevisions(employerId, holidaySchemeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getHolidaySchemeRevisions");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
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

<a id="getHolidaySchemesByEffectiveDate"></a>
# **getHolidaySchemesByEffectiveDate**
> LinkCollection getHolidaySchemesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get holiday schemes from employer at a given effective date.

Get links to all holiday schemes for the employer on specified effective date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getHolidaySchemesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getHolidaySchemesByEffectiveDate");
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

<a id="getHolidaySchemesFromEmployer"></a>
# **getHolidaySchemesFromEmployer**
> LinkCollection getHolidaySchemesFromEmployer(employerId, authorization, apiVersion)

Get holiday schemes from employer.

Get links to all holiday schemes for the specified employer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getHolidaySchemesFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getHolidaySchemesFromEmployer");
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

<a id="getHolidaySchemesWithTag_0"></a>
# **getHolidaySchemesWithTag_0**
> LinkCollection getHolidaySchemesWithTag_0(employerId, tagId, authorization, apiVersion)

Get holiday schemes with tag

Gets the holiday scheme with the tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getHolidaySchemesWithTag_0(employerId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getHolidaySchemesWithTag_0");
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

<a id="getTagFromHolidaySchemeRevision_0"></a>
# **getTagFromHolidaySchemeRevision_0**
> Tag getTagFromHolidaySchemeRevision_0(employerId, holidaySchemeId, tagId, effectiveDate, authorization, apiVersion)

Get holiday scheme revision tag

Gets the tag from the holiday scheme revision

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.getTagFromHolidaySchemeRevision_0(employerId, holidaySchemeId, tagId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getTagFromHolidaySchemeRevision_0");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **tagId** | **String**| The tag unique identifier. E.g. MyTag | |
| **effectiveDate** | **LocalDate**| The effective date to be applied. E.g 2016-04-06 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tag object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getTagFromHolidayScheme_0"></a>
# **getTagFromHolidayScheme_0**
> Tag getTagFromHolidayScheme_0(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Get holiday scheme tag

Gets the tag from the holiday scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.getTagFromHolidayScheme_0(employerId, holidaySchemeId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getTagFromHolidayScheme_0");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **tagId** | **String**| The tag unique identifier. E.g. MyTag | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tag object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getTagsFromHolidaySchemeRevision_0"></a>
# **getTagsFromHolidaySchemeRevision_0**
> LinkCollection getTagsFromHolidaySchemeRevision_0(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion)

Get all holiday scheme revision tags

Gets all the tags from the holiday scheme revision

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTagsFromHolidaySchemeRevision_0(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getTagsFromHolidaySchemeRevision_0");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
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

<a id="getTagsFromHolidayScheme_0"></a>
# **getTagsFromHolidayScheme_0**
> LinkCollection getTagsFromHolidayScheme_0(employerId, holidaySchemeId, authorization, apiVersion)

Get all tags from the holiday scheme

Gets all the tags from the holiday scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTagsFromHolidayScheme_0(employerId, holidaySchemeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#getTagsFromHolidayScheme_0");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
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

<a id="patchHolidayScheme"></a>
# **patchHolidayScheme**
> HolidayScheme patchHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme)

Patches the holiday scheme

Patches the specified holiday scheme with the supplied values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    HolidayScheme holidayScheme = new HolidayScheme(); // HolidayScheme | The holiday scheme object.
    try {
      HolidayScheme result = apiInstance.patchHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#patchHolidayScheme");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **holidayScheme** | [**HolidayScheme**](HolidayScheme.md)| The holiday scheme object. | |

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The holiday scheme object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postHolidaySchemeIntoEmployer"></a>
# **postHolidaySchemeIntoEmployer**
> Link postHolidaySchemeIntoEmployer(employerId, authorization, apiVersion, holidayScheme)

Create a new holiday scheme

Create a new holiday scheme object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    HolidayScheme holidayScheme = new HolidayScheme(); // HolidayScheme | The holiday scheme object.
    try {
      Link result = apiInstance.postHolidaySchemeIntoEmployer(employerId, authorization, apiVersion, holidayScheme);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#postHolidaySchemeIntoEmployer");
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
| **holidayScheme** | [**HolidayScheme**](HolidayScheme.md)| The holiday scheme object. | |

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

<a id="putHolidaySchemeIntoEmployer"></a>
# **putHolidaySchemeIntoEmployer**
> HolidayScheme putHolidaySchemeIntoEmployer(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme)

Updates the holiday scheme

Updates the existing specified holiday scheme object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    HolidayScheme holidayScheme = new HolidayScheme(); // HolidayScheme | The holiday scheme object.
    try {
      HolidayScheme result = apiInstance.putHolidaySchemeIntoEmployer(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#putHolidaySchemeIntoEmployer");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **holidayScheme** | [**HolidayScheme**](HolidayScheme.md)| The holiday scheme object. | |

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The holiday scheme object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putHolidaySchemeTag_0"></a>
# **putHolidaySchemeTag_0**
> Tag putHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Insert holiday scheme tag

Inserts a new tag on the holiday scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HolidaySchemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    HolidaySchemeApi apiInstance = new HolidaySchemeApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.putHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HolidaySchemeApi#putHolidaySchemeTag_0");
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
| **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | |
| **tagId** | **String**| The tag unique identifier. E.g. MyTag | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tag object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |


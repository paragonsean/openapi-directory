# PayInstructionApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePayInstruction**](PayInstructionApi.md#deletePayInstruction) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Deletes a pay instruction |
| [**getAllPayInstructionTags_0**](PayInstructionApi.md#getAllPayInstructionTags_0) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions/Tags | Get all pay instruction tags |
| [**getPayInstructionFromEmployee**](PayInstructionApi.md#getPayInstructionFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Gets the specified pay instruction from the employee |
| [**getPayInstructionsFromEmployee**](PayInstructionApi.md#getPayInstructionsFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions | Gets the pay instructions from the specified employee |
| [**getPayInstructionsWithTag_0**](PayInstructionApi.md#getPayInstructionsWithTag_0) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions/Tag/{TagId} | Get pay instructions with tag |
| [**patchPayInstruction**](PayInstructionApi.md#patchPayInstruction) | **PATCH** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Sparse Update of a Pay Instruction |
| [**postPayInstruction**](PayInstructionApi.md#postPayInstruction) | **POST** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions | Creates a new Pay Instruction |
| [**putPayInstruction**](PayInstructionApi.md#putPayInstruction) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Update a Pay Instruction |


<a id="deletePayInstruction"></a>
# **deletePayInstruction**
> deletePayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion)

Deletes a pay instruction

Delete the specified pay instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deletePayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#deletePayInstruction");
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
| **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | |
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

<a id="getAllPayInstructionTags_0"></a>
# **getAllPayInstructionTags_0**
> LinkCollection getAllPayInstructionTags_0(employerId, employeeId, authorization, apiVersion)

Get all pay instruction tags

Gets all the pay instruction tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAllPayInstructionTags_0(employerId, employeeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#getAllPayInstructionTags_0");
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

<a id="getPayInstructionFromEmployee"></a>
# **getPayInstructionFromEmployee**
> PayInstruction getPayInstructionFromEmployee(employerId, employeeId, payInstructionId, authorization, apiVersion)

Gets the specified pay instruction from the employee

Returns the specified pay instruction from employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      PayInstruction result = apiInstance.getPayInstructionFromEmployee(employerId, employeeId, payInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#getPayInstructionFromEmployee");
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
| **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**PayInstruction**](PayInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pay instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPayInstructionsFromEmployee"></a>
# **getPayInstructionsFromEmployee**
> LinkCollection getPayInstructionsFromEmployee(employerId, employeeId, authorization, apiVersion)

Gets the pay instructions from the specified employee

Get links to all pay instructions for the specified employee

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getPayInstructionsFromEmployee(employerId, employeeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#getPayInstructionsFromEmployee");
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

<a id="getPayInstructionsWithTag_0"></a>
# **getPayInstructionsWithTag_0**
> LinkCollection getPayInstructionsWithTag_0(employerId, employeeId, tagId, authorization, apiVersion)

Get pay instructions with tag

Gets the pay instructions with the tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getPayInstructionsWithTag_0(employerId, employeeId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#getPayInstructionsWithTag_0");
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

<a id="patchPayInstruction"></a>
# **patchPayInstruction**
> PayInstruction patchPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction)

Sparse Update of a Pay Instruction

Patches the specified pay instruction with the supplied values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    PayInstruction payInstruction = new PayInstruction(); // PayInstruction | The pay instruction object.
    try {
      PayInstruction result = apiInstance.patchPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#patchPayInstruction");
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
| **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **payInstruction** | [**PayInstruction**](PayInstruction.md)| The pay instruction object. | |

### Return type

[**PayInstruction**](PayInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pay instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postPayInstruction"></a>
# **postPayInstruction**
> Link postPayInstruction(employerId, employeeId, authorization, apiVersion, payInstruction)

Creates a new Pay Instruction

Creates a new pay instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    PayInstruction payInstruction = new PayInstruction(); // PayInstruction | The pay instruction object.
    try {
      Link result = apiInstance.postPayInstruction(employerId, employeeId, authorization, apiVersion, payInstruction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#postPayInstruction");
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
| **payInstruction** | [**PayInstruction**](PayInstruction.md)| The pay instruction object. | |

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

<a id="putPayInstruction"></a>
# **putPayInstruction**
> PayInstruction putPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction)

Update a Pay Instruction

Updates the existing specified pay instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayInstructionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    PayInstructionApi apiInstance = new PayInstructionApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
    String payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    PayInstruction payInstruction = new PayInstruction(); // PayInstruction | The pay instruction object.
    try {
      PayInstruction result = apiInstance.putPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayInstructionApi#putPayInstruction");
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
| **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **payInstruction** | [**PayInstruction**](PayInstruction.md)| The pay instruction object. | |

### Return type

[**PayInstruction**](PayInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pay instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |


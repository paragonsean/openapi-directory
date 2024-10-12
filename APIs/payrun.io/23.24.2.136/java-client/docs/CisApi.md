# CisApi

All URIs are relative to *https://api.test.payrun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCisInstruction**](CisApi.md#deleteCisInstruction) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Delete a CIS instruction |
| [**deleteCisInstructionTag_0**](CisApi.md#deleteCisInstructionTag_0) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Delete CIS instruction tag |
| [**deleteCisLine**](CisApi.md#deleteCisLine) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId} | Delete a CIS line |
| [**deleteCisLineTag_0**](CisApi.md#deleteCisLineTag_0) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Delete CIS line tag |
| [**deleteCisLineType**](CisApi.md#deleteCisLineType) | **DELETE** /Employer/{EmployerId}/CisLineType/{CisLineTypeId} | Delete an CIS line type |
| [**deleteCisLineTypeTag_0**](CisApi.md#deleteCisLineTypeTag_0) | **DELETE** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Delete CIS line type tag |
| [**deleteCisTransaction**](CisApi.md#deleteCisTransaction) | **DELETE** /Employer/{EmployerId}/CisTransaction/{CisTransactionId} | Delete the CIS transaction |
| [**deleteSubContractorTag_0**](CisApi.md#deleteSubContractorTag_0) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Delete sub contractor tag |
| [**getAllCisInstructionTags_0**](CisApi.md#getAllCisInstructionTags_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions/Tags | Get all CIS instruction tags |
| [**getAllCisLineTags_0**](CisApi.md#getAllCisLineTags_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines/Tags | Get all CIS line tags |
| [**getAllCisLineTypeTags_0**](CisApi.md#getAllCisLineTypeTags_0) | **GET** /Employer/{EmployerId}/CisLineTypes/Tags | Get all CIS line type tags |
| [**getAllSubContractorTags_0**](CisApi.md#getAllSubContractorTags_0) | **GET** /Employer/{EmployerId}/SubContractors/Tags | Get all sub contractor tags |
| [**getCisInstructionFromSubContractor**](CisApi.md#getCisInstructionFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Get CIS instruction from sub contractor |
| [**getCisInstructionsFromSubContractor**](CisApi.md#getCisInstructionsFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions | Get CIS instructions from sub contractor. |
| [**getCisInstructionsWithTag_0**](CisApi.md#getCisInstructionsWithTag_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions/Tag/{TagId} | Get CIS instructions with tag |
| [**getCisLineFromSubContractor**](CisApi.md#getCisLineFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId} | Get CIS line from sub contractor |
| [**getCisLineTypeFromEmployer**](CisApi.md#getCisLineTypeFromEmployer) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId} | Get CIS line type from employer |
| [**getCisLineTypesFromEmployer**](CisApi.md#getCisLineTypesFromEmployer) | **GET** /Employer/{EmployerId}/CisLineTypes | Get CIS line types from employer. |
| [**getCisLineTypesWithTag_0**](CisApi.md#getCisLineTypesWithTag_0) | **GET** /Employer/{EmployerId}/CisLineTypes/Tag/{TagId} | Get CIS line types with tag |
| [**getCisLinesFromSubContractor**](CisApi.md#getCisLinesFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines | Get CIS lines from sub contractor. |
| [**getCisLinesWithTag_0**](CisApi.md#getCisLinesWithTag_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines/Tag/{TagId} | Get CIS lines with tag |
| [**getCisTransactionFromEmployer**](CisApi.md#getCisTransactionFromEmployer) | **GET** /Employer/{EmployerId}/CisTransaction/{CisTransactionId} | Get the CIS transaction |
| [**getCisTransactionsFromEmployer**](CisApi.md#getCisTransactionsFromEmployer) | **GET** /Employer/{EmployerId}/CisTransactions | Get all CIS transactions for the employer |
| [**getSubContractorsWithTag_0**](CisApi.md#getSubContractorsWithTag_0) | **GET** /Employer/{EmployerId}/SubContractors/Tag/{TagId} | Get sub contractors with tag |
| [**getTagFromCisInstruction_0**](CisApi.md#getTagFromCisInstruction_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Get CIS instruction tag |
| [**getTagFromCisLineType_0**](CisApi.md#getTagFromCisLineType_0) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Get CIS line type tag |
| [**getTagFromCisLine_0**](CisApi.md#getTagFromCisLine_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Get CIS line tag |
| [**getTagFromSubContractorRevision_0**](CisApi.md#getTagFromSubContractorRevision_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId}/{EffectiveDate} | Get sub contractor revision tag |
| [**getTagFromSubContractor_0**](CisApi.md#getTagFromSubContractor_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Get sub contractor tag |
| [**getTagsFromCisInstruction_0**](CisApi.md#getTagsFromCisInstruction_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tags | Get all tags from the CIS instruction |
| [**getTagsFromCisLineType_0**](CisApi.md#getTagsFromCisLineType_0) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tags | Get all tags from the CIS line type |
| [**getTagsFromCisLine_0**](CisApi.md#getTagsFromCisLine_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tags | Get all tags from the CIS line |
| [**getTagsFromSubContractorRevision_0**](CisApi.md#getTagsFromSubContractorRevision_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tags/{EffectiveDate} | Get all sub contractor revision tags |
| [**getTagsFromSubContractor_0**](CisApi.md#getTagsFromSubContractor_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tags | Get all tags from the sub contractor |
| [**patchCisInstruction**](CisApi.md#patchCisInstruction) | **PATCH** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Patches the CIS instruction |
| [**postCisInstructionIntoSubContractor**](CisApi.md#postCisInstructionIntoSubContractor) | **POST** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions | Create a new CIS instruction |
| [**postCisLineTypeIntoEmployer**](CisApi.md#postCisLineTypeIntoEmployer) | **POST** /Employer/{EmployerId}/CisLineTypes | Create a new CIS line type |
| [**putCisInstructionIntoSubContractor**](CisApi.md#putCisInstructionIntoSubContractor) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Updates the CIS instruction |
| [**putCisInstructionTag_0**](CisApi.md#putCisInstructionTag_0) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Insert CIS instruction tag |
| [**putCisLineTag_0**](CisApi.md#putCisLineTag_0) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Insert CIS line tag |
| [**putCisLineTypeIntoEmployer**](CisApi.md#putCisLineTypeIntoEmployer) | **PUT** /Employer/{EmployerId}/CisLineType/{CisLineTypeId} | Updates the CIS line type |
| [**putCisLineTypeTag_0**](CisApi.md#putCisLineTypeTag_0) | **PUT** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Insert CIS line type tag |
| [**putSubContractorTag_0**](CisApi.md#putSubContractorTag_0) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Insert sub contractor tag |


<a id="deleteCisInstruction"></a>
# **deleteCisInstruction**
> deleteCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Delete a CIS instruction

Delete the specified CIS instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteCisInstruction");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
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

<a id="deleteCisInstructionTag_0"></a>
# **deleteCisInstructionTag_0**
> deleteCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Delete CIS instruction tag

Deletes a tag from the CIS instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteCisInstructionTag_0");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
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

<a id="deleteCisLine"></a>
# **deleteCisLine**
> deleteCisLine(employerId, subContractorId, cisLineId, authorization, apiVersion)

Delete a CIS line

Delete the specified CIS line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteCisLine(employerId, subContractorId, cisLineId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteCisLine");
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
| **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | |
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

<a id="deleteCisLineTag_0"></a>
# **deleteCisLineTag_0**
> deleteCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Delete CIS line tag

Deletes a tag from the CIS line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteCisLineTag_0");
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
| **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | |
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

<a id="deleteCisLineType"></a>
# **deleteCisLineType**
> deleteCisLineType(employerId, cisLineTypeId, authorization, apiVersion)

Delete an CIS line type

Delete the specified CIS line type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteCisLineType(employerId, cisLineTypeId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteCisLineType");
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
| **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | |
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

<a id="deleteCisLineTypeTag_0"></a>
# **deleteCisLineTypeTag_0**
> deleteCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Delete CIS line type tag

Deletes a tag from the CIS line type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteCisLineTypeTag_0");
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
| **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | |
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

<a id="deleteCisTransaction"></a>
# **deleteCisTransaction**
> deleteCisTransaction(employerId, cisTransactionId, authorization, apiVersion)

Delete the CIS transaction

Deletes the specified CIS transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisTransactionId = "cisTransactionId_example"; // String | The CIS transaction unique identifier. E.g. CISTRAN001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteCisTransaction(employerId, cisTransactionId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteCisTransaction");
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
| **cisTransactionId** | **String**| The CIS transaction unique identifier. E.g. CISTRAN001 | |
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

<a id="deleteSubContractorTag_0"></a>
# **deleteSubContractorTag_0**
> deleteSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Delete sub contractor tag

Deletes a tag from the sub contractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      apiInstance.deleteSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#deleteSubContractorTag_0");
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

<a id="getAllCisInstructionTags_0"></a>
# **getAllCisInstructionTags_0**
> LinkCollection getAllCisInstructionTags_0(employerId, subContractorId, authorization, apiVersion)

Get all CIS instruction tags

Gets all the CIS instruction tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAllCisInstructionTags_0(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getAllCisInstructionTags_0");
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

<a id="getAllCisLineTags_0"></a>
# **getAllCisLineTags_0**
> LinkCollection getAllCisLineTags_0(employerId, subContractorId, authorization, apiVersion)

Get all CIS line tags

Gets all the CIS line tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAllCisLineTags_0(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getAllCisLineTags_0");
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

<a id="getAllCisLineTypeTags_0"></a>
# **getAllCisLineTypeTags_0**
> LinkCollection getAllCisLineTypeTags_0(employerId, authorization, apiVersion)

Get all CIS line type tags

Gets all the CIS line type tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAllCisLineTypeTags_0(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getAllCisLineTypeTags_0");
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

<a id="getAllSubContractorTags_0"></a>
# **getAllSubContractorTags_0**
> LinkCollection getAllSubContractorTags_0(employerId, authorization, apiVersion)

Get all sub contractor tags

Gets all the sub contractor tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getAllSubContractorTags_0(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getAllSubContractorTags_0");
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

<a id="getCisInstructionFromSubContractor"></a>
# **getCisInstructionFromSubContractor**
> CisInstruction getCisInstructionFromSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Get CIS instruction from sub contractor

Gets the specified CIS instruction from sub contractor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      CisInstruction result = apiInstance.getCisInstructionFromSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisInstructionFromSubContractor");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**CisInstruction**](CisInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cis instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCisInstructionsFromSubContractor"></a>
# **getCisInstructionsFromSubContractor**
> LinkCollection getCisInstructionsFromSubContractor(employerId, subContractorId, authorization, apiVersion)

Get CIS instructions from sub contractor.

Get links to all CIS instructions for the specified sub contractor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getCisInstructionsFromSubContractor(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisInstructionsFromSubContractor");
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

<a id="getCisInstructionsWithTag_0"></a>
# **getCisInstructionsWithTag_0**
> LinkCollection getCisInstructionsWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Get CIS instructions with tag

Gets the CIS instruction with the tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getCisInstructionsWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisInstructionsWithTag_0");
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

<a id="getCisLineFromSubContractor"></a>
# **getCisLineFromSubContractor**
> CisLine getCisLineFromSubContractor(employerId, subContractorId, cisLineId, authorization, apiVersion)

Get CIS line from sub contractor

Gets the specified CIS line from sub contractor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      CisLine result = apiInstance.getCisLineFromSubContractor(employerId, subContractorId, cisLineId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisLineFromSubContractor");
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
| **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**CisLine**](CisLine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cis line object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCisLineTypeFromEmployer"></a>
# **getCisLineTypeFromEmployer**
> CisLineType getCisLineTypeFromEmployer(employerId, cisLineTypeId, authorization, apiVersion)

Get CIS line type from employer

Gets the specified CIS line type from employer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      CisLineType result = apiInstance.getCisLineTypeFromEmployer(employerId, cisLineTypeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisLineTypeFromEmployer");
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
| **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**CisLineType**](CisLineType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cis line type object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCisLineTypesFromEmployer"></a>
# **getCisLineTypesFromEmployer**
> LinkCollection getCisLineTypesFromEmployer(employerId, authorization, apiVersion)

Get CIS line types from employer.

Get links to all CIS line types for the specified employer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getCisLineTypesFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisLineTypesFromEmployer");
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

<a id="getCisLineTypesWithTag_0"></a>
# **getCisLineTypesWithTag_0**
> LinkCollection getCisLineTypesWithTag_0(employerId, tagId, authorization, apiVersion)

Get CIS line types with tag

Gets the CIS line type with the tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getCisLineTypesWithTag_0(employerId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisLineTypesWithTag_0");
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

<a id="getCisLinesFromSubContractor"></a>
# **getCisLinesFromSubContractor**
> LinkCollection getCisLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion)

Get CIS lines from sub contractor.

Get links to all CIS lines for the specified sub contractor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getCisLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisLinesFromSubContractor");
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

<a id="getCisLinesWithTag_0"></a>
# **getCisLinesWithTag_0**
> LinkCollection getCisLinesWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Get CIS lines with tag

Gets the CIS line with the tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getCisLinesWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisLinesWithTag_0");
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

<a id="getCisTransactionFromEmployer"></a>
# **getCisTransactionFromEmployer**
> CisTransaction getCisTransactionFromEmployer(employerId, cisTransactionId, authorization, apiVersion)

Get the CIS transaction

Returns the specified CIS transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisTransactionId = "cisTransactionId_example"; // String | The CIS transaction unique identifier. E.g. CISTRAN001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      CisTransaction result = apiInstance.getCisTransactionFromEmployer(employerId, cisTransactionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisTransactionFromEmployer");
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
| **cisTransactionId** | **String**| The CIS transaction unique identifier. E.g. CISTRAN001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**CisTransaction**](CisTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cis transaction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCisTransactionsFromEmployer"></a>
# **getCisTransactionsFromEmployer**
> LinkCollection getCisTransactionsFromEmployer(employerId, authorization, apiVersion)

Get all CIS transactions for the employer

Get links for all CIS transactions for the specified employer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getCisTransactionsFromEmployer(employerId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getCisTransactionsFromEmployer");
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

<a id="getSubContractorsWithTag_0"></a>
# **getSubContractorsWithTag_0**
> LinkCollection getSubContractorsWithTag_0(employerId, tagId, authorization, apiVersion)

Get sub contractors with tag

Gets the sub contractor with the tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getSubContractorsWithTag_0(employerId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getSubContractorsWithTag_0");
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

<a id="getTagFromCisInstruction_0"></a>
# **getTagFromCisInstruction_0**
> Tag getTagFromCisInstruction_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Get CIS instruction tag

Gets the tag from the CIS instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.getTagFromCisInstruction_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagFromCisInstruction_0");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
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

<a id="getTagFromCisLineType_0"></a>
# **getTagFromCisLineType_0**
> Tag getTagFromCisLineType_0(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Get CIS line type tag

Gets the tag from the CIS line type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.getTagFromCisLineType_0(employerId, cisLineTypeId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagFromCisLineType_0");
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
| **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | |
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

<a id="getTagFromCisLine_0"></a>
# **getTagFromCisLine_0**
> Tag getTagFromCisLine_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Get CIS line tag

Gets the tag from the CIS line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.getTagFromCisLine_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagFromCisLine_0");
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
| **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | |
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

<a id="getTagFromSubContractorRevision_0"></a>
# **getTagFromSubContractorRevision_0**
> Tag getTagFromSubContractorRevision_0(employerId, subContractorId, tagId, effectiveDate, authorization, apiVersion)

Get sub contractor revision tag

Gets the tag from the sub contractor revision

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.getTagFromSubContractorRevision_0(employerId, subContractorId, tagId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagFromSubContractorRevision_0");
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

<a id="getTagFromSubContractor_0"></a>
# **getTagFromSubContractor_0**
> Tag getTagFromSubContractor_0(employerId, subContractorId, tagId, authorization, apiVersion)

Get sub contractor tag

Gets the tag from the sub contractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.getTagFromSubContractor_0(employerId, subContractorId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagFromSubContractor_0");
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

<a id="getTagsFromCisInstruction_0"></a>
# **getTagsFromCisInstruction_0**
> LinkCollection getTagsFromCisInstruction_0(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Get all tags from the CIS instruction

Gets all the tags from the CIS instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTagsFromCisInstruction_0(employerId, subContractorId, cisInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagsFromCisInstruction_0");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
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

<a id="getTagsFromCisLineType_0"></a>
# **getTagsFromCisLineType_0**
> LinkCollection getTagsFromCisLineType_0(employerId, cisLineTypeId, authorization, apiVersion)

Get all tags from the CIS line type

Gets all the tags from the CIS line type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTagsFromCisLineType_0(employerId, cisLineTypeId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagsFromCisLineType_0");
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
| **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | |
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

<a id="getTagsFromCisLine_0"></a>
# **getTagsFromCisLine_0**
> LinkCollection getTagsFromCisLine_0(employerId, subContractorId, cisLineId, authorization, apiVersion)

Get all tags from the CIS line

Gets all the tags from the CIS line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTagsFromCisLine_0(employerId, subContractorId, cisLineId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagsFromCisLine_0");
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
| **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | |
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

<a id="getTagsFromSubContractorRevision_0"></a>
# **getTagsFromSubContractorRevision_0**
> LinkCollection getTagsFromSubContractorRevision_0(employerId, subContractorId, effectiveDate, authorization, apiVersion)

Get all sub contractor revision tags

Gets all the tags from the sub contractor revision

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    LocalDate effectiveDate = LocalDate.now(); // LocalDate | The effective date to be applied. E.g 2016-04-06
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTagsFromSubContractorRevision_0(employerId, subContractorId, effectiveDate, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagsFromSubContractorRevision_0");
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

<a id="getTagsFromSubContractor_0"></a>
# **getTagsFromSubContractor_0**
> LinkCollection getTagsFromSubContractor_0(employerId, subContractorId, authorization, apiVersion)

Get all tags from the sub contractor

Gets all the tags from the sub contractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      LinkCollection result = apiInstance.getTagsFromSubContractor_0(employerId, subContractorId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#getTagsFromSubContractor_0");
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

<a id="patchCisInstruction"></a>
# **patchCisInstruction**
> CisInstruction patchCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Patches the CIS instruction

Update an existing CIS instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      CisInstruction result = apiInstance.patchCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#patchCisInstruction");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |

### Return type

[**CisInstruction**](CisInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cis instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="postCisInstructionIntoSubContractor"></a>
# **postCisInstructionIntoSubContractor**
> Link postCisInstructionIntoSubContractor(employerId, subContractorId, authorization, apiVersion, cisInstruction)

Create a new CIS instruction

Create a new CIS instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    CisInstruction cisInstruction = new CisInstruction(); // CisInstruction | The CIS instruction object.
    try {
      Link result = apiInstance.postCisInstructionIntoSubContractor(employerId, subContractorId, authorization, apiVersion, cisInstruction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#postCisInstructionIntoSubContractor");
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
| **cisInstruction** | [**CisInstruction**](CisInstruction.md)| The CIS instruction object. | |

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

<a id="postCisLineTypeIntoEmployer"></a>
# **postCisLineTypeIntoEmployer**
> Link postCisLineTypeIntoEmployer(employerId, authorization, apiVersion, cisLineType)

Create a new CIS line type

Create a new CIS line type object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    CisLineType cisLineType = new CisLineType(); // CisLineType | The CIS line type object.
    try {
      Link result = apiInstance.postCisLineTypeIntoEmployer(employerId, authorization, apiVersion, cisLineType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#postCisLineTypeIntoEmployer");
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
| **cisLineType** | [**CisLineType**](CisLineType.md)| The CIS line type object. | |

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

<a id="putCisInstructionIntoSubContractor"></a>
# **putCisInstructionIntoSubContractor**
> CisInstruction putCisInstructionIntoSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion, cisInstruction)

Updates the CIS instruction

Insert or update existing CIS instruction object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    CisInstruction cisInstruction = new CisInstruction(); // CisInstruction | The CIS instruction object.
    try {
      CisInstruction result = apiInstance.putCisInstructionIntoSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion, cisInstruction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#putCisInstructionIntoSubContractor");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **cisInstruction** | [**CisInstruction**](CisInstruction.md)| The CIS instruction object. | |

### Return type

[**CisInstruction**](CisInstruction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cis instruction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putCisInstructionTag_0"></a>
# **putCisInstructionTag_0**
> Tag putCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Insert CIS instruction tag

Inserts a new tag on the CIS instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.putCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#putCisInstructionTag_0");
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
| **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | |
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

<a id="putCisLineTag_0"></a>
# **putCisLineTag_0**
> Tag putCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Insert CIS line tag

Inserts a new tag on the CIS line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.putCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#putCisLineTag_0");
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
| **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | |
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

<a id="putCisLineTypeIntoEmployer"></a>
# **putCisLineTypeIntoEmployer**
> CisLineType putCisLineTypeIntoEmployer(employerId, cisLineTypeId, authorization, apiVersion, cisLineType)

Updates the CIS line type

Updates the existing specified CIS line type object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    CisLineType cisLineType = new CisLineType(); // CisLineType | The CIS line type object.
    try {
      CisLineType result = apiInstance.putCisLineTypeIntoEmployer(employerId, cisLineTypeId, authorization, apiVersion, cisLineType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#putCisLineTypeIntoEmployer");
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
| **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | |
| **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to Auto] |
| **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to default] |
| **cisLineType** | [**CisLineType**](CisLineType.md)| The CIS line type object. | |

### Return type

[**CisLineType**](CisLineType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The cis line type object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="putCisLineTypeTag_0"></a>
# **putCisLineTypeTag_0**
> Tag putCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Insert CIS line type tag

Inserts a new tag on the CIS line type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.putCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#putCisLineTypeTag_0");
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
| **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | |
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

<a id="putSubContractorTag_0"></a>
# **putSubContractorTag_0**
> Tag putSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Insert sub contractor tag

Inserts a new tag on the sub contractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.payrun.io");

    CisApi apiInstance = new CisApi(defaultClient);
    String employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
    String subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
    String tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
    String authorization = "Auto"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
    String apiVersion = "default"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
    try {
      Tag result = apiInstance.putSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CisApi#putSubContractorTag_0");
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


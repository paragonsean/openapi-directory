# QuoteApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getQuote**](QuoteApi.md#getQuote) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/quotes/{quote_id} | Get a specific quote of project |
| [**getQuoteList**](QuoteApi.md#getQuoteList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/quotes | List the quotes |
| [**getQuoteStateList**](QuoteApi.md#getQuoteStateList) | **GET** /v1/workgroups/{workgroup_id}/quoteStates | List the quote states |
| [**putQuote**](QuoteApi.md#putQuote) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/quotes/{quote_id} | Accept / Reject a Quote |
| [**v1WorkgroupsWorkgroupIdQuotesGet**](QuoteApi.md#v1WorkgroupsWorkgroupIdQuotesGet) | **GET** /v1/workgroups/{workgroup_id}/quotes | List the quotes of workgroup level |


<a id="getQuote"></a>
# **getQuote**
> QuoteExpandVO getQuote(workgroupId, projectId, quoteId)

Get a specific quote of project

Get a specific quote of project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String quoteId = "quoteId_example"; // String | 
    try {
      QuoteExpandVO result = apiInstance.getQuote(workgroupId, projectId, quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#getQuote");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **quoteId** | **String**|  | |

### Return type

[**QuoteExpandVO**](QuoteExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getQuoteList"></a>
# **getQuoteList**
> QuoteListVO getQuoteList(workgroupId, projectId, quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket)

List the quotes

List the quotes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket = "quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket_example"; // String | Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value
    try {
      QuoteListVO result = apiInstance.getQuoteList(workgroupId, projectId, quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#getQuoteList");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket** | **String**| Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value | [optional] |

### Return type

[**QuoteListVO**](QuoteListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getQuoteStateList"></a>
# **getQuoteStateList**
> ObjectStateListVO getQuoteStateList(workgroupId)

List the quote states

List the quote states

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ObjectStateListVO result = apiInstance.getQuoteStateList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#getQuoteStateList");
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
| **workgroupId** | **String**|  | |

### Return type

[**ObjectStateListVO**](ObjectStateListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="putQuote"></a>
# **putQuote**
> HTTPStatusVO putQuote(workgroupId, projectId, quoteId, quotePutPersistVO)

Accept / Reject a Quote

Accept / Reject a Quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String quoteId = "quoteId_example"; // String | 
    QuotePutPersistVO quotePutPersistVO = new QuotePutPersistVO(); // QuotePutPersistVO | 
    try {
      HTTPStatusVO result = apiInstance.putQuote(workgroupId, projectId, quoteId, quotePutPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#putQuote");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **quoteId** | **String**|  | |
| **quotePutPersistVO** | [**QuotePutPersistVO**](QuotePutPersistVO.md)|  | [optional] |

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful updated |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="v1WorkgroupsWorkgroupIdQuotesGet"></a>
# **v1WorkgroupsWorkgroupIdQuotesGet**
> QuoteOfWgLevelSimpleVO v1WorkgroupsWorkgroupIdQuotesGet(workgroupId, quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket)

List the quotes of workgroup level

List the quotes of workgroup level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket = "quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket_example"; // String | Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value
    try {
      QuoteOfWgLevelSimpleVO result = apiInstance.v1WorkgroupsWorkgroupIdQuotesGet(workgroupId, quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#v1WorkgroupsWorkgroupIdQuotesGet");
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
| **workgroupId** | **String**|  | |
| **quoteStateIdCommaUseFiltersEqualLeftCurlyBracketDoubleQuoteQuoteStateIdDoubleQuoteColon111111RightCurlyBracket** | **String**| Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value | [optional] |

### Return type

[**QuoteOfWgLevelSimpleVO**](QuoteOfWgLevelSimpleVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |


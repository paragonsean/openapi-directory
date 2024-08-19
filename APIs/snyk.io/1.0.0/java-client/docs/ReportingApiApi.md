# ReportingApiApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIssueCounts**](ReportingApiApi.md#getIssueCounts) | **POST** /reporting/counts/issues | Get issue counts |
| [**getLatestIssueCounts**](ReportingApiApi.md#getLatestIssueCounts) | **POST** /reporting/counts/issues/latest | Get latest issue counts |
| [**getLatestProjectCounts**](ReportingApiApi.md#getLatestProjectCounts) | **POST** /reporting/counts/projects/latest | Get latest project counts |
| [**getListOfIssues**](ReportingApiApi.md#getListOfIssues) | **POST** /reporting/issues/ | Get list of issues |
| [**getListOfLatestIssues**](ReportingApiApi.md#getListOfLatestIssues) | **POST** /reporting/issues/latest | Get list of latest issues |
| [**getProjectCounts**](ReportingApiApi.md#getProjectCounts) | **POST** /reporting/counts/projects | Get project counts |
| [**getTestCounts**](ReportingApiApi.md#getTestCounts) | **POST** /reporting/counts/tests | Get test counts |


<a id="getIssueCounts"></a>
# **getIssueCounts**
> GetIssueCounts200Response getIssueCounts(from, to, groupBy, getIssueCountsRequest)

Get issue counts



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ReportingApiApi apiInstance = new ReportingApiApi(defaultClient);
    String from = "2017-07-01"; // String | The date you wish to fetch results from, in the format `YYYY-MM-DD`
    String to = "2017-07-03"; // String | The date you wish to fetch results until, in the format `YYYY-MM-DD`
    String groupBy = "severity"; // String | The field to group results by
    GetIssueCountsRequest getIssueCountsRequest = new GetIssueCountsRequest(); // GetIssueCountsRequest | 
    try {
      GetIssueCounts200Response result = apiInstance.getIssueCounts(from, to, groupBy, getIssueCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApiApi#getIssueCounts");
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
| **from** | **String**| The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60; | |
| **to** | **String**| The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60; | |
| **groupBy** | **String**| The field to group results by | [optional] [enum: severity, fixable, project,[severity|fixable]] |
| **getIssueCountsRequest** | [**GetIssueCountsRequest**](GetIssueCountsRequest.md)|  | [optional] |

### Return type

[**GetIssueCounts200Response**](GetIssueCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getLatestIssueCounts"></a>
# **getLatestIssueCounts**
> GetIssueCounts200Response getLatestIssueCounts(groupBy, getIssueCountsRequest)

Get latest issue counts



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ReportingApiApi apiInstance = new ReportingApiApi(defaultClient);
    String groupBy = "severity"; // String | The field to group results by
    GetIssueCountsRequest getIssueCountsRequest = new GetIssueCountsRequest(); // GetIssueCountsRequest | 
    try {
      GetIssueCounts200Response result = apiInstance.getLatestIssueCounts(groupBy, getIssueCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApiApi#getLatestIssueCounts");
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
| **groupBy** | **String**| The field to group results by | [optional] [enum: severity, fixable, project,[severity|fixable]] |
| **getIssueCountsRequest** | [**GetIssueCountsRequest**](GetIssueCountsRequest.md)|  | [optional] |

### Return type

[**GetIssueCounts200Response**](GetIssueCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getLatestProjectCounts"></a>
# **getLatestProjectCounts**
> GetProjectCounts200Response getLatestProjectCounts(getProjectCountsRequest)

Get latest project counts



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ReportingApiApi apiInstance = new ReportingApiApi(defaultClient);
    GetProjectCountsRequest getProjectCountsRequest = new GetProjectCountsRequest(); // GetProjectCountsRequest | 
    try {
      GetProjectCounts200Response result = apiInstance.getLatestProjectCounts(getProjectCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApiApi#getLatestProjectCounts");
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
| **getProjectCountsRequest** | [**GetProjectCountsRequest**](GetProjectCountsRequest.md)|  | [optional] |

### Return type

[**GetProjectCounts200Response**](GetProjectCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getListOfIssues"></a>
# **getListOfIssues**
> GetListOfIssues200Response getListOfIssues(from, to, page, perPage, sortBy, order, groupBy, getListOfIssuesRequest)

Get list of issues



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ReportingApiApi apiInstance = new ReportingApiApi(defaultClient);
    String from = "2017-07-01"; // String | The date you wish to fetch results from, in the format `YYYY-MM-DD`
    String to = "2017-07-07"; // String | The date you wish to fetch results until, in the format `YYYY-MM-DD`
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page of results to request
    BigDecimal perPage = new BigDecimal("100"); // BigDecimal | The number of results to return per page (Maximum: 1000)
    String sortBy = "severity"; // String | The key to sort results by
    String order = "asc"; // String | The direction to sort results.
    String groupBy = "issue"; // String | Set to issue to group the same issue in multiple projects
    GetListOfIssuesRequest getListOfIssuesRequest = new GetListOfIssuesRequest(); // GetListOfIssuesRequest | 
    try {
      GetListOfIssues200Response result = apiInstance.getListOfIssues(from, to, page, perPage, sortBy, order, groupBy, getListOfIssuesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApiApi#getListOfIssues");
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
| **from** | **String**| The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60; | |
| **to** | **String**| The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60; | |
| **page** | **BigDecimal**| The page of results to request | [optional] |
| **perPage** | **BigDecimal**| The number of results to return per page (Maximum: 1000) | [optional] |
| **sortBy** | **String**| The key to sort results by | [optional] [enum: severity, issueTitle, projectName, isFixed, isPatched, isIgnored, introducedDate, isUpgradable, isPatchable, priorityScore] |
| **order** | **String**| The direction to sort results. | [optional] |
| **groupBy** | **String**| Set to issue to group the same issue in multiple projects | [optional] [enum: issue] |
| **getListOfIssuesRequest** | [**GetListOfIssuesRequest**](GetListOfIssuesRequest.md)|  | [optional] |

### Return type

[**GetListOfIssues200Response**](GetListOfIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getListOfLatestIssues"></a>
# **getListOfLatestIssues**
> GetListOfIssues200Response getListOfLatestIssues(page, perPage, sortBy, order, groupBy, getListOfIssuesRequest)

Get list of latest issues



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ReportingApiApi apiInstance = new ReportingApiApi(defaultClient);
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page of results to request
    BigDecimal perPage = new BigDecimal("100"); // BigDecimal | The number of results to return per page (Maximum: 1000)
    String sortBy = "severity"; // String | The key to sort results by
    String order = "asc"; // String | The direction to sort results.
    String groupBy = "issue"; // String | Set to issue to group the same issue in multiple projects
    GetListOfIssuesRequest getListOfIssuesRequest = new GetListOfIssuesRequest(); // GetListOfIssuesRequest | 
    try {
      GetListOfIssues200Response result = apiInstance.getListOfLatestIssues(page, perPage, sortBy, order, groupBy, getListOfIssuesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApiApi#getListOfLatestIssues");
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
| **page** | **BigDecimal**| The page of results to request | [optional] |
| **perPage** | **BigDecimal**| The number of results to return per page (Maximum: 1000) | [optional] |
| **sortBy** | **String**| The key to sort results by | [optional] [enum: severity, issueTitle, projectName, isFixed, isPatched, isIgnored, introducedDate, isUpgradable, isPatchable, priorityScore] |
| **order** | **String**| The direction to sort results. | [optional] |
| **groupBy** | **String**| Set to issue to group the same issue in multiple projects | [optional] [enum: issue] |
| **getListOfIssuesRequest** | [**GetListOfIssuesRequest**](GetListOfIssuesRequest.md)|  | [optional] |

### Return type

[**GetListOfIssues200Response**](GetListOfIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getProjectCounts"></a>
# **getProjectCounts**
> GetProjectCounts200Response getProjectCounts(from, to, getProjectCountsRequest)

Get project counts



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ReportingApiApi apiInstance = new ReportingApiApi(defaultClient);
    String from = "2017-07-01"; // String | The date you wish to fetch results from, in the format `YYYY-MM-DD`
    String to = "2017-07-03"; // String | The date you wish to fetch results until, in the format `YYYY-MM-DD`
    GetProjectCountsRequest getProjectCountsRequest = new GetProjectCountsRequest(); // GetProjectCountsRequest | 
    try {
      GetProjectCounts200Response result = apiInstance.getProjectCounts(from, to, getProjectCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApiApi#getProjectCounts");
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
| **from** | **String**| The date you wish to fetch results from, in the format &#x60;YYYY-MM-DD&#x60; | |
| **to** | **String**| The date you wish to fetch results until, in the format &#x60;YYYY-MM-DD&#x60; | |
| **getProjectCountsRequest** | [**GetProjectCountsRequest**](GetProjectCountsRequest.md)|  | [optional] |

### Return type

[**GetProjectCounts200Response**](GetProjectCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getTestCounts"></a>
# **getTestCounts**
> GetTestCounts200Response getTestCounts(from, to, groupBy, getTestCountsRequest)

Get test counts



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ReportingApiApi apiInstance = new ReportingApiApi(defaultClient);
    String from = "2017-07-01"; // String | The date you wish to count tests from, in the format `YYYY-MM-DD`
    String to = "2017-07-03"; // String | The date you wish to count tests until, in the format `YYYY-MM-DD`
    String groupBy = "isPrivate"; // String | The field to group results by
    GetTestCountsRequest getTestCountsRequest = new GetTestCountsRequest(); // GetTestCountsRequest | 
    try {
      GetTestCounts200Response result = apiInstance.getTestCounts(from, to, groupBy, getTestCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApiApi#getTestCounts");
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
| **from** | **String**| The date you wish to count tests from, in the format &#x60;YYYY-MM-DD&#x60; | |
| **to** | **String**| The date you wish to count tests until, in the format &#x60;YYYY-MM-DD&#x60; | |
| **groupBy** | **String**| The field to group results by | [optional] [enum: isPrivate, issuesPrevented] |
| **getTestCountsRequest** | [**GetTestCountsRequest**](GetTestCountsRequest.md)|  | [optional] |

### Return type

[**GetTestCounts200Response**](GetTestCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |


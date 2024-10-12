# IssuesApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getV3Issues**](IssuesApi.md#getV3Issues) | **GET** /v3/issues | Get currently authenticated user&#39;s issues |


<a id="getV3Issues"></a>
# **getV3Issues**
> Issue getV3Issues(state, labels, milestone, orderBy, sort, page, perPage)

Get currently authenticated user&#39;s issues

Get currently authenticated user&#39;s issues

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String state = "opened"; // String | Return opened, closed, or all issues
    String labels = "labels_example"; // String | Comma-separated list of label names
    String milestone = "milestone_example"; // String | Return issues for a specific milestone
    String orderBy = "created_at"; // String | Return issues ordered by `created_at` or `updated_at` fields.
    String sort = "asc"; // String | Return issues sorted in `asc` or `desc` order.
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Issue result = apiInstance.getV3Issues(state, labels, milestone, orderBy, sort, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#getV3Issues");
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
| **state** | **String**| Return opened, closed, or all issues | [optional] [default to all] [enum: opened, closed, all] |
| **labels** | **String**| Comma-separated list of label names | [optional] |
| **milestone** | **String**| Return issues for a specific milestone | [optional] |
| **orderBy** | **String**| Return issues ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields. | [optional] [default to created_at] [enum: created_at, updated_at] |
| **sort** | **String**| Return issues sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order. | [optional] [default to desc] [enum: asc, desc] |
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get currently authenticated user&#39;s issues |  -  |


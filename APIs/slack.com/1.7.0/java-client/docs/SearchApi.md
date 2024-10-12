# SearchApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchMessages**](SearchApi.md#searchMessages) | **GET** /search.messages |  |


<a id="searchMessages"></a>
# **searchMessages**
> DefaultSuccessTemplate searchMessages(token, query, count, highlight, page, sort, sortDir)



Searches for messages matching a query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `search:read`
    String query = "query_example"; // String | Search query.
    Integer count = 56; // Integer | Pass the number of results you want per \"page\". Maximum of `100`.
    Boolean highlight = true; // Boolean | Pass a value of `true` to enable query highlight markers (see below).
    Integer page = 56; // Integer | 
    String sort = "sort_example"; // String | Return matches sorted by either `score` or `timestamp`.
    String sortDir = "sortDir_example"; // String | Change sort direction to ascending (`asc`) or descending (`desc`).
    try {
      DefaultSuccessTemplate result = apiInstance.searchMessages(token, query, count, highlight, page, sort, sortDir);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchMessages");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;search:read&#x60; | |
| **query** | **String**| Search query. | |
| **count** | **Integer**| Pass the number of results you want per \&quot;page\&quot;. Maximum of &#x60;100&#x60;. | [optional] |
| **highlight** | **Boolean**| Pass a value of &#x60;true&#x60; to enable query highlight markers (see below). | [optional] |
| **page** | **Integer**|  | [optional] |
| **sort** | **String**| Return matches sorted by either &#x60;score&#x60; or &#x60;timestamp&#x60;. | [optional] |
| **sortDir** | **String**| Change sort direction to ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |


# ReportingApi

All URIs are relative to *https://www.beanstream.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsPost**](ReportingApi.md#reportsPost) | **POST** /reports | Search Query |


<a id="reportsPost"></a>
# **reportsPost**
> SearchResult reportsPost(searchQuery)

Search Query

Query for transactions using a date range and optional search criteria. This method allows you to page your search results if you are expecting a lot of results to be returned. The page start value begins at 1. If no records are found the API will return a 404 error message. For details on the parameters and allowed values for Criteria please visit the documentation http://developer.beanstream.com/documentation/analyze-payments/search-specific-criteria/

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.beanstream.com/api/v1");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    SearchQuery searchQuery = new SearchQuery(); // SearchQuery | 
    try {
      SearchResult result = apiInstance.reportsPost(searchQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportsPost");
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
| **searchQuery** | [**SearchQuery**](SearchQuery.md)|  | [optional] |

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A transaction object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication Failure |  -  |
| **402** | Business Rule Violation or Decline |  -  |
| **403** | Authorization Failure |  -  |
| **405** | Invalid Request Method |  -  |
| **500** | Internal Server Error |  -  |


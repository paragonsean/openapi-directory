# BillNewsApi

All URIs are relative to *https://bills-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNewsArticles**](BillNewsApi.md#getNewsArticles) | **GET** /api/v1/Bills/{billId}/NewsArticles | Returns a list of news articles for a Bill. |


<a id="getNewsArticles"></a>
# **getNewsArticles**
> NewsArticlesSummarySearchResult getNewsArticles(billId, skip, take)

Returns a list of news articles for a Bill.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillNewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bills-api.parliament.uk");

    BillNewsApi apiInstance = new BillNewsApi(defaultClient);
    Integer billId = 56; // Integer | 
    Integer skip = 56; // Integer | 
    Integer take = 56; // Integer | 
    try {
      NewsArticlesSummarySearchResult result = apiInstance.getNewsArticles(billId, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillNewsApi#getNewsArticles");
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
| **billId** | **Integer**|  | |
| **skip** | **Integer**|  | [optional] |
| **take** | **Integer**|  | [optional] |

### Return type

[**NewsArticlesSummarySearchResult**](NewsArticlesSummarySearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |


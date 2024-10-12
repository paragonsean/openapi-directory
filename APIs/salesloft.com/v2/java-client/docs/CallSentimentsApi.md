# CallSentimentsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CallSentimentsJsonGet**](CallSentimentsApi.md#v2CallSentimentsJsonGet) | **GET** /v2/call_sentiments.json | List call sentiments |


<a id="v2CallSentimentsJsonGet"></a>
# **v2CallSentimentsJsonGet**
> List&lt;CallSentiment&gt; v2CallSentimentsJsonGet(name, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List call sentiments

Fetches multiple call sentiment records. The records can be sorted according to the respective parameters. Call sentiments must be configured in application. This will change in the future, but please contact us if you have a pressing use case. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallSentimentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    CallSentimentsApi apiInstance = new CallSentimentsApi(defaultClient);
    String name = "name_example"; // String | Filters call sentiments by name
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: name, updated_at. Defaults to name
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to ASC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<CallSentiment> result = apiInstance.v2CallSentimentsJsonGet(name, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallSentimentsApi#v2CallSentimentsJsonGet");
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
| **name** | **String**| Filters call sentiments by name | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: name, updated_at. Defaults to name | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to ASC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;CallSentiment&gt;**](CallSentiment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


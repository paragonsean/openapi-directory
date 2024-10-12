# SeoApi

All URIs are relative to *http://,*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**seoLatestRankings**](SeoApi.md#seoLatestRankings) | **GET** /api/seo/ranking/latest | SEO Latest Rankings |


<a id="seoLatestRankings"></a>
# **seoLatestRankings**
> seoLatestRankings()

SEO Latest Rankings

This resource lists all pricing rules that are currently saved in you account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://,");

    SeoApi apiInstance = new SeoApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.seoLatestRankings();
    } catch (ApiException e) {
      System.err.println("Exception when calling SeoApi#seoLatestRankings");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |


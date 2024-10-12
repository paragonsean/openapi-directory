# CuratedSetsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**curatedSetsSlugGet**](CuratedSetsApi.md#curatedSetsSlugGet) | **GET** /curated_sets/{slug} |  |


<a id="curatedSetsSlugGet"></a>
# **curatedSetsSlugGet**
> curatedSetsSlugGet(slug)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CuratedSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    CuratedSetsApi apiInstance = new CuratedSetsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.curatedSetsSlugGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling CuratedSetsApi#curatedSetsSlugGet");
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
| **slug** | **String**|  | |

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
| **0** | Unexpected error |  -  |


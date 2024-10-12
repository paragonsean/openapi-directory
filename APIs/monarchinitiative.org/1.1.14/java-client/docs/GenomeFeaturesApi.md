# GenomeFeaturesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFeaturesWithinResource**](GenomeFeaturesApi.md#getFeaturesWithinResource) | **GET** /genome/features/within/{build}/{reference}/{begin}/{end} | Returns list of matches |


<a id="getFeaturesWithinResource"></a>
# **getFeaturesWithinResource**
> List&lt;SequenceFeature&gt; getFeaturesWithinResource(build, reference, begin, end)

Returns list of matches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenomeFeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    GenomeFeaturesApi apiInstance = new GenomeFeaturesApi(defaultClient);
    String build = "build_example"; // String | 
    String reference = "reference_example"; // String | 
    String begin = "begin_example"; // String | 
    String end = "end_example"; // String | 
    try {
      List<SequenceFeature> result = apiInstance.getFeaturesWithinResource(build, reference, begin, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenomeFeaturesApi#getFeaturesWithinResource");
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
| **build** | **String**|  | |
| **reference** | **String**|  | |
| **begin** | **String**|  | |
| **end** | **String**|  | |

### Return type

[**List&lt;SequenceFeature&gt;**](SequenceFeature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


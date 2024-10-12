# SearchApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSearch_0**](SearchApi.md#getSearch_0) | **GET** /platform/public/search | Search for a disease or a target |


<a id="getSearch_0"></a>
# **getSearch_0**
> getSearch_0(q, size, from, filter)

Search for a disease or a target

This method allows you to look for gene or diseases of interest using a free text search, replicating the functionality of the search box on our homepage. It should be used to identify the best match for a disease or target of interest, rather than gathering a specific set of evidence. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | A full text query.
    String size = "size_example"; // String | Maximum amount of results to return. Defaults to 10, max is 10000.
    String from = "from_example"; // String | How many initial results should be skipped. Defaults to 0.
    String filter = "filter_example"; // String | Restrict the search to the type requested. Eg. `target` or `disease`.
    try {
      apiInstance.getSearch_0(q, size, from, filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSearch_0");
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
| **q** | **String**| A full text query. | |
| **size** | **String**| Maximum amount of results to return. Defaults to 10, max is 10000. | [optional] |
| **from** | **String**| How many initial results should be skipped. Defaults to 0. | [optional] |
| **filter** | **String**| Restrict the search to the type requested. Eg. &#x60;target&#x60; or &#x60;disease&#x60;. | [optional] |

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
| **200** | Successful response |  -  |


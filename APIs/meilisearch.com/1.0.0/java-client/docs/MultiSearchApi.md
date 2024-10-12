# MultiSearchApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchOneOrMoreIndexes**](MultiSearchApi.md#searchOneOrMoreIndexes) | **POST** /multi-search | Search one or more indexes |


<a id="searchOneOrMoreIndexes"></a>
# **searchOneOrMoreIndexes**
> searchOneOrMoreIndexes(searchOneOrMoreIndexesRequest)

Search one or more indexes

Search one or more indexes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultiSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    MultiSearchApi apiInstance = new MultiSearchApi(defaultClient);
    SearchOneOrMoreIndexesRequest searchOneOrMoreIndexesRequest = new SearchOneOrMoreIndexesRequest(); // SearchOneOrMoreIndexesRequest | 
    try {
      apiInstance.searchOneOrMoreIndexes(searchOneOrMoreIndexesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultiSearchApi#searchOneOrMoreIndexes");
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
| **searchOneOrMoreIndexesRequest** | [**SearchOneOrMoreIndexesRequest**](SearchOneOrMoreIndexesRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |


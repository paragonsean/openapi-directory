# SearchApi

All URIs are relative to *http://vmware.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchEntities**](SearchApi.md#searchEntities) | **POST** /search | Search entities |


<a id="searchEntities"></a>
# **searchEntities**
> PagedListResponseWithTime searchEntities(searchRequest)

Search entities

Using search API you can search vRealize Network Insight entities by specifying entity type and filter expression. A filter expression is a predicate expression (similar to SQL where clause) used to define the search criteria. Please refer to API Guide on details of how to construct filter expression. A successful search request will return a list of entity ids that matches the search criteria.

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
    defaultClient.setBasePath("http://vmware.local");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    SearchRequest searchRequest = new SearchRequest(); // SearchRequest | Search Request
    try {
      PagedListResponseWithTime result = apiInstance.searchEntities(searchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchEntities");
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
| **searchRequest** | [**SearchRequest**](SearchRequest.md)| Search Request | [optional] |

### Return type

[**PagedListResponseWithTime**](PagedListResponseWithTime.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |


# SearchApi

All URIs are relative to *https://api.isbndb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchGet**](SearchApi.md#searchGet) | **GET** /search | Search all ISBNDB databases |


<a id="searchGet"></a>
# **searchGet**
> searchGet(q)

Search all ISBNDB databases

Uses a free query string compatible with ElasticSearch 6 to search in any of the ISBNDB&#39;s databases

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
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | A query string compatible with ElasticSearch 6
    try {
      apiInstance.searchGet(q);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchGet");
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
| **q** | **String**| A query string compatible with ElasticSearch 6 | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results were found in the requested database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | No results found in the requested database |  -  |


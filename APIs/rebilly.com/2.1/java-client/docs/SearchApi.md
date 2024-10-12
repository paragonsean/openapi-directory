# SearchApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSearch**](SearchApi.md#getSearch) | **GET** /search | Search merchant data |


<a id="getSearch"></a>
# **getSearch**
> List&lt;Search&gt; getSearch(organizationId, sort, limit, offset, q)

Search merchant data

Search merchant&#39;s data to return resources such as customers, invoices, orders, transactions. 

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
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    List<String> sort = Arrays.asList(); // List<String> | The collection items sort field and order (prefix with \"-\" for descending sort).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    String q = "q_example"; // String | The default search. It will search across resources and many fields.
    try {
      List<Search> result = apiInstance.getSearch(organizationId, sort, limit, offset, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSearch");
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
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |
| **q** | **String**| The default search. It will search across resources and many fields. | [optional] |

### Return type

[**List&lt;Search&gt;**](Search.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Results keyed by resource. |  * Pagination-Limit -  <br>  * Pagination-Offset -  <br>  * Pagination-Total -  <br>  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |


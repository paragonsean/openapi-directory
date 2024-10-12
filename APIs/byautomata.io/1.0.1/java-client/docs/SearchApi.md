# SearchApi

All URIs are relative to *https://api.byautomata.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchGet**](SearchApi.md#searchGet) | **GET** /search | Send search terms to receive the most relevant companies along with text snippets. |


<a id="searchGet"></a>
# **searchGet**
> SearchGet200Response searchGet(terms, page)

Send search terms to receive the most relevant companies along with text snippets.

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
    defaultClient.setBasePath("https://api.byautomata.io");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String terms = "terms_example"; // String | We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link=cloud+computing,enterprise,security
    String page = "0"; // String | Page number of search results. Ex. https://api.byautomata.io/search?page=0&link=cloud+computing,enterprise,security
    try {
      SearchGet200Response result = apiInstance.searchGet(terms, page);
      System.out.println(result);
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
| **terms** | [**String**](.md)| We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link&#x3D;cloud+computing,enterprise,security | |
| **page** | [**String**](.md)| Page number of search results. Ex. https://api.byautomata.io/search?page&#x3D;0&amp;link&#x3D;cloud+computing,enterprise,security | [optional] [default to 0] |

### Return type

[**SearchGet200Response**](SearchGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation |  -  |
| **400** | Your request was not valid. Please refer to the API documentation https://api-specs.byautomata.io. |  -  |
| **403** | Invalid API Key. Please refer to the API documentation https://api-specs.byautomata.io. |  -  |
| **501** | There was a server error. Please try again later or contact support@byautomata.io |  -  |


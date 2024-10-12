# FacetsApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**facetsFacetGet**](FacetsApi.md#facetsFacetGet) | **GET** /facets/{facet} | Returns facets |


<a id="facetsFacetGet"></a>
# **facetsFacetGet**
> List&lt;Facet&gt; facetsFacetGet(facet, scope, docType, term, offset, limit)

Returns facets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    FacetsApi apiInstance = new FacetsApi(defaultClient);
    String facet = "sender"; // String | The facet to search for
    String scope = "scope_example"; // String | The scope of the result set, i.e. 'indices' or a WeGA ID
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    String term = "term_example"; // String | The search term to be looked for in the facet's label
    Integer offset = 1; // Integer | Position of first item to retrieve (starting from 1)
    Integer limit = 10; // Integer | Number of items to retrieve (200 max)
    try {
      List<Facet> result = apiInstance.facetsFacetGet(facet, scope, docType, term, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacetsApi#facetsFacetGet");
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
| **facet** | **String**| The facet to search for | [enum: sender, addressee] |
| **scope** | **String**| The scope of the result set, i.e. &#39;indices&#39; or a WeGA ID | |
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |
| **term** | **String**| The search term to be looked for in the facet&#39;s label | [optional] |
| **offset** | **Integer**| Position of first item to retrieve (starting from 1) | [optional] [default to 1] |
| **limit** | **Integer**| Number of items to retrieve (200 max) | [optional] [default to 10] |

### Return type

[**List&lt;Facet&gt;**](Facet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of facets |  * totalrecordcount - The total size of the result set <br>  |
| **0** | Unexpected error |  -  |


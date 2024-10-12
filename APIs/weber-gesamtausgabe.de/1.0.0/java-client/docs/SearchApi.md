# SearchApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchEntityGet**](SearchApi.md#searchEntityGet) | **GET** /search/entity | Search for a WeGA entity |


<a id="searchEntityGet"></a>
# **searchEntityGet**
> List&lt;Document&gt; searchEntityGet(docType, q, offset, limit)

Search for a WeGA entity

This endpoint returns the search results for an entity&#39;s name or title. 

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
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    String q = "q_example"; // String | The query string
    Integer offset = 1; // Integer | Position of first item to retrieve (starting from 1)
    Integer limit = 10; // Integer | Number of items to retrieve (200 max)
    try {
      List<Document> result = apiInstance.searchEntityGet(docType, q, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchEntityGet");
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
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [optional] [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |
| **q** | **String**| The query string | [optional] |
| **offset** | **Integer**| Position of first item to retrieve (starting from 1) | [optional] [default to 1] |
| **limit** | **Integer**| Number of items to retrieve (200 max) | [optional] [default to 10] |

### Return type

[**List&lt;Document&gt;**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of documents |  * totalrecordcount - The total size of the result set <br>  |
| **0** | Unexpected error |  -  |


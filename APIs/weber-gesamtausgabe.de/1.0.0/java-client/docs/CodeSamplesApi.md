# CodeSamplesApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**codeFindByElementElementGet**](CodeSamplesApi.md#codeFindByElementElementGet) | **GET** /code/findByElement/{element} | Finds code samples by XML element |


<a id="codeFindByElementElementGet"></a>
# **codeFindByElementElementGet**
> List&lt;CodeSample&gt; codeFindByElementElementGet(element, namespace, docType, offset, limit)

Finds code samples by XML element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeSamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    CodeSamplesApi apiInstance = new CodeSamplesApi(defaultClient);
    String element = "element_example"; // String | The XML element to search for
    String namespace = "http://www.tei-c.org/ns/1.0"; // String | The element namespace. Defaults to the TEI namespace
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    Integer offset = 1; // Integer | Position of first item to retrieve (starting from 1)
    Integer limit = 10; // Integer | Number of items to retrieve (200 max)
    try {
      List<CodeSample> result = apiInstance.codeFindByElementElementGet(element, namespace, docType, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeSamplesApi#codeFindByElementElementGet");
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
| **element** | **String**| The XML element to search for | |
| **namespace** | **String**| The element namespace. Defaults to the TEI namespace | [optional] [default to http://www.tei-c.org/ns/1.0] |
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [optional] [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |
| **offset** | **Integer**| Position of first item to retrieve (starting from 1) | [optional] [default to 1] |
| **limit** | **Integer**| Number of items to retrieve (200 max) | [optional] [default to 10] |

### Return type

[**List&lt;CodeSample&gt;**](CodeSample.md)

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


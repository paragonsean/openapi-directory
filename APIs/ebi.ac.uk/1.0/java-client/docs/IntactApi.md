# IntactApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIntactUsingGET**](IntactApi.md#getIntactUsingGET) | **GET** /intact | Molecular Interactions collected from IntAct |


<a id="getIntactUsingGET"></a>
# **getIntactUsingGET**
> IntactInteractions getIntactUsingGET(accession, confidence, gene, limit, page)

Molecular Interactions collected from IntAct

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    IntactApi apiInstance = new IntactApi(defaultClient);
    List<String> accession = Arrays.asList(); // List<String> | accession
    Double confidence = 3.4D; // Double | confidence
    List<String> gene = Arrays.asList(); // List<String> | gene
    Integer limit = 10; // Integer | limit
    Integer page = 0; // Integer | page
    try {
      IntactInteractions result = apiInstance.getIntactUsingGET(accession, confidence, gene, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntactApi#getIntactUsingGET");
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
| **accession** | [**List&lt;String&gt;**](String.md)| accession | [optional] |
| **confidence** | **Double**| confidence | [optional] |
| **gene** | [**List&lt;String&gt;**](String.md)| gene | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **page** | **Integer**| page | [optional] [default to 0] |

### Return type

[**IntactInteractions**](IntactInteractions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |


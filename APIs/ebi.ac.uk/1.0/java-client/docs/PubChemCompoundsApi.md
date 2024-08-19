# PubChemCompoundsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompoundsUsingGET**](PubChemCompoundsApi.md#getCompoundsUsingGET) | **GET** /pubchem/compounds | Get pubchem compounds |


<a id="getCompoundsUsingGET"></a>
# **getCompoundsUsingGET**
> PubchemCompounds getCompoundsUsingGET(canonicalSmiles, cid, inchiKey, limit, page)

Get pubchem compounds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PubChemCompoundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    PubChemCompoundsApi apiInstance = new PubChemCompoundsApi(defaultClient);
    List<String> canonicalSmiles = Arrays.asList(); // List<String> | canonicalSmiles
    List<String> cid = Arrays.asList(); // List<String> | cid
    List<String> inchiKey = Arrays.asList(); // List<String> | inchiKey
    Integer limit = 10; // Integer | limit
    Integer page = 0; // Integer | page
    try {
      PubchemCompounds result = apiInstance.getCompoundsUsingGET(canonicalSmiles, cid, inchiKey, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PubChemCompoundsApi#getCompoundsUsingGET");
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
| **canonicalSmiles** | [**List&lt;String&gt;**](String.md)| canonicalSmiles | [optional] |
| **cid** | [**List&lt;String&gt;**](String.md)| cid | [optional] |
| **inchiKey** | [**List&lt;String&gt;**](String.md)| inchiKey | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **page** | **Integer**| page | [optional] [default to 0] |

### Return type

[**PubchemCompounds**](PubchemCompounds.md)

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


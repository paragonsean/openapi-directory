# PubChemBiossaysApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBioassaysUsingGET**](PubChemBiossaysApi.md#getBioassaysUsingGET) | **GET** /pubchem/bioassays | Get pubchem bioassays |


<a id="getBioassaysUsingGET"></a>
# **getBioassaysUsingGET**
> Bioassays getBioassaysUsingGET(accession, assayPubchemId, limit, ncbiProteinId, page)

Get pubchem bioassays

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PubChemBiossaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    PubChemBiossaysApi apiInstance = new PubChemBiossaysApi(defaultClient);
    List<String> accession = Arrays.asList(); // List<String> | accession
    List<String> assayPubchemId = Arrays.asList(); // List<String> | assayPubchemId
    Integer limit = 1; // Integer | limit
    List<String> ncbiProteinId = Arrays.asList(); // List<String> | ncbiProteinId
    Integer page = 0; // Integer | page
    try {
      Bioassays result = apiInstance.getBioassaysUsingGET(accession, assayPubchemId, limit, ncbiProteinId, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PubChemBiossaysApi#getBioassaysUsingGET");
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
| **assayPubchemId** | [**List&lt;String&gt;**](String.md)| assayPubchemId | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 1] |
| **ncbiProteinId** | [**List&lt;String&gt;**](String.md)| ncbiProteinId | [optional] |
| **page** | **Integer**| page | [optional] [default to 0] |

### Return type

[**Bioassays**](Bioassays.md)

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


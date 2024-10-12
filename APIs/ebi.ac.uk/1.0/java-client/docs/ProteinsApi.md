# ProteinsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProteinsUsingGET**](ProteinsApi.md#getProteinsUsingGET) | **GET** /proteins | Proteins collected from Uniprot for selective tax ids  HUMAN(9606), MOUSE(10090), RAT(10116), BOVINE(9913), ESCHERICHIA_COLI(83333), SUS_SCROFA(9823), MYCOBACTERIUM_TUBERCULOSIS(83332), ORYCTOLAGUS_CUNICULUS(9986), SACCHAROMYCES_CEREVISIAE(559292), CVHSA(694009) &amp; SARS2(2697049) |


<a id="getProteinsUsingGET"></a>
# **getProteinsUsingGET**
> Proteins getProteinsUsingGET(accession, ec, fullName, gene, go, interpro, limit, omim, orphanet, page, pfam, reactome, taxId)

Proteins collected from Uniprot for selective tax ids  HUMAN(9606), MOUSE(10090), RAT(10116), BOVINE(9913), ESCHERICHIA_COLI(83333), SUS_SCROFA(9823), MYCOBACTERIUM_TUBERCULOSIS(83332), ORYCTOLAGUS_CUNICULUS(9986), SACCHAROMYCES_CEREVISIAE(559292), CVHSA(694009) &amp; SARS2(2697049)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProteinsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    ProteinsApi apiInstance = new ProteinsApi(defaultClient);
    List<String> accession = Arrays.asList(); // List<String> | accession
    List<String> ec = Arrays.asList(); // List<String> | ec
    List<String> fullName = Arrays.asList(); // List<String> | fullName
    List<String> gene = Arrays.asList(); // List<String> | gene
    List<String> go = Arrays.asList(); // List<String> | go
    List<String> interpro = Arrays.asList(); // List<String> | interpro
    Integer limit = 10; // Integer | limit
    List<String> omim = Arrays.asList(); // List<String> | omim
    List<String> orphanet = Arrays.asList(); // List<String> | orphanet
    Integer page = 0; // Integer | page
    List<String> pfam = Arrays.asList(); // List<String> | pfam
    List<String> reactome = Arrays.asList(); // List<String> | reactome
    List<Integer> taxId = Arrays.asList(); // List<Integer> | taxId
    try {
      Proteins result = apiInstance.getProteinsUsingGET(accession, ec, fullName, gene, go, interpro, limit, omim, orphanet, page, pfam, reactome, taxId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProteinsApi#getProteinsUsingGET");
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
| **ec** | [**List&lt;String&gt;**](String.md)| ec | [optional] |
| **fullName** | [**List&lt;String&gt;**](String.md)| fullName | [optional] |
| **gene** | [**List&lt;String&gt;**](String.md)| gene | [optional] |
| **go** | [**List&lt;String&gt;**](String.md)| go | [optional] |
| **interpro** | [**List&lt;String&gt;**](String.md)| interpro | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **omim** | [**List&lt;String&gt;**](String.md)| omim | [optional] |
| **orphanet** | [**List&lt;String&gt;**](String.md)| orphanet | [optional] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **pfam** | [**List&lt;String&gt;**](String.md)| pfam | [optional] |
| **reactome** | [**List&lt;String&gt;**](String.md)| reactome | [optional] |
| **taxId** | [**List&lt;Integer&gt;**](Integer.md)| taxId | [optional] |

### Return type

[**Proteins**](Proteins.md)

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


# PubChemBioassaySidsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBioassaysUsingGET1**](PubChemBioassaySidsApi.md#getBioassaysUsingGET1) | **GET** /pubchem/bioassays/sids | Get pubchem bioassays associated to particular substance ids (sid) &amp; outcome |


<a id="getBioassaysUsingGET1"></a>
# **getBioassaysUsingGET1**
> Bioassays getBioassaysUsingGET1(limit, outcome, page, sids)

Get pubchem bioassays associated to particular substance ids (sid) &amp; outcome

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PubChemBioassaySidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    PubChemBioassaySidsApi apiInstance = new PubChemBioassaySidsApi(defaultClient);
    Integer limit = 10; // Integer | limit
    String outcome = "outcome_example"; // String | outcome
    Integer page = 0; // Integer | page
    List<String> sids = Arrays.asList(); // List<String> | sids
    try {
      Bioassays result = apiInstance.getBioassaysUsingGET1(limit, outcome, page, sids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PubChemBioassaySidsApi#getBioassaysUsingGET1");
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
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **outcome** | **String**| outcome | [optional] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **sids** | [**List&lt;String&gt;**](String.md)| sids | [optional] |

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


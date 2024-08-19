# MoleculesApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMoleculesUsingGET**](MoleculesApi.md#getMoleculesUsingGET) | **GET** /molecules | Get ChEMBL molecules |


<a id="getMoleculesUsingGET"></a>
# **getMoleculesUsingGET**
> Molecules getMoleculesUsingGET(canonicalSmiles, inchiKey, limit, moleculeChemblId, page)

Get ChEMBL molecules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MoleculesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    MoleculesApi apiInstance = new MoleculesApi(defaultClient);
    List<String> canonicalSmiles = Arrays.asList(); // List<String> | canonicalSmiles
    List<String> inchiKey = Arrays.asList(); // List<String> | inchiKey
    Integer limit = 10; // Integer | limit
    List<String> moleculeChemblId = Arrays.asList(); // List<String> | moleculeChemblId
    Integer page = 0; // Integer | page
    try {
      Molecules result = apiInstance.getMoleculesUsingGET(canonicalSmiles, inchiKey, limit, moleculeChemblId, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MoleculesApi#getMoleculesUsingGET");
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
| **inchiKey** | [**List&lt;String&gt;**](String.md)| inchiKey | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **moleculeChemblId** | [**List&lt;String&gt;**](String.md)| moleculeChemblId | [optional] |
| **page** | **Integer**| page | [optional] [default to 0] |

### Return type

[**Molecules**](Molecules.md)

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


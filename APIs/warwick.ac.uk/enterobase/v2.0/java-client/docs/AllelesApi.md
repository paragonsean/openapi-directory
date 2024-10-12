# AllelesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseSchemeAllelesGet**](AllelesApi.md#apiV20DatabaseSchemeAllelesGet) | **GET** /api/v2.0/{database}/{scheme}/alleles |  |


<a id="apiV20DatabaseSchemeAllelesGet"></a>
# **apiV20DatabaseSchemeAllelesGet**
> apiV20DatabaseSchemeAllelesGet(locus, database, scheme, barcode, offset, alleleId, onlyFields, seq, reldate, limit)



Alleles  data 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllelesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AllelesApi apiInstance = new AllelesApi(defaultClient);
    String locus = "locus_example"; // String | 
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String scheme = "scheme_example"; // String | 
    List<String> barcode = Arrays.asList(); // List<String> | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    Integer offset = 0; // Integer | 
    String alleleId = "alleleId_example"; // String | 
    List<String> onlyFields = Arrays.asList(); // List<String> | 
    String seq = "seq_example"; // String | 
    Integer reldate = 56; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      apiInstance.apiV20DatabaseSchemeAllelesGet(locus, database, scheme, barcode, offset, alleleId, onlyFields, seq, reldate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllelesApi#apiV20DatabaseSchemeAllelesGet");
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
| **locus** | **String**|  | |
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **scheme** | **String**|  | |
| **barcode** | [**List&lt;String&gt;**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **alleleId** | **String**|  | [optional] |
| **onlyFields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **seq** | **String**|  | [optional] |
| **reldate** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of alleles objects |  -  |
| **400** | Malformed request, contains an error |  -  |
| **403** | Unauthorised access for this specific resource |  -  |


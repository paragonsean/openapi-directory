# EfoDiseaseTermsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEFOUsingGET**](EfoDiseaseTermsApi.md#getEFOUsingGET) | **GET** /efo | Get EFO diseases data |


<a id="getEFOUsingGET"></a>
# **getEFOUsingGET**
> EFOEntities getEFOUsingGET(doid, label, limit, mesh, oboId, omimId, page, synonym)

Get EFO diseases data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EfoDiseaseTermsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    EfoDiseaseTermsApi apiInstance = new EfoDiseaseTermsApi(defaultClient);
    List<String> doid = Arrays.asList(); // List<String> | doid
    List<String> label = Arrays.asList(); // List<String> | label
    Integer limit = 10; // Integer | limit
    List<String> mesh = Arrays.asList(); // List<String> | mesh
    List<String> oboId = Arrays.asList(); // List<String> | oboId
    List<String> omimId = Arrays.asList(); // List<String> | omimId
    Integer page = 0; // Integer | page
    List<String> synonym = Arrays.asList(); // List<String> | synonym
    try {
      EFOEntities result = apiInstance.getEFOUsingGET(doid, label, limit, mesh, oboId, omimId, page, synonym);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EfoDiseaseTermsApi#getEFOUsingGET");
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
| **doid** | [**List&lt;String&gt;**](String.md)| doid | [optional] |
| **label** | [**List&lt;String&gt;**](String.md)| label | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **mesh** | [**List&lt;String&gt;**](String.md)| mesh | [optional] |
| **oboId** | [**List&lt;String&gt;**](String.md)| oboId | [optional] |
| **omimId** | [**List&lt;String&gt;**](String.md)| omimId | [optional] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **synonym** | [**List&lt;String&gt;**](String.md)| synonym | [optional] |

### Return type

[**EFOEntities**](EFOEntities.md)

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


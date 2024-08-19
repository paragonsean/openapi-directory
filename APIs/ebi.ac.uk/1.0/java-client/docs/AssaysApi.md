# AssaysApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssaysUsingGET**](AssaysApi.md#getAssaysUsingGET) | **GET** /assays | Get ChEMBL assays |


<a id="getAssaysUsingGET"></a>
# **getAssaysUsingGET**
> Assays getAssaysUsingGET(assayChemblId, assayOrg, assayType, limit, page, targetChemblId)

Get ChEMBL assays

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    AssaysApi apiInstance = new AssaysApi(defaultClient);
    List<String> assayChemblId = Arrays.asList(); // List<String> | assayChemblId
    List<String> assayOrg = Arrays.asList(); // List<String> | assayOrg
    List<String> assayType = Arrays.asList(); // List<String> | assayType
    Integer limit = 10; // Integer | limit
    Integer page = 0; // Integer | page
    List<String> targetChemblId = Arrays.asList(); // List<String> | targetChemblId
    try {
      Assays result = apiInstance.getAssaysUsingGET(assayChemblId, assayOrg, assayType, limit, page, targetChemblId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssaysApi#getAssaysUsingGET");
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
| **assayChemblId** | [**List&lt;String&gt;**](String.md)| assayChemblId | [optional] |
| **assayOrg** | [**List&lt;String&gt;**](String.md)| assayOrg | [optional] |
| **assayType** | [**List&lt;String&gt;**](String.md)| assayType | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **targetChemblId** | [**List&lt;String&gt;**](String.md)| targetChemblId | [optional] |

### Return type

[**Assays**](Assays.md)

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


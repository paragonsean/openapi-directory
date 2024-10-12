# PairSimApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPairSimJaccardResource**](PairSimApi.md#getPairSimJaccardResource) | **GET** /pair/sim/jaccard/{id1}/{id2} | Get pairwise similarity |


<a id="getPairSimJaccardResource"></a>
# **getPairSimJaccardResource**
> getPairSimJaccardResource(id2, id1, objectCategory)

Get pairwise similarity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PairSimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    PairSimApi apiInstance = new PairSimApi(defaultClient);
    String id2 = "id2_example"; // String | id, e.g. NCBIGene:1200; ZFIN:ZDB-GENE-980528-2059; UniProtKB:P12644
    String id1 = "id1_example"; // String | id, e.g. NCBIGene:10891; ZFIN:ZDB-GENE-980526-166; UniProtKB:Q15465
    String objectCategory = "objectCategory_example"; // String | e.g. disease, phenotype, gene. Two subjects will be compared based on overlap between associations to objects in this category
    try {
      apiInstance.getPairSimJaccardResource(id2, id1, objectCategory);
    } catch (ApiException e) {
      System.err.println("Exception when calling PairSimApi#getPairSimJaccardResource");
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
| **id2** | **String**| id, e.g. NCBIGene:1200; ZFIN:ZDB-GENE-980528-2059; UniProtKB:P12644 | |
| **id1** | **String**| id, e.g. NCBIGene:10891; ZFIN:ZDB-GENE-980526-166; UniProtKB:Q15465 | |
| **objectCategory** | **String**| e.g. disease, phenotype, gene. Two subjects will be compared based on overlap between associations to objects in this category | [optional] |

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
| **200** | Success |  -  |


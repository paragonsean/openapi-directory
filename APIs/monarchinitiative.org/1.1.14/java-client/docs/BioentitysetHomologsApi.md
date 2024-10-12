# BioentitysetHomologsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEntitySetHomologs**](BioentitysetHomologsApi.md#getEntitySetHomologs) | **GET** /bioentityset/homologs/ | Returns homology associations for a given input set of genes |


<a id="getEntitySetHomologs"></a>
# **getEntitySetHomologs**
> List&lt;AssociationResults&gt; getEntitySetHomologs(subject)

Returns homology associations for a given input set of genes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetHomologsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetHomologsApi apiInstance = new BioentitysetHomologsApi(defaultClient);
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    try {
      List<AssociationResults> result = apiInstance.getEntitySetHomologs(subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetHomologsApi#getEntitySetHomologs");
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
| **subject** | [**List&lt;String&gt;**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] |

### Return type

[**List&lt;AssociationResults&gt;**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


# EnrichmentWebServiceApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEnrichmentDataUsingPOST**](EnrichmentWebServiceApi.md#getEnrichmentDataUsingPOST) | **POST** /enrichment/annotatedGenes | Return a list of genes annotated to the term.Genes are rgdids separated by comma.Species type is an integer value.term is the ontology |
| [**getEnrichmentDataUsingPOST1**](EnrichmentWebServiceApi.md#getEnrichmentDataUsingPOST1) | **POST** /enrichment/data | Return a chart of ontology terms annotated to the genes.Genes are rgdids separated by comma.Species type is an integer value.Aspect is the Ontology group |


<a id="getEnrichmentDataUsingPOST"></a>
# **getEnrichmentDataUsingPOST**
> Object getEnrichmentDataUsingPOST(enrichmentGeneRequest)

Return a list of genes annotated to the term.Genes are rgdids separated by comma.Species type is an integer value.term is the ontology

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnrichmentWebServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    EnrichmentWebServiceApi apiInstance = new EnrichmentWebServiceApi(defaultClient);
    EnrichmentGeneRequest enrichmentGeneRequest = new EnrichmentGeneRequest(); // EnrichmentGeneRequest | geneRequest
    try {
      Object result = apiInstance.getEnrichmentDataUsingPOST(enrichmentGeneRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnrichmentWebServiceApi#getEnrichmentDataUsingPOST");
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
| **enrichmentGeneRequest** | [**EnrichmentGeneRequest**](EnrichmentGeneRequest.md)| geneRequest | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEnrichmentDataUsingPOST1"></a>
# **getEnrichmentDataUsingPOST1**
> Object getEnrichmentDataUsingPOST1(enrichmentRequest)

Return a chart of ontology terms annotated to the genes.Genes are rgdids separated by comma.Species type is an integer value.Aspect is the Ontology group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnrichmentWebServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    EnrichmentWebServiceApi apiInstance = new EnrichmentWebServiceApi(defaultClient);
    EnrichmentRequest enrichmentRequest = new EnrichmentRequest(); // EnrichmentRequest | enrichmentRequest
    try {
      Object result = apiInstance.getEnrichmentDataUsingPOST1(enrichmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnrichmentWebServiceApi#getEnrichmentDataUsingPOST1");
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
| **enrichmentRequest** | [**EnrichmentRequest**](EnrichmentRequest.md)| enrichmentRequest | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |


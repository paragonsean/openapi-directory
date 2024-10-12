# BioentitysetApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEntitySetAssociations**](BioentitysetApi.md#getEntitySetAssociations) | **GET** /bioentityset/associations | Returns compact associations for a given input set |
| [**getEntitySetGraphResource**](BioentitysetApi.md#getEntitySetGraphResource) | **GET** /bioentityset/graph | TODO Graph object spanning all entities |
| [**getEntitySetSummary**](BioentitysetApi.md#getEntitySetSummary) | **GET** /bioentityset/descriptor/counts | Summary statistics for objects associated |
| [**getOverRepresentation**](BioentitysetApi.md#getOverRepresentation) | **GET** /bioentityset/overrepresentation | Summary statistics for objects associated |


<a id="getEntitySetAssociations"></a>
# **getEntitySetAssociations**
> List&lt;AssociationResults&gt; getEntitySetAssociations(subject, background, objectCategory, objectSlim)

Returns compact associations for a given input set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetApi apiInstance = new BioentitysetApi(defaultClient);
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    List<String> background = Arrays.asList(); // List<String> | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    String objectCategory = "objectCategory_example"; // String | E.g. phenotype, function
    String objectSlim = "objectSlim_example"; // String | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
    try {
      List<AssociationResults> result = apiInstance.getEntitySetAssociations(subject, background, objectCategory, objectSlim);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetApi#getEntitySetAssociations");
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
| **background** | [**List&lt;String&gt;**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] |
| **objectCategory** | **String**| E.g. phenotype, function | [optional] |
| **objectSlim** | **String**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] |

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

<a id="getEntitySetGraphResource"></a>
# **getEntitySetGraphResource**
> getEntitySetGraphResource(subject, background, objectCategory, objectSlim)

TODO Graph object spanning all entities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetApi apiInstance = new BioentitysetApi(defaultClient);
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    List<String> background = Arrays.asList(); // List<String> | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    String objectCategory = "objectCategory_example"; // String | E.g. phenotype, function
    String objectSlim = "objectSlim_example"; // String | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
    try {
      apiInstance.getEntitySetGraphResource(subject, background, objectCategory, objectSlim);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetApi#getEntitySetGraphResource");
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
| **background** | [**List&lt;String&gt;**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] |
| **objectCategory** | **String**| E.g. phenotype, function | [optional] |
| **objectSlim** | **String**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] |

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

<a id="getEntitySetSummary"></a>
# **getEntitySetSummary**
> getEntitySetSummary(subject, background, objectCategory, objectSlim)

Summary statistics for objects associated

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetApi apiInstance = new BioentitysetApi(defaultClient);
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    List<String> background = Arrays.asList(); // List<String> | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    String objectCategory = "objectCategory_example"; // String | E.g. phenotype, function
    String objectSlim = "objectSlim_example"; // String | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
    try {
      apiInstance.getEntitySetSummary(subject, background, objectCategory, objectSlim);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetApi#getEntitySetSummary");
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
| **background** | [**List&lt;String&gt;**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] |
| **objectCategory** | **String**| E.g. phenotype, function | [optional] |
| **objectSlim** | **String**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] |

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

<a id="getOverRepresentation"></a>
# **getOverRepresentation**
> getOverRepresentation(objectCategory, subject, background, subjectCategory, maxPValue, ontology, taxon)

Summary statistics for objects associated

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentitysetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentitysetApi apiInstance = new BioentitysetApi(defaultClient);
    String objectCategory = "objectCategory_example"; // String | E.g. phenotype, function
    List<String> subject = Arrays.asList(); // List<String> | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
    List<String> background = Arrays.asList(); // List<String> | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
    String subjectCategory = "gene"; // String | Default: gene. Other types may be used e.g. disease but statistics may not make sense
    String maxPValue = "0.05"; // String | Exclude results with p-value greater than this
    String ontology = "ontology_example"; // String | ontology id. Must be obo id. Examples: go, mp, hp, uberon (optional: will be inferred if left blank)
    String taxon = "taxon_example"; // String | must be NCBITaxon CURIE. Example: NCBITaxon:9606
    try {
      apiInstance.getOverRepresentation(objectCategory, subject, background, subjectCategory, maxPValue, ontology, taxon);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentitysetApi#getOverRepresentation");
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
| **objectCategory** | **String**| E.g. phenotype, function | [optional] |
| **subject** | [**List&lt;String&gt;**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] |
| **background** | [**List&lt;String&gt;**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] |
| **subjectCategory** | **String**| Default: gene. Other types may be used e.g. disease but statistics may not make sense | [optional] [default to gene] |
| **maxPValue** | **String**| Exclude results with p-value greater than this | [optional] [default to 0.05] |
| **ontology** | **String**| ontology id. Must be obo id. Examples: go, mp, hp, uberon (optional: will be inferred if left blank) | [optional] |
| **taxon** | **String**| must be NCBITaxon CURIE. Example: NCBITaxon:9606 | [optional] |

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


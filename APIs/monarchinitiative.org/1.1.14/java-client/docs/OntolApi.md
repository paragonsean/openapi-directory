# OntolApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExtractOntologySubgraphResource**](OntolApi.md#getExtractOntologySubgraphResource) | **GET** /ontol/subgraph/{ontology}/{node} | Extract a subgraph from an ontology |
| [**getInformationContentResource**](OntolApi.md#getInformationContentResource) | **GET** /ontol/information_content/{subject_category}/{object_category}/{subject_taxon} | Returns information content (IC) for a set of relevant ontology classes |
| [**postExtractOntologySubgraphResource**](OntolApi.md#postExtractOntologySubgraphResource) | **POST** /ontol/subgraph/{ontology}/{node} | Extract a subgraph from an ontology |


<a id="getExtractOntologySubgraphResource"></a>
# **getExtractOntologySubgraphResource**
> getExtractOntologySubgraphResource(node, ontology, cnode, includeAncestors, includeDescendants, relation, includeMeta)

Extract a subgraph from an ontology

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntolApi apiInstance = new OntolApi(defaultClient);
    String node = "node_example"; // String | class ID, e.g. HP:0001288
    String ontology = "ontology_example"; // String | ontology ID, e.g. go, uberon, mp, hp
    List<String> cnode = Arrays.asList(); // List<String> | Additional classes
    Boolean includeAncestors = true; // Boolean | Include Ancestors
    Boolean includeDescendants = true; // Boolean | Include Descendants
    List<String> relation = Arrays.asList(); // List<String> | Additional classes
    Boolean includeMeta = false; // Boolean | Include metadata in response
    try {
      apiInstance.getExtractOntologySubgraphResource(node, ontology, cnode, includeAncestors, includeDescendants, relation, includeMeta);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntolApi#getExtractOntologySubgraphResource");
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
| **node** | **String**| class ID, e.g. HP:0001288 | |
| **ontology** | **String**| ontology ID, e.g. go, uberon, mp, hp | |
| **cnode** | [**List&lt;String&gt;**](String.md)| Additional classes | [optional] |
| **includeAncestors** | **Boolean**| Include Ancestors | [optional] [default to true] |
| **includeDescendants** | **Boolean**| Include Descendants | [optional] |
| **relation** | [**List&lt;String&gt;**](String.md)| Additional classes | [optional] |
| **includeMeta** | **Boolean**| Include metadata in response | [optional] [default to false] |

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

<a id="getInformationContentResource"></a>
# **getInformationContentResource**
> getInformationContentResource(subjectCategory, objectCategory, subjectTaxon, evidence)

Returns information content (IC) for a set of relevant ontology classes

&#x60;&#x60;&#x60; IC &#x3D; -log2( freq(t) / popSize ) &#x60;&#x60;&#x60;  Here the frequency and population is calculated for a particular dataset: e.g. all human disease-phenotype associations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntolApi apiInstance = new OntolApi(defaultClient);
    String subjectCategory = "subjectCategory_example"; // String | 
    String objectCategory = "objectCategory_example"; // String | 
    String subjectTaxon = "subjectTaxon_example"; // String | 
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    try {
      apiInstance.getInformationContentResource(subjectCategory, objectCategory, subjectTaxon, evidence);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntolApi#getInformationContentResource");
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
| **subjectCategory** | **String**|  | |
| **objectCategory** | **String**|  | |
| **subjectTaxon** | **String**|  | |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] |

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

<a id="postExtractOntologySubgraphResource"></a>
# **postExtractOntologySubgraphResource**
> postExtractOntologySubgraphResource(node, ontology, cnode, includeAncestors, includeDescendants, relation, includeMeta)

Extract a subgraph from an ontology

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntolApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntolApi apiInstance = new OntolApi(defaultClient);
    String node = "node_example"; // String | class ID, e.g. HP:0001288
    String ontology = "ontology_example"; // String | ontology ID, e.g. go, uberon, mp, hp
    List<String> cnode = Arrays.asList(); // List<String> | Additional classes
    Boolean includeAncestors = true; // Boolean | Include Ancestors
    Boolean includeDescendants = true; // Boolean | Include Descendants
    List<String> relation = Arrays.asList(); // List<String> | Additional classes
    Boolean includeMeta = false; // Boolean | Include metadata in response
    try {
      apiInstance.postExtractOntologySubgraphResource(node, ontology, cnode, includeAncestors, includeDescendants, relation, includeMeta);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntolApi#postExtractOntologySubgraphResource");
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
| **node** | **String**| class ID, e.g. HP:0001288 | |
| **ontology** | **String**| ontology ID, e.g. go, uberon, mp, hp | |
| **cnode** | [**List&lt;String&gt;**](String.md)| Additional classes | [optional] |
| **includeAncestors** | **Boolean**| Include Ancestors | [optional] [default to true] |
| **includeDescendants** | **Boolean**| Include Descendants | [optional] |
| **relation** | [**List&lt;String&gt;**](String.md)| Additional classes | [optional] |
| **includeMeta** | **Boolean**| Include metadata in response | [optional] [default to false] |

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


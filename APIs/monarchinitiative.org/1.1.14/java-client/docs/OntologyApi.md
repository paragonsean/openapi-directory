# OntologyApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOntologySubset**](OntologyApi.md#getOntologySubset) | **GET** /ontology/subset/{id} | Returns meta data of an ontology subset (slim) |
| [**getOntologyTerm**](OntologyApi.md#getOntologyTerm) | **GET** /ontology/term/{id} | Returns meta data of an ontology term |
| [**getOntologyTermGraph**](OntologyApi.md#getOntologyTermGraph) | **GET** /ontology/term/{id}/graph | Returns graph of an ontology term |
| [**getOntologyTermSubgraph**](OntologyApi.md#getOntologyTermSubgraph) | **GET** /ontology/term/{id}/subgraph | Extract a subgraph from an ontology term |
| [**getOntologyTermSubsets**](OntologyApi.md#getOntologyTermSubsets) | **GET** /ontology/term/{id}/subsets | Returns subsets (slims) associated to an ontology term |
| [**getOntologyTermsSharedAncestor**](OntologyApi.md#getOntologyTermsSharedAncestor) | **GET** /ontology/shared/{subject}/{object} | Returns the ancestor ontology terms shared by two ontology terms |


<a id="getOntologySubset"></a>
# **getOntologySubset**
> getOntologySubset(id)

Returns meta data of an ontology subset (slim)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String id = "id_example"; // String | name of a slim subset, e.g. goslim_agr, goslim_generic
    try {
      apiInstance.getOntologySubset(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getOntologySubset");
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
| **id** | **String**| name of a slim subset, e.g. goslim_agr, goslim_generic | |

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

<a id="getOntologyTerm"></a>
# **getOntologyTerm**
> getOntologyTerm(id)

Returns meta data of an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0003677
    try {
      apiInstance.getOntologyTerm(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getOntologyTerm");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0003677 | |

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

<a id="getOntologyTermGraph"></a>
# **getOntologyTermGraph**
> getOntologyTermGraph(id, graphType)

Returns graph of an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0000981
    String graphType = "topology_graph"; // String | graph type ('topology_graph', 'regulates_transitivity_graph' or 'neighborhood_graph')
    try {
      apiInstance.getOntologyTermGraph(id, graphType);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getOntologyTermGraph");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0000981 | |
| **graphType** | **String**| graph type (&#39;topology_graph&#39;, &#39;regulates_transitivity_graph&#39; or &#39;neighborhood_graph&#39;) | [optional] [default to topology_graph] [enum: topology_graph, regulates_transitivity_graph, neighborhood_graph, neighborhood_limited_graph] |

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

<a id="getOntologyTermSubgraph"></a>
# **getOntologyTermSubgraph**
> getOntologyTermSubgraph(id, cnode, includeAncestors, includeDescendants, relation, includeMeta)

Extract a subgraph from an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0007275
    List<String> cnode = Arrays.asList(); // List<String> | Additional classes
    Boolean includeAncestors = true; // Boolean | Include Ancestors
    Boolean includeDescendants = true; // Boolean | Include Descendants
    List<String> relation = Arrays.asList(); // List<String> | Additional classes
    Boolean includeMeta = false; // Boolean | Include metadata in response
    try {
      apiInstance.getOntologyTermSubgraph(id, cnode, includeAncestors, includeDescendants, relation, includeMeta);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getOntologyTermSubgraph");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0007275 | |
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

<a id="getOntologyTermSubsets"></a>
# **getOntologyTermSubsets**
> getOntologyTermSubsets(id)

Returns subsets (slims) associated to an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0006259
    try {
      apiInstance.getOntologyTermSubsets(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getOntologyTermSubsets");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0006259 | |

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

<a id="getOntologyTermsSharedAncestor"></a>
# **getOntologyTermsSharedAncestor**
> getOntologyTermsSharedAncestor(subject, _object)

Returns the ancestor ontology terms shared by two ontology terms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntologyApi apiInstance = new OntologyApi(defaultClient);
    String subject = "subject_example"; // String | CURIE identifier of a GO term, e.g. GO:0006259
    String _object = "_object_example"; // String | CURIE identifier of a GO term, e.g. GO:0046483
    try {
      apiInstance.getOntologyTermsSharedAncestor(subject, _object);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntologyApi#getOntologyTermsSharedAncestor");
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
| **subject** | **String**| CURIE identifier of a GO term, e.g. GO:0006259 | |
| **_object** | **String**| CURIE identifier of a GO term, e.g. GO:0046483 | |

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


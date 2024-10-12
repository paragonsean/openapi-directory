# GraphApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEdgeResource**](GraphApi.md#getEdgeResource) | **GET** /graph/edges/from/{id} | Returns edges emanating from a given node |
| [**getNodeResource**](GraphApi.md#getNodeResource) | **GET** /graph/node/{id} | Returns a graph node |


<a id="getEdgeResource"></a>
# **getEdgeResource**
> List&lt;Graph&gt; getEdgeResource(id, depth, direction, relationshipType, entail, graph)

Returns edges emanating from a given node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GraphApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    GraphApi apiInstance = new GraphApi(defaultClient);
    String id = "id_example"; // String | CURIE e.g. HP:0000465
    Integer depth = 1; // Integer | How far to traverse for neighbors
    String direction = "INCOMING"; // String | Which direction to traverse (used only if relationship_type is defined)
    List<String> relationshipType = Arrays.asList(); // List<String> | Relationship type to traverse
    Boolean entail = false; // Boolean | Include sub-properties and equivalent properties
    String graph = "data"; // String | Which monarch graph to query
    try {
      List<Graph> result = apiInstance.getEdgeResource(id, depth, direction, relationshipType, entail, graph);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GraphApi#getEdgeResource");
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
| **id** | **String**| CURIE e.g. HP:0000465 | |
| **depth** | **Integer**| How far to traverse for neighbors | [optional] [default to 1] |
| **direction** | **String**| Which direction to traverse (used only if relationship_type is defined) | [optional] [default to BOTH] [enum: INCOMING, OUTGOING, BOTH] |
| **relationshipType** | [**List&lt;String&gt;**](String.md)| Relationship type to traverse | [optional] |
| **entail** | **Boolean**| Include sub-properties and equivalent properties | [optional] [default to false] |
| **graph** | **String**| Which monarch graph to query | [optional] [default to data] [enum: data, ontology] |

### Return type

[**List&lt;Graph&gt;**](Graph.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getNodeResource"></a>
# **getNodeResource**
> List&lt;BioObject&gt; getNodeResource(id)

Returns a graph node

A node is an abstract representation of some kind of entity. The entity may be a physical thing such as a patient, a molecular entity such as a gene or protein, or a conceptual entity such as a class from an ontology.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GraphApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    GraphApi apiInstance = new GraphApi(defaultClient);
    String id = "id_example"; // String | CURIE e.g. HP:0000465
    try {
      List<BioObject> result = apiInstance.getNodeResource(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GraphApi#getNodeResource");
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
| **id** | **String**| CURIE e.g. HP:0000465 | |

### Return type

[**List&lt;BioObject&gt;**](BioObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


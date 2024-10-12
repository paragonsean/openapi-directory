# EvidenceGraphApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEvidenceGraphObject**](EvidenceGraphApi.md#getEvidenceGraphObject) | **GET** /evidence/graph/{id} | Returns evidence graph object for a given association |
| [**getEvidenceGraphTable**](EvidenceGraphApi.md#getEvidenceGraphTable) | **GET** /evidence/graph/{id}/table | Returns evidence as a association_results object given an association |


<a id="getEvidenceGraphObject"></a>
# **getEvidenceGraphObject**
> List&lt;Graph&gt; getEvidenceGraphObject(id)

Returns evidence graph object for a given association

Note that every association is assumed to have a unique ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EvidenceGraphApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    EvidenceGraphApi apiInstance = new EvidenceGraphApi(defaultClient);
    String id = "id_example"; // String | association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada
    try {
      List<Graph> result = apiInstance.getEvidenceGraphObject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EvidenceGraphApi#getEvidenceGraphObject");
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
| **id** | **String**| association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada | |

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

<a id="getEvidenceGraphTable"></a>
# **getEvidenceGraphTable**
> List&lt;AssociationResults&gt; getEvidenceGraphTable(id, isPublication)

Returns evidence as a association_results object given an association

Note that every association is assumed to have a unique ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EvidenceGraphApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    EvidenceGraphApi apiInstance = new EvidenceGraphApi(defaultClient);
    String id = "id_example"; // String | association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada
    Boolean isPublication = false; // Boolean | If true, considers dc:source as edge
    try {
      List<AssociationResults> result = apiInstance.getEvidenceGraphTable(id, isPublication);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EvidenceGraphApi#getEvidenceGraphTable");
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
| **id** | **String**| association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada | |
| **isPublication** | **Boolean**| If true, considers dc:source as edge | [optional] [default to false] |

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


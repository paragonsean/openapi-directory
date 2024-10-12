# OwlOntologyApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDlQuery**](OwlOntologyApi.md#getDlQuery) | **GET** /owl/ontology/dlquery/{query} | Placeholder - use OWLery for now |
| [**getSparqlQuery**](OwlOntologyApi.md#getSparqlQuery) | **GET** /owl/ontology/sparql/{query} | Placeholder - use direct SPARQL endpoint for now |


<a id="getDlQuery"></a>
# **getDlQuery**
> List&lt;Association&gt; getDlQuery(query)

Placeholder - use OWLery for now

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwlOntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OwlOntologyApi apiInstance = new OwlOntologyApi(defaultClient);
    String query = "query_example"; // String | 
    try {
      List<Association> result = apiInstance.getDlQuery(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwlOntologyApi#getDlQuery");
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
| **query** | **String**|  | |

### Return type

[**List&lt;Association&gt;**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSparqlQuery"></a>
# **getSparqlQuery**
> List&lt;Association&gt; getSparqlQuery(query)

Placeholder - use direct SPARQL endpoint for now

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwlOntologyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OwlOntologyApi apiInstance = new OwlOntologyApi(defaultClient);
    String query = "query_example"; // String | 
    try {
      List<Association> result = apiInstance.getSparqlQuery(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwlOntologyApi#getSparqlQuery");
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
| **query** | **String**|  | |

### Return type

[**List&lt;Association&gt;**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


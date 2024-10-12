# SparqlApi

All URIs are relative to *http://api.aucklandmuseum.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSparql**](SparqlApi.md#getSparql) | **GET** /sparql | Auckland Museum SPARQL endpoint |
| [**postSparql**](SparqlApi.md#postSparql) | **POST** /sparql | Auckland Museum SPARQL endpoint |


<a id="getSparql"></a>
# **getSparql**
> Object getSparql(query, paramCallback, infer)

Auckland Museum SPARQL endpoint

You can execute your [SPARQL](http://www.w3.org/TR/rdf-sparql-query/) queries against this endpoint.  The sparql query should be provided as the value of the request parameter &#x60;query&#x60;. Set the &#x60;Accept&#x60; header to &#x60;application/sparql-results+xml&#x60; to get results in XML. Set it to &#x60;application/sparql-results+json&#x60; to get results in JSON.   **Note:** This endpoints supports [JSON-P](http://json-p.org/). In order to get a JSON-P response, set the query parameter &#x60;callback&#x60; to your preferred callback function name. The default function name is &#x60;callback()&#x60;. When using JSON-P, there is no need to set the &#x60;Accept&#x60; header because the response will always be in &#x60;application/javascript&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SparqlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.aucklandmuseum.com");

    SparqlApi apiInstance = new SparqlApi(defaultClient);
    String query = "query_example"; // String | sparql query
    String paramCallback = "callback"; // String | The [JSON-P](http://json-p.org/) callback parameter
    Boolean infer = true; // Boolean | Whether to get inferred results in the response
    try {
      Object result = apiInstance.getSparql(query, paramCallback, infer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SparqlApi#getSparql");
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
| **query** | **String**| sparql query | |
| **paramCallback** | **String**| The [JSON-P](http://json-p.org/) callback parameter | [optional] [default to callback] |
| **infer** | **Boolean**| Whether to get inferred results in the response | [optional] [default to true] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/sparql-results+json, application/sparql-results+xml, application/javascript

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="postSparql"></a>
# **postSparql**
> postSparql(query, infer)

Auckland Museum SPARQL endpoint

You can execute your [SPARQL](http://www.w3.org/TR/rdf-sparql-query/) queries against this endpoint. The sparql query should be provided as the value of the request parameter &#x60;query&#x60;. Set the &#x60;Accept&#x60; header to &#x60;application/sparql-results+xml&#x60; to get results in XML. Set it to &#x60;application/sparql-results+json&#x60; to get results in JSON.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SparqlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.aucklandmuseum.com");

    SparqlApi apiInstance = new SparqlApi(defaultClient);
    String query = "query_example"; // String | sparql query
    Boolean infer = true; // Boolean | Whether to get inferred results in the response
    try {
      apiInstance.postSparql(query, infer);
    } catch (ApiException e) {
      System.err.println("Exception when calling SparqlApi#postSparql");
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
| **query** | **String**| sparql query | |
| **infer** | **Boolean**| Whether to get inferred results in the response | [optional] [default to true] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |


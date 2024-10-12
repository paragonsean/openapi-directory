# ConceptsApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConcept**](ConceptsApi.md#getConcept) | **GET** /concepts/{id} |  |
| [**getConcepts**](ConceptsApi.md#getConcepts) | **GET** /concepts |  |


<a id="getConcept"></a>
# **getConcept**
> ConceptItemModelPublic getConcept(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConceptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    ConceptsApi apiInstance = new ConceptsApi(defaultClient);
    String id = "id_example"; // String | concept id
    try {
      ConceptItemModelPublic result = apiInstance.getConcept(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConceptsApi#getConcept");
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
| **id** | **String**| concept id | |

### Return type

[**ConceptItemModelPublic**](ConceptItemModelPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getConcepts"></a>
# **getConcepts**
> Set&lt;ConceptItemModelPublic&gt; getConcepts(ids, types)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConceptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    ConceptsApi apiInstance = new ConceptsApi(defaultClient);
    String ids = "ids_example"; // String | ids
    String types = "types_example"; // String | types
    try {
      Set<ConceptItemModelPublic> result = apiInstance.getConcepts(ids, types);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConceptsApi#getConcepts");
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
| **ids** | **String**| ids | [optional] |
| **types** | **String**| types | [optional] |

### Return type

[**Set&lt;ConceptItemModelPublic&gt;**](ConceptItemModelPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |


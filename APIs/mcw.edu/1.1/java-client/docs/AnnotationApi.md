# AnnotationApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAnnotationCountByAccIdAndObjectTypeUsingGET**](AnnotationApi.md#getAnnotationCountByAccIdAndObjectTypeUsingGET) | **GET** /annotations/count/{accId}/{speciesTypeKey}/{includeChildren}/{objectType} | Returns annotation count for ontology accession ID and object type |
| [**getAnnotationCountByAccIdAndSpeciesUsingGET**](AnnotationApi.md#getAnnotationCountByAccIdAndSpeciesUsingGET) | **GET** /annotations/count/{accId}/{speciesTypeKey}/{includeChildren} | Returns annotation count for ontology accession ID and speicies |
| [**getAnnotationCountByAccIdUsingGET**](AnnotationApi.md#getAnnotationCountByAccIdUsingGET) | **GET** /annotations/count/{accId}/{includeChildren} | Returns annotation count for ontology accession ID |
| [**getAnnotationsByAccIdAndRgdIdUsingGET**](AnnotationApi.md#getAnnotationsByAccIdAndRgdIdUsingGET) | **GET** /annotations/{accId}/{rgdId} | Returns a list of annotations by RGD ID and ontology term accession ID |
| [**getAnnotationsByRgdIdAndOntologyUsingGET**](AnnotationApi.md#getAnnotationsByRgdIdAndOntologyUsingGET) | **GET** /annotations/rgdId/{rgdId}/{ontologyPrefix} | Returns a list of annotations by RGD ID and ontology prefix |
| [**getAnnotationsByRgdIdUsingGET**](AnnotationApi.md#getAnnotationsByRgdIdUsingGET) | **GET** /annotations/rgdId/{rgdId} | Returns a list of annotations by RGD ID |
| [**getAnnotationsUsingGET**](AnnotationApi.md#getAnnotationsUsingGET) | **GET** /annotations/{accId}/{speciesTypeKey}/{includeChildren} | Returns a list annotations for an ontology term or a term and it&#39;s children |
| [**getAnnotationsUsingPOST**](AnnotationApi.md#getAnnotationsUsingPOST) | **POST** /annotations/ | Return a list of genes annotated to an ontology term |
| [**getAnnotsByRefrerenceUsingGET**](AnnotationApi.md#getAnnotsByRefrerenceUsingGET) | **GET** /annotations/reference/{refRgdId} | Returns a list of annotations for a reference |
| [**getTermAccIdsUsingGET**](AnnotationApi.md#getTermAccIdsUsingGET) | **GET** /annotations/accId/{rgdId} | Returns a list ontology term accession IDs annotated to an rgd object |


<a id="getAnnotationCountByAccIdAndObjectTypeUsingGET"></a>
# **getAnnotationCountByAccIdAndObjectTypeUsingGET**
> Integer getAnnotationCountByAccIdAndObjectTypeUsingGET(accId, speciesTypeKey, includeChildren, objectType)

Returns annotation count for ontology accession ID and object type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    String accId = "accId_example"; // String | Ontology term accession ID
    Integer speciesTypeKey = 56; // Integer | A list of species type keys can be found using the lookup service
    Boolean includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
    Integer objectType = 56; // Integer | A list of object types can be found using the lookup service
    try {
      Integer result = apiInstance.getAnnotationCountByAccIdAndObjectTypeUsingGET(accId, speciesTypeKey, includeChildren, objectType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationCountByAccIdAndObjectTypeUsingGET");
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
| **accId** | **String**| Ontology term accession ID | |
| **speciesTypeKey** | **Integer**| A list of species type keys can be found using the lookup service | |
| **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | |
| **objectType** | **Integer**| A list of object types can be found using the lookup service | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAnnotationCountByAccIdAndSpeciesUsingGET"></a>
# **getAnnotationCountByAccIdAndSpeciesUsingGET**
> Integer getAnnotationCountByAccIdAndSpeciesUsingGET(accId, speciesTypeKey, includeChildren)

Returns annotation count for ontology accession ID and speicies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    String accId = "accId_example"; // String | Ontology term accession ID
    Integer speciesTypeKey = 56; // Integer | A list of species type keys can be found using the lookup service
    Boolean includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
    try {
      Integer result = apiInstance.getAnnotationCountByAccIdAndSpeciesUsingGET(accId, speciesTypeKey, includeChildren);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationCountByAccIdAndSpeciesUsingGET");
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
| **accId** | **String**| Ontology term accession ID | |
| **speciesTypeKey** | **Integer**| A list of species type keys can be found using the lookup service | |
| **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAnnotationCountByAccIdUsingGET"></a>
# **getAnnotationCountByAccIdUsingGET**
> Integer getAnnotationCountByAccIdUsingGET(accId, includeChildren)

Returns annotation count for ontology accession ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    String accId = "accId_example"; // String | Ontology term accession ID
    Boolean includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
    try {
      Integer result = apiInstance.getAnnotationCountByAccIdUsingGET(accId, includeChildren);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationCountByAccIdUsingGET");
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
| **accId** | **String**| Ontology term accession ID | |
| **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAnnotationsByAccIdAndRgdIdUsingGET"></a>
# **getAnnotationsByAccIdAndRgdIdUsingGET**
> List&lt;Annotation&gt; getAnnotationsByAccIdAndRgdIdUsingGET(accId, rgdId)

Returns a list of annotations by RGD ID and ontology term accession ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    String accId = "accId_example"; // String | Ontology Term Accession ID
    Integer rgdId = 56; // Integer | RGD ID
    try {
      List<Annotation> result = apiInstance.getAnnotationsByAccIdAndRgdIdUsingGET(accId, rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationsByAccIdAndRgdIdUsingGET");
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
| **accId** | **String**| Ontology Term Accession ID | |
| **rgdId** | **Integer**| RGD ID | |

### Return type

[**List&lt;Annotation&gt;**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAnnotationsByRgdIdAndOntologyUsingGET"></a>
# **getAnnotationsByRgdIdAndOntologyUsingGET**
> List&lt;Annotation&gt; getAnnotationsByRgdIdAndOntologyUsingGET(rgdId, ontologyPrefix)

Returns a list of annotations by RGD ID and ontology prefix

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    String ontologyPrefix = "ontologyPrefix_example"; // String | Ontology Prefix.  The prefix can be found left of the semicolon in an ontology term accession ID.  As an example, term accession PW:0000034 has the ontology prefix PW
    try {
      List<Annotation> result = apiInstance.getAnnotationsByRgdIdAndOntologyUsingGET(rgdId, ontologyPrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationsByRgdIdAndOntologyUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |
| **ontologyPrefix** | **String**| Ontology Prefix.  The prefix can be found left of the semicolon in an ontology term accession ID.  As an example, term accession PW:0000034 has the ontology prefix PW | |

### Return type

[**List&lt;Annotation&gt;**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAnnotationsByRgdIdUsingGET"></a>
# **getAnnotationsByRgdIdUsingGET**
> List&lt;Annotation&gt; getAnnotationsByRgdIdUsingGET(rgdId)

Returns a list of annotations by RGD ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      List<Annotation> result = apiInstance.getAnnotationsByRgdIdUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationsByRgdIdUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

### Return type

[**List&lt;Annotation&gt;**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAnnotationsUsingGET"></a>
# **getAnnotationsUsingGET**
> List&lt;Annotation&gt; getAnnotationsUsingGET(accId, speciesTypeKey, includeChildren)

Returns a list annotations for an ontology term or a term and it&#39;s children

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    String accId = "accId_example"; // String | Ontology term accession ID
    Integer speciesTypeKey = 56; // Integer | A list of species type keys can be found using the lookup service
    Boolean includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
    try {
      List<Annotation> result = apiInstance.getAnnotationsUsingGET(accId, speciesTypeKey, includeChildren);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationsUsingGET");
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
| **accId** | **String**| Ontology term accession ID | |
| **speciesTypeKey** | **Integer**| A list of species type keys can be found using the lookup service | |
| **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | |

### Return type

[**List&lt;Annotation&gt;**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAnnotationsUsingPOST"></a>
# **getAnnotationsUsingPOST**
> List&lt;Annotation&gt; getAnnotationsUsingPOST(annotationRequest)

Return a list of genes annotated to an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    AnnotationRequest annotationRequest = new AnnotationRequest(); // AnnotationRequest | data
    try {
      List<Annotation> result = apiInstance.getAnnotationsUsingPOST(annotationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotationsUsingPOST");
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
| **annotationRequest** | [**AnnotationRequest**](AnnotationRequest.md)| data | [optional] |

### Return type

[**List&lt;Annotation&gt;**](Annotation.md)

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

<a id="getAnnotsByRefrerenceUsingGET"></a>
# **getAnnotsByRefrerenceUsingGET**
> List&lt;Annotation&gt; getAnnotsByRefrerenceUsingGET(refRgdId)

Returns a list of annotations for a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    Integer refRgdId = 56; // Integer | Reference RGD ID
    try {
      List<Annotation> result = apiInstance.getAnnotsByRefrerenceUsingGET(refRgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getAnnotsByRefrerenceUsingGET");
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
| **refRgdId** | **Integer**| Reference RGD ID | |

### Return type

[**List&lt;Annotation&gt;**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getTermAccIdsUsingGET"></a>
# **getTermAccIdsUsingGET**
> List&lt;MapPair&gt; getTermAccIdsUsingGET(rgdId)

Returns a list ontology term accession IDs annotated to an rgd object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnnotationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AnnotationApi apiInstance = new AnnotationApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      List<MapPair> result = apiInstance.getTermAccIdsUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnnotationApi#getTermAccIdsUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

### Return type

[**List&lt;MapPair&gt;**](MapPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |


# PrivateApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getApiDocs**](PrivateApi.md#getApiDocs) | **GET** /platform/docs | Browse API documentation |
| [**getApiSwaggerUI**](PrivateApi.md#getApiSwaggerUI) | **GET** /platform/docs/swagger-ui | Browse interactive API documentation |
| [**getAutocomplete**](PrivateApi.md#getAutocomplete) | **GET** /platform/private/autocomplete | Get &#x60;autocomplete&#x60; objects. |
| [**getDiseaseById**](PrivateApi.md#getDiseaseById) | **GET** /platform/private/disease/{disease} | Find information about a disease |
| [**getDrugByID**](PrivateApi.md#getDrugByID) | **GET** /platform/private/drug/{DRUG_ID} | Get drug by ID |
| [**getECObyID**](PrivateApi.md#getECObyID) | **GET** /platform/private/eco/{ECO_ID} | Get evidence code by ID |
| [**getQuickSearch**](PrivateApi.md#getQuickSearch) | **GET** /platform/private/quicksearch | Search most relevant results |
| [**getRelationByEFOID**](PrivateApi.md#getRelationByEFOID) | **GET** /platform/private/relation/disease/{disease} | Find related entities by disease |
| [**getRelationByENSGID**](PrivateApi.md#getRelationByENSGID) | **GET** /platform/private/relation/target/{target} | Find related entities by target |
| [**getSwagger**](PrivateApi.md#getSwagger) | **GET** /platform/swagger | Get OpenAPI schema |
| [**getTargetByENSGID**](PrivateApi.md#getTargetByENSGID) | **GET** /platform/private/target/{target} | Find information about a target |
| [**getTargetExpressionByENSGID**](PrivateApi.md#getTargetExpressionByENSGID) | **GET** /platform/private/target/expression | Query expression levels |
| [**postBestHitSearch**](PrivateApi.md#postBestHitSearch) | **POST** /platform/private/besthitsearch | Find the best hit |
| [**postDiseaseById**](PrivateApi.md#postDiseaseById) | **POST** /platform/private/disease | Find information about a list of diseases |
| [**postEnrichmentTarget**](PrivateApi.md#postEnrichmentTarget) | **POST** /platform/private/enrichment/targets | Enrichment analysis |
| [**postRelation**](PrivateApi.md#postRelation) | **POST** /platform/private/relation | Find related entities |
| [**postTargetByENSGID**](PrivateApi.md#postTargetByENSGID) | **POST** /platform/private/target | Find information about a list of targets |
| [**postTargetExpressionByENSGID**](PrivateApi.md#postTargetExpressionByENSGID) | **POST** /platform/private/target/expression | Batch query expression levels |


<a id="getApiDocs"></a>
# **getApiDocs**
> getApiDocs()

Browse API documentation

Access api docs as served by Redoc

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    try {
      apiInstance.getApiDocs();
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getApiDocs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Redoc API documentation file |  -  |

<a id="getApiSwaggerUI"></a>
# **getApiSwaggerUI**
> getApiSwaggerUI()

Browse interactive API documentation

Interactive API docs using swagger-ui

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    try {
      apiInstance.getApiSwaggerUI();
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getApiSwaggerUI");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Swagger-UI API documentation file |  -  |

<a id="getAutocomplete"></a>
# **getAutocomplete**
> getAutocomplete(q, size)

Get &#x60;autocomplete&#x60; objects.

Search for the closest term to autocomplete in the search box. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String q = "q_example"; // String | A full text query.
    String size = "size_example"; // String | Maximum amount of results to return. Defaults to 5.
    try {
      apiInstance.getAutocomplete(q, size);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getAutocomplete");
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
| **q** | **String**| A full text query. | |
| **size** | **String**| Maximum amount of results to return. Defaults to 5. | [optional] |

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
| **200** | Successful response |  -  |

<a id="getDiseaseById"></a>
# **getDiseaseById**
> getDiseaseById(disease)

Find information about a disease

Get &#x60;disease&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String disease = "disease_example"; // String | An EFO identifier.
    try {
      apiInstance.getDiseaseById(disease);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getDiseaseById");
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
| **disease** | **String**| An EFO identifier. | |

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
| **200** | Successful response |  -  |

<a id="getDrugByID"></a>
# **getDrugByID**
> getDrugByID(drugId, DRUG_ID)

Get drug by ID

Get &#x60;drug&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String drugId = "drugId_example"; // String | An ID in the drug index.
    String DRUG_ID = "DRUG_ID_example"; // String | Automatically added
    try {
      apiInstance.getDrugByID(drugId, DRUG_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getDrugByID");
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
| **drugId** | **String**| An ID in the drug index. | |
| **DRUG_ID** | **String**| Automatically added | |

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
| **200** | Successful response |  -  |

<a id="getECObyID"></a>
# **getECObyID**
> getECObyID(ECO_ID)

Get evidence code by ID

Get &#x60;ECO&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String ECO_ID = "ECO_ID_example"; // String | An [evidence code ontology](http://www.ebi.ac.uk/ols/v2/browse.do?ontName=ECO) ID.
    try {
      apiInstance.getECObyID(ECO_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getECObyID");
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
| **ECO_ID** | **String**| An [evidence code ontology](http://www.ebi.ac.uk/ols/v2/browse.do?ontName&#x3D;ECO) ID. | |

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
| **200** | Successful response |  -  |

<a id="getQuickSearch"></a>
# **getQuickSearch**
> getQuickSearch(q, size)

Search most relevant results

Get &#x60;search-result&#x60; objects. Enables search bar functionality. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String q = "q_example"; // String | A full text query.
    String size = "size_example"; // String | Maximum amount of results to return. Defaults to 5.
    try {
      apiInstance.getQuickSearch(q, size);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getQuickSearch");
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
| **q** | **String**| A full text query. | |
| **size** | **String**| Maximum amount of results to return. Defaults to 5. | [optional] |

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
| **200** | Successful response |  -  |

<a id="getRelationByEFOID"></a>
# **getRelationByEFOID**
> getRelationByEFOID(disease)

Find related entities by disease

Get &#x60;relation&#x60; objects starting from diseases. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String disease = "disease_example"; // String | An EFO gene identifier.
    try {
      apiInstance.getRelationByEFOID(disease);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getRelationByEFOID");
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
| **disease** | **String**| An EFO gene identifier. | |

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
| **200** | Successful response |  -  |

<a id="getRelationByENSGID"></a>
# **getRelationByENSGID**
> getRelationByENSGID(target)

Find related entities by target

Get &#x60;relation&#x60; objects starting from diseases. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String target = "target_example"; // String | An Ensembl gene identifier.
    try {
      apiInstance.getRelationByENSGID(target);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getRelationByENSGID");
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
| **target** | **String**| An Ensembl gene identifier. | |

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
| **200** | Successful response |  -  |

<a id="getSwagger"></a>
# **getSwagger**
> getSwagger()

Get OpenAPI schema

Get swagger.yaml specs for the API

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    try {
      apiInstance.getSwagger();
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getSwagger");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Swagger.yaml file |  -  |

<a id="getTargetByENSGID"></a>
# **getTargetByENSGID**
> getTargetByENSGID(target)

Find information about a target

Get &#x60;target&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String target = "target_example"; // String | An Ensembl gene ID for the target of interest.
    try {
      apiInstance.getTargetByENSGID(target);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getTargetByENSGID");
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
| **target** | **String**| An Ensembl gene ID for the target of interest. | |

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
| **200** | Successful response |  -  |

<a id="getTargetExpressionByENSGID"></a>
# **getTargetExpressionByENSGID**
> getTargetExpressionByENSGID(gene)

Query expression levels

Get &#x60;gene-expression&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String gene = "gene_example"; // String | An Ensembl gene identifier.
    try {
      apiInstance.getTargetExpressionByENSGID(gene);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#getTargetExpressionByENSGID");
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
| **gene** | **String**| An Ensembl gene identifier. | |

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
| **200** | Successful response |  -  |

<a id="postBestHitSearch"></a>
# **postBestHitSearch**
> postBestHitSearch(body)

Find the best hit

Fire the search method for multiple strings 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String body = "body_example"; // String | list of strings to search for
    try {
      apiInstance.postBestHitSearch(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#postBestHitSearch");
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
| **body** | **String**| list of strings to search for | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="postDiseaseById"></a>
# **postDiseaseById**
> postDiseaseById(body)

Find information about a list of diseases

Get &#x60;disease&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String body = "body_example"; // String | An EFO identifier.
    try {
      apiInstance.postDiseaseById(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#postDiseaseById");
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
| **body** | **String**| An EFO identifier. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="postEnrichmentTarget"></a>
# **postEnrichmentTarget**
> postEnrichmentTarget(body)

Enrichment analysis

Returns an enrichment analysis for a list of targets passed in the body 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String body = "body_example"; // String | IDs of the targets to do the enrichment analysis for.
    try {
      apiInstance.postEnrichmentTarget(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#postEnrichmentTarget");
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
| **body** | **String**| IDs of the targets to do the enrichment analysis for. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="postRelation"></a>
# **postRelation**
> postRelation(body)

Find related entities

Get &#x60;relation&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String body = "body_example"; // String | An Ensembl gene identifier.
    try {
      apiInstance.postRelation(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#postRelation");
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
| **body** | **String**| An Ensembl gene identifier. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="postTargetByENSGID"></a>
# **postTargetByENSGID**
> postTargetByENSGID(body)

Find information about a list of targets

Get &#x60;target&#x60; objects. Used for the target profile page. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String body = "body_example"; // String | An Ensembl gene identifier.
    try {
      apiInstance.postTargetByENSGID(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#postTargetByENSGID");
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
| **body** | **String**| An Ensembl gene identifier. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="postTargetExpressionByENSGID"></a>
# **postTargetExpressionByENSGID**
> postTargetExpressionByENSGID(body)

Batch query expression levels

Get &#x60;gene-expression&#x60; objects. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    PrivateApi apiInstance = new PrivateApi(defaultClient);
    String body = "body_example"; // String | An Ensembl gene identifier.
    try {
      apiInstance.postTargetExpressionByENSGID(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateApi#postTargetExpressionByENSGID");
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
| **body** | **String**| An Ensembl gene identifier. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |


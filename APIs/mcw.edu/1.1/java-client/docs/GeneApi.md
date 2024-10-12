# GeneApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllAnnotatedGenesUsingGET**](GeneApi.md#getAllAnnotatedGenesUsingGET) | **GET** /genes/annotation/{accId} | Return a list of genes annotated to an ontology term |
| [**getAnnotatedGenesUsingPOST**](GeneApi.md#getAnnotatedGenesUsingPOST) | **POST** /genes/annotation | Return a list of genes annotated to an ontology term |
| [**getGeneAllelesUsingGET**](GeneApi.md#getGeneAllelesUsingGET) | **GET** /genes/allele/{rgdId} | Return a list of gene alleles |
| [**getGeneByMapKeyUsingGET**](GeneApi.md#getGeneByMapKeyUsingGET) | **GET** /genes/map/{mapKey} | Return a list of all genes with position information for an assembly |
| [**getGeneByRgdIdUsingGET**](GeneApi.md#getGeneByRgdIdUsingGET) | **GET** /genes/{rgdId} | Get a gene record by RGD ID |
| [**getGeneBySymbolUsingGET**](GeneApi.md#getGeneBySymbolUsingGET) | **GET** /genes/{symbol}/{speciesTypeKey} | Get a gene record by symbol and species type key |
| [**getGeneOrthologsUsingGET**](GeneApi.md#getGeneOrthologsUsingGET) | **GET** /genes/orthologs/{rgdId} | Return a list of gene orthologs |
| [**getGenesAnnotatedUsingGET**](GeneApi.md#getGenesAnnotatedUsingGET) | **GET** /genes/annotation/{accId}/{speciesTypeKey} | Return a list of genes annotated to an ontology term |
| [**getGenesByAffyIdUsingGET**](GeneApi.md#getGenesByAffyIdUsingGET) | **GET** /genes/affyId/{affyId}/{speciesTypeKey} | Return a list of genes for an affymetrix ID |
| [**getGenesByAliasSymbolUsingGET**](GeneApi.md#getGenesByAliasSymbolUsingGET) | **GET** /genes/alias/{aliasSymbol}/{speciesTypeKey} | Return a list of genes for an alias and species |
| [**getGenesByKeywordUsingGET**](GeneApi.md#getGenesByKeywordUsingGET) | **GET** /genes/keyword/{keyword}/{speciesTypeKey} | Return a list of genes by keyword and species type key |
| [**getGenesByPositionUsingGET**](GeneApi.md#getGenesByPositionUsingGET) | **GET** /genes/{chr}/{start}/{stop}/{mapKey} | Return a list of genes position and map key |
| [**getGenesBySpeciesUsingGET**](GeneApi.md#getGenesBySpeciesUsingGET) | **GET** /genes/species/{speciesTypeKey} | Return a list of all genes for a species in RGD |
| [**getGenesInRegionUsingGET**](GeneApi.md#getGenesInRegionUsingGET) | **GET** /genes/region/{chr}/{start}/{stop}/{mapKey} | Return a list of genes in region |
| [**getMappedGenesByPositionUsingGET**](GeneApi.md#getMappedGenesByPositionUsingGET) | **GET** /genes/mapped/{chr}/{start}/{stop}/{mapKey} | Return a list of genes position and map key |
| [**getOrthologsByListUsingPOST**](GeneApi.md#getOrthologsByListUsingPOST) | **POST** /genes/orthologs | Return a list of gene orthologs |


<a id="getAllAnnotatedGenesUsingGET"></a>
# **getAllAnnotatedGenesUsingGET**
> List&lt;Gene&gt; getAllAnnotatedGenesUsingGET(accId)

Return a list of genes annotated to an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String accId = "accId_example"; // String | Accesstion ID
    try {
      List<Gene> result = apiInstance.getAllAnnotatedGenesUsingGET(accId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getAllAnnotatedGenesUsingGET");
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
| **accId** | **String**| Accesstion ID | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getAnnotatedGenesUsingPOST"></a>
# **getAnnotatedGenesUsingPOST**
> List&lt;Gene&gt; getAnnotatedGenesUsingPOST(annotatedGeneRequest)

Return a list of genes annotated to an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    AnnotatedGeneRequest annotatedGeneRequest = new AnnotatedGeneRequest(); // AnnotatedGeneRequest | data
    try {
      List<Gene> result = apiInstance.getAnnotatedGenesUsingPOST(annotatedGeneRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getAnnotatedGenesUsingPOST");
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
| **annotatedGeneRequest** | [**AnnotatedGeneRequest**](AnnotatedGeneRequest.md)| data | [optional] |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGeneAllelesUsingGET"></a>
# **getGeneAllelesUsingGET**
> List&lt;Gene&gt; getGeneAllelesUsingGET(rgdId)

Return a list of gene alleles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID of gene
    try {
      List<Gene> result = apiInstance.getGeneAllelesUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGeneAllelesUsingGET");
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
| **rgdId** | **Integer**| RGD ID of gene | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGeneByMapKeyUsingGET"></a>
# **getGeneByMapKeyUsingGET**
> List&lt;MappedGene&gt; getGeneByMapKeyUsingGET(mapKey)

Return a list of all genes with position information for an assembly

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    Integer mapKey = 56; // Integer | A list of RGD assembly map keys can be found in the lookup service
    try {
      List<MappedGene> result = apiInstance.getGeneByMapKeyUsingGET(mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGeneByMapKeyUsingGET");
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
| **mapKey** | **Integer**| A list of RGD assembly map keys can be found in the lookup service | |

### Return type

[**List&lt;MappedGene&gt;**](MappedGene.md)

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

<a id="getGeneByRgdIdUsingGET"></a>
# **getGeneByRgdIdUsingGET**
> Gene getGeneByRgdIdUsingGET(rgdId)

Get a gene record by RGD ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    Integer rgdId = 56; // Integer | The RGD ID of a Gene in RGD
    try {
      Gene result = apiInstance.getGeneByRgdIdUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGeneByRgdIdUsingGET");
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
| **rgdId** | **Integer**| The RGD ID of a Gene in RGD | |

### Return type

[**Gene**](Gene.md)

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

<a id="getGeneBySymbolUsingGET"></a>
# **getGeneBySymbolUsingGET**
> Gene getGeneBySymbolUsingGET(symbol, speciesTypeKey)

Get a gene record by symbol and species type key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String symbol = "symbol_example"; // String | Gene Symbol
    Integer speciesTypeKey = 56; // Integer | Species type key.  A list of species type keys can be found in the lookup service
    try {
      Gene result = apiInstance.getGeneBySymbolUsingGET(symbol, speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGeneBySymbolUsingGET");
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
| **symbol** | **String**| Gene Symbol | |
| **speciesTypeKey** | **Integer**| Species type key.  A list of species type keys can be found in the lookup service | |

### Return type

[**Gene**](Gene.md)

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

<a id="getGeneOrthologsUsingGET"></a>
# **getGeneOrthologsUsingGET**
> List&lt;Gene&gt; getGeneOrthologsUsingGET(rgdId)

Return a list of gene orthologs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID of a gene
    try {
      List<Gene> result = apiInstance.getGeneOrthologsUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGeneOrthologsUsingGET");
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
| **rgdId** | **Integer**| RGD ID of a gene | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGenesAnnotatedUsingGET"></a>
# **getGenesAnnotatedUsingGET**
> List&lt;Gene&gt; getGenesAnnotatedUsingGET(accId, speciesTypeKey)

Return a list of genes annotated to an ontology term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String accId = "accId_example"; // String | Ontology term accession ID
    Integer speciesTypeKey = 56; // Integer | Species type key.  A list of species type keys can be found in the lookup service
    try {
      List<Gene> result = apiInstance.getGenesAnnotatedUsingGET(accId, speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGenesAnnotatedUsingGET");
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
| **speciesTypeKey** | **Integer**| Species type key.  A list of species type keys can be found in the lookup service | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGenesByAffyIdUsingGET"></a>
# **getGenesByAffyIdUsingGET**
> List&lt;Gene&gt; getGenesByAffyIdUsingGET(affyId, speciesTypeKey)

Return a list of genes for an affymetrix ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String affyId = "affyId_example"; // String | Affymetrix ID
    Integer speciesTypeKey = 56; // Integer | A list of RGD species type keys can be found in the lookup service
    try {
      List<Gene> result = apiInstance.getGenesByAffyIdUsingGET(affyId, speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGenesByAffyIdUsingGET");
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
| **affyId** | **String**| Affymetrix ID | |
| **speciesTypeKey** | **Integer**| A list of RGD species type keys can be found in the lookup service | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGenesByAliasSymbolUsingGET"></a>
# **getGenesByAliasSymbolUsingGET**
> List&lt;Gene&gt; getGenesByAliasSymbolUsingGET(aliasSymbol, speciesTypeKey)

Return a list of genes for an alias and species

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String aliasSymbol = "aliasSymbol_example"; // String | Gene alias symbol
    Integer speciesTypeKey = 56; // Integer | A list of RGD species type keys can be found in the lookup service
    try {
      List<Gene> result = apiInstance.getGenesByAliasSymbolUsingGET(aliasSymbol, speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGenesByAliasSymbolUsingGET");
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
| **aliasSymbol** | **String**| Gene alias symbol | |
| **speciesTypeKey** | **Integer**| A list of RGD species type keys can be found in the lookup service | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGenesByKeywordUsingGET"></a>
# **getGenesByKeywordUsingGET**
> List&lt;Gene&gt; getGenesByKeywordUsingGET(keyword, speciesTypeKey)

Return a list of genes by keyword and species type key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String keyword = "keyword_example"; // String | Search keyword
    Integer speciesTypeKey = 56; // Integer | Species type key.  A list of species type keys can be found in the lookup service
    try {
      List<Gene> result = apiInstance.getGenesByKeywordUsingGET(keyword, speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGenesByKeywordUsingGET");
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
| **keyword** | **String**| Search keyword | |
| **speciesTypeKey** | **Integer**| Species type key.  A list of species type keys can be found in the lookup service | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGenesByPositionUsingGET"></a>
# **getGenesByPositionUsingGET**
> List&lt;Gene&gt; getGenesByPositionUsingGET(chr, start, stop, mapKey)

Return a list of genes position and map key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String chr = "chr_example"; // String | Chromosome
    Long start = 56L; // Long | Start Position
    Long stop = 56L; // Long | Stop Position
    Integer mapKey = 56; // Integer | A list of RGD assembly map keys can be found in the lookup service
    try {
      List<Gene> result = apiInstance.getGenesByPositionUsingGET(chr, start, stop, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGenesByPositionUsingGET");
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
| **chr** | **String**| Chromosome | |
| **start** | **Long**| Start Position | |
| **stop** | **Long**| Stop Position | |
| **mapKey** | **Integer**| A list of RGD assembly map keys can be found in the lookup service | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGenesBySpeciesUsingGET"></a>
# **getGenesBySpeciesUsingGET**
> List&lt;Gene&gt; getGenesBySpeciesUsingGET(speciesTypeKey)

Return a list of all genes for a species in RGD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | A list of RGD species type keys can be found in the lookup service
    try {
      List<Gene> result = apiInstance.getGenesBySpeciesUsingGET(speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGenesBySpeciesUsingGET");
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
| **speciesTypeKey** | **Integer**| A list of RGD species type keys can be found in the lookup service | |

### Return type

[**List&lt;Gene&gt;**](Gene.md)

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

<a id="getGenesInRegionUsingGET"></a>
# **getGenesInRegionUsingGET**
> List&lt;MappedGenePosition&gt; getGenesInRegionUsingGET(chr, start, stop, mapKey)

Return a list of genes in region

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String chr = "chr_example"; // String | Chromosome
    Long start = 56L; // Long | Start Position
    Long stop = 56L; // Long | Stop Position
    Integer mapKey = 56; // Integer | A list of RGD assembly map keys can be found in the lookup service
    try {
      List<MappedGenePosition> result = apiInstance.getGenesInRegionUsingGET(chr, start, stop, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getGenesInRegionUsingGET");
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
| **chr** | **String**| Chromosome | |
| **start** | **Long**| Start Position | |
| **stop** | **Long**| Stop Position | |
| **mapKey** | **Integer**| A list of RGD assembly map keys can be found in the lookup service | |

### Return type

[**List&lt;MappedGenePosition&gt;**](MappedGenePosition.md)

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

<a id="getMappedGenesByPositionUsingGET"></a>
# **getMappedGenesByPositionUsingGET**
> List&lt;MappedGene&gt; getMappedGenesByPositionUsingGET(chr, start, stop, mapKey)

Return a list of genes position and map key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    String chr = "chr_example"; // String | Chromosome
    Long start = 56L; // Long | Start Position
    Long stop = 56L; // Long | Stop Position
    Integer mapKey = 56; // Integer | A list of RGD assembly map keys can be found in the lookup service
    try {
      List<MappedGene> result = apiInstance.getMappedGenesByPositionUsingGET(chr, start, stop, mapKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getMappedGenesByPositionUsingGET");
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
| **chr** | **String**| Chromosome | |
| **start** | **Long**| Start Position | |
| **stop** | **Long**| Stop Position | |
| **mapKey** | **Integer**| A list of RGD assembly map keys can be found in the lookup service | |

### Return type

[**List&lt;MappedGene&gt;**](MappedGene.md)

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

<a id="getOrthologsByListUsingPOST"></a>
# **getOrthologsByListUsingPOST**
> Map&lt;String, List&lt;Gene&gt;&gt; getOrthologsByListUsingPOST(orthologRequest)

Return a list of gene orthologs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    GeneApi apiInstance = new GeneApi(defaultClient);
    OrthologRequest orthologRequest = new OrthologRequest(); // OrthologRequest | orthologRequest
    try {
      Map<String, List<Gene>> result = apiInstance.getOrthologsByListUsingPOST(orthologRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneApi#getOrthologsByListUsingPOST");
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
| **orthologRequest** | [**OrthologRequest**](OrthologRequest.md)| orthologRequest | |

### Return type

[**Map&lt;String, List&lt;Gene&gt;&gt;**](List.md)

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


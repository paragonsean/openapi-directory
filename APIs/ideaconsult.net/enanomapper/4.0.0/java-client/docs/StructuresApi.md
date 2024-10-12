# StructuresApi

All URIs are relative to *https://api.ideaconsult.net/enanomapper*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSubstanceComposition**](StructuresApi.md#getSubstanceComposition) | **GET** /enm/{db}/substance/{uuid}/composition | Substance composition |
| [**getSubstanceStructures**](StructuresApi.md#getSubstanceStructures) | **GET** /enm/{db}/substance/{uuid}/structures | Get substance composition as a dataset |
| [**searchByIdentifier**](StructuresApi.md#searchByIdentifier) | **GET** /enm/{db}/query/compound/{term}/{representation} | Exact chemical structure search |
| [**searchBySimilarity**](StructuresApi.md#searchBySimilarity) | **GET** /enm/{db}/query/similarity | Exact similarity search |
| [**searchBySmarts**](StructuresApi.md#searchBySmarts) | **GET** /enm/{db}/query/smarts | Substructure search |


<a id="getSubstanceComposition"></a>
# **getSubstanceComposition**
> SubstanceComposition getSubstanceComposition(db, uuid, all, page, pagesize)

Substance composition

Returns substance composition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StructuresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/enanomapper");

    StructuresApi apiInstance = new StructuresApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String uuid = "uuid_example"; // String | Substance UUID
    Boolean all = true; // Boolean | true (Show all compositions) false (do not show hidden compositions)
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      SubstanceComposition result = apiInstance.getSubstanceComposition(db, uuid, all, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StructuresApi#getSubstanceComposition");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **uuid** | **String**| Substance UUID | |
| **all** | **Boolean**| true (Show all compositions) false (do not show hidden compositions) | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**SubstanceComposition**](SubstanceComposition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. compositions found |  -  |
| **404** | compositions not found |  -  |

<a id="getSubstanceStructures"></a>
# **getSubstanceStructures**
> Dataset getSubstanceStructures(db, uuid, page, pagesize)

Get substance composition as a dataset

Returns substance composition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StructuresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/enanomapper");

    StructuresApi apiInstance = new StructuresApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String uuid = "uuid_example"; // String | Substance UUID
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Dataset result = apiInstance.getSubstanceStructures(db, uuid, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StructuresApi#getSubstanceStructures");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **uuid** | **String**| Substance UUID | |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. compositions found |  -  |
| **404** | compositions not found |  -  |

<a id="searchByIdentifier"></a>
# **searchByIdentifier**
> Dataset searchByIdentifier(db, term, representation, search, b64search, casesens, bundleUri, sameas, page, pagesize)

Exact chemical structure search

Returns compounds found

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StructuresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/enanomapper");

    StructuresApi apiInstance = new StructuresApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String term = "search"; // String | search term type
    String representation = "all"; // String | 
    String search = "search_example"; // String | Compound identifier (SMILES, InChI, name, registry identifiers)
    String b64search = "b64search_example"; // String | Base64 encoded mol file; if included, will be used instead of the 'search' parameter
    Boolean casesens = true; // Boolean | Case sensitive search if yes
    String bundleUri = "bundleUri_example"; // String | Bundle URI
    String sameas = "sameas_example"; // String | Ontology URI to define groups of columns
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Dataset result = apiInstance.searchByIdentifier(db, term, representation, search, b64search, casesens, bundleUri, sameas, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StructuresApi#searchByIdentifier");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **term** | **String**| search term type | [enum: search, url, inchikey] |
| **representation** | **String**|  | [enum: all, smiles, reach, stdinchi, stdinchikey, names, iupac_name, synonym, cas, einecs] |
| **search** | **String**| Compound identifier (SMILES, InChI, name, registry identifiers) | [optional] |
| **b64search** | **String**| Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter | [optional] |
| **casesens** | **Boolean**| Case sensitive search if yes | [optional] |
| **bundleUri** | **String**| Bundle URI | [optional] |
| **sameas** | **String**| Ontology URI to define groups of columns | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Entries found |  -  |
| **404** | Entries not found |  -  |

<a id="searchBySimilarity"></a>
# **searchBySimilarity**
> Dataset searchBySimilarity(db, search, b64search, type, threshold, datasetUri, filterBySubstance, bundleUri, sameas, mol, page, pagesize)

Exact similarity search

Returns similar compounds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StructuresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/enanomapper");

    StructuresApi apiInstance = new StructuresApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String search = "search_example"; // String | Compound identifier (SMILES, InChI, name, registry identifiers)
    String b64search = "b64search_example"; // String | Base64 encoded mol file; if included, will be used instead of the 'search' parameter
    String type = "smiles"; // String | Defines the expected content of the search parameter
    BigDecimal threshold = new BigDecimal(78); // BigDecimal | Similarity threshold
    String datasetUri = "datasetUri_example"; // String | Restrict the search within the AMBIT dataset specified with the URI
    Boolean filterBySubstance = true; // Boolean | Restrict the search within the set of structures with assigned substances
    String bundleUri = "bundleUri_example"; // String | If the structure is used in the specified bundle URI, the selection tag will be returned
    String sameas = "sameas_example"; // String | Ontology URI to define groups of columns
    Boolean mol = true; // Boolean | Only for application/json; to include mol as JSON field
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Dataset result = apiInstance.searchBySimilarity(db, search, b64search, type, threshold, datasetUri, filterBySubstance, bundleUri, sameas, mol, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StructuresApi#searchBySimilarity");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **search** | **String**| Compound identifier (SMILES, InChI, name, registry identifiers) | [optional] |
| **b64search** | **String**| Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter | [optional] |
| **type** | **String**| Defines the expected content of the search parameter | [optional] [enum: smiles, mol, url] |
| **threshold** | **BigDecimal**| Similarity threshold | [optional] |
| **datasetUri** | **String**| Restrict the search within the AMBIT dataset specified with the URI | [optional] |
| **filterBySubstance** | **Boolean**| Restrict the search within the set of structures with assigned substances | [optional] |
| **bundleUri** | **String**| If the structure is used in the specified bundle URI, the selection tag will be returned | [optional] |
| **sameas** | **String**| Ontology URI to define groups of columns | [optional] |
| **mol** | **Boolean**| Only for application/json; to include mol as JSON field | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Entries found |  -  |
| **404** | Entries not found |  -  |

<a id="searchBySmarts"></a>
# **searchBySmarts**
> Dataset searchBySmarts(db, search, b64search, type, datasetUri, filterBySubstance, bundleUri, sameas, mol, page, pagesize)

Substructure search

Returns compounds with the specified substructure

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StructuresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/enanomapper");

    StructuresApi apiInstance = new StructuresApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String search = "search_example"; // String | Compound identifier (SMILES, InChI, name, registry identifiers)
    String b64search = "b64search_example"; // String | Base64 encoded mol file; if included, will be used instead of the 'search' parameter
    String type = "smiles"; // String | Defines the expected content of the search parameter
    String datasetUri = "datasetUri_example"; // String | Restrict the search within the AMBIT dataset specified with the URI
    Boolean filterBySubstance = true; // Boolean | Restrict the search within the set of structures with assigned substances
    String bundleUri = "bundleUri_example"; // String | If the structure is used in the specified bundle URI, the selection tag will be returned
    String sameas = "sameas_example"; // String | Ontology URI to define groups of columns
    Boolean mol = true; // Boolean | Only for application/json; to include mol as JSON field
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Dataset result = apiInstance.searchBySmarts(db, search, b64search, type, datasetUri, filterBySubstance, bundleUri, sameas, mol, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StructuresApi#searchBySmarts");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **search** | **String**| Compound identifier (SMILES, InChI, name, registry identifiers) | [optional] |
| **b64search** | **String**| Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter | [optional] |
| **type** | **String**| Defines the expected content of the search parameter | [optional] [enum: smiles, mol, url] |
| **datasetUri** | **String**| Restrict the search within the AMBIT dataset specified with the URI | [optional] |
| **filterBySubstance** | **Boolean**| Restrict the search within the set of structures with assigned substances | [optional] |
| **bundleUri** | **String**| If the structure is used in the specified bundle URI, the selection tag will be returned | [optional] |
| **sameas** | **String**| Ontology URI to define groups of columns | [optional] |
| **mol** | **Boolean**| Only for application/json; to include mol as JSON field | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Entries found |  -  |
| **404** | Entries not found |  -  |


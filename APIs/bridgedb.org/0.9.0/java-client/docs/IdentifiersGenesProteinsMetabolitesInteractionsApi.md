# IdentifiersGenesProteinsMetabolitesInteractionsApi

All URIs are relative to *https://webservice.bridgedb.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organismAttributeSearchQueryGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismAttributeSearchQueryGet) | **GET** /{organism}/attributeSearch/{query} |  |
| [**organismAttributeSetGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismAttributeSetGet) | **GET** /{organism}/attributeSet |  |
| [**organismAttributesSystemCodeIdentifierGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismAttributesSystemCodeIdentifierGet) | **GET** /{organism}/attributes/{systemCode}/{identifier} |  |
| [**organismIsFreeSearchSupportedGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismIsFreeSearchSupportedGet) | **GET** /{organism}/isFreeSearchSupported |  |
| [**organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet) | **GET** /{organism}/isMappingSupported/{sourceSystemCode}/{targetSystemCode} |  |
| [**organismPropertiesGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismPropertiesGet) | **GET** /{organism}/properties |  |
| [**organismSearchQueryGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismSearchQueryGet) | **GET** /{organism}/search/{query} |  |
| [**organismSourceDataSourcesGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismSourceDataSourcesGet) | **GET** /{organism}/sourceDataSources |  |
| [**organismTargetDataSourcesGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismTargetDataSourcesGet) | **GET** /{organism}/targetDataSources |  |
| [**organismXrefExistsSystemCodeIdentifierGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefExistsSystemCodeIdentifierGet) | **GET** /{organism}/xrefExists/{systemCode}/{identifier} |  |
| [**organismXrefsBatchPost**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefsBatchPost) | **POST** /{organism}/xrefsBatch |  |
| [**organismXrefsBatchSystemCodePost**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefsBatchSystemCodePost) | **POST** /{organism}/xrefsBatch/{systemCode} |  |
| [**organismXrefsSystemCodeIdentifierGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefsSystemCodeIdentifierGet) | **GET** /{organism}/xrefs/{systemCode}/{identifier} |  |


<a id="organismAttributeSearchQueryGet"></a>
# **organismAttributeSearchQueryGet**
> organismAttributeSearchQueryGet(organism, query, limit, attrName)



Returns a list of xrefs and associated attributes that contain the query string for a given organism. Results are not restricted to exact matches. Optionally limit results to a specified number per data source, or by the type of attribute. See possible attribute types via /{organism}/attributeSet. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String query = "query_example"; // String | Text to find in attributes
    Integer limit = 56; // Integer | Number of results
    String attrName = "attrName_example"; // String | Restrict search by attribute name (case sensitive). Use GET /{organism}/attributeSet to find out which attributes are supported.
    try {
      apiInstance.organismAttributeSearchQueryGet(organism, query, limit, attrName);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismAttributeSearchQueryGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **query** | **String**| Text to find in attributes | |
| **limit** | **Integer**| Number of results | [optional] |
| **attrName** | **String**| Restrict search by attribute name (case sensitive). Use GET /{organism}/attributeSet to find out which attributes are supported. | [optional] |

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
| **200** | returns a tab-delimited list with the identifier, data source and descriptions found. |  -  |

<a id="organismAttributeSetGet"></a>
# **organismAttributeSetGet**
> organismAttributeSetGet(organism)



Returns the supported attributes to the given Organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    try {
      apiInstance.organismAttributeSetGet(organism);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismAttributeSetGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |

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
| **200** | Returns the supported attributes |  -  |

<a id="organismAttributesSystemCodeIdentifierGet"></a>
# **organismAttributesSystemCodeIdentifierGet**
> organismAttributesSystemCodeIdentifierGet(organism, systemCode, identifier, attrName)



Returns the attributes for a given identifier, data source, organism. Optionally display only a specified attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String systemCode = "En"; // String | System
    String identifier = "ENSG00000122375"; // String | Identifier
    String attrName = "attrName_example"; // String | Type of attribute
    try {
      apiInstance.organismAttributesSystemCodeIdentifierGet(organism, systemCode, identifier, attrName);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismAttributesSystemCodeIdentifierGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **systemCode** | **String**| System | [default to En] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |
| **identifier** | **String**| Identifier | [default to ENSG00000122375] |
| **attrName** | **String**| Type of attribute | [optional] |

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
| **200** | Returns a tab-delimited list with the attributes and their content |  -  |

<a id="organismIsFreeSearchSupportedGet"></a>
# **organismIsFreeSearchSupportedGet**
> organismIsFreeSearchSupportedGet(organism)



Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not /{organism}/search/{query} is supported for a given organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    try {
      apiInstance.organismIsFreeSearchSupportedGet(organism);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismIsFreeSearchSupportedGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |

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
| **200** | Returns &#x60;true&#x60; or &#x60;false&#x60;. |  -  |

<a id="organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet"></a>
# **organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet**
> organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet(organism, sourceSystemCode, targetSystemCode)



Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not /{organism}/xrefs/{systemCode}/{identifier} would possibly return a {targetSystemCode} result given a {sourceSystemCode} query. This function basically combines the results of /{organism}/sourceDataSources and /{organism}/targetDataSources into a single boolean result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String sourceSystemCode = "En"; // String | [System code](http://vocabularies.bridgedb.org/#systemCode) for source (input/query) data source
    String targetSystemCode = "En"; // String | [System code](http://vocabularies.bridgedb.org/#systemCode) for target (output/result) data source
    try {
      apiInstance.organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet(organism, sourceSystemCode, targetSystemCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **sourceSystemCode** | **String**| [System code](http://vocabularies.bridgedb.org/#systemCode) for source (input/query) data source | [default to L] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |
| **targetSystemCode** | **String**| [System code](http://vocabularies.bridgedb.org/#systemCode) for target (output/result) data source | [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |

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
| **200** | Returns &#x60;true&#x60; or &#x60;false&#x60;. |  -  |

<a id="organismPropertiesGet"></a>
# **organismPropertiesGet**
> organismPropertiesGet(organism)



Returns the list of properties available for a given organism 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    try {
      apiInstance.organismPropertiesGet(organism);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismPropertiesGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |

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
| **200** | Returns the list of properties available for a given organism |  -  |

<a id="organismSearchQueryGet"></a>
# **organismSearchQueryGet**
> organismSearchQueryGet(organism, query, limit)



Returns a list of xrefs with identifiers that contain the query string for a given organism. Results are not restricted to exact matches. Optionally limit results to a specified number per data source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String query = "1234"; // String | Identifier query
    Integer limit = 56; // Integer | Number of results per data source
    try {
      apiInstance.organismSearchQueryGet(organism, query, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismSearchQueryGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **query** | **String**| Identifier query | [default to 1234] |
| **limit** | **Integer**| Number of results per data source | [optional] |

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
| **200** | Returns a tab-delimited list of xrefs with identifiers that contain the query string for a given organism |  -  |

<a id="organismSourceDataSourcesGet"></a>
# **organismSourceDataSourcesGet**
> organismSourceDataSourcesGet(organism)



Returns a list of data sources available as xref sources for a given organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    try {
      apiInstance.organismSourceDataSourcesGet(organism);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismSourceDataSourcesGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |

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
| **200** | Returns a list of data sources available as xref sources. |  -  |

<a id="organismTargetDataSourcesGet"></a>
# **organismTargetDataSourcesGet**
> organismTargetDataSourcesGet(organism)



Returns a list of data sources available as xref targets for a given organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    try {
      apiInstance.organismTargetDataSourcesGet(organism);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismTargetDataSourcesGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |

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
| **200** | Returns a list of data sources available as xref targets. |  -  |

<a id="organismXrefExistsSystemCodeIdentifierGet"></a>
# **organismXrefExistsSystemCodeIdentifierGet**
> organismXrefExistsSystemCodeIdentifierGet(organism, systemCode, identifier)



Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not an xref exists in the database given an identifier, data source, and organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String systemCode = "En"; // String | Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    String identifier = "1234"; // String | Identifier
    try {
      apiInstance.organismXrefExistsSystemCodeIdentifierGet(organism, systemCode, identifier);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismXrefExistsSystemCodeIdentifierGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **systemCode** | **String**| Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [default to L] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |
| **identifier** | **String**| Identifier | [default to 1234] |

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
| **200** | Returns &#x60;true&#x60; or &#x60;false&#x60; |  -  |

<a id="organismXrefsBatchPost"></a>
# **organismXrefsBatchPost**
> organismXrefsBatchPost(organism, body, dataSource)



Returns a list of xrefs, per identifier, that maps to a given list of identifiers an data source given an organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String body = "body_example"; // String | List of tab separated values: id<tab>systemcode\\n
    String dataSource = "En"; // String | (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    try {
      apiInstance.organismXrefsBatchPost(organism, body, dataSource);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismXrefsBatchPost");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **body** | **String**| List of tab separated values: id&lt;tab&gt;systemcode\\n | |
| **dataSource** | **String**| (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [optional] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a tab-delimited list of xrefs that map to a given identifier |  -  |

<a id="organismXrefsBatchSystemCodePost"></a>
# **organismXrefsBatchSystemCodePost**
> organismXrefsBatchSystemCodePost(organism, systemCode, body, dataSource)



Returns a list of xrefs, that maps to a given list of identifiers to a given data source and organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String systemCode = "En"; // String | Source (input) data source [system code](http://vocabularies.bridgedb.org/#systemCode)
    String body = "body_example"; // String | List of identifiers. The separator is a new line (\\n)
    String dataSource = "En"; // String | (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    try {
      apiInstance.organismXrefsBatchSystemCodePost(organism, systemCode, body, dataSource);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismXrefsBatchSystemCodePost");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **systemCode** | **String**| Source (input) data source [system code](http://vocabularies.bridgedb.org/#systemCode) | [default to L] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |
| **body** | **String**| List of identifiers. The separator is a new line (\\n) | |
| **dataSource** | **String**| (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [optional] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/html
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a tab-delimited list of xrefs that map to a given identifier |  -  |

<a id="organismXrefsSystemCodeIdentifierGet"></a>
# **organismXrefsSystemCodeIdentifierGet**
> organismXrefsSystemCodeIdentifierGet(organism, systemCode, identifier, dataSource)



Returns a list of xrefs that map to a given identifier, data source, and organism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifiersGenesProteinsMetabolitesInteractionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webservice.bridgedb.org");

    IdentifiersGenesProteinsMetabolitesInteractionsApi apiInstance = new IdentifiersGenesProteinsMetabolitesInteractionsApi(defaultClient);
    String organism = "Human"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
    String systemCode = "En"; // String | Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    String identifier = "1234"; // String | Identifier
    String dataSource = "En"; // String | (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
    try {
      apiInstance.organismXrefsSystemCodeIdentifierGet(organism, systemCode, identifier, dataSource);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifiersGenesProteinsMetabolitesInteractionsApi#organismXrefsSystemCodeIdentifierGet");
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
| **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | [enum: Human, Homo sapiens, Tuberculosis, Mycobacterium tuberculosis, Mosquito, Anopheles gambiae, Zebra fish, Danio rerio, Arabidopsis thaliana, Rice, Oryza sativa, Sea Squirt, Ciona intestinalis, Barley, Hordeum vulgare, Frog, Xenopus tropicalis, Soybean, Glycine max, Fruit fly, Drosophila melanogaster, Horse, Equus caballus, Rhesus Monkey, Macaca mulatta, Wine Grape, Vitis vinifera, Yeast, Saccharomyces cerevisiae, Tomato, Solanum lycopersicum, Rat, Rattus norvegicus, Cow, Bos taurus, Western Balsam Poplar, Populus trichocarpa, Chimpanzee, Pan troglodytes, Indian Rice, Oryza indica, Dog, Canis familiaris, Maize, Zea mays, Pig, Sus scrofa, Worm, Caenorhabditis elegans, Platypus, Ornithorhynchus anatinus, Chicken, Gallus gallus, Fusarium graminearum, Gibberella zeae, Bacillus subtilis, Escherichia coli, Black mold, Aspergillus niger, Mouse, Mus musculus] |
| **systemCode** | **String**| Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [default to L] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |
| **identifier** | **String**| Identifier | [default to 1234] |
| **dataSource** | **String**| (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [optional] [enum: En, Cs, X, E, Rh, Ck, Eco, Cg, Ch, Il, Uc, Rf, Pd, U, Ma, Lm, Wd, Wi, Cpc, Mb, Rk, Ce, S, L, Wg, Om, T, Mc, Ik, H, Re, Ag, Q, Ca, Up, Cks] |

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
| **200** | Returns a tab-delimited list of xrefs that map to a given identifier |  -  |


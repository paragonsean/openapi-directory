# SearchApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAutocomplete**](SearchApi.md#getAutocomplete) | **GET** /search/entity/autocomplete/{term} | Returns list of matching concepts or entities using lexical search |
| [**getSearchEntities**](SearchApi.md#getSearchEntities) | **GET** /search/entity/{term} | Returns list of matching concepts or entities using lexical search |
| [**getSearchHpoEntities**](SearchApi.md#getSearchHpoEntities) | **GET** /search/entity/hpo-pl/{term} | Returns list of matching concepts or entities using lexical search |


<a id="getAutocomplete"></a>
# **getAutocomplete**
> AutocompleteResults getAutocomplete(term, fq, category, prefix, includeEqs, boostFx, boostQ, taxon, rows, start, highlightClass, minMatch, excludeGroups, minimalTokenizer)

Returns list of matching concepts or entities using lexical search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String term = "term_example"; // String | 
    List<String> fq = Arrays.asList(); // List<String> | fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior.
    List<String> category = Arrays.asList(); // List<String> | e.g. gene, disease
    List<String> prefix = Arrays.asList(); // List<String> | ontology prefix: HP, -MONDO
    Boolean includeEqs = false; // Boolean | Include equivalent ids in prefix filter
    List<String> boostFx = Arrays.asList(); // List<String> | boost function e.g. pow(edges,0.334)
    List<String> boostQ = Arrays.asList(); // List<String> | boost query e.g. category:genotype^-10
    List<String> taxon = Arrays.asList(); // List<String> | taxon filter, eg NCBITaxon:9606, includes inferred taxa
    Integer rows = 20; // Integer | number of rows
    String start = "0"; // String | row number to start from
    String highlightClass = "highlightClass_example"; // String | highlight class
    String minMatch = "minMatch_example"; // String | minimum should match parameter, see solr docs for details
    Boolean excludeGroups = false; // Boolean | Exclude grouping classes (classes with subclasses)
    Boolean minimalTokenizer = false; // Boolean | set to true to use the minimal tokenizer, good for variants and genotypes
    try {
      AutocompleteResults result = apiInstance.getAutocomplete(term, fq, category, prefix, includeEqs, boostFx, boostQ, taxon, rows, start, highlightClass, minMatch, excludeGroups, minimalTokenizer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getAutocomplete");
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
| **term** | **String**|  | |
| **fq** | [**List&lt;String&gt;**](String.md)| fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. | [optional] |
| **category** | [**List&lt;String&gt;**](String.md)| e.g. gene, disease | [optional] |
| **prefix** | [**List&lt;String&gt;**](String.md)| ontology prefix: HP, -MONDO | [optional] |
| **includeEqs** | **Boolean**| Include equivalent ids in prefix filter | [optional] [default to false] |
| **boostFx** | [**List&lt;String&gt;**](String.md)| boost function e.g. pow(edges,0.334) | [optional] |
| **boostQ** | [**List&lt;String&gt;**](String.md)| boost query e.g. category:genotype^-10 | [optional] |
| **taxon** | [**List&lt;String&gt;**](String.md)| taxon filter, eg NCBITaxon:9606, includes inferred taxa | [optional] |
| **rows** | **Integer**| number of rows | [optional] [default to 20] |
| **start** | **String**| row number to start from | [optional] [default to 0] |
| **highlightClass** | **String**| highlight class | [optional] |
| **minMatch** | **String**| minimum should match parameter, see solr docs for details | [optional] |
| **excludeGroups** | **Boolean**| Exclude grouping classes (classes with subclasses) | [optional] [default to false] |
| **minimalTokenizer** | **Boolean**| set to true to use the minimal tokenizer, good for variants and genotypes | [optional] [default to false] |

### Return type

[**AutocompleteResults**](AutocompleteResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSearchEntities"></a>
# **getSearchEntities**
> SearchResult getSearchEntities(term, fq, category, prefix, includeEqs, boostFx, boostQ, taxon, rows, start, highlightClass, minMatch, excludeGroups, minimalTokenizer)

Returns list of matching concepts or entities using lexical search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String term = "term_example"; // String | search string, e.g. shh, parkinson, femur
    List<String> fq = Arrays.asList(); // List<String> | fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior.
    List<String> category = Arrays.asList(); // List<String> | e.g. gene, disease
    List<String> prefix = Arrays.asList(); // List<String> | ontology prefix: HP, -MONDO
    Boolean includeEqs = false; // Boolean | Include equivalent ids in prefix filter
    List<String> boostFx = Arrays.asList(); // List<String> | boost function e.g. pow(edges,0.334)
    List<String> boostQ = Arrays.asList(); // List<String> | boost query e.g. category:genotype^-10
    List<String> taxon = Arrays.asList(); // List<String> | taxon filter, eg NCBITaxon:9606, includes inferred taxa
    Integer rows = 20; // Integer | number of rows
    String start = "0"; // String | row number to start from
    String highlightClass = "highlightClass_example"; // String | highlight class
    String minMatch = "minMatch_example"; // String | minimum should match parameter, see solr docs for details
    Boolean excludeGroups = false; // Boolean | Exclude grouping classes (classes with subclasses)
    Boolean minimalTokenizer = false; // Boolean | set to true to use the minimal tokenizer, good for variants and genotypes
    try {
      SearchResult result = apiInstance.getSearchEntities(term, fq, category, prefix, includeEqs, boostFx, boostQ, taxon, rows, start, highlightClass, minMatch, excludeGroups, minimalTokenizer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSearchEntities");
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
| **term** | **String**| search string, e.g. shh, parkinson, femur | |
| **fq** | [**List&lt;String&gt;**](String.md)| fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. | [optional] |
| **category** | [**List&lt;String&gt;**](String.md)| e.g. gene, disease | [optional] |
| **prefix** | [**List&lt;String&gt;**](String.md)| ontology prefix: HP, -MONDO | [optional] |
| **includeEqs** | **Boolean**| Include equivalent ids in prefix filter | [optional] [default to false] |
| **boostFx** | [**List&lt;String&gt;**](String.md)| boost function e.g. pow(edges,0.334) | [optional] |
| **boostQ** | [**List&lt;String&gt;**](String.md)| boost query e.g. category:genotype^-10 | [optional] |
| **taxon** | [**List&lt;String&gt;**](String.md)| taxon filter, eg NCBITaxon:9606, includes inferred taxa | [optional] |
| **rows** | **Integer**| number of rows | [optional] [default to 20] |
| **start** | **String**| row number to start from | [optional] [default to 0] |
| **highlightClass** | **String**| highlight class | [optional] |
| **minMatch** | **String**| minimum should match parameter, see solr docs for details | [optional] |
| **excludeGroups** | **Boolean**| Exclude grouping classes (classes with subclasses) | [optional] [default to false] |
| **minimalTokenizer** | **Boolean**| set to true to use the minimal tokenizer, good for variants and genotypes | [optional] [default to false] |

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSearchHpoEntities"></a>
# **getSearchHpoEntities**
> LayResults getSearchHpoEntities(term, rows, start, phenotypeGroup, phenotypeGroupLabel, anatomicalSystem, anatomicalSystemLabel, highlightClass)

Returns list of matching concepts or entities using lexical search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String term = "term_example"; // String | search string, e.g. muscle atrophy, frequent infections
    Integer rows = 10; // Integer | number of rows
    String start = "0"; // String | row number to start from
    String phenotypeGroup = "phenotypeGroup_example"; // String | phenotype group id
    String phenotypeGroupLabel = "phenotypeGroupLabel_example"; // String | phenotype group label
    String anatomicalSystem = "anatomicalSystem_example"; // String | anatomical system id
    String anatomicalSystemLabel = "anatomicalSystemLabel_example"; // String | anatomical system label
    String highlightClass = "highlightClass_example"; // String | highlight class
    try {
      LayResults result = apiInstance.getSearchHpoEntities(term, rows, start, phenotypeGroup, phenotypeGroupLabel, anatomicalSystem, anatomicalSystemLabel, highlightClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSearchHpoEntities");
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
| **term** | **String**| search string, e.g. muscle atrophy, frequent infections | |
| **rows** | **Integer**| number of rows | [optional] [default to 10] |
| **start** | **String**| row number to start from | [optional] [default to 0] |
| **phenotypeGroup** | **String**| phenotype group id | [optional] |
| **phenotypeGroupLabel** | **String**| phenotype group label | [optional] |
| **anatomicalSystem** | **String**| anatomical system id | [optional] |
| **anatomicalSystemLabel** | **String**| anatomical system label | [optional] |
| **highlightClass** | **String**| highlight class | [optional] |

### Return type

[**LayResults**](LayResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


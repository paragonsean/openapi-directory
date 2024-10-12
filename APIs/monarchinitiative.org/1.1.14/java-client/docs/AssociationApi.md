# AssociationApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssociationBySubjectAndAssocType**](AssociationApi.md#getAssociationBySubjectAndAssocType) | **GET** /association/type/{association_type} | Returns list of matching associations of a given type |
| [**getAssociationBySubjectAndObjectCategorySearch**](AssociationApi.md#getAssociationBySubjectAndObjectCategorySearch) | **GET** /association/find/{subject_category}/{object_category} | Returns list of matching associations between a given subject and object category |
| [**getAssociationBySubjectCategorySearch**](AssociationApi.md#getAssociationBySubjectCategorySearch) | **GET** /association/find/{subject_category} | Returns list of matching associations for a given subject category |
| [**getAssociationObject**](AssociationApi.md#getAssociationObject) | **GET** /association/{id} | Returns the association with a given identifier |
| [**getAssociationsBetween**](AssociationApi.md#getAssociationsBetween) | **GET** /association/between/{subject}/{object} | Returns associations connecting two entities |
| [**getAssociationsFrom**](AssociationApi.md#getAssociationsFrom) | **GET** /association/from/{subject} | Returns list of matching associations starting from a given subject (source) |
| [**getAssociationsTo**](AssociationApi.md#getAssociationsTo) | **GET** /association/to/{object} | Returns list of matching associations pointing to a given object (target) |


<a id="getAssociationBySubjectAndAssocType"></a>
# **getAssociationBySubjectAndAssocType**
> List&lt;AssociationResults&gt; getAssociationBySubjectAndAssocType(associationType, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, subject, _object)

Returns list of matching associations of a given type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AssociationApi apiInstance = new AssociationApi(defaultClient);
    String associationType = "associationType_example"; // String | Association type, eg gene_phenotype
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    String subject = "subject_example"; // String | Subject CURIE
    String _object = "_object_example"; // String | Object CURIE
    try {
      List<AssociationResults> result = apiInstance.getAssociationBySubjectAndAssocType(associationType, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, subject, _object);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationApi#getAssociationBySubjectAndAssocType");
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
| **associationType** | **String**| Association type, eg gene_phenotype | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **subject** | **String**| Subject CURIE | [optional] |
| **_object** | **String**| Object CURIE | [optional] |

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

<a id="getAssociationBySubjectAndObjectCategorySearch"></a>
# **getAssociationBySubjectAndObjectCategorySearch**
> List&lt;AssociationResults&gt; getAssociationBySubjectAndObjectCategorySearch(objectCategory, subjectCategory, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, subject, _object, subjectTaxon, objectTaxon, relation)

Returns list of matching associations between a given subject and object category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AssociationApi apiInstance = new AssociationApi(defaultClient);
    String objectCategory = "objectCategory_example"; // String | Category of entity at link Object (target), e.g. gene, disease, phenotype
    String subjectCategory = "subjectCategory_example"; // String | Category of entity at link Subject (source), e.g. gene, disease, phenotype
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    String subject = "subject_example"; // String | Subject CURIE
    String _object = "_object_example"; // String | Object CURIE
    String subjectTaxon = "subjectTaxon_example"; // String | Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default)
    String objectTaxon = "objectTaxon_example"; // String | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
    String relation = "relation_example"; // String | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
    try {
      List<AssociationResults> result = apiInstance.getAssociationBySubjectAndObjectCategorySearch(objectCategory, subjectCategory, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, subject, _object, subjectTaxon, objectTaxon, relation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationApi#getAssociationBySubjectAndObjectCategorySearch");
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
| **objectCategory** | **String**| Category of entity at link Object (target), e.g. gene, disease, phenotype | |
| **subjectCategory** | **String**| Category of entity at link Subject (source), e.g. gene, disease, phenotype | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **subject** | **String**| Subject CURIE | [optional] |
| **_object** | **String**| Object CURIE | [optional] |
| **subjectTaxon** | **String**| Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) | [optional] |
| **objectTaxon** | **String**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] |
| **relation** | **String**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] |

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

<a id="getAssociationBySubjectCategorySearch"></a>
# **getAssociationBySubjectCategorySearch**
> List&lt;AssociationResults&gt; getAssociationBySubjectCategorySearch(subjectCategory, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, subjectTaxon, objectTaxon, relation)

Returns list of matching associations for a given subject category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AssociationApi apiInstance = new AssociationApi(defaultClient);
    String subjectCategory = "subjectCategory_example"; // String | Category of entity at link Subject (source), e.g. gene, disease, phenotype
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    String subjectTaxon = "subjectTaxon_example"; // String | Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default)
    String objectTaxon = "objectTaxon_example"; // String | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
    String relation = "relation_example"; // String | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
    try {
      List<AssociationResults> result = apiInstance.getAssociationBySubjectCategorySearch(subjectCategory, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, subjectTaxon, objectTaxon, relation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationApi#getAssociationBySubjectCategorySearch");
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
| **subjectCategory** | **String**| Category of entity at link Subject (source), e.g. gene, disease, phenotype | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **subjectTaxon** | **String**| Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) | [optional] |
| **objectTaxon** | **String**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] |
| **relation** | **String**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] |

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

<a id="getAssociationObject"></a>
# **getAssociationObject**
> List&lt;AssociationResults&gt; getAssociationObject(id)

Returns the association with a given identifier

An association connects, at a minimum, two things, designated subject and object, via some relationship. Associations also include evidence, provenance etc.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AssociationApi apiInstance = new AssociationApi(defaultClient);
    String id = "id_example"; // String | identifier for an association, e.g. f5ba436c-f851-41b3-9d9d-bb2b5fc879d4
    try {
      List<AssociationResults> result = apiInstance.getAssociationObject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationApi#getAssociationObject");
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
| **id** | **String**| identifier for an association, e.g. f5ba436c-f851-41b3-9d9d-bb2b5fc879d4 | |

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

<a id="getAssociationsBetween"></a>
# **getAssociationsBetween**
> List&lt;AssociationResults&gt; getAssociationsBetween(_object, subject, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations)

Returns associations connecting two entities

Given two entities (e.g. a particular gene and a particular disease), if these two entities are connected (directly or indirectly), then return the association objects describing the connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AssociationApi apiInstance = new AssociationApi(defaultClient);
    String _object = "_object_example"; // String | Return associations pointing to this node, e.g. MP:0013765. Can also be a biological entity such as a gene
    String subject = "subject_example"; // String | Return associations emanating from this node, e.g. MGI:1342287 (If ID is from an ontology then results would include inferred associations, by default)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    try {
      List<AssociationResults> result = apiInstance.getAssociationsBetween(_object, subject, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationApi#getAssociationsBetween");
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
| **_object** | **String**| Return associations pointing to this node, e.g. MP:0013765. Can also be a biological entity such as a gene | |
| **subject** | **String**| Return associations emanating from this node, e.g. MGI:1342287 (If ID is from an ontology then results would include inferred associations, by default) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |

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

<a id="getAssociationsFrom"></a>
# **getAssociationsFrom**
> List&lt;AssociationResults&gt; getAssociationsFrom(subject, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, objectTaxon, relation)

Returns list of matching associations starting from a given subject (source)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AssociationApi apiInstance = new AssociationApi(defaultClient);
    String subject = "subject_example"; // String | Return associations emanating from this node, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357 (If ID is from an ontology then results would include inferred associations, by default)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    String objectTaxon = "objectTaxon_example"; // String | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
    String relation = "relation_example"; // String | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
    try {
      List<AssociationResults> result = apiInstance.getAssociationsFrom(subject, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations, objectTaxon, relation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationApi#getAssociationsFrom");
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
| **subject** | **String**| Return associations emanating from this node, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357 (If ID is from an ontology then results would include inferred associations, by default) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **objectTaxon** | **String**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] |
| **relation** | **String**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] |

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

<a id="getAssociationsTo"></a>
# **getAssociationsTo**
> List&lt;AssociationResults&gt; getAssociationsTo(_object, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations)

Returns list of matching associations pointing to a given object (target)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    AssociationApi apiInstance = new AssociationApi(defaultClient);
    String _object = "_object_example"; // String | Return associations pointing to this node, e.g. specifying MP:0013765 will return all genes, variants, strains, etc. annotated with this term. Can also be a biological entity such as a gene
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    try {
      List<AssociationResults> result = apiInstance.getAssociationsTo(_object, rows, start, evidence, unselectEvidence, excludeAutomaticAssertions, useCompactAssociations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssociationApi#getAssociationsTo");
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
| **_object** | **String**| Return associations pointing to this node, e.g. specifying MP:0013765 will return all genes, variants, strains, etc. annotated with this term. Can also be a biological entity such as a gene | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |

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


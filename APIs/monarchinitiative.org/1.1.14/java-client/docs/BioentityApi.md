# BioentityApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAnatomyGeneAssociations**](BioentityApi.md#getAnatomyGeneAssociations) | **GET** /bioentity/anatomy/{id}/genes | Returns genes associated with a given anatomy |
| [**getAnatomyGeneByTaxonAssociations**](BioentityApi.md#getAnatomyGeneByTaxonAssociations) | **GET** /bioentity/anatomy/{id}/genes/{taxid} | Returns gene IDs for all genes associated with a given anatomy, filtered by taxon |
| [**getCaseDiseaseAssociations**](BioentityApi.md#getCaseDiseaseAssociations) | **GET** /bioentity/case/{id}/diseases | Returns diseases associated with a case |
| [**getCaseGenotypeAssociations**](BioentityApi.md#getCaseGenotypeAssociations) | **GET** /bioentity/case/{id}/genotypes | Returns genotypes associated with a case |
| [**getCaseModelAssociations**](BioentityApi.md#getCaseModelAssociations) | **GET** /bioentity/case/{id}/models | Returns models associated with a case |
| [**getCasePhenotypeAssociations**](BioentityApi.md#getCasePhenotypeAssociations) | **GET** /bioentity/case/{id}/phenotypes | Returns phenotypes associated with a case |
| [**getCaseVariantAssociations**](BioentityApi.md#getCaseVariantAssociations) | **GET** /bioentity/case/{id}/variants | Returns variants associated with a case |
| [**getDiseaseCaseAssociations**](BioentityApi.md#getDiseaseCaseAssociations) | **GET** /bioentity/disease/{id}/cases | Returns cases associated with a disease |
| [**getDiseaseGeneAssociations**](BioentityApi.md#getDiseaseGeneAssociations) | **GET** /bioentity/disease/{id}/genes | Returns genes associated with a disease |
| [**getDiseaseGenotypeAssociations**](BioentityApi.md#getDiseaseGenotypeAssociations) | **GET** /bioentity/disease/{id}/genotypes | Returns genotypes associated with a disease |
| [**getDiseaseModelAssociations**](BioentityApi.md#getDiseaseModelAssociations) | **GET** /bioentity/disease/{id}/models | Returns associations to models of the disease |
| [**getDiseaseModelTaxonAssociations**](BioentityApi.md#getDiseaseModelTaxonAssociations) | **GET** /bioentity/disease/{id}/models/{taxon} | Returns associations to models of the disease constrained by taxon |
| [**getDiseasePathwayAssociations**](BioentityApi.md#getDiseasePathwayAssociations) | **GET** /bioentity/disease/{id}/pathways | Returns pathways associated with a disease |
| [**getDiseasePhenotypeAssociations**](BioentityApi.md#getDiseasePhenotypeAssociations) | **GET** /bioentity/disease/{id}/phenotypes | Returns phenotypes associated with disease |
| [**getDiseasePublicationAssociations**](BioentityApi.md#getDiseasePublicationAssociations) | **GET** /bioentity/disease/{id}/publications | Returns publications associated with a disease |
| [**getDiseaseSubstanceAssociations**](BioentityApi.md#getDiseaseSubstanceAssociations) | **GET** /bioentity/disease/{id}/treatment | Returns substances associated with a disease |
| [**getDiseaseVariantAssociations**](BioentityApi.md#getDiseaseVariantAssociations) | **GET** /bioentity/disease/{id}/variants | Returns variants associated with a disease |
| [**getFunctionAssociations**](BioentityApi.md#getFunctionAssociations) | **GET** /bioentity/function/{id} | Returns annotations associated to a function term |
| [**getFunctionGeneAssociations**](BioentityApi.md#getFunctionGeneAssociations) | **GET** /bioentity/function/{id}/genes | Returns genes associated to a GO term |
| [**getFunctionPublicationAssociations**](BioentityApi.md#getFunctionPublicationAssociations) | **GET** /bioentity/function/{id}/publications | Returns publications associated to a GO term |
| [**getFunctionTaxonAssociations**](BioentityApi.md#getFunctionTaxonAssociations) | **GET** /bioentity/function/{id}/taxons | Returns taxons associated to a GO term |
| [**getGeneAnatomyAssociations**](BioentityApi.md#getGeneAnatomyAssociations) | **GET** /bioentity/gene/{id}/anatomy | Returns anatomical entities associated with a gene |
| [**getGeneCaseAssociations**](BioentityApi.md#getGeneCaseAssociations) | **GET** /bioentity/gene/{id}/cases | Returns cases associated with a gene |
| [**getGeneDiseaseAssociations**](BioentityApi.md#getGeneDiseaseAssociations) | **GET** /bioentity/gene/{id}/diseases | Returns diseases associated with gene |
| [**getGeneExpressionAssociations**](BioentityApi.md#getGeneExpressionAssociations) | **GET** /bioentity/gene/{id}/expression/anatomy | Returns expression events for a gene |
| [**getGeneFunctionAssociations**](BioentityApi.md#getGeneFunctionAssociations) | **GET** /bioentity/gene/{id}/function | Returns function associations for a gene |
| [**getGeneGenotypeAssociations**](BioentityApi.md#getGeneGenotypeAssociations) | **GET** /bioentity/gene/{id}/genotypes | Returns genotypes associated with a gene |
| [**getGeneHomologAssociations**](BioentityApi.md#getGeneHomologAssociations) | **GET** /bioentity/gene/{id}/homologs | Returns homologs for a gene |
| [**getGeneInteractions**](BioentityApi.md#getGeneInteractions) | **GET** /bioentity/gene/{id}/interactions | Returns interactions for a gene |
| [**getGeneModelAssociations**](BioentityApi.md#getGeneModelAssociations) | **GET** /bioentity/gene/{id}/models | Returns models associated with a gene |
| [**getGeneOrthologDiseaseAssociations**](BioentityApi.md#getGeneOrthologDiseaseAssociations) | **GET** /bioentity/gene/{id}/ortholog/diseases | Return diseases associated with orthologs of a gene |
| [**getGeneOrthologPhenotypeAssociations**](BioentityApi.md#getGeneOrthologPhenotypeAssociations) | **GET** /bioentity/gene/{id}/ortholog/phenotypes | Return phenotypes associated with orthologs for a gene |
| [**getGenePathwayAssociations**](BioentityApi.md#getGenePathwayAssociations) | **GET** /bioentity/gene/{id}/pathways | Returns pathways associated with gene |
| [**getGenePhenotypeAssociations**](BioentityApi.md#getGenePhenotypeAssociations) | **GET** /bioentity/gene/{id}/phenotypes | Returns phenotypes associated with gene |
| [**getGenePublicationAssociations**](BioentityApi.md#getGenePublicationAssociations) | **GET** /bioentity/gene/{id}/publications | Returns publications associated with a gene |
| [**getGeneVariantAssociations**](BioentityApi.md#getGeneVariantAssociations) | **GET** /bioentity/gene/{id}/variants | Returns variants associated with a gene |
| [**getGenericAssociations**](BioentityApi.md#getGenericAssociations) | **GET** /bioentity/{id}/associations | Returns associations for an entity regardless of the type |
| [**getGenericObject**](BioentityApi.md#getGenericObject) | **GET** /bioentity/{id} | Returns basic info on object of any type |
| [**getGenericObjectByType**](BioentityApi.md#getGenericObjectByType) | **GET** /bioentity/{type}/{id} | Return basic info on an object for a given type |
| [**getGenotypeCaseAssociations**](BioentityApi.md#getGenotypeCaseAssociations) | **GET** /bioentity/genotype/{id}/cases | Returns cases associated with a genotype |
| [**getGenotypeDiseaseAssociations**](BioentityApi.md#getGenotypeDiseaseAssociations) | **GET** /bioentity/genotype/{id}/diseases | Returns diseases associated with a genotype |
| [**getGenotypeGeneAssociations**](BioentityApi.md#getGenotypeGeneAssociations) | **GET** /bioentity/genotype/{id}/genes | Returns genes associated with a genotype |
| [**getGenotypeGenotypeAssociations**](BioentityApi.md#getGenotypeGenotypeAssociations) | **GET** /bioentity/genotype/{id}/genotypes | Returns genotypes-genotype associations |
| [**getGenotypeModelAssociations**](BioentityApi.md#getGenotypeModelAssociations) | **GET** /bioentity/genotype/{id}/models | Returns models associated with a genotype |
| [**getGenotypePhenotypeAssociations**](BioentityApi.md#getGenotypePhenotypeAssociations) | **GET** /bioentity/genotype/{id}/phenotypes | Returns phenotypes associated with a genotype |
| [**getGenotypePublicationAssociations**](BioentityApi.md#getGenotypePublicationAssociations) | **GET** /bioentity/genotype/{id}/publications | Returns publications associated with a genotype |
| [**getGenotypeVariantAssociations**](BioentityApi.md#getGenotypeVariantAssociations) | **GET** /bioentity/genotype/{id}/variants | Returns genotypes-variant associations |
| [**getGotermGeneAssociations**](BioentityApi.md#getGotermGeneAssociations) | **GET** /bioentity/goterm/{id}/genes | Returns associations to GO terms for a gene |
| [**getModelCaseAssociations**](BioentityApi.md#getModelCaseAssociations) | **GET** /bioentity/model/{id}/cases | Returns cases associated with a model |
| [**getModelDiseaseAssociations**](BioentityApi.md#getModelDiseaseAssociations) | **GET** /bioentity/model/{id}/diseases | Returns diseases associated with a model |
| [**getModelGeneAssociations**](BioentityApi.md#getModelGeneAssociations) | **GET** /bioentity/model/{id}/genes | Returns genes associated with a model |
| [**getModelGenotypeAssociations**](BioentityApi.md#getModelGenotypeAssociations) | **GET** /bioentity/model/{id}/genotypes | Returns genotypes associated with a model |
| [**getModelPhenotypeAssociations**](BioentityApi.md#getModelPhenotypeAssociations) | **GET** /bioentity/model/{id}/phenotypes | Returns phenotypes associated with a model |
| [**getModelPublicationAssociations**](BioentityApi.md#getModelPublicationAssociations) | **GET** /bioentity/model/{id}/publications | Returns publications associated with a model |
| [**getModelVariantAssociations**](BioentityApi.md#getModelVariantAssociations) | **GET** /bioentity/model/{id}/variants | Returns variants associated with a model |
| [**getPathwayDiseaseAssociations**](BioentityApi.md#getPathwayDiseaseAssociations) | **GET** /bioentity/pathway/{id}/diseases | Returns diseases associated with a pathway |
| [**getPathwayGeneAssociations**](BioentityApi.md#getPathwayGeneAssociations) | **GET** /bioentity/pathway/{id}/genes | Returns genes associated with a pathway |
| [**getPathwayPhenotypeAssociations**](BioentityApi.md#getPathwayPhenotypeAssociations) | **GET** /bioentity/pathway/{id}/phenotypes | Returns phenotypes associated with a pathway |
| [**getPhenotypeAnatomyAssociations**](BioentityApi.md#getPhenotypeAnatomyAssociations) | **GET** /bioentity/phenotype/{id}/anatomy | Returns anatomical entities associated with a phenotype |
| [**getPhenotypeCaseAssociations**](BioentityApi.md#getPhenotypeCaseAssociations) | **GET** /bioentity/phenotype/{id}/cases | Returns cases associated with a phenotype |
| [**getPhenotypeDiseaseAssociations**](BioentityApi.md#getPhenotypeDiseaseAssociations) | **GET** /bioentity/phenotype/{id}/diseases | Returns diseases associated with a phenotype |
| [**getPhenotypeGeneAssociations**](BioentityApi.md#getPhenotypeGeneAssociations) | **GET** /bioentity/phenotype/{id}/genes | Returns genes associated with a phenotype |
| [**getPhenotypeGeneByTaxonAssociations**](BioentityApi.md#getPhenotypeGeneByTaxonAssociations) | **GET** /bioentity/phenotype/{id}/gene/{taxid}/ids | Returns gene IDs for all genes associated with a given phenotype, filtered by taxon |
| [**getPhenotypeGenotypeAssociations**](BioentityApi.md#getPhenotypeGenotypeAssociations) | **GET** /bioentity/phenotype/{id}/genotypes | Returns genotypes associated with a phenotype |
| [**getPhenotypePathwayAssociations**](BioentityApi.md#getPhenotypePathwayAssociations) | **GET** /bioentity/phenotype/{id}/pathways | Returns pathways associated with a phenotype |
| [**getPhenotypePublicationAssociations**](BioentityApi.md#getPhenotypePublicationAssociations) | **GET** /bioentity/phenotype/{id}/publications | Returns publications associated with a phenotype |
| [**getPhenotypeVariantAssociations**](BioentityApi.md#getPhenotypeVariantAssociations) | **GET** /bioentity/phenotype/{id}/variants | Returns variants associated with a phenotype |
| [**getPublicationDiseaseAssociations**](BioentityApi.md#getPublicationDiseaseAssociations) | **GET** /bioentity/publication/{id}/diseases | Returns diseases associated with a publication |
| [**getPublicationGeneAssociations**](BioentityApi.md#getPublicationGeneAssociations) | **GET** /bioentity/publication/{id}/genes | Returns genes associated with a publication |
| [**getPublicationGenotypeAssociations**](BioentityApi.md#getPublicationGenotypeAssociations) | **GET** /bioentity/publication/{id}/genotypes | Returns genotypes associated with a publication |
| [**getPublicationModelAssociations**](BioentityApi.md#getPublicationModelAssociations) | **GET** /bioentity/publication/{id}/models | Returns models associated with a publication |
| [**getPublicationPhenotypeAssociations**](BioentityApi.md#getPublicationPhenotypeAssociations) | **GET** /bioentity/publication/{id}/phenotypes | Returns phenotypes associated with a publication |
| [**getPublicationVariantAssociations**](BioentityApi.md#getPublicationVariantAssociations) | **GET** /bioentity/publication/{id}/variants | Returns variants associated with a publication |
| [**getSubstanceParticipantInAssociations**](BioentityApi.md#getSubstanceParticipantInAssociations) | **GET** /bioentity/substance/{id}/participant_in | Returns associations between an activity and process and the specified substance |
| [**getSubstanceRoleAssociations**](BioentityApi.md#getSubstanceRoleAssociations) | **GET** /bioentity/substance/{id}/roles | Returns associations between given drug and roles |
| [**getSubstanceTreatsAssociations**](BioentityApi.md#getSubstanceTreatsAssociations) | **GET** /bioentity/substance/{id}/treats | Returns substances associated with a disease |
| [**getVariantCaseAssociations**](BioentityApi.md#getVariantCaseAssociations) | **GET** /bioentity/variant/{id}/cases | Returns cases associated with a variant |
| [**getVariantDiseaseAssociations**](BioentityApi.md#getVariantDiseaseAssociations) | **GET** /bioentity/variant/{id}/diseases | Returns diseases associated with a variant |
| [**getVariantGeneAssociations**](BioentityApi.md#getVariantGeneAssociations) | **GET** /bioentity/variant/{id}/genes | Returns genes associated with a variant |
| [**getVariantGenotypeAssociations**](BioentityApi.md#getVariantGenotypeAssociations) | **GET** /bioentity/variant/{id}/genotypes | Returns genotypes associated with a variant |
| [**getVariantModelAssociations**](BioentityApi.md#getVariantModelAssociations) | **GET** /bioentity/variant/{id}/models | Returns models associated with a variant |
| [**getVariantPhenotypeAssociations**](BioentityApi.md#getVariantPhenotypeAssociations) | **GET** /bioentity/variant/{id}/phenotypes | Returns phenotypes associated with a variant |
| [**getVariantPublicationAssociations**](BioentityApi.md#getVariantPublicationAssociations) | **GET** /bioentity/variant/{id}/publications | Returns publications associated with a variant |


<a id="getAnatomyGeneAssociations"></a>
# **getAnatomyGeneAssociations**
> AssociationResults getAnatomyGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genes associated with a given anatomy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getAnatomyGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getAnatomyGeneAssociations");
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
| **id** | **String**| CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getAnatomyGeneByTaxonAssociations"></a>
# **getAnatomyGeneByTaxonAssociations**
> getAnatomyGeneByTaxonAssociations(taxid, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns gene IDs for all genes associated with a given anatomy, filtered by taxon

For example, + NCBITaxon:10090 (mouse)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String taxid = "taxid_example"; // String | Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
    String id = "id_example"; // String | CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      apiInstance.getAnatomyGeneByTaxonAssociations(taxid, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getAnatomyGeneByTaxonAssociations");
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
| **taxid** | **String**| Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus) | |
| **id** | **String**| CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

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
| **200** | Success |  -  |

<a id="getCaseDiseaseAssociations"></a>
# **getCaseDiseaseAssociations**
> AssociationResults getCaseDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns diseases associated with a case

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a case
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getCaseDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getCaseDiseaseAssociations");
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
| **id** | **String**| CURIE identifier for a case | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getCaseGenotypeAssociations"></a>
# **getCaseGenotypeAssociations**
> AssociationResults getCaseGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns genotypes associated with a case

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a case
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getCaseGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getCaseGenotypeAssociations");
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
| **id** | **String**| CURIE identifier for a case | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getCaseModelAssociations"></a>
# **getCaseModelAssociations**
> AssociationResults getCaseModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns models associated with a case

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a case
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getCaseModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getCaseModelAssociations");
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
| **id** | **String**| CURIE identifier for a case | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getCasePhenotypeAssociations"></a>
# **getCasePhenotypeAssociations**
> AssociationResults getCasePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns phenotypes associated with a case

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a case
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getCasePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getCasePhenotypeAssociations");
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
| **id** | **String**| CURIE identifier for a case | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getCaseVariantAssociations"></a>
# **getCaseVariantAssociations**
> AssociationResults getCaseVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns variants associated with a case

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a case
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getCaseVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getCaseVariantAssociations");
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
| **id** | **String**| CURIE identifier for a case | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseaseCaseAssociations"></a>
# **getDiseaseCaseAssociations**
> AssociationResults getDiseaseCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns cases associated with a disease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. MONDO:0007103, MONDO:0010918. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getDiseaseCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseaseCaseAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. MONDO:0007103, MONDO:0010918. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseaseGeneAssociations"></a>
# **getDiseaseGeneAssociations**
> AssociationResults getDiseaseGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q, associationType)

Returns genes associated with a disease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    String associationType = "causal"; // String | Additional filters: causal, non_causal, both
    try {
      AssociationResults result = apiInstance.getDiseaseGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q, associationType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseaseGeneAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |
| **associationType** | **String**| Additional filters: causal, non_causal, both | [optional] [default to both] [enum: causal, non_causal, both] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseaseGenotypeAssociations"></a>
# **getDiseaseGenotypeAssociations**
> AssociationResults getDiseaseGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes associated with a disease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. Orphanet:399158, DOID:0080008. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getDiseaseGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseaseGenotypeAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. Orphanet:399158, DOID:0080008. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseaseModelAssociations"></a>
# **getDiseaseModelAssociations**
> AssociationResults getDiseaseModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns associations to models of the disease

In the association object returned, the subject will be the disease, and the object will be the model. The model may be a gene or genetic element.  If the query disease is a general class, the association subject may be to a specific disease.  In some cases the association will be *direct*, for example if a paper asserts a genotype is a model of a disease.  In other cases, the association will be *indirect*, for example, chaining over orthology. In these cases the chain will be reflected in the *evidence graph*  * TODO: provide hook into owlsim for dynamic computation of models by similarity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getDiseaseModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseaseModelAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseaseModelTaxonAssociations"></a>
# **getDiseaseModelTaxonAssociations**
> AssociationResults getDiseaseModelTaxonAssociations(taxon, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns associations to models of the disease constrained by taxon

See /disease/&lt;id&gt;/models route for full details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String taxon = "taxon_example"; // String | CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:10090 (M. musculus).   Higher level taxa may be used
    String id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getDiseaseModelTaxonAssociations(taxon, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseaseModelTaxonAssociations");
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
| **taxon** | **String**| CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:10090 (M. musculus).   Higher level taxa may be used | |
| **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseasePathwayAssociations"></a>
# **getDiseasePathwayAssociations**
> AssociationResults getDiseasePathwayAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns pathways associated with a disease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. DOID:4450. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getDiseasePathwayAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseasePathwayAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. DOID:4450. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseasePhenotypeAssociations"></a>
# **getDiseasePhenotypeAssociations**
> D2PAssociationResults getDiseasePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns phenotypes associated with disease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, Orphanet:1934, DOID:678. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      D2PAssociationResults result = apiInstance.getDiseasePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseasePhenotypeAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, Orphanet:1934, DOID:678. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**D2PAssociationResults**](D2PAssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseasePublicationAssociations"></a>
# **getDiseasePublicationAssociations**
> AssociationResults getDiseasePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns publications associated with a disease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getDiseasePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseasePublicationAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getDiseaseSubstanceAssociations"></a>
# **getDiseaseSubstanceAssociations**
> getDiseaseSubstanceAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      apiInstance.getDiseaseSubstanceAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseaseSubstanceAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

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
| **200** | Success |  -  |

<a id="getDiseaseVariantAssociations"></a>
# **getDiseaseVariantAssociations**
> AssociationResults getDiseaseVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns variants associated with a disease

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getDiseaseVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getDiseaseVariantAssociations");
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
| **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getFunctionAssociations"></a>
# **getFunctionAssociations**
> getFunctionAssociations(id, start, rows, evidence)

Returns annotations associated to a function term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a function term (e.g. GO:0044598)
    Integer start = 0; // Integer | beginning row
    Integer rows = 100; // Integer | number of rows
    List<String> evidence = Arrays.asList(); // List<String> | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    try {
      apiInstance.getFunctionAssociations(id, start, rows, evidence);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getFunctionAssociations");
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
| **id** | **String**| CURIE identifier of a function term (e.g. GO:0044598) | |
| **start** | **Integer**| beginning row | [optional] [default to 0] |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **evidence** | [**List&lt;String&gt;**](String.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |

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
| **200** | Success |  -  |

<a id="getFunctionGeneAssociations"></a>
# **getFunctionGeneAssociations**
> AssociationResults getFunctionGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q, relationshipType)

Returns genes associated to a GO term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    String relationshipType = "involved_in"; // String | relationship type ('involved_in', 'involved_in_regulation_of' or 'acts_upstream_of_or_within')
    try {
      AssociationResults result = apiInstance.getFunctionGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q, relationshipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getFunctionGeneAssociations");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |
| **relationshipType** | **String**| relationship type (&#39;involved_in&#39;, &#39;involved_in_regulation_of&#39; or &#39;acts_upstream_of_or_within&#39;) | [optional] [default to involved_in] [enum: involved_in, involved_in_regulation_of, acts_upstream_of_or_within] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getFunctionPublicationAssociations"></a>
# **getFunctionPublicationAssociations**
> getFunctionPublicationAssociations(id, start, rows, evidence)

Returns publications associated to a GO term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
    Integer start = 0; // Integer | beginning row
    Integer rows = 100; // Integer | number of rows
    List<String> evidence = Arrays.asList(); // List<String> | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    try {
      apiInstance.getFunctionPublicationAssociations(id, start, rows, evidence);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getFunctionPublicationAssociations");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | |
| **start** | **Integer**| beginning row | [optional] [default to 0] |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **evidence** | [**List&lt;String&gt;**](String.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |

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
| **200** | Success |  -  |

<a id="getFunctionTaxonAssociations"></a>
# **getFunctionTaxonAssociations**
> getFunctionTaxonAssociations(id, start, rows, evidence)

Returns taxons associated to a GO term

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
    Integer start = 0; // Integer | beginning row
    Integer rows = 100; // Integer | number of rows
    List<String> evidence = Arrays.asList(); // List<String> | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    try {
      apiInstance.getFunctionTaxonAssociations(id, start, rows, evidence);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getFunctionTaxonAssociations");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | |
| **start** | **Integer**| beginning row | [optional] [default to 0] |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **evidence** | [**List&lt;String&gt;**](String.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |

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
| **200** | Success |  -  |

<a id="getGeneAnatomyAssociations"></a>
# **getGeneAnatomyAssociations**
> AssociationResults getGeneAnatomyAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns anatomical entities associated with a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:13434
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneAnatomyAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneAnatomyAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:13434 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneCaseAssociations"></a>
# **getGeneCaseAssociations**
> AssociationResults getGeneCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns cases associated with a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. HGNC:613, HGNC:11025
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getGeneCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneCaseAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. HGNC:613, HGNC:11025 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneDiseaseAssociations"></a>
# **getGeneDiseaseAssociations**
> AssociationResults getGeneDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q, associationType)

Returns diseases associated with gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    String associationType = "causal"; // String | Additional filters: causal, non_causal, both
    try {
      AssociationResults result = apiInstance.getGeneDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q, associationType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneDiseaseAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |
| **associationType** | **String**| Additional filters: causal, non_causal, both | [optional] [default to both] [enum: causal, non_causal, both] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneExpressionAssociations"></a>
# **getGeneExpressionAssociations**
> AssociationResults getGeneExpressionAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns expression events for a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneExpressionAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneExpressionAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneFunctionAssociations"></a>
# **getGeneFunctionAssociations**
> AssociationResults getGeneFunctionAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns function associations for a gene

IMPLEMENTATION DETAILS ----------------------  Note: currently this is implemented as a query to the GO/AmiGO solr instance. This directly supports IDs such as:   - ZFIN e.g. ZFIN:ZDB-GENE-050417-357  Note that the AmiGO GOlr natively stores MGI annotations to MGI:MGI:nn. However, the standard for biolink is MGI:nnnn, so you should use this (will be transparently mapped to legacy ID)  Additionally, for some species such as Human, GO has the annotation attached to the UniProt ID. Again, this should be transparently handled; e.g. you can use NCBIGene:6469, and this will be mapped behind the scenes for querying.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | id, e.g. NCBIGene:6469. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getGeneFunctionAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneFunctionAssociations");
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
| **id** | **String**| id, e.g. NCBIGene:6469. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneGenotypeAssociations"></a>
# **getGeneGenotypeAssociations**
> AssociationResults getGeneGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes associated with a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. ZFIN:ZDB-GENE-980526-166
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneGenotypeAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. ZFIN:ZDB-GENE-980526-166 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneHomologAssociations"></a>
# **getGeneHomologAssociations**
> AssociationResults getGeneHomologAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, homologyType, directTaxon)

Returns homologs for a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | Taxon CURIE of homolog, e.g. NCBITaxon:9606 (Can be an ancestral node in the ontology; includes inferred associations by default)
    String homologyType = "P"; // String | P (paralog), O (Ortholog) or LDO (least-diverged ortholog)
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    try {
      AssociationResults result = apiInstance.getGeneHomologAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, homologyType, directTaxon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneHomologAssociations");
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
| **id** | **String**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| Taxon CURIE of homolog, e.g. NCBITaxon:9606 (Can be an ancestral node in the ontology; includes inferred associations by default) | [optional] |
| **homologyType** | **String**| P (paralog), O (Ortholog) or LDO (least-diverged ortholog) | [optional] [enum: P, O, LDO] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneInteractions"></a>
# **getGeneInteractions**
> AssociationResults getGeneInteractions(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns interactions for a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneInteractions(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneInteractions");
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
| **id** | **String**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneModelAssociations"></a>
# **getGeneModelAssociations**
> AssociationResults getGeneModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns models associated with a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:17988
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneModelAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:17988 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneOrthologDiseaseAssociations"></a>
# **getGeneOrthologDiseaseAssociations**
> AssociationResults getGeneOrthologDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Return diseases associated with orthologs of a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneOrthologDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneOrthologDiseaseAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneOrthologPhenotypeAssociations"></a>
# **getGeneOrthologPhenotypeAssociations**
> AssociationResults getGeneOrthologPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Return phenotypes associated with orthologs for a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneOrthologPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneOrthologPhenotypeAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenePathwayAssociations"></a>
# **getGenePathwayAssociations**
> AssociationResults getGenePathwayAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns pathways associated with gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:50846. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenePathwayAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenePathwayAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:50846. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenePhenotypeAssociations"></a>
# **getGenePhenotypeAssociations**
> AssociationResults getGenePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns phenotypes associated with gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenePhenotypeAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenePublicationAssociations"></a>
# **getGenePublicationAssociations**
> AssociationResults getGenePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns publications associated with a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenePublicationAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGeneVariantAssociations"></a>
# **getGeneVariantAssociations**
> AssociationResults getGeneVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns variants associated with a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of gene, e.g. HGNC:10896
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGeneVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGeneVariantAssociations");
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
| **id** | **String**| CURIE identifier of gene, e.g. HGNC:10896 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenericAssociations"></a>
# **getGenericAssociations**
> AssociationResults getGenericAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns associations for an entity regardless of the type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | 
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenericAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenericAssociations");
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
| **id** | **String**|  | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenericObject"></a>
# **getGenericObject**
> BioObject getGenericObject(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns basic info on object of any type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | id, e.g. NCBIGene:84570
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      BioObject result = apiInstance.getGenericObject(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenericObject");
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
| **id** | **String**| id, e.g. NCBIGene:84570 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**BioObject**](BioObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenericObjectByType"></a>
# **getGenericObjectByType**
> getGenericObjectByType(type, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, getAssociationCounts, distinctCounts)

Return basic info on an object for a given type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String type = "gene"; // String | bioentity type
    String id = "id_example"; // String | id, e.g. NCBIGene:84570
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    Boolean getAssociationCounts = false; // Boolean | Get association counts
    Boolean distinctCounts = false; // Boolean | Get distinct counts for associations (to be used in conjunction with 'get_association_counts' parameter)
    try {
      apiInstance.getGenericObjectByType(type, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, getAssociationCounts, distinctCounts);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenericObjectByType");
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
| **type** | **String**| bioentity type | [enum: gene, variant, genotype, phenotype, disease, goterm, pathway, anatomy, substance, individual, publication, model, case] |
| **id** | **String**| id, e.g. NCBIGene:84570 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **getAssociationCounts** | **Boolean**| Get association counts | [optional] [default to false] |
| **distinctCounts** | **Boolean**| Get distinct counts for associations (to be used in conjunction with &#39;get_association_counts&#39; parameter) | [optional] [default to false] |

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
| **200** | Success |  -  |

<a id="getGenotypeCaseAssociations"></a>
# **getGenotypeCaseAssociations**
> AssociationResults getGenotypeCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns cases associated with a genotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. dbSNPIndividual:10440, dbSNPIndividual:22633
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getGenotypeCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypeCaseAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. dbSNPIndividual:10440, dbSNPIndividual:22633 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenotypeDiseaseAssociations"></a>
# **getGenotypeDiseaseAssociations**
> AssociationResults getGenotypeDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns diseases associated with a genotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. dbSNPIndividual:11441 (if non-human will return models)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenotypeDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypeDiseaseAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. dbSNPIndividual:11441 (if non-human will return models) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenotypeGeneAssociations"></a>
# **getGenotypeGeneAssociations**
> AssociationResults getGenotypeGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genes associated with a genotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenotypeGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypeGeneAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenotypeGenotypeAssociations"></a>
# **getGenotypeGenotypeAssociations**
> AssociationResults getGenotypeGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes-genotype associations

Genotypes may be related to one another according to the GENO model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenotypeGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypeGenotypeAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenotypeModelAssociations"></a>
# **getGenotypeModelAssociations**
> AssociationResults getGenotypeModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns models associated with a genotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenotypeModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypeModelAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenotypePhenotypeAssociations"></a>
# **getGenotypePhenotypeAssociations**
> AssociationResults getGenotypePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns phenotypes associated with a genotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenotypePhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypePhenotypeAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenotypePublicationAssociations"></a>
# **getGenotypePublicationAssociations**
> AssociationResults getGenotypePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns publications associated with a genotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenotypePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypePublicationAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGenotypeVariantAssociations"></a>
# **getGenotypeVariantAssociations**
> AssociationResults getGenotypeVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes-variant associations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of genotype, e.g. MONARCH:FBgeno422705
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getGenotypeVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGenotypeVariantAssociations");
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
| **id** | **String**| CURIE identifier of genotype, e.g. MONARCH:FBgeno422705 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getGotermGeneAssociations"></a>
# **getGotermGeneAssociations**
> AssociationResults getGotermGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, relationshipType)

Returns associations to GO terms for a gene

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    String relationshipType = "involved_in"; // String | relationship type ('involved_in', 'involved_in_regulation_of' or 'acts_upstream_of_or_within')
    try {
      AssociationResults result = apiInstance.getGotermGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, relationshipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getGotermGeneAssociations");
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
| **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **relationshipType** | **String**| relationship type (&#39;involved_in&#39;, &#39;involved_in_regulation_of&#39; or &#39;acts_upstream_of_or_within&#39;) | [optional] [default to involved_in] [enum: involved_in, involved_in_regulation_of, acts_upstream_of_or_within] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getModelCaseAssociations"></a>
# **getModelCaseAssociations**
> AssociationResults getModelCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns cases associated with a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a model, e.g. Coriell:GM22295, Coriell:HG02187
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getModelCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getModelCaseAssociations");
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
| **id** | **String**| CURIE identifier for a model, e.g. Coriell:GM22295, Coriell:HG02187 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getModelDiseaseAssociations"></a>
# **getModelDiseaseAssociations**
> AssociationResults getModelDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns diseases associated with a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a model, e.g. MGI:5573196
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getModelDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getModelDiseaseAssociations");
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
| **id** | **String**| CURIE identifier for a model, e.g. MGI:5573196 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getModelGeneAssociations"></a>
# **getModelGeneAssociations**
> AssociationResults getModelGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genes associated with a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a model, e.g. MMRRC:042787
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getModelGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getModelGeneAssociations");
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
| **id** | **String**| CURIE identifier for a model, e.g. MMRRC:042787 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getModelGenotypeAssociations"></a>
# **getModelGenotypeAssociations**
> AssociationResults getModelGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes associated with a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a model, e.g. Coriell:NA16660
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getModelGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getModelGenotypeAssociations");
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
| **id** | **String**| CURIE identifier for a model, e.g. Coriell:NA16660 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getModelPhenotypeAssociations"></a>
# **getModelPhenotypeAssociations**
> AssociationResults getModelPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns phenotypes associated with a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | id
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getModelPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getModelPhenotypeAssociations");
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
| **id** | **String**| id | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getModelPublicationAssociations"></a>
# **getModelPublicationAssociations**
> AssociationResults getModelPublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns publications associated with a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a model, e.g. MGI:5644542
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getModelPublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getModelPublicationAssociations");
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
| **id** | **String**| CURIE identifier for a model, e.g. MGI:5644542 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getModelVariantAssociations"></a>
# **getModelVariantAssociations**
> AssociationResults getModelVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns variants associated with a model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a model, e.g. MMRRC:042787
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getModelVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getModelVariantAssociations");
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
| **id** | **String**| CURIE identifier for a model, e.g. MMRRC:042787 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPathwayDiseaseAssociations"></a>
# **getPathwayDiseaseAssociations**
> AssociationResults getPathwayDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns diseases associated with a pathway

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE any pathway element. E.g. REACT:R-HSA-5387390
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPathwayDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPathwayDiseaseAssociations");
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
| **id** | **String**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPathwayGeneAssociations"></a>
# **getPathwayGeneAssociations**
> AssociationResults getPathwayGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genes associated with a pathway

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE any pathway element. E.g. REACT:R-HSA-5387390
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPathwayGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPathwayGeneAssociations");
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
| **id** | **String**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPathwayPhenotypeAssociations"></a>
# **getPathwayPhenotypeAssociations**
> AssociationResults getPathwayPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns phenotypes associated with a pathway

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE any pathway element. E.g. REACT:R-HSA-5387390
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPathwayPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPathwayPhenotypeAssociations");
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
| **id** | **String**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypeAnatomyAssociations"></a>
# **getPhenotypeAnatomyAssociations**
> List&lt;NamedObject&gt; getPhenotypeAnatomyAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns anatomical entities associated with a phenotype

Example IDs:   * MP:0008521 abnormal Bowman membrane

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of phenotype, e.g. MP:0008521. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      List<NamedObject> result = apiInstance.getPhenotypeAnatomyAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypeAnatomyAssociations");
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
| **id** | **String**| CURIE identifier of phenotype, e.g. MP:0008521. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**List&lt;NamedObject&gt;**](NamedObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypeCaseAssociations"></a>
# **getPhenotypeCaseAssociations**
> AssociationResults getPhenotypeCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns cases associated with a phenotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | Pheno class CURIE identifier, e.g  HP:0011951 (Aspiration pneumonia), HP:0002450 (Abnormal motor neuron morphology)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getPhenotypeCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypeCaseAssociations");
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
| **id** | **String**| Pheno class CURIE identifier, e.g  HP:0011951 (Aspiration pneumonia), HP:0002450 (Abnormal motor neuron morphology) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypeDiseaseAssociations"></a>
# **getPhenotypeDiseaseAssociations**
> D2PAssociationResults getPhenotypeDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns diseases associated with a phenotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of phenotype, e.g. HP:0007359. Equivalent IDs can be used with same results
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      D2PAssociationResults result = apiInstance.getPhenotypeDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypeDiseaseAssociations");
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
| **id** | **String**| CURIE identifier of phenotype, e.g. HP:0007359. Equivalent IDs can be used with same results | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**D2PAssociationResults**](D2PAssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypeGeneAssociations"></a>
# **getPhenotypeGeneAssociations**
> AssociationResults getPhenotypeGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genes associated with a phenotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level), 
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPhenotypeGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypeGeneAssociations");
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
| **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level),  | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypeGeneByTaxonAssociations"></a>
# **getPhenotypeGeneByTaxonAssociations**
> getPhenotypeGeneByTaxonAssociations(taxid, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns gene IDs for all genes associated with a given phenotype, filtered by taxon

For example, MP:0001569 + NCBITaxon:10090 (mouse)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String taxid = "taxid_example"; // String | Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
    String id = "id_example"; // String | Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      apiInstance.getPhenotypeGeneByTaxonAssociations(taxid, id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypeGeneByTaxonAssociations");
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
| **taxid** | **String**| Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus) | |
| **id** | **String**| Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

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
| **200** | Success |  -  |

<a id="getPhenotypeGenotypeAssociations"></a>
# **getPhenotypeGenotypeAssociations**
> AssociationResults getPhenotypeGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes associated with a phenotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPhenotypeGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypeGenotypeAssociations");
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
| **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypePathwayAssociations"></a>
# **getPhenotypePathwayAssociations**
> AssociationResults getPhenotypePathwayAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns pathways associated with a phenotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPhenotypePathwayAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypePathwayAssociations");
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
| **id** | **String**| Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypePublicationAssociations"></a>
# **getPhenotypePublicationAssociations**
> AssociationResults getPhenotypePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns publications associated with a phenotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPhenotypePublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypePublicationAssociations");
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
| **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPhenotypeVariantAssociations"></a>
# **getPhenotypeVariantAssociations**
> AssociationResults getPhenotypeVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns variants associated with a phenotype

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPhenotypeVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPhenotypeVariantAssociations");
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
| **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPublicationDiseaseAssociations"></a>
# **getPublicationDiseaseAssociations**
> AssociationResults getPublicationDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns diseases associated with a publication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPublicationDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPublicationDiseaseAssociations");
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
| **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPublicationGeneAssociations"></a>
# **getPublicationGeneAssociations**
> AssociationResults getPublicationGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genes associated with a publication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPublicationGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPublicationGeneAssociations");
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
| **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPublicationGenotypeAssociations"></a>
# **getPublicationGenotypeAssociations**
> AssociationResults getPublicationGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes associated with a publication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPublicationGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPublicationGenotypeAssociations");
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
| **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPublicationModelAssociations"></a>
# **getPublicationModelAssociations**
> AssociationResults getPublicationModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns models associated with a publication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPublicationModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPublicationModelAssociations");
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
| **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPublicationPhenotypeAssociations"></a>
# **getPublicationPhenotypeAssociations**
> AssociationResults getPublicationPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns phenotypes associated with a publication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPublicationPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPublicationPhenotypeAssociations");
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
| **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getPublicationVariantAssociations"></a>
# **getPublicationVariantAssociations**
> AssociationResults getPublicationVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns variants associated with a publication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getPublicationVariantAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getPublicationVariantAssociations");
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
| **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSubstanceParticipantInAssociations"></a>
# **getSubstanceParticipantInAssociations**
> List&lt;Association&gt; getSubstanceParticipantInAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns associations between an activity and process and the specified substance

Examples relationships:   * substance is a metabolite of a process  * substance is synthesized by a process  * substance is modified by an activity  * substance elicits a response program/pathway  * substance is transported by activity or pathway  For example, CHEBI:40036 (amitrole)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of substance, e.g. CHEBI:40036
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      List<Association> result = apiInstance.getSubstanceParticipantInAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getSubstanceParticipantInAssociations");
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
| **id** | **String**| CURIE identifier of substance, e.g. CHEBI:40036 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

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

<a id="getSubstanceRoleAssociations"></a>
# **getSubstanceRoleAssociations**
> List&lt;Association&gt; getSubstanceRoleAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns associations between given drug and roles

Roles may be human-oriented (e.g. pesticide) or molecular (e.g. enzyme inhibitor)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of substance, e.g. CHEBI:40036
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      List<Association> result = apiInstance.getSubstanceRoleAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getSubstanceRoleAssociations");
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
| **id** | **String**| CURIE identifier of substance, e.g. CHEBI:40036 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

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

<a id="getSubstanceTreatsAssociations"></a>
# **getSubstanceTreatsAssociations**
> getSubstanceTreatsAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of substance, e.g. CHEBI:40036
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      apiInstance.getSubstanceTreatsAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getSubstanceTreatsAssociations");
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
| **id** | **String**| CURIE identifier of substance, e.g. CHEBI:40036 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

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
| **200** | Success |  -  |

<a id="getVariantCaseAssociations"></a>
# **getVariantCaseAssociations**
> AssociationResults getVariantCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns cases associated with a variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of variant, e.g. OMIM:309550.0004, dbSNP:rs5030868
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getVariantCaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getVariantCaseAssociations");
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
| **id** | **String**| CURIE identifier of variant, e.g. OMIM:309550.0004, dbSNP:rs5030868 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantDiseaseAssociations"></a>
# **getVariantDiseaseAssociations**
> AssociationResults getVariantDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns diseases associated with a variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of variant, e.g. ClinVarVariant:14925
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getVariantDiseaseAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getVariantDiseaseAssociations");
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
| **id** | **String**| CURIE identifier of variant, e.g. ClinVarVariant:14925 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantGeneAssociations"></a>
# **getVariantGeneAssociations**
> AssociationResults getVariantGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genes associated with a variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getVariantGeneAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getVariantGeneAssociations");
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
| **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantGenotypeAssociations"></a>
# **getVariantGenotypeAssociations**
> AssociationResults getVariantGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns genotypes associated with a variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getVariantGenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getVariantGenotypeAssociations");
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
| **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantModelAssociations"></a>
# **getVariantModelAssociations**
> AssociationResults getVariantModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct)

Returns models associated with a variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of variant, e.g. OMIM:607623.0012, dbSNP:rs5030868
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    try {
      AssociationResults result = apiInstance.getVariantModelAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getVariantModelAssociations");
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
| **id** | **String**| CURIE identifier of variant, e.g. OMIM:607623.0012, dbSNP:rs5030868 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantPhenotypeAssociations"></a>
# **getVariantPhenotypeAssociations**
> AssociationResults getVariantPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns phenotypes associated with a variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getVariantPhenotypeAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getVariantPhenotypeAssociations");
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
| **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantPublicationAssociations"></a>
# **getVariantPublicationAssociations**
> AssociationResults getVariantPublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q)

Returns publications associated with a variant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BioentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    BioentityApi apiInstance = new BioentityApi(defaultClient);
    String id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
    Integer rows = 100; // Integer | number of rows
    Integer start = 56; // Integer | beginning row
    Boolean facet = false; // Boolean | Enable faceting
    List<String> facetFields = Arrays.asList(); // List<String> | Fields to facet on
    Boolean unselectEvidence = false; // Boolean | If true, excludes evidence objects in response
    Boolean excludeAutomaticAssertions = false; // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
    Boolean fetchObjects = false; // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
    Boolean useCompactAssociations = false; // Boolean | If true, returns results in compact associations format
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
    Boolean direct = false; // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
    List<String> taxon = Arrays.asList(); // List<String> | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
    Boolean directTaxon = false; // Boolean | Set true to exclude inferred taxa
    String relation = "relation_example"; // String | A relation CURIE to filter associations
    String sort = "sort_example"; // String | Sorting responses <field> <desc,asc>
    String q = "q_example"; // String | Query string to filter documents
    try {
      AssociationResults result = apiInstance.getVariantPublicationAssociations(id, rows, start, facet, facetFields, unselectEvidence, excludeAutomaticAssertions, fetchObjects, useCompactAssociations, slim, evidence, direct, taxon, directTaxon, relation, sort, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BioentityApi#getVariantPublicationAssociations");
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
| **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | |
| **rows** | **Integer**| number of rows | [optional] [default to 100] |
| **start** | **Integer**| beginning row | [optional] |
| **facet** | **Boolean**| Enable faceting | [optional] [default to false] |
| **facetFields** | [**List&lt;String&gt;**](String.md)| Fields to facet on | [optional] |
| **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false] |
| **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false] |
| **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false] |
| **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false] |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] |
| **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false] |
| **taxon** | [**List&lt;String&gt;**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] |
| **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false] |
| **relation** | **String**| A relation CURIE to filter associations | [optional] |
| **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] |
| **q** | **String**| Query string to filter documents | [optional] |

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


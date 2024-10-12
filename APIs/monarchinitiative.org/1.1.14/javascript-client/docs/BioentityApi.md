# BioLinkApi.BioentityApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAnatomyGeneAssociations**](BioentityApi.md#getAnatomyGeneAssociations) | **GET** /bioentity/anatomy/{id}/genes | Returns genes associated with a given anatomy
[**getAnatomyGeneByTaxonAssociations**](BioentityApi.md#getAnatomyGeneByTaxonAssociations) | **GET** /bioentity/anatomy/{id}/genes/{taxid} | Returns gene IDs for all genes associated with a given anatomy, filtered by taxon
[**getCaseDiseaseAssociations**](BioentityApi.md#getCaseDiseaseAssociations) | **GET** /bioentity/case/{id}/diseases | Returns diseases associated with a case
[**getCaseGenotypeAssociations**](BioentityApi.md#getCaseGenotypeAssociations) | **GET** /bioentity/case/{id}/genotypes | Returns genotypes associated with a case
[**getCaseModelAssociations**](BioentityApi.md#getCaseModelAssociations) | **GET** /bioentity/case/{id}/models | Returns models associated with a case
[**getCasePhenotypeAssociations**](BioentityApi.md#getCasePhenotypeAssociations) | **GET** /bioentity/case/{id}/phenotypes | Returns phenotypes associated with a case
[**getCaseVariantAssociations**](BioentityApi.md#getCaseVariantAssociations) | **GET** /bioentity/case/{id}/variants | Returns variants associated with a case
[**getDiseaseCaseAssociations**](BioentityApi.md#getDiseaseCaseAssociations) | **GET** /bioentity/disease/{id}/cases | Returns cases associated with a disease
[**getDiseaseGeneAssociations**](BioentityApi.md#getDiseaseGeneAssociations) | **GET** /bioentity/disease/{id}/genes | Returns genes associated with a disease
[**getDiseaseGenotypeAssociations**](BioentityApi.md#getDiseaseGenotypeAssociations) | **GET** /bioentity/disease/{id}/genotypes | Returns genotypes associated with a disease
[**getDiseaseModelAssociations**](BioentityApi.md#getDiseaseModelAssociations) | **GET** /bioentity/disease/{id}/models | Returns associations to models of the disease
[**getDiseaseModelTaxonAssociations**](BioentityApi.md#getDiseaseModelTaxonAssociations) | **GET** /bioentity/disease/{id}/models/{taxon} | Returns associations to models of the disease constrained by taxon
[**getDiseasePathwayAssociations**](BioentityApi.md#getDiseasePathwayAssociations) | **GET** /bioentity/disease/{id}/pathways | Returns pathways associated with a disease
[**getDiseasePhenotypeAssociations**](BioentityApi.md#getDiseasePhenotypeAssociations) | **GET** /bioentity/disease/{id}/phenotypes | Returns phenotypes associated with disease
[**getDiseasePublicationAssociations**](BioentityApi.md#getDiseasePublicationAssociations) | **GET** /bioentity/disease/{id}/publications | Returns publications associated with a disease
[**getDiseaseSubstanceAssociations**](BioentityApi.md#getDiseaseSubstanceAssociations) | **GET** /bioentity/disease/{id}/treatment | Returns substances associated with a disease
[**getDiseaseVariantAssociations**](BioentityApi.md#getDiseaseVariantAssociations) | **GET** /bioentity/disease/{id}/variants | Returns variants associated with a disease
[**getFunctionAssociations**](BioentityApi.md#getFunctionAssociations) | **GET** /bioentity/function/{id} | Returns annotations associated to a function term
[**getFunctionGeneAssociations**](BioentityApi.md#getFunctionGeneAssociations) | **GET** /bioentity/function/{id}/genes | Returns genes associated to a GO term
[**getFunctionPublicationAssociations**](BioentityApi.md#getFunctionPublicationAssociations) | **GET** /bioentity/function/{id}/publications | Returns publications associated to a GO term
[**getFunctionTaxonAssociations**](BioentityApi.md#getFunctionTaxonAssociations) | **GET** /bioentity/function/{id}/taxons | Returns taxons associated to a GO term
[**getGeneAnatomyAssociations**](BioentityApi.md#getGeneAnatomyAssociations) | **GET** /bioentity/gene/{id}/anatomy | Returns anatomical entities associated with a gene
[**getGeneCaseAssociations**](BioentityApi.md#getGeneCaseAssociations) | **GET** /bioentity/gene/{id}/cases | Returns cases associated with a gene
[**getGeneDiseaseAssociations**](BioentityApi.md#getGeneDiseaseAssociations) | **GET** /bioentity/gene/{id}/diseases | Returns diseases associated with gene
[**getGeneExpressionAssociations**](BioentityApi.md#getGeneExpressionAssociations) | **GET** /bioentity/gene/{id}/expression/anatomy | Returns expression events for a gene
[**getGeneFunctionAssociations**](BioentityApi.md#getGeneFunctionAssociations) | **GET** /bioentity/gene/{id}/function | Returns function associations for a gene
[**getGeneGenotypeAssociations**](BioentityApi.md#getGeneGenotypeAssociations) | **GET** /bioentity/gene/{id}/genotypes | Returns genotypes associated with a gene
[**getGeneHomologAssociations**](BioentityApi.md#getGeneHomologAssociations) | **GET** /bioentity/gene/{id}/homologs | Returns homologs for a gene
[**getGeneInteractions**](BioentityApi.md#getGeneInteractions) | **GET** /bioentity/gene/{id}/interactions | Returns interactions for a gene
[**getGeneModelAssociations**](BioentityApi.md#getGeneModelAssociations) | **GET** /bioentity/gene/{id}/models | Returns models associated with a gene
[**getGeneOrthologDiseaseAssociations**](BioentityApi.md#getGeneOrthologDiseaseAssociations) | **GET** /bioentity/gene/{id}/ortholog/diseases | Return diseases associated with orthologs of a gene
[**getGeneOrthologPhenotypeAssociations**](BioentityApi.md#getGeneOrthologPhenotypeAssociations) | **GET** /bioentity/gene/{id}/ortholog/phenotypes | Return phenotypes associated with orthologs for a gene
[**getGenePathwayAssociations**](BioentityApi.md#getGenePathwayAssociations) | **GET** /bioentity/gene/{id}/pathways | Returns pathways associated with gene
[**getGenePhenotypeAssociations**](BioentityApi.md#getGenePhenotypeAssociations) | **GET** /bioentity/gene/{id}/phenotypes | Returns phenotypes associated with gene
[**getGenePublicationAssociations**](BioentityApi.md#getGenePublicationAssociations) | **GET** /bioentity/gene/{id}/publications | Returns publications associated with a gene
[**getGeneVariantAssociations**](BioentityApi.md#getGeneVariantAssociations) | **GET** /bioentity/gene/{id}/variants | Returns variants associated with a gene
[**getGenericAssociations**](BioentityApi.md#getGenericAssociations) | **GET** /bioentity/{id}/associations | Returns associations for an entity regardless of the type
[**getGenericObject**](BioentityApi.md#getGenericObject) | **GET** /bioentity/{id} | Returns basic info on object of any type
[**getGenericObjectByType**](BioentityApi.md#getGenericObjectByType) | **GET** /bioentity/{type}/{id} | Return basic info on an object for a given type
[**getGenotypeCaseAssociations**](BioentityApi.md#getGenotypeCaseAssociations) | **GET** /bioentity/genotype/{id}/cases | Returns cases associated with a genotype
[**getGenotypeDiseaseAssociations**](BioentityApi.md#getGenotypeDiseaseAssociations) | **GET** /bioentity/genotype/{id}/diseases | Returns diseases associated with a genotype
[**getGenotypeGeneAssociations**](BioentityApi.md#getGenotypeGeneAssociations) | **GET** /bioentity/genotype/{id}/genes | Returns genes associated with a genotype
[**getGenotypeGenotypeAssociations**](BioentityApi.md#getGenotypeGenotypeAssociations) | **GET** /bioentity/genotype/{id}/genotypes | Returns genotypes-genotype associations
[**getGenotypeModelAssociations**](BioentityApi.md#getGenotypeModelAssociations) | **GET** /bioentity/genotype/{id}/models | Returns models associated with a genotype
[**getGenotypePhenotypeAssociations**](BioentityApi.md#getGenotypePhenotypeAssociations) | **GET** /bioentity/genotype/{id}/phenotypes | Returns phenotypes associated with a genotype
[**getGenotypePublicationAssociations**](BioentityApi.md#getGenotypePublicationAssociations) | **GET** /bioentity/genotype/{id}/publications | Returns publications associated with a genotype
[**getGenotypeVariantAssociations**](BioentityApi.md#getGenotypeVariantAssociations) | **GET** /bioentity/genotype/{id}/variants | Returns genotypes-variant associations
[**getGotermGeneAssociations**](BioentityApi.md#getGotermGeneAssociations) | **GET** /bioentity/goterm/{id}/genes | Returns associations to GO terms for a gene
[**getModelCaseAssociations**](BioentityApi.md#getModelCaseAssociations) | **GET** /bioentity/model/{id}/cases | Returns cases associated with a model
[**getModelDiseaseAssociations**](BioentityApi.md#getModelDiseaseAssociations) | **GET** /bioentity/model/{id}/diseases | Returns diseases associated with a model
[**getModelGeneAssociations**](BioentityApi.md#getModelGeneAssociations) | **GET** /bioentity/model/{id}/genes | Returns genes associated with a model
[**getModelGenotypeAssociations**](BioentityApi.md#getModelGenotypeAssociations) | **GET** /bioentity/model/{id}/genotypes | Returns genotypes associated with a model
[**getModelPhenotypeAssociations**](BioentityApi.md#getModelPhenotypeAssociations) | **GET** /bioentity/model/{id}/phenotypes | Returns phenotypes associated with a model
[**getModelPublicationAssociations**](BioentityApi.md#getModelPublicationAssociations) | **GET** /bioentity/model/{id}/publications | Returns publications associated with a model
[**getModelVariantAssociations**](BioentityApi.md#getModelVariantAssociations) | **GET** /bioentity/model/{id}/variants | Returns variants associated with a model
[**getPathwayDiseaseAssociations**](BioentityApi.md#getPathwayDiseaseAssociations) | **GET** /bioentity/pathway/{id}/diseases | Returns diseases associated with a pathway
[**getPathwayGeneAssociations**](BioentityApi.md#getPathwayGeneAssociations) | **GET** /bioentity/pathway/{id}/genes | Returns genes associated with a pathway
[**getPathwayPhenotypeAssociations**](BioentityApi.md#getPathwayPhenotypeAssociations) | **GET** /bioentity/pathway/{id}/phenotypes | Returns phenotypes associated with a pathway
[**getPhenotypeAnatomyAssociations**](BioentityApi.md#getPhenotypeAnatomyAssociations) | **GET** /bioentity/phenotype/{id}/anatomy | Returns anatomical entities associated with a phenotype
[**getPhenotypeCaseAssociations**](BioentityApi.md#getPhenotypeCaseAssociations) | **GET** /bioentity/phenotype/{id}/cases | Returns cases associated with a phenotype
[**getPhenotypeDiseaseAssociations**](BioentityApi.md#getPhenotypeDiseaseAssociations) | **GET** /bioentity/phenotype/{id}/diseases | Returns diseases associated with a phenotype
[**getPhenotypeGeneAssociations**](BioentityApi.md#getPhenotypeGeneAssociations) | **GET** /bioentity/phenotype/{id}/genes | Returns genes associated with a phenotype
[**getPhenotypeGeneByTaxonAssociations**](BioentityApi.md#getPhenotypeGeneByTaxonAssociations) | **GET** /bioentity/phenotype/{id}/gene/{taxid}/ids | Returns gene IDs for all genes associated with a given phenotype, filtered by taxon
[**getPhenotypeGenotypeAssociations**](BioentityApi.md#getPhenotypeGenotypeAssociations) | **GET** /bioentity/phenotype/{id}/genotypes | Returns genotypes associated with a phenotype
[**getPhenotypePathwayAssociations**](BioentityApi.md#getPhenotypePathwayAssociations) | **GET** /bioentity/phenotype/{id}/pathways | Returns pathways associated with a phenotype
[**getPhenotypePublicationAssociations**](BioentityApi.md#getPhenotypePublicationAssociations) | **GET** /bioentity/phenotype/{id}/publications | Returns publications associated with a phenotype
[**getPhenotypeVariantAssociations**](BioentityApi.md#getPhenotypeVariantAssociations) | **GET** /bioentity/phenotype/{id}/variants | Returns variants associated with a phenotype
[**getPublicationDiseaseAssociations**](BioentityApi.md#getPublicationDiseaseAssociations) | **GET** /bioentity/publication/{id}/diseases | Returns diseases associated with a publication
[**getPublicationGeneAssociations**](BioentityApi.md#getPublicationGeneAssociations) | **GET** /bioentity/publication/{id}/genes | Returns genes associated with a publication
[**getPublicationGenotypeAssociations**](BioentityApi.md#getPublicationGenotypeAssociations) | **GET** /bioentity/publication/{id}/genotypes | Returns genotypes associated with a publication
[**getPublicationModelAssociations**](BioentityApi.md#getPublicationModelAssociations) | **GET** /bioentity/publication/{id}/models | Returns models associated with a publication
[**getPublicationPhenotypeAssociations**](BioentityApi.md#getPublicationPhenotypeAssociations) | **GET** /bioentity/publication/{id}/phenotypes | Returns phenotypes associated with a publication
[**getPublicationVariantAssociations**](BioentityApi.md#getPublicationVariantAssociations) | **GET** /bioentity/publication/{id}/variants | Returns variants associated with a publication
[**getSubstanceParticipantInAssociations**](BioentityApi.md#getSubstanceParticipantInAssociations) | **GET** /bioentity/substance/{id}/participant_in | Returns associations between an activity and process and the specified substance
[**getSubstanceRoleAssociations**](BioentityApi.md#getSubstanceRoleAssociations) | **GET** /bioentity/substance/{id}/roles | Returns associations between given drug and roles
[**getSubstanceTreatsAssociations**](BioentityApi.md#getSubstanceTreatsAssociations) | **GET** /bioentity/substance/{id}/treats | Returns substances associated with a disease
[**getVariantCaseAssociations**](BioentityApi.md#getVariantCaseAssociations) | **GET** /bioentity/variant/{id}/cases | Returns cases associated with a variant
[**getVariantDiseaseAssociations**](BioentityApi.md#getVariantDiseaseAssociations) | **GET** /bioentity/variant/{id}/diseases | Returns diseases associated with a variant
[**getVariantGeneAssociations**](BioentityApi.md#getVariantGeneAssociations) | **GET** /bioentity/variant/{id}/genes | Returns genes associated with a variant
[**getVariantGenotypeAssociations**](BioentityApi.md#getVariantGenotypeAssociations) | **GET** /bioentity/variant/{id}/genotypes | Returns genotypes associated with a variant
[**getVariantModelAssociations**](BioentityApi.md#getVariantModelAssociations) | **GET** /bioentity/variant/{id}/models | Returns models associated with a variant
[**getVariantPhenotypeAssociations**](BioentityApi.md#getVariantPhenotypeAssociations) | **GET** /bioentity/variant/{id}/phenotypes | Returns phenotypes associated with a variant
[**getVariantPublicationAssociations**](BioentityApi.md#getVariantPublicationAssociations) | **GET** /bioentity/variant/{id}/publications | Returns publications associated with a variant



## getAnatomyGeneAssociations

> AssociationResults getAnatomyGeneAssociations(id, opts)

Returns genes associated with a given anatomy

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getAnatomyGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnatomyGeneByTaxonAssociations

> getAnatomyGeneByTaxonAssociations(taxid, id, opts)

Returns gene IDs for all genes associated with a given anatomy, filtered by taxon

For example, + NCBITaxon:10090 (mouse)

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let taxid = "taxid_example"; // String | Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
let id = "id_example"; // String | CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getAnatomyGeneByTaxonAssociations(taxid, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxid** | **String**| Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus) | 
 **id** | **String**| CURIE identifier of anatomical entity, e.g. GO:0005634 (nucleus), UBERON:0002037 (cerebellum), CL:0000540 (neuron). Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCaseDiseaseAssociations

> AssociationResults getCaseDiseaseAssociations(id, opts)

Returns diseases associated with a case

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a case
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getCaseDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a case | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCaseGenotypeAssociations

> AssociationResults getCaseGenotypeAssociations(id, opts)

Returns genotypes associated with a case

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a case
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getCaseGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a case | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCaseModelAssociations

> AssociationResults getCaseModelAssociations(id, opts)

Returns models associated with a case

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a case
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getCaseModelAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a case | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCasePhenotypeAssociations

> AssociationResults getCasePhenotypeAssociations(id, opts)

Returns phenotypes associated with a case

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a case
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getCasePhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a case | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCaseVariantAssociations

> AssociationResults getCaseVariantAssociations(id, opts)

Returns variants associated with a case

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a case
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getCaseVariantAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a case | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseaseCaseAssociations

> AssociationResults getDiseaseCaseAssociations(id, opts)

Returns cases associated with a disease

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. MONDO:0007103, MONDO:0010918. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getDiseaseCaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. MONDO:0007103, MONDO:0010918. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseaseGeneAssociations

> AssociationResults getDiseaseGeneAssociations(id, opts)

Returns genes associated with a disease

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example", // String | Query string to filter documents
  'associationType': "'both'" // String | Additional filters: causal, non_causal, both
};
apiInstance.getDiseaseGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 
 **associationType** | **String**| Additional filters: causal, non_causal, both | [optional] [default to &#39;both&#39;]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseaseGenotypeAssociations

> AssociationResults getDiseaseGenotypeAssociations(id, opts)

Returns genotypes associated with a disease

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. Orphanet:399158, DOID:0080008. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getDiseaseGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. Orphanet:399158, DOID:0080008. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseaseModelAssociations

> AssociationResults getDiseaseModelAssociations(id, opts)

Returns associations to models of the disease

In the association object returned, the subject will be the disease, and the object will be the model. The model may be a gene or genetic element.  If the query disease is a general class, the association subject may be to a specific disease.  In some cases the association will be *direct*, for example if a paper asserts a genotype is a model of a disease.  In other cases, the association will be *indirect*, for example, chaining over orthology. In these cases the chain will be reflected in the *evidence graph*  * TODO: provide hook into owlsim for dynamic computation of models by similarity

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getDiseaseModelAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseaseModelTaxonAssociations

> AssociationResults getDiseaseModelTaxonAssociations(taxon, id, opts)

Returns associations to models of the disease constrained by taxon

See /disease/&lt;id&gt;/models route for full details

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let taxon = "taxon_example"; // String | CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:10090 (M. musculus).   Higher level taxa may be used
let id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getDiseaseModelTaxonAssociations(taxon, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxon** | **String**| CURIE of organism taxonomy class to constrain models, e.g NCBITaxon:10090 (M. musculus).   Higher level taxa may be used | 
 **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseasePathwayAssociations

> AssociationResults getDiseasePathwayAssociations(id, opts)

Returns pathways associated with a disease

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. DOID:4450. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getDiseasePathwayAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. DOID:4450. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseasePhenotypeAssociations

> D2PAssociationResults getDiseasePhenotypeAssociations(id, opts)

Returns phenotypes associated with disease

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, Orphanet:1934, DOID:678. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getDiseasePhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, Orphanet:1934, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**D2PAssociationResults**](D2PAssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseasePublicationAssociations

> AssociationResults getDiseasePublicationAssociations(id, opts)

Returns publications associated with a disease

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getDiseasePublicationAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDiseaseSubstanceAssociations

> getDiseaseSubstanceAssociations(id, opts)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getDiseaseSubstanceAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. DOID:2841 (asthma). Equivalent IDs not yet supported | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDiseaseVariantAssociations

> AssociationResults getDiseaseVariantAssociations(id, opts)

Returns variants associated with a disease

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getDiseaseVariantAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of disease, e.g. OMIM:605543, DOID:678. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFunctionAssociations

> getFunctionAssociations(id, opts)

Returns annotations associated to a function term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of a function term (e.g. GO:0044598)
let opts = {
  'start': 0, // Number | beginning row
  'rows': 100, // Number | number of rows
  'evidence': ["null"] // [String] | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
};
apiInstance.getFunctionAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of a function term (e.g. GO:0044598) | 
 **start** | **Number**| beginning row | [optional] [default to 0]
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **evidence** | [**[String]**](String.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFunctionGeneAssociations

> AssociationResults getFunctionGeneAssociations(id, opts)

Returns genes associated to a GO term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example", // String | Query string to filter documents
  'relationshipType': "'involved_in'" // String | relationship type ('involved_in', 'involved_in_regulation_of' or 'acts_upstream_of_or_within')
};
apiInstance.getFunctionGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 
 **relationshipType** | **String**| relationship type (&#39;involved_in&#39;, &#39;involved_in_regulation_of&#39; or &#39;acts_upstream_of_or_within&#39;) | [optional] [default to &#39;involved_in&#39;]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFunctionPublicationAssociations

> getFunctionPublicationAssociations(id, opts)

Returns publications associated to a GO term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
let opts = {
  'start': 0, // Number | beginning row
  'rows': 100, // Number | number of rows
  'evidence': ["null"] // [String] | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
};
apiInstance.getFunctionPublicationAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **start** | **Number**| beginning row | [optional] [default to 0]
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **evidence** | [**[String]**](String.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFunctionTaxonAssociations

> getFunctionTaxonAssociations(id, opts)

Returns taxons associated to a GO term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
let opts = {
  'start': 0, // Number | beginning row
  'rows': 100, // Number | number of rows
  'evidence': ["null"] // [String] | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
};
apiInstance.getFunctionTaxonAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **start** | **Number**| beginning row | [optional] [default to 0]
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **evidence** | [**[String]**](String.md)| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGeneAnatomyAssociations

> AssociationResults getGeneAnatomyAssociations(id, opts)

Returns anatomical entities associated with a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:13434
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneAnatomyAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:13434 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneCaseAssociations

> AssociationResults getGeneCaseAssociations(id, opts)

Returns cases associated with a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. HGNC:613, HGNC:11025
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getGeneCaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. HGNC:613, HGNC:11025 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneDiseaseAssociations

> AssociationResults getGeneDiseaseAssociations(id, opts)

Returns diseases associated with gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example", // String | Query string to filter documents
  'associationType': "'both'" // String | Additional filters: causal, non_causal, both
};
apiInstance.getGeneDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 
 **associationType** | **String**| Additional filters: causal, non_causal, both | [optional] [default to &#39;both&#39;]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneExpressionAssociations

> AssociationResults getGeneExpressionAssociations(id, opts)

Returns expression events for a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneExpressionAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneFunctionAssociations

> AssociationResults getGeneFunctionAssociations(id, opts)

Returns function associations for a gene

IMPLEMENTATION DETAILS ----------------------  Note: currently this is implemented as a query to the GO/AmiGO solr instance. This directly supports IDs such as:   - ZFIN e.g. ZFIN:ZDB-GENE-050417-357  Note that the AmiGO GOlr natively stores MGI annotations to MGI:MGI:nn. However, the standard for biolink is MGI:nnnn, so you should use this (will be transparently mapped to legacy ID)  Additionally, for some species such as Human, GO has the annotation attached to the UniProt ID. Again, this should be transparently handled; e.g. you can use NCBIGene:6469, and this will be mapped behind the scenes for querying.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | id, e.g. NCBIGene:6469. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getGeneFunctionAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id, e.g. NCBIGene:6469. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneGenotypeAssociations

> AssociationResults getGeneGenotypeAssociations(id, opts)

Returns genotypes associated with a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. ZFIN:ZDB-GENE-980526-166
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. ZFIN:ZDB-GENE-980526-166 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneHomologAssociations

> AssociationResults getGeneHomologAssociations(id, opts)

Returns homologs for a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | Taxon CURIE of homolog, e.g. NCBITaxon:9606 (Can be an ancestral node in the ontology; includes inferred associations by default)
  'homologyType': "homologyType_example", // String | P (paralog), O (Ortholog) or LDO (least-diverged ortholog)
  'directTaxon': false // Boolean | Set true to exclude inferred taxa
};
apiInstance.getGeneHomologAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| Taxon CURIE of homolog, e.g. NCBITaxon:9606 (Can be an ancestral node in the ontology; includes inferred associations by default) | [optional] 
 **homologyType** | **String**| P (paralog), O (Ortholog) or LDO (least-diverged ortholog) | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneInteractions

> AssociationResults getGeneInteractions(id, opts)

Returns interactions for a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneInteractions(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id, e.g. NCBIGene:3630. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneModelAssociations

> AssociationResults getGeneModelAssociations(id, opts)

Returns models associated with a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:17988
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneModelAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:17988 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneOrthologDiseaseAssociations

> AssociationResults getGeneOrthologDiseaseAssociations(id, opts)

Return diseases associated with orthologs of a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneOrthologDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneOrthologPhenotypeAssociations

> AssociationResults getGeneOrthologPhenotypeAssociations(id, opts)

Return phenotypes associated with orthologs for a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneOrthologPhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenePathwayAssociations

> AssociationResults getGenePathwayAssociations(id, opts)

Returns pathways associated with gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:50846. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenePathwayAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:50846. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenePhenotypeAssociations

> AssociationResults getGenePhenotypeAssociations(id, opts)

Returns phenotypes associated with gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenePhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenePublicationAssociations

> AssociationResults getGenePublicationAssociations(id, opts)

Returns publications associated with a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. NCBIGene:4750
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenePublicationAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. NCBIGene:4750 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGeneVariantAssociations

> AssociationResults getGeneVariantAssociations(id, opts)

Returns variants associated with a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of gene, e.g. HGNC:10896
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGeneVariantAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of gene, e.g. HGNC:10896 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenericAssociations

> AssociationResults getGenericAssociations(id, opts)

Returns associations for an entity regardless of the type

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | 
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenericAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenericObject

> BioObject getGenericObject(id, opts)

Returns basic info on object of any type

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | id, e.g. NCBIGene:84570
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getGenericObject(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id, e.g. NCBIGene:84570 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**BioObject**](BioObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenericObjectByType

> getGenericObjectByType(type, id, opts)

Return basic info on an object for a given type

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let type = "type_example"; // String | bioentity type
let id = "id_example"; // String | id, e.g. NCBIGene:84570
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'getAssociationCounts': false, // Boolean | Get association counts
  'distinctCounts': false // Boolean | Get distinct counts for associations (to be used in conjunction with 'get_association_counts' parameter)
};
apiInstance.getGenericObjectByType(type, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| bioentity type | 
 **id** | **String**| id, e.g. NCBIGene:84570 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **getAssociationCounts** | **Boolean**| Get association counts | [optional] [default to false]
 **distinctCounts** | **Boolean**| Get distinct counts for associations (to be used in conjunction with &#39;get_association_counts&#39; parameter) | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGenotypeCaseAssociations

> AssociationResults getGenotypeCaseAssociations(id, opts)

Returns cases associated with a genotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. dbSNPIndividual:10440, dbSNPIndividual:22633
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getGenotypeCaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. dbSNPIndividual:10440, dbSNPIndividual:22633 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenotypeDiseaseAssociations

> AssociationResults getGenotypeDiseaseAssociations(id, opts)

Returns diseases associated with a genotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. dbSNPIndividual:11441 (if non-human will return models)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenotypeDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. dbSNPIndividual:11441 (if non-human will return models) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenotypeGeneAssociations

> AssociationResults getGenotypeGeneAssociations(id, opts)

Returns genes associated with a genotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenotypeGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenotypeGenotypeAssociations

> AssociationResults getGenotypeGenotypeAssociations(id, opts)

Returns genotypes-genotype associations

Genotypes may be related to one another according to the GENO model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenotypeGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenotypeModelAssociations

> AssociationResults getGenotypeModelAssociations(id, opts)

Returns models associated with a genotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenotypeModelAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenotypePhenotypeAssociations

> AssociationResults getGenotypePhenotypeAssociations(id, opts)

Returns phenotypes associated with a genotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenotypePhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-4286 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenotypePublicationAssociations

> AssociationResults getGenotypePublicationAssociations(id, opts)

Returns publications associated with a genotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenotypePublicationAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. ZFIN:ZDB-FISH-150901-6607 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGenotypeVariantAssociations

> AssociationResults getGenotypeVariantAssociations(id, opts)

Returns genotypes-variant associations

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of genotype, e.g. MONARCH:FBgeno422705
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getGenotypeVariantAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of genotype, e.g. MONARCH:FBgeno422705 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGotermGeneAssociations

> AssociationResults getGotermGeneAssociations(id, opts)

Returns associations to GO terms for a gene

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0044598
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'relationshipType': "'involved_in'" // String | relationship type ('involved_in', 'involved_in_regulation_of' or 'acts_upstream_of_or_within')
};
apiInstance.getGotermGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0044598 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **relationshipType** | **String**| relationship type (&#39;involved_in&#39;, &#39;involved_in_regulation_of&#39; or &#39;acts_upstream_of_or_within&#39;) | [optional] [default to &#39;involved_in&#39;]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelCaseAssociations

> AssociationResults getModelCaseAssociations(id, opts)

Returns cases associated with a model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a model, e.g. Coriell:GM22295, Coriell:HG02187
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getModelCaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a model, e.g. Coriell:GM22295, Coriell:HG02187 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelDiseaseAssociations

> AssociationResults getModelDiseaseAssociations(id, opts)

Returns diseases associated with a model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a model, e.g. MGI:5573196
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getModelDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a model, e.g. MGI:5573196 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelGeneAssociations

> AssociationResults getModelGeneAssociations(id, opts)

Returns genes associated with a model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a model, e.g. MMRRC:042787
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getModelGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a model, e.g. MMRRC:042787 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelGenotypeAssociations

> AssociationResults getModelGenotypeAssociations(id, opts)

Returns genotypes associated with a model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a model, e.g. Coriell:NA16660
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getModelGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a model, e.g. Coriell:NA16660 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelPhenotypeAssociations

> AssociationResults getModelPhenotypeAssociations(id, opts)

Returns phenotypes associated with a model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | id
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getModelPhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelPublicationAssociations

> AssociationResults getModelPublicationAssociations(id, opts)

Returns publications associated with a model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a model, e.g. MGI:5644542
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getModelPublicationAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a model, e.g. MGI:5644542 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getModelVariantAssociations

> AssociationResults getModelVariantAssociations(id, opts)

Returns variants associated with a model

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a model, e.g. MMRRC:042787
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getModelVariantAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a model, e.g. MMRRC:042787 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPathwayDiseaseAssociations

> AssociationResults getPathwayDiseaseAssociations(id, opts)

Returns diseases associated with a pathway

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE any pathway element. E.g. REACT:R-HSA-5387390
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPathwayDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPathwayGeneAssociations

> AssociationResults getPathwayGeneAssociations(id, opts)

Returns genes associated with a pathway

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE any pathway element. E.g. REACT:R-HSA-5387390
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPathwayGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPathwayPhenotypeAssociations

> AssociationResults getPathwayPhenotypeAssociations(id, opts)

Returns phenotypes associated with a pathway

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE any pathway element. E.g. REACT:R-HSA-5387390
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPathwayPhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE any pathway element. E.g. REACT:R-HSA-5387390 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypeAnatomyAssociations

> [NamedObject] getPhenotypeAnatomyAssociations(id, opts)

Returns anatomical entities associated with a phenotype

Example IDs:   * MP:0008521 abnormal Bowman membrane

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of phenotype, e.g. MP:0008521. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getPhenotypeAnatomyAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of phenotype, e.g. MP:0008521. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**[NamedObject]**](NamedObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypeCaseAssociations

> AssociationResults getPhenotypeCaseAssociations(id, opts)

Returns cases associated with a phenotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | Pheno class CURIE identifier, e.g  HP:0011951 (Aspiration pneumonia), HP:0002450 (Abnormal motor neuron morphology)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getPhenotypeCaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Pheno class CURIE identifier, e.g  HP:0011951 (Aspiration pneumonia), HP:0002450 (Abnormal motor neuron morphology) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypeDiseaseAssociations

> D2PAssociationResults getPhenotypeDiseaseAssociations(id, opts)

Returns diseases associated with a phenotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of phenotype, e.g. HP:0007359. Equivalent IDs can be used with same results
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPhenotypeDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of phenotype, e.g. HP:0007359. Equivalent IDs can be used with same results | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**D2PAssociationResults**](D2PAssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypeGeneAssociations

> AssociationResults getPhenotypeGeneAssociations(id, opts)

Returns genes associated with a phenotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level), 
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPhenotypeGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level),  | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypeGeneByTaxonAssociations

> getPhenotypeGeneByTaxonAssociations(taxid, id, opts)

Returns gene IDs for all genes associated with a given phenotype, filtered by taxon

For example, MP:0001569 + NCBITaxon:10090 (mouse)

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let taxid = "taxid_example"; // String | Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus)
let id = "id_example"; // String | Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getPhenotypeGeneByTaxonAssociations(taxid, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxid** | **String**| Species or high level taxon grouping, e.g  NCBITaxon:10090 (Mus musculus) | 
 **id** | **String**| Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPhenotypeGenotypeAssociations

> AssociationResults getPhenotypeGenotypeAssociations(id, opts)

Returns genotypes associated with a phenotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPhenotypeGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypePathwayAssociations

> AssociationResults getPhenotypePathwayAssociations(id, opts)

Returns pathways associated with a phenotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPhenotypePathwayAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Pheno class CURIE identifier, e.g  MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypePublicationAssociations

> AssociationResults getPhenotypePublicationAssociations(id, opts)

Returns publications associated with a phenotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPhenotypePublicationAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhenotypeVariantAssociations

> AssociationResults getPhenotypeVariantAssociations(id, opts)

Returns variants associated with a phenotype

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPhenotypeVariantAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Pheno class CURIE identifier, e.g  WBPhenotype:0000180 (axon morphology variant), MP:0001569 (abnormal circulating bilirubin level) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicationDiseaseAssociations

> AssociationResults getPublicationDiseaseAssociations(id, opts)

Returns diseases associated with a publication

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPublicationDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicationGeneAssociations

> AssociationResults getPublicationGeneAssociations(id, opts)

Returns genes associated with a publication

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPublicationGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicationGenotypeAssociations

> AssociationResults getPublicationGenotypeAssociations(id, opts)

Returns genotypes associated with a publication

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPublicationGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicationModelAssociations

> AssociationResults getPublicationModelAssociations(id, opts)

Returns models associated with a publication

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPublicationModelAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicationPhenotypeAssociations

> AssociationResults getPublicationPhenotypeAssociations(id, opts)

Returns phenotypes associated with a publication

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPublicationPhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicationVariantAssociations

> AssociationResults getPublicationVariantAssociations(id, opts)

Returns variants associated with a publication

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier for a publication, e.g. PMID:11751940
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getPublicationVariantAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier for a publication, e.g. PMID:11751940 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubstanceParticipantInAssociations

> [Association] getSubstanceParticipantInAssociations(id, opts)

Returns associations between an activity and process and the specified substance

Examples relationships:   * substance is a metabolite of a process  * substance is synthesized by a process  * substance is modified by an activity  * substance elicits a response program/pathway  * substance is transported by activity or pathway  For example, CHEBI:40036 (amitrole)

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of substance, e.g. CHEBI:40036
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getSubstanceParticipantInAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of substance, e.g. CHEBI:40036 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubstanceRoleAssociations

> [Association] getSubstanceRoleAssociations(id, opts)

Returns associations between given drug and roles

Roles may be human-oriented (e.g. pesticide) or molecular (e.g. enzyme inhibitor)

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of substance, e.g. CHEBI:40036
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getSubstanceRoleAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of substance, e.g. CHEBI:40036 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubstanceTreatsAssociations

> getSubstanceTreatsAssociations(id, opts)

Returns substances associated with a disease

e.g. drugs or small molecules used to treat

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of substance, e.g. CHEBI:40036
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getSubstanceTreatsAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of substance, e.g. CHEBI:40036 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVariantCaseAssociations

> AssociationResults getVariantCaseAssociations(id, opts)

Returns cases associated with a variant

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of variant, e.g. OMIM:309550.0004, dbSNP:rs5030868
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getVariantCaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of variant, e.g. OMIM:309550.0004, dbSNP:rs5030868 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantDiseaseAssociations

> AssociationResults getVariantDiseaseAssociations(id, opts)

Returns diseases associated with a variant

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of variant, e.g. ClinVarVariant:14925
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getVariantDiseaseAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of variant, e.g. ClinVarVariant:14925 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantGeneAssociations

> AssociationResults getVariantGeneAssociations(id, opts)

Returns genes associated with a variant

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getVariantGeneAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantGenotypeAssociations

> AssociationResults getVariantGenotypeAssociations(id, opts)

Returns genotypes associated with a variant

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getVariantGenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantModelAssociations

> AssociationResults getVariantModelAssociations(id, opts)

Returns models associated with a variant

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of variant, e.g. OMIM:607623.0012, dbSNP:rs5030868
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
};
apiInstance.getVariantModelAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of variant, e.g. OMIM:607623.0012, dbSNP:rs5030868 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantPhenotypeAssociations

> AssociationResults getVariantPhenotypeAssociations(id, opts)

Returns phenotypes associated with a variant

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getVariantPhenotypeAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariantPublicationAssociations

> AssociationResults getVariantPublicationAssociations(id, opts)

Returns publications associated with a variant

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentityApi();
let id = "id_example"; // String | CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'facet': false, // Boolean | Enable faceting
  'facetFields': ["null"], // [String] | Fields to facet on
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'fetchObjects': false, // Boolean | If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'slim': ["null"], // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'direct': false, // Boolean | Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default=False
  'taxon': ["null"], // [String] | One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default
  'directTaxon': false, // Boolean | Set true to exclude inferred taxa
  'relation': "relation_example", // String | A relation CURIE to filter associations
  'sort': "sort_example", // String | Sorting responses <field> <desc,asc>
  'q': "q_example" // String | Query string to filter documents
};
apiInstance.getVariantPublicationAssociations(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| CURIE identifier of variant, e.g. ZFIN:ZDB-ALT-010427-8, ClinVarVariant:39783 | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **facet** | **Boolean**| Enable faceting | [optional] [default to false]
 **facetFields** | [**[String]**](String.md)| Fields to facet on | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **fetchObjects** | **Boolean**| If true, returns a distinct set of association.objects (typically ontology terms). This appears at the top level of the results payload | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **direct** | **Boolean**| Set true to only include direct associations, and false to include inferred (via subclass or subclass|part of), default&#x3D;False | [optional] [default to false]
 **taxon** | [**[String]**](String.md)| One or more taxon CURIE to filter associations by subject taxon; includes inferred associations by default | [optional] 
 **directTaxon** | **Boolean**| Set true to exclude inferred taxa | [optional] [default to false]
 **relation** | **String**| A relation CURIE to filter associations | [optional] 
 **sort** | **String**| Sorting responses &lt;field&gt; &lt;desc,asc&gt; | [optional] 
 **q** | **String**| Query string to filter documents | [optional] 

### Return type

[**AssociationResults**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json




# BioObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **List&lt;String&gt;** |  |  [optional] |
|**id** | **String** | ID or CURIE e.g. MGI:1201606 |  |
|**iri** | **String** | IRI |  [optional] |
|**label** | **String** | RDFS Label |  [optional] |
|**consider** | **List&lt;String&gt;** |  |  [optional] |
|**deprecated** | **Boolean** | True if the node is deprecated/obsoleted. |  [optional] |
|**description** | **String** | Descriptive text for the entity. For ontology classes, this will be a definition. |  [optional] |
|**replacedBy** | **List&lt;String&gt;** |  |  [optional] |
|**synonyms** | [**List&lt;SynonymPropertyValue&gt;**](SynonymPropertyValue.md) | list of synonyms or alternate labels |  [optional] |
|**types** | **List&lt;String&gt;** |  |  [optional] |
|**associationCounts** | **Object** | association counts |  [optional] |
|**taxon** | [**Taxon**](Taxon.md) | Taxon to which the object belongs |  [optional] |
|**xrefs** | **List&lt;String&gt;** | Database cross-references. These are usually CURIEs, but may also be URLs. E.g. ENSEMBL:ENSG00000099940  |  [optional] |




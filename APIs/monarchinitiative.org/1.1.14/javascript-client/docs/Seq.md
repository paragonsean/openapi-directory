# BioLinkApi.Seq

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **[String]** |  | [optional] 
**id** | **String** | ID or CURIE e.g. MGI:1201606 | 
**iri** | **String** | IRI | [optional] 
**label** | **String** | RDFS Label | [optional] 
**consider** | **[String]** |  | [optional] 
**deprecated** | **Boolean** | True if the node is deprecated/obsoleted. | [optional] 
**description** | **String** | Descriptive text for the entity. For ontology classes, this will be a definition. | [optional] 
**replacedBy** | **[String]** |  | [optional] 
**synonyms** | [**[SynonymPropertyValue]**](SynonymPropertyValue.md) | list of synonyms or alternate labels | [optional] 
**types** | **[String]** |  | [optional] 
**associationCounts** | **Object** | association counts | [optional] 
**taxon** | [**Taxon**](Taxon.md) | Taxon to which the object belongs | [optional] 
**xrefs** | **[String]** | Database cross-references. These are usually CURIEs, but may also be URLs. E.g. ENSEMBL:ENSG00000099940  | [optional] 
**alphabet** | **String** | one of: DNA, RNA or AA | [optional] 
**md5checksum** | **String** | checksum | [optional] 
**residues** | **String** | string representing sequence of residues | [optional] 
**seqlen** | **String** | length of sequence | [optional] 



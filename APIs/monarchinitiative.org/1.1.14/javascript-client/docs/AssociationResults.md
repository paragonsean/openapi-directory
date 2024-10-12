# BioLinkApi.AssociationResults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docs** | **[Object]** | solr docs | [optional] 
**facetCounts** | **Object** | Mapping between field names and association counts | [optional] 
**highlighting** | **Object** | Mapping between id and solr highlight | [optional] 
**numFound** | **Number** | total number of associations matching query | [optional] 
**associations** | [**[Association]**](Association.md) | Complete representation of full association object, plus evidence | [optional] 
**compactAssociations** | [**[CompactAssociationSet]**](CompactAssociationSet.md) | Compact representation in which objects (e.g. phenotypes) are collected for subject-predicate pairs | [optional] 
**objects** | **[String]** | List of distinct objects used | [optional] 



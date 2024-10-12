

# AssociationResults


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**docs** | **List&lt;Object&gt;** | solr docs |  [optional] |
|**facetCounts** | **Object** | Mapping between field names and association counts |  [optional] |
|**highlighting** | **Object** | Mapping between id and solr highlight |  [optional] |
|**numFound** | **Integer** | total number of associations matching query |  [optional] |
|**associations** | [**List&lt;Association&gt;**](Association.md) | Complete representation of full association object, plus evidence |  [optional] |
|**compactAssociations** | [**List&lt;CompactAssociationSet&gt;**](CompactAssociationSet.md) | Compact representation in which objects (e.g. phenotypes) are collected for subject-predicate pairs |  [optional] |
|**objects** | **List&lt;String&gt;** | List of distinct objects used |  [optional] |






# Association


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evidenceGraph** | [**Graph**](Graph.md) | An indirect association is a join between two or more direct assocations, e.g. gene to disease via ortholog. We record the full set of associations as a graph object |  [optional] |
|**evidenceTypes** | [**List&lt;EntityReference&gt;**](EntityReference.md) | Evidence types (ECO classes) |  [optional] |
|**id** | **String** | Association/annotation unique ID |  |
|**negated** | **Boolean** | True if association is negated |  [optional] |
|**_object** | [**BioObjectCore**](BioObjectCore.md) | Object (sensu RDF), aka target, e.g. HP:0000448, MP:0002109, DOID:14330 |  |
|**objectEq** | **List&lt;String&gt;** | Equivalent identifiers to object node |  [optional] |
|**objectExtensions** | [**List&lt;AnnotationExtension&gt;**](AnnotationExtension.md) |  |  [optional] |
|**providedBy** | **List&lt;String&gt;** | Provider of association, e.g. Orphanet, ClinVar |  [optional] |
|**publications** | [**List&lt;EntityReference&gt;**](EntityReference.md) | Publications supporting association, extracted from evidence graph |  [optional] |
|**qualifiers** | **List&lt;String&gt;** | Qualifier on the association |  [optional] |
|**relation** | [**RelationRef**](RelationRef.md) | Relationship type connecting subject and object |  |
|**slim** | **List&lt;String&gt;** | Objects mapped to a slim |  [optional] |
|**subject** | [**BioObjectCore**](BioObjectCore.md) | Subject of association (what it is about), e.g. ClinVar:nnn, MGI:1201606 |  |
|**subjectEq** | **List&lt;String&gt;** | Equivalent identifiers to subject node |  [optional] |
|**subjectExtensions** | [**List&lt;AnnotationExtension&gt;**](AnnotationExtension.md) |  |  [optional] |
|**type** | **String** | Type of association, e.g. gene-phenotype |  [optional] |




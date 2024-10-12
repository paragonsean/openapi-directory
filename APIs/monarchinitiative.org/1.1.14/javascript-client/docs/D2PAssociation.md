# BioLinkApi.D2PAssociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidenceGraph** | [**Graph**](Graph.md) | An indirect association is a join between two or more direct assocations, e.g. gene to disease via ortholog. We record the full set of associations as a graph object | [optional] 
**evidenceTypes** | [**[EntityReference]**](EntityReference.md) | Evidence types (ECO classes) | [optional] 
**id** | **String** | Association/annotation unique ID | 
**negated** | **Boolean** | True if association is negated | [optional] 
**object** | [**BioObjectCore**](BioObjectCore.md) | Object (sensu RDF), aka target, e.g. HP:0000448, MP:0002109, DOID:14330 | 
**objectEq** | **[String]** | Equivalent identifiers to object node | [optional] 
**objectExtensions** | [**[AnnotationExtension]**](AnnotationExtension.md) |  | [optional] 
**providedBy** | **[String]** | Provider of association, e.g. Orphanet, ClinVar | [optional] 
**publications** | [**[EntityReference]**](EntityReference.md) | Publications supporting association, extracted from evidence graph | [optional] 
**qualifiers** | **[String]** | Qualifier on the association | [optional] 
**relation** | [**RelationRef**](RelationRef.md) | Relationship type connecting subject and object | 
**slim** | **[String]** | Objects mapped to a slim | [optional] 
**subject** | [**BioObjectCore**](BioObjectCore.md) | Subject of association (what it is about), e.g. ClinVar:nnn, MGI:1201606 | 
**subjectEq** | **[String]** | Equivalent identifiers to subject node | [optional] 
**subjectExtensions** | [**[AnnotationExtension]**](AnnotationExtension.md) |  | [optional] 
**type** | **String** | Type of association, e.g. gene-phenotype | [optional] 
**frequency** | [**EntityReference**](EntityReference.md) | Frequency of phenotype in patients with disease | [optional] 
**onset** | [**EntityReference**](EntityReference.md) | Onset of phenotype in disease process | [optional] 



# CloudHealthcareApi.AnalyzeEntitiesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**[Entity]**](Entity.md) | The union of all the candidate entities that the entity_mentions in this response could link to. These are UMLS concepts or normalized mention content. | [optional] 
**entityMentions** | [**[EntityMention]**](EntityMention.md) | The &#x60;entity_mentions&#x60; field contains all the annotated medical entities that were mentioned in the provided document. | [optional] 
**fhirBundle** | **String** | The FHIR bundle ([&#x60;R4&#x60;](http://hl7.org/fhir/R4/bundle.html)) that includes all the entities, the entity mentions, and the relationships in JSON format. | [optional] 
**relationships** | [**[EntityMentionRelationship]**](EntityMentionRelationship.md) | relationships contains all the binary relationships that were identified between entity mentions within the provided document. | [optional] 



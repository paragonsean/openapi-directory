# CloudHealthcareApi.Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityId** | **String** | entity_id is a first class field entity_id uniquely identifies this concept and its meta-vocabulary. For example, \&quot;UMLS/C0000970\&quot;. | [optional] 
**preferredTerm** | **String** | preferred_term is the preferred term for this concept. For example, \&quot;Acetaminophen\&quot;. For ad hoc entities formed by normalization, this is the most popular unnormalized string. | [optional] 
**vocabularyCodes** | **[String]** | Vocabulary codes are first-class fields and differentiated from the concept unique identifier (entity_id). vocabulary_codes contains the representation of this concept in particular vocabularies, such as ICD-10, SNOMED-CT and RxNORM. These are prefixed by the name of the vocabulary, followed by the unique code within that vocabulary. For example, \&quot;RXNORM/A10334543\&quot;. | [optional] 



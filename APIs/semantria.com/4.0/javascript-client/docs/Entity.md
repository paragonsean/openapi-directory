# Semantria.Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | The count of occurrences of the entity across the documents | 
**entityType** | **String** | Type of the entity (Company, Person, Place, Product, etc.) | 
**label** | **String** | Descriptive label for the entity, if applicable | 
**mentions** | [**[Mention]**](Mention.md) | Returns the genuine forms of entity mentioned across the documents | 
**negativeCount** | **Number** | The count of negative occurrences of the entity across the documents | 
**neutralCount** | **Number** | The count of neutral occurrences of the entity across the documents | 
**positiveCount** | **Number** | The count of positive occurrences of the entity across the documents | 
**title** | **String** | Normalized form of the entity. It is the normalized entity title | 
**type** | **String** | Type of the entity; can be either “named” or “user” (reserved for future usage) | 



## Enum: TypeEnum


* `named` (value: `"named"`)

* `user` (value: `"user"`)





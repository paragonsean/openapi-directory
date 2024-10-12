

# Entity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | The count of occurrences of the entity across the documents |  |
|**entityType** | **String** | Type of the entity (Company, Person, Place, Product, etc.) |  |
|**label** | **String** | Descriptive label for the entity, if applicable |  |
|**mentions** | [**List&lt;Mention&gt;**](Mention.md) | Returns the genuine forms of entity mentioned across the documents |  |
|**negativeCount** | **Integer** | The count of negative occurrences of the entity across the documents |  |
|**neutralCount** | **Integer** | The count of neutral occurrences of the entity across the documents |  |
|**positiveCount** | **Integer** | The count of positive occurrences of the entity across the documents |  |
|**title** | **String** | Normalized form of the entity. It is the normalized entity title |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the entity; can be either “named” or “user” (reserved for future usage) |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NAMED | &quot;named&quot; |
| USER | &quot;user&quot; |




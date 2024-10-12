

# Relation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceScore** | **Float** | A measure of confidence in the relationship extraction |  |
|**entities** | [**List&lt;RelationEntity&gt;**](RelationEntity.md) | Returns entities which presents parent relationship |  |
|**extra** | **String** | Extra information that has been extracted about the relationship |  |
|**relationType** | **String** | A label describing the nature of the relationship |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of relation according to extracted entities |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NAMED | &quot;named&quot; |
| USER | &quot;user&quot; |




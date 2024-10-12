

# SourceDefinitionRead


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dockerImageTag** | **String** |  |  |
|**dockerRepository** | **String** |  |  |
|**documentationUrl** | **URI** |  |  [optional] |
|**icon** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**protocolVersion** | **String** | The Airbyte Protocol version supported by the connector |  [optional] |
|**releaseDate** | **LocalDate** | The date when this connector was first released, in yyyy-mm-dd format. |  [optional] |
|**releaseStage** | **ReleaseStage** |  |  [optional] |
|**resourceRequirements** | [**ActorDefinitionResourceRequirements**](ActorDefinitionResourceRequirements.md) |  |  [optional] |
|**sourceDefinitionId** | **UUID** |  |  |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) |  |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| API | &quot;api&quot; |
| FILE | &quot;file&quot; |
| DATABASE | &quot;database&quot; |
| CUSTOM | &quot;custom&quot; |




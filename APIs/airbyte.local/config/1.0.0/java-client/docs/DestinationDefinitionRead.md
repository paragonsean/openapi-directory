

# DestinationDefinitionRead


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationDefinitionId** | **UUID** |  |  |
|**dockerImageTag** | **String** |  |  |
|**dockerRepository** | **String** |  |  |
|**documentationUrl** | **URI** |  |  |
|**icon** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**normalizationConfig** | [**NormalizationDestinationDefinitionConfig**](NormalizationDestinationDefinitionConfig.md) |  |  |
|**protocolVersion** | **String** | The Airbyte Protocol version supported by the connector |  [optional] |
|**releaseDate** | **LocalDate** | The date when this connector was first released, in yyyy-mm-dd format. |  [optional] |
|**releaseStage** | **ReleaseStage** |  |  [optional] |
|**resourceRequirements** | [**ActorDefinitionResourceRequirements**](ActorDefinitionResourceRequirements.md) |  |  [optional] |
|**supportsDbt** | **Boolean** | an optional flag indicating whether DBT is used in the normalization. If the flag value is NULL - DBT is not used. |  |




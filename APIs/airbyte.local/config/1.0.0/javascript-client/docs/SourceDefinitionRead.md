# AirbyteConfigurationApi.SourceDefinitionRead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dockerImageTag** | **String** |  | 
**dockerRepository** | **String** |  | 
**documentationUrl** | **String** |  | [optional] 
**icon** | **String** |  | [optional] 
**name** | **String** |  | 
**protocolVersion** | **String** | The Airbyte Protocol version supported by the connector | [optional] 
**releaseDate** | **Date** | The date when this connector was first released, in yyyy-mm-dd format. | [optional] 
**releaseStage** | [**ReleaseStage**](ReleaseStage.md) |  | [optional] 
**resourceRequirements** | [**ActorDefinitionResourceRequirements**](ActorDefinitionResourceRequirements.md) |  | [optional] 
**sourceDefinitionId** | **String** |  | 
**sourceType** | **String** |  | [optional] 



## Enum: SourceTypeEnum


* `api` (value: `"api"`)

* `file` (value: `"file"`)

* `database` (value: `"database"`)

* `custom` (value: `"custom"`)





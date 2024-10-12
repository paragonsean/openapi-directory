

# ConnectorMapping

The connector mapping definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectorMappingName** | **String** | The connector mapping name |  [optional] [readonly] |
|**connectorName** | **String** | The connector name. |  [optional] [readonly] |
|**connectorType** | **ConnectorType** |  |  [optional] |
|**created** | **OffsetDateTime** | The created time. |  [optional] [readonly] |
|**dataFormatId** | **String** | The DataFormat ID. |  [optional] [readonly] |
|**description** | **String** | The description of the connector mapping. |  [optional] |
|**displayName** | **String** | Display name for the connector mapping. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | Defines which entity type the file should map to. |  |
|**entityTypeName** | **String** | The mapping entity name. |  |
|**lastModified** | **OffsetDateTime** | The last modified time. |  [optional] [readonly] |
|**mappingProperties** | [**ConnectorMappingProperties**](ConnectorMappingProperties.md) |  |  |
|**nextRunTime** | **OffsetDateTime** | The next run time based on customer&#39;s settings. |  [optional] [readonly] |
|**runId** | **String** | The RunId. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | State of connector mapping. |  [optional] [readonly] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PROFILE | &quot;Profile&quot; |
| INTERACTION | &quot;Interaction&quot; |
| RELATIONSHIP | &quot;Relationship&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| CREATED | &quot;Created&quot; |
| FAILED | &quot;Failed&quot; |
| READY | &quot;Ready&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPED | &quot;Stopped&quot; |
| EXPIRING | &quot;Expiring&quot; |




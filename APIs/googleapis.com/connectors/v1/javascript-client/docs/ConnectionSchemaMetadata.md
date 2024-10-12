# ConnectorsApi.ConnectionSchemaMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **[String]** | Output only. List of actions. | [optional] [readonly] 
**entities** | **[String]** | Output only. List of entity names. | [optional] [readonly] 
**errorMessage** | **String** | Error message for users. | [optional] 
**name** | **String** | Output only. Resource name. Format: projects/{project}/locations/{location}/connections/{connection}/connectionSchemaMetadata | [optional] [readonly] 
**refreshTime** | **String** | Output only. Timestamp when the connection runtime schema refresh was triggered. | [optional] [readonly] 
**state** | **String** | Output only. The current state of runtime schema. | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when the connection runtime schema was updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `REFRESHING` (value: `"REFRESHING"`)

* `UPDATED` (value: `"UPDATED"`)

* `REFRESHING_SCHEMA_METADATA` (value: `"REFRESHING_SCHEMA_METADATA"`)

* `UPDATED_SCHEMA_METADATA` (value: `"UPDATED_SCHEMA_METADATA"`)

* `REFRESH_SCHEMA_METADATA_FAILED` (value: `"REFRESH_SCHEMA_METADATA_FAILED"`)

* `REFRESHING_FULL_SCHEMA` (value: `"REFRESHING_FULL_SCHEMA"`)

* `UPDATED_FULL_SCHEMA` (value: `"UPDATED_FULL_SCHEMA"`)





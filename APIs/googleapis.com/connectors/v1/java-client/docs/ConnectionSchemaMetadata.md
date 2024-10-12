

# ConnectionSchemaMetadata

ConnectionSchemaMetadata is the singleton resource of each connection. It includes the entity and action names of runtime resources exposed by a connection backend.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | **List&lt;String&gt;** | Output only. List of actions. |  [optional] [readonly] |
|**entities** | **List&lt;String&gt;** | Output only. List of entity names. |  [optional] [readonly] |
|**errorMessage** | **String** | Error message for users. |  [optional] |
|**name** | **String** | Output only. Resource name. Format: projects/{project}/locations/{location}/connections/{connection}/connectionSchemaMetadata |  [optional] [readonly] |
|**refreshTime** | **String** | Output only. Timestamp when the connection runtime schema refresh was triggered. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of runtime schema. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when the connection runtime schema was updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| REFRESHING | &quot;REFRESHING&quot; |
| UPDATED | &quot;UPDATED&quot; |
| REFRESHING_SCHEMA_METADATA | &quot;REFRESHING_SCHEMA_METADATA&quot; |
| UPDATED_SCHEMA_METADATA | &quot;UPDATED_SCHEMA_METADATA&quot; |
| REFRESH_SCHEMA_METADATA_FAILED | &quot;REFRESH_SCHEMA_METADATA_FAILED&quot; |
| REFRESHING_FULL_SCHEMA | &quot;REFRESHING_FULL_SCHEMA&quot; |
| UPDATED_FULL_SCHEMA | &quot;UPDATED_FULL_SCHEMA&quot; |




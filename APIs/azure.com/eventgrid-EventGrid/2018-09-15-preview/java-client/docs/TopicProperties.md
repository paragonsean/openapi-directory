

# TopicProperties

Properties of the Topic

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | **String** | Endpoint for the topic. |  [optional] [readonly] |
|**inputSchema** | [**InputSchemaEnum**](#InputSchemaEnum) | This determines the format that Event Grid should expect for incoming events published to the topic. |  [optional] |
|**inputSchemaMapping** | [**InputSchemaMapping**](InputSchemaMapping.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the topic. |  [optional] [readonly] |



## Enum: InputSchemaEnum

| Name | Value |
|---- | -----|
| EVENT_GRID_SCHEMA | &quot;EventGridSchema&quot; |
| CUSTOM_EVENT_SCHEMA | &quot;CustomEventSchema&quot; |
| CLOUD_EVENT_V01_SCHEMA | &quot;CloudEventV01Schema&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELED | &quot;Canceled&quot; |
| FAILED | &quot;Failed&quot; |






# DomainProperties

Properties of the Domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowTrafficFromAllIPs** | **Boolean** | This determines if IP filtering rules ought to be evaluated or not. By default it will not evaluate and will allow traffic from all IPs. |  [optional] |
|**endpoint** | **String** | Endpoint for the domain. |  [optional] [readonly] |
|**inboundIpRules** | [**List&lt;InboundIpRule&gt;**](InboundIpRule.md) | This determines the IP filtering rules that ought be applied when events are received on this domain. |  [optional] |
|**inputSchema** | [**InputSchemaEnum**](#InputSchemaEnum) | This determines the format that Event Grid should expect for incoming events published to the domain. |  [optional] |
|**inputSchemaMapping** | [**InputSchemaMapping**](InputSchemaMapping.md) |  |  [optional] |
|**metricResourceId** | **String** | Metric resource id for the domain. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the domain. |  [optional] [readonly] |



## Enum: InputSchemaEnum

| Name | Value |
|---- | -----|
| EVENT_GRID_SCHEMA | &quot;EventGridSchema&quot; |
| CUSTOM_EVENT_SCHEMA | &quot;CustomEventSchema&quot; |
| CLOUD_EVENT_SCHEMA_V1_0 | &quot;CloudEventSchemaV1_0&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELED | &quot;Canceled&quot; |
| FAILED | &quot;Failed&quot; |




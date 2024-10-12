

# GoogleCloudDialogflowCxV3ValidationMessage

Agent/flow validation message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | The message detail. |  [optional] |
|**resourceNames** | [**List&lt;GoogleCloudDialogflowCxV3ResourceName&gt;**](GoogleCloudDialogflowCxV3ResourceName.md) | The resource names of the resources where the message is found. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | The type of the resources where the message is found. |  [optional] |
|**resources** | **List&lt;String&gt;** | The names of the resources where the message is found. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Indicates the severity of the message. |  [optional] |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| RESOURCE_TYPE_UNSPECIFIED | &quot;RESOURCE_TYPE_UNSPECIFIED&quot; |
| AGENT | &quot;AGENT&quot; |
| INTENT | &quot;INTENT&quot; |
| INTENT_TRAINING_PHRASE | &quot;INTENT_TRAINING_PHRASE&quot; |
| INTENT_PARAMETER | &quot;INTENT_PARAMETER&quot; |
| INTENTS | &quot;INTENTS&quot; |
| INTENT_TRAINING_PHRASES | &quot;INTENT_TRAINING_PHRASES&quot; |
| ENTITY_TYPE | &quot;ENTITY_TYPE&quot; |
| ENTITY_TYPES | &quot;ENTITY_TYPES&quot; |
| WEBHOOK | &quot;WEBHOOK&quot; |
| FLOW | &quot;FLOW&quot; |
| PAGE | &quot;PAGE&quot; |
| PAGES | &quot;PAGES&quot; |
| TRANSITION_ROUTE_GROUP | &quot;TRANSITION_ROUTE_GROUP&quot; |
| AGENT_TRANSITION_ROUTE_GROUP | &quot;AGENT_TRANSITION_ROUTE_GROUP&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| INFO | &quot;INFO&quot; |
| WARNING | &quot;WARNING&quot; |
| ERROR | &quot;ERROR&quot; |




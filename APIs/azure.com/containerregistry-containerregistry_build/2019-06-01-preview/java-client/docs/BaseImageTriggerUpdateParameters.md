

# BaseImageTriggerUpdateParameters

The properties for updating base image dependency trigger.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseImageTriggerType** | [**BaseImageTriggerTypeEnum**](#BaseImageTriggerTypeEnum) | The type of the auto trigger for base image dependency updates. |  [optional] |
|**name** | **String** | The name of the trigger. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of trigger. |  [optional] |
|**updateTriggerEndpoint** | **String** | The endpoint URL for receiving update triggers. |  [optional] |
|**updateTriggerPayloadType** | [**UpdateTriggerPayloadTypeEnum**](#UpdateTriggerPayloadTypeEnum) | Type of Payload body for Base image update triggers. |  [optional] |



## Enum: BaseImageTriggerTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;All&quot; |
| RUNTIME | &quot;Runtime&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



## Enum: UpdateTriggerPayloadTypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| TOKEN | &quot;Token&quot; |




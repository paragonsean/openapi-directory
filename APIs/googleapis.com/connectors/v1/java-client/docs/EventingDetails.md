

# EventingDetails

Eventing Details message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customEventTypes** | **Boolean** | Output only. Custom Event Types. |  [optional] [readonly] |
|**description** | **String** | Output only. Description. |  [optional] [readonly] |
|**documentationLink** | **String** | Output only. Link to public documentation. |  [optional] [readonly] |
|**iconLocation** | **String** | Output only. Cloud storage location of the icon. |  [optional] [readonly] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | Output only. Eventing Launch Stage. |  [optional] [readonly] |
|**name** | **String** | Output only. Name of the Eventing trigger. |  [optional] [readonly] |
|**searchTags** | **List&lt;String&gt;** | Output only. Array of search keywords. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of the event listener for a specific connector. |  [optional] [readonly] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| PREVIEW | &quot;PREVIEW&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| PRIVATE_PREVIEW | &quot;PRIVATE_PREVIEW&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| WEBHOOK | &quot;WEBHOOK&quot; |
| JMS | &quot;JMS&quot; |




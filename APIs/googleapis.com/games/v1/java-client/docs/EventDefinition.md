

# EventDefinition

An event definition resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childEvents** | [**List&lt;EventChild&gt;**](EventChild.md) | A list of events that are a child of this event. |  [optional] |
|**description** | **String** | Description of what this event represents. |  [optional] |
|**displayName** | **String** | The name to display for the event. |  [optional] |
|**id** | **String** | The ID of the event. |  [optional] |
|**imageUrl** | **String** | The base URL for the image that represents the event. |  [optional] |
|**isDefaultImageUrl** | **Boolean** | Indicates whether the icon image being returned is a default image, or is game-provided. |  [optional] |
|**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#eventDefinition&#x60;. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | The visibility of event being tracked in this definition. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| REVEALED | &quot;REVEALED&quot; |
| HIDDEN | &quot;HIDDEN&quot; |




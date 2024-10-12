

# GoogleAdsSearchads360V0ResourcesLabel

A label.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Output only. ID of the label. Read only. |  [optional] [readonly] |
|**name** | **String** | The name of the label. This field is required and should not be empty when creating a new label. The length of this string should be between 1 and 80, inclusive. |  [optional] |
|**resourceName** | **String** | Immutable. Name of the resource. Label resource names have the form: &#x60;customers/{customer_id}/labels/{label_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. Status of the label. Read only. |  [optional] [readonly] |
|**textLabel** | [**GoogleAdsSearchads360V0CommonTextLabel**](GoogleAdsSearchads360V0CommonTextLabel.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |




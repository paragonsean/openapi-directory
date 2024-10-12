

# GoogleCloudDialogflowCxV3WebhookResponseFulfillmentResponse

Represents a fulfillment response to the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mergeBehavior** | [**MergeBehaviorEnum**](#MergeBehaviorEnum) | Merge behavior for &#x60;messages&#x60;. |  [optional] |
|**messages** | [**List&lt;GoogleCloudDialogflowCxV3ResponseMessage&gt;**](GoogleCloudDialogflowCxV3ResponseMessage.md) | The list of rich message responses to present to the user. |  [optional] |



## Enum: MergeBehaviorEnum

| Name | Value |
|---- | -----|
| MERGE_BEHAVIOR_UNSPECIFIED | &quot;MERGE_BEHAVIOR_UNSPECIFIED&quot; |
| APPEND | &quot;APPEND&quot; |
| REPLACE | &quot;REPLACE&quot; |




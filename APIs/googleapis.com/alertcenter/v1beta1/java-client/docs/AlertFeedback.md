

# AlertFeedback

A customer feedback about an alert.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertId** | **String** | Output only. The alert identifier. |  [optional] |
|**createTime** | **String** | Output only. The time this feedback was created. |  [optional] |
|**customerId** | **String** | Output only. The unique identifier of the Google Workspace account of the customer. |  [optional] |
|**email** | **String** | Output only. The email of the user that provided the feedback. |  [optional] |
|**feedbackId** | **String** | Output only. The unique identifier for the feedback. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the feedback. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ALERT_FEEDBACK_TYPE_UNSPECIFIED | &quot;ALERT_FEEDBACK_TYPE_UNSPECIFIED&quot; |
| NOT_USEFUL | &quot;NOT_USEFUL&quot; |
| SOMEWHAT_USEFUL | &quot;SOMEWHAT_USEFUL&quot; |
| VERY_USEFUL | &quot;VERY_USEFUL&quot; |




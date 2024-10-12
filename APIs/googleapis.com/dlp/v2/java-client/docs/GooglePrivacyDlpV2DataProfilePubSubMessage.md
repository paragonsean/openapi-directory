

# GooglePrivacyDlpV2DataProfilePubSubMessage

Pub/Sub topic message for a DataProfileAction.PubSubNotification event. To receive a message of protocol buffer schema type, convert the message data to an object of this proto class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**event** | [**EventEnum**](#EventEnum) | The event that caused the Pub/Sub message to be sent. |  [optional] |
|**profile** | [**GooglePrivacyDlpV2TableDataProfile**](GooglePrivacyDlpV2TableDataProfile.md) |  |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| NEW_PROFILE | &quot;NEW_PROFILE&quot; |
| CHANGED_PROFILE | &quot;CHANGED_PROFILE&quot; |
| SCORE_INCREASED | &quot;SCORE_INCREASED&quot; |
| ERROR_CHANGED | &quot;ERROR_CHANGED&quot; |




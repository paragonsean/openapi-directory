

# GooglePrivacyDlpV2PubSubNotification

Send a Pub/Sub message into the given Pub/Sub topic to connect other systems to data profile generation. The message payload data will be the byte serialization of `DataProfilePubSubMessage`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detailOfMessage** | [**DetailOfMessageEnum**](#DetailOfMessageEnum) | How much data to include in the Pub/Sub message. If the user wishes to limit the size of the message, they can use resource_name and fetch the profile fields they wish to. Per table profile (not per column). |  [optional] |
|**event** | [**EventEnum**](#EventEnum) | The type of event that triggers a Pub/Sub. At most one &#x60;PubSubNotification&#x60; per EventType is permitted. |  [optional] |
|**pubsubCondition** | [**GooglePrivacyDlpV2DataProfilePubSubCondition**](GooglePrivacyDlpV2DataProfilePubSubCondition.md) |  |  [optional] |
|**topic** | **String** | Cloud Pub/Sub topic to send notifications to. Format is projects/{project}/topics/{topic}. |  [optional] |



## Enum: DetailOfMessageEnum

| Name | Value |
|---- | -----|
| DETAIL_LEVEL_UNSPECIFIED | &quot;DETAIL_LEVEL_UNSPECIFIED&quot; |
| TABLE_PROFILE | &quot;TABLE_PROFILE&quot; |
| RESOURCE_NAME | &quot;RESOURCE_NAME&quot; |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| NEW_PROFILE | &quot;NEW_PROFILE&quot; |
| CHANGED_PROFILE | &quot;CHANGED_PROFILE&quot; |
| SCORE_INCREASED | &quot;SCORE_INCREASED&quot; |
| ERROR_CHANGED | &quot;ERROR_CHANGED&quot; |




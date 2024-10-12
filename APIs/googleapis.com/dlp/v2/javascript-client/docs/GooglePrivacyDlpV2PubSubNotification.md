# SensitiveDataProtectionDlp.GooglePrivacyDlpV2PubSubNotification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailOfMessage** | **String** | How much data to include in the Pub/Sub message. If the user wishes to limit the size of the message, they can use resource_name and fetch the profile fields they wish to. Per table profile (not per column). | [optional] 
**event** | **String** | The type of event that triggers a Pub/Sub. At most one &#x60;PubSubNotification&#x60; per EventType is permitted. | [optional] 
**pubsubCondition** | [**GooglePrivacyDlpV2DataProfilePubSubCondition**](GooglePrivacyDlpV2DataProfilePubSubCondition.md) |  | [optional] 
**topic** | **String** | Cloud Pub/Sub topic to send notifications to. Format is projects/{project}/topics/{topic}. | [optional] 



## Enum: DetailOfMessageEnum


* `DETAIL_LEVEL_UNSPECIFIED` (value: `"DETAIL_LEVEL_UNSPECIFIED"`)

* `TABLE_PROFILE` (value: `"TABLE_PROFILE"`)

* `RESOURCE_NAME` (value: `"RESOURCE_NAME"`)





## Enum: EventEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `NEW_PROFILE` (value: `"NEW_PROFILE"`)

* `CHANGED_PROFILE` (value: `"CHANGED_PROFILE"`)

* `SCORE_INCREASED` (value: `"SCORE_INCREASED"`)

* `ERROR_CHANGED` (value: `"ERROR_CHANGED"`)





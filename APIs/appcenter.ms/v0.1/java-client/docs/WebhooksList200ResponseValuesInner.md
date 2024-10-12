

# WebhooksList200ResponseValuesInner

Alerting webhook

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Allows eanble/disable webhook |  [optional] |
|**eventTypes** | [**List&lt;EventTypesEnum&gt;**](#List&lt;EventTypesEnum&gt;) | Event types enabled for webhook |  |
|**id** | **String** | The unique id (UUID) of the webhook |  [optional] |
|**name** | **String** | display name of the webhook |  |
|**url** | **String** | target url of the webhook |  |



## Enum: List&lt;EventTypesEnum&gt;

| Name | Value |
|---- | -----|
| NEW_CRASH_GROUP_CREATED | &quot;newCrashGroupCreated&quot; |
| NEW_APP_RELEASED | &quot;newAppReleased&quot; |




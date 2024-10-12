

# GoogleDevtoolsRemotebuildexecutionAdminV1alphaSchedulerNotificationConfig

Defines configurations for an instance's scheduler notifications, where a target Pub/Sub topic will be notified whenever a task (e.g. an action or reservation) completes on this instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topic** | **String** | The Pub/Sub topic resource name to issue notifications to. Note that the topic does not need to be owned by the same project as this instance. Format: &#x60;projects//topics/&#x60;. |  [optional] |






# ScheduledAction

Information about a scheduled configuration change for an OpenSearch Service domain. This actions can be a <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\">service software update</a> or a <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types\">blue/green Auto-Tune enhancement</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  |
|**type** | [**ActionType**](ActionType.md) |  |  |
|**severity** | [**ActionSeverity**](ActionSeverity.md) |  |  |
|**scheduledTime** | [**Integer**](Integer.md) |  |  |
|**description** | [**String**](String.md) |  |  [optional] |
|**scheduledBy** | [**ScheduledBy**](ScheduledBy.md) |  |  [optional] |
|**status** | [**ActionStatus**](ActionStatus.md) |  |  [optional] |
|**mandatory** | [**Boolean**](Boolean.md) |  |  [optional] |
|**cancellable** | [**Boolean**](Boolean.md) |  |  [optional] |




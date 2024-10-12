

# AlertingAction

Specify action need to be taken when rule type is Alert

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aznsAction** | [**AzNsActionGroup**](AzNsActionGroup.md) |  |  [optional] |
|**severity** | **AlertSeverity** |  |  |
|**throttlingInMin** | **Integer** | time (in minutes) for which Alerts should be throttled or suppressed. |  [optional] |
|**trigger** | [**TriggerCondition**](TriggerCondition.md) |  |  |




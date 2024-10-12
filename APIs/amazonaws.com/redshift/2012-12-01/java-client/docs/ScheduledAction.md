

# ScheduledAction

Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift API operations on a schedule. For information about which API operations can be scheduled, see <a>ScheduledActionType</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scheduledActionName** | [**String**](String.md) |  |  [optional] |
|**targetAction** | [**ScheduledActionTargetAction**](ScheduledActionTargetAction.md) |  |  [optional] |
|**schedule** | [**String**](String.md) |  |  [optional] |
|**iamRole** | [**String**](String.md) |  |  [optional] |
|**scheduledActionDescription** | [**String**](String.md) |  |  [optional] |
|**state** | [**ScheduledActionState**](ScheduledActionState.md) |  |  [optional] |
|**nextInvocations** | [**List**](List.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |




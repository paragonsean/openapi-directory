

# LifecycleHook

Describes a lifecycle hook. A lifecycle hook lets you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lifecycleHookName** | [**String**](String.md) |  |  [optional] |
|**autoScalingGroupName** | [**String**](String.md) |  |  [optional] |
|**lifecycleTransition** | [**String**](String.md) |  |  [optional] |
|**notificationTargetARN** | [**String**](String.md) |  |  [optional] |
|**roleARN** | [**String**](String.md) |  |  [optional] |
|**notificationMetadata** | [**String**](String.md) |  |  [optional] |
|**heartbeatTimeout** | [**Integer**](Integer.md) |  |  [optional] |
|**globalTimeout** | [**Integer**](Integer.md) |  |  [optional] |
|**defaultResult** | [**String**](String.md) |  |  [optional] |




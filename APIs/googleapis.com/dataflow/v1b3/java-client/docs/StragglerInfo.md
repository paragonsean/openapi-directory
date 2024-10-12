

# StragglerInfo

Information useful for straggler identification and debugging.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**causes** | [**Map&lt;String, StragglerDebuggingInfo&gt;**](StragglerDebuggingInfo.md) | The straggler causes, keyed by the string representation of the StragglerCause enum and contains specialized debugging information for each straggler cause. |  [optional] |
|**startTime** | **String** | The time when the work item attempt became a straggler. |  [optional] |




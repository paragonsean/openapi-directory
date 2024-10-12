

# EventProperties

The properties of a monitoring event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affectedObjectCorrelationId** | **String** | The affected object correlationId for the event. |  [optional] [readonly] |
|**affectedObjectFriendlyName** | **String** | The friendly name of the source of the event on which it is raised (for example, VM, VMM etc). |  [optional] |
|**description** | **String** | The event name. |  [optional] |
|**eventCode** | **String** | The Id of the monitoring event. |  [optional] |
|**eventSpecificDetails** | [**EventSpecificDetails**](EventSpecificDetails.md) |  |  [optional] |
|**eventType** | **String** | The type of the event. for example: VM Health, Server Health, Job Failure etc. |  [optional] |
|**fabricId** | **String** | The ARM ID of the fabric. |  [optional] |
|**healthErrors** | [**List&lt;HealthError&gt;**](HealthError.md) | The list of errors / warnings capturing details associated with the issue(s). |  [optional] |
|**providerSpecificDetails** | [**EventProviderSpecificDetails**](EventProviderSpecificDetails.md) |  |  [optional] |
|**severity** | **String** | The severity of the event. |  [optional] |
|**timeOfOccurrence** | **OffsetDateTime** | The time of occurrence of the event. |  [optional] |




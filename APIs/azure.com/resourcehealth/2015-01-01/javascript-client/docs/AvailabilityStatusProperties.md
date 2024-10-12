# MicrosoftResourceHealth.AvailabilityStatusProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityState** | **String** | Availability status of the resource. | [optional] 
**detailedStatus** | **String** | Details of the availability status. | [optional] 
**isArmResource** | **Boolean** | flag to show if child resource need detail health.  | [optional] 
**occuredTime** | **Date** | Timestamp for when last change in health status occurred. | [optional] 
**reasonChronicity** | **String** | Chronicity of the availability transition. | [optional] 
**reasonType** | **String** | When the resource&#39;s availabilityState is Unavailable, it describes where the health impacting event was originated. Examples are planned, unplanned, user initiated or an outage etc. | [optional] 
**recentlyResolvedState** | [**AvailabilityStatusPropertiesRecentlyResolvedState**](AvailabilityStatusPropertiesRecentlyResolvedState.md) |  | [optional] 
**recommendedActions** | [**[RecommendedAction]**](RecommendedAction.md) | Lists actions the user can take based on the current availabilityState of the resource. | [optional] 
**reportedTime** | **Date** | Timestamp for when the health was last checked.  | [optional] 
**resolutionETA** | **Date** | When the resource&#39;s availabilityState is Unavailable and the reasonType is not User Initiated, it provides the date and time for when the issue is expected to be resolved. | [optional] 
**rootCauseAttributionTime** | **Date** | When the resource&#39;s availabilityState is Unavailable, it provides the Timestamp for when the health impacting event was received. | [optional] 
**serviceImpactingEvents** | [**[ServiceImpactingEvent]**](ServiceImpactingEvent.md) | Lists the service impacting events that may be affecting the health of the resource. | [optional] 
**summary** | **String** | Summary description of the availability state. | [optional] 



## Enum: AvailabilityStateEnum


* `Available` (value: `"Available"`)

* `Unavailable` (value: `"Unavailable"`)

* `Unknown` (value: `"Unknown"`)





## Enum: ReasonChronicityEnum


* `Transient` (value: `"Transient"`)

* `Persistent` (value: `"Persistent"`)





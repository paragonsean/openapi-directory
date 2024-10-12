# MicrosoftResourceHealth.AvailabilityStatusProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityState** | **String** | Availability status of the resource. When it is null, this availabilityStatus object represents an availability impacting event | [optional] 
**detailedStatus** | **String** | Details of the availability status. | [optional] 
**healthEventCategory** | **String** | In case of an availability impacting event, it describes the category of a PlatformInitiated health impacting event. Examples are Planned, Unplanned etc. | [optional] 
**healthEventCause** | **String** | In case of an availability impacting event, it describes where the health impacting event was originated. Examples are PlatformInitiated, UserInitiated etc. | [optional] 
**healthEventId** | **String** | It is a unique Id that identifies the event | [optional] 
**healthEventType** | **String** | In case of an availability impacting event, it describes when the health impacting event was originated. Examples are Lifecycle, Downtime, Fault Analysis etc. | [optional] 
**occuredTime** | **Date** | Timestamp for when last change in health status occurred. | [optional] 
**reasonChronicity** | **String** | Chronicity of the availability transition. | [optional] 
**reasonType** | **String** | When the resource&#39;s availabilityState is Unavailable, it describes where the health impacting event was originated. Examples are planned, unplanned, user initiated or an outage etc. | [optional] 
**recentlyResolved** | [**AvailabilityStatusPropertiesRecentlyResolved**](AvailabilityStatusPropertiesRecentlyResolved.md) |  | [optional] 
**recommendedActions** | [**[RecommendedAction]**](RecommendedAction.md) | Lists actions the user can take based on the current availabilityState of the resource. | [optional] 
**reportedTime** | **Date** | Timestamp for when the health was last checked.  | [optional] 
**resolutionETA** | **Date** | When the resource&#39;s availabilityState is Unavailable and the reasonType is not User Initiated, it provides the date and time for when the issue is expected to be resolved. | [optional] 
**rootCauseAttributionTime** | **Date** | When the resource&#39;s availabilityState is Unavailable, it provides the Timestamp for when the health impacting event was received. | [optional] 
**serviceImpactingEvents** | [**[ServiceImpactingEvent]**](ServiceImpactingEvent.md) | Lists the service impacting events that may be affecting the health of the resource. | [optional] 
**summary** | **String** | Summary description of the availability status. | [optional] 



## Enum: AvailabilityStateEnum


* `Available` (value: `"Available"`)

* `Unavailable` (value: `"Unavailable"`)

* `Degraded` (value: `"Degraded"`)

* `Unknown` (value: `"Unknown"`)





## Enum: ReasonChronicityEnum


* `Transient` (value: `"Transient"`)

* `Persistent` (value: `"Persistent"`)







# AvailabilityStatusProperties

Properties of availability state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityState** | [**AvailabilityStateEnum**](#AvailabilityStateEnum) | Availability status of the resource. |  [optional] |
|**detailedStatus** | **String** | Details of the availability status. |  [optional] |
|**isArmResource** | **Boolean** | flag to show if child resource need detail health.  |  [optional] |
|**occuredTime** | **OffsetDateTime** | Timestamp for when last change in health status occurred. |  [optional] |
|**reasonChronicity** | [**ReasonChronicityEnum**](#ReasonChronicityEnum) | Chronicity of the availability transition. |  [optional] |
|**reasonType** | **String** | When the resource&#39;s availabilityState is Unavailable, it describes where the health impacting event was originated. Examples are planned, unplanned, user initiated or an outage etc. |  [optional] |
|**recentlyResolvedState** | [**AvailabilityStatusPropertiesRecentlyResolvedState**](AvailabilityStatusPropertiesRecentlyResolvedState.md) |  |  [optional] |
|**recommendedActions** | [**List&lt;RecommendedAction&gt;**](RecommendedAction.md) | Lists actions the user can take based on the current availabilityState of the resource. |  [optional] |
|**reportedTime** | **OffsetDateTime** | Timestamp for when the health was last checked.  |  [optional] |
|**resolutionETA** | **OffsetDateTime** | When the resource&#39;s availabilityState is Unavailable and the reasonType is not User Initiated, it provides the date and time for when the issue is expected to be resolved. |  [optional] |
|**rootCauseAttributionTime** | **OffsetDateTime** | When the resource&#39;s availabilityState is Unavailable, it provides the Timestamp for when the health impacting event was received. |  [optional] |
|**serviceImpactingEvents** | [**List&lt;ServiceImpactingEvent&gt;**](ServiceImpactingEvent.md) | Lists the service impacting events that may be affecting the health of the resource. |  [optional] |
|**summary** | **String** | Summary description of the availability state. |  [optional] |



## Enum: AvailabilityStateEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;Available&quot; |
| UNAVAILABLE | &quot;Unavailable&quot; |
| UNKNOWN | &quot;Unknown&quot; |



## Enum: ReasonChronicityEnum

| Name | Value |
|---- | -----|
| TRANSIENT | &quot;Transient&quot; |
| PERSISTENT | &quot;Persistent&quot; |




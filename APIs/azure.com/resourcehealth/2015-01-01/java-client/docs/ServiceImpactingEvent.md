

# ServiceImpactingEvent

Lists the service impacting events that may be affecting the health of the resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correlationId** | **String** | Correlation id for the event |  [optional] |
|**eventStartTime** | **OffsetDateTime** | Timestamp for when the event started. |  [optional] |
|**eventStatusLastModifiedTime** | **OffsetDateTime** | Timestamp for when event was submitted/detected. |  [optional] |
|**incidentProperties** | [**ServiceImpactingEventIncidentProperties**](ServiceImpactingEventIncidentProperties.md) |  |  [optional] |
|**status** | [**ServiceImpactingEventStatus**](ServiceImpactingEventStatus.md) |  |  [optional] |




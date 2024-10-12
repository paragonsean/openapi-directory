

# FlightSegment

defining a flight segment; including both operating and marketing details when applicable

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aircraft** | [**AircraftEquipment**](AircraftEquipment.md) |  |  [optional] |
|**arrival** | [**FlightEndPoint**](FlightEndPoint.md) |  |  [optional] |
|**bookingStatus** | [**BookingStatusEnum**](#BookingStatusEnum) | booking status of the segment |  [optional] |
|**carrierCode** | **String** | providing the airline / carrier code |  [optional] |
|**departure** | [**FlightEndPoint**](FlightEndPoint.md) |  |  [optional] |
|**duration** | **String** | stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M |  [optional] |
|**isFlown** | **Boolean** | indicator set to true if segment is flown |  [optional] |
|**number** | **String** | the flight number as assigned by the carrier |  [optional] |
|**operating** | [**OperatingFlight**](OperatingFlight.md) |  |  [optional] |
|**segmentType** | [**SegmentTypeEnum**](#SegmentTypeEnum) | type of the segment |  [optional] |
|**stops** | [**List&lt;FlightStop&gt;**](FlightStop.md) | information regarding the different stops composing the flight segment. E.g. technical stop, change of gauge... |  [optional] |



## Enum: BookingStatusEnum

| Name | Value |
|---- | -----|
| CONFIRMED | &quot;CONFIRMED&quot; |
| WAITLISTED | &quot;WAITLISTED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| PENDING | &quot;PENDING&quot; |
| DENIED | &quot;DENIED&quot; |



## Enum: SegmentTypeEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PASSIVE | &quot;PASSIVE&quot; |
| GHOST | &quot;GHOST&quot; |
| STAFF | &quot;STAFF&quot; |




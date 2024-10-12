# FlightOrderManagement.FlightSegment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aircraft** | [**AircraftEquipment**](AircraftEquipment.md) |  | [optional] 
**arrival** | [**FlightEndPoint**](FlightEndPoint.md) |  | [optional] 
**bookingStatus** | **String** | booking status of the segment | [optional] 
**carrierCode** | **String** | providing the airline / carrier code | [optional] 
**departure** | [**FlightEndPoint**](FlightEndPoint.md) |  | [optional] 
**duration** | **String** | stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M | [optional] 
**isFlown** | **Boolean** | indicator set to true if segment is flown | [optional] 
**number** | **String** | the flight number as assigned by the carrier | [optional] 
**operating** | [**OperatingFlight**](OperatingFlight.md) |  | [optional] 
**segmentType** | **String** | type of the segment | [optional] 
**stops** | [**[FlightStop]**](FlightStop.md) | information regarding the different stops composing the flight segment. E.g. technical stop, change of gauge... | [optional] 



## Enum: BookingStatusEnum


* `CONFIRMED` (value: `"CONFIRMED"`)

* `WAITLISTED` (value: `"WAITLISTED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `PENDING` (value: `"PENDING"`)

* `DENIED` (value: `"DENIED"`)





## Enum: SegmentTypeEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `PASSIVE` (value: `"PASSIVE"`)

* `GHOST` (value: `"GHOST"`)

* `STAFF` (value: `"STAFF"`)





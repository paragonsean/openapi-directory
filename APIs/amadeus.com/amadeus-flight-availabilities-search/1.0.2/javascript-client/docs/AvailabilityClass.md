# FlightAvailibilitiesSearch.AvailabilityClass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **String** | The code of the booking class, a.k.a. class of service or Reservations/Booking Designator (RBD) | [optional] 
**closedStatus** | **String** | Status of the booking class when it is closed. | [optional] 
**numberOfBookableSeats** | **Number** | Number of seats bookable in a single request. Can not be higher than 9. | [optional] 
**tourAllotment** | [**TourAllotment**](TourAllotment.md) |  | [optional] 



## Enum: ClosedStatusEnum


* `WAITLIST_OPEN` (value: `"WAITLIST_OPEN"`)

* `WAITLIST_CLOSED` (value: `"WAITLIST_CLOSED"`)

* `ON_REQUEST` (value: `"ON_REQUEST"`)





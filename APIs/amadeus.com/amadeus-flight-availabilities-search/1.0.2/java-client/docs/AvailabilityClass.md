

# AvailabilityClass


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**propertyClass** | **String** | The code of the booking class, a.k.a. class of service or Reservations/Booking Designator (RBD) |  [optional] |
|**closedStatus** | [**ClosedStatusEnum**](#ClosedStatusEnum) | Status of the booking class when it is closed. |  [optional] |
|**numberOfBookableSeats** | **BigDecimal** | Number of seats bookable in a single request. Can not be higher than 9. |  [optional] |
|**tourAllotment** | [**TourAllotment**](TourAllotment.md) |  |  [optional] |



## Enum: ClosedStatusEnum

| Name | Value |
|---- | -----|
| WAITLIST_OPEN | &quot;WAITLIST_OPEN&quot; |
| WAITLIST_CLOSED | &quot;WAITLIST_CLOSED&quot; |
| ON_REQUEST | &quot;ON_REQUEST&quot; |




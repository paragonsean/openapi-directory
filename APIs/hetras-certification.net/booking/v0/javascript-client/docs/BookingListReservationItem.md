# HetrasBookingApiVersion0.BookingListReservationItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**adults** | **Number** | The number of adults per room | [optional] 
**arrivalDate** | **Date** | The arrival date of the guests | [optional] 
**balance** | **Number** | The balance for all folios of this reservartion. It is calculated by all already charged room and service rates plus manual charges               or charges from other systems like POS minus all payments. A negative balance indicates the reservation is overpaid, a positive balance               that the guest owes the hotel money | [optional] 
**blockCode** | **String** | If this reservation is a pick-up from a block you will see the appropriate block code here | [optional] 
**cancellationId** | **String** | The cancellation id if the reservation has been cancelled | [optional] 
**channelCode** | **String** | The code of the channel that was used when the booking has been created. It is also known as source.               Possible values can be OTA, GDS or DIRECT, but it is configurable per hotel | [optional] 
**companies** | [**CompaniesInfo**](CompaniesInfo.md) |  | [optional] 
**created** | **Date** | Timestamp the reservation was created | [optional] 
**customers** | [**CustomersInfo**](CustomersInfo.md) |  | [optional] 
**departureDate** | **Date** | The departure date of the guests | [optional] 
**externalId** | **String** | The external id for this reservation is the unique identifier from the system that created the booking in hetras. It could be the id of an              OTA like Expedia or booking.com or one of the GDS systems like Amadeus or Galileo | [optional] 
**hotel** | [**HotelInfo**](HotelInfo.md) |  | [optional] 
**labels** | **[String]** | The labels attached to this reservation. | [optional] 
**marketCode** | **String** | The code of the market segment the rate plan for this reservation is linked to | [optional] 
**ratePlan** | [**RatePlan**](RatePlan.md) |  | [optional] 
**reservationNumber** | **Number** | The reservation number of the reservation | [optional] 
**reservationStatus** | **String** | The current status of this reservation | [optional] 
**room** | [**RoomInfo**](RoomInfo.md) |  | [optional] 
**rooms** | **Number** | The number of rooms this reservation is valid for. After a multi-room booking is done there will be               one reservation in hetras for this booking for all rooms. The hotel staff then will split this reservation into              one reservation per room to be able to check in the guests | [optional] 
**subchannelCode** | **String** | The code of the subchannel that was used when the booking has been created. Possible values can be               BOOKING, EXPEDIA or WALKIN, but it is configurable per hotel | [optional] 
**updated** | **Date** | Timestamp of when the reservation was changed the last time | [optional] 



## Enum: ReservationStatusEnum


* `Tentative` (value: `"Tentative"`)

* `Waitlisted` (value: `"Waitlisted"`)

* `OnRequest` (value: `"OnRequest"`)

* `NonGuaranteed` (value: `"NonGuaranteed"`)

* `Guaranteed` (value: `"Guaranteed"`)

* `InHouse` (value: `"InHouse"`)

* `CheckedOut` (value: `"CheckedOut"`)

* `NoShow` (value: `"NoShow"`)

* `Denied` (value: `"Denied"`)

* `Cancelled` (value: `"Cancelled"`)

* `Released` (value: `"Released"`)

* `Walked` (value: `"Walked"`)

* `Expired` (value: `"Expired"`)

* `WalkIn` (value: `"WalkIn"`)

* `Registered` (value: `"Registered"`)





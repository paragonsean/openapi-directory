# HetrasHotelApiVersion0.EmbeddedReservation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**arrivalDate** | **Date** | The arrival date of the guests | 
**confirmationId** | **String** | he confirmation id for the booking which the guest can use to check in on the kiosk, add the               booking to the mobile app etc. It is used as identifier for all reservations done with the               same booking request | 
**departureDate** | **Date** | The departure date of the guests | 
**reservationNumber** | **Number** | The reservation number of the reservation | 
**reservationStatus** | **String** | The current status of this reservation | 



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





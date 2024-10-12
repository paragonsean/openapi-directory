# HetrasBookingApiVersion0.BookingListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**confirmationId** | **String** | The confirmation id for the booking which the guest can use to check in on the kiosk, add the              booking to the mobile app etc. It is used as identifier for all reservations done with the same              booking request. | [optional] 
**created** | **Date** | Timestamp the booking was created | [optional] 
**reservations** | [**[BookingListReservationItem]**](BookingListReservationItem.md) | Collection of reservations made with on booking request. | [optional] 
**updated** | **Date** | Timestamp of when the booking was changed the last time | [optional] 



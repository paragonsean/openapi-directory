

# BookingListItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, LinkObject&gt;**](LinkObject.md) | Collection of links to related resources |  [optional] |
|**confirmationId** | **String** | The confirmation id for the booking which the guest can use to check in on the kiosk, add the              booking to the mobile app etc. It is used as identifier for all reservations done with the same              booking request. |  [optional] |
|**created** | **OffsetDateTime** | Timestamp the booking was created |  [optional] |
|**reservations** | [**List&lt;BookingListReservationItem&gt;**](BookingListReservationItem.md) | Collection of reservations made with on booking request. |  [optional] |
|**updated** | **OffsetDateTime** | Timestamp of when the booking was changed the last time |  [optional] |




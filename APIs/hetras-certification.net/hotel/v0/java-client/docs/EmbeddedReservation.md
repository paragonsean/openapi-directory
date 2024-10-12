

# EmbeddedReservation

Basic data about a reservation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, LinkObject&gt;**](LinkObject.md) | Collection of links to related resources |  [optional] |
|**arrivalDate** | **OffsetDateTime** | The arrival date of the guests |  |
|**confirmationId** | **String** | he confirmation id for the booking which the guest can use to check in on the kiosk, add the               booking to the mobile app etc. It is used as identifier for all reservations done with the               same booking request |  |
|**departureDate** | **OffsetDateTime** | The departure date of the guests |  |
|**reservationNumber** | **Integer** | The reservation number of the reservation |  |
|**reservationStatus** | [**ReservationStatusEnum**](#ReservationStatusEnum) | The current status of this reservation |  |



## Enum: ReservationStatusEnum

| Name | Value |
|---- | -----|
| TENTATIVE | &quot;Tentative&quot; |
| WAITLISTED | &quot;Waitlisted&quot; |
| ON_REQUEST | &quot;OnRequest&quot; |
| NON_GUARANTEED | &quot;NonGuaranteed&quot; |
| GUARANTEED | &quot;Guaranteed&quot; |
| IN_HOUSE | &quot;InHouse&quot; |
| CHECKED_OUT | &quot;CheckedOut&quot; |
| NO_SHOW | &quot;NoShow&quot; |
| DENIED | &quot;Denied&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| RELEASED | &quot;Released&quot; |
| WALKED | &quot;Walked&quot; |
| EXPIRED | &quot;Expired&quot; |
| WALK_IN | &quot;WalkIn&quot; |
| REGISTERED | &quot;Registered&quot; |




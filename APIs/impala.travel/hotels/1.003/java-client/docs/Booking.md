

# Booking

Details of an existing booking.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookedRooms** | [**List&lt;BookedRoom&gt;**](BookedRoom.md) | List of rooms booked |  |
|**bookingId** | **String** | Unique identifier for this booking within the Impala platform. |  |
|**cancellation** | [**BookingCancellation**](BookingCancellation.md) |  |  [optional] |
|**contact** | [**BookingContact**](BookingContact.md) |  |  |
|**createdAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the booking was created. |  |
|**end** | **LocalDate** | The departure date of the booking. |  |
|**hotel** | [**HotelStub**](HotelStub.md) |  |  |
|**hotelConfirmationCode** | **String** | The hotel&#39;s confirmation identifier for this booking. |  [optional] |
|**notes** | [**BookingNotes**](BookingNotes.md) |  |  |
|**paymentBearerToken** | **String** | If status is PAYMENT_REQUIRED, then this should be used as the Authorisation header for the POST to the /payments endpoint. |  [optional] |
|**paymentClientSecret** | **String** | If status is PAYMENT_REQUIRED, then this should be used as the client secret when rendering Impala Payment Elements in the UI. |  [optional] |
|**start** | **LocalDate** | The arrival date of the booking. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of this booking within the Impala platform. When you make a booking, it&#39;ll first appear as &#x60;PENDING&#x60; until we receive the hotel&#39;s confirmation details. At this point your booking will move to &#x60;ACCEPTED&#x60;. |  |
|**updatedAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the booking was last updated. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CANCELLED | &quot;CANCELLED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| PAYMENT_REQUIRED | &quot;PAYMENT_REQUIRED&quot; |
| PAYMENT_ABANDONED | &quot;PAYMENT_ABANDONED&quot; |




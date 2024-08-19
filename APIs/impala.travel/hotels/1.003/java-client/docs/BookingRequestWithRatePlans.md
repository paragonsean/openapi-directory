

# BookingRequestWithRatePlans

Request body with the explicit rate taken from the rate calendar endpoint

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookingContact** | [**BookingContact**](BookingContact.md) |  |  |
|**dealId** | **String** | The id of the deal that contains agreement made between the hotel and company |  [optional] |
|**end** | **LocalDate** | The last day of the desired stay range in ISO 8601 format YYYY-MM-DD. |  |
|**notes** | [**NotesBooking**](NotesBooking.md) |  |  [optional] |
|**paymentType** | [**PaymentTypeEnum**](#PaymentTypeEnum) | How will the guest make payment for this booking? |  [optional] |
|**rooms** | [**List&lt;RatePlanRoom&gt;**](RatePlanRoom.md) | Array of rooms booked within this booking |  |
|**start** | **LocalDate** | The first day of the desired stay range in ISO 8601 format YYYY-MM-DD. |  |



## Enum: PaymentTypeEnum

| Name | Value |
|---- | -----|
| API | &quot;API&quot; |




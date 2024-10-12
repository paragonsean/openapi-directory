# ImpalaHotelBookingApi.BookingRequestWithRatePlans

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookingContact** | [**BookingContact**](BookingContact.md) |  | 
**dealId** | **String** | The id of the deal that contains agreement made between the hotel and company | [optional] 
**end** | **Date** | The last day of the desired stay range in ISO 8601 format YYYY-MM-DD. | 
**notes** | [**NotesBooking**](NotesBooking.md) |  | [optional] 
**paymentType** | **String** | How will the guest make payment for this booking? | [optional] 
**rooms** | [**[RatePlanRoom]**](RatePlanRoom.md) | Array of rooms booked within this booking | 
**start** | **Date** | The first day of the desired stay range in ISO 8601 format YYYY-MM-DD. | 



## Enum: PaymentTypeEnum


* `API` (value: `"API"`)





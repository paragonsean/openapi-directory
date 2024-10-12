# ImpalaHotelBookingApi.UpdateBookingRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookingContact** | [**PersonInfo**](PersonInfo.md) | Details of your guest (will be provided to the hotel in case of questions). | 
**end** | **Date** | The last day of the desired stay range in ISO 8601 format YYYY-MM-DD. | 
**notes** | [**NotesBooking**](NotesBooking.md) |  | [optional] 
**paymentType** | **String** | How will the guest make payment for this booking? | [optional] 
**rooms** | [**[BookingRequestRoomsInner]**](BookingRequestRoomsInner.md) | List of room type identifiers to be booked. | 
**start** | **Date** | The first day of the desired stay range in ISO 8601 format YYYY-MM-DD. | 
**updateBookingVersionAtTimestamp** | **Date** | The timestamp of when the booking was last updated | 



## Enum: PaymentTypeEnum


* `API` (value: `"API"`)





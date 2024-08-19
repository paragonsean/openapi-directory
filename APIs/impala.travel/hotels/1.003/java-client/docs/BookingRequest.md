

# BookingRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookingContact** | [**PersonInfo**](PersonInfo.md) | Details of your guest (will be provided to the hotel in case of questions). |  |
|**end** | **LocalDate** | The last day of the desired stay range in ISO 8601 format YYYY-MM-DD. |  |
|**notes** | [**NotesBooking**](NotesBooking.md) |  |  [optional] |
|**paymentType** | [**PaymentTypeEnum**](#PaymentTypeEnum) | How will the guest make payment for this booking? |  [optional] |
|**rooms** | [**List&lt;BookingRequestRoomsInner&gt;**](BookingRequestRoomsInner.md) | List of room type identifiers to be booked. |  |
|**start** | **LocalDate** | The first day of the desired stay range in ISO 8601 format YYYY-MM-DD. |  |



## Enum: PaymentTypeEnum

| Name | Value |
|---- | -----|
| API | &quot;API&quot; |




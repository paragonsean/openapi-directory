# HetrasBookingApiVersion0.GetAddonsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **Blob** | Number of adults per room. | 
**arrivalDate** | **Date** | Date from when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | 
**channelCode** | **String** | Channel Code the rate plan needs to be configured for. | 
**departureDate** | **Date** | Date until when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.              This is usually the departure date of the reservation. | 
**expand** | **String** | Expand the rates breakdown if required. | [optional] 
**hotelId** | **Number** | Specifies the hotel id to request offers for. | 
**ratePlanCode** | **String** | Only return offers for the specified rate plan code. | 
**roomType** | **String** | Only return offers for the specified room type code. | 
**rooms** | **Blob** | Number of rooms. | 



## Enum: ExpandEnum


* `None` (value: `"None"`)

* `Breakdown` (value: `"Breakdown"`)





# HetrasBookingApiVersion0.RatesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **Blob** | Number of adults per room. | 
**arrivalDate** | **Date** | Date of arrival for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | 
**channelCode** | **String** | Channel Code the rate plan needs to be configured for. | 
**departureDate** | **Date** | Date of departure for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | 
**expand** | **String** | Expand the rates breakdown if required. | [optional] 
**groupCode** | **String** | Only return offers for the specified group code. | [optional] 
**hotelId** | **Number** | Specifies the hotel id to request offers for. | 
**ratePlanCode** | **String** | Only return offers for the specified room type code. | [optional] 
**roomType** | **String** | Only return offers with rates for the specified room type code. | [optional] 
**rooms** | **Blob** | Number of rooms (default is 1). | [optional] 



## Enum: ExpandEnum


* `None` (value: `"None"`)

* `Breakdown` (value: `"Breakdown"`)





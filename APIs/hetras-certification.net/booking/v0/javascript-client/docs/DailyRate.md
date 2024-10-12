# HetrasBookingApiVersion0.DailyRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addonServices** | [**[ServiceRate]**](ServiceRate.md) | List of addon services with additional price information. | [optional] 
**date** | **Date** | Date the room rate will be charged to the folio | [optional] 
**excludedTax** | **Number** | The amount of extra taxes also calculated for all rooms and all persons per room. | [optional] 
**includedServices** | **[String]** | List of codes for all services already included in the gross rate | [optional] 
**includedTax** | **Number** | The amount of taxes already included in the gross nightly rate also calculated for all rooms and              all persons per room. | [optional] 
**rate** | **Number** | The gross room rate. It is the price calculated for all rooms and all persons per room. | [optional] 
**roomType** | **String** | Code of the room type which is booked for that day | [optional] 



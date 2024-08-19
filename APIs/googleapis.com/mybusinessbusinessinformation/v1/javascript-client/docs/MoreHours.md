# MyBusinessBusinessInformationApi.MoreHours

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hoursTypeId** | **String** | Required. Type of hours. Clients should call {#link businessCategories:BatchGet} to get supported hours types for categories of their locations. | [optional] 
**periods** | [**[TimePeriod]**](TimePeriod.md) | Required. A collection of times that this location is open. Each period represents a range of hours when the location is open during the week. | [optional] 



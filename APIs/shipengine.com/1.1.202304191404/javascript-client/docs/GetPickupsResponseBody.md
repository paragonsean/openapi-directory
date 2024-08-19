# ShipEngineApi.GetPickupsResponseBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLink**](PaginationLink.md) | Helpful links to other pages of results | [readonly] 
**page** | **Number** | Current page of the list pickups results | [readonly] 
**pages** | **Number** | Total number of pages for list pickups results | [readonly] 
**pickups** | [**[Pickup]**](Pickup.md) | An array of pickups associated with the user&#39;s account. | 
**total** | **Number** | The total number of pickups returned | [readonly] 
**errors** | [**[Error]**](Error.md) | The errors associated with the failed API call | [readonly] 
**requestId** | **String** | A UUID that uniquely identifies the request id. This can be given to the support team to help debug non-trivial issues that may occur  | 



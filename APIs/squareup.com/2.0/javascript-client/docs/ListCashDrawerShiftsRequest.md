# SquareConnectApi.ListCashDrawerShiftsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beginTime** | **String** | The inclusive start time of the query on opened_at, in ISO 8601 format. | [optional] 
**cursor** | **String** | Opaque cursor for fetching the next page of results. | [optional] 
**endTime** | **String** | The exclusive end date of the query on opened_at, in ISO 8601 format. | [optional] 
**limit** | **Number** | Number of cash drawer shift events in a page of results (200 by default, 1000 max). | [optional] 
**locationId** | **String** | The ID of the location to query for a list of cash drawer shifts. | 
**sortOrder** | **String** | The order in which cash drawer shifts are listed in the response, based on their opened_at field. Default value: ASC | [optional] 



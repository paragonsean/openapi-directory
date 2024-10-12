# HetrasBookingApiVersion0.BlockListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countDetails** | **Boolean** | If true it will include also details of block count per each room type. | [optional] 
**from** | **Date** | Return all blocks where the block&#39;s last_departure is greater than specified date. | [optional] 
**groupCode** | **String** | Filter the blocks by the specified group code | [optional] 
**hotelId** | **Number** | Only return blocks for this specific hotel. | [optional] 
**ratePlanCodes** | **[String]** | Return all blocks that have related the specified comma-separated rate plans. | [optional] 
**status** | **String** | Return all blocks where the block status is one of the specified values. | [optional] 
**to** | **Date** | Return all blocks where the block&#39;s last_departure is less than specified date. | [optional] 



## Enum: StatusEnum


* `Cancelled` (value: `"Cancelled"`)

* `Tentative` (value: `"Tentative"`)

* `Definite` (value: `"Definite"`)





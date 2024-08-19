# ShipEngineApi.SchedulePickupRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelledAt** | **Date** | The date and time that the pickup was cancelled in ShipEngine. | [optional] [readonly] 
**carrierId** | **String** | The carrier_id associated with the pickup | [optional] [readonly] 
**confirmationNumber** | **String** | The carrier confirmation number for the scheduled pickup. | [optional] [readonly] 
**contactDetails** | [**ContactDetails**](ContactDetails.md) |  | 
**createdAt** | **Date** | The date and time that the pickup was created in ShipEngine. | [optional] [readonly] 
**labelIds** | **[String]** | Label IDs that will be included in the pickup request | 
**pickupAddress** | [**Address**](Address.md) |  | [optional] [readonly] 
**pickupId** | **String** | Pickup Resource ID | [optional] [readonly] 
**pickupNotes** | **String** | Used by some carriers to give special instructions for a package pickup | [optional] 
**pickupWindow** | [**PickupWindow**](PickupWindow.md) |  | 
**pickupWindows** | [**[PickupWindows]**](PickupWindows.md) | An array of available pickup windows. Carriers can return multiple times that they will pickup packages.  | [optional] [readonly] 
**warehouseId** | **String** | The warehouse_id associated with the pickup | [optional] [readonly] 



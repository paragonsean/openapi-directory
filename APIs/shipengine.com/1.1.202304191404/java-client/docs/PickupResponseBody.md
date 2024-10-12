

# PickupResponseBody

A pickup response body

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancelledAt** | **OffsetDateTime** | The date and time that the pickup was cancelled in ShipEngine. |  [optional] [readonly] |
|**carrierId** | **String** | The carrier_id associated with the pickup |  [readonly] |
|**confirmationNumber** | **String** | The carrier confirmation number for the scheduled pickup. |  [readonly] |
|**contactDetails** | [**ContactDetails**](ContactDetails.md) |  |  |
|**createdAt** | **OffsetDateTime** | The date and time that the pickup was created in ShipEngine. |  [readonly] |
|**labelIds** | **List&lt;String&gt;** | Label IDs that will be included in the pickup request |  |
|**pickupAddress** | [**Address**](Address.md) |  |  [readonly] |
|**pickupId** | **String** | Pickup Resource ID |  [readonly] |
|**pickupNotes** | **String** | Used by some carriers to give special instructions for a package pickup |  [optional] |
|**pickupWindow** | [**PickupWindow**](PickupWindow.md) |  |  |
|**pickupWindows** | [**List&lt;PickupWindows&gt;**](PickupWindows.md) | An array of available pickup windows. Carriers can return multiple times that they will pickup packages.  |  [optional] [readonly] |
|**warehouseId** | **String** | The warehouse_id associated with the pickup |  [readonly] |




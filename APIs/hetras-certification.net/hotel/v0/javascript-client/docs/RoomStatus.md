# HetrasHotelApiVersion0.RoomStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **String** | Room Condition status | [optional] 
**frontdeskOccupancy** | **String** | The frontdesk occupancy is set by reservation checkin and checkout. It can differ from the              housekeeping occupancy | [optional] 
**housekeepingOccupancy** | **String** | The housekeeping occupancy status is defined by the housekeeping staff. Usually it matches the              frontdesk occupancy, but sometimes the reservation is still inhouse, but it looks like there is no              guest in the room anymore. Then the statuses can differ. | [optional] 
**maintenance** | [**RoomMaintenance**](RoomMaintenance.md) |  | [optional] 



## Enum: ConditionEnum


* `CleanNotInspected` (value: `"CleanNotInspected"`)

* `Clean` (value: `"Clean"`)

* `Dirty` (value: `"Dirty"`)





## Enum: FrontdeskOccupancyEnum


* `Occupied` (value: `"Occupied"`)

* `Vacant` (value: `"Vacant"`)





## Enum: HousekeepingOccupancyEnum


* `Occupied` (value: `"Occupied"`)

* `Vacant` (value: `"Vacant"`)





# HetrasHotelApiVersion0.GetRoomListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | **[String]** | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] 
**conditions** | **[String]** | Return results only for rooms that have the given room condition status. | [optional] 
**locations** | **[String]** | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] 
**maintenances** | **[String]** | Return results only for rooms that have the given maintenance status. | [optional] 
**occupancy** | **String** | Return results only for rooms that have the given frontdesk ocuppancy status. | [optional] 
**roomTypes** | **[String]** | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] 
**views** | **[String]** | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] 



## Enum: [ConditionsEnum]


* `CleanNotInspected` (value: `"CleanNotInspected"`)

* `Clean` (value: `"Clean"`)

* `Dirty` (value: `"Dirty"`)





## Enum: [MaintenancesEnum]


* `NotSet` (value: `"NotSet"`)

* `None` (value: `"None"`)

* `OutOfInventory` (value: `"OutOfInventory"`)

* `OutOfOrder` (value: `"OutOfOrder"`)

* `OutOfService` (value: `"OutOfService"`)





## Enum: OccupancyEnum


* `Occupied` (value: `"Occupied"`)

* `Vacant` (value: `"Vacant"`)





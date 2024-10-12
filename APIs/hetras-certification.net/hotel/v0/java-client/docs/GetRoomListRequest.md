

# GetRoomListRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amenities** | **List&lt;String&gt;** | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. |  [optional] |
|**conditions** | [**List&lt;ConditionsEnum&gt;**](#List&lt;ConditionsEnum&gt;) | Return results only for rooms that have the given room condition status. |  [optional] |
|**locations** | **List&lt;String&gt;** | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. |  [optional] |
|**maintenances** | [**List&lt;MaintenancesEnum&gt;**](#List&lt;MaintenancesEnum&gt;) | Return results only for rooms that have the given maintenance status. |  [optional] |
|**occupancy** | [**OccupancyEnum**](#OccupancyEnum) | Return results only for rooms that have the given frontdesk ocuppancy status. |  [optional] |
|**roomTypes** | **List&lt;String&gt;** | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. |  [optional] |
|**views** | **List&lt;String&gt;** | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. |  [optional] |



## Enum: List&lt;ConditionsEnum&gt;

| Name | Value |
|---- | -----|
| CLEAN_NOT_INSPECTED | &quot;CleanNotInspected&quot; |
| CLEAN | &quot;Clean&quot; |
| DIRTY | &quot;Dirty&quot; |



## Enum: List&lt;MaintenancesEnum&gt;

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| NONE | &quot;None&quot; |
| OUT_OF_INVENTORY | &quot;OutOfInventory&quot; |
| OUT_OF_ORDER | &quot;OutOfOrder&quot; |
| OUT_OF_SERVICE | &quot;OutOfService&quot; |



## Enum: OccupancyEnum

| Name | Value |
|---- | -----|
| OCCUPIED | &quot;Occupied&quot; |
| VACANT | &quot;Vacant&quot; |






# RoomStatus

Represents current room status data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | [**ConditionEnum**](#ConditionEnum) | Room Condition status |  [optional] |
|**frontdeskOccupancy** | [**FrontdeskOccupancyEnum**](#FrontdeskOccupancyEnum) | The frontdesk occupancy is set by reservation checkin and checkout. It can differ from the              housekeeping occupancy |  [optional] |
|**housekeepingOccupancy** | [**HousekeepingOccupancyEnum**](#HousekeepingOccupancyEnum) | The housekeeping occupancy status is defined by the housekeeping staff. Usually it matches the              frontdesk occupancy, but sometimes the reservation is still inhouse, but it looks like there is no              guest in the room anymore. Then the statuses can differ. |  [optional] |
|**maintenance** | [**RoomMaintenance**](RoomMaintenance.md) |  |  [optional] |



## Enum: ConditionEnum

| Name | Value |
|---- | -----|
| CLEAN_NOT_INSPECTED | &quot;CleanNotInspected&quot; |
| CLEAN | &quot;Clean&quot; |
| DIRTY | &quot;Dirty&quot; |



## Enum: FrontdeskOccupancyEnum

| Name | Value |
|---- | -----|
| OCCUPIED | &quot;Occupied&quot; |
| VACANT | &quot;Vacant&quot; |



## Enum: HousekeepingOccupancyEnum

| Name | Value |
|---- | -----|
| OCCUPIED | &quot;Occupied&quot; |
| VACANT | &quot;Vacant&quot; |




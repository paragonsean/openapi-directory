

# Register201ResponseDataShipNav

The navigation information of the ship.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**flightMode** | [**FlightModeEnum**](#FlightModeEnum) | The ship&#39;s set speed when traveling between waypoints or systems. |  |
|**route** | [**Register201ResponseDataShipNavRoute**](Register201ResponseDataShipNavRoute.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the ship |  |
|**systemSymbol** | **String** | The system symbol of the ship&#39;s current location. |  |
|**waypointSymbol** | **String** | The waypoint symbol of the ship&#39;s current location, or if the ship is in-transit, the waypoint symbol of the ship&#39;s destination. |  |



## Enum: FlightModeEnum

| Name | Value |
|---- | -----|
| DRIFT | &quot;DRIFT&quot; |
| STEALTH | &quot;STEALTH&quot; |
| CRUISE | &quot;CRUISE&quot; |
| BURN | &quot;BURN&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IN_TRANSIT | &quot;IN_TRANSIT&quot; |
| IN_ORBIT | &quot;IN_ORBIT&quot; |
| DOCKED | &quot;DOCKED&quot; |




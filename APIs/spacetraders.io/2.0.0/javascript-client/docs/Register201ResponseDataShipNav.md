# SpaceTradersApi.Register201ResponseDataShipNav

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flightMode** | **String** | The ship&#39;s set speed when traveling between waypoints or systems. | [default to &#39;CRUISE&#39;]
**route** | [**Register201ResponseDataShipNavRoute**](Register201ResponseDataShipNavRoute.md) |  | 
**status** | **String** | The current status of the ship | 
**systemSymbol** | **String** | The system symbol of the ship&#39;s current location. | 
**waypointSymbol** | **String** | The waypoint symbol of the ship&#39;s current location, or if the ship is in-transit, the waypoint symbol of the ship&#39;s destination. | 



## Enum: FlightModeEnum


* `DRIFT` (value: `"DRIFT"`)

* `STEALTH` (value: `"STEALTH"`)

* `CRUISE` (value: `"CRUISE"`)

* `BURN` (value: `"BURN"`)





## Enum: StatusEnum


* `IN_TRANSIT` (value: `"IN_TRANSIT"`)

* `IN_ORBIT` (value: `"IN_ORBIT"`)

* `DOCKED` (value: `"DOCKED"`)





# SpaceTradersApi.Register201ResponseDataShipCrew

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **Number** | The maximum number of crew members the ship can support. | 
**current** | **Number** | The current number of crew members on the ship. | 
**morale** | **Number** | A rough measure of the crew&#39;s morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents. | 
**required** | **Number** | The minimum number of crew members required to maintain the ship. | 
**rotation** | **String** | The rotation of crew shifts. A stricter shift improves the ship&#39;s performance. A more relaxed shift improves the crew&#39;s morale. | [default to &#39;STRICT&#39;]
**wages** | **Number** | The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint. | 



## Enum: RotationEnum


* `STRICT` (value: `"STRICT"`)

* `RELAXED` (value: `"RELAXED"`)







# Register201ResponseDataShipCrew

The ship's crew service and maintain the ship's systems and equipment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The maximum number of crew members the ship can support. |  |
|**current** | **Integer** | The current number of crew members on the ship. |  |
|**morale** | **Integer** | A rough measure of the crew&#39;s morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents. |  |
|**required** | **Integer** | The minimum number of crew members required to maintain the ship. |  |
|**rotation** | [**RotationEnum**](#RotationEnum) | The rotation of crew shifts. A stricter shift improves the ship&#39;s performance. A more relaxed shift improves the crew&#39;s morale. |  |
|**wages** | **Integer** | The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint. |  |



## Enum: RotationEnum

| Name | Value |
|---- | -----|
| STRICT | &quot;STRICT&quot; |
| RELAXED | &quot;RELAXED&quot; |






# PropertyRoomModel

A single room (bedroom) property structure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**area** | **String** | The area the property is located in. |  [optional] |
|**branch** | **String** | The branch the block, property or room is assigned to |  [optional] |
|**description** | **String** | The block, property or room description. |  [optional] |
|**etag** | **String** | A unique identifier defining the object and change revision. |  [optional] |
|**fullAddress** | **String** | The full address of a block, property or room, formatted with line breaks such that it may be used on a letter directly. |  [optional] |
|**globalReference** | **String** | The global reference to this block, property or room |  [optional] |
|**heightCentimeters** | **Integer** | Gets the CentiMeter part of the room Height. |  [optional] |
|**heightMeters** | **Integer** | Gets the Meter part of the room Height. |  [optional] |
|**lengthCentimeters** | **Integer** | Gets the CentiMeter part of the room Length. |  [optional] |
|**lengthMeters** | **Integer** | Gets the Meter part of the room Length. |  [optional] |
|**mainPhoto** | **String** | Gets the main photo, if there is one. |  [optional] |
|**managedByStaff** | **String** | The staff memeber that manages the block, property or room |  [optional] |
|**OID** | **String** | The unique Object ID (OID). |  [optional] |
|**propertySource** | **String** | The block, property or room source type |  [optional] |
|**roomFloor** | [**RoomFloorEnum**](#RoomFloorEnum) | Gets and sets the room floor. |  [optional] |
|**roomName** | **String** | The room name (if applicable). |  [optional] |
|**widthCentiMeters** | **Integer** | Gets the CentiMeter part of the room width. |  [optional] |
|**widthMeters** | **Integer** | Gets the Meter part of the room width. |  [optional] |



## Enum: RoomFloorEnum

| Name | Value |
|---- | -----|
| BASEMENT | &quot;Basement&quot; |
| GROUND | &quot;Ground&quot; |
| FIRST | &quot;First&quot; |
| SECOND | &quot;Second&quot; |
| THIRD | &quot;Third&quot; |
| FOURTH | &quot;Fourth&quot; |
| FIFTH | &quot;Fifth&quot; |
| SIXTH_PLUS | &quot;SixthPlus&quot; |
| UNKNOWN | &quot;Unknown&quot; |




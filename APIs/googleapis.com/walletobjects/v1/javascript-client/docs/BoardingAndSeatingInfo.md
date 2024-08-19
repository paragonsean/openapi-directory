# GoogleWalletApi.BoardingAndSeatingInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boardingDoor** | **String** | Set this field only if this flight boards through more than one door or bridge and you want to explicitly print the door location on the boarding pass. Most airlines route their passengers to the right door or bridge by refering to doors/bridges by the &#x60;seatClass&#x60;. In those cases &#x60;boardingDoor&#x60; should not be set. | [optional] 
**boardingGroup** | **String** | The value of boarding group (or zone) this passenger shall board with. eg: \&quot;B\&quot; The label for this value will be determined by the &#x60;boardingPolicy&#x60; field in the &#x60;flightClass&#x60; referenced by this object. | [optional] 
**boardingPosition** | **String** | The value of boarding position. eg: \&quot;76\&quot; | [optional] 
**boardingPrivilegeImage** | [**Image**](Image.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#boardingAndSeatingInfo\&quot;&#x60;. | [optional] 
**seatAssignment** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**seatClass** | **String** | The value of the seat class. eg: \&quot;Economy\&quot; or \&quot;Economy Plus\&quot; | [optional] 
**seatNumber** | **String** | The value of passenger seat. If there is no specific identifier, use &#x60;seatAssignment&#x60; instead. eg: \&quot;25A\&quot; | [optional] 
**sequenceNumber** | **String** | The sequence number on the boarding pass. This usually matches the sequence in which the passengers checked in. Airline might use the number for manual boarding and bag tags. eg: \&quot;49\&quot; | [optional] 



## Enum: BoardingDoorEnum


* `BOARDING_DOOR_UNSPECIFIED` (value: `"BOARDING_DOOR_UNSPECIFIED"`)

* `FRONT` (value: `"FRONT"`)

* `front` (value: `"front"`)

* `BACK` (value: `"BACK"`)

* `back` (value: `"back"`)





# HetrasHotelApiVersion0.Room

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | [**[SimpleAttribute]**](SimpleAttribute.md) | List of amenities for the room | [optional] 
**beddings** | [**[RoomBedding]**](RoomBedding.md) | Provides information about available beds in the room | [optional] 
**created** | **Date** | Timestamp the room was created | [optional] 
**description** | **String** | Description of the room | [optional] 
**expectedOccupancy** | **Number** | The common amount of persons for the room | 
**extraBedAllowed** | **Boolean** | Is there an extra bed allowed in the room | [optional] 
**floor** | **Number** | Floor of the room | 
**locations** | [**[SimpleAttribute]**](SimpleAttribute.md) | List of locations for the room | [optional] 
**maxPersons** | **Number** | Maximum number of allowed persons in the room | 
**minPersons** | **Number** | Minimum number of allowed persons in the room | 
**name** | **String** | Name of the room | [optional] 
**number** | **String** | Number of the room | 
**reservations** | [**[EmbeddedReservation]**](EmbeddedReservation.md) | Current reservation(s) for the room. It shows reservations due to arrive today and the one still inhouse.              If there is a day-use reservation assigned for today it can show you up to 3 reservations. One that will              depart today, the day-use reservqation for today and the one due to arrive | [optional] 
**roomType** | [**EmbeddedRoomType**](EmbeddedRoomType.md) |  | 
**status** | [**RoomStatus**](RoomStatus.md) |  | 
**updated** | **Date** | Timestamp of when the room was changed the last time | [optional] 
**views** | [**[SimpleAttribute]**](SimpleAttribute.md) | List of views for the room | [optional] 



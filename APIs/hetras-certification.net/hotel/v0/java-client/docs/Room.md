

# Room

Represents a room for a property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amenities** | [**List&lt;SimpleAttribute&gt;**](SimpleAttribute.md) | List of amenities for the room |  [optional] |
|**beddings** | [**List&lt;RoomBedding&gt;**](RoomBedding.md) | Provides information about available beds in the room |  [optional] |
|**created** | **OffsetDateTime** | Timestamp the room was created |  [optional] |
|**description** | **String** | Description of the room |  [optional] |
|**expectedOccupancy** | **Integer** | The common amount of persons for the room |  |
|**extraBedAllowed** | **Boolean** | Is there an extra bed allowed in the room |  [optional] |
|**floor** | **Integer** | Floor of the room |  |
|**locations** | [**List&lt;SimpleAttribute&gt;**](SimpleAttribute.md) | List of locations for the room |  [optional] |
|**maxPersons** | **Integer** | Maximum number of allowed persons in the room |  |
|**minPersons** | **Integer** | Minimum number of allowed persons in the room |  |
|**name** | **String** | Name of the room |  [optional] |
|**number** | **String** | Number of the room |  |
|**reservations** | [**List&lt;EmbeddedReservation&gt;**](EmbeddedReservation.md) | Current reservation(s) for the room. It shows reservations due to arrive today and the one still inhouse.              If there is a day-use reservation assigned for today it can show you up to 3 reservations. One that will              depart today, the day-use reservqation for today and the one due to arrive |  [optional] |
|**roomType** | [**EmbeddedRoomType**](EmbeddedRoomType.md) |  |  |
|**status** | [**RoomStatus**](RoomStatus.md) |  |  |
|**updated** | **OffsetDateTime** | Timestamp of when the room was changed the last time |  [optional] |
|**views** | [**List&lt;SimpleAttribute&gt;**](SimpleAttribute.md) | List of views for the room |  [optional] |




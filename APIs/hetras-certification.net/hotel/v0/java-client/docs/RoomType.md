

# RoomType

Represent a room type for a property

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amenities** | [**List&lt;SimpleAttribute&gt;**](SimpleAttribute.md) | List of amenities for the room type |  [optional] |
|**beddingType** | [**BeddingTypeEnum**](#BeddingTypeEnum) | The type of bed for the room type |  [optional] |
|**code** | **String** | Code of the room type |  [optional] |
|**created** | **OffsetDateTime** | Timestamp the room type was created |  [optional] |
|**_default** | **Boolean** | Specifies if the room type is the default room type of the hotel |  [optional] |
|**description** | **String** | Description of the room type |  [optional] |
|**expectedOccupancy** | **Integer** | The common amount of persons for the room |  [optional] |
|**facilities** | [**List&lt;SimpleAttribute&gt;**](SimpleAttribute.md) | List of facilities for the room type |  [optional] |
|**maxPersons** | **Integer** | Maximum number of allowed persons for that room type |  [optional] |
|**minPersons** | **Integer** | Minimum number of allowed persons for that room type |  [optional] |
|**name** | **String** | Name of the room type |  [optional] |
|**updated** | **OffsetDateTime** | Timestamp of when the room type was changed the last time |  [optional] |
|**views** | [**List&lt;SimpleAttribute&gt;**](SimpleAttribute.md) | List of views for the room type |  [optional] |



## Enum: BeddingTypeEnum

| Name | Value |
|---- | -----|
| NOT_DEFINED | &quot;NotDefined&quot; |
| DOUBLE | &quot;Double&quot; |
| FUTON | &quot;Futon&quot; |
| KING | &quot;King&quot; |
| MURPHY_BED | &quot;MurphyBed&quot; |
| QUEEN | &quot;Queen&quot; |
| SOFA_BED | &quot;SofaBed&quot; |
| TATAMI_MATS | &quot;TatamiMats&quot; |
| TWIN | &quot;Twin&quot; |
| SINGLE | &quot;Single&quot; |




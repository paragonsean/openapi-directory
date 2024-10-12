

# GetCharactersCharacterIdOk

200 ok object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allianceId** | **Integer** | The character&#39;s alliance ID |  [optional] |
|**ancestryId** | **Integer** | ancestry_id integer |  [optional] |
|**birthday** | **OffsetDateTime** | Creation date of the character |  |
|**bloodlineId** | **Integer** | bloodline_id integer |  |
|**corporationId** | **Integer** | The character&#39;s corporation ID |  |
|**description** | **String** | description string |  [optional] |
|**factionId** | **Integer** | ID of the faction the character is fighting for, if the character is enlisted in Factional Warfare |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | gender string |  |
|**name** | **String** | name string |  |
|**raceId** | **Integer** | race_id integer |  |
|**securityStatus** | **Float** | security_status number |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| FEMALE | &quot;female&quot; |
| MALE | &quot;male&quot; |




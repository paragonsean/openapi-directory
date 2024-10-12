

# ScoutingObservation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339). |  |
|**fieldIds** | **List&lt;String&gt;** | Array of field ids associated with this observation. |  |
|**id** | **UUID** | The id of a scouting observation. |  |
|**location** | [**Geometry**](Geometry.md) |  |  |
|**locationDisplayColor** | [**LocationDisplayColorEnum**](#LocationDisplayColorEnum) | Color of scouting pin assigned in the Climate FieldView app. Limited in the Ux to a set of RGB values. * #307af7 * #38d753 * #b037e4 * #ef3e3e * #f7ec41 * #ff8439 * #808080  |  |
|**note** | **String** | The text of the scouting observation. Maximum of 4000 characters. |  |
|**startTime** | **OffsetDateTime** | The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339). |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the scouting observation For example : ACTIVE, DELETED |  |
|**tags** | [**List&lt;ScoutingTag&gt;**](ScoutingTag.md) | For example, ROCK_STONE, PONDING_WET, HAIL Maximum 20 tags allowed, 40 characters per tag. |  |
|**timespan** | [**TimespanEnum**](#TimespanEnum) | Permanent or seasonal |  |
|**title** | **String** | The title or summary of the scouting observation. 40 Characters long, no emojis, and leading and trailing whitespace will be trimmed. |  |
|**updatedAt** | **OffsetDateTime** | The time the scouting observation or any of its attachments was last updated.Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339). |  |



## Enum: LocationDisplayColorEnum

| Name | Value |
|---- | -----|
| _307AF7 | &quot;#307af7&quot; |
| _38D753 | &quot;#38d753&quot; |
| B037E4 | &quot;#b037e4&quot; |
| EF3E3E | &quot;#ef3e3e&quot; |
| F7EC41 | &quot;#f7ec41&quot; |
| FF8439 | &quot;#ff8439&quot; |
| _808080 | &quot;#808080&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: TimespanEnum

| Name | Value |
|---- | -----|
| PERMANENT | &quot;PERMANENT&quot; |
| SEASONAL | &quot;SEASONAL&quot; |




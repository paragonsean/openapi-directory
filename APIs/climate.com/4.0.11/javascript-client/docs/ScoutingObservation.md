# ClimateFieldViewPlatformApis.ScoutingObservation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339). | 
**fieldIds** | **[String]** | Array of field ids associated with this observation. | 
**id** | **String** | The id of a scouting observation. | 
**location** | [**Geometry**](Geometry.md) |  | 
**locationDisplayColor** | **String** | Color of scouting pin assigned in the Climate FieldView app. Limited in the Ux to a set of RGB values. * #307af7 * #38d753 * #b037e4 * #ef3e3e * #f7ec41 * #ff8439 * #808080  | 
**note** | **String** | The text of the scouting observation. Maximum of 4000 characters. | 
**startTime** | **Date** | The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339). | 
**status** | **String** | The status of the scouting observation For example : ACTIVE, DELETED | 
**tags** | [**[ScoutingTag]**](ScoutingTag.md) | For example, ROCK_STONE, PONDING_WET, HAIL Maximum 20 tags allowed, 40 characters per tag. | 
**timespan** | **String** | Permanent or seasonal | 
**title** | **String** | The title or summary of the scouting observation. 40 Characters long, no emojis, and leading and trailing whitespace will be trimmed. | 
**updatedAt** | **Date** | The time the scouting observation or any of its attachments was last updated.Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339). | 



## Enum: LocationDisplayColorEnum


* `307af7` (value: `"#307af7"`)

* `38d753` (value: `"#38d753"`)

* `b037e4` (value: `"#b037e4"`)

* `ef3e3e` (value: `"#ef3e3e"`)

* `f7ec41` (value: `"#f7ec41"`)

* `ff8439` (value: `"#ff8439"`)

* `808080` (value: `"#808080"`)





## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `DELETED` (value: `"DELETED"`)





## Enum: TimespanEnum


* `PERMANENT` (value: `"PERMANENT"`)

* `SEASONAL` (value: `"SEASONAL"`)





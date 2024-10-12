

# CreateTextTrackAlt1Request


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Active text tracks appear in the player and are visible to other users. Only one text track per language can be active. |  [optional] |
|**language** | **String** | The language of the text track. For a complete list of valid languages, use the [/languages?filter&#x3D;texttracks](https://developer.vimeo.com/api/endpoints/videos#GET/languages) endpoint. |  |
|**name** | **String** | The name of the text track. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the text track. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAPTIONS | &quot;captions&quot; |
| CHAPTERS | &quot;chapters&quot; |
| DESCRIPTIONS | &quot;descriptions&quot; |
| METADATA | &quot;metadata&quot; |
| SUBTITLES | &quot;subtitles&quot; |




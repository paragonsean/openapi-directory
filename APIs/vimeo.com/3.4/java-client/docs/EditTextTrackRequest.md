

# EditTextTrackRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether the text track is active, meaning that it appears in the player. Only one text track per language, and type, can be active. |  [optional] |
|**language** | **String** | The language of the text track. For a full list of valid languages, use the [/languages?filter&#x3D;texttracks](https://developer.vimeo.com/api/endpoints/videos#GET/languages) endpoint. |  [optional] |
|**name** | **String** | The name of the text track. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The text track type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAPTIONS | &quot;captions&quot; |
| CHAPTERS | &quot;chapters&quot; |
| DESCRIPTIONS | &quot;descriptions&quot; |
| METADATA | &quot;metadata&quot; |
| SUBTITLES | &quot;subtitles&quot; |




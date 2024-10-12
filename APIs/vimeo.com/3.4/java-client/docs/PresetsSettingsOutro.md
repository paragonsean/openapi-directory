

# PresetsSettingsOutro


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clips** | **String** | A comma-separated list of video URIs. Present only if the type is &#x60;uploaded_clips&#x60;. |  [optional] |
|**link** | [**PresetsSettingsOutroLink**](PresetsSettingsOutroLink.md) |  |  [optional] |
|**text** | **String** | The outro text. Present only if the type is &#x60;text&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The preset outro type: |  |
|**videos** | **String** | A comma-separated list of video URIs. Present only if type is &#x60;no idea&#x60;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LINK | &quot;link&quot; |
| NO_IDEA | &quot;no idea&quot; |
| TEXT | &quot;text&quot; |
| UPLOADED_CLIPS | &quot;uploaded_clips&quot; |
| UPLOADED_VIDEOS | &quot;uploaded_videos&quot; |






# Webcast


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | **String** | Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe. |  |
|**date** | **String** | The date for the webcast in &#x60;yyyy-mm-dd&#x60; format. May be null. |  [optional] |
|**_file** | **String** | File identification as may be required for some types. May be null. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of webcast, typically descriptive of the streaming provider. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| YOUTUBE | &quot;youtube&quot; |
| TWITCH | &quot;twitch&quot; |
| USTREAM | &quot;ustream&quot; |
| IFRAME | &quot;iframe&quot; |
| HTML5 | &quot;html5&quot; |
| RTMP | &quot;rtmp&quot; |
| LIVESTREAM | &quot;livestream&quot; |
| DIRECT_LINK | &quot;direct_link&quot; |
| MMS | &quot;mms&quot; |
| JUSTIN | &quot;justin&quot; |
| STEMTV | &quot;stemtv&quot; |
| DACAST | &quot;dacast&quot; |




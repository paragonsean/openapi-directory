# TheBlueAllianceApiV3.Webcast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **String** | Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case of iframe types, contains HTML to embed the stream in an HTML iframe. | 
**date** | **String** | The date for the webcast in &#x60;yyyy-mm-dd&#x60; format. May be null. | [optional] 
**file** | **String** | File identification as may be required for some types. May be null. | [optional] 
**type** | **String** | Type of webcast, typically descriptive of the streaming provider. | 



## Enum: TypeEnum


* `youtube` (value: `"youtube"`)

* `twitch` (value: `"twitch"`)

* `ustream` (value: `"ustream"`)

* `iframe` (value: `"iframe"`)

* `html5` (value: `"html5"`)

* `rtmp` (value: `"rtmp"`)

* `livestream` (value: `"livestream"`)

* `direct_link` (value: `"direct_link"`)

* `mms` (value: `"mms"`)

* `justin` (value: `"justin"`)

* `stemtv` (value: `"stemtv"`)

* `dacast` (value: `"dacast"`)





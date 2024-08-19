

# RenderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockAds** | **Boolean** | Whether to block ads on the rendered page |  [optional] |
|**clickAccept** | **Boolean** | Whether to automatically click accept buttons on the rendered page |  [optional] |
|**delay** | **String** | The amount of milliseconds to delay before taking a screenshot |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | The format of the rendered output |  [optional] |
|**fullPage** | **Boolean** | Whether to capture the full page |  [optional] |
|**gpu** | **Boolean** | Whether to enable GPU rendering |  [optional] |
|**height** | **Integer** | The viewport height of the rendered output |  [optional] |
|**hideCookieBanners** | **Boolean** | Whether to hide cookie banners on the rendered page |  [optional] |
|**html** | **String** | The raw HTML to render as an image or video |  [optional] |
|**metadata** | **Boolean** | Whether to return metadata about the URL |  [optional] |
|**retina** | **Boolean** | Whether to render the image in retina quality |  [optional] |
|**selector** | **String** | The CSS selector of an element you would like to capture |  [optional] |
|**thumbHeight** | **Integer** | The height of the thumbnail image |  [optional] |
|**thumbWidth** | **Integer** | The width of the thumbnail image |  [optional] |
|**url** | **String** | The URL to render as an image or video |  [optional] |
|**waitFor** | **String** | CSS selector of an element to wait to be present in the web page before rendering |  [optional] |
|**waitToLeave** | **String** | CSS selector of an element, such as a loading spinner, to wait to leave the web page before rendering |  [optional] |
|**waitUntil** | [**WaitUntilEnum**](#WaitUntilEnum) | When |  [optional] |
|**width** | **Integer** | The viewport width of the rendered output |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PNG | &quot;png&quot; |
| JPG | &quot;jpg&quot; |
| PDF | &quot;pdf&quot; |
| SVG | &quot;svg&quot; |
| MP4 | &quot;mp4&quot; |
| WEBP | &quot;webp&quot; |
| WEBM | &quot;webm&quot; |
| HTML | &quot;html&quot; |



## Enum: WaitUntilEnum

| Name | Value |
|---- | -----|
| REQUESTSFINISHED | &quot;requestsfinished&quot; |
| MOSTREQUESTSFINISHED | &quot;mostrequestsfinished&quot; |
| LOADED | &quot;loaded&quot; |
| DOMLOADED | &quot;domloaded&quot; |




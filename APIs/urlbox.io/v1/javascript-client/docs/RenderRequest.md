# UrlboxApi.RenderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockAds** | **Boolean** | Whether to block ads on the rendered page | [optional] 
**clickAccept** | **Boolean** | Whether to automatically click accept buttons on the rendered page | [optional] 
**delay** | **String** | The amount of milliseconds to delay before taking a screenshot | [optional] 
**format** | **String** | The format of the rendered output | [optional] 
**fullPage** | **Boolean** | Whether to capture the full page | [optional] 
**gpu** | **Boolean** | Whether to enable GPU rendering | [optional] 
**height** | **Number** | The viewport height of the rendered output | [optional] 
**hideCookieBanners** | **Boolean** | Whether to hide cookie banners on the rendered page | [optional] 
**html** | **String** | The raw HTML to render as an image or video | [optional] 
**metadata** | **Boolean** | Whether to return metadata about the URL | [optional] 
**retina** | **Boolean** | Whether to render the image in retina quality | [optional] 
**selector** | **String** | The CSS selector of an element you would like to capture | [optional] 
**thumbHeight** | **Number** | The height of the thumbnail image | [optional] 
**thumbWidth** | **Number** | The width of the thumbnail image | [optional] 
**url** | **String** | The URL to render as an image or video | [optional] 
**waitFor** | **String** | CSS selector of an element to wait to be present in the web page before rendering | [optional] 
**waitToLeave** | **String** | CSS selector of an element, such as a loading spinner, to wait to leave the web page before rendering | [optional] 
**waitUntil** | **String** | When | [optional] 
**width** | **Number** | The viewport width of the rendered output | [optional] 



## Enum: FormatEnum


* `png` (value: `"png"`)

* `jpg` (value: `"jpg"`)

* `pdf` (value: `"pdf"`)

* `svg` (value: `"svg"`)

* `mp4` (value: `"mp4"`)

* `webp` (value: `"webp"`)

* `webm` (value: `"webm"`)

* `html` (value: `"html"`)





## Enum: WaitUntilEnum


* `requestsfinished` (value: `"requestsfinished"`)

* `mostrequestsfinished` (value: `"mostrequestsfinished"`)

* `loaded` (value: `"loaded"`)

* `domloaded` (value: `"domloaded"`)





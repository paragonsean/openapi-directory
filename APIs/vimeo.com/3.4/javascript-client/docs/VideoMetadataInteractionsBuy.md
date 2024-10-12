# Vimeo.VideoMetadataInteractionsBuy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | The currency code for the current user&#39;s region. | 
**displayPrice** | **String** | Formatted price to display to buy an On Demand video. | 
**download** | **String** | The user&#39;s download access to this On Demand video:  Option descriptions:  * &#x60;available&#x60; - The video is available for download.  * &#x60;purchased&#x60; - The user has purchased the video.  * &#x60;restricted&#x60; - The user isn&#39;t permitted to download the video.  * &#x60;unavailable&#x60; - The video isn&#39;t available for download.  | 
**drm** | **Boolean** | Whether the video has DRM. | 
**link** | **String** | The URL to buy the On Demand video on Vimeo. | 
**price** | **Number** | The numeric value of the price for buying the On Demand video. | 
**purchaseTime** | **String** | The time in ISO 8601 format when the On Demand video was purchased. | 
**stream** | **String** | The user&#39;s streaming access to this On Demand video:  Option descriptions:  * &#x60;available&#x60; - The video is available for streaming.  * &#x60;purchased&#x60; - The user has purchased the video.  * &#x60;restricted&#x60; - The user isn&#39;t permitted to stream the video.  * &#x60;unavailable&#x60; - The video isn&#39;t available for streaming  | 
**uri** | **String** | The product URI to purchase the On Demand video. | 



## Enum: DownloadEnum


* `available` (value: `"available"`)

* `purchased` (value: `"purchased"`)

* `restricted` (value: `"restricted"`)

* `unavailable` (value: `"unavailable"`)





## Enum: StreamEnum


* `available` (value: `"available"`)

* `purchased` (value: `"purchased"`)

* `restricted` (value: `"restricted"`)

* `unavailable` (value: `"unavailable"`)





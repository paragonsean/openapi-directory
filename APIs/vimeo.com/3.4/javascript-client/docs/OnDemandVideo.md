# Vimeo.OnDemandVideo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buy** | [**OnDemandVideoBuy**](OnDemandVideoBuy.md) |  | 
**description** | **String** | Description of the On Demand video. | [optional] 
**duration** | **String** | The duration of the On Demand video. | [optional] 
**episode** | **Number** | The episode number of the On Demand video. | [optional] 
**interactions** | [**OnDemandVideoInteractions**](OnDemandVideoInteractions.md) |  | 
**link** | **String** | The link to this video on Vimeo. | 
**metadata** | [**OnDemandVideoMetadata**](OnDemandVideoMetadata.md) |  | 
**name** | **String** | The title of the On Demand video. | [optional] 
**options** | **[String]** | An array of HTTP methods permitted on this URI. | [optional] 
**pictures** | [**Picture**](Picture.md) | The active picture for this video. | [optional] 
**playProgress** | **Number** | The user&#39;s most recent play position in seconds for this video. | 
**position** | **Number** | Describes the manual position of this video relative to the other videos owned by this On Demand page. | [optional] 
**releaseDate** | **String** | The time in ISO 8601 format when the On Demand video was created or published. | [optional] 
**releaseYear** | **Number** | The year that this On Demand video was released. | 
**rent** | [**OnDemandVideoRent**](OnDemandVideoRent.md) |  | 
**type** | **String** | The type of the On Demand video:  Option descriptions:  * &#x60;extra&#x60; - The On Demand video is an extra feature.  * &#x60;main&#x60; - The On Demand video is a main feature.  * &#x60;trailer&#x60; - The On Demand video is a trailer.  | 
**uri** | **String** | The video container&#39;s relative URI. | 
**user** | [**User**](User.md) | The owner of the video. | [optional] 



## Enum: TypeEnum


* `extra` (value: `"extra"`)

* `main` (value: `"main"`)

* `trailer` (value: `"trailer"`)





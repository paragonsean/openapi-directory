# Vimeo.OnDemandPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | [**Picture**](Picture.md) | The background image for the On Demand page on Vimeo. | 
**colors** | [**OnDemandPageColors**](OnDemandPageColors.md) |  | 
**contentRating** | **[String]** | An array of the page&#39;s content ratings. | 
**createdTime** | **String** | The time in ISO 8601 format when the page was created. | [optional] 
**description** | **String** | The description of this On Demand page. | 
**domainLink** | **String** | The link to this page on its own domain. | 
**episodes** | [**OnDemandPageEpisodes**](OnDemandPageEpisodes.md) |  | 
**film** | [**Video**](Video.md) | This On Demand page&#39;s film, if it is a film. | [optional] 
**genres** | [**[OnDemandGenre]**](OnDemandGenre.md) | All the genres assigned to this page. | 
**link** | **String** | The link to the page on Vimeo. | 
**metadata** | [**OnDemandPageMetadata**](OnDemandPageMetadata.md) |  | 
**modifiedTime** | **String** | he time in ISO 8601 format when the page was last modified. | [optional] 
**name** | **String** | A descriptive title of this On Demand page. | 
**pictures** | [**Picture**](Picture.md) | The active poster for this On Demand page. | 
**preorder** | [**OnDemandPagePreorder**](OnDemandPagePreorder.md) |  | 
**published** | [**OnDemandPagePublished**](OnDemandPagePublished.md) |  | 
**rating** | **Number** | The rating of this page. | 
**resourceKey** | **String** | The VOD resource key. | 
**sku** | **String** | The creator-designated SKU for this On Demand page. | [optional] 
**subscription** | [**OnDemandPageSubscription**](OnDemandPageSubscription.md) |  | 
**theme** | **String** | The graphical theme for this On Demand page. | 
**thumbnail** | [**Picture**](Picture.md) | The thumbnail image for the On Demand page on Vimeo. | 
**trailer** | [**Video**](Video.md) | The trailer for this On Demand page. | 
**type** | **String** | Whether this On Demand page is for a film or a series.  Option descriptions:  * &#x60;film&#x60; - The On Demand page is for a film.  * &#x60;series&#x60; - The On Demand page is for a series.  | 
**uri** | **String** | The relative URI of the On Demand page. | 
**user** | [**User**](User.md) | The user who created this On Demand page. | 



## Enum: TypeEnum


* `film` (value: `"film"`)

* `series` (value: `"series"`)





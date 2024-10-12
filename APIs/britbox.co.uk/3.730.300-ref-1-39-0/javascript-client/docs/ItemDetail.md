# RocketServices.ItemDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyright** | **String** | Copyright information about this item | [optional] 
**credits** | [**[Credit]**](Credit.md) | A list of credits associated with this item. | [optional] 
**customMetadata** | [**[ItemCustomMetadata]**](ItemCustomMetadata.md) | An ordered list of custom name-value-pair item metadata.  Usually displayed on an item detail page.  | [optional] 
**description** | **String** | The description of this item. | [optional] 
**distributor** | **String** | The distributor of this item. | [optional] 
**episodes** | [**ItemList**](ItemList.md) |  | [optional] 
**eventDate** | **Date** | The optional date of an event. Specific to a Program item type.  | [optional] 
**genrePaths** | **[String]** | An array of genre paths mapping to the values within the &#x60;genres&#x60; array from ItemSummary.  | [optional] 
**location** | **String** | The optional location (e.g. city) of an event. Specific to a Program item type.  | [optional] 
**season** | [**ItemDetail**](ItemDetail.md) |  | [optional] 
**seasons** | [**ItemList**](ItemList.md) |  | [optional] 
**show** | [**ItemDetail**](ItemDetail.md) |  | [optional] 
**totalUserRatings** | **Number** | The total number of users who have rated this item. | [optional] 
**trailers** | [**[ItemSummary]**](ItemSummary.md) | A list of trailers associated with this item. | [optional] 
**venue** | **String** | The optional venue of an event. Specific to a Program item type.  | [optional] 



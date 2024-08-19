# RocketServices.ItemSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisoryText** | **String** | Advisory text about this item, related to the classification | [optional] 
**availableEpisodeCount** | **Number** | The number of available episodes in the season, if the item is a season. | [optional] 
**availableSeasonCount** | **Number** | The number of available seasons in the show, if the item is a show. | [optional] 
**averageUserRating** | **Number** | The average user rating. When based on user ratings from our system this will be out of 10.  | [optional] 
**badge** | **String** | The badge this item has. | [optional] 
**channelShortCode** | **String** | The channel short code, if the item is a channel. | [optional] 
**classification** | [**ClassificationSummary**](ClassificationSummary.md) |  | [optional] 
**contextualTitle** | **String** | A contextually relative title to display after a parent title. Mostly applicable to Season, Episode and Trailer.  | [optional] 
**customFields** | **{String: Object}** | A map of custom fields defined by a curator for an item. | [optional] 
**customId** | **String** | A custom identifier for this item. For example the id for this item under a different content system.  | [optional] 
**duration** | **Number** | The duration of the media in seconds. | [optional] 
**episodeCount** | **Number** | The number of episodes in the season, if the item is a season. | [optional] 
**episodeName** | **String** | The full name of an episode. | [optional] 
**episodeNumber** | **Number** | The number of an episode, if the item is an episode. | [optional] 
**genres** | **[String]** | The array of genres this item belongs to. | [optional] 
**hasClosedCaptions** | **Boolean** | Whether closed captioning is available. | [optional] 
**id** | **String** | Unique identifier for an Item | 
**images** | **{String: String}** |  | [optional] 
**offers** | [**[Offer]**](Offer.md) | The array of available offers for this item. | [optional] 
**path** | **String** | The path to the detail page of this item. Can be used to load the item detail page via the /page endpoint. | 
**releaseYear** | **Number** | The year this item was released | [optional] 
**scopes** | **[String]** | The scopes for this item | [optional] 
**seasonId** | **String** | The identifier of the season this item belongs to, if the item is an episode. | [optional] 
**seasonNumber** | **Number** | The number of a season, if the item is a season. | [optional] 
**shortDescription** | **String** | A truncated description of the item | [optional] 
**showId** | **String** | The identifier of the show this item belongs to, if the item is a season or episode. | [optional] 
**showTitle** | **String** |  | [optional] 
**subtype** | **String** | Subtype of the item. Mainly used to identify different types when &#x60;type&#x60; is &#x60;customAsset&#x60;  | [optional] 
**tagline** | **String** | The tagline of the item | [optional] 
**themes** | [**[Theme]**](Theme.md) | Gets themes associated with the item | [optional] 
**title** | **String** | The display title of the item. | 
**type** | **String** | The type of item | 
**watchPath** | **String** | The path to watch this item, if the item is a watchable type, e.g. a &#x60;movie&#x60;, &#x60;program&#x60; and &#x60;episode&#x60;. | [optional] 



## Enum: TypeEnum


* `movie` (value: `"movie"`)

* `show` (value: `"show"`)

* `season` (value: `"season"`)

* `episode` (value: `"episode"`)

* `program` (value: `"program"`)

* `link` (value: `"link"`)

* `trailer` (value: `"trailer"`)

* `channel` (value: `"channel"`)

* `customAsset` (value: `"customAsset"`)





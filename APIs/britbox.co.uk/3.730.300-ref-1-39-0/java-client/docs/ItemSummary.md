

# ItemSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advisoryText** | **String** | Advisory text about this item, related to the classification |  [optional] |
|**availableEpisodeCount** | **Integer** | The number of available episodes in the season, if the item is a season. |  [optional] |
|**availableSeasonCount** | **Integer** | The number of available seasons in the show, if the item is a show. |  [optional] |
|**averageUserRating** | **BigDecimal** | The average user rating. When based on user ratings from our system this will be out of 10.  |  [optional] |
|**badge** | **String** | The badge this item has. |  [optional] |
|**channelShortCode** | **String** | The channel short code, if the item is a channel. |  [optional] |
|**classification** | [**ClassificationSummary**](ClassificationSummary.md) |  |  [optional] |
|**contextualTitle** | **String** | A contextually relative title to display after a parent title. Mostly applicable to Season, Episode and Trailer.  |  [optional] |
|**customFields** | **Map&lt;String, Object&gt;** | A map of custom fields defined by a curator for an item. |  [optional] |
|**customId** | **String** | A custom identifier for this item. For example the id for this item under a different content system.  |  [optional] |
|**duration** | **Integer** | The duration of the media in seconds. |  [optional] |
|**episodeCount** | **Integer** | The number of episodes in the season, if the item is a season. |  [optional] |
|**episodeName** | **String** | The full name of an episode. |  [optional] |
|**episodeNumber** | **Integer** | The number of an episode, if the item is an episode. |  [optional] |
|**genres** | **List&lt;String&gt;** | The array of genres this item belongs to. |  [optional] |
|**hasClosedCaptions** | **Boolean** | Whether closed captioning is available. |  [optional] |
|**id** | **String** | Unique identifier for an Item |  |
|**images** | **Map&lt;String, URI&gt;** |  |  [optional] |
|**offers** | [**List&lt;Offer&gt;**](Offer.md) | The array of available offers for this item. |  [optional] |
|**path** | **String** | The path to the detail page of this item. Can be used to load the item detail page via the /page endpoint. |  |
|**releaseYear** | **Integer** | The year this item was released |  [optional] |
|**scopes** | **List&lt;String&gt;** | The scopes for this item |  [optional] |
|**seasonId** | **String** | The identifier of the season this item belongs to, if the item is an episode. |  [optional] |
|**seasonNumber** | **Integer** | The number of a season, if the item is a season. |  [optional] |
|**shortDescription** | **String** | A truncated description of the item |  [optional] |
|**showId** | **String** | The identifier of the show this item belongs to, if the item is a season or episode. |  [optional] |
|**showTitle** | **String** |  |  [optional] |
|**subtype** | **String** | Subtype of the item. Mainly used to identify different types when &#x60;type&#x60; is &#x60;customAsset&#x60;  |  [optional] |
|**tagline** | **String** | The tagline of the item |  [optional] |
|**themes** | [**List&lt;Theme&gt;**](Theme.md) | Gets themes associated with the item |  [optional] |
|**title** | **String** | The display title of the item. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of item |  |
|**watchPath** | **String** | The path to watch this item, if the item is a watchable type, e.g. a &#x60;movie&#x60;, &#x60;program&#x60; and &#x60;episode&#x60;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MOVIE | &quot;movie&quot; |
| SHOW | &quot;show&quot; |
| SEASON | &quot;season&quot; |
| EPISODE | &quot;episode&quot; |
| PROGRAM | &quot;program&quot; |
| LINK | &quot;link&quot; |
| TRAILER | &quot;trailer&quot; |
| CHANNEL | &quot;channel&quot; |
| CUSTOM_ASSET | &quot;customAsset&quot; |




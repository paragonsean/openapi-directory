

# VideosForXMLInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentColonEncoded** | **String** | video description |  [optional] |
|**dcColonCreator** | **String** | publisher user name |  [optional] |
|**description** | **String** | video description |  [optional] |
|**enclosure** | [**VideosForXMLInnerEnclosure**](VideosForXMLInnerEnclosure.md) |  |  [optional] |
|**guid** | **String** | video canonical URL |  [optional] |
|**link** | **String** | video watch page URL |  [optional] |
|**mediaColonCategory** | **Integer** | video category (MRSS) |  [optional] |
|**mediaColonCommunity** | [**VideosForXMLInnerMediaCommunity**](VideosForXMLInnerMediaCommunity.md) |  |  [optional] |
|**mediaColonDescription** | **String** |  |  [optional] |
|**mediaColonEmbed** | [**VideosForXMLInnerMediaEmbed**](VideosForXMLInnerMediaEmbed.md) |  |  [optional] |
|**mediaColonGroup** | [**List&lt;VideosForXMLInnerMediaGroupInner&gt;**](VideosForXMLInnerMediaGroupInner.md) | list of streamable files for the video. see [media:peerLink](https://www.rssboard.org/media-rss#media-peerlink) and [media:content](https://www.rssboard.org/media-rss#media-content) or  (MRSS) |  [optional] |
|**mediaColonPlayer** | [**VideosForXMLInnerMediaPlayer**](VideosForXMLInnerMediaPlayer.md) |  |  [optional] |
|**mediaColonRating** | [**MediaColonRatingEnum**](#MediaColonRatingEnum) | see [media:rating](https://www.rssboard.org/media-rss#media-rating) (MRSS) |  [optional] |
|**mediaColonThumbnail** | [**VideosForXMLInnerMediaThumbnail**](VideosForXMLInnerMediaThumbnail.md) |  |  [optional] |
|**mediaColonTitle** | **String** | see [media:title](https://www.rssboard.org/media-rss#media-title) (MRSS). We only use &#x60;plain&#x60; titles. |  [optional] |
|**pubDate** | **OffsetDateTime** | video publication date |  [optional] |



## Enum: MediaColonRatingEnum

| Name | Value |
|---- | -----|
| NONADULT | &quot;nonadult&quot; |
| ADULT | &quot;adult&quot; |




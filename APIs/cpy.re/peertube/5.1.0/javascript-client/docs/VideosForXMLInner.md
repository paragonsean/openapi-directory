# PeerTube.VideosForXMLInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentencoded** | **String** | video description | [optional] 
**dccreator** | **String** | publisher user name | [optional] 
**description** | **String** | video description | [optional] 
**enclosure** | [**VideosForXMLInnerEnclosure**](VideosForXMLInnerEnclosure.md) |  | [optional] 
**guid** | **String** | video canonical URL | [optional] 
**link** | **String** | video watch page URL | [optional] 
**mediacategory** | **Number** | video category (MRSS) | [optional] 
**mediacommunity** | [**VideosForXMLInnerMediaCommunity**](VideosForXMLInnerMediaCommunity.md) |  | [optional] 
**mediadescription** | **String** |  | [optional] 
**mediaembed** | [**VideosForXMLInnerMediaEmbed**](VideosForXMLInnerMediaEmbed.md) |  | [optional] 
**mediagroup** | [**[VideosForXMLInnerMediaGroupInner]**](VideosForXMLInnerMediaGroupInner.md) | list of streamable files for the video. see [media:peerLink](https://www.rssboard.org/media-rss#media-peerlink) and [media:content](https://www.rssboard.org/media-rss#media-content) or  (MRSS) | [optional] 
**mediaplayer** | [**VideosForXMLInnerMediaPlayer**](VideosForXMLInnerMediaPlayer.md) |  | [optional] 
**mediarating** | **String** | see [media:rating](https://www.rssboard.org/media-rss#media-rating) (MRSS) | [optional] 
**mediathumbnail** | [**VideosForXMLInnerMediaThumbnail**](VideosForXMLInnerMediaThumbnail.md) |  | [optional] 
**mediatitle** | **String** | see [media:title](https://www.rssboard.org/media-rss#media-title) (MRSS). We only use &#x60;plain&#x60; titles. | [optional] 
**pubDate** | **Date** | video publication date | [optional] 



## Enum: MediaratingEnum


* `nonadult` (value: `"nonadult"`)

* `adult` (value: `"adult"`)





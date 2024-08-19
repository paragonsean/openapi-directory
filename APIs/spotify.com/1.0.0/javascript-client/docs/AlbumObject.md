# SpotifyWebApi.AlbumObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albumType** | **String** | The type of the album.  | 
**availableMarkets** | **[String]** | The markets in which the album is available: [ISO 3166-1 alpha-2 country codes](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). _**NOTE**: an album is considered available in a market when at least 1 of its tracks is available in that market._  | 
**copyrights** | [**[CopyrightObject]**](CopyrightObject.md) | The copyright statements of the album.  | [optional] 
**externalIds** | [**ExternalIdObject**](ExternalIdObject.md) | Known external IDs for the album.  | [optional] 
**externalUrls** | [**ExternalUrlObject**](ExternalUrlObject.md) | Known external URLs for this album.  | 
**genres** | **[String]** | A list of the genres the album is associated with. If not yet classified, the array is empty.  | [optional] 
**href** | **String** | A link to the Web API endpoint providing full details of the album.  | 
**id** | **String** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the album.  | 
**images** | [**[ImageObject]**](ImageObject.md) | The cover art for the album in various sizes, widest first.  | 
**label** | **String** | The label associated with the album.  | [optional] 
**name** | **String** | The name of the album. In case of an album takedown, the value may be an empty string.  | 
**popularity** | **Number** | The popularity of the album. The value will be between 0 and 100, with 100 being the most popular.  | [optional] 
**releaseDate** | **String** | The date the album was first released.  | 
**releaseDatePrecision** | **String** | The precision with which &#x60;release_date&#x60; value is known.  | 
**restrictions** | [**AlbumRestrictionObject**](AlbumRestrictionObject.md) | Included in the response when a content restriction is applied.  | [optional] 
**totalTracks** | **Number** | The number of tracks in the album. | 
**type** | **String** | The object type.  | 
**uri** | **String** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the album.  | 
**artists** | [**[ArtistObject]**](ArtistObject.md) | The artists of the album. Each artist object includes a link in &#x60;href&#x60; to more detailed information about the artist.  | [optional] 
**tracks** | [**PagingSimplifiedTrackObject**](PagingSimplifiedTrackObject.md) |  | [optional] 



## Enum: AlbumTypeEnum


* `album` (value: `"album"`)

* `single` (value: `"single"`)

* `compilation` (value: `"compilation"`)





## Enum: ReleaseDatePrecisionEnum


* `year` (value: `"year"`)

* `month` (value: `"month"`)

* `day` (value: `"day"`)





## Enum: TypeEnum


* `album` (value: `"album"`)





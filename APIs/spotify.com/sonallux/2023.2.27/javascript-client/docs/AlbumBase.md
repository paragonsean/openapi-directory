# SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**albumType** | **String** | The type of the album.  | 
**availableMarkets** | **[String]** | The markets in which the album is available: [ISO 3166-1 alpha-2 country codes](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). _**NOTE**: an album is considered available in a market when at least 1 of its tracks is available in that market._  | 
**externalUrls** | [**ExternalUrlObject**](ExternalUrlObject.md) | Known external URLs for this album.  | 
**href** | **String** | A link to the Web API endpoint providing full details of the album.  | 
**id** | **String** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the album.  | 
**images** | [**[ImageObject]**](ImageObject.md) | The cover art for the album in various sizes, widest first.  | 
**name** | **String** | The name of the album. In case of an album takedown, the value may be an empty string.  | 
**releaseDate** | **String** | The date the album was first released.  | 
**releaseDatePrecision** | **String** | The precision with which &#x60;release_date&#x60; value is known.  | 
**restrictions** | [**AlbumRestrictionObject**](AlbumRestrictionObject.md) | Included in the response when a content restriction is applied.  | [optional] 
**totalTracks** | **Number** | The number of tracks in the album. | 
**type** | **String** | The object type.  | 
**uri** | **String** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the album.  | 



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







# PlaylistTrackObjectTrack

Information about the track or episode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**album** | [**SimplifiedAlbumObject**](SimplifiedAlbumObject.md) | The album on which the track appears. The album object includes a link in &#x60;href&#x60; to full information about the album.  |  [optional] |
|**artists** | [**List&lt;ArtistObject&gt;**](ArtistObject.md) | The artists who performed the track. Each artist object includes a link in &#x60;href&#x60; to more detailed information about the artist.  |  [optional] |
|**availableMarkets** | **List&lt;String&gt;** | A list of the countries in which the track can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.  |  [optional] |
|**discNumber** | **Integer** | The disc number (usually &#x60;1&#x60; unless the album consists of more than one disc).  |  [optional] |
|**durationMs** | **Integer** | The episode length in milliseconds.  |  |
|**explicit** | **Boolean** | Whether or not the episode has explicit content (true &#x3D; yes it does; false &#x3D; no it does not OR unknown).  |  |
|**externalIds** | [**ExternalIdObject**](ExternalIdObject.md) | Known external IDs for the track.  |  [optional] |
|**externalUrls** | [**ExternalUrlObject**](ExternalUrlObject.md) | External URLs for this episode.  |  |
|**href** | **String** | A link to the Web API endpoint providing full details of the episode.  |  |
|**id** | **String** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the episode.  |  |
|**isLocal** | **Boolean** | Whether or not the track is from a local file.  |  [optional] |
|**isPlayable** | **Boolean** | True if the episode is playable in the given market. Otherwise false.  |  |
|**linkedFrom** | [**LinkedTrackObject**](LinkedTrackObject.md) | Part of the response when [Track Relinking](/documentation/web-api/concepts/track-relinking) is applied, and the requested track has been replaced with different track. The track in the &#x60;linked_from&#x60; object contains information about the originally requested track. |  [optional] |
|**name** | **String** | The name of the episode.  |  |
|**popularity** | **Integer** | The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.&lt;br/&gt;The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are.&lt;br/&gt;Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. _**Note**: the popularity value may lag actual popularity by a few days: the value is not updated in real time._  |  [optional] |
|**previewUrl** | **String** | A link to a 30 second preview (MP3 format) of the track. Can be &#x60;null&#x60;  |  [optional] |
|**restrictions** | [**EpisodeRestrictionObject**](EpisodeRestrictionObject.md) | Included in the response when a content restriction is applied.  |  [optional] |
|**trackNumber** | **Integer** | The number of the track. If an album has several discs, the track number is the number on the specified disc.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The object type: \&quot;track\&quot;.  |  |
|**uri** | **String** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the episode.  |  |
|**audioPreviewUrl** | **String** | A URL to a 30 second preview (MP3 format) of the episode. &#x60;null&#x60; if not available.  |  |
|**description** | **String** | A description of the episode. HTML tags are stripped away from this field, use &#x60;html_description&#x60; field in case HTML tags are needed.  |  |
|**htmlDescription** | **String** | A description of the episode. This field may contain HTML tags.  |  |
|**images** | [**List&lt;ImageObject&gt;**](ImageObject.md) | The cover art for the episode in various sizes, widest first.  |  |
|**isExternallyHosted** | **Boolean** | True if the episode is hosted outside of Spotify&#39;s CDN.  |  |
|**language** | **String** | The language used in the episode, identified by a [ISO 639](https://en.wikipedia.org/wiki/ISO_639) code. This field is deprecated and might be removed in the future. Please use the &#x60;languages&#x60; field instead.  |  [optional] |
|**languages** | **List&lt;String&gt;** | A list of the languages used in the episode, identified by their [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639) code.  |  |
|**releaseDate** | **String** | The date the episode was first released, for example &#x60;\&quot;1981-12-15\&quot;&#x60;. Depending on the precision, it might be shown as &#x60;\&quot;1981\&quot;&#x60; or &#x60;\&quot;1981-12\&quot;&#x60;.  |  |
|**releaseDatePrecision** | [**ReleaseDatePrecisionEnum**](#ReleaseDatePrecisionEnum) | The precision with which &#x60;release_date&#x60; value is known.  |  |
|**resumePoint** | [**ResumePointObject**](ResumePointObject.md) | The user&#39;s most recent position in the episode. Set if the supplied access token is a user token and has the scope &#39;user-read-playback-position&#39;.  |  |
|**show** | [**SimplifiedShowObject**](SimplifiedShowObject.md) | The show on which the episode belongs.  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TRACK | &quot;track&quot; |
| EPISODE | &quot;episode&quot; |



## Enum: ReleaseDatePrecisionEnum

| Name | Value |
|---- | -----|
| YEAR | &quot;year&quot; |
| MONTH | &quot;month&quot; |
| DAY | &quot;day&quot; |




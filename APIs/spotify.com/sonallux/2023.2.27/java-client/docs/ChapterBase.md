

# ChapterBase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioPreviewUrl** | **String** | A URL to a 30 second preview (MP3 format) of the episode. &#x60;null&#x60; if not available.  |  |
|**availableMarkets** | **List&lt;String&gt;** | A list of the countries in which the chapter can be played, identified by their [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code.  |  [optional] |
|**chapterNumber** | **Integer** | The number of the chapter  |  |
|**description** | **String** | A description of the episode. HTML tags are stripped away from this field, use &#x60;html_description&#x60; field in case HTML tags are needed.  |  |
|**durationMs** | **Integer** | The episode length in milliseconds.  |  |
|**explicit** | **Boolean** | Whether or not the episode has explicit content (true &#x3D; yes it does; false &#x3D; no it does not OR unknown).  |  |
|**externalUrls** | [**ExternalUrlObject**](ExternalUrlObject.md) | External URLs for this episode.  |  |
|**href** | **String** | A link to the Web API endpoint providing full details of the episode.  |  |
|**htmlDescription** | **String** | A description of the episode. This field may contain HTML tags.  |  |
|**id** | **String** | The [Spotify ID](/documentation/web-api/concepts/spotify-uris-ids) for the episode.  |  |
|**images** | [**List&lt;ImageObject&gt;**](ImageObject.md) | The cover art for the episode in various sizes, widest first.  |  |
|**isPlayable** | **Boolean** | True if the episode is playable in the given market. Otherwise false.  |  |
|**languages** | **List&lt;String&gt;** | A list of the languages used in the episode, identified by their [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639) code.  |  |
|**name** | **String** | The name of the episode.  |  |
|**releaseDate** | **String** | The date the episode was first released, for example &#x60;\&quot;1981-12-15\&quot;&#x60;. Depending on the precision, it might be shown as &#x60;\&quot;1981\&quot;&#x60; or &#x60;\&quot;1981-12\&quot;&#x60;.  |  |
|**releaseDatePrecision** | [**ReleaseDatePrecisionEnum**](#ReleaseDatePrecisionEnum) | The precision with which &#x60;release_date&#x60; value is known.  |  |
|**restrictions** | [**ChapterRestrictionObject**](ChapterRestrictionObject.md) | Included in the response when a content restriction is applied.  |  [optional] |
|**resumePoint** | [**ResumePointObject**](ResumePointObject.md) | The user&#39;s most recent position in the episode. Set if the supplied access token is a user token and has the scope &#39;user-read-playback-position&#39;.  |  |
|**type** | [**TypeEnum**](#TypeEnum) | The object type.  |  |
|**uri** | **String** | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the episode.  |  |



## Enum: ReleaseDatePrecisionEnum

| Name | Value |
|---- | -----|
| YEAR | &quot;year&quot; |
| MONTH | &quot;month&quot; |
| DAY | &quot;day&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EPISODE | &quot;episode&quot; |






# BaseItemDto

This is strictly used as a data transfer object from the api layer.  This holds information about a BaseItem in a format that is convenient for the client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airDays** | **List&lt;DayOfWeek&gt;** | Gets or sets the air days. |  [optional] |
|**airTime** | **String** | Gets or sets the air time. |  [optional] |
|**airsAfterSeasonNumber** | **Integer** |  |  [optional] |
|**airsBeforeEpisodeNumber** | **Integer** |  |  [optional] |
|**airsBeforeSeasonNumber** | **Integer** |  |  [optional] |
|**album** | **String** | Gets or sets the album. |  [optional] |
|**albumArtist** | **String** | Gets or sets the album artist. |  [optional] |
|**albumArtists** | [**List&lt;NameGuidPair&gt;**](NameGuidPair.md) | Gets or sets the album artists. |  [optional] |
|**albumCount** | **Integer** | Gets or sets the album count. |  [optional] |
|**albumId** | **UUID** | Gets or sets the album id. |  [optional] |
|**albumPrimaryImageTag** | **String** | Gets or sets the album image tag. |  [optional] |
|**altitude** | **Double** |  |  [optional] |
|**aperture** | **Double** |  |  [optional] |
|**artistCount** | **Integer** |  |  [optional] |
|**artistItems** | [**List&lt;NameGuidPair&gt;**](NameGuidPair.md) | Gets or sets the artist items. |  [optional] |
|**artists** | **List&lt;String&gt;** | Gets or sets the artists. |  [optional] |
|**aspectRatio** | **String** | Gets or sets the aspect ratio. |  [optional] |
|**audio** | **ProgramAudio** |  |  [optional] |
|**backdropImageTags** | **List&lt;String&gt;** | Gets or sets the backdrop image tags. |  [optional] |
|**cameraMake** | **String** |  |  [optional] |
|**cameraModel** | **String** |  |  [optional] |
|**canDelete** | **Boolean** |  |  [optional] |
|**canDownload** | **Boolean** |  |  [optional] |
|**channelId** | **UUID** | Gets or sets the channel identifier. |  [optional] |
|**channelName** | **String** |  |  [optional] |
|**channelNumber** | **String** |  |  [optional] |
|**channelPrimaryImageTag** | **String** | Gets or sets the channel primary image tag. |  [optional] |
|**channelType** | **ChannelType** |  |  [optional] |
|**chapters** | [**List&lt;ChapterInfo&gt;**](ChapterInfo.md) | Gets or sets the chapters. |  [optional] |
|**childCount** | **Integer** | Gets or sets the child count. |  [optional] |
|**collectionType** | **String** | Gets or sets the type of the collection. |  [optional] |
|**communityRating** | **Float** | Gets or sets the community rating. |  [optional] |
|**completionPercentage** | **Double** | Gets or sets the completion percentage. |  [optional] |
|**container** | **String** |  |  [optional] |
|**criticRating** | **Float** | Gets or sets the critic rating. |  [optional] |
|**cumulativeRunTimeTicks** | **Long** | Gets or sets the cumulative run time ticks. |  [optional] |
|**currentProgram** | [**BaseItemDto**](BaseItemDto.md) |  |  [optional] |
|**customRating** | **String** | Gets or sets the custom rating. |  [optional] |
|**dateCreated** | **OffsetDateTime** | Gets or sets the date created. |  [optional] |
|**dateLastMediaAdded** | **OffsetDateTime** |  |  [optional] |
|**displayOrder** | **String** | Gets or sets the display order. |  [optional] |
|**displayPreferencesId** | **String** | Gets or sets the display preferences id. |  [optional] |
|**enableMediaSourceDisplay** | **Boolean** |  |  [optional] |
|**endDate** | **OffsetDateTime** | Gets or sets the end date. |  [optional] |
|**episodeCount** | **Integer** | Gets or sets the episode count. |  [optional] |
|**episodeTitle** | **String** | Gets or sets the episode title. |  [optional] |
|**etag** | **String** | Gets or sets the etag. |  [optional] |
|**exposureTime** | **Double** |  |  [optional] |
|**externalUrls** | [**List&lt;ExternalUrl&gt;**](ExternalUrl.md) | Gets or sets the external urls. |  [optional] |
|**extraType** | **String** |  |  [optional] |
|**focalLength** | **Double** |  |  [optional] |
|**forcedSortName** | **String** |  |  [optional] |
|**genreItems** | [**List&lt;NameGuidPair&gt;**](NameGuidPair.md) |  |  [optional] |
|**genres** | **List&lt;String&gt;** | Gets or sets the genres. |  [optional] |
|**hasSubtitles** | **Boolean** |  |  [optional] |
|**height** | **Integer** |  |  [optional] |
|**id** | **UUID** | Gets or sets the id. |  [optional] |
|**imageBlurHashes** | [**BaseItemDtoImageBlurHashes**](BaseItemDtoImageBlurHashes.md) |  |  [optional] |
|**imageOrientation** | **ImageOrientation** |  |  [optional] |
|**imageTags** | **Map&lt;String, String&gt;** | Gets or sets the image tags. |  [optional] |
|**indexNumber** | **Integer** | Gets or sets the index number. |  [optional] |
|**indexNumberEnd** | **Integer** | Gets or sets the index number end. |  [optional] |
|**isFolder** | **Boolean** | Gets or sets a value indicating whether this instance is folder. |  [optional] |
|**isHD** | **Boolean** | Gets or sets a value indicating whether this instance is HD. |  [optional] |
|**isKids** | **Boolean** | Gets or sets a value indicating whether this instance is kids. |  [optional] |
|**isLive** | **Boolean** | Gets or sets a value indicating whether this instance is live. |  [optional] |
|**isMovie** | **Boolean** | Gets or sets a value indicating whether this instance is movie. |  [optional] |
|**isNews** | **Boolean** | Gets or sets a value indicating whether this instance is news. |  [optional] |
|**isPlaceHolder** | **Boolean** | Gets or sets a value indicating whether this instance is place holder. |  [optional] |
|**isPremiere** | **Boolean** | Gets or sets a value indicating whether this instance is premiere. |  [optional] |
|**isRepeat** | **Boolean** | Gets or sets a value indicating whether this instance is repeat. |  [optional] |
|**isSeries** | **Boolean** | Gets or sets a value indicating whether this instance is series. |  [optional] |
|**isSports** | **Boolean** | Gets or sets a value indicating whether this instance is sports. |  [optional] |
|**isoSpeedRating** | **Integer** |  |  [optional] |
|**isoType** | **IsoType** |  |  [optional] |
|**latitude** | **Double** |  |  [optional] |
|**localTrailerCount** | **Integer** | Gets or sets the local trailer count. |  [optional] |
|**locationType** | **LocationType** |  |  [optional] |
|**lockData** | **Boolean** | Gets or sets a value indicating whether [enable internet providers]. |  [optional] |
|**lockedFields** | **List&lt;MetadataField&gt;** | Gets or sets the locked fields. |  [optional] |
|**longitude** | **Double** |  |  [optional] |
|**mediaSourceCount** | **Integer** |  |  [optional] |
|**mediaSources** | [**List&lt;MediaSourceInfo&gt;**](MediaSourceInfo.md) | Gets or sets the media versions. |  [optional] |
|**mediaStreams** | [**List&lt;MediaStream&gt;**](MediaStream.md) | Gets or sets the media streams. |  [optional] |
|**mediaType** | **String** | Gets or sets the type of the media. |  [optional] |
|**movieCount** | **Integer** | Gets or sets the movie count. |  [optional] |
|**musicVideoCount** | **Integer** | Gets or sets the music video count. |  [optional] |
|**name** | **String** | Gets or sets the name. |  [optional] |
|**number** | **String** | Gets or sets the number. |  [optional] |
|**officialRating** | **String** | Gets or sets the official rating. |  [optional] |
|**originalTitle** | **String** |  |  [optional] |
|**overview** | **String** | Gets or sets the overview. |  [optional] |
|**parentArtImageTag** | **String** | Gets or sets the parent art image tag. |  [optional] |
|**parentArtItemId** | **String** | If the item does not have a art, this will hold the Id of the Parent that has one. |  [optional] |
|**parentBackdropImageTags** | **List&lt;String&gt;** | Gets or sets the parent backdrop image tags. |  [optional] |
|**parentBackdropItemId** | **String** | If the item does not have any backdrops, this will hold the Id of the Parent that has one. |  [optional] |
|**parentId** | **UUID** | Gets or sets the parent id. |  [optional] |
|**parentIndexNumber** | **Integer** | Gets or sets the parent index number. |  [optional] |
|**parentLogoImageTag** | **String** | Gets or sets the parent logo image tag. |  [optional] |
|**parentLogoItemId** | **String** | If the item does not have a logo, this will hold the Id of the Parent that has one. |  [optional] |
|**parentPrimaryImageItemId** | **String** | Gets or sets the parent primary image item identifier. |  [optional] |
|**parentPrimaryImageTag** | **String** | Gets or sets the parent primary image tag. |  [optional] |
|**parentThumbImageTag** | **String** | Gets or sets the parent thumb image tag. |  [optional] |
|**parentThumbItemId** | **String** | Gets or sets the parent thumb item id. |  [optional] |
|**partCount** | **Integer** | Gets or sets the part count. |  [optional] |
|**path** | **String** | Gets or sets the path. |  [optional] |
|**people** | [**List&lt;BaseItemPerson&gt;**](BaseItemPerson.md) | Gets or sets the people. |  [optional] |
|**playAccess** | **PlayAccess** |  |  [optional] |
|**playlistItemId** | **String** | Gets or sets the playlist item identifier. |  [optional] |
|**preferredMetadataCountryCode** | **String** |  |  [optional] |
|**preferredMetadataLanguage** | **String** |  |  [optional] |
|**premiereDate** | **OffsetDateTime** | Gets or sets the premiere date. |  [optional] |
|**primaryImageAspectRatio** | **Double** | Gets or sets the primary image aspect ratio, after image enhancements. |  [optional] |
|**productionLocations** | **List&lt;String&gt;** |  |  [optional] |
|**productionYear** | **Integer** | Gets or sets the production year. |  [optional] |
|**programCount** | **Integer** |  |  [optional] |
|**programId** | **String** | Gets or sets the program identifier. |  [optional] |
|**providerIds** | **Map&lt;String, String&gt;** | Gets or sets the provider ids. |  [optional] |
|**recursiveItemCount** | **Integer** | Gets or sets the recursive item count. |  [optional] |
|**remoteTrailers** | [**List&lt;MediaUrl&gt;**](MediaUrl.md) | Gets or sets the trailer urls. |  [optional] |
|**runTimeTicks** | **Long** | Gets or sets the run time ticks. |  [optional] |
|**screenshotImageTags** | **List&lt;String&gt;** | Gets or sets the screenshot image tags. |  [optional] |
|**seasonId** | **UUID** | Gets or sets the season identifier. |  [optional] |
|**seasonName** | **String** | Gets or sets the name of the season. |  [optional] |
|**seriesCount** | **Integer** | Gets or sets the series count. |  [optional] |
|**seriesId** | **UUID** | Gets or sets the series id. |  [optional] |
|**seriesName** | **String** | Gets or sets the name of the series. |  [optional] |
|**seriesPrimaryImageTag** | **String** | Gets or sets the series primary image tag. |  [optional] |
|**seriesStudio** | **String** | Gets or sets the series studio. |  [optional] |
|**seriesThumbImageTag** | **String** | Gets or sets the series thumb image tag. |  [optional] |
|**seriesTimerId** | **String** | Gets or sets the series timer identifier. |  [optional] |
|**serverId** | **String** | Gets or sets the server identifier. |  [optional] |
|**shutterSpeed** | **Double** |  |  [optional] |
|**software** | **String** |  |  [optional] |
|**songCount** | **Integer** | Gets or sets the song count. |  [optional] |
|**sortName** | **String** | Gets or sets the name of the sort. |  [optional] |
|**sourceType** | **String** | Gets or sets the type of the source. |  [optional] |
|**specialFeatureCount** | **Integer** | Gets or sets the special feature count. |  [optional] |
|**startDate** | **OffsetDateTime** | The start date of the recording, in UTC. |  [optional] |
|**status** | **String** | Gets or sets the status. |  [optional] |
|**studios** | [**List&lt;NameGuidPair&gt;**](NameGuidPair.md) | Gets or sets the studios. |  [optional] |
|**supportsSync** | **Boolean** | Gets or sets a value indicating whether [supports synchronize]. |  [optional] |
|**taglines** | **List&lt;String&gt;** | Gets or sets the taglines. |  [optional] |
|**tags** | **List&lt;String&gt;** | Gets or sets the tags. |  [optional] |
|**timerId** | **String** | Gets or sets the timer identifier. |  [optional] |
|**trailerCount** | **Integer** | Gets or sets the trailer count. |  [optional] |
|**type** | **String** | Gets or sets the type. |  [optional] |
|**userData** | [**UserItemDataDto**](UserItemDataDto.md) |  |  [optional] |
|**video3DFormat** | **Video3DFormat** |  |  [optional] |
|**videoType** | **VideoType** |  |  [optional] |
|**width** | **Integer** |  |  [optional] |




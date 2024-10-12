# JellyfinApi.GetProgramsDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelIds** | **[String]** | Gets or sets the channels to return guide information for. | [optional] 
**enableImageTypes** | [**[ImageType]**](ImageType.md) | Gets or sets the image types to include in the output.  Optional. | [optional] 
**enableImages** | **Boolean** | Gets or sets include image information in output.  Optional. | [optional] 
**enableTotalRecordCount** | **Boolean** | Gets or sets a value indicating whether retrieve total record count. | [optional] 
**enableUserData** | **Boolean** | Gets or sets include user data.  Optional. | [optional] 
**fields** | [**[ItemFields]**](ItemFields.md) | Gets or sets specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.  Optional. | [optional] 
**genreIds** | **[String]** | Gets or sets the genre ids to return guide information for. | [optional] 
**genres** | **[String]** | Gets or sets the genres to return guide information for. | [optional] 
**hasAired** | **Boolean** | Gets or sets filter by programs that have completed airing, or not.  Optional. | [optional] 
**imageTypeLimit** | **Number** | Gets or sets the max number of images to return, per image type.  Optional. | [optional] 
**isAiring** | **Boolean** | Gets or sets filter by programs that are currently airing, or not.  Optional. | [optional] 
**isKids** | **Boolean** | Gets or sets filter for kids.  Optional. | [optional] 
**isMovie** | **Boolean** | Gets or sets filter for movies.  Optional. | [optional] 
**isNews** | **Boolean** | Gets or sets filter for news.  Optional. | [optional] 
**isSeries** | **Boolean** | Gets or sets filter for series.  Optional. | [optional] 
**isSports** | **Boolean** | Gets or sets filter for sports.  Optional. | [optional] 
**librarySeriesId** | **String** | Gets or sets filter by library series id.  Optional. | [optional] 
**limit** | **Number** | Gets or sets the maximum number of records to return.  Optional. | [optional] 
**maxEndDate** | **Date** | Gets or sets the maximum premiere end date.  Optional. | [optional] 
**maxStartDate** | **Date** | Gets or sets the maximum premiere start date.  Optional. | [optional] 
**minEndDate** | **Date** | Gets or sets the minimum premiere end date.  Optional. | [optional] 
**minStartDate** | **Date** | Gets or sets the minimum premiere start date.  Optional. | [optional] 
**seriesTimerId** | **String** | Gets or sets filter by series timer id.  Optional. | [optional] 
**sortBy** | **String** | Gets or sets specify one or more sort orders, comma delimited. Options: Name, StartDate.  Optional. | [optional] 
**sortOrder** | **String** | Gets or sets sort Order - Ascending,Descending. | [optional] 
**startIndex** | **Number** | Gets or sets the record index to start at. All items with a lower index will be dropped from the results.  Optional. | [optional] 
**userId** | **String** | Gets or sets optional. Filter by user id. | [optional] 



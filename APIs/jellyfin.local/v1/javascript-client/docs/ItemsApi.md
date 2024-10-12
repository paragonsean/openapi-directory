# JellyfinApi.ItemsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getItems**](ItemsApi.md#getItems) | **GET** /Items | Gets items based on a query.
[**getItemsByUserId**](ItemsApi.md#getItemsByUserId) | **GET** /Users/{userId}/Items | Gets items based on a query.
[**getResumeItems**](ItemsApi.md#getResumeItems) | **GET** /Users/{userId}/Items/Resume | Gets items based on a query.



## getItems

> BaseItemDtoQueryResult getItems(opts)

Gets items based on a query.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemsApi();
let opts = {
  'userId': "userId_example", // String | The user id supplied as query parameter.
  'maxOfficialRating': "maxOfficialRating_example", // String | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc).
  'hasThemeSong': true, // Boolean | Optional filter by items with theme songs.
  'hasThemeVideo': true, // Boolean | Optional filter by items with theme videos.
  'hasSubtitles': true, // Boolean | Optional filter by items with subtitles.
  'hasSpecialFeature': true, // Boolean | Optional filter by items with special features.
  'hasTrailer': true, // Boolean | Optional filter by items with trailers.
  'adjacentTo': "adjacentTo_example", // String | Optional. Return items that are siblings of a supplied item.
  'parentIndexNumber': 56, // Number | Optional filter by parent index number.
  'hasParentalRating': true, // Boolean | Optional filter by items that have or do not have a parental rating.
  'isHd': true, // Boolean | Optional filter by items that are HD or not.
  'is4K': true, // Boolean | Optional filter by items that are 4K or not.
  'locationTypes': [new JellyfinApi.LocationType()], // [LocationType] | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimited.
  'excludeLocationTypes': [new JellyfinApi.LocationType()], // [LocationType] | Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimited.
  'isMissing': true, // Boolean | Optional filter by items that are missing episodes or not.
  'isUnaired': true, // Boolean | Optional filter by items that are unaired episodes or not.
  'minCommunityRating': 3.4, // Number | Optional filter by minimum community rating.
  'minCriticRating': 3.4, // Number | Optional filter by minimum critic rating.
  'minPremiereDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum premiere date. Format = ISO.
  'minDateLastSaved': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum last saved date. Format = ISO.
  'minDateLastSavedForUser': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum last saved date for the current user. Format = ISO.
  'maxPremiereDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The maximum premiere date. Format = ISO.
  'hasOverview': true, // Boolean | Optional filter by items that have an overview or not.
  'hasImdbId': true, // Boolean | Optional filter by items that have an imdb id or not.
  'hasTmdbId': true, // Boolean | Optional filter by items that have a tmdb id or not.
  'hasTvdbId': true, // Boolean | Optional filter by items that have a tvdb id or not.
  'excludeItemIds': ["null"], // [String] | Optional. If specified, results will be filtered by excluding item ids. This allows multiple, comma delimited.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'recursive': true, // Boolean | When searching within folders, this determines whether or not the search will be recursive. true/false.
  'searchTerm': "searchTerm_example", // String | Optional. Filter based on a search term.
  'sortOrder': "sortOrder_example", // String | Sort Order - Ascending,Descending.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
  'excludeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited.
  'filters': [new JellyfinApi.ItemFilter()], // [ItemFilter] | Optional. Specify additional filters to apply. This allows multiple, comma delimited. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
  'isFavorite': true, // Boolean | Optional filter by items that are marked as favorite, or not.
  'mediaTypes': ["null"], // [String] | Optional filter by MediaType. Allows multiple, comma delimited.
  'imageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited.
  'sortBy': "sortBy_example", // String | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
  'isPlayed': true, // Boolean | Optional filter by items that are played, or not.
  'genres': ["null"], // [String] | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
  'officialRatings': ["null"], // [String] | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
  'tags': ["null"], // [String] | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
  'years': [null], // [Number] | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
  'enableUserData': true, // Boolean | Optional, include user data.
  'imageTypeLimit': 56, // Number | Optional, the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'person': "person_example", // String | Optional. If specified, results will be filtered to include only those containing the specified person.
  'personIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified person id.
  'personTypes': ["null"], // [String] | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
  'studios': ["null"], // [String] | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
  'artists': ["null"], // [String] | Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimited.
  'excludeArtistIds': ["null"], // [String] | Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimited.
  'artistIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified artist id.
  'albumArtistIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified album artist id.
  'contributingArtistIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified contributing artist id.
  'albums': ["null"], // [String] | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimited.
  'albumIds': ["null"], // [String] | Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimited.
  'ids': ["null"], // [String] | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited.
  'videoTypes': [new JellyfinApi.VideoType()], // [VideoType] | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimited.
  'minOfficialRating': "minOfficialRating_example", // String | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc).
  'isLocked': true, // Boolean | Optional filter by items that are locked.
  'isPlaceHolder': true, // Boolean | Optional filter by items that are placeholders.
  'hasOfficialRating': true, // Boolean | Optional filter by items that have official ratings.
  'collapseBoxSetItems': true, // Boolean | Whether or not to hide items behind their boxsets.
  'minWidth': 56, // Number | Optional. Filter by the minimum width of the item.
  'minHeight': 56, // Number | Optional. Filter by the minimum height of the item.
  'maxWidth': 56, // Number | Optional. Filter by the maximum width of the item.
  'maxHeight': 56, // Number | Optional. Filter by the maximum height of the item.
  'is3D': true, // Boolean | Optional filter by items that are 3D, or not.
  'seriesStatus': [new JellyfinApi.SeriesStatus()], // [SeriesStatus] | Optional filter by Series Status. Allows multiple, comma delimited.
  'nameStartsWithOrGreater': "nameStartsWithOrGreater_example", // String | Optional filter by items whose name is sorted equally or greater than a given input string.
  'nameStartsWith': "nameStartsWith_example", // String | Optional filter by items whose name is sorted equally than a given input string.
  'nameLessThan': "nameLessThan_example", // String | Optional filter by items whose name is equally or lesser than a given input string.
  'studioIds': ["null"], // [String] | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
  'genreIds': ["null"], // [String] | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
  'enableTotalRecordCount': true, // Boolean | Optional. Enable the total record count.
  'enableImages': true // Boolean | Optional, include image information in output.
};
apiInstance.getItems(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The user id supplied as query parameter. | [optional] 
 **maxOfficialRating** | **String**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **hasThemeSong** | **Boolean**| Optional filter by items with theme songs. | [optional] 
 **hasThemeVideo** | **Boolean**| Optional filter by items with theme videos. | [optional] 
 **hasSubtitles** | **Boolean**| Optional filter by items with subtitles. | [optional] 
 **hasSpecialFeature** | **Boolean**| Optional filter by items with special features. | [optional] 
 **hasTrailer** | **Boolean**| Optional filter by items with trailers. | [optional] 
 **adjacentTo** | **String**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **parentIndexNumber** | **Number**| Optional filter by parent index number. | [optional] 
 **hasParentalRating** | **Boolean**| Optional filter by items that have or do not have a parental rating. | [optional] 
 **isHd** | **Boolean**| Optional filter by items that are HD or not. | [optional] 
 **is4K** | **Boolean**| Optional filter by items that are 4K or not. | [optional] 
 **locationTypes** | [**[LocationType]**](LocationType.md)| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimited. | [optional] 
 **excludeLocationTypes** | [**[LocationType]**](LocationType.md)| Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimited. | [optional] 
 **isMissing** | **Boolean**| Optional filter by items that are missing episodes or not. | [optional] 
 **isUnaired** | **Boolean**| Optional filter by items that are unaired episodes or not. | [optional] 
 **minCommunityRating** | **Number**| Optional filter by minimum community rating. | [optional] 
 **minCriticRating** | **Number**| Optional filter by minimum critic rating. | [optional] 
 **minPremiereDate** | **Date**| Optional. The minimum premiere date. Format &#x3D; ISO. | [optional] 
 **minDateLastSaved** | **Date**| Optional. The minimum last saved date. Format &#x3D; ISO. | [optional] 
 **minDateLastSavedForUser** | **Date**| Optional. The minimum last saved date for the current user. Format &#x3D; ISO. | [optional] 
 **maxPremiereDate** | **Date**| Optional. The maximum premiere date. Format &#x3D; ISO. | [optional] 
 **hasOverview** | **Boolean**| Optional filter by items that have an overview or not. | [optional] 
 **hasImdbId** | **Boolean**| Optional filter by items that have an imdb id or not. | [optional] 
 **hasTmdbId** | **Boolean**| Optional filter by items that have a tmdb id or not. | [optional] 
 **hasTvdbId** | **Boolean**| Optional filter by items that have a tvdb id or not. | [optional] 
 **excludeItemIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered by excluding item ids. This allows multiple, comma delimited. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **recursive** | **Boolean**| When searching within folders, this determines whether or not the search will be recursive. true/false. | [optional] 
 **searchTerm** | **String**| Optional. Filter based on a search term. | [optional] 
 **sortOrder** | **String**| Sort Order - Ascending,Descending. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited. | [optional] 
 **filters** | [**[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. This allows multiple, comma delimited. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes. | [optional] 
 **isFavorite** | **Boolean**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **imageTypes** | [**[ImageType]**](ImageType.md)| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sortBy** | **String**| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 
 **isPlayed** | **Boolean**| Optional filter by items that are played, or not. | [optional] 
 **genres** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. | [optional] 
 **officialRatings** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. | [optional] 
 **tags** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. | [optional] 
 **years** | [**[Number]**](Number.md)| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. | [optional] 
 **enableUserData** | **Boolean**| Optional, include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional, the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **person** | **String**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **personIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified person id. | [optional] 
 **personTypes** | [**[String]**](String.md)| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. | [optional] 
 **studios** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. | [optional] 
 **artists** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimited. | [optional] 
 **excludeArtistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimited. | [optional] 
 **artistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified artist id. | [optional] 
 **albumArtistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified album artist id. | [optional] 
 **contributingArtistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified contributing artist id. | [optional] 
 **albums** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimited. | [optional] 
 **albumIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimited. | [optional] 
 **ids** | [**[String]**](String.md)| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **videoTypes** | [**[VideoType]**](VideoType.md)| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimited. | [optional] 
 **minOfficialRating** | **String**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **isLocked** | **Boolean**| Optional filter by items that are locked. | [optional] 
 **isPlaceHolder** | **Boolean**| Optional filter by items that are placeholders. | [optional] 
 **hasOfficialRating** | **Boolean**| Optional filter by items that have official ratings. | [optional] 
 **collapseBoxSetItems** | **Boolean**| Whether or not to hide items behind their boxsets. | [optional] 
 **minWidth** | **Number**| Optional. Filter by the minimum width of the item. | [optional] 
 **minHeight** | **Number**| Optional. Filter by the minimum height of the item. | [optional] 
 **maxWidth** | **Number**| Optional. Filter by the maximum width of the item. | [optional] 
 **maxHeight** | **Number**| Optional. Filter by the maximum height of the item. | [optional] 
 **is3D** | **Boolean**| Optional filter by items that are 3D, or not. | [optional] 
 **seriesStatus** | [**[SeriesStatus]**](SeriesStatus.md)| Optional filter by Series Status. Allows multiple, comma delimited. | [optional] 
 **nameStartsWithOrGreater** | **String**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **nameStartsWith** | **String**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **nameLessThan** | **String**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **studioIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. | [optional] 
 **genreIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Optional. Enable the total record count. | [optional] [default to true]
 **enableImages** | **Boolean**| Optional, include image information in output. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getItemsByUserId

> BaseItemDtoQueryResult getItemsByUserId(userId, opts)

Gets items based on a query.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemsApi();
let userId = "userId_example"; // String | The user id supplied as query parameter.
let opts = {
  'maxOfficialRating': "maxOfficialRating_example", // String | Optional filter by maximum official rating (PG, PG-13, TV-MA, etc).
  'hasThemeSong': true, // Boolean | Optional filter by items with theme songs.
  'hasThemeVideo': true, // Boolean | Optional filter by items with theme videos.
  'hasSubtitles': true, // Boolean | Optional filter by items with subtitles.
  'hasSpecialFeature': true, // Boolean | Optional filter by items with special features.
  'hasTrailer': true, // Boolean | Optional filter by items with trailers.
  'adjacentTo': "adjacentTo_example", // String | Optional. Return items that are siblings of a supplied item.
  'parentIndexNumber': 56, // Number | Optional filter by parent index number.
  'hasParentalRating': true, // Boolean | Optional filter by items that have or do not have a parental rating.
  'isHd': true, // Boolean | Optional filter by items that are HD or not.
  'is4K': true, // Boolean | Optional filter by items that are 4K or not.
  'locationTypes': [new JellyfinApi.LocationType()], // [LocationType] | Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted.
  'excludeLocationTypes': [new JellyfinApi.LocationType()], // [LocationType] | Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimeted.
  'isMissing': true, // Boolean | Optional filter by items that are missing episodes or not.
  'isUnaired': true, // Boolean | Optional filter by items that are unaired episodes or not.
  'minCommunityRating': 3.4, // Number | Optional filter by minimum community rating.
  'minCriticRating': 3.4, // Number | Optional filter by minimum critic rating.
  'minPremiereDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum premiere date. Format = ISO.
  'minDateLastSaved': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum last saved date. Format = ISO.
  'minDateLastSavedForUser': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum last saved date for the current user. Format = ISO.
  'maxPremiereDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The maximum premiere date. Format = ISO.
  'hasOverview': true, // Boolean | Optional filter by items that have an overview or not.
  'hasImdbId': true, // Boolean | Optional filter by items that have an imdb id or not.
  'hasTmdbId': true, // Boolean | Optional filter by items that have a tmdb id or not.
  'hasTvdbId': true, // Boolean | Optional filter by items that have a tvdb id or not.
  'excludeItemIds': ["null"], // [String] | Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'recursive': true, // Boolean | When searching within folders, this determines whether or not the search will be recursive. true/false.
  'searchTerm': "searchTerm_example", // String | Optional. Filter based on a search term.
  'sortOrder': "sortOrder_example", // String | Sort Order - Ascending,Descending.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
  'excludeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimeted.
  'filters': [new JellyfinApi.ItemFilter()], // [ItemFilter] | Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
  'isFavorite': true, // Boolean | Optional filter by items that are marked as favorite, or not.
  'mediaTypes': ["null"], // [String] | Optional filter by MediaType. Allows multiple, comma delimited.
  'imageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited.
  'sortBy': "sortBy_example", // String | Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
  'isPlayed': true, // Boolean | Optional filter by items that are played, or not.
  'genres': ["null"], // [String] | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted.
  'officialRatings': ["null"], // [String] | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted.
  'tags': ["null"], // [String] | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted.
  'years': [null], // [Number] | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted.
  'enableUserData': true, // Boolean | Optional, include user data.
  'imageTypeLimit': 56, // Number | Optional, the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'person': "person_example", // String | Optional. If specified, results will be filtered to include only those containing the specified person.
  'personIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified person id.
  'personTypes': ["null"], // [String] | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
  'studios': ["null"], // [String] | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted.
  'artists': ["null"], // [String] | Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimeted.
  'excludeArtistIds': ["null"], // [String] | Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimeted.
  'artistIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified artist id.
  'albumArtistIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified album artist id.
  'contributingArtistIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified contributing artist id.
  'albums': ["null"], // [String] | Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted.
  'albumIds': ["null"], // [String] | Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimeted.
  'ids': ["null"], // [String] | Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited.
  'videoTypes': [new JellyfinApi.VideoType()], // [VideoType] | Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted.
  'minOfficialRating': "minOfficialRating_example", // String | Optional filter by minimum official rating (PG, PG-13, TV-MA, etc).
  'isLocked': true, // Boolean | Optional filter by items that are locked.
  'isPlaceHolder': true, // Boolean | Optional filter by items that are placeholders.
  'hasOfficialRating': true, // Boolean | Optional filter by items that have official ratings.
  'collapseBoxSetItems': true, // Boolean | Whether or not to hide items behind their boxsets.
  'minWidth': 56, // Number | Optional. Filter by the minimum width of the item.
  'minHeight': 56, // Number | Optional. Filter by the minimum height of the item.
  'maxWidth': 56, // Number | Optional. Filter by the maximum width of the item.
  'maxHeight': 56, // Number | Optional. Filter by the maximum height of the item.
  'is3D': true, // Boolean | Optional filter by items that are 3D, or not.
  'seriesStatus': [new JellyfinApi.SeriesStatus()], // [SeriesStatus] | Optional filter by Series Status. Allows multiple, comma delimeted.
  'nameStartsWithOrGreater': "nameStartsWithOrGreater_example", // String | Optional filter by items whose name is sorted equally or greater than a given input string.
  'nameStartsWith': "nameStartsWith_example", // String | Optional filter by items whose name is sorted equally than a given input string.
  'nameLessThan': "nameLessThan_example", // String | Optional filter by items whose name is equally or lesser than a given input string.
  'studioIds': ["null"], // [String] | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimeted.
  'genreIds': ["null"], // [String] | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimeted.
  'enableTotalRecordCount': true, // Boolean | Optional. Enable the total record count.
  'enableImages': true // Boolean | Optional, include image information in output.
};
apiInstance.getItemsByUserId(userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The user id supplied as query parameter. | 
 **maxOfficialRating** | **String**| Optional filter by maximum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **hasThemeSong** | **Boolean**| Optional filter by items with theme songs. | [optional] 
 **hasThemeVideo** | **Boolean**| Optional filter by items with theme videos. | [optional] 
 **hasSubtitles** | **Boolean**| Optional filter by items with subtitles. | [optional] 
 **hasSpecialFeature** | **Boolean**| Optional filter by items with special features. | [optional] 
 **hasTrailer** | **Boolean**| Optional filter by items with trailers. | [optional] 
 **adjacentTo** | **String**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **parentIndexNumber** | **Number**| Optional filter by parent index number. | [optional] 
 **hasParentalRating** | **Boolean**| Optional filter by items that have or do not have a parental rating. | [optional] 
 **isHd** | **Boolean**| Optional filter by items that are HD or not. | [optional] 
 **is4K** | **Boolean**| Optional filter by items that are 4K or not. | [optional] 
 **locationTypes** | [**[LocationType]**](LocationType.md)| Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted. | [optional] 
 **excludeLocationTypes** | [**[LocationType]**](LocationType.md)| Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimeted. | [optional] 
 **isMissing** | **Boolean**| Optional filter by items that are missing episodes or not. | [optional] 
 **isUnaired** | **Boolean**| Optional filter by items that are unaired episodes or not. | [optional] 
 **minCommunityRating** | **Number**| Optional filter by minimum community rating. | [optional] 
 **minCriticRating** | **Number**| Optional filter by minimum critic rating. | [optional] 
 **minPremiereDate** | **Date**| Optional. The minimum premiere date. Format &#x3D; ISO. | [optional] 
 **minDateLastSaved** | **Date**| Optional. The minimum last saved date. Format &#x3D; ISO. | [optional] 
 **minDateLastSavedForUser** | **Date**| Optional. The minimum last saved date for the current user. Format &#x3D; ISO. | [optional] 
 **maxPremiereDate** | **Date**| Optional. The maximum premiere date. Format &#x3D; ISO. | [optional] 
 **hasOverview** | **Boolean**| Optional filter by items that have an overview or not. | [optional] 
 **hasImdbId** | **Boolean**| Optional filter by items that have an imdb id or not. | [optional] 
 **hasTmdbId** | **Boolean**| Optional filter by items that have a tmdb id or not. | [optional] 
 **hasTvdbId** | **Boolean**| Optional filter by items that have a tvdb id or not. | [optional] 
 **excludeItemIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **recursive** | **Boolean**| When searching within folders, this determines whether or not the search will be recursive. true/false. | [optional] 
 **searchTerm** | **String**| Optional. Filter based on a search term. | [optional] 
 **sortOrder** | **String**| Sort Order - Ascending,Descending. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimeted. | [optional] 
 **filters** | [**[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes. | [optional] 
 **isFavorite** | **Boolean**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **imageTypes** | [**[ImageType]**](ImageType.md)| Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited. | [optional] 
 **sortBy** | **String**| Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 
 **isPlayed** | **Boolean**| Optional filter by items that are played, or not. | [optional] 
 **genres** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted. | [optional] 
 **officialRatings** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted. | [optional] 
 **tags** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted. | [optional] 
 **years** | [**[Number]**](Number.md)| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted. | [optional] 
 **enableUserData** | **Boolean**| Optional, include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional, the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **person** | **String**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **personIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified person id. | [optional] 
 **personTypes** | [**[String]**](String.md)| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. | [optional] 
 **studios** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted. | [optional] 
 **artists** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimeted. | [optional] 
 **excludeArtistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimeted. | [optional] 
 **artistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified artist id. | [optional] 
 **albumArtistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified album artist id. | [optional] 
 **contributingArtistIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified contributing artist id. | [optional] 
 **albums** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted. | [optional] 
 **albumIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimeted. | [optional] 
 **ids** | [**[String]**](String.md)| Optional. If specific items are needed, specify a list of item id&#39;s to retrieve. This allows multiple, comma delimited. | [optional] 
 **videoTypes** | [**[VideoType]**](VideoType.md)| Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted. | [optional] 
 **minOfficialRating** | **String**| Optional filter by minimum official rating (PG, PG-13, TV-MA, etc). | [optional] 
 **isLocked** | **Boolean**| Optional filter by items that are locked. | [optional] 
 **isPlaceHolder** | **Boolean**| Optional filter by items that are placeholders. | [optional] 
 **hasOfficialRating** | **Boolean**| Optional filter by items that have official ratings. | [optional] 
 **collapseBoxSetItems** | **Boolean**| Whether or not to hide items behind their boxsets. | [optional] 
 **minWidth** | **Number**| Optional. Filter by the minimum width of the item. | [optional] 
 **minHeight** | **Number**| Optional. Filter by the minimum height of the item. | [optional] 
 **maxWidth** | **Number**| Optional. Filter by the maximum width of the item. | [optional] 
 **maxHeight** | **Number**| Optional. Filter by the maximum height of the item. | [optional] 
 **is3D** | **Boolean**| Optional filter by items that are 3D, or not. | [optional] 
 **seriesStatus** | [**[SeriesStatus]**](SeriesStatus.md)| Optional filter by Series Status. Allows multiple, comma delimeted. | [optional] 
 **nameStartsWithOrGreater** | **String**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **nameStartsWith** | **String**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **nameLessThan** | **String**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **studioIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimeted. | [optional] 
 **genreIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimeted. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Optional. Enable the total record count. | [optional] [default to true]
 **enableImages** | **Boolean**| Optional, include image information in output. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getResumeItems

> BaseItemDtoQueryResult getResumeItems(userId, opts)

Gets items based on a query.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemsApi();
let userId = "userId_example"; // String | The user id.
let opts = {
  'startIndex': 56, // Number | The start index.
  'limit': 56, // Number | The item limit.
  'searchTerm': "searchTerm_example", // String | The search term.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
  'mediaTypes': ["null"], // [String] | Optional. Filter by MediaType. Allows multiple, comma delimited.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'excludeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited.
  'enableTotalRecordCount': true, // Boolean | Optional. Enable the total record count.
  'enableImages': true // Boolean | Optional. Include image information in output.
};
apiInstance.getResumeItems(userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| The user id. | 
 **startIndex** | **Number**| The start index. | [optional] 
 **limit** | **Number**| The item limit. | [optional] 
 **searchTerm** | **String**| The search term. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| Optional. Filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Optional. Enable the total record count. | [optional] [default to true]
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


# GeodesystemsCom443.TypeTmdbmoviesApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchTmdbmovies**](TypeTmdbmoviesApi.md#searchTmdbmovies) | **GET** /repository/search/type/tmdbmovies | Search API for &#39;Tmdb Movies&#39; entry type



## searchTmdbmovies

> searchTmdbmovies(opts)

Search API for &#39;Tmdb Movies&#39; entry type

API to search for entries of type Tmdb Movies

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeTmdbmoviesApi();
let opts = {
  'text': "text_example", // String | Search text
  'name': "name_example", // String | Search name
  'description': "description_example", // String | Search description
  'fromdate': new Date("2013-10-20T19:20:30+01:00"), // Date | From date
  'todate': new Date("2013-10-20T19:20:30+01:00"), // Date | To date
  'createdateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date from
  'createdateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date to
  'changedateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date from
  'changedateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date to
  'group': "group_example", // String | Parent entry
  'filesuffix': "filesuffix_example", // String | File suffix
  'maxlatitude': 3.4, // Number | Northern bounds of search
  'minlongitude': 3.4, // Number | Western bounds of search
  'minlatitude': 3.4, // Number | Southern bounds of search
  'maxlongitude': 3.4, // Number | Eastern bounds of search
  'max': 56, // Number | Max number of results
  'skip': 56, // Number | Number to skip
  'searchDbTmdbmoviesOriginalTitle': "searchDbTmdbmoviesOriginalTitle_example", // String | Original Title
  'searchDbTmdbmoviesOverview': "searchDbTmdbmoviesOverview_example", // String | Overview
  'searchDbTmdbmoviesBudget': 3.4, // Number | Budget
  'searchDbTmdbmoviesGenres': "searchDbTmdbmoviesGenres_example", // String | Genres
  'searchDbTmdbmoviesHomepage': "searchDbTmdbmoviesHomepage_example", // String | Homepage
  'searchDbTmdbmoviesMovieId': "searchDbTmdbmoviesMovieId_example", // String | Id
  'searchDbTmdbmoviesKeywords': "searchDbTmdbmoviesKeywords_example", // String | Keywords
  'searchDbTmdbmoviesOriginalLanguage': "searchDbTmdbmoviesOriginalLanguage_example", // String | Original Language
  'searchDbTmdbmoviesPopularity': 3.4, // Number | Popularity
  'searchDbTmdbmoviesProductionCompanies': "searchDbTmdbmoviesProductionCompanies_example", // String | Production Companies
  'searchDbTmdbmoviesProductionCountries': "searchDbTmdbmoviesProductionCountries_example", // String | Production Countries
  'searchDbTmdbmoviesReleaseDate': "searchDbTmdbmoviesReleaseDate_example", // String | Release Date
  'searchDbTmdbmoviesRevenue': 3.4, // Number | Revenue
  'searchDbTmdbmoviesRuntime': 3.4, // Number | Runtime
  'searchDbTmdbmoviesSpokenLanguages': "searchDbTmdbmoviesSpokenLanguages_example", // String | Spoken Languages
  'searchDbTmdbmoviesStatus': "searchDbTmdbmoviesStatus_example", // String | Status
  'searchDbTmdbmoviesTagline': "searchDbTmdbmoviesTagline_example", // String | Tagline
  'searchDbTmdbmoviesTitle': "searchDbTmdbmoviesTitle_example", // String | Title
  'searchDbTmdbmoviesVoteAverage': 3.4, // Number | Vote Average
  'searchDbTmdbmoviesVoteCount': 3.4 // Number | Vote Count
};
apiInstance.searchTmdbmovies(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Search text | [optional] 
 **name** | **String**| Search name | [optional] 
 **description** | **String**| Search description | [optional] 
 **fromdate** | **Date**| From date | [optional] 
 **todate** | **Date**| To date | [optional] 
 **createdateFrom** | **Date**| Archive create date from | [optional] 
 **createdateTo** | **Date**| Archive create date to | [optional] 
 **changedateFrom** | **Date**| Archive change date from | [optional] 
 **changedateTo** | **Date**| Archive change date to | [optional] 
 **group** | **String**| Parent entry | [optional] 
 **filesuffix** | **String**| File suffix | [optional] 
 **maxlatitude** | **Number**| Northern bounds of search | [optional] 
 **minlongitude** | **Number**| Western bounds of search | [optional] 
 **minlatitude** | **Number**| Southern bounds of search | [optional] 
 **maxlongitude** | **Number**| Eastern bounds of search | [optional] 
 **max** | **Number**| Max number of results | [optional] 
 **skip** | **Number**| Number to skip | [optional] 
 **searchDbTmdbmoviesOriginalTitle** | **String**| Original Title | [optional] 
 **searchDbTmdbmoviesOverview** | **String**| Overview | [optional] 
 **searchDbTmdbmoviesBudget** | **Number**| Budget | [optional] 
 **searchDbTmdbmoviesGenres** | **String**| Genres | [optional] 
 **searchDbTmdbmoviesHomepage** | **String**| Homepage | [optional] 
 **searchDbTmdbmoviesMovieId** | **String**| Id | [optional] 
 **searchDbTmdbmoviesKeywords** | **String**| Keywords | [optional] 
 **searchDbTmdbmoviesOriginalLanguage** | **String**| Original Language | [optional] 
 **searchDbTmdbmoviesPopularity** | **Number**| Popularity | [optional] 
 **searchDbTmdbmoviesProductionCompanies** | **String**| Production Companies | [optional] 
 **searchDbTmdbmoviesProductionCountries** | **String**| Production Countries | [optional] 
 **searchDbTmdbmoviesReleaseDate** | **String**| Release Date | [optional] 
 **searchDbTmdbmoviesRevenue** | **Number**| Revenue | [optional] 
 **searchDbTmdbmoviesRuntime** | **Number**| Runtime | [optional] 
 **searchDbTmdbmoviesSpokenLanguages** | **String**| Spoken Languages | [optional] 
 **searchDbTmdbmoviesStatus** | **String**| Status | [optional] 
 **searchDbTmdbmoviesTagline** | **String**| Tagline | [optional] 
 **searchDbTmdbmoviesTitle** | **String**| Title | [optional] 
 **searchDbTmdbmoviesVoteAverage** | **Number**| Vote Average | [optional] 
 **searchDbTmdbmoviesVoteCount** | **Number**| Vote Count | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


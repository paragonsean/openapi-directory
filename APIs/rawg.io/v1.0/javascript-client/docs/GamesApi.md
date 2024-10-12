# RawgVideoGamesDatabaseApi.GamesApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gamesAchievementsRead**](GamesApi.md#gamesAchievementsRead) | **GET** /games/{id}/achievements | Get a list of game achievements.
[**gamesAdditionsList**](GamesApi.md#gamesAdditionsList) | **GET** /games/{game_pk}/additions | Get a list of DLC&#39;s for the game, GOTY and other editions, companion apps, etc.
[**gamesDevelopmentTeamList**](GamesApi.md#gamesDevelopmentTeamList) | **GET** /games/{game_pk}/development-team | Get a list of individual creators that were part of the development team.
[**gamesGameSeriesList**](GamesApi.md#gamesGameSeriesList) | **GET** /games/{game_pk}/game-series | Get a list of games that are part of the same series.
[**gamesList**](GamesApi.md#gamesList) | **GET** /games | Get a list of games.
[**gamesMoviesRead**](GamesApi.md#gamesMoviesRead) | **GET** /games/{id}/movies | Get a list of game trailers.
[**gamesParentGamesList**](GamesApi.md#gamesParentGamesList) | **GET** /games/{game_pk}/parent-games | Get a list of parent games for DLC&#39;s and editions.
[**gamesRead**](GamesApi.md#gamesRead) | **GET** /games/{id} | Get details of the game.
[**gamesRedditRead**](GamesApi.md#gamesRedditRead) | **GET** /games/{id}/reddit | Get a list of most recent posts from the game&#39;s subreddit.
[**gamesScreenshotsList**](GamesApi.md#gamesScreenshotsList) | **GET** /games/{game_pk}/screenshots | Get screenshots for the game.
[**gamesStoresList**](GamesApi.md#gamesStoresList) | **GET** /games/{game_pk}/stores | Get links to the stores that sell the game.
[**gamesSuggestedRead**](GamesApi.md#gamesSuggestedRead) | **GET** /games/{id}/suggested | Get a list of visually similar games, available only for business and enterprise API users.
[**gamesTwitchRead**](GamesApi.md#gamesTwitchRead) | **GET** /games/{id}/twitch | Get streams on Twitch associated with the game, available only for business and enterprise API users.
[**gamesYoutubeRead**](GamesApi.md#gamesYoutubeRead) | **GET** /games/{id}/youtube | Get videos from YouTube associated with the game, available only for business and enterprise API users.



## gamesAchievementsRead

> ParentAchievement gamesAchievementsRead(id)

Get a list of game achievements.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let id = "id_example"; // String | An ID or a slug identifying this Game.
apiInstance.gamesAchievementsRead(id, (error, data, response) => {
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
 **id** | **String**| An ID or a slug identifying this Game. | 

### Return type

[**ParentAchievement**](ParentAchievement.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesAdditionsList

> GamesList200Response gamesAdditionsList(gamePk, opts)

Get a list of DLC&#39;s for the game, GOTY and other editions, companion apps, etc.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let gamePk = "gamePk_example"; // String | 
let opts = {
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.gamesAdditionsList(gamePk, opts, (error, data, response) => {
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
 **gamePk** | **String**|  | 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**GamesList200Response**](GamesList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesDevelopmentTeamList

> GamesDevelopmentTeamList200Response gamesDevelopmentTeamList(gamePk, opts)

Get a list of individual creators that were part of the development team.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let gamePk = "gamePk_example"; // String | 
let opts = {
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.gamesDevelopmentTeamList(gamePk, opts, (error, data, response) => {
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
 **gamePk** | **String**|  | 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**GamesDevelopmentTeamList200Response**](GamesDevelopmentTeamList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesGameSeriesList

> GamesList200Response gamesGameSeriesList(gamePk, opts)

Get a list of games that are part of the same series.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let gamePk = "gamePk_example"; // String | 
let opts = {
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.gamesGameSeriesList(gamePk, opts, (error, data, response) => {
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
 **gamePk** | **String**|  | 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**GamesList200Response**](GamesList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesList

> GamesList200Response gamesList(opts)

Get a list of games.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let opts = {
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56, // Number | Number of results to return per page.
  'search': "search_example", // String | Search query.
  'searchPrecise': true, // Boolean | Disable fuzziness for the search query.
  'searchExact': true, // Boolean | Mark the search query as exact.
  'parentPlatforms': "parentPlatforms_example", // String | Filter by parent platforms, for example: `1,2,3`.
  'platforms': "platforms_example", // String | Filter by platforms, for example: `4,5`.
  'stores': "stores_example", // String | Filter by stores, for example: `5,6`.
  'developers': "developers_example", // String | Filter by developers, for example: `1612,18893` or `valve-software,feral-interactive`.
  'publishers': "publishers_example", // String | Filter by publishers, for example: `354,20987` or `electronic-arts,microsoft-studios`.
  'genres': "genres_example", // String | Filter by genres, for example: `4,51` or `action,indie`.
  'tags': "tags_example", // String | Filter by tags, for example: `31,7` or `singleplayer,multiplayer`.
  'creators': "creators_example", // String | Filter by creators, for example: `78,28` or `cris-velasco,mike-morasky`.
  'dates': "dates_example", // String | Filter by a release date, for example: `2010-01-01,2018-12-31.1960-01-01,1969-12-31`.
  'updated': "updated_example", // String | Filter by an update date, for example: `2020-12-01,2020-12-31`.
  'platformsCount': 56, // Number | Filter by platforms count, for example: `1`.
  'metacritic': "metacritic_example", // String | Filter by a metacritic rating, for example: `80,100`.
  'excludeCollection': 56, // Number | Exclude games from a particular collection, for example: `123`.
  'excludeAdditions': true, // Boolean | Exclude additions.
  'excludeParents': true, // Boolean | Exclude games which have additions.
  'excludeGameSeries': true, // Boolean | Exclude games which included in a game series.
  'excludeStores': "excludeStores_example", // String | Exclude stores, for example: `5,6`.
  'ordering': "ordering_example" // String | Available fields: `name`, `released`, `added`, `created`, `updated`, `rating`, `metacritic`. You can reverse the sort order adding a hyphen, for example: `-released`.
};
apiInstance.gamesList(opts, (error, data, response) => {
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
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 
 **search** | **String**| Search query. | [optional] 
 **searchPrecise** | **Boolean**| Disable fuzziness for the search query. | [optional] 
 **searchExact** | **Boolean**| Mark the search query as exact. | [optional] 
 **parentPlatforms** | **String**| Filter by parent platforms, for example: &#x60;1,2,3&#x60;. | [optional] 
 **platforms** | **String**| Filter by platforms, for example: &#x60;4,5&#x60;. | [optional] 
 **stores** | **String**| Filter by stores, for example: &#x60;5,6&#x60;. | [optional] 
 **developers** | **String**| Filter by developers, for example: &#x60;1612,18893&#x60; or &#x60;valve-software,feral-interactive&#x60;. | [optional] 
 **publishers** | **String**| Filter by publishers, for example: &#x60;354,20987&#x60; or &#x60;electronic-arts,microsoft-studios&#x60;. | [optional] 
 **genres** | **String**| Filter by genres, for example: &#x60;4,51&#x60; or &#x60;action,indie&#x60;. | [optional] 
 **tags** | **String**| Filter by tags, for example: &#x60;31,7&#x60; or &#x60;singleplayer,multiplayer&#x60;. | [optional] 
 **creators** | **String**| Filter by creators, for example: &#x60;78,28&#x60; or &#x60;cris-velasco,mike-morasky&#x60;. | [optional] 
 **dates** | **String**| Filter by a release date, for example: &#x60;2010-01-01,2018-12-31.1960-01-01,1969-12-31&#x60;. | [optional] 
 **updated** | **String**| Filter by an update date, for example: &#x60;2020-12-01,2020-12-31&#x60;. | [optional] 
 **platformsCount** | **Number**| Filter by platforms count, for example: &#x60;1&#x60;. | [optional] 
 **metacritic** | **String**| Filter by a metacritic rating, for example: &#x60;80,100&#x60;. | [optional] 
 **excludeCollection** | **Number**| Exclude games from a particular collection, for example: &#x60;123&#x60;. | [optional] 
 **excludeAdditions** | **Boolean**| Exclude additions. | [optional] 
 **excludeParents** | **Boolean**| Exclude games which have additions. | [optional] 
 **excludeGameSeries** | **Boolean**| Exclude games which included in a game series. | [optional] 
 **excludeStores** | **String**| Exclude stores, for example: &#x60;5,6&#x60;. | [optional] 
 **ordering** | **String**| Available fields: &#x60;name&#x60;, &#x60;released&#x60;, &#x60;added&#x60;, &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;rating&#x60;, &#x60;metacritic&#x60;. You can reverse the sort order adding a hyphen, for example: &#x60;-released&#x60;. | [optional] 

### Return type

[**GamesList200Response**](GamesList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesMoviesRead

> Movie gamesMoviesRead(id)

Get a list of game trailers.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let id = "id_example"; // String | An ID or a slug identifying this Game.
apiInstance.gamesMoviesRead(id, (error, data, response) => {
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
 **id** | **String**| An ID or a slug identifying this Game. | 

### Return type

[**Movie**](Movie.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesParentGamesList

> GamesList200Response gamesParentGamesList(gamePk, opts)

Get a list of parent games for DLC&#39;s and editions.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let gamePk = "gamePk_example"; // String | 
let opts = {
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.gamesParentGamesList(gamePk, opts, (error, data, response) => {
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
 **gamePk** | **String**|  | 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**GamesList200Response**](GamesList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesRead

> GameSingle gamesRead(id)

Get details of the game.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let id = "id_example"; // String | An ID or a slug identifying this Game.
apiInstance.gamesRead(id, (error, data, response) => {
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
 **id** | **String**| An ID or a slug identifying this Game. | 

### Return type

[**GameSingle**](GameSingle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesRedditRead

> Reddit gamesRedditRead(id)

Get a list of most recent posts from the game&#39;s subreddit.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let id = "id_example"; // String | An ID or a slug identifying this Game.
apiInstance.gamesRedditRead(id, (error, data, response) => {
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
 **id** | **String**| An ID or a slug identifying this Game. | 

### Return type

[**Reddit**](Reddit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesScreenshotsList

> GamesScreenshotsList200Response gamesScreenshotsList(gamePk, opts)

Get screenshots for the game.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let gamePk = "gamePk_example"; // String | 
let opts = {
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.gamesScreenshotsList(gamePk, opts, (error, data, response) => {
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
 **gamePk** | **String**|  | 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**GamesScreenshotsList200Response**](GamesScreenshotsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesStoresList

> GamesStoresList200Response gamesStoresList(gamePk, opts)

Get links to the stores that sell the game.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let gamePk = "gamePk_example"; // String | 
let opts = {
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.gamesStoresList(gamePk, opts, (error, data, response) => {
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
 **gamePk** | **String**|  | 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**GamesStoresList200Response**](GamesStoresList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesSuggestedRead

> GameSingle gamesSuggestedRead(id)

Get a list of visually similar games, available only for business and enterprise API users.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let id = "id_example"; // String | An ID or a slug identifying this Game.
apiInstance.gamesSuggestedRead(id, (error, data, response) => {
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
 **id** | **String**| An ID or a slug identifying this Game. | 

### Return type

[**GameSingle**](GameSingle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesTwitchRead

> Twitch gamesTwitchRead(id)

Get streams on Twitch associated with the game, available only for business and enterprise API users.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let id = "id_example"; // String | An ID or a slug identifying this Game.
apiInstance.gamesTwitchRead(id, (error, data, response) => {
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
 **id** | **String**| An ID or a slug identifying this Game. | 

### Return type

[**Twitch**](Twitch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gamesYoutubeRead

> Youtube gamesYoutubeRead(id)

Get videos from YouTube associated with the game, available only for business and enterprise API users.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GamesApi();
let id = "id_example"; // String | An ID or a slug identifying this Game.
apiInstance.gamesYoutubeRead(id, (error, data, response) => {
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
 **id** | **String**| An ID or a slug identifying this Game. | 

### Return type

[**Youtube**](Youtube.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


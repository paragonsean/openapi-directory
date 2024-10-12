# Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actorGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#actorGet) | **GET** /Actors/Search/{accesstoken}/{Query} | Returns data on queried actor/actress. Result set limited to 5 records
[**actorInShowsGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#actorInShowsGet) | **GET** /Cast/ActorBySearch/{AccessToken}/{Actor} | Returns all shows queried actor/actress is or has been in
[**actorsInTVShowGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#actorsInTVShowGet) | **GET** /Cast/ByTVShow/{accesstoken}/{ShowName} | Returns all actors in queried tvshow
[**addActorPost**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#addActorPost) | **POST** /AddActor | Add new actor or actress to database
[**castByActorGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#castByActorGet) | **GET** /Cast/ByActor/{AccessToken}/{Actor} | Returns list of show actor is appearing in
[**crewByIDGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewByIDGet) | **GET** /Crew/ByID/{AccessToken}/{ID} | Get crew list by ID
[**crewByPersonGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewByPersonGet) | **GET** /Crew/ByPerson/{AccessToken}/{PersonName} | Gets list of productions searched person is/was involved in.
[**crewGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewGet) | **GET** /Crew/Search/{AccessToken}/{Phrase} | Returns crew for queried show.
[**crewbyShownameGet**](CastCrewCastCrewInMoviesTelevisionShowsApi.md#crewbyShownameGet) | **GET** /Crew/ByShowName/{AccessToken}/{ShowName} | Get crew list by showname



## actorGet

> [Actor] actorGet(accesstoken, query)

Returns data on queried actor/actress. Result set limited to 5 records

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accesstoken = "accesstoken_example"; // String | 
let query = "query_example"; // String | 
apiInstance.actorGet(accesstoken, query, (error, data, response) => {
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
 **accesstoken** | **String**|  | 
 **query** | **String**|  | 

### Return type

[**[Actor]**](Actor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## actorInShowsGet

> [TVShowActor] actorInShowsGet(accessToken, actor)

Returns all shows queried actor/actress is or has been in

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let actor = "actor_example"; // String | Part of, or full name of actor
apiInstance.actorInShowsGet(accessToken, actor, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **actor** | **String**| Part of, or full name of actor | 

### Return type

[**[TVShowActor]**](TVShowActor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## actorsInTVShowGet

> [TVShowActor] actorsInTVShowGet(accesstoken, showName)

Returns all actors in queried tvshow

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accesstoken = "accesstoken_example"; // String | 
let showName = "showName_example"; // String | 
apiInstance.actorsInTVShowGet(accesstoken, showName, (error, data, response) => {
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
 **accesstoken** | **String**|  | 
 **showName** | **String**|  | 

### Return type

[**[TVShowActor]**](TVShowActor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## addActorPost

> PostResult addActorPost(value)

Add new actor or actress to database

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let value = new Shinobiapi.ActorPost(); // ActorPost | 
apiInstance.addActorPost(value, (error, data, response) => {
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
 **value** | [**ActorPost**](ActorPost.md)|  | 

### Return type

[**PostResult**](PostResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## castByActorGet

> [TVShowActor] castByActorGet(accessToken, actor)

Returns list of show actor is appearing in

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let actor = "actor_example"; // String | Full name of actor
apiInstance.castByActorGet(accessToken, actor, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **actor** | **String**| Full name of actor | 

### Return type

[**[TVShowActor]**](TVShowActor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## crewByIDGet

> [Crew] crewByIDGet(accessToken, ID)

Get crew list by ID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let ID = "ID_example"; // String | IMDBID, TVmazeID, or TVDBID
apiInstance.crewByIDGet(accessToken, ID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **ID** | **String**| IMDBID, TVmazeID, or TVDBID | 

### Return type

[**[Crew]**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## crewByPersonGet

> [Crew] crewByPersonGet(accessToken, personName)

Gets list of productions searched person is/was involved in.

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let personName = "personName_example"; // String | 
apiInstance.crewByPersonGet(accessToken, personName, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **personName** | **String**|  | 

### Return type

[**[Crew]**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## crewGet

> [Crew] crewGet(accessToken, phrase)

Returns crew for queried show.

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let phrase = "phrase_example"; // String | Part of, or full showname to search for
apiInstance.crewGet(accessToken, phrase, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **phrase** | **String**| Part of, or full showname to search for | 

### Return type

[**[Crew]**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## crewbyShownameGet

> [Crew] crewbyShownameGet(accessToken, showName)

Get crew list by showname

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.CastCrewCastCrewInMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let showName = "showName_example"; // String | Full exact showname
apiInstance.crewbyShownameGet(accessToken, showName, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **showName** | **String**| Full exact showname | 

### Return type

[**[Crew]**](Crew.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


# PandaScoreRestApiForAllVideogames.IncidentsApi

All URIs are relative to *https://api.pandascore.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAdditions**](IncidentsApi.md#getAdditions) | **GET** /additions | List additions
[**getChanges**](IncidentsApi.md#getChanges) | **GET** /changes | List changes
[**getDeletions**](IncidentsApi.md#getDeletions) | **GET** /deletions | List deletions
[**getIncidents**](IncidentsApi.md#getIncidents) | **GET** /incidents | List changes, additions and deletions



## getAdditions

> [NonDeletionIncident] getAdditions(opts)

List additions

Get the latest additions.  This endpoint only shows unchanged objects.

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.IncidentsApi();
let opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5, // Number | Equivalent to `page[size]`
  'type': ["null"], // [String] | Filter by result type(s)
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out older results
  'videogame': [new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug()] // [VideogameIDOrSlug] | Filter by videogame(s)
};
apiInstance.getAdditions(opts, (error, data, response) => {
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
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]
 **type** | [**[String]**](String.md)| Filter by result type(s) | [optional] 
 **since** | **Date**| Filter out older results | [optional] 
 **videogame** | [**[VideogameIDOrSlug]**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] 

### Return type

[**[NonDeletionIncident]**](NonDeletionIncident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChanges

> [Incident] getChanges(opts)

List changes

Get the latest updates.  This endpoint only provides the latest change for an object. It does not keep track of previous changes.

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.IncidentsApi();
let opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5, // Number | Equivalent to `page[size]`
  'type': ["null"], // [String] | Filter by result type(s)
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out older results
  'videogame': [new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug()] // [VideogameIDOrSlug] | Filter by videogame(s)
};
apiInstance.getChanges(opts, (error, data, response) => {
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
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]
 **type** | [**[String]**](String.md)| Filter by result type(s) | [optional] 
 **since** | **Date**| Filter out older results | [optional] 
 **videogame** | [**[VideogameIDOrSlug]**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] 

### Return type

[**[Incident]**](Incident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeletions

> [DeletionIncident] getDeletions(opts)

List deletions

Get the latest deleted documents

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.IncidentsApi();
let opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5, // Number | Equivalent to `page[size]`
  'type': ["null"], // [String] | Filter by result type(s)
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out older results
  'videogame': [new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug()] // [VideogameIDOrSlug] | Filter by videogame(s)
};
apiInstance.getDeletions(opts, (error, data, response) => {
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
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]
 **type** | [**[String]**](String.md)| Filter by result type(s) | [optional] 
 **since** | **Date**| Filter out older results | [optional] 
 **videogame** | [**[VideogameIDOrSlug]**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] 

### Return type

[**[DeletionIncident]**](DeletionIncident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIncidents

> [Incident] getIncidents(opts)

List changes, additions and deletions

 Get the latest updates and additions.  This endpoint only provides the latest incident for an object. It does not keep track of previous incidents.

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.IncidentsApi();
let opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5, // Number | Equivalent to `page[size]`
  'type': ["null"], // [String] | Filter by result type(s)
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out older results
  'videogame': [new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug()] // [VideogameIDOrSlug] | Filter by videogame(s)
};
apiInstance.getIncidents(opts, (error, data, response) => {
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
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]
 **type** | [**[String]**](String.md)| Filter by result type(s) | [optional] 
 **since** | **Date**| Filter out older results | [optional] 
 **videogame** | [**[VideogameIDOrSlug]**](VideogameIDOrSlug.md)| Filter by videogame(s) | [optional] 

### Return type

[**[Incident]**](Incident.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


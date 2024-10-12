# SpinitronV2Api.ShowApi

All URIs are relative to *https://spinitron.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**showsGet**](ShowApi.md#showsGet) | **GET** /shows | Returns scheduled shows optionally filtered by {start} and/or {end} datetimes
[**showsIdGet**](ShowApi.md#showsIdGet) | **GET** /shows/{id} | Get a Show by id



## showsGet

> ShowsGet200Response showsGet(opts)

Returns scheduled shows optionally filtered by {start} and/or {end} datetimes

**Terminology**: Spinitron defines a *show* as a radio program. A show can have one or more *schedules*, each of which may specify either an *occurence* or a *repetition*, which represents a set of occurences. Thus scheduled shows have occurences that, for example, may be displayed in a calendar.  In the response, &#x60;items&#x60; is an array of objects representing occurences of scheduled shows.  You may optionally filter &#x60;items&#x60; to a datetime *range* by including in the request {start} and/or {end} parameters, both of which must be no more than one hour in the past. An occurence starting at {end} is included in the reponse.  &#x60;itmes&#x60; can include occurences that begin *or* end within the filter range. A show that goes on air before {start} appears in &#x60;items&#x60; if it ends *after* but not *at* {start}. An occurence starting at or before {end} is included.  If the request omits the {start} parameter, the server sets its value to the current time so that the filter range&#39;s start is always defined. If the request specifies {end} then the requested range is *bounded*, otherwise it is *unbounded*.  For a bounded request, &#x60;items&#x60; includes *every* occurence of all shows occuring in the range. The only difference between objects in &#x60;items&#x60; representing a given show will be the &#x60;start&#x60; field value.  For an unbounded request, &#x60;items&#x60; includes *only one* occurence per show, specifically, the next occurrence after {start} of all shows occuring after {start}.  Use an unbounded request to get a straight list all shows. Use a bounded request to get a calendar/agenda of shows expanded into occurrences by thir shedules and repetitions.  Objects in &#x60;items&#x60; are ordered first by &#x60;datetime&#x60; and then by &#x60;id&#x60;. 

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.ShowApi();
let opts = {
  'start': new Date("2013-10-20T19:20:30+01:00"), // Date | The datetime starting from items must be returned. Maximum 1 hour in past. 
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | The ending datetime. Maximum 1 hour in past. 
  'count': 20, // Number | Amount of items to return
  'page': 56, // Number | Offset, used together with count
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.showsGet(opts, (error, data, response) => {
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
 **start** | **Date**| The datetime starting from items must be returned. Maximum 1 hour in past.  | [optional] 
 **end** | **Date**| The ending datetime. Maximum 1 hour in past.  | [optional] 
 **count** | **Number**| Amount of items to return | [optional] [default to 20]
 **page** | **Number**| Offset, used together with count | [optional] 
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**ShowsGet200Response**](ShowsGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## showsIdGet

> Show showsIdGet(id, opts)

Get a Show by id

The response object represents the next occurence of the show specified by {id}.  Status 404 is returned if a show with {id} does not exist or if it does but all its scheduled occurences elapsed in the past. 

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.ShowApi();
let id = 56; // Number | 
let opts = {
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.showsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**Show**](Show.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


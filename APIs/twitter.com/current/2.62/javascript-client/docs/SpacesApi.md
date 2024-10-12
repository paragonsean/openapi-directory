# TwitterApiV2.SpacesApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findSpaceById**](SpacesApi.md#findSpaceById) | **GET** /2/spaces/{id} | Space lookup by Space ID
[**findSpacesByCreatorIds**](SpacesApi.md#findSpacesByCreatorIds) | **GET** /2/spaces/by/creator_ids | Space lookup by their creators
[**findSpacesByIds**](SpacesApi.md#findSpacesByIds) | **GET** /2/spaces | Space lookup up Space IDs
[**searchSpaces**](SpacesApi.md#searchSpaces) | **GET** /2/spaces/search | Search for Spaces
[**spaceBuyers**](SpacesApi.md#spaceBuyers) | **GET** /2/spaces/{id}/buyers | Retrieve the list of Users who purchased a ticket to the given space
[**spaceTweets**](SpacesApi.md#spaceTweets) | **GET** /2/spaces/{id}/tweets | Retrieve Tweets from a Space.



## findSpaceById

> Get2SpacesIdResponse findSpaceById(id, opts)

Space lookup by Space ID

Returns a variety of information about the Space specified by the requested ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.SpacesApi();
let id = "1YqKDqWqdPLsV"; // String | The ID of the Space to be retrieved.
let opts = {
  'spaceFields': ["null"], // [String] | A comma separated list of Space fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'topicFields': ["null"] // [String] | A comma separated list of Topic fields to display.
};
apiInstance.findSpaceById(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the Space to be retrieved. | 
 **spaceFields** | [**[String]**](String.md)| A comma separated list of Space fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **topicFields** | [**[String]**](String.md)| A comma separated list of Topic fields to display. | [optional] 

### Return type

[**Get2SpacesIdResponse**](Get2SpacesIdResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findSpacesByCreatorIds

> Get2SpacesByCreatorIdsResponse findSpacesByCreatorIds(userIds, opts)

Space lookup by their creators

Returns a variety of information about the Spaces created by the provided User IDs

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.SpacesApi();
let userIds = ["2244994945"]; // [String] | The IDs of Users to search through.
let opts = {
  'spaceFields': ["null"], // [String] | A comma separated list of Space fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'topicFields': ["null"] // [String] | A comma separated list of Topic fields to display.
};
apiInstance.findSpacesByCreatorIds(userIds, opts, (error, data, response) => {
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
 **userIds** | [**[String]**](String.md)| The IDs of Users to search through. | 
 **spaceFields** | [**[String]**](String.md)| A comma separated list of Space fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **topicFields** | [**[String]**](String.md)| A comma separated list of Topic fields to display. | [optional] 

### Return type

[**Get2SpacesByCreatorIdsResponse**](Get2SpacesByCreatorIdsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findSpacesByIds

> Get2SpacesResponse findSpacesByIds(ids, opts)

Space lookup up Space IDs

Returns a variety of information about the Spaces specified by the requested IDs

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.SpacesApi();
let ids = ["1SLjjRYNejbKM"]; // [String] | The list of Space IDs to return.
let opts = {
  'spaceFields': ["null"], // [String] | A comma separated list of Space fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'topicFields': ["null"] // [String] | A comma separated list of Topic fields to display.
};
apiInstance.findSpacesByIds(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| The list of Space IDs to return. | 
 **spaceFields** | [**[String]**](String.md)| A comma separated list of Space fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **topicFields** | [**[String]**](String.md)| A comma separated list of Topic fields to display. | [optional] 

### Return type

[**Get2SpacesResponse**](Get2SpacesResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## searchSpaces

> Get2SpacesSearchResponse searchSpaces(query, opts)

Search for Spaces

Returns Spaces that match the provided query.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.SpacesApi();
let query = "crypto"; // String | The search query.
let opts = {
  'state': "'all'", // String | The state of Spaces to search for.
  'maxResults': 100, // Number | The number of results to return.
  'spaceFields': ["null"], // [String] | A comma separated list of Space fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'topicFields': ["null"] // [String] | A comma separated list of Topic fields to display.
};
apiInstance.searchSpaces(query, opts, (error, data, response) => {
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
 **query** | **String**| The search query. | 
 **state** | **String**| The state of Spaces to search for. | [optional] [default to &#39;all&#39;]
 **maxResults** | **Number**| The number of results to return. | [optional] [default to 100]
 **spaceFields** | [**[String]**](String.md)| A comma separated list of Space fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **topicFields** | [**[String]**](String.md)| A comma separated list of Topic fields to display. | [optional] 

### Return type

[**Get2SpacesSearchResponse**](Get2SpacesSearchResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## spaceBuyers

> Get2SpacesIdBuyersResponse spaceBuyers(id, opts)

Retrieve the list of Users who purchased a ticket to the given space

Retrieves the list of Users who purchased a ticket to the given space

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.SpacesApi();
let id = "1YqKDqWqdPLsV"; // String | The ID of the Space to be retrieved.
let opts = {
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'maxResults': 100, // Number | The maximum number of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.spaceBuyers(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the Space to be retrieved. | 
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2SpacesIdBuyersResponse**](Get2SpacesIdBuyersResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## spaceTweets

> Get2SpacesIdTweetsResponse spaceTweets(id, opts)

Retrieve Tweets from a Space.

Retrieves Tweets shared in the specified Space.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.SpacesApi();
let id = "1YqKDqWqdPLsV"; // String | The ID of the Space to be retrieved.
let opts = {
  'maxResults': 25, // Number | The number of Tweets to fetch from the provided space. If not provided, the value will default to the maximum of 100.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.spaceTweets(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the Space to be retrieved. | 
 **maxResults** | **Number**| The number of Tweets to fetch from the provided space. If not provided, the value will default to the maximum of 100. | [optional] [default to 100]
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2SpacesIdTweetsResponse**](Get2SpacesIdTweetsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


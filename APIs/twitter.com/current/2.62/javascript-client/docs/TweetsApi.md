# TwitterApiV2.TweetsApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrDeleteRules**](TweetsApi.md#addOrDeleteRules) | **POST** /2/tweets/search/stream/rules | Add/Delete rules
[**createTweet**](TweetsApi.md#createTweet) | **POST** /2/tweets | Creation of a Tweet
[**deleteTweetById**](TweetsApi.md#deleteTweetById) | **DELETE** /2/tweets/{id} | Tweet delete by Tweet ID
[**findTweetById**](TweetsApi.md#findTweetById) | **GET** /2/tweets/{id} | Tweet lookup by Tweet ID
[**findTweetsById**](TweetsApi.md#findTweetsById) | **GET** /2/tweets | Tweet lookup by Tweet IDs
[**findTweetsThatQuoteATweet**](TweetsApi.md#findTweetsThatQuoteATweet) | **GET** /2/tweets/{id}/quote_tweets | Retrieve Tweets that quote a Tweet.
[**getRules**](TweetsApi.md#getRules) | **GET** /2/tweets/search/stream/rules | Rules lookup
[**getTweetsFirehoseStream**](TweetsApi.md#getTweetsFirehoseStream) | **GET** /2/tweets/firehose/stream | Firehose stream
[**getTweetsSample10Stream**](TweetsApi.md#getTweetsSample10Stream) | **GET** /2/tweets/sample10/stream | Sample 10% stream
[**hideReplyById**](TweetsApi.md#hideReplyById) | **PUT** /2/tweets/{tweet_id}/hidden | Hide replies
[**listsIdTweets**](TweetsApi.md#listsIdTweets) | **GET** /2/lists/{id}/tweets | List Tweets timeline by List ID.
[**sampleStream**](TweetsApi.md#sampleStream) | **GET** /2/tweets/sample/stream | Sample stream
[**searchStream**](TweetsApi.md#searchStream) | **GET** /2/tweets/search/stream | Filtered stream
[**spaceBuyers_0**](TweetsApi.md#spaceBuyers_0) | **GET** /2/spaces/{id}/buyers | Retrieve the list of Users who purchased a ticket to the given space
[**spaceTweets_0**](TweetsApi.md#spaceTweets_0) | **GET** /2/spaces/{id}/tweets | Retrieve Tweets from a Space.
[**tweetCountsFullArchiveSearch**](TweetsApi.md#tweetCountsFullArchiveSearch) | **GET** /2/tweets/counts/all | Full archive search counts
[**tweetCountsRecentSearch**](TweetsApi.md#tweetCountsRecentSearch) | **GET** /2/tweets/counts/recent | Recent search counts
[**tweetsFullarchiveSearch**](TweetsApi.md#tweetsFullarchiveSearch) | **GET** /2/tweets/search/all | Full-archive search
[**tweetsRecentSearch**](TweetsApi.md#tweetsRecentSearch) | **GET** /2/tweets/search/recent | Recent search
[**usersIdLike**](TweetsApi.md#usersIdLike) | **POST** /2/users/{id}/likes | Causes the User (in the path) to like the specified Tweet
[**usersIdLikedTweets**](TweetsApi.md#usersIdLikedTweets) | **GET** /2/users/{id}/liked_tweets | Returns Tweet objects liked by the provided User ID
[**usersIdMentions**](TweetsApi.md#usersIdMentions) | **GET** /2/users/{id}/mentions | User mention timeline by User ID
[**usersIdRetweets**](TweetsApi.md#usersIdRetweets) | **POST** /2/users/{id}/retweets | Causes the User (in the path) to retweet the specified Tweet.
[**usersIdTimeline**](TweetsApi.md#usersIdTimeline) | **GET** /2/users/{id}/timelines/reverse_chronological | User home timeline by User ID
[**usersIdTweets**](TweetsApi.md#usersIdTweets) | **GET** /2/users/{id}/tweets | User Tweets timeline by User ID
[**usersIdUnlike**](TweetsApi.md#usersIdUnlike) | **DELETE** /2/users/{id}/likes/{tweet_id} | Causes the User (in the path) to unlike the specified Tweet
[**usersIdUnretweets**](TweetsApi.md#usersIdUnretweets) | **DELETE** /2/users/{id}/retweets/{source_tweet_id} | Causes the User (in the path) to unretweet the specified Tweet



## addOrDeleteRules

> AddOrDeleteRulesResponse addOrDeleteRules(addOrDeleteRulesRequest, opts)

Add/Delete rules

Add or delete rules from a User&#39;s active rule set. Users can provide unique, optionally tagged rules to add. Users can delete their entire rule set or a subset specified by rule ids or values.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let addOrDeleteRulesRequest = new TwitterApiV2.AddOrDeleteRulesRequest(); // AddOrDeleteRulesRequest | 
let opts = {
  'dryRun': true // Boolean | Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
};
apiInstance.addOrDeleteRules(addOrDeleteRulesRequest, opts, (error, data, response) => {
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
 **addOrDeleteRulesRequest** | [**AddOrDeleteRulesRequest**](AddOrDeleteRulesRequest.md)|  | 
 **dryRun** | **Boolean**| Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes. | [optional] 

### Return type

[**AddOrDeleteRulesResponse**](AddOrDeleteRulesResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## createTweet

> TweetCreateResponse createTweet(tweetCreateRequest)

Creation of a Tweet

Causes the User to create a Tweet under the authorized account.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let tweetCreateRequest = new TwitterApiV2.TweetCreateRequest(); // TweetCreateRequest | 
apiInstance.createTweet(tweetCreateRequest, (error, data, response) => {
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
 **tweetCreateRequest** | [**TweetCreateRequest**](TweetCreateRequest.md)|  | 

### Return type

[**TweetCreateResponse**](TweetCreateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## deleteTweetById

> TweetDeleteResponse deleteTweetById(id)

Tweet delete by Tweet ID

Delete specified Tweet (in the path) by ID.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | The ID of the Tweet to be deleted.
apiInstance.deleteTweetById(id, (error, data, response) => {
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
 **id** | **String**| The ID of the Tweet to be deleted. | 

### Return type

[**TweetDeleteResponse**](TweetDeleteResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findTweetById

> Get2TweetsIdResponse findTweetById(id, opts)

Tweet lookup by Tweet ID

Returns a variety of information about the Tweet specified by the requested ID.

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

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | A single Tweet ID.
let opts = {
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.findTweetById(id, opts, (error, data, response) => {
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
 **id** | **String**| A single Tweet ID. | 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2TweetsIdResponse**](Get2TweetsIdResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findTweetsById

> Get2TweetsResponse findTweetsById(ids, opts)

Tweet lookup by Tweet IDs

Returns a variety of information about the Tweet specified by the requested ID.

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

let apiInstance = new TwitterApiV2.TweetsApi();
let ids = ["1346889436626259968"]; // [String] | A comma separated list of Tweet IDs. Up to 100 are allowed in a single request.
let opts = {
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.findTweetsById(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma separated list of Tweet IDs. Up to 100 are allowed in a single request. | 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2TweetsResponse**](Get2TweetsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## findTweetsThatQuoteATweet

> Get2TweetsIdQuoteTweetsResponse findTweetsThatQuoteATweet(id, opts)

Retrieve Tweets that quote a Tweet.

Returns a variety of information about each Tweet that quotes the Tweet specified by the requested ID.

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

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | A single Tweet ID.
let opts = {
  'maxResults': 10, // Number | The maximum number of results to be returned.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'exclude': ["null"], // [String] | The set of entities to exclude (e.g. 'replies' or 'retweets').
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.findTweetsThatQuoteATweet(id, opts, (error, data, response) => {
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
 **id** | **String**| A single Tweet ID. | 
 **maxResults** | **Number**| The maximum number of results to be returned. | [optional] [default to 10]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **exclude** | [**[String]**](String.md)| The set of entities to exclude (e.g. &#39;replies&#39; or &#39;retweets&#39;). | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2TweetsIdQuoteTweetsResponse**](Get2TweetsIdQuoteTweetsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getRules

> RulesLookupResponse getRules(opts)

Rules lookup

Returns rules from a User&#39;s active rule set. Users can fetch all of their rules or a subset, specified by the provided rule ids.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let opts = {
  'ids': ["120897978112909812"], // [String] | A comma-separated list of Rule IDs.
  'maxResults': 1000, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example" // String | This value is populated by passing the 'next_token' returned in a request to paginate through results.
};
apiInstance.getRules(opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| A comma-separated list of Rule IDs. | [optional] 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 1000]
 **paginationToken** | **String**| This value is populated by passing the &#39;next_token&#39; returned in a request to paginate through results. | [optional] 

### Return type

[**RulesLookupResponse**](RulesLookupResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getTweetsFirehoseStream

> StreamingTweetResponse getTweetsFirehoseStream(partition, opts)

Firehose stream

Streams 100% of public Tweets.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let partition = 56; // Number | The partition number.
let opts = {
  'backfillMinutes': 56, // Number | The number of minutes of backfill requested.
  'startTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.
  'endTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.getTweetsFirehoseStream(partition, opts, (error, data, response) => {
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
 **partition** | **Number**| The partition number. | 
 **backfillMinutes** | **Number**| The number of minutes of backfill requested. | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**StreamingTweetResponse**](StreamingTweetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getTweetsSample10Stream

> Get2TweetsSample10StreamResponse getTweetsSample10Stream(partition, opts)

Sample 10% stream

Streams a deterministic 10% of public Tweets.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let partition = 56; // Number | The partition number.
let opts = {
  'backfillMinutes': 56, // Number | The number of minutes of backfill requested.
  'startTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.
  'endTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.getTweetsSample10Stream(partition, opts, (error, data, response) => {
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
 **partition** | **Number**| The partition number. | 
 **backfillMinutes** | **Number**| The number of minutes of backfill requested. | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2TweetsSample10StreamResponse**](Get2TweetsSample10StreamResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## hideReplyById

> TweetHideResponse hideReplyById(tweetId, opts)

Hide replies

Hides or unhides a reply to an owned conversation.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let tweetId = "tweetId_example"; // String | The ID of the reply that you want to hide or unhide.
let opts = {
  'tweetHideRequest': new TwitterApiV2.TweetHideRequest() // TweetHideRequest | 
};
apiInstance.hideReplyById(tweetId, opts, (error, data, response) => {
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
 **tweetId** | **String**| The ID of the reply that you want to hide or unhide. | 
 **tweetHideRequest** | [**TweetHideRequest**](TweetHideRequest.md)|  | [optional] 

### Return type

[**TweetHideResponse**](TweetHideResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## listsIdTweets

> Get2ListsIdTweetsResponse listsIdTweets(id, opts)

List Tweets timeline by List ID.

Returns a list of Tweets associated with the provided List ID.

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

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | The ID of the List.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.listsIdTweets(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the List. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2ListsIdTweetsResponse**](Get2ListsIdTweetsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## sampleStream

> StreamingTweetResponse sampleStream(opts)

Sample stream

Streams a deterministic 1% of public Tweets.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let opts = {
  'backfillMinutes': 56, // Number | The number of minutes of backfill requested.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.sampleStream(opts, (error, data, response) => {
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
 **backfillMinutes** | **Number**| The number of minutes of backfill requested. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**StreamingTweetResponse**](StreamingTweetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## searchStream

> FilteredStreamingTweetResponse searchStream(opts)

Filtered stream

Streams Tweets matching the stream&#39;s active rule set.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let opts = {
  'backfillMinutes': 56, // Number | The number of minutes of backfill requested.
  'startTime': new Date("2021-02-01T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided.
  'endTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.searchStream(opts, (error, data, response) => {
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
 **backfillMinutes** | **Number**| The number of minutes of backfill requested. | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**FilteredStreamingTweetResponse**](FilteredStreamingTweetResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## spaceBuyers_0

> Get2SpacesIdBuyersResponse spaceBuyers_0(id, opts)

Retrieve the list of Users who purchased a ticket to the given space

Retrieves the list of Users who purchased a ticket to the given space

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "1YqKDqWqdPLsV"; // String | The ID of the Space to be retrieved.
let opts = {
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'maxResults': 100, // Number | The maximum number of results.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.spaceBuyers_0(id, opts, (error, data, response) => {
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


## spaceTweets_0

> Get2SpacesIdTweetsResponse spaceTweets_0(id, opts)

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

let apiInstance = new TwitterApiV2.TweetsApi();
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
apiInstance.spaceTweets_0(id, opts, (error, data, response) => {
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


## tweetCountsFullArchiveSearch

> Get2TweetsCountsAllResponse tweetCountsFullArchiveSearch(query, opts)

Full archive search counts

Returns Tweet Counts that match a search query.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let query = "(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet"; // String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
  'sinceId': "sinceId_example", // String | Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
  'untilId': "untilId_example", // String | Returns results with a Tweet ID less than (that is, older than) the specified ID.
  'nextToken': "nextToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'granularity': "'hour'", // String | The granularity for the search counts results.
  'searchCountFields': ["null"] // [String] | A comma separated list of SearchCount fields to display.
};
apiInstance.tweetCountsFullArchiveSearch(query, opts, (error, data, response) => {
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
 **query** | **String**| One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length. | 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). | [optional] 
 **sinceId** | **String**| Returns results with a Tweet ID greater than (that is, more recent than) the specified ID. | [optional] 
 **untilId** | **String**| Returns results with a Tweet ID less than (that is, older than) the specified ID. | [optional] 
 **nextToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **granularity** | **String**| The granularity for the search counts results. | [optional] [default to &#39;hour&#39;]
 **searchCountFields** | [**[String]**](String.md)| A comma separated list of SearchCount fields to display. | [optional] 

### Return type

[**Get2TweetsCountsAllResponse**](Get2TweetsCountsAllResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## tweetCountsRecentSearch

> Get2TweetsCountsRecentResponse tweetCountsRecentSearch(query, opts)

Recent search counts

Returns Tweet Counts from the last 7 days that match a search query.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let query = "(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet"; // String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
  'sinceId': "sinceId_example", // String | Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
  'untilId': "untilId_example", // String | Returns results with a Tweet ID less than (that is, older than) the specified ID.
  'nextToken': "nextToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'granularity': "'hour'", // String | The granularity for the search counts results.
  'searchCountFields': ["null"] // [String] | A comma separated list of SearchCount fields to display.
};
apiInstance.tweetCountsRecentSearch(query, opts, (error, data, response) => {
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
 **query** | **String**| One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length. | 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). | [optional] 
 **sinceId** | **String**| Returns results with a Tweet ID greater than (that is, more recent than) the specified ID. | [optional] 
 **untilId** | **String**| Returns results with a Tweet ID less than (that is, older than) the specified ID. | [optional] 
 **nextToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **granularity** | **String**| The granularity for the search counts results. | [optional] [default to &#39;hour&#39;]
 **searchCountFields** | [**[String]**](String.md)| A comma separated list of SearchCount fields to display. | [optional] 

### Return type

[**Get2TweetsCountsRecentResponse**](Get2TweetsCountsRecentResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## tweetsFullarchiveSearch

> Get2TweetsSearchAllResponse tweetsFullarchiveSearch(query, opts)

Full-archive search

Returns Tweets that match a search query.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TwitterApiV2.TweetsApi();
let query = "(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet"; // String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
  'sinceId': "sinceId_example", // String | Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
  'untilId': "untilId_example", // String | Returns results with a Tweet ID less than (that is, older than) the specified ID.
  'maxResults': 10, // Number | The maximum number of search results to be returned by a request.
  'nextToken': "nextToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'sortOrder': "sortOrder_example", // String | This order in which to return results.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.tweetsFullarchiveSearch(query, opts, (error, data, response) => {
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
 **query** | **String**| One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length. | 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). | [optional] 
 **sinceId** | **String**| Returns results with a Tweet ID greater than (that is, more recent than) the specified ID. | [optional] 
 **untilId** | **String**| Returns results with a Tweet ID less than (that is, older than) the specified ID. | [optional] 
 **maxResults** | **Number**| The maximum number of search results to be returned by a request. | [optional] [default to 10]
 **nextToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **sortOrder** | **String**| This order in which to return results. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2TweetsSearchAllResponse**](Get2TweetsSearchAllResponse.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## tweetsRecentSearch

> Get2TweetsSearchRecentResponse tweetsRecentSearch(query, opts)

Recent search

Returns Tweets from the last 7 days that match a search query.

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

let apiInstance = new TwitterApiV2.TweetsApi();
let query = "(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet"; // String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
  'sinceId': "sinceId_example", // String | Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.
  'untilId': "untilId_example", // String | Returns results with a Tweet ID less than (that is, older than) the specified ID.
  'maxResults': 10, // Number | The maximum number of search results to be returned by a request.
  'nextToken': "nextToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
  'sortOrder': "sortOrder_example", // String | This order in which to return results.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.tweetsRecentSearch(query, opts, (error, data, response) => {
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
 **query** | **String**| One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length. | 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). | [optional] 
 **sinceId** | **String**| Returns results with a Tweet ID greater than (that is, more recent than) the specified ID. | [optional] 
 **untilId** | **String**| Returns results with a Tweet ID less than (that is, older than) the specified ID. | [optional] 
 **maxResults** | **Number**| The maximum number of search results to be returned by a request. | [optional] [default to 10]
 **nextToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | [optional] 
 **sortOrder** | **String**| This order in which to return results. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2TweetsSearchRecentResponse**](Get2TweetsSearchRecentResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdLike

> UsersLikesCreateResponse usersIdLike(id, opts)

Causes the User (in the path) to like the specified Tweet

Causes the User (in the path) to like the specified Tweet. The User in the path must match the User context authorizing the request.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | The ID of the authenticated source User that is requesting to like the Tweet.
let opts = {
  'usersLikesCreateRequest': new TwitterApiV2.UsersLikesCreateRequest() // UsersLikesCreateRequest | 
};
apiInstance.usersIdLike(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User that is requesting to like the Tweet. | 
 **usersLikesCreateRequest** | [**UsersLikesCreateRequest**](UsersLikesCreateRequest.md)|  | [optional] 

### Return type

[**UsersLikesCreateResponse**](UsersLikesCreateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## usersIdLikedTweets

> Get2UsersIdLikedTweetsResponse usersIdLikedTweets(id, opts)

Returns Tweet objects liked by the provided User ID

Returns a list of Tweets liked by the provided User ID

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

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.usersIdLikedTweets(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the User to lookup. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2UsersIdLikedTweetsResponse**](Get2UsersIdLikedTweetsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdMentions

> Get2UsersIdMentionsResponse usersIdMentions(id, opts)

User mention timeline by User ID

Returns Tweet objects that mention username associated to the provided User ID

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

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'sinceId': "sinceId_example", // String | The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
  'untilId': "1346889436626259968", // String | The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'startTime': new Date("2021-02-01T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.
  'endTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.usersIdMentions(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the User to lookup. | 
 **sinceId** | **String**| The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified. | [optional] 
 **untilId** | **String**| The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified. | [optional] 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2UsersIdMentionsResponse**](Get2UsersIdMentionsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdRetweets

> UsersRetweetsCreateResponse usersIdRetweets(id, opts)

Causes the User (in the path) to retweet the specified Tweet.

Causes the User (in the path) to retweet the specified Tweet. The User in the path must match the User context authorizing the request.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | The ID of the authenticated source User that is requesting to retweet the Tweet.
let opts = {
  'usersRetweetsCreateRequest': new TwitterApiV2.UsersRetweetsCreateRequest() // UsersRetweetsCreateRequest | 
};
apiInstance.usersIdRetweets(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User that is requesting to retweet the Tweet. | 
 **usersRetweetsCreateRequest** | [**UsersRetweetsCreateRequest**](UsersRetweetsCreateRequest.md)|  | [optional] 

### Return type

[**UsersRetweetsCreateResponse**](UsersRetweetsCreateResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## usersIdTimeline

> Get2UsersIdTimelinesReverseChronologicalResponse usersIdTimeline(id, opts)

User home timeline by User ID

Returns Tweet objects that appears in the provided User ID&#39;s home timeline

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | The ID of the authenticated source User to list Reverse Chronological Timeline Tweets of.
let opts = {
  'sinceId': "791775337160081409", // String | The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
  'untilId': "1346889436626259968", // String | The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'exclude': ["null"], // [String] | The set of entities to exclude (e.g. 'replies' or 'retweets').
  'startTime': new Date("2021-02-01T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.
  'endTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.usersIdTimeline(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User to list Reverse Chronological Timeline Tweets of. | 
 **sinceId** | **String**| The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified. | [optional] 
 **untilId** | **String**| The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified. | [optional] 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **exclude** | [**[String]**](String.md)| The set of entities to exclude (e.g. &#39;replies&#39; or &#39;retweets&#39;). | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2UsersIdTimelinesReverseChronologicalResponse**](Get2UsersIdTimelinesReverseChronologicalResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdTweets

> Get2UsersIdTweetsResponse usersIdTweets(id, opts)

User Tweets timeline by User ID

Returns a list of Tweets authored by the provided User ID

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

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "2244994945"; // String | The ID of the User to lookup.
let opts = {
  'sinceId': "791775337160081409", // String | The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
  'untilId': "1346889436626259968", // String | The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'exclude': ["null"], // [String] | The set of entities to exclude (e.g. 'replies' or 'retweets').
  'startTime': new Date("2021-02-01T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.
  'endTime': new Date("2021-02-14T18:40:40.000Z"), // Date | YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.usersIdTweets(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the User to lookup. | 
 **sinceId** | **String**| The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified. | [optional] 
 **untilId** | **String**| The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified. | [optional] 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **exclude** | [**[String]**](String.md)| The set of entities to exclude (e.g. &#39;replies&#39; or &#39;retweets&#39;). | [optional] 
 **startTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified. | [optional] 
 **endTime** | **Date**| YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2UsersIdTweetsResponse**](Get2UsersIdTweetsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [BearerToken](../README.md#BearerToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdUnlike

> UsersLikesDeleteResponse usersIdUnlike(id, tweetId)

Causes the User (in the path) to unlike the specified Tweet

Causes the User (in the path) to unlike the specified Tweet. The User must match the User context authorizing the request

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | The ID of the authenticated source User that is requesting to unlike the Tweet.
let tweetId = "tweetId_example"; // String | The ID of the Tweet that the User is requesting to unlike.
apiInstance.usersIdUnlike(id, tweetId, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User that is requesting to unlike the Tweet. | 
 **tweetId** | **String**| The ID of the Tweet that the User is requesting to unlike. | 

### Return type

[**UsersLikesDeleteResponse**](UsersLikesDeleteResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## usersIdUnretweets

> UsersRetweetsDeleteResponse usersIdUnretweets(id, sourceTweetId)

Causes the User (in the path) to unretweet the specified Tweet

Causes the User (in the path) to unretweet the specified Tweet. The User must match the User context authorizing the request

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.TweetsApi();
let id = "id_example"; // String | The ID of the authenticated source User that is requesting to retweet the Tweet.
let sourceTweetId = "sourceTweetId_example"; // String | The ID of the Tweet that the User is requesting to unretweet.
apiInstance.usersIdUnretweets(id, sourceTweetId, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User that is requesting to retweet the Tweet. | 
 **sourceTweetId** | **String**| The ID of the Tweet that the User is requesting to unretweet. | 

### Return type

[**UsersRetweetsDeleteResponse**](UsersRetweetsDeleteResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


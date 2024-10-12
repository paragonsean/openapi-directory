# AdafruitIoRestApi.FeedsApi

All URIs are relative to *https://io.adafruit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFeedToGroup_0**](FeedsApi.md#addFeedToGroup_0) | **POST** /{username}/groups/{group_key}/add | Add an existing Feed to a Group
[**allFeeds**](FeedsApi.md#allFeeds) | **GET** /{username}/feeds | All feeds for current user
[**allGroupFeeds_0**](FeedsApi.md#allGroupFeeds_0) | **GET** /{username}/groups/{group_key}/feeds | All feeds for current user in a given group
[**createFeed**](FeedsApi.md#createFeed) | **POST** /{username}/feeds | Create a new Feed
[**createGroupFeed**](FeedsApi.md#createGroupFeed) | **POST** /{username}/groups/{group_key}/feeds | Create a new Feed in a Group
[**destroyFeed**](FeedsApi.md#destroyFeed) | **DELETE** /{username}/feeds/{feed_key} | Delete an existing Feed
[**getFeed**](FeedsApi.md#getFeed) | **GET** /{username}/feeds/{feed_key} | Get feed by feed key
[**getFeedDetails**](FeedsApi.md#getFeedDetails) | **GET** /{username}/feeds/{feed_key}/details | Get detailed feed by feed key
[**removeFeedFromGroup_0**](FeedsApi.md#removeFeedFromGroup_0) | **POST** /{username}/groups/{group_key}/remove | Remove a Feed from a Group
[**replaceFeed**](FeedsApi.md#replaceFeed) | **PUT** /{username}/feeds/{feed_key} | Replace an existing Feed
[**updateFeed**](FeedsApi.md#updateFeed) | **PATCH** /{username}/feeds/{feed_key} | Update properties of an existing Feed



## addFeedToGroup_0

> Group addFeedToGroup_0(groupKey, username, opts)

Add an existing Feed to a Group

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let groupKey = "groupKey_example"; // String | 
let username = "username_example"; // String | a valid username string
let opts = {
  'feedKey': "feedKey_example" // String | 
};
apiInstance.addFeedToGroup_0(groupKey, username, opts, (error, data, response) => {
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
 **groupKey** | **String**|  | 
 **username** | **String**| a valid username string | 
 **feedKey** | **String**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## allFeeds

> [Feed] allFeeds(username)

All feeds for current user

The Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed.

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
apiInstance.allFeeds(username, (error, data, response) => {
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
 **username** | **String**| a valid username string | 

### Return type

[**[Feed]**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## allGroupFeeds_0

> [Feed] allGroupFeeds_0(groupKey, username)

All feeds for current user in a given group

The Group Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed, but only for feeds within the given group.

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let groupKey = "groupKey_example"; // String | 
let username = "username_example"; // String | a valid username string
apiInstance.allGroupFeeds_0(groupKey, username, (error, data, response) => {
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
 **groupKey** | **String**|  | 
 **username** | **String**| a valid username string | 

### Return type

[**[Feed]**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## createFeed

> Feed createFeed(username, feed, opts)

Create a new Feed

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
let feed = new AdafruitIoRestApi.CreateFeedRequest(); // CreateFeedRequest | 
let opts = {
  'groupKey': "groupKey_example" // String | 
};
apiInstance.createFeed(username, feed, opts, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | 
 **groupKey** | **String**|  | [optional] 

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## createGroupFeed

> Feed createGroupFeed(username, groupKey, feed)

Create a new Feed in a Group

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
let groupKey = "groupKey_example"; // String | 
let feed = new AdafruitIoRestApi.CreateFeedRequest(); // CreateFeedRequest | 
apiInstance.createGroupFeed(username, groupKey, feed, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **groupKey** | **String**|  | 
 **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | 

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## destroyFeed

> destroyFeed(username, feedKey)

Delete an existing Feed

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
apiInstance.destroyFeed(username, feedKey, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **feedKey** | **String**| a valid feed key | 

### Return type

null (empty response body)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFeed

> Feed getFeed(username, feedKey)

Get feed by feed key

Returns feed based on the feed key

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
apiInstance.getFeed(username, feedKey, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **feedKey** | **String**| a valid feed key | 

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## getFeedDetails

> Feed getFeedDetails(username, feedKey)

Get detailed feed by feed key

Returns more detailed feed record based on the feed key

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
apiInstance.getFeedDetails(username, feedKey, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **feedKey** | **String**| a valid feed key | 

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## removeFeedFromGroup_0

> Group removeFeedFromGroup_0(groupKey, username, opts)

Remove a Feed from a Group

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let groupKey = "groupKey_example"; // String | 
let username = "username_example"; // String | a valid username string
let opts = {
  'feedKey': "feedKey_example" // String | 
};
apiInstance.removeFeedFromGroup_0(groupKey, username, opts, (error, data, response) => {
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
 **groupKey** | **String**|  | 
 **username** | **String**| a valid username string | 
 **feedKey** | **String**|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## replaceFeed

> Feed replaceFeed(username, feedKey, feed)

Replace an existing Feed

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let feed = new AdafruitIoRestApi.CreateFeedRequest(); // CreateFeedRequest | 
apiInstance.replaceFeed(username, feedKey, feed, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **feedKey** | **String**| a valid feed key | 
 **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | 

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## updateFeed

> Feed updateFeed(username, feedKey, feed)

Update properties of an existing Feed

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.FeedsApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let feed = new AdafruitIoRestApi.CreateFeedRequest(); // CreateFeedRequest | 
apiInstance.updateFeed(username, feedKey, feed, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **feedKey** | **String**| a valid feed key | 
 **feed** | [**CreateFeedRequest**](CreateFeedRequest.md)|  | 

### Return type

[**Feed**](Feed.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


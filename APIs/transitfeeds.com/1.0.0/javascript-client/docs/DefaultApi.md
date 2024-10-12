# TransitFeedsApi.DefaultApi

All URIs are relative to *https://api.transitfeeds.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFeedVersions**](DefaultApi.md#getFeedVersions) | **GET** /getFeedVersions | Retrieve a list of versions of specified (or all) feeds.
[**getFeeds**](DefaultApi.md#getFeeds) | **GET** /getFeeds | Retrieve a list of feeds.
[**getLatestFeedVersion**](DefaultApi.md#getLatestFeedVersion) | **GET** /getLatestFeedVersion | Retrieve the download URL for the latest version of a feed.
[**getLocations**](DefaultApi.md#getLocations) | **GET** /getLocations | Retrieve a list of locations.



## getFeedVersions

> GetFeedVersionsResponse getFeedVersions(key, opts)

Retrieve a list of versions of specified (or all) feeds.

This API call allows you to easily see every single feed update in the TranstiFeeds.com system. Since this can be quite long, it&#39;s also possible to filter this list by a single feed ID. 

### Example

```javascript
import TransitFeedsApi from 'transit_feeds_api';

let apiInstance = new TransitFeedsApi.DefaultApi();
let key = "'YOUR_API_KEY'"; // String | Your personal API key, used for authentication.
let opts = {
  'feed': "feed_example", // String | If you only want to retrieve feed versions for a particular feed, include its ID here. You can use the `/getFeeds` call to discover feed IDs.
  'page': 1, // Number | The page number of results to return. For example, if you specify a `page` of `2` with a `limit` of 10, then results 11-20 are returned. The number of pages available is included in the response. 
  'limit': 10, // Number | The maximum number of results to return..
  'err': 1, // Number | To include any errors detected when importing this feed in the response, specify a valud of `1`.
  'warn': 1 // Number | To include any warnings detected when importing this feed in the response, specify a valud of `1`.
};
apiInstance.getFeedVersions(key, opts, (error, data, response) => {
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
 **key** | **String**| Your personal API key, used for authentication. | [default to &#39;YOUR_API_KEY&#39;]
 **feed** | **String**| If you only want to retrieve feed versions for a particular feed, include its ID here. You can use the &#x60;/getFeeds&#x60; call to discover feed IDs. | [optional] 
 **page** | **Number**| The page number of results to return. For example, if you specify a &#x60;page&#x60; of &#x60;2&#x60; with a &#x60;limit&#x60; of 10, then results 11-20 are returned. The number of pages available is included in the response.  | [optional] [default to 1]
 **limit** | **Number**| The maximum number of results to return.. | [optional] [default to 10]
 **err** | **Number**| To include any errors detected when importing this feed in the response, specify a valud of &#x60;1&#x60;. | [optional] [default to 1]
 **warn** | **Number**| To include any warnings detected when importing this feed in the response, specify a valud of &#x60;1&#x60;. | [optional] [default to 1]

### Return type

[**GetFeedVersionsResponse**](GetFeedVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeeds

> GetFeedsResponse getFeeds(key, opts)

Retrieve a list of feeds.

Used this API to retrieve a list of feeds in the system. Doing so can be usedful to discover feed IDs that can be used in other API calls. 

### Example

```javascript
import TransitFeedsApi from 'transit_feeds_api';

let apiInstance = new TransitFeedsApi.DefaultApi();
let key = "'YOUR_API_KEY'"; // String | Your personal API key, used for authentication.
let opts = {
  'location': 56, // Number | This is the unique ID of a location. If specified, feeds will only be returned that belong to this location (and perhaps sub-locations too, depending on the `descendants` value). You can use the `/getLocations` API endpoint to determine location IDs. 
  'descendants': 1, // Number | If a location is specified in `location`, this flag can be used to control if returned feeds must be assigned directly to the location, or if feeds belonging to sub-locations can also be returned. If `0`, then feeds must be assigned directly to the specified location.
  'page': 1, // Number | The page number of results to return. For example, if you specify a `page` of `2` with a `limit` of 10, then results 11-20 are returned. The number of pages available is included in the response. 
  'limit': 10, // Number | The maximum number of results to return..
  'type': "type_example" // String | The type of feeds to return. If unspecified, feeds of all types are returned.
};
apiInstance.getFeeds(key, opts, (error, data, response) => {
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
 **key** | **String**| Your personal API key, used for authentication. | [default to &#39;YOUR_API_KEY&#39;]
 **location** | **Number**| This is the unique ID of a location. If specified, feeds will only be returned that belong to this location (and perhaps sub-locations too, depending on the &#x60;descendants&#x60; value). You can use the &#x60;/getLocations&#x60; API endpoint to determine location IDs.  | [optional] 
 **descendants** | **Number**| If a location is specified in &#x60;location&#x60;, this flag can be used to control if returned feeds must be assigned directly to the location, or if feeds belonging to sub-locations can also be returned. If &#x60;0&#x60;, then feeds must be assigned directly to the specified location. | [optional] [default to 1]
 **page** | **Number**| The page number of results to return. For example, if you specify a &#x60;page&#x60; of &#x60;2&#x60; with a &#x60;limit&#x60; of 10, then results 11-20 are returned. The number of pages available is included in the response.  | [optional] [default to 1]
 **limit** | **Number**| The maximum number of results to return.. | [optional] [default to 10]
 **type** | **String**| The type of feeds to return. If unspecified, feeds of all types are returned. | [optional] 

### Return type

[**GetFeedsResponse**](GetFeedsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLatestFeedVersion

> GetLatestFeedVersionResponse getLatestFeedVersion(key, feed)

Retrieve the download URL for the latest version of a feed.

Once you have used &#x60;/getFeeds&#x60; to discover a feed&#39;s URL, you can use this endpoint to download its latest version from TranstiFeeds. It will be unmodified in the original format from the provider. 

### Example

```javascript
import TransitFeedsApi from 'transit_feeds_api';

let apiInstance = new TransitFeedsApi.DefaultApi();
let key = "'YOUR_API_KEY'"; // String | Your personal API key, used for authentication.
let feed = "feed_example"; // String | The ID of the feed to retrieve the latest feed version for. You can use the `/getFeeds` call to discover feed IDs.
apiInstance.getLatestFeedVersion(key, feed, (error, data, response) => {
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
 **key** | **String**| Your personal API key, used for authentication. | [default to &#39;YOUR_API_KEY&#39;]
 **feed** | **String**| The ID of the feed to retrieve the latest feed version for. You can use the &#x60;/getFeeds&#x60; call to discover feed IDs. | 

### Return type

[**GetLatestFeedVersionResponse**](GetLatestFeedVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLocations

> GetLocationsResponse getLocations(key)

Retrieve a list of locations.

Retrieve a list of locations. Each location (except for the root) has a parent location, and each location has zero or more child locations. This hierarchy is generally structured so countries contain states, states contain cities (although this typically depends on the country). 

### Example

```javascript
import TransitFeedsApi from 'transit_feeds_api';

let apiInstance = new TransitFeedsApi.DefaultApi();
let key = "'YOUR_API_KEY'"; // String | Your personal API key, used for authentication.
apiInstance.getLocations(key, (error, data, response) => {
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
 **key** | **String**| Your personal API key, used for authentication. | [default to &#39;YOUR_API_KEY&#39;]

### Return type

[**GetLocationsResponse**](GetLocationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


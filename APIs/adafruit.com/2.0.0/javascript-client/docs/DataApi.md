# AdafruitIoRestApi.DataApi

All URIs are relative to *https://io.adafruit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allData**](DataApi.md#allData) | **GET** /{username}/feeds/{feed_key}/data | Get all data for the given feed
[**allGroupFeedData**](DataApi.md#allGroupFeedData) | **GET** /{username}/groups/{group_key}/feeds/{feed_key}/data | All data for current feed in a specific group
[**batchCreateData**](DataApi.md#batchCreateData) | **POST** /{username}/feeds/{feed_key}/data/batch | Create multiple new Data records
[**batchCreateGroupFeedData**](DataApi.md#batchCreateGroupFeedData) | **POST** /{username}/groups/{group_key}/feeds/{feed_key}/data/batch | Create multiple new Data records in a feed belonging to a particular group
[**chartData**](DataApi.md#chartData) | **GET** /{username}/feeds/{feed_key}/data/chart | Chart data for current feed
[**createData**](DataApi.md#createData) | **POST** /{username}/feeds/{feed_key}/data | Create new Data
[**createGroupData**](DataApi.md#createGroupData) | **POST** /{username}/groups/{group_key}/data | Create new data for multiple feeds in a group
[**createGroupFeedData**](DataApi.md#createGroupFeedData) | **POST** /{username}/groups/{group_key}/feeds/{feed_key}/data | Create new Data in a feed belonging to a particular group
[**createRawWebhookFeedData_0**](DataApi.md#createRawWebhookFeedData_0) | **POST** /webhooks/feed/:token/raw | Send arbitrary data to a feed via webhook URL.
[**createWebhookFeedData_0**](DataApi.md#createWebhookFeedData_0) | **POST** /webhooks/feed/:token | Send data to a feed via webhook URL.
[**destroyData**](DataApi.md#destroyData) | **DELETE** /{username}/feeds/{feed_key}/data/{id} | Delete existing Data
[**firstData**](DataApi.md#firstData) | **GET** /{username}/feeds/{feed_key}/data/first | First Data in Queue
[**getData**](DataApi.md#getData) | **GET** /{username}/feeds/{feed_key}/data/{id} | Returns data based on feed key
[**lastData**](DataApi.md#lastData) | **GET** /{username}/feeds/{feed_key}/data/last | Last Data in Queue
[**nextData**](DataApi.md#nextData) | **GET** /{username}/feeds/{feed_key}/data/next | Next Data in Queue
[**previousData**](DataApi.md#previousData) | **GET** /{username}/feeds/{feed_key}/data/previous | Previous Data in Queue
[**replaceData**](DataApi.md#replaceData) | **PUT** /{username}/feeds/{feed_key}/data/{id} | Replace existing Data
[**retainData**](DataApi.md#retainData) | **GET** /{username}/feeds/{feed_key}/data/retain | Last Data in MQTT CSV format
[**updateData**](DataApi.md#updateData) | **PATCH** /{username}/feeds/{feed_key}/data/{id} | Update properties of existing Data



## allData

> [DataResponse] allData(username, feedKey, opts)

Get all data for the given feed

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start time for filtering, returns records created after given time.
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End time for filtering, returns records created before give time.
  'limit': 56, // Number | Limit the number of records returned.
  'include': "include_example" // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
};
apiInstance.allData(username, feedKey, opts, (error, data, response) => {
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
 **startTime** | **Date**| Start time for filtering, returns records created after given time. | [optional] 
 **endTime** | **Date**| End time for filtering, returns records created before give time. | [optional] 
 **limit** | **Number**| Limit the number of records returned. | [optional] 
 **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] 

### Return type

[**[DataResponse]**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## allGroupFeedData

> [DataResponse] allGroupFeedData(username, groupKey, feedKey, opts)

All data for current feed in a specific group

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let groupKey = "groupKey_example"; // String | 
let feedKey = "feedKey_example"; // String | a valid feed key
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start time for filtering data. Returns data created after given time.
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End time for filtering data. Returns data created before give time.
  'limit': 56 // Number | Limit the number of records returned.
};
apiInstance.allGroupFeedData(username, groupKey, feedKey, opts, (error, data, response) => {
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
 **feedKey** | **String**| a valid feed key | 
 **startTime** | **Date**| Start time for filtering data. Returns data created after given time. | [optional] 
 **endTime** | **Date**| End time for filtering data. Returns data created before give time. | [optional] 
 **limit** | **Number**| Limit the number of records returned. | [optional] 

### Return type

[**[DataResponse]**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## batchCreateData

> [DataResponse] batchCreateData(username, feedKey, data)

Create multiple new Data records

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let data = [new AdafruitIoRestApi.CreateDataRequest()]; // [CreateDataRequest] | A collection of data records including `value` (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
apiInstance.batchCreateData(username, feedKey, data, (error, data, response) => {
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
 **data** | [**[CreateDataRequest]**](CreateDataRequest.md)| A collection of data records including &#x60;value&#x60; (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | 

### Return type

[**[DataResponse]**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## batchCreateGroupFeedData

> [DataResponse] batchCreateGroupFeedData(username, groupKey, feedKey, data)

Create multiple new Data records in a feed belonging to a particular group

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let groupKey = "groupKey_example"; // String | 
let feedKey = "feedKey_example"; // String | a valid feed key
let data = [new AdafruitIoRestApi.CreateDataRequest()]; // [CreateDataRequest] | A collection of data records including `value` (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
apiInstance.batchCreateGroupFeedData(username, groupKey, feedKey, data, (error, data, response) => {
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
 **feedKey** | **String**| a valid feed key | 
 **data** | [**[CreateDataRequest]**](CreateDataRequest.md)| A collection of data records including &#x60;value&#x60; (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | 

### Return type

[**[DataResponse]**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## chartData

> ChartData200Response chartData(username, feedKey, opts)

Chart data for current feed

The Chart API is what we use on io.adafruit.com to populate charts over varying timespans with a consistent number of data points. The maximum number of points returned is 480. This API works by aggregating slices of time into a single value by averaging.  All time-based parameters are optional, if none are given it will default to 1 hour at the finest-grained resolution possible.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start time for filtering, returns records created after given time.
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End time for filtering, returns records created before give time.
  'resolution': 56, // Number | A resolution size in minutes. By giving a resolution value you will get back grouped data points aggregated over resolution-sized intervals. NOTE: time span is preferred over resolution, so if you request a span of time that includes more than max limit points you may get a larger resolution than you requested. Valid resolutions are 1, 5, 10, 30, 60, and 120.
  'hours': 56 // Number | The number of hours the chart should cover.
};
apiInstance.chartData(username, feedKey, opts, (error, data, response) => {
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
 **startTime** | **Date**| Start time for filtering, returns records created after given time. | [optional] 
 **endTime** | **Date**| End time for filtering, returns records created before give time. | [optional] 
 **resolution** | **Number**| A resolution size in minutes. By giving a resolution value you will get back grouped data points aggregated over resolution-sized intervals. NOTE: time span is preferred over resolution, so if you request a span of time that includes more than max limit points you may get a larger resolution than you requested. Valid resolutions are 1, 5, 10, 30, 60, and 120. | [optional] 
 **hours** | **Number**| The number of hours the chart should cover. | [optional] 

### Return type

[**ChartData200Response**](ChartData200Response.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## createData

> Data createData(username, feedKey, datum)

Create new Data

Create new data records on the given feed.  **NOTE:** when feed history is on, data &#x60;value&#x60; size is limited to 1KB, when feed history is turned off data value size is limited to 100KB.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let datum = new AdafruitIoRestApi.CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
apiInstance.createData(username, feedKey, datum, (error, data, response) => {
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
 **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | 

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## createGroupData

> [DataResponse] createGroupData(username, groupKey, groupFeedData)

Create new data for multiple feeds in a group

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let groupKey = "groupKey_example"; // String | 
let groupFeedData = new AdafruitIoRestApi.CreateGroupDataRequest(); // CreateGroupDataRequest | 
apiInstance.createGroupData(username, groupKey, groupFeedData, (error, data, response) => {
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
 **groupFeedData** | [**CreateGroupDataRequest**](CreateGroupDataRequest.md)|  | 

### Return type

[**[DataResponse]**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## createGroupFeedData

> DataResponse createGroupFeedData(username, groupKey, feedKey, datum)

Create new Data in a feed belonging to a particular group

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let groupKey = "groupKey_example"; // String | 
let feedKey = "feedKey_example"; // String | a valid feed key
let datum = new AdafruitIoRestApi.CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
apiInstance.createGroupFeedData(username, groupKey, feedKey, datum, (error, data, response) => {
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
 **feedKey** | **String**| a valid feed key | 
 **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## createRawWebhookFeedData_0

> Data createRawWebhookFeedData_0()

Send arbitrary data to a feed via webhook URL.

The raw data webhook receiver accepts POST requests and stores the raw request body on your feed. This is useful when you don&#39;t have control of the webhook sender. If feed history is turned on, payloads will be truncated at 1024 bytes. If feed history is turned off, payloads will be truncated at 100KB.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
apiInstance.createRawWebhookFeedData_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## createWebhookFeedData_0

> Data createWebhookFeedData_0(payload)

Send data to a feed via webhook URL.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let payload = new AdafruitIoRestApi.CreateWebhookFeedDataRequest(); // CreateWebhookFeedDataRequest | Webhook payload containing data `value` parameter.
apiInstance.createWebhookFeedData_0(payload, (error, data, response) => {
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
 **payload** | [**CreateWebhookFeedDataRequest**](CreateWebhookFeedDataRequest.md)| Webhook payload containing data &#x60;value&#x60; parameter. | 

### Return type

[**Data**](Data.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## destroyData

> String destroyData(username, feedKey, id)

Delete existing Data

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let id = "id_example"; // String | 
apiInstance.destroyData(username, feedKey, id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**String**

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## firstData

> DataResponse firstData(username, feedKey, opts)

First Data in Queue

Get the oldest data point in the feed. This request sets the queue pointer to the beginning of the feed.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let opts = {
  'include': "include_example" // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
};
apiInstance.firstData(username, feedKey, opts, (error, data, response) => {
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
 **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## getData

> DataResponse getData(username, feedKey, id, opts)

Returns data based on feed key

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let id = "id_example"; // String | 
let opts = {
  'include': "include_example" // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
};
apiInstance.getData(username, feedKey, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## lastData

> DataResponse lastData(username, feedKey, opts)

Last Data in Queue

Get the most recent data point in the feed. This request sets the queue pointer to the end of the feed.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let opts = {
  'include': "include_example" // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
};
apiInstance.lastData(username, feedKey, opts, (error, data, response) => {
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
 **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## nextData

> DataResponse nextData(username, feedKey, opts)

Next Data in Queue

Get the next newest data point in the feed. If queue processing hasn&#39;t been started, the first data point in the feed will be returned.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let opts = {
  'include': "include_example" // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
};
apiInstance.nextData(username, feedKey, opts, (error, data, response) => {
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
 **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## previousData

> DataResponse previousData(username, feedKey, opts)

Previous Data in Queue

Get the previously processed data point in the feed. NOTE: this method doesn&#39;t move the processing queue pointer.

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let opts = {
  'include': "include_example" // String | List of Data record fields to include in response as comma separated list. Acceptable values are: `value`, `lat`, `lon`, `ele`, `id`, and `created_at`. 
};
apiInstance.previousData(username, feedKey, opts, (error, data, response) => {
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
 **include** | **String**| List of Data record fields to include in response as comma separated list. Acceptable values are: &#x60;value&#x60;, &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60;, &#x60;id&#x60;, and &#x60;created_at&#x60;.  | [optional] 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## replaceData

> DataResponse replaceData(username, feedKey, id, datum)

Replace existing Data

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let id = "id_example"; // String | 
let datum = new AdafruitIoRestApi.CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
apiInstance.replaceData(username, feedKey, id, datum, (error, data, response) => {
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
 **id** | **String**|  | 
 **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## retainData

> String retainData(username, feedKey)

Last Data in MQTT CSV format

Get the most recent data point in the feed in an MQTT compatible CSV format: &#x60;value,lat,lon,ele&#x60;

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
apiInstance.retainData(username, feedKey, (error, data, response) => {
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

**String**

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv


## updateData

> DataResponse updateData(username, feedKey, id, datum)

Update properties of existing Data

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

let apiInstance = new AdafruitIoRestApi.DataApi();
let username = "username_example"; // String | a valid username string
let feedKey = "feedKey_example"; // String | a valid feed key
let id = "id_example"; // String | 
let datum = new AdafruitIoRestApi.CreateDataRequest(); // CreateDataRequest | Data record including a `value` field (required) and optionally including: `lat`, `lon`, `ele` (latitude, longitude, and elevation values), and `created_at` (a date/time string).
apiInstance.updateData(username, feedKey, id, datum, (error, data, response) => {
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
 **id** | **String**|  | 
 **datum** | [**CreateDataRequest**](CreateDataRequest.md)| Data record including a &#x60;value&#x60; field (required) and optionally including: &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;ele&#x60; (latitude, longitude, and elevation values), and &#x60;created_at&#x60; (a date/time string). | 

### Return type

[**DataResponse**](DataResponse.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


# TheBlueAllianceApiV3.EventApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistrictEventsKeys_0**](EventApi.md#getDistrictEventsKeys_0) | **GET** /district/{district_key}/events/keys | 
[**getDistrictEventsSimple_0**](EventApi.md#getDistrictEventsSimple_0) | **GET** /district/{district_key}/events/simple | 
[**getDistrictEvents_0**](EventApi.md#getDistrictEvents_0) | **GET** /district/{district_key}/events | 
[**getEvent**](EventApi.md#getEvent) | **GET** /event/{event_key} | 
[**getEventAlliances**](EventApi.md#getEventAlliances) | **GET** /event/{event_key}/alliances | 
[**getEventAwards**](EventApi.md#getEventAwards) | **GET** /event/{event_key}/awards | 
[**getEventDistrictPoints**](EventApi.md#getEventDistrictPoints) | **GET** /event/{event_key}/district_points | 
[**getEventInsights**](EventApi.md#getEventInsights) | **GET** /event/{event_key}/insights | 
[**getEventMatchTimeseries**](EventApi.md#getEventMatchTimeseries) | **GET** /event/{event_key}/matches/timeseries | 
[**getEventMatches**](EventApi.md#getEventMatches) | **GET** /event/{event_key}/matches | 
[**getEventMatchesKeys**](EventApi.md#getEventMatchesKeys) | **GET** /event/{event_key}/matches/keys | 
[**getEventMatchesSimple**](EventApi.md#getEventMatchesSimple) | **GET** /event/{event_key}/matches/simple | 
[**getEventOPRs**](EventApi.md#getEventOPRs) | **GET** /event/{event_key}/oprs | 
[**getEventPredictions**](EventApi.md#getEventPredictions) | **GET** /event/{event_key}/predictions | 
[**getEventRankings**](EventApi.md#getEventRankings) | **GET** /event/{event_key}/rankings | 
[**getEventSimple**](EventApi.md#getEventSimple) | **GET** /event/{event_key}/simple | 
[**getEventTeams**](EventApi.md#getEventTeams) | **GET** /event/{event_key}/teams | 
[**getEventTeamsKeys**](EventApi.md#getEventTeamsKeys) | **GET** /event/{event_key}/teams/keys | 
[**getEventTeamsSimple**](EventApi.md#getEventTeamsSimple) | **GET** /event/{event_key}/teams/simple | 
[**getEventTeamsStatuses**](EventApi.md#getEventTeamsStatuses) | **GET** /event/{event_key}/teams/statuses | 
[**getEventsByYear**](EventApi.md#getEventsByYear) | **GET** /events/{year} | 
[**getEventsByYearKeys**](EventApi.md#getEventsByYearKeys) | **GET** /events/{year}/keys | 
[**getEventsByYearSimple**](EventApi.md#getEventsByYearSimple) | **GET** /events/{year}/simple | 
[**getTeamEventAwards_0**](EventApi.md#getTeamEventAwards_0) | **GET** /team/{team_key}/event/{event_key}/awards | 
[**getTeamEventMatchesKeys_0**](EventApi.md#getTeamEventMatchesKeys_0) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
[**getTeamEventMatchesSimple_0**](EventApi.md#getTeamEventMatchesSimple_0) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
[**getTeamEventMatches_0**](EventApi.md#getTeamEventMatches_0) | **GET** /team/{team_key}/event/{event_key}/matches | 
[**getTeamEventStatus_0**](EventApi.md#getTeamEventStatus_0) | **GET** /team/{team_key}/event/{event_key}/status | 
[**getTeamEventsByYearKeys_0**](EventApi.md#getTeamEventsByYearKeys_0) | **GET** /team/{team_key}/events/{year}/keys | 
[**getTeamEventsByYearSimple_0**](EventApi.md#getTeamEventsByYearSimple_0) | **GET** /team/{team_key}/events/{year}/simple | 
[**getTeamEventsByYear_0**](EventApi.md#getTeamEventsByYear_0) | **GET** /team/{team_key}/events/{year} | 
[**getTeamEventsKeys_0**](EventApi.md#getTeamEventsKeys_0) | **GET** /team/{team_key}/events/keys | 
[**getTeamEventsSimple_0**](EventApi.md#getTeamEventsSimple_0) | **GET** /team/{team_key}/events/simple | 
[**getTeamEventsStatusesByYear_1**](EventApi.md#getTeamEventsStatusesByYear_1) | **GET** /team/{team_key}/events/{year}/statuses | 
[**getTeamEvents_0**](EventApi.md#getTeamEvents_0) | **GET** /team/{team_key}/events | 



## getDistrictEventsKeys_0

> [String] getDistrictEventsKeys_0(districtKey, opts)



Gets a list of event keys for events in the given district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEventsKeys_0(districtKey, opts, (error, data, response) => {
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
 **districtKey** | **String**| TBA District Key, eg &#x60;2016fim&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDistrictEventsSimple_0

> [EventSimple] getDistrictEventsSimple_0(districtKey, opts)



Gets a short-form list of events in the given district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEventsSimple_0(districtKey, opts, (error, data, response) => {
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
 **districtKey** | **String**| TBA District Key, eg &#x60;2016fim&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDistrictEvents_0

> [Event] getDistrictEvents_0(districtKey, opts)



Gets a list of events in the given district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEvents_0(districtKey, opts, (error, data, response) => {
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
 **districtKey** | **String**| TBA District Key, eg &#x60;2016fim&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvent

> Event getEvent(eventKey, opts)



Gets an Event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEvent(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventAlliances

> [EliminationAlliance] getEventAlliances(eventKey, opts)



Gets a list of Elimination Alliances for the given Event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventAlliances(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[EliminationAlliance]**](EliminationAlliance.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventAwards

> [Award] getEventAwards(eventKey, opts)



Gets a list of awards from the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventAwards(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Award]**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventDistrictPoints

> EventDistrictPoints getEventDistrictPoints(eventKey, opts)



Gets a list of team rankings for the Event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventDistrictPoints(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventDistrictPoints**](EventDistrictPoints.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventInsights

> EventInsights getEventInsights(eventKey, opts)



Gets a set of Event-specific insights for the given Event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventInsights(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventInsights**](EventInsights.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventMatchTimeseries

> [String] getEventMatchTimeseries(eventKey, opts)



Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatchTimeseries(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventMatches

> [Match] getEventMatches(eventKey, opts)



Gets a list of matches for the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatches(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventMatchesKeys

> [String] getEventMatchesKeys(eventKey, opts)



Gets a list of match keys for the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatchesKeys(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventMatchesSimple

> [MatchSimple] getEventMatchesSimple(eventKey, opts)



Gets a short-form list of matches for the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatchesSimple(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[MatchSimple]**](MatchSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventOPRs

> EventOPRs getEventOPRs(eventKey, opts)



Gets a set of Event OPRs (including OPR, DPR, and CCWM) for the given Event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventOPRs(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventOPRs**](EventOPRs.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventPredictions

> Object getEventPredictions(eventKey, opts)



Gets information on TBA-generated predictions for the given Event. Contains year-specific information. *WARNING* This endpoint is currently under development and may change at any time.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventPredictions(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventRankings

> EventRanking getEventRankings(eventKey, opts)



Gets a list of team rankings for the Event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventRankings(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventRanking**](EventRanking.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventSimple

> EventSimple getEventSimple(eventKey, opts)



Gets a short-form Event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventSimple(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**EventSimple**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventTeams

> [Team] getEventTeams(eventKey, opts)



Gets a list of &#x60;Team&#x60; objects that competed in the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeams(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventTeamsKeys

> [String] getEventTeamsKeys(eventKey, opts)



Gets a list of &#x60;Team&#x60; keys that competed in the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeamsKeys(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventTeamsSimple

> [TeamSimple] getEventTeamsSimple(eventKey, opts)



Gets a short-form list of &#x60;Team&#x60; objects that competed in the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeamsSimple(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventTeamsStatuses

> {String: TeamEventStatus} getEventTeamsStatuses(eventKey, opts)



Gets a key-value list of the event statuses for teams competing at the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeamsStatuses(eventKey, opts, (error, data, response) => {
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
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**{String: TeamEventStatus}**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsByYear

> [Event] getEventsByYear(year, opts)



Gets a list of events in the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventsByYear(year, opts, (error, data, response) => {
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
 **year** | **Number**| Competition Year (or Season). Must be 4 digits. | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsByYearKeys

> [String] getEventsByYearKeys(year, opts)



Gets a list of event keys in the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventsByYearKeys(year, opts, (error, data, response) => {
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
 **year** | **Number**| Competition Year (or Season). Must be 4 digits. | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsByYearSimple

> [EventSimple] getEventsByYearSimple(year, opts)



Gets a short-form list of events in the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventsByYearSimple(year, opts, (error, data, response) => {
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
 **year** | **Number**| Competition Year (or Season). Must be 4 digits. | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventAwards_0

> [Award] getTeamEventAwards_0(teamKey, eventKey, opts)



Gets a list of awards the given team won at the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventAwards_0(teamKey, eventKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Award]**](Award.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventMatchesKeys_0

> [String] getTeamEventMatchesKeys_0(teamKey, eventKey, opts)



Gets a list of match keys for matches for the given team and event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventMatchesKeys_0(teamKey, eventKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventMatchesSimple_0

> [Match] getTeamEventMatchesSimple_0(teamKey, eventKey, opts)



Gets a short-form list of matches for the given team and event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventMatchesSimple_0(teamKey, eventKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventMatches_0

> [Match] getTeamEventMatches_0(teamKey, eventKey, opts)



Gets a list of matches for the given team and event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventMatches_0(teamKey, eventKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventStatus_0

> TeamEventStatus getTeamEventStatus_0(teamKey, eventKey, opts)



Gets the competition rank and status of the team at the given event.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventStatus_0(teamKey, eventKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **eventKey** | **String**| TBA Event Key, eg &#x60;2016nytr&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**TeamEventStatus**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventsByYearKeys_0

> [String] getTeamEventsByYearKeys_0(teamKey, year, opts)



Gets a list of the event keys for events this team has competed at in the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventsByYearKeys_0(teamKey, year, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **Number**| Competition Year (or Season). Must be 4 digits. | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventsByYearSimple_0

> [EventSimple] getTeamEventsByYearSimple_0(teamKey, year, opts)



Gets a short-form list of events this team has competed at in the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventsByYearSimple_0(teamKey, year, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **Number**| Competition Year (or Season). Must be 4 digits. | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventsByYear_0

> [Event] getTeamEventsByYear_0(teamKey, year, opts)



Gets a list of events this team has competed at in the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventsByYear_0(teamKey, year, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **Number**| Competition Year (or Season). Must be 4 digits. | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventsKeys_0

> [String] getTeamEventsKeys_0(teamKey, opts)



Gets a list of the event keys for all events this team has competed at.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventsKeys_0(teamKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventsSimple_0

> [EventSimple] getTeamEventsSimple_0(teamKey, opts)



Gets a short-form list of all events this team has competed at.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventsSimple_0(teamKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[EventSimple]**](EventSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventsStatusesByYear_1

> {String: TeamEventStatus} getTeamEventsStatusesByYear_1(teamKey, year, opts)



Gets a key-value list of the event statuses for events this team has competed at in the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventsStatusesByYear_1(teamKey, year, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **year** | **Number**| Competition Year (or Season). Must be 4 digits. | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**{String: TeamEventStatus}**](TeamEventStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEvents_0

> [Event] getTeamEvents_0(teamKey, opts)



Gets a list of all events this team has competed at.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.EventApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEvents_0(teamKey, opts, (error, data, response) => {
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
 **teamKey** | **String**| TBA Team Key, eg &#x60;frc254&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Event]**](Event.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


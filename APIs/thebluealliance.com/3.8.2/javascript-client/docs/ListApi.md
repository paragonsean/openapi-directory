# TheBlueAllianceApiV3.ListApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistrictEventsKeys_1**](ListApi.md#getDistrictEventsKeys_1) | **GET** /district/{district_key}/events/keys | 
[**getDistrictEventsSimple_1**](ListApi.md#getDistrictEventsSimple_1) | **GET** /district/{district_key}/events/simple | 
[**getDistrictEvents_1**](ListApi.md#getDistrictEvents_1) | **GET** /district/{district_key}/events | 
[**getDistrictRankings_1**](ListApi.md#getDistrictRankings_1) | **GET** /district/{district_key}/rankings | 
[**getDistrictTeamsKeys_1**](ListApi.md#getDistrictTeamsKeys_1) | **GET** /district/{district_key}/teams/keys | 
[**getDistrictTeamsSimple_1**](ListApi.md#getDistrictTeamsSimple_1) | **GET** /district/{district_key}/teams/simple | 
[**getDistrictTeams_1**](ListApi.md#getDistrictTeams_1) | **GET** /district/{district_key}/teams | 
[**getEventTeamsKeys_1**](ListApi.md#getEventTeamsKeys_1) | **GET** /event/{event_key}/teams/keys | 
[**getEventTeamsSimple_1**](ListApi.md#getEventTeamsSimple_1) | **GET** /event/{event_key}/teams/simple | 
[**getEventTeamsStatuses_1**](ListApi.md#getEventTeamsStatuses_1) | **GET** /event/{event_key}/teams/statuses | 
[**getEventTeams_1**](ListApi.md#getEventTeams_1) | **GET** /event/{event_key}/teams | 
[**getEventsByYearKeys_0**](ListApi.md#getEventsByYearKeys_0) | **GET** /events/{year}/keys | 
[**getEventsByYearSimple_0**](ListApi.md#getEventsByYearSimple_0) | **GET** /events/{year}/simple | 
[**getEventsByYear_0**](ListApi.md#getEventsByYear_0) | **GET** /events/{year} | 
[**getTeamEventsStatusesByYear**](ListApi.md#getTeamEventsStatusesByYear) | **GET** /team/{team_key}/events/{year}/statuses | 
[**getTeamsByYearKeys_0**](ListApi.md#getTeamsByYearKeys_0) | **GET** /teams/{year}/{page_num}/keys | 
[**getTeamsByYearSimple_0**](ListApi.md#getTeamsByYearSimple_0) | **GET** /teams/{year}/{page_num}/simple | 
[**getTeamsByYear_0**](ListApi.md#getTeamsByYear_0) | **GET** /teams/{year}/{page_num} | 
[**getTeamsKeys_0**](ListApi.md#getTeamsKeys_0) | **GET** /teams/{page_num}/keys | 
[**getTeamsSimple_0**](ListApi.md#getTeamsSimple_0) | **GET** /teams/{page_num}/simple | 
[**getTeams_0**](ListApi.md#getTeams_0) | **GET** /teams/{page_num} | 



## getDistrictEventsKeys_1

> [String] getDistrictEventsKeys_1(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEventsKeys_1(districtKey, opts, (error, data, response) => {
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


## getDistrictEventsSimple_1

> [EventSimple] getDistrictEventsSimple_1(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEventsSimple_1(districtKey, opts, (error, data, response) => {
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


## getDistrictEvents_1

> [Event] getDistrictEvents_1(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEvents_1(districtKey, opts, (error, data, response) => {
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


## getDistrictRankings_1

> [DistrictRanking] getDistrictRankings_1(districtKey, opts)



Gets a list of team district rankings for the given district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictRankings_1(districtKey, opts, (error, data, response) => {
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

[**[DistrictRanking]**](DistrictRanking.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDistrictTeamsKeys_1

> [String] getDistrictTeamsKeys_1(districtKey, opts)



Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictTeamsKeys_1(districtKey, opts, (error, data, response) => {
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


## getDistrictTeamsSimple_1

> [TeamSimple] getDistrictTeamsSimple_1(districtKey, opts)



Gets a short-form list of &#x60;Team&#x60; objects that competed in events in the given district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictTeamsSimple_1(districtKey, opts, (error, data, response) => {
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

[**[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDistrictTeams_1

> [Team] getDistrictTeams_1(districtKey, opts)



Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictTeams_1(districtKey, opts, (error, data, response) => {
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

[**[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventTeamsKeys_1

> [String] getEventTeamsKeys_1(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeamsKeys_1(eventKey, opts, (error, data, response) => {
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


## getEventTeamsSimple_1

> [TeamSimple] getEventTeamsSimple_1(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeamsSimple_1(eventKey, opts, (error, data, response) => {
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


## getEventTeamsStatuses_1

> {String: TeamEventStatus} getEventTeamsStatuses_1(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeamsStatuses_1(eventKey, opts, (error, data, response) => {
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


## getEventTeams_1

> [Team] getEventTeams_1(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventTeams_1(eventKey, opts, (error, data, response) => {
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


## getEventsByYearKeys_0

> [String] getEventsByYearKeys_0(year, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventsByYearKeys_0(year, opts, (error, data, response) => {
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


## getEventsByYearSimple_0

> [EventSimple] getEventsByYearSimple_0(year, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventsByYearSimple_0(year, opts, (error, data, response) => {
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


## getEventsByYear_0

> [Event] getEventsByYear_0(year, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventsByYear_0(year, opts, (error, data, response) => {
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


## getTeamEventsStatusesByYear

> {String: TeamEventStatus} getTeamEventsStatusesByYear(teamKey, year, opts)



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

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventsStatusesByYear(teamKey, year, opts, (error, data, response) => {
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


## getTeamsByYearKeys_0

> [String] getTeamsByYearKeys_0(year, pageNum, opts)



Gets a list Team Keys that competed in the given year, paginated in groups of 500.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let pageNum = 56; // Number | Page number of results to return, zero-indexed
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamsByYearKeys_0(year, pageNum, opts, (error, data, response) => {
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
 **pageNum** | **Number**| Page number of results to return, zero-indexed | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamsByYearSimple_0

> [TeamSimple] getTeamsByYearSimple_0(year, pageNum, opts)



Gets a list of short form &#x60;Team_Simple&#x60; objects that competed in the given year, paginated in groups of 500.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let pageNum = 56; // Number | Page number of results to return, zero-indexed
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamsByYearSimple_0(year, pageNum, opts, (error, data, response) => {
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
 **pageNum** | **Number**| Page number of results to return, zero-indexed | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamsByYear_0

> [Team] getTeamsByYear_0(year, pageNum, opts)



Gets a list of &#x60;Team&#x60; objects that competed in the given year, paginated in groups of 500.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let pageNum = 56; // Number | Page number of results to return, zero-indexed
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamsByYear_0(year, pageNum, opts, (error, data, response) => {
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
 **pageNum** | **Number**| Page number of results to return, zero-indexed | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamsKeys_0

> [String] getTeamsKeys_0(pageNum, opts)



Gets a list of Team keys, paginated in groups of 500. (Note, each page will not have 500 teams, but will include the teams within that range of 500.)

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let pageNum = 56; // Number | Page number of results to return, zero-indexed
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamsKeys_0(pageNum, opts, (error, data, response) => {
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
 **pageNum** | **Number**| Page number of results to return, zero-indexed | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[String]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamsSimple_0

> [TeamSimple] getTeamsSimple_0(pageNum, opts)



Gets a list of short form &#x60;Team_Simple&#x60; objects, paginated in groups of 500.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let pageNum = 56; // Number | Page number of results to return, zero-indexed
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamsSimple_0(pageNum, opts, (error, data, response) => {
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
 **pageNum** | **Number**| Page number of results to return, zero-indexed | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[TeamSimple]**](TeamSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeams_0

> [Team] getTeams_0(pageNum, opts)



Gets a list of &#x60;Team&#x60; objects, paginated in groups of 500.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.ListApi();
let pageNum = 56; // Number | Page number of results to return, zero-indexed
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeams_0(pageNum, opts, (error, data, response) => {
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
 **pageNum** | **Number**| Page number of results to return, zero-indexed | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**[Team]**](Team.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


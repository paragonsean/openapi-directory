# TheBlueAllianceApiV3.DistrictApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistrictEvents**](DistrictApi.md#getDistrictEvents) | **GET** /district/{district_key}/events | 
[**getDistrictEventsKeys**](DistrictApi.md#getDistrictEventsKeys) | **GET** /district/{district_key}/events/keys | 
[**getDistrictEventsSimple**](DistrictApi.md#getDistrictEventsSimple) | **GET** /district/{district_key}/events/simple | 
[**getDistrictRankings**](DistrictApi.md#getDistrictRankings) | **GET** /district/{district_key}/rankings | 
[**getDistrictTeams**](DistrictApi.md#getDistrictTeams) | **GET** /district/{district_key}/teams | 
[**getDistrictTeamsKeys**](DistrictApi.md#getDistrictTeamsKeys) | **GET** /district/{district_key}/teams/keys | 
[**getDistrictTeamsSimple**](DistrictApi.md#getDistrictTeamsSimple) | **GET** /district/{district_key}/teams/simple | 
[**getDistrictsByYear**](DistrictApi.md#getDistrictsByYear) | **GET** /districts/{year} | 
[**getEventDistrictPoints_0**](DistrictApi.md#getEventDistrictPoints_0) | **GET** /event/{event_key}/district_points | 
[**getTeamDistricts_0**](DistrictApi.md#getTeamDistricts_0) | **GET** /team/{team_key}/districts | 



## getDistrictEvents

> [Event] getDistrictEvents(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEvents(districtKey, opts, (error, data, response) => {
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


## getDistrictEventsKeys

> [String] getDistrictEventsKeys(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEventsKeys(districtKey, opts, (error, data, response) => {
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


## getDistrictEventsSimple

> [EventSimple] getDistrictEventsSimple(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictEventsSimple(districtKey, opts, (error, data, response) => {
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


## getDistrictRankings

> [DistrictRanking] getDistrictRankings(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictRankings(districtKey, opts, (error, data, response) => {
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


## getDistrictTeams

> [Team] getDistrictTeams(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictTeams(districtKey, opts, (error, data, response) => {
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


## getDistrictTeamsKeys

> [String] getDistrictTeamsKeys(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictTeamsKeys(districtKey, opts, (error, data, response) => {
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


## getDistrictTeamsSimple

> [TeamSimple] getDistrictTeamsSimple(districtKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let districtKey = "districtKey_example"; // String | TBA District Key, eg `2016fim`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictTeamsSimple(districtKey, opts, (error, data, response) => {
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


## getDistrictsByYear

> [DistrictList] getDistrictsByYear(year, opts)



Gets a list of districts and their corresponding district key, for the given year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getDistrictsByYear(year, opts, (error, data, response) => {
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

[**[DistrictList]**](DistrictList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventDistrictPoints_0

> EventDistrictPoints getEventDistrictPoints_0(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventDistrictPoints_0(eventKey, opts, (error, data, response) => {
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


## getTeamDistricts_0

> [DistrictList] getTeamDistricts_0(teamKey, opts)



Gets an array of districts representing each year the team was in a district. Will return an empty array if the team was never in a district.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.DistrictApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamDistricts_0(teamKey, opts, (error, data, response) => {
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

[**[DistrictList]**](DistrictList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


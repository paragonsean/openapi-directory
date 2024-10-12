# TheBlueAllianceApiV3.MatchApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEventMatchTimeseries_0**](MatchApi.md#getEventMatchTimeseries_0) | **GET** /event/{event_key}/matches/timeseries | 
[**getEventMatchesKeys_0**](MatchApi.md#getEventMatchesKeys_0) | **GET** /event/{event_key}/matches/keys | 
[**getEventMatchesSimple_0**](MatchApi.md#getEventMatchesSimple_0) | **GET** /event/{event_key}/matches/simple | 
[**getEventMatches_0**](MatchApi.md#getEventMatches_0) | **GET** /event/{event_key}/matches | 
[**getMatch**](MatchApi.md#getMatch) | **GET** /match/{match_key} | 
[**getMatchSimple**](MatchApi.md#getMatchSimple) | **GET** /match/{match_key}/simple | 
[**getMatchTimeseries**](MatchApi.md#getMatchTimeseries) | **GET** /match/{match_key}/timeseries | 
[**getMatchZebra**](MatchApi.md#getMatchZebra) | **GET** /match/{match_key}/zebra_motionworks | 
[**getTeamEventMatchesKeys_1**](MatchApi.md#getTeamEventMatchesKeys_1) | **GET** /team/{team_key}/event/{event_key}/matches/keys | 
[**getTeamEventMatchesSimple_1**](MatchApi.md#getTeamEventMatchesSimple_1) | **GET** /team/{team_key}/event/{event_key}/matches/simple | 
[**getTeamEventMatches_1**](MatchApi.md#getTeamEventMatches_1) | **GET** /team/{team_key}/event/{event_key}/matches | 
[**getTeamMatchesByYearKeys_0**](MatchApi.md#getTeamMatchesByYearKeys_0) | **GET** /team/{team_key}/matches/{year}/keys | 
[**getTeamMatchesByYearSimple_0**](MatchApi.md#getTeamMatchesByYearSimple_0) | **GET** /team/{team_key}/matches/{year}/simple | 
[**getTeamMatchesByYear_0**](MatchApi.md#getTeamMatchesByYear_0) | **GET** /team/{team_key}/matches/{year} | 



## getEventMatchTimeseries_0

> [String] getEventMatchTimeseries_0(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatchTimeseries_0(eventKey, opts, (error, data, response) => {
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


## getEventMatchesKeys_0

> [String] getEventMatchesKeys_0(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatchesKeys_0(eventKey, opts, (error, data, response) => {
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


## getEventMatchesSimple_0

> [MatchSimple] getEventMatchesSimple_0(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatchesSimple_0(eventKey, opts, (error, data, response) => {
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


## getEventMatches_0

> [Match] getEventMatches_0(eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getEventMatches_0(eventKey, opts, (error, data, response) => {
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


## getMatch

> Match getMatch(matchKey, opts)



Gets a &#x60;Match&#x60; object for the given match key.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let matchKey = "matchKey_example"; // String | TBA Match Key, eg `2016nytr_qm1`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getMatch(matchKey, opts, (error, data, response) => {
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
 **matchKey** | **String**| TBA Match Key, eg &#x60;2016nytr_qm1&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**Match**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMatchSimple

> MatchSimple getMatchSimple(matchKey, opts)



Gets a short-form &#x60;Match&#x60; object for the given match key.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let matchKey = "matchKey_example"; // String | TBA Match Key, eg `2016nytr_qm1`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getMatchSimple(matchKey, opts, (error, data, response) => {
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
 **matchKey** | **String**| TBA Match Key, eg &#x60;2016nytr_qm1&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**MatchSimple**](MatchSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMatchTimeseries

> [Object] getMatchTimeseries(matchKey, opts)



Gets an array of game-specific Match Timeseries objects for the given match key or an empty array if not available. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let matchKey = "matchKey_example"; // String | TBA Match Key, eg `2016nytr_qm1`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getMatchTimeseries(matchKey, opts, (error, data, response) => {
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
 **matchKey** | **String**| TBA Match Key, eg &#x60;2016nytr_qm1&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

**[Object]**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMatchZebra

> Zebra getMatchZebra(matchKey, opts)



Gets Zebra MotionWorks data for a Match for the given match key.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let matchKey = "matchKey_example"; // String | TBA Match Key, eg `2016nytr_qm1`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getMatchZebra(matchKey, opts, (error, data, response) => {
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
 **matchKey** | **String**| TBA Match Key, eg &#x60;2016nytr_qm1&#x60; | 
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**Zebra**](Zebra.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamEventMatchesKeys_1

> [String] getTeamEventMatchesKeys_1(teamKey, eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventMatchesKeys_1(teamKey, eventKey, opts, (error, data, response) => {
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


## getTeamEventMatchesSimple_1

> [Match] getTeamEventMatchesSimple_1(teamKey, eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventMatchesSimple_1(teamKey, eventKey, opts, (error, data, response) => {
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


## getTeamEventMatches_1

> [Match] getTeamEventMatches_1(teamKey, eventKey, opts)



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

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let eventKey = "eventKey_example"; // String | TBA Event Key, eg `2016nytr`
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamEventMatches_1(teamKey, eventKey, opts, (error, data, response) => {
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


## getTeamMatchesByYearKeys_0

> [String] getTeamMatchesByYearKeys_0(teamKey, year, opts)



Gets a list of match keys for matches for the given team and year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamMatchesByYearKeys_0(teamKey, year, opts, (error, data, response) => {
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


## getTeamMatchesByYearSimple_0

> [MatchSimple] getTeamMatchesByYearSimple_0(teamKey, year, opts)



Gets a short-form list of matches for the given team and year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamMatchesByYearSimple_0(teamKey, year, opts, (error, data, response) => {
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

[**[MatchSimple]**](MatchSimple.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamMatchesByYear_0

> [Match] getTeamMatchesByYear_0(teamKey, year, opts)



Gets a list of matches for the given team and year.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.MatchApi();
let teamKey = "teamKey_example"; // String | TBA Team Key, eg `frc254`
let year = 56; // Number | Competition Year (or Season). Must be 4 digits.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getTeamMatchesByYear_0(teamKey, year, opts, (error, data, response) => {
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

[**[Match]**](Match.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


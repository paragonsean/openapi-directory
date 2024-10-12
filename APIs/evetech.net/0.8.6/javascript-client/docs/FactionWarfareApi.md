# EveSwaggerInterface.FactionWarfareApi

All URIs are relative to *https://esi.evetech.net/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCharactersCharacterIdFwStats**](FactionWarfareApi.md#getCharactersCharacterIdFwStats) | **GET** /characters/{character_id}/fw/stats/ | Overview of a character involved in faction warfare
[**getCorporationsCorporationIdFwStats**](FactionWarfareApi.md#getCorporationsCorporationIdFwStats) | **GET** /corporations/{corporation_id}/fw/stats/ | Overview of a corporation involved in faction warfare
[**getFwLeaderboards**](FactionWarfareApi.md#getFwLeaderboards) | **GET** /fw/leaderboards/ | List of the top factions in faction warfare
[**getFwLeaderboardsCharacters**](FactionWarfareApi.md#getFwLeaderboardsCharacters) | **GET** /fw/leaderboards/characters/ | List of the top pilots in faction warfare
[**getFwLeaderboardsCorporations**](FactionWarfareApi.md#getFwLeaderboardsCorporations) | **GET** /fw/leaderboards/corporations/ | List of the top corporations in faction warfare
[**getFwStats**](FactionWarfareApi.md#getFwStats) | **GET** /fw/stats/ | An overview of statistics about factions involved in faction warfare
[**getFwSystems**](FactionWarfareApi.md#getFwSystems) | **GET** /fw/systems/ | Ownership of faction warfare systems
[**getFwWars**](FactionWarfareApi.md#getFwWars) | **GET** /fw/wars/ | Data about which NPC factions are at war



## getCharactersCharacterIdFwStats

> GetCharactersCharacterIdFwStatsOk getCharactersCharacterIdFwStats(characterId, opts)

Overview of a character involved in faction warfare

Statistical overview of a character involved in faction warfare  --- Alternate route: &#x60;/dev/characters/{character_id}/fw/stats/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/fw/stats/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/fw/stats/&#x60;  --- This route expires daily at 11:05

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let characterId = 56; // Number | An EVE character ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCharactersCharacterIdFwStats(characterId, opts, (error, data, response) => {
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
 **characterId** | **Number**| An EVE character ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCharactersCharacterIdFwStatsOk**](GetCharactersCharacterIdFwStatsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorporationsCorporationIdFwStats

> GetCorporationsCorporationIdFwStatsOk getCorporationsCorporationIdFwStats(corporationId, opts)

Overview of a corporation involved in faction warfare

Statistics about a corporation involved in faction warfare  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/fw/stats/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/fw/stats/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/fw/stats/&#x60;  --- This route expires daily at 11:05

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';
let defaultClient = EveSwaggerInterface.ApiClient.instance;
// Configure OAuth2 access token for authorization: evesso
let evesso = defaultClient.authentications['evesso'];
evesso.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let corporationId = 56; // Number | An EVE corporation ID
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
  'token': "token_example" // String | Access token to use if unable to set a header
};
apiInstance.getCorporationsCorporationIdFwStats(corporationId, opts, (error, data, response) => {
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
 **corporationId** | **Number**| An EVE corporation ID | 
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 
 **token** | **String**| Access token to use if unable to set a header | [optional] 

### Return type

[**GetCorporationsCorporationIdFwStatsOk**](GetCorporationsCorporationIdFwStatsOk.md)

### Authorization

[evesso](../README.md#evesso)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFwLeaderboards

> GetFwLeaderboardsOk getFwLeaderboards(opts)

List of the top factions in faction warfare

Top 4 leaderboard of factions for kills and victory points separated by total, last week and yesterday  --- Alternate route: &#x60;/dev/fw/leaderboards/&#x60;  Alternate route: &#x60;/legacy/fw/leaderboards/&#x60;  Alternate route: &#x60;/v1/fw/leaderboards/&#x60;  --- This route expires daily at 11:05

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getFwLeaderboards(opts, (error, data, response) => {
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
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetFwLeaderboardsOk**](GetFwLeaderboardsOk.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFwLeaderboardsCharacters

> GetFwLeaderboardsCharactersOk getFwLeaderboardsCharacters(opts)

List of the top pilots in faction warfare

Top 100 leaderboard of pilots for kills and victory points separated by total, last week and yesterday  --- Alternate route: &#x60;/dev/fw/leaderboards/characters/&#x60;  Alternate route: &#x60;/legacy/fw/leaderboards/characters/&#x60;  Alternate route: &#x60;/v1/fw/leaderboards/characters/&#x60;  --- This route expires daily at 11:05

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getFwLeaderboardsCharacters(opts, (error, data, response) => {
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
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetFwLeaderboardsCharactersOk**](GetFwLeaderboardsCharactersOk.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFwLeaderboardsCorporations

> GetFwLeaderboardsCorporationsOk getFwLeaderboardsCorporations(opts)

List of the top corporations in faction warfare

Top 10 leaderboard of corporations for kills and victory points separated by total, last week and yesterday  --- Alternate route: &#x60;/dev/fw/leaderboards/corporations/&#x60;  Alternate route: &#x60;/legacy/fw/leaderboards/corporations/&#x60;  Alternate route: &#x60;/v1/fw/leaderboards/corporations/&#x60;  --- This route expires daily at 11:05

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getFwLeaderboardsCorporations(opts, (error, data, response) => {
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
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**GetFwLeaderboardsCorporationsOk**](GetFwLeaderboardsCorporationsOk.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFwStats

> [GetFwStats200Ok] getFwStats(opts)

An overview of statistics about factions involved in faction warfare

Statistical overviews of factions involved in faction warfare  --- Alternate route: &#x60;/dev/fw/stats/&#x60;  Alternate route: &#x60;/legacy/fw/stats/&#x60;  Alternate route: &#x60;/v1/fw/stats/&#x60;  --- This route expires daily at 11:05

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getFwStats(opts, (error, data, response) => {
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
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**[GetFwStats200Ok]**](GetFwStats200Ok.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFwSystems

> [GetFwSystems200Ok] getFwSystems(opts)

Ownership of faction warfare systems

An overview of the current ownership of faction warfare solar systems  --- Alternate route: &#x60;/dev/fw/systems/&#x60;  Alternate route: &#x60;/v2/fw/systems/&#x60;  --- This route is cached for up to 1800 seconds

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getFwSystems(opts, (error, data, response) => {
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
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**[GetFwSystems200Ok]**](GetFwSystems200Ok.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFwWars

> [GetFwWars200Ok] getFwWars(opts)

Data about which NPC factions are at war

Data about which NPC factions are at war  --- Alternate route: &#x60;/dev/fw/wars/&#x60;  Alternate route: &#x60;/legacy/fw/wars/&#x60;  Alternate route: &#x60;/v1/fw/wars/&#x60;  --- This route expires daily at 11:05

### Example

```javascript
import EveSwaggerInterface from 'eve_swagger_interface';

let apiInstance = new EveSwaggerInterface.FactionWarfareApi();
let opts = {
  'datasource': "'tranquility'", // String | The server name you would like data from
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
};
apiInstance.getFwWars(opts, (error, data, response) => {
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
 **datasource** | **String**| The server name you would like data from | [optional] [default to &#39;tranquility&#39;]
 **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] 

### Return type

[**[GetFwWars200Ok]**](GetFwWars200Ok.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


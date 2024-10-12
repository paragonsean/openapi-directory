# ApiVideo.PlayersApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dELETEPlayersPlayerId**](PlayersApi.md#dELETEPlayersPlayerId) | **DELETE** /players/{playerId} | Delete a player
[**dELETEPlayersPlayerIdLogo**](PlayersApi.md#dELETEPlayersPlayerIdLogo) | **DELETE** /players/{playerId}/logo | Delete logo
[**gETPlayers**](PlayersApi.md#gETPlayers) | **GET** /players | List all players
[**gETPlayersPlayerId**](PlayersApi.md#gETPlayersPlayerId) | **GET** /players/{playerId} | Show a player
[**pATCHPlayersPlayerId**](PlayersApi.md#pATCHPlayersPlayerId) | **PATCH** /players/{playerId} | Update a player
[**pOSTPlayers**](PlayersApi.md#pOSTPlayers) | **POST** /players | Create a player
[**pOSTPlayersPlayerIdLogo**](PlayersApi.md#pOSTPlayersPlayerIdLogo) | **POST** /players/{playerId}/logo | Upload a logo



## dELETEPlayersPlayerId

> dELETEPlayersPlayerId(playerId)

Delete a player

Delete a player if you no longer need it. You can delete any player that you have the player ID for.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.PlayersApi();
let playerId = "pl45d5vFFGrfdsdsd156dGhh"; // String | The unique identifier for the player you want to delete.
apiInstance.dELETEPlayersPlayerId(playerId, (error, data, response) => {
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
 **playerId** | **String**| The unique identifier for the player you want to delete. | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dELETEPlayersPlayerIdLogo

> Object dELETEPlayersPlayerIdLogo(playerId)

Delete logo

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.PlayersApi();
let playerId = "pl14Db6oMJRH6SRVoOwORacK"; // String | The unique identifier for the player.
apiInstance.dELETEPlayersPlayerIdLogo(playerId, (error, data, response) => {
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
 **playerId** | **String**| The unique identifier for the player. | 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETPlayers

> PlayersListResponse gETPlayers(opts)

List all players

Retrieve a list of all the players you created, as well as details about each one. Tutorials that use the [player endpoint](https://api.video/blog/endpoints/player).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.PlayersApi();
let opts = {
  'sortBy': "createdAt", // String | createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format.
  'sortOrder': "asc", // String | Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones.
  'currentPage': 2, // Number | Choose the number of search results to return per page. Minimum value: 1
  'pageSize': 30 // Number | Results per page. Allowed values 1-100, default is 25.
};
apiInstance.gETPlayers(opts, (error, data, response) => {
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
 **sortBy** | **String**| createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format. | [optional] 
 **sortOrder** | **String**| Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones. | [optional] 
 **currentPage** | **Number**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1]
 **pageSize** | **Number**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25]

### Return type

[**PlayersListResponse**](PlayersListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETPlayersPlayerId

> Player gETPlayersPlayerId(playerId)

Show a player

Use a player ID to retrieve details about the player and display it for viewers.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.PlayersApi();
let playerId = "pl45d5vFFGrfdsdsd156dGhh"; // String | The unique identifier for the player you want to retrieve. 
apiInstance.gETPlayersPlayerId(playerId, (error, data, response) => {
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
 **playerId** | **String**| The unique identifier for the player you want to retrieve.  | 

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pATCHPlayersPlayerId

> Player pATCHPlayersPlayerId(playerId, playerUpdatePayload)

Update a player

Use a player ID to update specific details for a player. NOTE: It may take up to 10 min before the new player configuration is available from our CDN.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.PlayersApi();
let playerId = "pl45d5vFFGrfdsdsd156dGhh"; // String | The unique identifier for the player.
let playerUpdatePayload = new ApiVideo.PlayerUpdatePayload(); // PlayerUpdatePayload | 
apiInstance.pATCHPlayersPlayerId(playerId, playerUpdatePayload, (error, data, response) => {
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
 **playerId** | **String**| The unique identifier for the player. | 
 **playerUpdatePayload** | [**PlayerUpdatePayload**](PlayerUpdatePayload.md)|  | 

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pOSTPlayers

> Player pOSTPlayers(playerCreationPayload)

Create a player

Create a player for your video, and customise it.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.PlayersApi();
let playerCreationPayload = new ApiVideo.PlayerCreationPayload(); // PlayerCreationPayload | 
apiInstance.pOSTPlayers(playerCreationPayload, (error, data, response) => {
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
 **playerCreationPayload** | [**PlayerCreationPayload**](PlayerCreationPayload.md)|  | 

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pOSTPlayersPlayerIdLogo

> Player pOSTPlayersPlayerIdLogo(playerId, file, link)

Upload a logo

The uploaded image maximum size should be 200x100 and its weight should be 200KB.  It will be scaled down to 30px height and converted to PNG to be displayed in the player.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.PlayersApi();
let playerId = "pl14Db6oMJRH6SRVoOwORacK"; // String | The unique identifier for the player.
let file = "/path/to/file"; // File | The name of the file you want to use for your logo.
let link = "link_example"; // String | The path to the file you want to upload and use as a logo.
apiInstance.pOSTPlayersPlayerIdLogo(playerId, file, link, (error, data, response) => {
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
 **playerId** | **String**| The unique identifier for the player. | 
 **file** | **File**| The name of the file you want to use for your logo. | 
 **link** | **String**| The path to the file you want to upload and use as a logo. | 

### Return type

[**Player**](Player.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


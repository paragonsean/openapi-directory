# GameSparksGameDetailsApi.GamesAdminApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGamesEndpointsUsingGET**](GamesAdminApi.md#getGamesEndpointsUsingGET) | **GET** /restv2/game/{apiKey}/endpoints | getGamesEndpoints
[**listDeletedUsingGET**](GamesAdminApi.md#listDeletedUsingGET) | **GET** /restv2/games/deleted | listDeleted
[**listUsingGET**](GamesAdminApi.md#listUsingGET) | **GET** /restv2/games | list
[**restoreDeletedGameUsingPOST**](GamesAdminApi.md#restoreDeletedGameUsingPOST) | **POST** /restv2/game/{apiKey}/restore | restoreDeletedGame



## getGamesEndpointsUsingGET

> GameEndpointsModel getGamesEndpointsUsingGET(apiKey)

getGamesEndpoints

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.GamesAdminApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getGamesEndpointsUsingGET(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 

### Return type

[**GameEndpointsModel**](GameEndpointsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## listDeletedUsingGET

> [DeletedGameModel] listDeletedUsingGET()

listDeleted

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.GamesAdminApi();
apiInstance.listDeletedUsingGET((error, data, response) => {
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

[**[DeletedGameModel]**](DeletedGameModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## listUsingGET

> [GameModel] listUsingGET()

list

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.GamesAdminApi();
apiInstance.listUsingGET((error, data, response) => {
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

[**[GameModel]**](GameModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## restoreDeletedGameUsingPOST

> MessageModel restoreDeletedGameUsingPOST(apiKey)

restoreDeletedGame

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.GamesAdminApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.restoreDeletedGameUsingPOST(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| apiKey | 

### Return type

[**MessageModel**](MessageModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


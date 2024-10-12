# GameSparksGameDetailsApi.RegionApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGameRegionOptionsUsingGET**](RegionApi.md#getGameRegionOptionsUsingGET) | **GET** /restv2/game/{gameApiKey}/regions | getGameRegionOptions
[**getRegionOptionsUsingGET**](RegionApi.md#getRegionOptionsUsingGET) | **GET** /restv2/game/regions | getRegionOptions
[**setGameRegionUsingPOST**](RegionApi.md#setGameRegionUsingPOST) | **POST** /restv2/game/{gameApiKey}/region/{regionCode} | setGameRegion



## getGameRegionOptionsUsingGET

> GameRegionOptionsDTO getGameRegionOptionsUsingGET(gameApiKey)

getGameRegionOptions

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.RegionApi();
let gameApiKey = "gameApiKey_example"; // String | gameApiKey
apiInstance.getGameRegionOptionsUsingGET(gameApiKey, (error, data, response) => {
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
 **gameApiKey** | **String**| gameApiKey | 

### Return type

[**GameRegionOptionsDTO**](GameRegionOptionsDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getRegionOptionsUsingGET

> GameRegionOptionsDTO getRegionOptionsUsingGET()

getRegionOptions

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.RegionApi();
apiInstance.getRegionOptionsUsingGET((error, data, response) => {
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

[**GameRegionOptionsDTO**](GameRegionOptionsDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## setGameRegionUsingPOST

> RegionResult setGameRegionUsingPOST(gameApiKey, regionCode)

setGameRegion

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.RegionApi();
let gameApiKey = "gameApiKey_example"; // String | gameApiKey
let regionCode = "regionCode_example"; // String | regionCode
apiInstance.setGameRegionUsingPOST(gameApiKey, regionCode, (error, data, response) => {
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
 **gameApiKey** | **String**| gameApiKey | 
 **regionCode** | **String**| regionCode | 

### Return type

[**RegionResult**](RegionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


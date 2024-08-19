# Balldontlie.GamesApi

All URIs are relative to *https://balldontlie.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allGamesExampleParameters**](GamesApi.md#allGamesExampleParameters) | **GET** /api/v1/games | all games (example parameters)
[**specificGame**](GamesApi.md#specificGame) | **GET** /api/v1/games/32881 | specific game



## allGamesExampleParameters

> allGamesExampleParameters(opts)

all games (example parameters)

all games (example parameters)

### Example

```javascript
import Balldontlie from 'balldontlie';

let apiInstance = new Balldontlie.GamesApi();
let opts = {
  'seasons': "2018", // String | 
  'teamIds': "1" // String | 
};
apiInstance.allGamesExampleParameters(opts, (error, data, response) => {
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
 **seasons** | **String**|  | [optional] 
 **teamIds** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## specificGame

> specificGame()

specific game

specific game

### Example

```javascript
import Balldontlie from 'balldontlie';

let apiInstance = new Balldontlie.GamesApi();
apiInstance.specificGame((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


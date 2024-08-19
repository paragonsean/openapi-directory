# Balldontlie.PlayersApi

All URIs are relative to *https://balldontlie.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allPlayersSearch**](PlayersApi.md#allPlayersSearch) | **GET** /api/v1/players | all players (search)
[**specificPlayer**](PlayersApi.md#specificPlayer) | **GET** /api/v1/players/237 | specific player



## allPlayersSearch

> allPlayersSearch(opts)

all players (search)

all players (search)

### Example

```javascript
import Balldontlie from 'balldontlie';

let apiInstance = new Balldontlie.PlayersApi();
let opts = {
  'search': "lebron" // String | 
};
apiInstance.allPlayersSearch(opts, (error, data, response) => {
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
 **search** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## specificPlayer

> specificPlayer()

specific player

specific player

### Example

```javascript
import Balldontlie from 'balldontlie';

let apiInstance = new Balldontlie.PlayersApi();
apiInstance.specificPlayer((error, data, response) => {
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


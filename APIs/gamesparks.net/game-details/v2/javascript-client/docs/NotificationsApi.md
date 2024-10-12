# GameSparksGameDetailsApi.NotificationsApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGameSummaryUsingGET**](NotificationsApi.md#getGameSummaryUsingGET) | **GET** /restv2/game/{apiKey}/admin/notifications/summary | getGameSummary



## getGameSummaryUsingGET

> GameSummaryModel getGameSummaryUsingGET(apiKey, stage, startDate, endDate)

getGameSummary

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.NotificationsApi();
let apiKey = "apiKey_example"; // String | apiKey
let stage = "stage_example"; // String | stage
let startDate = new Date("2013-10-20"); // Date | yyyy-MM-dd
let endDate = new Date("2013-10-20"); // Date | yyyy-MM-dd
apiInstance.getGameSummaryUsingGET(apiKey, stage, startDate, endDate, (error, data, response) => {
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
 **stage** | **String**| stage | 
 **startDate** | **Date**| yyyy-MM-dd | 
 **endDate** | **Date**| yyyy-MM-dd | 

### Return type

[**GameSummaryModel**](GameSummaryModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


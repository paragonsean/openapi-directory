# GameSparksGameDetailsApi.AnalyticsApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAnalyticsDataUsingGET**](AnalyticsApi.md#getAnalyticsDataUsingGET) | **GET** /restv2/game/{apiKey}/admin/analytics | Returns the results of executed query defined by the parameters passed in
[**getDataCountUsingGET**](AnalyticsApi.md#getDataCountUsingGET) | **GET** /restv2/game/{apiKey}/admin/analytics/count | Returns the count of executed query
[**getRetentionUsingGET**](AnalyticsApi.md#getRetentionUsingGET) | **GET** /restv2/game/{apiKey}/admin/analytics/rollingRetention | Returns the percentage of user retention over the last 30 days



## getAnalyticsDataUsingGET

> [AnalyticsDataSwaggerModel] getAnalyticsDataUsingGET(apiKey, stage, dataType, precision, startDate, endDate, opts)

Returns the results of executed query defined by the parameters passed in

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.AnalyticsApi();
let apiKey = "apiKey_example"; // String | apiKey
let stage = "stage_example"; // String | stage
let dataType = "dataType_example"; // String | dataType
let precision = "precision_example"; // String | precision
let startDate = new Date("2013-10-20"); // Date | yyyy-MM-dd
let endDate = new Date("2013-10-20"); // Date | yyyy-MM-dd
let opts = {
  'keys': "keys_example" // String | the keys to select. For example \"ReturningUsers\", \"NewUsers\", etc
};
apiInstance.getAnalyticsDataUsingGET(apiKey, stage, dataType, precision, startDate, endDate, opts, (error, data, response) => {
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
 **dataType** | **String**| dataType | 
 **precision** | **String**| precision | 
 **startDate** | **Date**| yyyy-MM-dd | 
 **endDate** | **Date**| yyyy-MM-dd | 
 **keys** | **String**| the keys to select. For example \&quot;ReturningUsers\&quot;, \&quot;NewUsers\&quot;, etc | [optional] 

### Return type

[**[AnalyticsDataSwaggerModel]**](AnalyticsDataSwaggerModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getDataCountUsingGET

> AnalyticsDataCountSwaggerModel getDataCountUsingGET(apiKey, stage, queryName)

Returns the count of executed query

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.AnalyticsApi();
let apiKey = "apiKey_example"; // String | apiKey
let stage = "stage_example"; // String | stage
let queryName = "queryName_example"; // String | queryName
apiInstance.getDataCountUsingGET(apiKey, stage, queryName, (error, data, response) => {
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
 **queryName** | **String**| queryName | 

### Return type

[**AnalyticsDataCountSwaggerModel**](AnalyticsDataCountSwaggerModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getRetentionUsingGET

> AnalyticsDataCountSwaggerModel getRetentionUsingGET(apiKey, stage)

Returns the percentage of user retention over the last 30 days

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.AnalyticsApi();
let apiKey = "apiKey_example"; // String | apiKey
let stage = "stage_example"; // String | stage
apiInstance.getRetentionUsingGET(apiKey, stage, (error, data, response) => {
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

### Return type

[**AnalyticsDataCountSwaggerModel**](AnalyticsDataCountSwaggerModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


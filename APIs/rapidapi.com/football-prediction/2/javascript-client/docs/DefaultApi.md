# FootballPredictionApi.DefaultApi

All URIs are relative to *https://football-prediction-api.p.rapidapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2ListFederationsGet**](DefaultApi.md#apiV2ListFederationsGet) | **GET** /api/v2/list-federations | 
[**apiV2ListMarketsGet**](DefaultApi.md#apiV2ListMarketsGet) | **GET** /api/v2/list-markets | 
[**apiV2PerformanceStatsGet**](DefaultApi.md#apiV2PerformanceStatsGet) | **GET** /api/v2/performance-stats | 
[**apiV2PredictionsGet**](DefaultApi.md#apiV2PredictionsGet) | **GET** /api/v2/predictions | 
[**apiV2PredictionsIdGet**](DefaultApi.md#apiV2PredictionsIdGet) | **GET** /api/v2/predictions/{id} | 



## apiV2ListFederationsGet

> ApiV2ListFederationsGet200Response apiV2ListFederationsGet(opts)



Returns an array of all the available federations.

### Example

```javascript
import FootballPredictionApi from 'football_prediction_api';

let apiInstance = new FootballPredictionApi.DefaultApi();
let opts = {
  'xRapidApiKey': "xRapidApiKey_example" // String | Your key obtained from https://boggio-analytics.com/fp-api/
};
apiInstance.apiV2ListFederationsGet(opts, (error, data, response) => {
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
 **xRapidApiKey** | **String**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] 

### Return type

[**ApiV2ListFederationsGet200Response**](ApiV2ListFederationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2ListMarketsGet

> ApiV2ListMarketsGet200Response apiV2ListMarketsGet(opts)



Returns an array of all the supported prediction markets

### Example

```javascript
import FootballPredictionApi from 'football_prediction_api';

let apiInstance = new FootballPredictionApi.DefaultApi();
let opts = {
  'xRapidApiKey': "xRapidApiKey_example" // String | Your key obtained from https://boggio-analytics.com/fp-api/
};
apiInstance.apiV2ListMarketsGet(opts, (error, data, response) => {
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
 **xRapidApiKey** | **String**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] 

### Return type

[**ApiV2ListMarketsGet200Response**](ApiV2ListMarketsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2PerformanceStatsGet

> ApiV2PerformanceStatsGet200Response apiV2PerformanceStatsGet(opts)



Returns predictions accuracy in the last 1, 7, 14, 30 days.

### Example

```javascript
import FootballPredictionApi from 'football_prediction_api';

let apiInstance = new FootballPredictionApi.DefaultApi();
let opts = {
  'xRapidApiKey': "xRapidApiKey_example" // String | Your key obtained from https://boggio-analytics.com/fp-api/
};
apiInstance.apiV2PerformanceStatsGet(opts, (error, data, response) => {
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
 **xRapidApiKey** | **String**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] 

### Return type

[**ApiV2PerformanceStatsGet200Response**](ApiV2PerformanceStatsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2PredictionsGet

> apiV2PredictionsGet(opts)



This endpoint returns by default the next non-expired football predictions. URL parameters can be specified to show specific date in the past or future or to filter by federation and prediction market name.

### Example

```javascript
import FootballPredictionApi from 'football_prediction_api';

let apiInstance = new FootballPredictionApi.DefaultApi();
let opts = {
  'xRapidApiKey': "xRapidApiKey_example" // String | Your key obtained from https://boggio-analytics.com/fp-api/
};
apiInstance.apiV2PredictionsGet(opts, (error, data, response) => {
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
 **xRapidApiKey** | **String**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2PredictionsIdGet

> ApiV2PredictionsIdGet200Response apiV2PredictionsIdGet(id)



Returns all predictions available for a match id.

### Example

```javascript
import FootballPredictionApi from 'football_prediction_api';

let apiInstance = new FootballPredictionApi.DefaultApi();
let id = 56; // Number | ID of match
apiInstance.apiV2PredictionsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of match | 

### Return type

[**ApiV2PredictionsIdGet200Response**](ApiV2PredictionsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


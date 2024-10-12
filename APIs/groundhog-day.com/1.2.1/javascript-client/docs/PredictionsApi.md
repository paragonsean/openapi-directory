# GroundhogDayApi.PredictionsApi

All URIs are relative to *https://virtserver.swaggerhub.com/pcraig3/groundhog-day-api/1.2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predictions**](PredictionsApi.md#predictions) | **GET** /api/v1/predictions | Get predictions for a given year



## predictions

> Predictions200Response predictions(opts)

Get predictions for a given year

Get all predictions for a given year.

### Example

```javascript
import GroundhogDayApi from 'groundhog_day_api';

let apiInstance = new GroundhogDayApi.PredictionsApi();
let opts = {
  'year': 56 // Number | A calendar year
};
apiInstance.predictions(opts, (error, data, response) => {
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
 **year** | **Number**| A calendar year | [optional] 

### Return type

[**Predictions200Response**](Predictions200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


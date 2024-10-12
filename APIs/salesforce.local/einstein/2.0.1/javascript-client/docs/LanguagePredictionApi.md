# EinsteinVisionAndEinsteinLanguage.LanguagePredictionApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**intentMultipart**](LanguagePredictionApi.md#intentMultipart) | **POST** /v2/language/intent | Prediction for Intent
[**sentimentMultipart**](LanguagePredictionApi.md#sentimentMultipart) | **POST** /v2/language/sentiment | Prediction for Sentiment



## intentMultipart

> IntentPredictResponse intentMultipart(opts)

Prediction for Intent

Returns an intent prediction for the given string.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguagePredictionApi();
let opts = {
  'intentPredictRequest': new EinsteinVisionAndEinsteinLanguage.IntentPredictRequest() // IntentPredictRequest | 
};
apiInstance.intentMultipart(opts, (error, data, response) => {
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
 **intentPredictRequest** | [**IntentPredictRequest**](IntentPredictRequest.md)|  | [optional] 

### Return type

[**IntentPredictResponse**](IntentPredictResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


## sentimentMultipart

> SentimentPredictResponse sentimentMultipart(opts)

Prediction for Sentiment

Returns a sentiment prediction for the given string.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguagePredictionApi();
let opts = {
  'sentimentPredictRequest': new EinsteinVisionAndEinsteinLanguage.SentimentPredictRequest() // SentimentPredictRequest | 
};
apiInstance.sentimentMultipart(opts, (error, data, response) => {
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
 **sentimentPredictRequest** | [**SentimentPredictRequest**](SentimentPredictRequest.md)|  | [optional] 

### Return type

[**SentimentPredictResponse**](SentimentPredictResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


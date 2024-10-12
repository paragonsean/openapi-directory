# MotaWordApi.MachineLearningApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeliveryPrediction**](MachineLearningApi.md#getDeliveryPrediction) | **POST** /ml/delivery-prediction | Get a delivery prediction for a project



## getDeliveryPrediction

> DeliveryPredictionResponse getDeliveryPrediction(opts)

Get a delivery prediction for a project

Get a delivery prediction for a project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.MachineLearningApi();
let opts = {
  'deliveryPredictionPayload': new MotaWordApi.DeliveryPredictionPayload() // DeliveryPredictionPayload | 
};
apiInstance.getDeliveryPrediction(opts, (error, data, response) => {
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
 **deliveryPredictionPayload** | [**DeliveryPredictionPayload**](DeliveryPredictionPayload.md)|  | [optional] 

### Return type

[**DeliveryPredictionResponse**](DeliveryPredictionResponse.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


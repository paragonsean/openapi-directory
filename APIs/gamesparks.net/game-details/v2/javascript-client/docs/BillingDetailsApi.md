# GameSparksGameDetailsApi.BillingDetailsApi

All URIs are relative to *http://config2.gamesparks.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBillingDetails**](BillingDetailsApi.md#getBillingDetails) | **GET** /restv2/game/{apiKey}/admin/billingDetails | Retrieves the Billing Details
[**putBillingDetails**](BillingDetailsApi.md#putBillingDetails) | **PUT** /restv2/game/{apiKey}/admin/billingDetails | Updates the Billing Details



## getBillingDetails

> BillingDetailsModel getBillingDetails(apiKey)

Retrieves the Billing Details

Retrieves the Billing Details.

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.BillingDetailsApi();
let apiKey = "apiKey_example"; // String | apiKey
apiInstance.getBillingDetails(apiKey, (error, data, response) => {
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

[**BillingDetailsModel**](BillingDetailsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## putBillingDetails

> BillingDetailsModel putBillingDetails(apiKey, billingDetailsModel)

Updates the Billing Details

Updates the Billing Details.

### Example

```javascript
import GameSparksGameDetailsApi from 'game_sparks_game_details_api';

let apiInstance = new GameSparksGameDetailsApi.BillingDetailsApi();
let apiKey = "apiKey_example"; // String | apiKey
let billingDetailsModel = new GameSparksGameDetailsApi.BillingDetailsModel(); // BillingDetailsModel | billingDetails
apiInstance.putBillingDetails(apiKey, billingDetailsModel, (error, data, response) => {
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
 **billingDetailsModel** | [**BillingDetailsModel**](BillingDetailsModel.md)| billingDetails | 

### Return type

[**BillingDetailsModel**](BillingDetailsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


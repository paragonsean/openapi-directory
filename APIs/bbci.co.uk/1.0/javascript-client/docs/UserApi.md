# BbcIPlayerBusinessLayer.UserApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserStorePurchases**](UserApi.md#getUserStorePurchases) | **GET** /user/purchases | Get user store purchases
[**getUserStoreRecommendations**](UserApi.md#getUserStoreRecommendations) | **GET** /user/recommendations | Get user store recommendations
[**getUserWatching**](UserApi.md#getUserWatching) | **GET** /user/watching | Get user watching



## getUserStorePurchases

> Object getUserStorePurchases(identityCookie)

Get user store purchases

Get user store purchases

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';
let defaultClient = BbcIPlayerBusinessLayer.ApiClient.instance;
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BbcIPlayerBusinessLayer.UserApi();
let identityCookie = 3.4; // Number | The BBC-id cookie value
apiInstance.getUserStorePurchases(identityCookie, (error, data, response) => {
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
 **identityCookie** | **Number**| The BBC-id cookie value | 

### Return type

**Object**

### Authorization

[basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserStoreRecommendations

> Object getUserStoreRecommendations(identityCookie)

Get user store recommendations

Get user store recommendations

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.UserApi();
let identityCookie = 3.4; // Number | The BBC-id cookie value
apiInstance.getUserStoreRecommendations(identityCookie, (error, data, response) => {
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
 **identityCookie** | **Number**| The BBC-id cookie value | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserWatching

> Object getUserWatching(identityCookie)

Get user watching

Get user watching

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.UserApi();
let identityCookie = 3.4; // Number | The BBC-id cookie value
apiInstance.getUserWatching(identityCookie, (error, data, response) => {
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
 **identityCookie** | **Number**| The BBC-id cookie value | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


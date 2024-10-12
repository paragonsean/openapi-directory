# ClickMeterApi.MeApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meGetMe**](MeApi.md#meGetMe) | **GET** /me | Retrieve current account data
[**meGetMePlan**](MeApi.md#meGetMePlan) | **GET** /me/plan | Retrieve current account plan



## meGetMe

> ApiCoreDtoAccountingUser meGetMe()

Retrieve current account data

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.MeApi();
apiInstance.meGetMe((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiCoreDtoAccountingUser**](ApiCoreDtoAccountingUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## meGetMePlan

> ApiCoreDtoAccountingPlan meGetMePlan()

Retrieve current account plan

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.MeApi();
apiInstance.meGetMePlan((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiCoreDtoAccountingPlan**](ApiCoreDtoAccountingPlan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


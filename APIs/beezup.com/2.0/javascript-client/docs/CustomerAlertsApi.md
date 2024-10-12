# BeezUpMerchantApi.CustomerAlertsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStoreAlerts**](CustomerAlertsApi.md#getStoreAlerts) | **GET** /v2/user/customer/stores/{storeId}/alerts | Get store&#39;s alerts
[**saveStoreAlerts**](CustomerAlertsApi.md#saveStoreAlerts) | **POST** /v2/user/customer/stores/{storeId}/alerts | Save store alerts



## getStoreAlerts

> StoreAlerts getStoreAlerts(storeId, opts)

Get store&#39;s alerts

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAlertsApi();
let storeId = "storeId_example"; // String | Your store identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getStoreAlerts(storeId, opts, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**StoreAlerts**](StoreAlerts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveStoreAlerts

> saveStoreAlerts(storeId, requestBody)

Save store alerts

You just have to send the alert you want to update, does not need all alerts. (PARTIAL UPDATE ACCEPTED)

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerAlertsApi();
let storeId = "storeId_example"; // String | Your store identifier
let requestBody = {key: new BeezUpMerchantApi.SaveStoreAlertRequest()}; // {String: SaveStoreAlertRequest} | 
apiInstance.saveStoreAlerts(storeId, requestBody, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **requestBody** | [**{String: SaveStoreAlertRequest}**](SaveStoreAlertRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


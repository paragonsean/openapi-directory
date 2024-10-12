# BeezUpMerchantApi.CustomerRightsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRights**](CustomerRightsApi.md#getRights) | **GET** /v2/user/customer/stores/{storeId}/rights | Get store&#39;s rights



## getRights

> [FunctionalityRightInfo] getRights(storeId)

Get store&#39;s rights

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerRightsApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.getRights(storeId, (error, data, response) => {
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

### Return type

[**[FunctionalityRightInfo]**](FunctionalityRightInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


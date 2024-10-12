# SpendingPulse.SubscriptionApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionGet**](SubscriptionApi.md#subscriptionGet) | **GET** /subscription | Returns a list of all reports one is currently subscribed to.



## subscriptionGet

> SubscriptionListResponse subscriptionGet(opts)

Returns a list of all reports one is currently subscribed to.

Returns a list of all reports one is currently subscribed to. 

### Example

```javascript
import SpendingPulse from 'spending_pulse';

let apiInstance = new SpendingPulse.SubscriptionApi();
let opts = {
  'currentRow': "1", // String | Starting record number to return.
  'offset': "25" // String | Used to restrict the number of records returned if needed to be less than max.
};
apiInstance.subscriptionGet(opts, (error, data, response) => {
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
 **currentRow** | **String**| Starting record number to return. | [optional] 
 **offset** | **String**| Used to restrict the number of records returned if needed to be less than max. | [optional] 

### Return type

[**SubscriptionListResponse**](SubscriptionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# ClimateKuulLive.UrbanDeliveryApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirmCarbonOffset**](UrbanDeliveryApi.md#confirmCarbonOffset) | **PATCH** /urbanDelivery/confirmCarbonOffset | confirmCarbonOffset
[**confirmPayment**](UrbanDeliveryApi.md#confirmPayment) | **PATCH** /urbanDelivery/confirmPayment | confirmPayment
[**confirmPaymentOfTransaction**](UrbanDeliveryApi.md#confirmPaymentOfTransaction) | **PATCH** /urbanDelivery/confirmTransaction | confirmTransaction
[**confirmsPlanting**](UrbanDeliveryApi.md#confirmsPlanting) | **PATCH** /urbanDelivery/confirmPlanting | confirmPlanting
[**urbanDelivery**](UrbanDeliveryApi.md#urbanDelivery) | **POST** /urbanDelivery | urbanDelivery



## confirmCarbonOffset

> confirmCarbonOffset(carbonOffset, transactionId, opts)

confirmCarbonOffset

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.UrbanDeliveryApi();
let carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
let opts = {
  'contactEmail': "contactEmail_example", // String | Contact email
  'contactFirstName': "contactFirstName_example", // String | Contact first name
  'contactLastName': "contactLastName_example" // String | Contact last name
};
apiInstance.confirmCarbonOffset(carbonOffset, transactionId, opts, (error, data, response) => {
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
 **carbonOffset** | **String**| Confirm Carbon Offset (Value &#x3D; y/n) | 
 **transactionId** | **String**| transaction_id | 
 **contactEmail** | **String**| Contact email | [optional] 
 **contactFirstName** | **String**| Contact first name | [optional] 
 **contactLastName** | **String**| Contact last name | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## confirmPayment

> confirmPayment(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.UrbanDeliveryApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
let paymentID = 56; // Number | Payment Id
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPayment(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId, (error, data, response) => {
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
 **apiKeyL1** | **String**| apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560) | 
 **apiKeyL2** | **String**| apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166) | 
 **confirmPayment** | **String**| Confirm Payment (Value &#x3D; y/n) | 
 **paymentID** | **Number**| Payment Id | 
 **transactionId** | **String**| transaction_id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## confirmPaymentOfTransaction

> confirmPaymentOfTransaction(confirmTransaction, transactionId)

confirmTransaction

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.UrbanDeliveryApi();
let confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPaymentOfTransaction(confirmTransaction, transactionId, (error, data, response) => {
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
 **confirmTransaction** | **String**| Confirm Payment Of Transaction (Value &#x3D; y/n) | 
 **transactionId** | **String**| transaction_id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## confirmsPlanting

> confirmsPlanting(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.UrbanDeliveryApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmsPlanting(apiKeyL1, apiKeyL2, confirmPlanting, transactionId, (error, data, response) => {
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
 **apiKeyL1** | **String**| apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560) | 
 **apiKeyL2** | **String**| apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166) | 
 **confirmPlanting** | **String**| Confirm Planting (Value &#x3D; y/n) | 
 **transactionId** | **String**| transaction_id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## urbanDelivery

> urbanDelivery(apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, itemCount, originLatitude, originLongitude, vehicleType)

urbanDelivery

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.UrbanDeliveryApi();
let apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
let apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
let destinationLatitude = 3.4; // Number | Destination latitude (like: 50.870752, value = -90<=x<=90)
let destinationLongitude = 3.4; // Number | Destination longitude (like: 4.669490, value = -180<=x<=180)
let itemCount = 56; // Number | item_count' (like:2, value = 0<x<=100)
let originLatitude = 3.4; // Number | Origin latitude (like: 23.372628, value = -90<=x<=90)
let originLongitude = 3.4; // Number | Origin longitude (like: 113.159339, value = -180<=x<=180)
let vehicleType = "vehicleType_example"; // String | Vehicle type (like: private car, motorcycle,cargo van,zero-emission)
apiInstance.urbanDelivery(apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, itemCount, originLatitude, originLongitude, vehicleType, (error, data, response) => {
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
 **apiKeyL1** | **String**| Client Api Key | 
 **apiKeyL2** | **String**| Integration Partner Api Key | 
 **destinationLatitude** | **Number**| Destination latitude (like: 50.870752, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90) | 
 **destinationLongitude** | **Number**| Destination longitude (like: 4.669490, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180) | 
 **itemCount** | **Number**| item_count&#39; (like:2, value &#x3D; 0&lt;x&lt;&#x3D;100) | 
 **originLatitude** | **Number**| Origin latitude (like: 23.372628, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90) | 
 **originLongitude** | **Number**| Origin longitude (like: 113.159339, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180) | 
 **vehicleType** | **String**| Vehicle type (like: private car, motorcycle,cargo van,zero-emission) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


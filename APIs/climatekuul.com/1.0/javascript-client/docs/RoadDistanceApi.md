# ClimateKuulLive.RoadDistanceApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirmCarbonOffset5**](RoadDistanceApi.md#confirmCarbonOffset5) | **PATCH** /roadDistance/confirmCarbonOffset | confirmCarbonOffset
[**confirmPayment5**](RoadDistanceApi.md#confirmPayment5) | **PATCH** /roadDistance/confirmPayment | confirmPayment
[**confirmPaymentOfTransaction5**](RoadDistanceApi.md#confirmPaymentOfTransaction5) | **PATCH** /roadDistance/confirmTransaction | confirmTransaction
[**confirmsPlanting5**](RoadDistanceApi.md#confirmsPlanting5) | **PATCH** /roadDistance/confirmPlanting | confirmPlanting
[**roadDistance**](RoadDistanceApi.md#roadDistance) | **POST** /roadDistance | RoadDistance



## confirmCarbonOffset5

> confirmCarbonOffset5(carbonOffset, transactionId, opts)

confirmCarbonOffset

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.RoadDistanceApi();
let carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
let opts = {
  'contactEmail': "contactEmail_example", // String | Contact email
  'contactFirstName': "contactFirstName_example", // String | Contact first name
  'contactLastName': "contactLastName_example" // String | Contact last name
};
apiInstance.confirmCarbonOffset5(carbonOffset, transactionId, opts, (error, data, response) => {
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


## confirmPayment5

> confirmPayment5(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.RoadDistanceApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
let paymentID = 56; // Number | Payment Id
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPayment5(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId, (error, data, response) => {
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


## confirmPaymentOfTransaction5

> confirmPaymentOfTransaction5(confirmTransaction, transactionId)

confirmTransaction

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.RoadDistanceApi();
let confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPaymentOfTransaction5(confirmTransaction, transactionId, (error, data, response) => {
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


## confirmsPlanting5

> confirmsPlanting5(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.RoadDistanceApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmsPlanting5(apiKeyL1, apiKeyL2, confirmPlanting, transactionId, (error, data, response) => {
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


## roadDistance

> roadDistance(apiKeyL1, apiKeyL2, travelDistance, tripEnd, tripStart, vehicleType, opts)

RoadDistance

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.RoadDistanceApi();
let apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
let apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
let travelDistance = 56; // Number | 
let tripEnd = 56; // Number | timestamp in epoch time (like: 1606780799)
let tripStart = 56; // Number | timestamp in epoch time (like: 1604188800)
let vehicleType = "vehicleType_example"; // String | Vehicle type can be 'personal car', 'light truck' or 'heavy-duty truck'
let opts = {
  'vehicleMake': "vehicleMake_example", // String | vehicle make (like: Honda, Toyota, Smart), Required only when vehicle_type is 'personal car' 
  'vehicleYear': 56 // Number | vehicle year (like: 2010, 2015, 2019), Required only when vehicle_type is 'personal car' 
};
apiInstance.roadDistance(apiKeyL1, apiKeyL2, travelDistance, tripEnd, tripStart, vehicleType, opts, (error, data, response) => {
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
 **travelDistance** | **Number**|  | 
 **tripEnd** | **Number**| timestamp in epoch time (like: 1606780799) | 
 **tripStart** | **Number**| timestamp in epoch time (like: 1604188800) | 
 **vehicleType** | **String**| Vehicle type can be &#39;personal car&#39;, &#39;light truck&#39; or &#39;heavy-duty truck&#39; | 
 **vehicleMake** | **String**| vehicle make (like: Honda, Toyota, Smart), Required only when vehicle_type is &#39;personal car&#39;  | [optional] 
 **vehicleYear** | **Number**| vehicle year (like: 2010, 2015, 2019), Required only when vehicle_type is &#39;personal car&#39;  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


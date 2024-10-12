# ClimateKuulLive.EcommerceDeliveryApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirmCarbonOffset1**](EcommerceDeliveryApi.md#confirmCarbonOffset1) | **PATCH** /ecommerceDelivery/confirmCarbonOffset | confirmCarbonOffset
[**confirmPayment1**](EcommerceDeliveryApi.md#confirmPayment1) | **PATCH** /ecommerceDelivery/confirmPayment | confirmPayment
[**confirmPaymentOfTransaction1**](EcommerceDeliveryApi.md#confirmPaymentOfTransaction1) | **PATCH** /ecommerceDelivery/confirmTransaction | confirmTransaction
[**confirmsPlanting2**](EcommerceDeliveryApi.md#confirmsPlanting2) | **PATCH** /ecommerceDelivery/confirmPlanting | confirmPlanting
[**ecommerceDelivery**](EcommerceDeliveryApi.md#ecommerceDelivery) | **POST** /ecommerceDelivery | ecommerceDelivery



## confirmCarbonOffset1

> confirmCarbonOffset1(carbonOffset, transactionId, opts)

confirmCarbonOffset

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.EcommerceDeliveryApi();
let carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
let opts = {
  'contactEmail': "contactEmail_example", // String | Contact email
  'contactFirstName': "contactFirstName_example", // String | Contact first name
  'contactLastName': "contactLastName_example" // String | Contact last name
};
apiInstance.confirmCarbonOffset1(carbonOffset, transactionId, opts, (error, data, response) => {
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


## confirmPayment1

> confirmPayment1(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.EcommerceDeliveryApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
let paymentID = 56; // Number | Payment Id
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPayment1(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId, (error, data, response) => {
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


## confirmPaymentOfTransaction1

> confirmPaymentOfTransaction1(confirmTransaction, transactionId)

confirmTransaction

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.EcommerceDeliveryApi();
let confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPaymentOfTransaction1(confirmTransaction, transactionId, (error, data, response) => {
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


## confirmsPlanting2

> confirmsPlanting2(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.EcommerceDeliveryApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmsPlanting2(apiKeyL1, apiKeyL2, confirmPlanting, transactionId, (error, data, response) => {
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


## ecommerceDelivery

> ecommerceDelivery(contentType, apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, originLatitude, originLongitude, volumetricWeight, waybillType, opts)

ecommerceDelivery

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.EcommerceDeliveryApi();
let contentType = "application/x-www-form-urlencoded"; // String | 
let apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
let apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
let destinationLatitude = 3.4; // Number | valid latitude of destination
let destinationLongitude = 3.4; // Number | valid longitude of destination
let originLatitude = 3.4; // Number | valid latitude of origin
let originLongitude = 3.4; // Number | valid longitude of origin
let volumetricWeight = 3.4; // Number | Volumetric weight' (like:2.70)
let waybillType = "waybillType_example"; // String | this can be 'air only', 'road only' or 'air and road'
let opts = {
  'destinationAirportCode': "destinationAirportCode_example", // String | valid airport code of destination
  'originAirportCode': "originAirportCode_example" // String | valid airport code of origin
};
apiInstance.ecommerceDelivery(contentType, apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, originLatitude, originLongitude, volumetricWeight, waybillType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **apiKeyL1** | **String**| Client Api Key | 
 **apiKeyL2** | **String**| Integration Partner Api Key | 
 **destinationLatitude** | **Number**| valid latitude of destination | 
 **destinationLongitude** | **Number**| valid longitude of destination | 
 **originLatitude** | **Number**| valid latitude of origin | 
 **originLongitude** | **Number**| valid longitude of origin | 
 **volumetricWeight** | **Number**| Volumetric weight&#39; (like:2.70) | 
 **waybillType** | **String**| this can be &#39;air only&#39;, &#39;road only&#39; or &#39;air and road&#39; | 
 **destinationAirportCode** | **String**| valid airport code of destination | [optional] 
 **originAirportCode** | **String**| valid airport code of origin | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


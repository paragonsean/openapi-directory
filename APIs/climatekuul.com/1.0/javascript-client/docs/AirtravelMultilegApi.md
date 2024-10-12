# ClimateKuulLive.AirtravelMultilegApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airtravelMultileg**](AirtravelMultilegApi.md#airtravelMultileg) | **POST** /airtravelMultileg | airtravelMultileg
[**confirmCarbonOffset3**](AirtravelMultilegApi.md#confirmCarbonOffset3) | **PATCH** /airtravelMultileg/confirmCarbonOffset | confirmCarbonOffset
[**confirmPayment3**](AirtravelMultilegApi.md#confirmPayment3) | **PATCH** /airtravelMultileg/confirmPayment | confirmPayment
[**confirmPaymentOfTransaction3**](AirtravelMultilegApi.md#confirmPaymentOfTransaction3) | **PATCH** /airtravelMultileg/confirmTransaction | confirmTransaction
[**confirmsPlanting3**](AirtravelMultilegApi.md#confirmsPlanting3) | **PATCH** /airtravelMultileg/confirmPlanting | confirmPlanting



## airtravelMultileg

> airtravelMultileg(airtravelMultilegRequest)

airtravelMultileg

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelMultilegApi();
let airtravelMultilegRequest = {"apiKey_l1":"d95fead6-e8a6-4547-9fb9-7835101a3960","apiKey_l2":"c60f8db5-7204-4427-960d-27400c38b166","leg1":{"destination_airport_code":"DXB","origin_airport_code":"KHI","travel_class":"Economy"},"leg2":{"destination_airport_code":"LHR","origin_airport_code":"DXB","travel_class":"Business"},"leg3":{"destination_airport_code":"KHI","origin_airport_code":"FRA","travel_class":"Premium Economy"},"legs_count":"2","number_of_passengers":"2","travel_mode":"multileg"}; // AirtravelMultilegRequest | 
apiInstance.airtravelMultileg(airtravelMultilegRequest, (error, data, response) => {
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
 **airtravelMultilegRequest** | [**AirtravelMultilegRequest**](AirtravelMultilegRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## confirmCarbonOffset3

> confirmCarbonOffset3(carbonOffset, transactionId, opts)

confirmCarbonOffset

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelMultilegApi();
let carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
let opts = {
  'contactEmail': "contactEmail_example", // String | Contact email
  'contactFirstName': "contactFirstName_example", // String | Contact first name
  'contactLastName': "contactLastName_example" // String | Contact last name
};
apiInstance.confirmCarbonOffset3(carbonOffset, transactionId, opts, (error, data, response) => {
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


## confirmPayment3

> confirmPayment3(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelMultilegApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
let paymentID = 56; // Number | Payment Id
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPayment3(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId, (error, data, response) => {
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


## confirmPaymentOfTransaction3

> confirmPaymentOfTransaction3(confirmTransaction, transactionId)

confirmTransaction

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelMultilegApi();
let confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPaymentOfTransaction3(confirmTransaction, transactionId, (error, data, response) => {
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


## confirmsPlanting3

> confirmsPlanting3(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelMultilegApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmsPlanting3(apiKeyL1, apiKeyL2, confirmPlanting, transactionId, (error, data, response) => {
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


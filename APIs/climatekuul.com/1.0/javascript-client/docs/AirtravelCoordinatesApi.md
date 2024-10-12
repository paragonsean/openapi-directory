# ClimateKuulLive.AirtravelCoordinatesApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airtravelCoordinates**](AirtravelCoordinatesApi.md#airtravelCoordinates) | **POST** /airtravelCoordinates | airtravelCoordinates
[**confirmCarbonOffset4**](AirtravelCoordinatesApi.md#confirmCarbonOffset4) | **PATCH** /airtravelCoordinates/confirmCarbonOffset | confirmCarbonOffset
[**confirmPayment4**](AirtravelCoordinatesApi.md#confirmPayment4) | **PATCH** /airtravelCoordinates/confirmPayment | confirmPayment
[**confirmPaymentOfTransaction4**](AirtravelCoordinatesApi.md#confirmPaymentOfTransaction4) | **PATCH** /airtravelCoordinates/confirmTransaction | confirmTransaction
[**confirmsPlanting4**](AirtravelCoordinatesApi.md#confirmsPlanting4) | **PATCH** /airtravelCoordinates/confirmPlanting | confirmPlanting



## airtravelCoordinates

> airtravelCoordinates(contentType, apiKeyL1, apiKeyL2, destinationAirportLatitude, destinationAirportLongitude, numberOfPassengers, originAirportLatitude, originAirportLongitude, travelClass, travelMode)

airtravelCoordinates

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelCoordinatesApi();
let contentType = "application/x-www-form-urlencoded"; // String | 
let apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
let apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
let destinationAirportLatitude = 3.4; // Number | Destination latitude (like:  50.870752, value = -90<=x<=90)
let destinationAirportLongitude = 3.4; // Number | Destination longitude (like:  4.669490, value = -180<=x<=180)
let numberOfPassengers = 56; // Number | Number of passengers (like: 1, 2 ,3 )
let originAirportLatitude = 3.4; // Number | Origin latitude (like: 23.372628 value = -90<=x<=90 )
let originAirportLongitude = 3.4; // Number | Origin longitude (like: 113.159339, value = -180<=x<=180 )
let travelClass = "travelClass_example"; // String | Travel class can be 'First Class', 'Economy', 'Business' or 'Premium Economy'
let travelMode = "travelMode_example"; // String | Travel mode can be 'one way' or 'round trip'
apiInstance.airtravelCoordinates(contentType, apiKeyL1, apiKeyL2, destinationAirportLatitude, destinationAirportLongitude, numberOfPassengers, originAirportLatitude, originAirportLongitude, travelClass, travelMode, (error, data, response) => {
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
 **destinationAirportLatitude** | **Number**| Destination latitude (like:  50.870752, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90) | 
 **destinationAirportLongitude** | **Number**| Destination longitude (like:  4.669490, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180) | 
 **numberOfPassengers** | **Number**| Number of passengers (like: 1, 2 ,3 ) | 
 **originAirportLatitude** | **Number**| Origin latitude (like: 23.372628 value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90 ) | 
 **originAirportLongitude** | **Number**| Origin longitude (like: 113.159339, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180 ) | 
 **travelClass** | **String**| Travel class can be &#39;First Class&#39;, &#39;Economy&#39;, &#39;Business&#39; or &#39;Premium Economy&#39; | 
 **travelMode** | **String**| Travel mode can be &#39;one way&#39; or &#39;round trip&#39; | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## confirmCarbonOffset4

> confirmCarbonOffset4(carbonOffset, transactionId, opts)

confirmCarbonOffset

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelCoordinatesApi();
let carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
let opts = {
  'contactEmail': "contactEmail_example", // String | Contact email
  'contactFirstName': "contactFirstName_example", // String | Contact first name
  'contactLastName': "contactLastName_example" // String | Contact last name
};
apiInstance.confirmCarbonOffset4(carbonOffset, transactionId, opts, (error, data, response) => {
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


## confirmPayment4

> confirmPayment4(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelCoordinatesApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
let paymentID = 56; // Number | Payment Id
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPayment4(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId, (error, data, response) => {
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


## confirmPaymentOfTransaction4

> confirmPaymentOfTransaction4(confirmTransaction, transactionId)

confirmTransaction

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelCoordinatesApi();
let confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmPaymentOfTransaction4(confirmTransaction, transactionId, (error, data, response) => {
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


## confirmsPlanting4

> confirmsPlanting4(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.AirtravelCoordinatesApi();
let apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
let apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
let confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
let transactionId = "transactionId_example"; // String | transaction_id
apiInstance.confirmsPlanting4(apiKeyL1, apiKeyL2, confirmPlanting, transactionId, (error, data, response) => {
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


# SendPersonToMerchant.TransferNotificationRegistrationApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTransferNotificationRegistration**](TransferNotificationRegistrationApi.md#createTransferNotificationRegistration) | **POST** /send/v1/partners/{partnerId}/notification-registries | This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.
[**deleteTransferNotificationRegistration**](TransferNotificationRegistrationApi.md#deleteTransferNotificationRegistration) | **DELETE** /send/v1/partners/{partnerId}/notification-registries/{account-reg-ref} | This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 
[**notificationRegistrationAPIReadBy**](TransferNotificationRegistrationApi.md#notificationRegistrationAPIReadBy) | **GET** /send/v1/partners/{partnerId}/notification-registries/{account-reg-ref} | This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications. 
[**notificationRegistrationAPIUpdate**](TransferNotificationRegistrationApi.md#notificationRegistrationAPIUpdate) | **PUT** /send/v1/partners/{partnerId}/notification-registries/{account-reg-ref} | This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.



## createTransferNotificationRegistration

> Accountregistration168Wrapper createTransferNotificationRegistration(partnerId, opts)

This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.

This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.TransferNotificationRegistrationApi();
let partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
let opts = {
  'accountregistration': new SendPersonToMerchant.Accountregistration167Wrapper() // Accountregistration167Wrapper | Contains the details of the request message.
};
apiInstance.createTransferNotificationRegistration(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | 
 **accountregistration** | [**Accountregistration167Wrapper**](Accountregistration167Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**Accountregistration168Wrapper**](Accountregistration168Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## deleteTransferNotificationRegistration

> Accountregistration171Wrapper deleteTransferNotificationRegistration(partnerId, accountRegRef)

This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 

This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.TransferNotificationRegistrationApi();
let partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
let accountRegRef = "areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF"; // String | Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40
apiInstance.deleteTransferNotificationRegistration(partnerId, accountRegRef, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | 
 **accountRegRef** | **String**| Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40 | 

### Return type

[**Accountregistration171Wrapper**](Accountregistration171Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## notificationRegistrationAPIReadBy

> Accountregistration172Wrapper notificationRegistrationAPIReadBy(partnerId, accountRegRef)

This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications. 

This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications. 

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.TransferNotificationRegistrationApi();
let partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
let accountRegRef = "areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF"; // String | Path Param - System generated unique account registration identifier. Type: Alphanumberic Special Length: 40
apiInstance.notificationRegistrationAPIReadBy(partnerId, accountRegRef, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | 
 **accountRegRef** | **String**| Path Param - System generated unique account registration identifier. Type: Alphanumberic Special Length: 40 | 

### Return type

[**Accountregistration172Wrapper**](Accountregistration172Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## notificationRegistrationAPIUpdate

> Accountregistration170Wrapper notificationRegistrationAPIUpdate(partnerId, accountRegRef, opts)

This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.

This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.TransferNotificationRegistrationApi();
let partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
let accountRegRef = "areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF"; // String | Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40
let opts = {
  'accountregistration': new SendPersonToMerchant.Accountregistration169Wrapper() // Accountregistration169Wrapper | Contains the details of the request message.
};
apiInstance.notificationRegistrationAPIUpdate(partnerId, accountRegRef, opts, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | 
 **accountRegRef** | **String**| Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40 | 
 **accountregistration** | [**Accountregistration169Wrapper**](Accountregistration169Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**Accountregistration170Wrapper**](Accountregistration170Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


# HandwryttenApi.AddressApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addRecipientAddress**](AddressApi.md#addRecipientAddress) | **POST** /profile/profileAddRecipient | add a new recipient address
[**deleteRecipient**](AddressApi.md#deleteRecipient) | **POST** /profile/deleteRecipient | deletes an existing recipient address
[**recipientsList**](AddressApi.md#recipientsList) | **POST** /profile/recipientsList | list the addresses in the user&#39;s account
[**updateRecipient**](AddressApi.md#updateRecipient) | **POST** /profile/updateRecipient | updates an existing new recipient address



## addRecipientAddress

> AddRecipientAddress200Response addRecipientAddress(opts)

add a new recipient address

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AddressApi();
let opts = {
  'body': new HandwryttenApi.AddRecipientAddressRequest() // AddRecipientAddressRequest | additional parameters
};
apiInstance.addRecipientAddress(opts, (error, data, response) => {
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
 **body** | [**AddRecipientAddressRequest**](AddRecipientAddressRequest.md)| additional parameters | [optional] 

### Return type

[**AddRecipientAddress200Response**](AddRecipientAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRecipient

> DeleteRecipient200Response deleteRecipient(body)

deletes an existing recipient address

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AddressApi();
let body = new HandwryttenApi.DeleteRecipientRequest(); // DeleteRecipientRequest | additional parameters
apiInstance.deleteRecipient(body, (error, data, response) => {
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
 **body** | [**DeleteRecipientRequest**](DeleteRecipientRequest.md)| additional parameters | 

### Return type

[**DeleteRecipient200Response**](DeleteRecipient200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recipientsList

> [RecipientAddress] recipientsList(body)

list the addresses in the user&#39;s account

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AddressApi();
let body = new HandwryttenApi.RecipientsListRequest(); // RecipientsListRequest | additional parameters
apiInstance.recipientsList(body, (error, data, response) => {
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
 **body** | [**RecipientsListRequest**](RecipientsListRequest.md)| additional parameters | 

### Return type

[**[RecipientAddress]**](RecipientAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRecipient

> AddRecipientAddress200Response updateRecipient(body)

updates an existing new recipient address

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.AddressApi();
let body = new HandwryttenApi.UpdateRecipientRequest(); // UpdateRecipientRequest | additional parameters
apiInstance.updateRecipient(body, (error, data, response) => {
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
 **body** | [**UpdateRecipientRequest**](UpdateRecipientRequest.md)| additional parameters | 

### Return type

[**AddRecipientAddress200Response**](AddRecipientAddress200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


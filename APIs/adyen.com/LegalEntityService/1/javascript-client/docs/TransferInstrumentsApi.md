# LegalEntityManagementApi.TransferInstrumentsApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteTransferInstrumentsId**](TransferInstrumentsApi.md#deleteTransferInstrumentsId) | **DELETE** /transferInstruments/{id} | Delete a transfer instrument
[**getTransferInstrumentsId**](TransferInstrumentsApi.md#getTransferInstrumentsId) | **GET** /transferInstruments/{id} | Get a transfer instrument
[**patchTransferInstrumentsId**](TransferInstrumentsApi.md#patchTransferInstrumentsId) | **PATCH** /transferInstruments/{id} | Update a transfer instrument
[**postTransferInstruments**](TransferInstrumentsApi.md#postTransferInstruments) | **POST** /transferInstruments | Create a transfer instrument



## deleteTransferInstrumentsId

> deleteTransferInstrumentsId(id)

Delete a transfer instrument

Deletes a transfer instrument.

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.TransferInstrumentsApi();
let id = "id_example"; // String | The unique identifier of the transfer instrument to be deleted.
apiInstance.deleteTransferInstrumentsId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the transfer instrument to be deleted. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransferInstrumentsId

> TransferInstrument getTransferInstrumentsId(id)

Get a transfer instrument

Returns the details of a transfer instrument.

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.TransferInstrumentsApi();
let id = "id_example"; // String | The unique identifier of the transfer instrument.
apiInstance.getTransferInstrumentsId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the transfer instrument. | 

### Return type

[**TransferInstrument**](TransferInstrument.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchTransferInstrumentsId

> TransferInstrument patchTransferInstrumentsId(id, opts)

Update a transfer instrument

Updates a transfer instrument.

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.TransferInstrumentsApi();
let id = "id_example"; // String | The unique identifier of the transfer instrument.
let opts = {
  'xRequestedVerificationCode': "1", // String | Use the requested verification code 0_0001 to resolve any suberrors associated with the transfer instrument. Requested verification codes can only be used in your test environment.
  'transferInstrumentInfo': new LegalEntityManagementApi.TransferInstrumentInfo() // TransferInstrumentInfo | 
};
apiInstance.patchTransferInstrumentsId(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the transfer instrument. | 
 **xRequestedVerificationCode** | **String**| Use the requested verification code 0_0001 to resolve any suberrors associated with the transfer instrument. Requested verification codes can only be used in your test environment. | [optional] 
 **transferInstrumentInfo** | [**TransferInstrumentInfo**](TransferInstrumentInfo.md)|  | [optional] 

### Return type

[**TransferInstrument**](TransferInstrument.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTransferInstruments

> TransferInstrument postTransferInstruments(opts)

Create a transfer instrument

Creates a transfer instrument.   A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the transfer instrument as required by payment industry regulations. We inform you of the verification results through webhooks or API responses.  When the transfer instrument passes the verification checks, you can start sending funds from the balance platform to the transfer instrument (such as payouts).

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.TransferInstrumentsApi();
let opts = {
  'xRequestedVerificationCode': "17002", // String | Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment.
  'transferInstrumentInfo': new LegalEntityManagementApi.TransferInstrumentInfo() // TransferInstrumentInfo | 
};
apiInstance.postTransferInstruments(opts, (error, data, response) => {
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
 **xRequestedVerificationCode** | **String**| Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment. | [optional] 
 **transferInstrumentInfo** | [**TransferInstrumentInfo**](TransferInstrumentInfo.md)|  | [optional] 

### Return type

[**TransferInstrument**](TransferInstrument.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# AccountAndTransactionApiSpecificationUk.AccountAccessApi

All URIs are relative to *https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountAccessConsentsConsentIdDelete**](AccountAccessApi.md#accountAccessConsentsConsentIdDelete) | **DELETE** /account-access-consents/{consentId} | Delete Account Access Consents
[**accountAccessConsentsConsentIdGet**](AccountAccessApi.md#accountAccessConsentsConsentIdGet) | **GET** /account-access-consents/{consentId} | Get Account Access Consents
[**accountAccessConsentsPost**](AccountAccessApi.md#accountAccessConsentsPost) | **POST** /account-access-consents | Create Account Access Consents



## accountAccessConsentsConsentIdDelete

> accountAccessConsentsConsentIdDelete(consentId, sandboxId, opts)

Delete Account Access Consents

Delete Account Access Consents by Consent ID

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Client-Credentials-Token
let Client-Credentials-Token = defaultClient.authentications['Client-Credentials-Token'];
Client-Credentials-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.AccountAccessApi();
let consentId = "consentId_example"; // String | ConsentId
let sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
let opts = {
  'xFapiAuthDate': "xFapiAuthDate_example", // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
  'xFapiCustomerIpAddress': "xFapiCustomerIpAddress_example", // String | The PSU's IP address if the PSU is currently logged in with the TPP.
  'xFapiInteractionId': "xFapiInteractionId_example", // String | An RFC4122 UID used as a correlation id.
  'xCustomerUserAgent': "xCustomerUserAgent_example" // String | Indicates the user-agent that the PSU is using.
};
apiInstance.accountAccessConsentsConsentIdDelete(consentId, sandboxId, opts, (error, data, response) => {
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
 **consentId** | **String**| ConsentId | 
 **sandboxId** | **String**| The unique id of the sandbox to be used | 
 **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] 
 **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] 

### Return type

null (empty response body)

### Authorization

[Client-Credentials-Token](../README.md#Client-Credentials-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; charset=utf-8


## accountAccessConsentsConsentIdGet

> OBReadConsentResponse1 accountAccessConsentsConsentIdGet(consentId, sandboxId, opts)

Get Account Access Consents

Get Account Access Consents by Consent ID

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Client-Credentials-Token
let Client-Credentials-Token = defaultClient.authentications['Client-Credentials-Token'];
Client-Credentials-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.AccountAccessApi();
let consentId = "consentId_example"; // String | ConsentId
let sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
let opts = {
  'xFapiAuthDate': "xFapiAuthDate_example", // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
  'xFapiCustomerIpAddress': "xFapiCustomerIpAddress_example", // String | The PSU's IP address if the PSU is currently logged in with the TPP.
  'xFapiInteractionId': "xFapiInteractionId_example", // String | An RFC4122 UID used as a correlation id.
  'xCustomerUserAgent': "xCustomerUserAgent_example" // String | Indicates the user-agent that the PSU is using.
};
apiInstance.accountAccessConsentsConsentIdGet(consentId, sandboxId, opts, (error, data, response) => {
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
 **consentId** | **String**| ConsentId | 
 **sandboxId** | **String**| The unique id of the sandbox to be used | 
 **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] 
 **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] 

### Return type

[**OBReadConsentResponse1**](OBReadConsentResponse1.md)

### Authorization

[Client-Credentials-Token](../README.md#Client-Credentials-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; charset=utf-8


## accountAccessConsentsPost

> OBReadConsentResponse1 accountAccessConsentsPost(sandboxId, opts)

Create Account Access Consents

Create Account Access Consents

### Example

```javascript
import AccountAndTransactionApiSpecificationUk from 'account_and_transaction_api_specification_uk';
let defaultClient = AccountAndTransactionApiSpecificationUk.ApiClient.instance;
// Configure OAuth2 access token for authorization: Client-Credentials-Token
let Client-Credentials-Token = defaultClient.authentications['Client-Credentials-Token'];
Client-Credentials-Token.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Client-Id
let Client-Id = defaultClient.authentications['Client-Id'];
Client-Id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Client-Id.apiKeyPrefix = 'Token';

let apiInstance = new AccountAndTransactionApiSpecificationUk.AccountAccessApi();
let sandboxId = "sandboxId_example"; // String | The unique id of the sandbox to be used
let opts = {
  'xFapiAuthDate': "xFapiAuthDate_example", // String | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
  'xFapiCustomerIpAddress': "xFapiCustomerIpAddress_example", // String | The PSU's IP address if the PSU is currently logged in with the TPP.
  'xFapiInteractionId': "xFapiInteractionId_example", // String | An RFC4122 UID used as a correlation id.
  'xCustomerUserAgent': "xCustomerUserAgent_example", // String | Indicates the user-agent that the PSU is using.
  'oBReadConsent1': new AccountAndTransactionApiSpecificationUk.OBReadConsent1() // OBReadConsent1 | Default
};
apiInstance.accountAccessConsentsPost(sandboxId, opts, (error, data, response) => {
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
 **sandboxId** | **String**| The unique id of the sandbox to be used | 
 **xFapiAuthDate** | **String**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **xFapiCustomerIpAddress** | **String**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **xFapiInteractionId** | **String**| An RFC4122 UID used as a correlation id. | [optional] 
 **xCustomerUserAgent** | **String**| Indicates the user-agent that the PSU is using. | [optional] 
 **oBReadConsent1** | [**OBReadConsent1**](OBReadConsent1.md)| Default | [optional] 

### Return type

[**OBReadConsentResponse1**](OBReadConsentResponse1.md)

### Authorization

[Client-Credentials-Token](../README.md#Client-Credentials-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

- **Content-Type**: application/json, application/json; charset=utf-8
- **Accept**: application/json, application/json; charset=utf-8


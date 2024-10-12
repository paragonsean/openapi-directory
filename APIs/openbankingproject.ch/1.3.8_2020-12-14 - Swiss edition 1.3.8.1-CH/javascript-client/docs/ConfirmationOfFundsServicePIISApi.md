# SwissNextGenBankingApiFramework.ConfirmationOfFundsServicePIISApi

All URIs are relative to *https://api.dev.openbankingproject.ch*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkAvailabilityOfFunds**](ConfirmationOfFundsServicePIISApi.md#checkAvailabilityOfFunds) | **POST** /v1/funds-confirmations | Confirmation of funds request



## checkAvailabilityOfFunds

> CheckAvailabilityOfFunds200Response checkAvailabilityOfFunds(xRequestID, confirmationOfFunds, opts)

Confirmation of funds request

Creates a confirmation of funds request at the ASPSP. Checks whether a specific amount is available at point of time of the request on an account linked to a given tuple card issuer(TPP)/card number, or addressed by IBAN and TPP respectively. If the related extended services are used a conditional Consent-ID is contained in the header. This field is contained but commented out in this specification.

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.ConfirmationOfFundsServicePIISApi();
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let confirmationOfFunds = new SwissNextGenBankingApiFramework.ConfirmationOfFunds(); // ConfirmationOfFunds | Request body for a confirmation of funds request. 
let opts = {
  'authorization': "authorization_example", // String | This field  might be used in case where a consent was agreed between ASPSP and PSU through an OAuth2 based protocol, facilitated by the TPP. 
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
};
apiInstance.checkAvailabilityOfFunds(xRequestID, confirmationOfFunds, opts, (error, data, response) => {
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
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **confirmationOfFunds** | [**ConfirmationOfFunds**](ConfirmationOfFunds.md)| Request body for a confirmation of funds request.  | 
 **authorization** | **String**| This field  might be used in case where a consent was agreed between ASPSP and PSU through an OAuth2 based protocol, facilitated by the TPP.  | [optional] 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 

### Return type

[**CheckAvailabilityOfFunds200Response**](CheckAvailabilityOfFunds200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


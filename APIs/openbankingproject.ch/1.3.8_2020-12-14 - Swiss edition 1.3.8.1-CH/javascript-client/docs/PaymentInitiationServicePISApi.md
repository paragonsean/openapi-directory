# SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi

All URIs are relative to *https://api.dev.openbankingproject.ch*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelPayment**](PaymentInitiationServicePISApi.md#cancelPayment) | **DELETE** /v1/{payment-service}/{payment-product}/{paymentId} | Payment cancellation request
[**getPaymentCancellationScaStatus**](PaymentInitiationServicePISApi.md#getPaymentCancellationScaStatus) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations/{authorisationId} | Read the SCA status of the payment cancellation&#39;s authorisation
[**getPaymentInformation**](PaymentInitiationServicePISApi.md#getPaymentInformation) | **GET** /v1/{payment-service}/{payment-product}/{paymentId} | Get payment information
[**getPaymentInitiationAuthorisation**](PaymentInitiationServicePISApi.md#getPaymentInitiationAuthorisation) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Get payment initiation authorisation sub-resources request
[**getPaymentInitiationCancellationAuthorisationInformation**](PaymentInitiationServicePISApi.md#getPaymentInitiationCancellationAuthorisationInformation) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Will deliver an array of resource identifications to all generated cancellation authorisation sub-resources
[**getPaymentInitiationScaStatus**](PaymentInitiationServicePISApi.md#getPaymentInitiationScaStatus) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations/{authorisationId} | Read the SCA status of the payment authorisation
[**getPaymentInitiationStatus**](PaymentInitiationServicePISApi.md#getPaymentInitiationStatus) | **GET** /v1/{payment-service}/{payment-product}/{paymentId}/status | Payment initiation status request
[**initiatePayment**](PaymentInitiationServicePISApi.md#initiatePayment) | **POST** /v1/{payment-service}/{payment-product} | Payment initiation request
[**startPaymentAuthorisation**](PaymentInitiationServicePISApi.md#startPaymentAuthorisation) | **POST** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations | Start the authorisation process for a payment initiation
[**startPaymentInitiationCancellationAuthorisation**](PaymentInitiationServicePISApi.md#startPaymentInitiationCancellationAuthorisation) | **POST** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations | Start the authorisation process for the cancellation of the addressed payment
[**updatePaymentCancellationPsuData**](PaymentInitiationServicePISApi.md#updatePaymentCancellationPsuData) | **PUT** /v1/{payment-service}/{payment-product}/{paymentId}/cancellation-authorisations/{authorisationId} | Update PSU data for payment initiation cancellation
[**updatePaymentPsuData**](PaymentInitiationServicePISApi.md#updatePaymentPsuData) | **PUT** /v1/{payment-service}/{payment-product}/{paymentId}/authorisations/{authorisationId} | Update PSU data for payment initiation



## cancelPayment

> PaymentInitiationCancelResponse202 cancelPayment(paymentService, paymentProduct, paymentId, xRequestID, opts)

Payment cancellation request

This method initiates the cancellation of a payment.  Depending on the payment-service, the payment-product and the ASPSP&#39;s implementation,  this TPP call might be sufficient to cancel a payment.  If an authorisation of the payment cancellation is mandated by the ASPSP,  a corresponding hyperlink will be contained in the response message.  Cancels the addressed payment with resource identification paymentId if applicable to the payment-service, payment-product and received in product related timelines (e.g. before end of business day for scheduled payments of the last business day before the scheduled execution day).   The response to this DELETE command will tell the TPP whether the   * access method was rejected,   * access method was successful, or   * access method is generally applicable, but further authorisation processes are needed. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'tPPRedirectPreferred': true, // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
  'tPPNokRedirectURI': "tPPNokRedirectURI_example", // String | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
  'tPPRedirectURI': "tPPRedirectURI_example", // String | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
  'tPPExplicitAuthorisationPreferred': true, // Boolean | If it equals \"true\", the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \"false\" or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.cancelPayment(paymentService, paymentProduct, paymentId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **tPPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tPPNokRedirectURI** | **String**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tPPRedirectURI** | **String**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tPPExplicitAuthorisationPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**PaymentInitiationCancelResponse202**](PaymentInitiationCancelResponse202.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getPaymentCancellationScaStatus

> ScaStatusResponse getPaymentCancellationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts)

Read the SCA status of the payment cancellation&#39;s authorisation

This method returns the SCA status of a payment initiation&#39;s authorisation sub-resource. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.getPaymentCancellationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **authorisationId** | **String**| Resource identification of the related SCA. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**ScaStatusResponse**](ScaStatusResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getPaymentInformation

> GetPaymentInformation200Response getPaymentInformation(paymentService, paymentProduct, paymentId, xRequestID, opts)

Get payment information

Returns the content of a payment object

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.getPaymentInformation(paymentService, paymentProduct, paymentId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**GetPaymentInformation200Response**](GetPaymentInformation200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, multipart/form-data, application/problem+json


## getPaymentInitiationAuthorisation

> Authorisations getPaymentInitiationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, opts)

Get payment initiation authorisation sub-resources request

Read a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.getPaymentInitiationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**Authorisations**](Authorisations.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getPaymentInitiationCancellationAuthorisationInformation

> Authorisations getPaymentInitiationCancellationAuthorisationInformation(paymentService, paymentProduct, paymentId, xRequestID, opts)

Will deliver an array of resource identifications to all generated cancellation authorisation sub-resources

Retrieve a list of all created cancellation authorisation sub-resources. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.getPaymentInitiationCancellationAuthorisationInformation(paymentService, paymentProduct, paymentId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**Authorisations**](Authorisations.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getPaymentInitiationScaStatus

> ScaStatusResponse getPaymentInitiationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts)

Read the SCA status of the payment authorisation

This method returns the SCA status of a payment initiation&#39;s authorisation sub-resource. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.getPaymentInitiationScaStatus(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **authorisationId** | **String**| Resource identification of the related SCA. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**ScaStatusResponse**](ScaStatusResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getPaymentInitiationStatus

> PaymentInitiationStatusResponse200Json getPaymentInitiationStatus(paymentService, paymentProduct, paymentId, xRequestID, opts)

Payment initiation status request

Check the transaction status of a payment initiation.

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.getPaymentInitiationStatus(paymentService, paymentProduct, paymentId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**PaymentInitiationStatusResponse200Json**](PaymentInitiationStatusResponse200Json.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, application/problem+json


## initiatePayment

> PaymentInitationRequestResponse201 initiatePayment(paymentService, paymentProduct, xRequestID, pSUIPAddress, initiatePaymentRequest, opts)

Payment initiation request

This method is used to initiate a payment at the ASPSP.  ## Variants of payment initiation requests  This method to initiate a payment initiation at the ASPSP can be sent with either a JSON body or an pain.001 body depending on the payment product in the path.  There are the following **payment products**:    - Payment products with payment information in *JSON* format:     - ***domestic-swiss-credit-transfers-isr***     - ***domestic-swiss-credit-transfers***     - ***domestic-swiss-credit-transfers-qr***     - ***domestic-swiss-foreign-credit-transfers***     - ***swiss-sepa-credit-transfers***     - ***swiss-cross-border-credit-transfers***   - Payment products with payment information in *SIX pain.001* XML format:     - ***pain.001-sepa-credit-transfers***     - ***pain.001-cross-border-credit-transfers***     - ***pain.001-swiss-six-credit-transfers***  Furthermore the request body depends on the **payment-service**:   * ***payments***: A single payment initiation request.   * ***bulk-payments***: A collection of several payment initiation requests.        In case of a *pain.001* message there are more than one payments contained in the *pain.001 message.      In case of a *JSON* there are several JSON payment blocks contained in a joining list.   * ***periodic-payments***:     Create a standing order initiation resource for recurrent i.e. periodic payments addressable under {paymentId}      with all data relevant for the corresponding payment product and the execution of the standing order contained in a JSON body.  This is the first step in the API to initiate the related recurring/periodic payment.  ## Single and mulitilevel SCA Processes  The payment initiation requests are independent from the need of one or multilevel  SCA processing, i.e. independent from the number of authorisations needed for the execution of payments.   But the response messages are specific to either one SCA processing or multilevel SCA processing.   For payment initiation with multilevel SCA, this specification requires an explicit start of the authorisation,  i.e. links directly associated with SCA processing like &#39;scaRedirect&#39; or &#39;scaOAuth&#39; cannot be contained in the  response message of a Payment Initation Request for a payment, where multiple authorisations are needed.  Also if any data is needed for the next action, like selecting an SCA method is not supported in the response,  since all starts of the multiple authorisations are fully equal.  In these cases, first an authorisation sub-resource has to be generated following the &#39;startAuthorisation&#39; link. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let pSUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request. 
let initiatePaymentRequest = new SwissNextGenBankingApiFramework.InitiatePaymentRequest(); // InitiatePaymentRequest | JSON request body for a payment inition request message.  There are the following payment-products supported:   * \"domestic-swiss-credit-transfers-isr\"   * \"domestic-swiss-credit-transfers\"   * \"domestic-swiss-credit-transfers-qr\"   * \"domestic-swiss-foreign-credit-transfers\"   * \"swiss-sepa-credit-transfers\" with JSON-Body   * \"swiss-cross-border-credit-transfers\" with JSON-Body   * \"pain.001-sepa-credit-transfers\" with XML pain.001.001.03 body for SCT scheme     Only country specific schemes are currently available   * \"pain.001-cross-border-credit-transfers\" with pain.001 body.     Only country specific schemes are currently available   * \"pain.001-swiss-six-credit-transfers\"  There are the following payment-services supported:   * \"payments\"   * \"periodic-payments\"   * \"bulk-paments\"  All optional, conditional and predefined but not yet used fields are defined. 
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'PSU_ID': "PSU-1234", // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
  'pSUIDType': "pSUIDType_example", // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
  'pSUCorporateID': "pSUCorporateID_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'pSUCorporateIDType': "pSUCorporateIDType_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'consentID': "consentID_example", // String | This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
  'tPPRedirectPreferred': true, // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
  'tPPRedirectURI': "tPPRedirectURI_example", // String | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
  'tPPNokRedirectURI': "tPPNokRedirectURI_example", // String | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
  'tPPExplicitAuthorisationPreferred': true, // Boolean | If it equals \"true\", the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \"false\" or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
  'tPPRejectionNoFundsPreferred': true, // Boolean | If it equals \"true\" then the TPP prefers a rejection of the payment initiation in case the ASPSP is providing an integrated confirmation of funds request an the result of this is that not sufficient funds are available.  If it equals \"false\" then the TPP prefers that the ASPSP is dealing with the payment initiation like in the ASPSPs online channel, potentially waiting for a certain time period for funds to arrive to initiate the payment.  This parameter might be ignored by the ASPSP. 
  'tPPBrandLoggingInformation': "tPPBrandLoggingInformation_example", // String | This header might be used by TPPs to inform the ASPSP about the brand used by the TPP towards the PSU.  This information is meant for logging entries to enhance communication between ASPSP and PSU or ASPSP and TPP.  This header might be ignored by the ASPSP. 
  'tPPNotificationURI': "tPPNotificationURI_example", // String | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
  'tPPNotificationContentPreferred': "tPPNotificationContentPreferred_example", // String | The string has the form  status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558" // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
};
apiInstance.initiatePayment(paymentService, paymentProduct, xRequestID, pSUIPAddress, initiatePaymentRequest, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request.  | 
 **initiatePaymentRequest** | [**InitiatePaymentRequest**](InitiatePaymentRequest.md)| JSON request body for a payment inition request message.  There are the following payment-products supported:   * \&quot;domestic-swiss-credit-transfers-isr\&quot;   * \&quot;domestic-swiss-credit-transfers\&quot;   * \&quot;domestic-swiss-credit-transfers-qr\&quot;   * \&quot;domestic-swiss-foreign-credit-transfers\&quot;   * \&quot;swiss-sepa-credit-transfers\&quot; with JSON-Body   * \&quot;swiss-cross-border-credit-transfers\&quot; with JSON-Body   * \&quot;pain.001-sepa-credit-transfers\&quot; with XML pain.001.001.03 body for SCT scheme     Only country specific schemes are currently available   * \&quot;pain.001-cross-border-credit-transfers\&quot; with pain.001 body.     Only country specific schemes are currently available   * \&quot;pain.001-swiss-six-credit-transfers\&quot;  There are the following payment-services supported:   * \&quot;payments\&quot;   * \&quot;periodic-payments\&quot;   * \&quot;bulk-paments\&quot;  All optional, conditional and predefined but not yet used fields are defined.  | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] 
 **pSUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] 
 **pSUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **consentID** | **String**| This data element may be contained, if the payment initiation transaction is part of a session, i.e. combined AIS/PIS service. This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | [optional] 
 **tPPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tPPRedirectURI** | **String**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tPPNokRedirectURI** | **String**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tPPExplicitAuthorisationPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket.  | [optional] 
 **tPPRejectionNoFundsPreferred** | **Boolean**| If it equals \&quot;true\&quot; then the TPP prefers a rejection of the payment initiation in case the ASPSP is providing an integrated confirmation of funds request an the result of this is that not sufficient funds are available.  If it equals \&quot;false\&quot; then the TPP prefers that the ASPSP is dealing with the payment initiation like in the ASPSPs online channel, potentially waiting for a certain time period for funds to arrive to initiate the payment.  This parameter might be ignored by the ASPSP.  | [optional] 
 **tPPBrandLoggingInformation** | **String**| This header might be used by TPPs to inform the ASPSP about the brand used by the TPP towards the PSU.  This information is meant for logging entries to enhance communication between ASPSP and PSU or ASPSP and TPP.  This header might be ignored by the ASPSP.  | [optional] 
 **tPPNotificationURI** | **String**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply.  | [optional] 
 **tPPNotificationContentPreferred** | **String**| The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 

### Return type

[**PaymentInitationRequestResponse201**](PaymentInitationRequestResponse201.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml, multipart/form-data
- **Accept**: application/json, application/problem+json


## startPaymentAuthorisation

> StartScaprocessResponse startPaymentAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, opts)

Start the authorisation process for a payment initiation

Create an authorisation sub-resource and start the authorisation process. The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the transaction.  The ASPSP might make the usage of this access method unnecessary in case of only one SCA process needed, since the related authorisation resource might be automatically created by the ASPSP after the submission of the payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding Payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;     * &#39;startAuthorisationWithPsuAuthentication&#39;     * &#39;startAuthorisationWithEncryptedPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;   * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding      Payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'PSU_ID': "PSU-1234", // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
  'pSUIDType': "pSUIDType_example", // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
  'pSUCorporateID': "pSUCorporateID_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'pSUCorporateIDType': "pSUCorporateIDType_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'tPPRedirectPreferred': true, // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
  'tPPRedirectURI': "tPPRedirectURI_example", // String | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
  'tPPNokRedirectURI': "tPPNokRedirectURI_example", // String | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
  'tPPNotificationURI': "tPPNotificationURI_example", // String | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
  'tPPNotificationContentPreferred': "tPPNotificationContentPreferred_example", // String | The string has the form  status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558", // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
  'startConsentAuthorisationRequest': new SwissNextGenBankingApiFramework.StartConsentAuthorisationRequest() // StartConsentAuthorisationRequest | 
};
apiInstance.startPaymentAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] 
 **pSUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] 
 **pSUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **tPPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tPPRedirectURI** | **String**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tPPNokRedirectURI** | **String**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tPPNotificationURI** | **String**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply.  | [optional] 
 **tPPNotificationContentPreferred** | **String**| The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 
 **startConsentAuthorisationRequest** | [**StartConsentAuthorisationRequest**](StartConsentAuthorisationRequest.md)|  | [optional] 

### Return type

[**StartScaprocessResponse**](StartScaprocessResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## startPaymentInitiationCancellationAuthorisation

> StartScaprocessResponse startPaymentInitiationCancellationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, opts)

Start the authorisation process for the cancellation of the addressed payment

Creates an authorisation sub-resource and start the authorisation process of the cancellation of the addressed payment. The message might in addition transmit authentication and authorisation related data.  This method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the cancellation-authorisation.  The ASPSP might make the usage of this access method unnecessary in case of only one SCA process needed, since the related authorisation resource might be automatically created by the ASPSP after the submission of the payment data with the first POST payments/{payment-product} call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;     * &#39;startAuthorisationWithPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;    * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with a &#39;startAuthorisation&#39; hyperlink in the preceding      payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'PSU_ID': "PSU-1234", // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
  'pSUIDType': "pSUIDType_example", // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
  'pSUCorporateID': "pSUCorporateID_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'pSUCorporateIDType': "pSUCorporateIDType_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'tPPRedirectPreferred': true, // Boolean | If it equals \"true\", the TPP prefers a redirect over an embedded SCA approach. If it equals \"false\", the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU. 
  'tPPRedirectURI': "tPPRedirectURI_example", // String | URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \"true\". It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification. 
  'tPPNokRedirectURI': "tPPNokRedirectURI_example", // String | If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP. 
  'tPPNotificationURI': "tPPNotificationURI_example", // String | URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply. 
  'tPPNotificationContentPreferred': "tPPNotificationContentPreferred_example", // String | The string has the form  status=X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558", // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
  'startConsentAuthorisationRequest': new SwissNextGenBankingApiFramework.StartConsentAuthorisationRequest() // StartConsentAuthorisationRequest | 
};
apiInstance.startPaymentInitiationCancellationAuthorisation(paymentService, paymentProduct, paymentId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] 
 **pSUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] 
 **pSUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **tPPRedirectPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers a redirect over an embedded SCA approach. If it equals \&quot;false\&quot;, the TPP prefers not to be redirected for SCA. The ASPSP will then choose between the Embedded or the Decoupled SCA approach, depending on the choice of the SCA procedure by the TPP/PSU. If the parameter is not used, the ASPSP will choose the SCA approach to be applied depending on the SCA method chosen by the TPP/PSU.  | [optional] 
 **tPPRedirectURI** | **String**| URI of the TPP, where the transaction flow shall be redirected to after a Redirect.  Mandated for the Redirect SCA Approach, specifically when TPP-Redirect-Preferred equals \&quot;true\&quot;. It is recommended to always use this header field.  **Remark for Future:** This field might be changed to mandatory in the next version of the specification.  | [optional] 
 **tPPNokRedirectURI** | **String**| If this URI is contained, the TPP is asking to redirect the transaction flow to this address instead of the TPP-Redirect-URI in case of a negative result of the redirect SCA method. This might be ignored by the ASPSP.  | [optional] 
 **tPPNotificationURI** | **String**| URI for the Endpoint of the TPP-API to which the status of the payment initiation should be sent. This header field may by ignored by the ASPSP.  For security reasons, it shall be ensured that the TPP-Notification-URI as introduced above is secured by the TPP eIDAS QWAC used for identification of the TPP. The following applies:  URIs which are provided by TPPs in TPP-Notification-URI shall comply with the domain secured by the eIDAS QWAC certificate of the TPP in the field CN or SubjectAltName of the certificate. Please note that in case of example-TPP.com as certificate entry TPP- Notification-URI like www.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications or notifications.example-TPP.com/xs2a-client/v1/ASPSPidentifcation/mytransaction- id/notifications would be compliant.  Wildcard definitions shall be taken into account for compliance checks by the ASPSP.  ASPSPs may respond with ASPSP-Notification-Support set to false, if the provided URIs do not comply.  | [optional] 
 **tPPNotificationContentPreferred** | **String**| The string has the form  status&#x3D;X1, ..., Xn  where Xi is one of the constants SCA, PROCESS, LAST and where constants are not repeated. The usage of the constants supports the of following semantics:    SCA: A notification on every change of the scaStatus attribute for all related authorisation processes is preferred by the TPP.    PROCESS: A notification on all changes of consentStatus or transactionStatus attributes is preferred by the TPP.   LAST: Only a notification on the last consentStatus or transactionStatus as available in the XS2A interface is preferred by the TPP.  This header field may be ignored, if the ASPSP does not support resource notification services for the related TPP.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 
 **startConsentAuthorisationRequest** | [**StartConsentAuthorisationRequest**](StartConsentAuthorisationRequest.md)|  | [optional] 

### Return type

[**StartScaprocessResponse**](StartScaprocessResponse.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## updatePaymentCancellationPsuData

> UpdateConsentsPsuData200Response updatePaymentCancellationPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts)

Update PSU data for payment initiation cancellation

This method updates PSU data on the cancellation authorisation resource if needed.  It may authorise a cancellation of the payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of a cancellation authorisation within the payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific Update PSU data request is only applicable for   * adding the PSU Identification, if not provided yet in the payment initiation request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA approach might depend on the chosen SCA method.  For that reason, the following possible update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'PSU_ID': "PSU-1234", // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
  'pSUIDType': "pSUIDType_example", // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
  'pSUCorporateID': "pSUCorporateID_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'pSUCorporateIDType': "pSUCorporateIDType_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558", // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
  'updateConsentsPsuDataRequest': new SwissNextGenBankingApiFramework.UpdateConsentsPsuDataRequest() // UpdateConsentsPsuDataRequest | 
};
apiInstance.updatePaymentCancellationPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **authorisationId** | **String**| Resource identification of the related SCA. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] 
 **pSUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] 
 **pSUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 
 **updateConsentsPsuDataRequest** | [**UpdateConsentsPsuDataRequest**](UpdateConsentsPsuDataRequest.md)|  | [optional] 

### Return type

[**UpdateConsentsPsuData200Response**](UpdateConsentsPsuData200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## updatePaymentPsuData

> UpdateConsentsPsuData200Response updatePaymentPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts)

Update PSU data for payment initiation

This methods updates PSU data on the authorisation resource if needed. It may authorise a payment within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of payment initiation services needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific update PSU data request is only applicable for   * adding the PSU identification, if not provided yet in the payment initiation request or the account information consent request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU Data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible Update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.PaymentInitiationServicePISApi();
let paymentService = "paymentService_example"; // String | Payment service:  Possible values are: * payments * bulk-payments * periodic-payments 
let paymentProduct = "paymentProduct_example"; // String | The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants. 
let paymentId = "paymentId_example"; // String | Resource identification of the generated payment initiation resource.
let authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'PSU_ID': "PSU-1234", // String | Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP's documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation. 
  'pSUIDType': "pSUIDType_example", // String | Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP's documentation. 
  'pSUCorporateID': "pSUCorporateID_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'pSUCorporateIDType': "pSUCorporateIDType_example", // String | Might be mandated in the ASPSP's documentation. Only used in a corporate context. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. 
  'pSUIPPort': "1234", // String | The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available. 
  'pSUAccept': "pSUAccept_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptCharset': "pSUAcceptCharset_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptEncoding': "pSUAcceptEncoding_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUAcceptLanguage': "pSUAcceptLanguage_example", // String | The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available. 
  'pSUUserAgent': "pSUUserAgent_example", // String | The forwarded Agent header field of the HTTP request between PSU and TPP, if available. 
  'pSUHttpMethod': "pSUHttpMethod_example", // String | HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE 
  'pSUDeviceID': "99435c7e-ad88-49ec-a2ad-99ddcb1f5555", // String | UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device. 
  'pSUGeoLocation': "GEO:52.506931;13.144558", // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
  'updateConsentsPsuDataRequest': new SwissNextGenBankingApiFramework.UpdateConsentsPsuDataRequest() // UpdateConsentsPsuDataRequest | 
};
apiInstance.updatePaymentPsuData(paymentService, paymentProduct, paymentId, authorisationId, xRequestID, opts, (error, data, response) => {
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
 **paymentService** | **String**| Payment service:  Possible values are: * payments * bulk-payments * periodic-payments  | 
 **paymentProduct** | **String**| The addressed payment product endpoint, e.g. for SEPA Credit Transfers (SCT). The ASPSP will publish which of the payment products/endpoints will be supported.  The following payment products are supported:   - domestic-swiss-credit-transfers-isr   - domestic-swiss-credit-transfers   - domestic-swiss-credit-transfers-qr   - domestic-swiss-foreign-credit-transfers   - swiss-sepa-credit-transfers   - swiss-cross-border-credit-transfers   - pain.001-sepa-credit-transfers   - pain.001-cross-border-credit-transfers   - pain.001-swiss-six-credit-transfers  **Remark:** For all SEPA Credit Transfer based endpoints which accept XML encoding, the XML pain.001 schemes provided by EPC are supported by the ASPSP as a minimum for the body content. Further XML schemes might be supported by some communities.  **Remark:** For cross-border and TARGET-2 payments only community wide pain.001 schemes do exist. There are plenty of country specificic scheme variants.  | 
 **paymentId** | **String**| Resource identification of the generated payment initiation resource. | 
 **authorisationId** | **String**| Resource identification of the related SCA. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] 
 **pSUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] 
 **pSUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP.  | [optional] 
 **pSUIPPort** | **String**| The forwarded IP Port header field consists of the corresponding HTTP request IP Port field between PSU and TPP, if available.  | [optional] 
 **pSUAccept** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptCharset** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptEncoding** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUAcceptLanguage** | **String**| The forwarded IP Accept header fields consist of the corresponding HTTP request Accept header fields between PSU and TPP, if available.  | [optional] 
 **pSUUserAgent** | **String**| The forwarded Agent header field of the HTTP request between PSU and TPP, if available.  | [optional] 
 **pSUHttpMethod** | **String**| HTTP method used at the PSU ? TPP interface, if available. Valid values are: * GET * POST * PUT * PATCH * DELETE  | [optional] 
 **pSUDeviceID** | **String**| UUID (Universally Unique Identifier) for a device, which is used by the PSU, if available. UUID identifies either a device or a device dependant application installation. In case of an installation identification this ID needs to be unaltered until removal from device.  | [optional] 
 **pSUGeoLocation** | **String**| The forwarded Geo Location of the corresponding http request between PSU and TPP if available.  | [optional] 
 **updateConsentsPsuDataRequest** | [**UpdateConsentsPsuDataRequest**](UpdateConsentsPsuDataRequest.md)|  | [optional] 

### Return type

[**UpdateConsentsPsuData200Response**](UpdateConsentsPsuData200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


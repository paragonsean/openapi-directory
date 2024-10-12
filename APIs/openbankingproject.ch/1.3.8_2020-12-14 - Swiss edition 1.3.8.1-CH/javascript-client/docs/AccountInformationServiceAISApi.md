# SwissNextGenBankingApiFramework.AccountInformationServiceAISApi

All URIs are relative to *https://api.dev.openbankingproject.ch*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConsent**](AccountInformationServiceAISApi.md#createConsent) | **POST** /v1/consents | Create consent
[**deleteConsent**](AccountInformationServiceAISApi.md#deleteConsent) | **DELETE** /v1/consents/{consentId} | Delete Consent
[**getAccountList**](AccountInformationServiceAISApi.md#getAccountList) | **GET** /v1/accounts | Read account list
[**getBalances**](AccountInformationServiceAISApi.md#getBalances) | **GET** /v1/accounts/{account-id}/balances | Read balance
[**getConsentAuthorisation**](AccountInformationServiceAISApi.md#getConsentAuthorisation) | **GET** /v1/consents/{consentId}/authorisations | Get consent authorisation sub-resources request
[**getConsentInformation**](AccountInformationServiceAISApi.md#getConsentInformation) | **GET** /v1/consents/{consentId} | Get consent request
[**getConsentScaStatus**](AccountInformationServiceAISApi.md#getConsentScaStatus) | **GET** /v1/consents/{consentId}/authorisations/{authorisationId} | Read the SCA status of the consent authorisation
[**getConsentStatus**](AccountInformationServiceAISApi.md#getConsentStatus) | **GET** /v1/consents/{consentId}/status | Consent status request
[**getTransactionDetails**](AccountInformationServiceAISApi.md#getTransactionDetails) | **GET** /v1/accounts/{account-id}/transactions/{transactionId} | Read transaction details
[**getTransactionList**](AccountInformationServiceAISApi.md#getTransactionList) | **GET** /v1/accounts/{account-id}/transactions | Read transaction list of an account
[**readAccountDetails**](AccountInformationServiceAISApi.md#readAccountDetails) | **GET** /v1/accounts/{account-id} | Read account details
[**startConsentAuthorisation**](AccountInformationServiceAISApi.md#startConsentAuthorisation) | **POST** /v1/consents/{consentId}/authorisations | Start the authorisation process for a consent
[**updateConsentsPsuData**](AccountInformationServiceAISApi.md#updateConsentsPsuData) | **PUT** /v1/consents/{consentId}/authorisations/{authorisationId} | Update PSU Data for consents



## createConsent

> ConsentsResponse201 createConsent(xRequestID, pSUIPAddress, opts)

Create consent

This method create a consent resource, defining access rights to dedicated accounts of  a given PSU-ID. These accounts are addressed explicitly in the method as  parameters as a core function.  **Side Effects** When this consent request is a request where the \&quot;recurringIndicator\&quot; equals \&quot;true\&quot;, and if it exists already a former consent for recurring access on account information  for the addressed PSU, then the former consent automatically expires as soon as the new  consent request is authorised by the PSU.  Optional Extension: As an option, an ASPSP might optionally accept a specific access right on the access on all PSD2 related services for all available accounts.  As another option an ASPSP might optionally also accept a command, where only access rights are inserted without mentioning the addressed account.  The relation to accounts is then handled afterwards between PSU and ASPSP.  This option is not supported for the Embedded SCA Approach.  As a last option, an ASPSP might in addition accept a command with access rights   * to see the list of available payment accounts or   * to see the list of available payment accounts with balances. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let pSUIPAddress = "192.168.8.78"; // String | The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request. 
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
  'tPPExplicitAuthorisationPreferred': true, // Boolean | If it equals \"true\", the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \"false\" or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket. 
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
  'pSUGeoLocation': "GEO:52.506931;13.144558", // String | The forwarded Geo Location of the corresponding http request between PSU and TPP if available. 
  'consents': new SwissNextGenBankingApiFramework.Consents() // Consents | Request body for a consents request. 
};
apiInstance.createConsent(xRequestID, pSUIPAddress, opts, (error, data, response) => {
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
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding http request IP Address field between PSU and TPP. If not available, the TPP shall use the IP Address used by the TPP when submitting this request.  | 
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
 **tPPExplicitAuthorisationPreferred** | **Boolean**| If it equals \&quot;true\&quot;, the TPP prefers to start the authorisation process separately, e.g. because of the usage of a signing basket. This preference might be ignored by the ASPSP, if a signing basket is not supported as functionality.  If it equals \&quot;false\&quot; or if the parameter is not used, there is no preference of the TPP. This especially indicates that the TPP assumes a direct authorisation of the transaction in the next step, without using a signing basket.  | [optional] 
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
 **consents** | [**Consents**](Consents.md)| Request body for a consents request.  | [optional] 

### Return type

[**ConsentsResponse201**](ConsentsResponse201.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## deleteConsent

> deleteConsent(consentId, xRequestID, opts)

Delete Consent

The TPP can delete an account information consent object if needed.

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let consentId = "consentId_example"; // String | ID of the corresponding consent object as returned by an account information consent request. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.deleteConsent(consentId, xRequestID, opts, (error, data, response) => {
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
 **consentId** | **String**| ID of the corresponding consent object as returned by an account information consent request.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

null (empty response body)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getAccountList

> AccountList getAccountList(xRequestID, consentID, opts)

Read account list

Read the identifiers of the available payment account together with  booking balance information, depending on the consent granted.  It is assumed that a consent of the PSU to this access is already given and stored on the ASPSP system. The addressed list of accounts depends then on the PSU ID and the stored consent addressed by consentId, respectively the OAuth2 access token.  Returns all identifiers of the accounts, to which an account access has been granted to through the /consents endpoint by the PSU. In addition, relevant information about the accounts and hyperlinks to corresponding account information resources are provided if a related consent has been already granted.  Remark: Note that the /consents endpoint optionally offers to grant an access on all available payment accounts of a PSU. In this case, this endpoint will deliver the information about all available payment accounts of the PSU at this ASPSP. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let consentID = "consentID_example"; // String | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
let opts = {
  'withBalance': true, // Boolean | If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP. 
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getAccountList(xRequestID, consentID, opts, (error, data, response) => {
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
 **consentID** | **String**| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **withBalance** | **Boolean**| If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP.  | [optional] 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

[**AccountList**](AccountList.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getBalances

> ReadAccountBalanceResponse200 getBalances(accountId, xRequestID, consentID, opts)

Read balance

Reads account data from a given account addressed by \&quot;account-id\&quot;.   **Remark:** This account-id can be a tokenised identification due to data protection reason since the path  information might be logged on intermediary servers within the ASPSP sphere.  This account-id then can be retrieved by the \&quot;Get account list\&quot; call.  The account-id is constant at least throughout the lifecycle of a given consent. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let accountId = "accountId_example"; // String | This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \"Read Account List\" or \"Read Card Account list\" call.  The account-id is the \"resourceId\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let consentID = "consentID_example"; // String | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getBalances(accountId, xRequestID, consentID, opts, (error, data, response) => {
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
 **accountId** | **String**| This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consentID** | **String**| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

[**ReadAccountBalanceResponse200**](ReadAccountBalanceResponse200.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getConsentAuthorisation

> Authorisations getConsentAuthorisation(consentId, xRequestID, opts)

Get consent authorisation sub-resources request

Return a list of all authorisation subresources IDs which have been created.  This function returns an array of hyperlinks to all generated authorisation sub-resources. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let consentId = "consentId_example"; // String | ID of the corresponding consent object as returned by an account information consent request. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getConsentAuthorisation(consentId, xRequestID, opts, (error, data, response) => {
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
 **consentId** | **String**| ID of the corresponding consent object as returned by an account information consent request.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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


## getConsentInformation

> ConsentInformationResponse200Json getConsentInformation(consentId, xRequestID, opts)

Get consent request

Returns the content of an account information consent object.  This is returning the data for the TPP especially in cases,  where the consent was directly managed between ASPSP and PSU e.g. in a redirect SCA Approach. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let consentId = "consentId_example"; // String | ID of the corresponding consent object as returned by an account information consent request. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getConsentInformation(consentId, xRequestID, opts, (error, data, response) => {
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
 **consentId** | **String**| ID of the corresponding consent object as returned by an account information consent request.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

[**ConsentInformationResponse200Json**](ConsentInformationResponse200Json.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getConsentScaStatus

> ScaStatusResponse getConsentScaStatus(consentId, authorisationId, xRequestID, opts)

Read the SCA status of the consent authorisation

This method returns the SCA status of a consent initiation&#39;s authorisation sub-resource. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let consentId = "consentId_example"; // String | ID of the corresponding consent object as returned by an account information consent request. 
let authorisationId = "authorisationId_example"; // String | Resource identification of the related SCA.
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getConsentScaStatus(consentId, authorisationId, xRequestID, opts, (error, data, response) => {
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
 **consentId** | **String**| ID of the corresponding consent object as returned by an account information consent request.  | 
 **authorisationId** | **String**| Resource identification of the related SCA. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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


## getConsentStatus

> ConsentStatusResponse200 getConsentStatus(consentId, xRequestID, opts)

Consent status request

Read the status of an account information consent resource.

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let consentId = "consentId_example"; // String | ID of the corresponding consent object as returned by an account information consent request. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getConsentStatus(consentId, xRequestID, opts, (error, data, response) => {
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
 **consentId** | **String**| ID of the corresponding consent object as returned by an account information consent request.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

[**ConsentStatusResponse200**](ConsentStatusResponse200.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getTransactionDetails

> GetTransactionDetails200Response getTransactionDetails(accountId, transactionId, xRequestID, consentID, opts)

Read transaction details

Reads transaction details from a given transaction addressed by \&quot;transactionId\&quot; on a given account addressed by \&quot;account-id\&quot;. This call is only available on transactions as reported in a JSON format.  **Remark:** Please note that the PATH might be already given in detail by the corresponding entry of the response of the \&quot;Read Transaction List\&quot; call within the _links subfield. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let accountId = "accountId_example"; // String | This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \"Read Account List\" or \"Read Card Account list\" call.  The account-id is the \"resourceId\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
let transactionId = "transactionId_example"; // String | This identification is given by the attribute transactionId of the corresponding entry of a transaction list. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let consentID = "consentID_example"; // String | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
let opts = {
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getTransactionDetails(accountId, transactionId, xRequestID, consentID, opts, (error, data, response) => {
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
 **accountId** | **String**| This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **transactionId** | **String**| This identification is given by the attribute transactionId of the corresponding entry of a transaction list.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consentID** | **String**| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

[**GetTransactionDetails200Response**](GetTransactionDetails200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getTransactionList

> TransactionsResponse200Json getTransactionList(accountId, bookingStatus, xRequestID, consentID, opts)

Read transaction list of an account

Read transaction reports or transaction lists of a given account ddressed by \&quot;account-id\&quot;, depending on the steering parameter \&quot;bookingStatus\&quot; together with balances.  For a given account, additional parameters are e.g. the attributes \&quot;dateFrom\&quot; and \&quot;dateTo\&quot;. The ASPSP might add balance information, if transaction lists without balances are not supported. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let accountId = "accountId_example"; // String | This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \"Read Account List\" or \"Read Card Account list\" call.  The account-id is the \"resourceId\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
let bookingStatus = "bookingStatus_example"; // String | Permitted codes are    * \"information\",   * \"booked\",   * \"pending\", and    * \"both\" \"booked\" shall be supported by the ASPSP. To support the \"pending\" and \"both\" feature is optional for the ASPSP, Error code if not supported in the online banking frontend 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let consentID = "consentID_example"; // String | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
let opts = {
  'dateFrom': new Date("2013-10-20"), // Date | Conditional: Starting date (inclusive the date dateFrom) of the transaction list, mandated if no delta access is required and if bookingStatus does not equal \"information\".  For booked transactions, the relevant date is the booking date.   For pending transactions, the relevant date is the entry date, which may not be transparent  neither in this API nor other channels of the ASPSP. 
  'dateTo': new Date("2013-10-20"), // Date | End date (inclusive the data dateTo) of the transaction list, default is \"now\" if not given.  Might be ignored if a delta function is used.  For booked transactions, the relevant date is the booking date.  For pending transactions, the relevant date is the entry date, which may not be transparent neither in this API nor other channels of the ASPSP. 
  'entryReferenceFrom': "entryReferenceFrom_example", // String | This data attribute is indicating that the AISP is in favour to get all transactions after the transaction with identification entryReferenceFrom alternatively to the above defined period. This is a implementation of a delta access. If this data element is contained, the entries \"dateFrom\" and \"dateTo\" might be ignored by the ASPSP if a delta report is supported.  Optional if supported by API provider. 
  'deltaList': true, // Boolean | This data attribute is indicating that the AISP is in favour to get all transactions after the last report access for this PSU on the addressed account. This is another implementation of a delta access-report. This delta indicator might be rejected by the ASPSP if this function is not supported. Optional if supported by API provider
  'withBalance': true, // Boolean | If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP. 
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.getTransactionList(accountId, bookingStatus, xRequestID, consentID, opts, (error, data, response) => {
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
 **accountId** | **String**| This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **bookingStatus** | **String**| Permitted codes are    * \&quot;information\&quot;,   * \&quot;booked\&quot;,   * \&quot;pending\&quot;, and    * \&quot;both\&quot; \&quot;booked\&quot; shall be supported by the ASPSP. To support the \&quot;pending\&quot; and \&quot;both\&quot; feature is optional for the ASPSP, Error code if not supported in the online banking frontend  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consentID** | **String**| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **dateFrom** | **Date**| Conditional: Starting date (inclusive the date dateFrom) of the transaction list, mandated if no delta access is required and if bookingStatus does not equal \&quot;information\&quot;.  For booked transactions, the relevant date is the booking date.   For pending transactions, the relevant date is the entry date, which may not be transparent  neither in this API nor other channels of the ASPSP.  | [optional] 
 **dateTo** | **Date**| End date (inclusive the data dateTo) of the transaction list, default is \&quot;now\&quot; if not given.  Might be ignored if a delta function is used.  For booked transactions, the relevant date is the booking date.  For pending transactions, the relevant date is the entry date, which may not be transparent neither in this API nor other channels of the ASPSP.  | [optional] 
 **entryReferenceFrom** | **String**| This data attribute is indicating that the AISP is in favour to get all transactions after the transaction with identification entryReferenceFrom alternatively to the above defined period. This is a implementation of a delta access. If this data element is contained, the entries \&quot;dateFrom\&quot; and \&quot;dateTo\&quot; might be ignored by the ASPSP if a delta report is supported.  Optional if supported by API provider.  | [optional] 
 **deltaList** | **Boolean**| This data attribute is indicating that the AISP is in favour to get all transactions after the last report access for this PSU on the addressed account. This is another implementation of a delta access-report. This delta indicator might be rejected by the ASPSP if this function is not supported. Optional if supported by API provider | [optional] 
 **withBalance** | **Boolean**| If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP.  | [optional] 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

[**TransactionsResponse200Json**](TransactionsResponse200Json.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain, application/problem+json


## readAccountDetails

> ReadAccountDetails200Response readAccountDetails(accountId, xRequestID, consentID, opts)

Read account details

Reads details about an account, with balances where required.  It is assumed that a consent of the PSU to  this access is already given and stored on the ASPSP system.  The addressed details of this account depends then on the stored consent addressed by consentId,  respectively the OAuth2 access token.  **NOTE:** The account-id can represent a multicurrency account. In this case the currency code is set to \&quot;XXX\&quot;.  Give detailed information about the addressed account.  Give detailed information about the addressed account together with balance information 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let accountId = "accountId_example"; // String | This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \"Read Account List\" or \"Read Card Account list\" call.  The account-id is the \"resourceId\" attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent. 
let xRequestID = "99391c7e-ad88-49ec-a2ad-99ddcb1f7721"; // String | ID of the request, unique to the call, as determined by the initiating party.
let consentID = "consentID_example"; // String | This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation. 
let opts = {
  'withBalance': true, // Boolean | If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP. 
  'digest': "SHA-256=hl1/Eps8BEQW58FJhDApwJXjGY4nr1ArGDHIT25vq6A=", // String | Is contained if and only if the \"Signature\" element is contained in the header of the request.
  'signature': "keyId=\"SN=9FA1,CA=CN=D-TRUST%20CA%202-1%202015,O=D-Trust%20GmbH,C=DE\",algorithm=\"rsa-sha256\", headers=\"Digest X-Request-ID PSU-ID TPP-Redirect-URI Date\", signature=\"Base64(RSA-SHA256(signing string))\" ", // String | A signature of the request by the TPP on application level. This might be mandated by ASPSP. 
  'tPPSignatureCertificate': null, // Blob | The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained. 
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.readAccountDetails(accountId, xRequestID, consentID, opts, (error, data, response) => {
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
 **accountId** | **String**| This identification is denoting the addressed (card) account.  The account-id is retrieved by using a \&quot;Read Account List\&quot; or \&quot;Read Card Account list\&quot; call.  The account-id is the \&quot;resourceId\&quot; attribute of the account structure.  Its value is constant at least throughout the lifecycle of a given consent.  | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **consentID** | **String**| This then contains the consentId of the related AIS consent, which was performed prior to this payment initiation.  | 
 **withBalance** | **Boolean**| If contained, this function reads the list of accessible payment accounts including the booking balance, if granted by the PSU in the related consent and available by the ASPSP. This parameter might be ignored by the ASPSP.  | [optional] 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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

[**ReadAccountDetails200Response**](ReadAccountDetails200Response.md)

### Authorization

[BearerAuthOAuth](../README.md#BearerAuthOAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## startConsentAuthorisation

> StartScaprocessResponse startConsentAuthorisation(consentId, xRequestID, opts)

Start the authorisation process for a consent

Create an authorisation sub-resource and start the authorisation process of a consent. The message might in addition transmit authentication and authorisation related data.  his method is iterated n times for a n times SCA authorisation in a corporate context, each creating an own authorisation sub-endpoint for the corresponding PSU authorising the consent.  The ASPSP might make the usage of this access method unnecessary, since the related authorisation resource will be automatically created by the ASPSP after the submission of the consent data with the first POST consents call.  The start authorisation process is a process which is needed for creating a new authorisation or cancellation sub-resource.  This applies in the following scenarios:    * The ASPSP has indicated with an &#39;startAuthorisation&#39; hyperlink in the preceding Payment      initiation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be      uploaded by using the extended forms:     * &#39;startAuthorisationWithPsuIdentfication&#39;,      * &#39;startAuthorisationWithPsuAuthentication&#39;      * &#39;startAuthorisationWithEncryptedPsuAuthentication&#39;     * &#39;startAuthorisationWithAuthentciationMethodSelection&#39;   * The related payment initiation cannot yet be executed since a multilevel SCA is mandated.   * The ASPSP has indicated with an &#39;startAuthorisation&#39; hyperlink in the preceding      payment cancellation response that an explicit start of the authorisation process is needed by the TPP.      The &#39;startAuthorisation&#39; hyperlink can transport more information about data which needs to be uploaded      by using the extended forms as indicated above.   * The related payment cancellation request cannot be applied yet since a multilevel SCA is mandate for     executing the cancellation.   * The signing basket needs to be authorised yet. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let consentId = "consentId_example"; // String | ID of the corresponding consent object as returned by an account information consent request. 
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
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.startConsentAuthorisation(consentId, xRequestID, opts, (error, data, response) => {
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
 **consentId** | **String**| ID of the corresponding consent object as returned by an account information consent request.  | 
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
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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


## updateConsentsPsuData

> UpdateConsentsPsuData200Response updateConsentsPsuData(consentId, authorisationId, xRequestID, opts)

Update PSU Data for consents

This method update PSU data on the consents  resource if needed. It may authorise a consent within the Embedded SCA Approach where needed.  Independently from the SCA Approach it supports e.g. the selection of the authentication method and a non-SCA PSU authentication.  There are several possible update PSU data requests in the context of a consent request if needed,  which depends on the SCA approach:  * Redirect SCA Approach:   A specific Update PSU data request is applicable for      * the selection of authentication methods, before choosing the actual SCA approach. * Decoupled SCA Approach:   A specific update PSU data request is only applicable for   * adding the PSU Identification, if not provided yet in the payment initiation request or the Account Information Consent Request, or if no OAuth2 access token is used, or   * the selection of authentication methods. * Embedded SCA Approach:    The Update PSU data request might be used    * to add credentials as a first factor authentication data of the PSU and   * to select the authentication method and   * transaction authorisation.  The SCA Approach might depend on the chosen SCA method.  For that reason, the following possible update PSU data request can apply to all SCA approaches:  * Select an SCA method in case of several SCA methods are available for the customer.  There are the following request types on this access path:   * Update PSU identification   * Update PSU authentication   * Select PSU autorization method      WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change.   * Transaction Authorisation     WARNING: This method needs a reduced header,      therefore many optional elements are not present.      Maybe in a later version the access path will change. 

### Example

```javascript
import SwissNextGenBankingApiFramework from 'swiss_next_gen_banking_api_framework';
let defaultClient = SwissNextGenBankingApiFramework.ApiClient.instance;
// Configure Bearer access token for authorization: BearerAuthOAuth
let BearerAuthOAuth = defaultClient.authentications['BearerAuthOAuth'];
BearerAuthOAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SwissNextGenBankingApiFramework.AccountInformationServiceAISApi();
let consentId = "consentId_example"; // String | ID of the corresponding consent object as returned by an account information consent request. 
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
  'pSUIPAddress': "192.168.8.78", // String | The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU. 
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
apiInstance.updateConsentsPsuData(consentId, authorisationId, xRequestID, opts, (error, data, response) => {
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
 **consentId** | **String**| ID of the corresponding consent object as returned by an account information consent request.  | 
 **authorisationId** | **String**| Resource identification of the related SCA. | 
 **xRequestID** | **String**| ID of the request, unique to the call, as determined by the initiating party. | 
 **digest** | **String**| Is contained if and only if the \&quot;Signature\&quot; element is contained in the header of the request. | [optional] 
 **signature** | **String**| A signature of the request by the TPP on application level. This might be mandated by ASPSP.  | [optional] 
 **tPPSignatureCertificate** | **Blob**| The certificate used for signing the request, in base64 encoding. Must be contained if a signature is contained.  | [optional] 
 **PSU_ID** | **String**| Client ID of the PSU in the ASPSP client interface.  Might be mandated in the ASPSP&#39;s documentation.  It might be contained even if an OAuth2 based authentication was performed in a pre-step or an OAuth2 based SCA was performed in an preceding AIS service in the same session. In this case the ASPSP might check whether PSU-ID and token match, according to ASPSP documentation.  | [optional] 
 **pSUIDType** | **String**| Type of the PSU-ID, needed in scenarios where PSUs have several PSU-IDs as access possibility.  In this case, the mean and use are then defined in the ASPSP&#39;s documentation.  | [optional] 
 **pSUCorporateID** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUCorporateIDType** | **String**| Might be mandated in the ASPSP&#39;s documentation. Only used in a corporate context.  | [optional] 
 **pSUIPAddress** | **String**| The forwarded IP Address header field consists of the corresponding HTTP request IP Address field between PSU and TPP. It shall be contained if and only if this request was actively initiated by the PSU.  | [optional] 
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


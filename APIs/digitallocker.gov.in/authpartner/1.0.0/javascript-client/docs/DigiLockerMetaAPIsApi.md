# AuthorizedPartnerApiSpecification.DigiLockerMetaAPIsApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getListOfDocumentsProvidedByAnIssuerId**](DigiLockerMetaAPIsApi.md#getListOfDocumentsProvidedByAnIssuerId) | **POST** /oauth2/1/pull/doctype | Get List of Documents Provided by an Issuer
[**getListOfIssuersId**](DigiLockerMetaAPIsApi.md#getListOfIssuersId) | **POST** /oauth2/1/pull/issuers | Get List of Issuers
[**getSearchParametersForADocumentId**](DigiLockerMetaAPIsApi.md#getSearchParametersForADocumentId) | **POST** /oauth2/1/pull/parameters | Get Search Parameters for a Document
[**getStatisticsId**](DigiLockerMetaAPIsApi.md#getStatisticsId) | **POST** /statistics/1/counts | Get Statistics
[**pushURIToAccountId**](DigiLockerMetaAPIsApi.md#pushURIToAccountId) | **POST** /account/1/pushuri | Push URI to Account
[**verifyAccountId**](DigiLockerMetaAPIsApi.md#verifyAccountId) | **POST** /account/2/verify | Verify Account



## getListOfDocumentsProvidedByAnIssuerId

> DocTypeResponse getListOfDocumentsProvidedByAnIssuerId(opts)

Get List of Documents Provided by an Issuer

Returns a list of documents/certificates issued by an issuer organization registered with DigiLocker.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerMetaAPIsApi();
let opts = {
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'orgid': "orgid_example", // String | The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier.
  'ts': "ts_example" // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
};
apiInstance.getListOfDocumentsProvidedByAnIssuerId(opts, (error, data, response) => {
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
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **orgid** | **String**| The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 

### Return type

[**DocTypeResponse**](DocTypeResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getListOfIssuersId

> IssuerResponse getListOfIssuersId(opts)

Get List of Issuers

Returns the list of issuers registered with DigiLocker.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerMetaAPIsApi();
let opts = {
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'ts': "ts_example" // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
};
apiInstance.getListOfIssuersId(opts, (error, data, response) => {
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
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 

### Return type

[**IssuerResponse**](IssuerResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getSearchParametersForADocumentId

> [SearchParametersResponseInner] getSearchParametersForADocumentId(opts)

Get Search Parameters for a Document

Returns a list of parameters required to search a document/certificate of an issuer organization registered with DigiLocker. These parameters are used to pull a document from issuer’s repository using Pull Document API mentioned in subsequent section.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerMetaAPIsApi();
let opts = {
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'doctype': "doctype_example", // String | A 5 character unique document type provided by DigiLocker.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'orgid': "orgid_example", // String | The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier.
  'ts': "ts_example" // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
};
apiInstance.getSearchParametersForADocumentId(opts, (error, data, response) => {
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
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **doctype** | **String**| A 5 character unique document type provided by DigiLocker. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **orgid** | **String**| The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned earlier. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 

### Return type

[**[SearchParametersResponseInner]**](SearchParametersResponseInner.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getStatisticsId

> GetStatisticsResponse getStatisticsId(opts)

Get Statistics

Returns DigiLocker statistics such as the count of users, authentic documents, issuers and requesters as on a specific date.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerMetaAPIsApi();
let opts = {
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'ts': "ts_example" // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
};
apiInstance.getStatisticsId(opts, (error, data, response) => {
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
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 

### Return type

[**GetStatisticsResponse**](GetStatisticsResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## pushURIToAccountId

> Object pushURIToAccountId(opts)

Push URI to Account

The API can use to push or delete a single URI into Digital Locker using DigiLocker Id acquired using Get User Details API. This API can be used to push the certificate details to Digital Locker as and when a certificate is generated in the issuer system. The issuing departments must register on DigiLocker as a registered Issuer and implement the requisite Issuer APIs as mentioned in Digital Locker Issuer API Specification document prior to pushing certificates using this API.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerMetaAPIsApi();
let opts = {
  'action': "action_example", // String | Action that needs to be taken for the Aadhaar number and URI combination. Possible values are A for adding a new URI, U for updating an already added URI details or D for deleting the URI.
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'digilockerid': 56, // Number | This is the DigiLocker Id of the user that was acquired using Get User Details API.
  'docid': "docid_example", // String | A unique number of the document. This id will be unique within the document type issued by the issuer.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'issuedate': "issuedate_example", // String | The issue date of the document in DDMMYYYY format.
  'ts': "ts_example", // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
  'uri': "uri_example", // String | This is the unique identifier of the document.
  'validfrom': 56, // Number | The date from which the document is valid in DDMMYYYY format. This may be same as the issue date.
  'validto': "validto_example" // String | The expiry date of the document in DDMMYYYY format.
};
apiInstance.pushURIToAccountId(opts, (error, data, response) => {
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
 **action** | **String**| Action that needs to be taken for the Aadhaar number and URI combination. Possible values are A for adding a new URI, U for updating an already added URI details or D for deleting the URI. | [optional] 
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **digilockerid** | **Number**| This is the DigiLocker Id of the user that was acquired using Get User Details API. | [optional] 
 **docid** | **String**| A unique number of the document. This id will be unique within the document type issued by the issuer. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **issuedate** | **String**| The issue date of the document in DDMMYYYY format. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 
 **uri** | **String**| This is the unique identifier of the document. | [optional] 
 **validfrom** | **Number**| The date from which the document is valid in DDMMYYYY format. This may be same as the issue date. | [optional] 
 **validto** | **String**| The expiry date of the document in DDMMYYYY format. | [optional] 

### Return type

**Object**

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## verifyAccountId

> VerifyAccountResponse verifyAccountId(opts)

Verify Account

This API can be used to verify whether a mobile number or Aadhaar number is already registered with DigiLocker.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauthsecurity
let oauthsecurity = defaultClient.authentications['oauthsecurity'];
oauthsecurity.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizedPartnerApiSpecification.DigiLockerMetaAPIsApi();
let opts = {
  'clientid': "clientid_example", // String | Provide the client id that was created during the application registration process on Partners Portal.
  'hmac': "/path/to/file", // File | Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret.
  'mobile': 56, // Number | This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists.
  'ts': "ts_example", // String | Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes.
  'uid': 56 // Number | This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists.
};
apiInstance.verifyAccountId(opts, (error, data, response) => {
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
 **clientid** | **String**| Provide the client id that was created during the application registration process on Partners Portal. | [optional] 
 **hmac** | **File**| Provide SHA-256 encrypted value of the client secret, clientid and ts parameters above concatenated in this sequence (client secret, clientid, ts). The hmac parameter is used by DigiLocker to ensure the data integrity and authentication of the request. Use the Client Secret Key generated during the application registration process on Partners Portal as the client secret. | [optional] 
 **mobile** | **Number**| This is the mobile number of the user. DigiLocker will check whether an account exists for this mobile number. Either uid or mobile is required to verify whether an account exists. | [optional] 
 **ts** | **String**| Provide a timestamp value in UNIX (or POSIX) format in IST time zone in seconds. This timestamp value must not be older than 30 minutes. | [optional] 
 **uid** | **Number**| This is the Aadhaar number of the user. DigiLocker will check whether an account exists for this Aadhaar number. Either uid or mobile is required to verify whether an account exists. | [optional] 

### Return type

[**VerifyAccountResponse**](VerifyAccountResponse.md)

### Authorization

[oauthsecurity](../README.md#oauthsecurity)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


# PostmarkAccountLevelApi.DomainsAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDomain**](DomainsAPIApi.md#createDomain) | **POST** /domains | Create a Domain
[**deleteDomain**](DomainsAPIApi.md#deleteDomain) | **DELETE** /domains/{domainid} | Delete a Domain
[**editDomain**](DomainsAPIApi.md#editDomain) | **PUT** /domains/{domainid} | Update a Domain
[**getDomain**](DomainsAPIApi.md#getDomain) | **GET** /domains/{domainid} | Get a Domain
[**listDomains**](DomainsAPIApi.md#listDomains) | **GET** /domains | List Domains
[**requestDkimVerificationForDomain**](DomainsAPIApi.md#requestDkimVerificationForDomain) | **PUT** /domains/{domainid}/verifydkim | Request DNS Verification for DKIM
[**requestReturnPathVerificationForDomain**](DomainsAPIApi.md#requestReturnPathVerificationForDomain) | **PUT** /domains/{domainid}/verifyreturnpath | Request DNS Verification for Return-Path
[**requestSPFVerificationForDomain**](DomainsAPIApi.md#requestSPFVerificationForDomain) | **POST** /domains/{domainid}/verifyspf | Request DNS Verification for SPF
[**rotateDKIMKeyForDomain**](DomainsAPIApi.md#rotateDKIMKeyForDomain) | **POST** /domains/{domainid}/rotatedkim | Rotate DKIM Key



## createDomain

> DomainExtendedInformation createDomain(xPostmarkAccountToken, opts)

Create a Domain

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let opts = {
  'body': new PostmarkAccountLevelApi.DomainCreationModel() // DomainCreationModel | 
};
apiInstance.createDomain(xPostmarkAccountToken, opts, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **body** | [**DomainCreationModel**](DomainCreationModel.md)|  | [optional] 

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDomain

> StandardPostmarkResponse deleteDomain(xPostmarkAccountToken, domainid)

Delete a Domain

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let domainid = 56; // Number | The ID for the Domain that should be deleted by the request.
apiInstance.deleteDomain(xPostmarkAccountToken, domainid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **domainid** | **Number**| The ID for the Domain that should be deleted by the request. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editDomain

> DomainExtendedInformation editDomain(xPostmarkAccountToken, domainid, opts)

Update a Domain

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let domainid = 56; // Number | The ID for the Domain that should be modified by the request.
let opts = {
  'body': new PostmarkAccountLevelApi.DomainEditingModel() // DomainEditingModel | 
};
apiInstance.editDomain(xPostmarkAccountToken, domainid, opts, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **domainid** | **Number**| The ID for the Domain that should be modified by the request. | 
 **body** | [**DomainEditingModel**](DomainEditingModel.md)|  | [optional] 

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDomain

> DomainExtendedInformation getDomain(xPostmarkAccountToken, domainid)

Get a Domain

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let domainid = 56; // Number | The ID for the Domain that should be retrieved.
apiInstance.getDomain(xPostmarkAccountToken, domainid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **domainid** | **Number**| The ID for the Domain that should be retrieved. | 

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDomains

> DomainListingResults listDomains(xPostmarkAccountToken, count, offset)

List Domains

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let count = 56; // Number | Number of records to return per request. Max 500.
let offset = 56; // Number | Number of records to skip
apiInstance.listDomains(xPostmarkAccountToken, count, offset, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **count** | **Number**| Number of records to return per request. Max 500. | 
 **offset** | **Number**| Number of records to skip | 

### Return type

[**DomainListingResults**](DomainListingResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestDkimVerificationForDomain

> DomainExtendedInformation requestDkimVerificationForDomain(xPostmarkAccountToken, domainid)

Request DNS Verification for DKIM

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let domainid = 56; // Number | The ID for the Domain for which DKIM DNS records should be verified.
apiInstance.requestDkimVerificationForDomain(xPostmarkAccountToken, domainid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **domainid** | **Number**| The ID for the Domain for which DKIM DNS records should be verified. | 

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestReturnPathVerificationForDomain

> DomainExtendedInformation requestReturnPathVerificationForDomain(xPostmarkAccountToken, domainid)

Request DNS Verification for Return-Path

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let domainid = 56; // Number | The ID for the Domain for which Return-Path DNS records should be verified.
apiInstance.requestReturnPathVerificationForDomain(xPostmarkAccountToken, domainid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **domainid** | **Number**| The ID for the Domain for which Return-Path DNS records should be verified. | 

### Return type

[**DomainExtendedInformation**](DomainExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSPFVerificationForDomain

> DomainSPFResult requestSPFVerificationForDomain(xPostmarkAccountToken, domainid)

Request DNS Verification for SPF

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let domainid = 56; // Number | The ID for the Domain for which SPF DNS records should be verified.
apiInstance.requestSPFVerificationForDomain(xPostmarkAccountToken, domainid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **domainid** | **Number**| The ID for the Domain for which SPF DNS records should be verified. | 

### Return type

[**DomainSPFResult**](DomainSPFResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rotateDKIMKeyForDomain

> DKIMRotationResponse rotateDKIMKeyForDomain(xPostmarkAccountToken, domainid)

Rotate DKIM Key

Creates a new DKIM key to replace your current key. Until the DNS entries are confirmed, the new values will be in the &#x60;DKIMPendingHost&#x60; and &#x60;DKIMPendingTextValue&#x60; fields. After the new DKIM value is verified in DNS, the pending values will migrate to &#x60;DKIMTextValue&#x60; and &#x60;DKIMPendingTextValue&#x60; and Postmark will begin to sign emails with the new DKIM key. 

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.DomainsAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let domainid = 56; // Number | The ID for the Sender Signature for which a new DKIM Key should be generated.
apiInstance.rotateDKIMKeyForDomain(xPostmarkAccountToken, domainid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **domainid** | **Number**| The ID for the Sender Signature for which a new DKIM Key should be generated. | 

### Return type

[**DKIMRotationResponse**](DKIMRotationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


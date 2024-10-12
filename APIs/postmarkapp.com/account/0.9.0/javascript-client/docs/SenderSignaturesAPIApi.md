# PostmarkAccountLevelApi.SenderSignaturesAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSenderSignature**](SenderSignaturesAPIApi.md#createSenderSignature) | **POST** /senders | Create a Sender Signature
[**deleteSenderSignature**](SenderSignaturesAPIApi.md#deleteSenderSignature) | **DELETE** /senders/{signatureid} | Delete a Sender Signature
[**editSenderSignature**](SenderSignaturesAPIApi.md#editSenderSignature) | **PUT** /senders/{signatureid} | Update a Sender Signature
[**getSenderSignature**](SenderSignaturesAPIApi.md#getSenderSignature) | **GET** /senders/{signatureid} | Get a Sender Signature
[**listSenderSignatures**](SenderSignaturesAPIApi.md#listSenderSignatures) | **GET** /senders | List Sender Signatures
[**requestNewDKIMKeyForSenderSignature**](SenderSignaturesAPIApi.md#requestNewDKIMKeyForSenderSignature) | **POST** /senders/{signatureid}/requestnewdkim | Request a new DKIM Key
[**requestSPFVerificationForSenderSignature**](SenderSignaturesAPIApi.md#requestSPFVerificationForSenderSignature) | **POST** /senders/{signatureid}/verifyspf | Request DNS Verification for SPF
[**resendSenderSignatureConfirmationEmail**](SenderSignaturesAPIApi.md#resendSenderSignatureConfirmationEmail) | **POST** /senders/{signatureid}/resend | Resend Signature Confirmation Email



## createSenderSignature

> SenderSignatureExtendedInformation createSenderSignature(xPostmarkAccountToken, opts)

Create a Sender Signature

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let opts = {
  'body': new PostmarkAccountLevelApi.SenderSignatureCreationModel() // SenderSignatureCreationModel | 
};
apiInstance.createSenderSignature(xPostmarkAccountToken, opts, (error, data, response) => {
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
 **body** | [**SenderSignatureCreationModel**](SenderSignatureCreationModel.md)|  | [optional] 

### Return type

[**SenderSignatureExtendedInformation**](SenderSignatureExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSenderSignature

> StandardPostmarkResponse deleteSenderSignature(xPostmarkAccountToken, signatureid)

Delete a Sender Signature

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let signatureid = 56; // Number | The ID for the Sender Signature that should be deleted by the request.
apiInstance.deleteSenderSignature(xPostmarkAccountToken, signatureid, (error, data, response) => {
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
 **signatureid** | **Number**| The ID for the Sender Signature that should be deleted by the request. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editSenderSignature

> SenderSignatureExtendedInformation editSenderSignature(xPostmarkAccountToken, signatureid, opts)

Update a Sender Signature

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let signatureid = 56; // Number | The ID for the Sender Signature that should be modified by the request.
let opts = {
  'body': new PostmarkAccountLevelApi.SenderSignatureEditingModel() // SenderSignatureEditingModel | 
};
apiInstance.editSenderSignature(xPostmarkAccountToken, signatureid, opts, (error, data, response) => {
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
 **signatureid** | **Number**| The ID for the Sender Signature that should be modified by the request. | 
 **body** | [**SenderSignatureEditingModel**](SenderSignatureEditingModel.md)|  | [optional] 

### Return type

[**SenderSignatureExtendedInformation**](SenderSignatureExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSenderSignature

> SenderSignatureExtendedInformation getSenderSignature(xPostmarkAccountToken, signatureid)

Get a Sender Signature

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let signatureid = 56; // Number | The ID for the Sender Signature that should be retrieved.
apiInstance.getSenderSignature(xPostmarkAccountToken, signatureid, (error, data, response) => {
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
 **signatureid** | **Number**| The ID for the Sender Signature that should be retrieved. | 

### Return type

[**SenderSignatureExtendedInformation**](SenderSignatureExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSenderSignatures

> SenderListingResults listSenderSignatures(xPostmarkAccountToken, count, offset)

List Sender Signatures

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let count = 56; // Number | Number of records to return per request. Max 500.
let offset = 56; // Number | Number of records to skip
apiInstance.listSenderSignatures(xPostmarkAccountToken, count, offset, (error, data, response) => {
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

[**SenderListingResults**](SenderListingResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestNewDKIMKeyForSenderSignature

> StandardPostmarkResponse requestNewDKIMKeyForSenderSignature(xPostmarkAccountToken, signatureid)

Request a new DKIM Key

Requests a new DKIM key to be created. Until the DNS entries are confirmed, the new values will be in the &#x60;DKIMPendingHost&#x60; and &#x60;DKIMPendingTextValue&#x60; fields. After the new DKIM value is verified in DNS, the pending values will migrate to &#x60;DKIMTextValue&#x60; and &#x60;DKIMPendingTextValue&#x60; and Postmark will begin to sign emails with the new DKIM key. 

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let signatureid = 56; // Number | The ID for the Sender Signature for which a new DKIM Key should be generated.
apiInstance.requestNewDKIMKeyForSenderSignature(xPostmarkAccountToken, signatureid, (error, data, response) => {
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
 **signatureid** | **Number**| The ID for the Sender Signature for which a new DKIM Key should be generated. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestSPFVerificationForSenderSignature

> SenderSignatureExtendedInformation requestSPFVerificationForSenderSignature(xPostmarkAccountToken, signatureid)

Request DNS Verification for SPF

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let signatureid = 56; // Number | The ID for the Sender Signature for which SPF DNS records should be verified.
apiInstance.requestSPFVerificationForSenderSignature(xPostmarkAccountToken, signatureid, (error, data, response) => {
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
 **signatureid** | **Number**| The ID for the Sender Signature for which SPF DNS records should be verified. | 

### Return type

[**SenderSignatureExtendedInformation**](SenderSignatureExtendedInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resendSenderSignatureConfirmationEmail

> StandardPostmarkResponse resendSenderSignatureConfirmationEmail(xPostmarkAccountToken, signatureid)

Resend Signature Confirmation Email

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.SenderSignaturesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let signatureid = 56; // Number | The ID for the Sender Signature that should have its confirmation email resent.
apiInstance.resendSenderSignatureConfirmationEmail(xPostmarkAccountToken, signatureid, (error, data, response) => {
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
 **signatureid** | **Number**| The ID for the Sender Signature that should have its confirmation email resent. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


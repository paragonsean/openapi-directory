# TwilioPreview.PreviewHostedNumbersAuthorizationDocumentApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#createHostedNumbersAuthorizationDocument) | **POST** /HostedNumbers/AuthorizationDocuments | 
[**fetchHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#fetchHostedNumbersAuthorizationDocument) | **GET** /HostedNumbers/AuthorizationDocuments/{Sid} | 
[**listHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#listHostedNumbersAuthorizationDocument) | **GET** /HostedNumbers/AuthorizationDocuments | 
[**updateHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocumentApi.md#updateHostedNumbersAuthorizationDocument) | **POST** /HostedNumbers/AuthorizationDocuments/{Sid} | 



## createHostedNumbersAuthorizationDocument

> PreviewHostedNumbersAuthorizationDocument createHostedNumbersAuthorizationDocument(addressSid, contactPhoneNumber, contactTitle, email, hostedNumberOrderSids, opts)



Create an AuthorizationDocument for authorizing the hosting of phone number capabilities on Twilio&#39;s platform.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersAuthorizationDocumentApi();
let addressSid = "addressSid_example"; // String | A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
let contactPhoneNumber = "contactPhoneNumber_example"; // String | The contact phone number of the person authorized to sign the Authorization Document.
let contactTitle = "contactTitle_example"; // String | The title of the person authorized to sign the Authorization Document for this phone number.
let email = "email_example"; // String | Email that this AuthorizationDocument will be sent to for signing.
let hostedNumberOrderSids = ["null"]; // [String] | A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
let opts = {
  'ccEmails': ["null"] // [String] | Email recipients who will be informed when an Authorization Document has been sent and signed.
};
apiInstance.createHostedNumbersAuthorizationDocument(addressSid, contactPhoneNumber, contactTitle, email, hostedNumberOrderSids, opts, (error, data, response) => {
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
 **addressSid** | **String**| A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument. | 
 **contactPhoneNumber** | **String**| The contact phone number of the person authorized to sign the Authorization Document. | 
 **contactTitle** | **String**| The title of the person authorized to sign the Authorization Document for this phone number. | 
 **email** | **String**| Email that this AuthorizationDocument will be sent to for signing. | 
 **hostedNumberOrderSids** | [**[String]**](String.md)| A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio&#39;s platform. | 
 **ccEmails** | [**[String]**](String.md)| Email recipients who will be informed when an Authorization Document has been sent and signed. | [optional] 

### Return type

[**PreviewHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchHostedNumbersAuthorizationDocument

> PreviewHostedNumbersAuthorizationDocument fetchHostedNumbersAuthorizationDocument(sid)



Fetch a specific AuthorizationDocument.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersAuthorizationDocumentApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this AuthorizationDocument.
apiInstance.fetchHostedNumbersAuthorizationDocument(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this AuthorizationDocument. | 

### Return type

[**PreviewHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHostedNumbersAuthorizationDocument

> ListHostedNumbersAuthorizationDocumentResponse listHostedNumbersAuthorizationDocument(opts)



Retrieve a list of AuthorizationDocuments belonging to the account initiating the request.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersAuthorizationDocumentApi();
let opts = {
  'email': "email_example", // String | Email that this AuthorizationDocument will be sent to for signing.
  'status': "status_example", // AuthorizationDocumentEnumStatus | Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listHostedNumbersAuthorizationDocument(opts, (error, data, response) => {
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
 **email** | **String**| Email that this AuthorizationDocument will be sent to for signing. | [optional] 
 **status** | **AuthorizationDocumentEnumStatus**| Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListHostedNumbersAuthorizationDocumentResponse**](ListHostedNumbersAuthorizationDocumentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateHostedNumbersAuthorizationDocument

> PreviewHostedNumbersAuthorizationDocument updateHostedNumbersAuthorizationDocument(sid, opts)



Updates a specific AuthorizationDocument.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersAuthorizationDocumentApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this AuthorizationDocument.
let opts = {
  'addressSid': "addressSid_example", // String | A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
  'ccEmails': ["null"], // [String] | Email recipients who will be informed when an Authorization Document has been sent and signed
  'contactPhoneNumber': "contactPhoneNumber_example", // String | The contact phone number of the person authorized to sign the Authorization Document.
  'contactTitle': "contactTitle_example", // String | The title of the person authorized to sign the Authorization Document for this phone number.
  'email': "email_example", // String | Email that this AuthorizationDocument will be sent to for signing.
  'hostedNumberOrderSids': ["null"], // [String] | A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
  'status': "status_example" // AuthorizationDocumentEnumStatus | 
};
apiInstance.updateHostedNumbersAuthorizationDocument(sid, opts, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this AuthorizationDocument. | 
 **addressSid** | **String**| A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument. | [optional] 
 **ccEmails** | [**[String]**](String.md)| Email recipients who will be informed when an Authorization Document has been sent and signed | [optional] 
 **contactPhoneNumber** | **String**| The contact phone number of the person authorized to sign the Authorization Document. | [optional] 
 **contactTitle** | **String**| The title of the person authorized to sign the Authorization Document for this phone number. | [optional] 
 **email** | **String**| Email that this AuthorizationDocument will be sent to for signing. | [optional] 
 **hostedNumberOrderSids** | [**[String]**](String.md)| A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio&#39;s platform. | [optional] 
 **status** | **AuthorizationDocumentEnumStatus**|  | [optional] 

### Return type

[**PreviewHostedNumbersAuthorizationDocument**](PreviewHostedNumbersAuthorizationDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


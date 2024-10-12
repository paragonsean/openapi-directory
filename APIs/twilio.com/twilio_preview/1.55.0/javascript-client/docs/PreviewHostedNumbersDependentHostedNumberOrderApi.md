# TwilioPreview.PreviewHostedNumbersDependentHostedNumberOrderApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listHostedNumbersDependentHostedNumberOrder**](PreviewHostedNumbersDependentHostedNumberOrderApi.md#listHostedNumbersDependentHostedNumberOrder) | **GET** /HostedNumbers/AuthorizationDocuments/{SigningDocumentSid}/DependentHostedNumberOrders | 



## listHostedNumbersDependentHostedNumberOrder

> ListHostedNumbersDependentHostedNumberOrderResponse listHostedNumbersDependentHostedNumberOrder(signingDocumentSid, opts)



Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewHostedNumbersDependentHostedNumberOrderApi();
let signingDocumentSid = "signingDocumentSid_example"; // String | A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder.
let opts = {
  'status': "status_example", // DependentHostedNumberOrderEnumStatus | Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
  'phoneNumber': "phoneNumber_example", // String | An E164 formatted phone number hosted by this HostedNumberOrder.
  'incomingPhoneNumberSid': "incomingPhoneNumberSid_example", // String | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 64 characters.
  'uniqueName': "uniqueName_example", // String | Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listHostedNumbersDependentHostedNumberOrder(signingDocumentSid, opts, (error, data, response) => {
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
 **signingDocumentSid** | **String**| A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder. | 
 **status** | **DependentHostedNumberOrderEnumStatus**| Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses. | [optional] 
 **phoneNumber** | **String**| An E164 formatted phone number hosted by this HostedNumberOrder. | [optional] 
 **incomingPhoneNumberSid** | **String**| A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. | [optional] 
 **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] 
 **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListHostedNumbersDependentHostedNumberOrderResponse**](ListHostedNumbersDependentHostedNumberOrderResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


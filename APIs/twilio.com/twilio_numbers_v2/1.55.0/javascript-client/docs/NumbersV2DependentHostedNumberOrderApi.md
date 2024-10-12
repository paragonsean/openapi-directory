# TwilioNumbers.NumbersV2DependentHostedNumberOrderApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listDependentHostedNumberOrder**](NumbersV2DependentHostedNumberOrderApi.md#listDependentHostedNumberOrder) | **GET** /v2/HostedNumber/AuthorizationDocuments/{SigningDocumentSid}/DependentHostedNumberOrders | 



## listDependentHostedNumberOrder

> ListDependentHostedNumberOrderResponse listDependentHostedNumberOrder(signingDocumentSid, opts)



Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2DependentHostedNumberOrderApi();
let signingDocumentSid = "signingDocumentSid_example"; // String | A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder.
let opts = {
  'status': "status_example", // DependentHostedNumberOrderEnumStatus | Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
  'phoneNumber': "phoneNumber_example", // String | An E164 formatted phone number hosted by this HostedNumberOrder.
  'incomingPhoneNumberSid': "incomingPhoneNumberSid_example", // String | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 128 characters.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDependentHostedNumberOrder(signingDocumentSid, opts, (error, data, response) => {
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
 **friendlyName** | **String**| A human readable description of this resource, up to 128 characters. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDependentHostedNumberOrderResponse**](ListDependentHostedNumberOrderResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


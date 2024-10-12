# TwilioNumbers.NumbersV2SupportingDocumentApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSupportingDocument**](NumbersV2SupportingDocumentApi.md#createSupportingDocument) | **POST** /v2/RegulatoryCompliance/SupportingDocuments | 
[**deleteSupportingDocument**](NumbersV2SupportingDocumentApi.md#deleteSupportingDocument) | **DELETE** /v2/RegulatoryCompliance/SupportingDocuments/{Sid} | 
[**fetchSupportingDocument**](NumbersV2SupportingDocumentApi.md#fetchSupportingDocument) | **GET** /v2/RegulatoryCompliance/SupportingDocuments/{Sid} | 
[**listSupportingDocument**](NumbersV2SupportingDocumentApi.md#listSupportingDocument) | **GET** /v2/RegulatoryCompliance/SupportingDocuments | 
[**updateSupportingDocument**](NumbersV2SupportingDocumentApi.md#updateSupportingDocument) | **POST** /v2/RegulatoryCompliance/SupportingDocuments/{Sid} | 



## createSupportingDocument

> NumbersV2RegulatoryComplianceSupportingDocument createSupportingDocument(friendlyName, type, opts)



Create a new Supporting Document.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2SupportingDocumentApi();
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
let type = "type_example"; // String | The type of the Supporting Document.
let opts = {
  'attributes': null // Object | The set of parameters that are the attributes of the Supporting Documents resource which are derived Supporting Document Types.
};
apiInstance.createSupportingDocument(friendlyName, type, opts, (error, data, response) => {
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
 **friendlyName** | **String**| The string that you assigned to describe the resource. | 
 **type** | **String**| The type of the Supporting Document. | 
 **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the Supporting Documents resource which are derived Supporting Document Types. | [optional] 

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocument**](NumbersV2RegulatoryComplianceSupportingDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSupportingDocument

> deleteSupportingDocument(sid)



Delete a specific Supporting Document.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2SupportingDocumentApi();
let sid = "sid_example"; // String | The unique string created by Twilio to identify the Supporting Document resource.
apiInstance.deleteSupportingDocument(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string created by Twilio to identify the Supporting Document resource. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSupportingDocument

> NumbersV2RegulatoryComplianceSupportingDocument fetchSupportingDocument(sid)



Fetch specific Supporting Document Instance.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2SupportingDocumentApi();
let sid = "sid_example"; // String | The unique string created by Twilio to identify the Supporting Document resource.
apiInstance.fetchSupportingDocument(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string created by Twilio to identify the Supporting Document resource. | 

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocument**](NumbersV2RegulatoryComplianceSupportingDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSupportingDocument

> ListSupportingDocumentResponse listSupportingDocument(opts)



Retrieve a list of all Supporting Document for an account.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2SupportingDocumentApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSupportingDocument(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSupportingDocumentResponse**](ListSupportingDocumentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSupportingDocument

> NumbersV2RegulatoryComplianceSupportingDocument updateSupportingDocument(sid, opts)



Update an existing Supporting Document.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2SupportingDocumentApi();
let sid = "sid_example"; // String | The unique string created by Twilio to identify the Supporting Document resource.
let opts = {
  'attributes': null, // Object | The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types.
  'friendlyName': "friendlyName_example" // String | The string that you assigned to describe the resource.
};
apiInstance.updateSupportingDocument(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string created by Twilio to identify the Supporting Document resource. | 
 **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocument**](NumbersV2RegulatoryComplianceSupportingDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


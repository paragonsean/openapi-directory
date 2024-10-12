# TwilioTrusthub.TrusthubV1SupportingDocumentApi

All URIs are relative to *https://trusthub.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSupportingDocument**](TrusthubV1SupportingDocumentApi.md#createSupportingDocument) | **POST** /v1/SupportingDocuments | 
[**deleteSupportingDocument**](TrusthubV1SupportingDocumentApi.md#deleteSupportingDocument) | **DELETE** /v1/SupportingDocuments/{Sid} | 
[**fetchSupportingDocument**](TrusthubV1SupportingDocumentApi.md#fetchSupportingDocument) | **GET** /v1/SupportingDocuments/{Sid} | 
[**listSupportingDocument**](TrusthubV1SupportingDocumentApi.md#listSupportingDocument) | **GET** /v1/SupportingDocuments | 
[**updateSupportingDocument**](TrusthubV1SupportingDocumentApi.md#updateSupportingDocument) | **POST** /v1/SupportingDocuments/{Sid} | 



## createSupportingDocument

> TrusthubV1SupportingDocument createSupportingDocument(friendlyName, type, opts)



Create a new Supporting Document.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1SupportingDocumentApi();
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

[**TrusthubV1SupportingDocument**](TrusthubV1SupportingDocument.md)

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
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1SupportingDocumentApi();
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

> TrusthubV1SupportingDocument fetchSupportingDocument(sid)



Fetch specific Supporting Document Instance.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1SupportingDocumentApi();
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

[**TrusthubV1SupportingDocument**](TrusthubV1SupportingDocument.md)

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
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1SupportingDocumentApi();
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

> TrusthubV1SupportingDocument updateSupportingDocument(sid, opts)



Update an existing Supporting Document.

### Example

```javascript
import TwilioTrusthub from 'twilio_trusthub';
let defaultClient = TwilioTrusthub.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrusthub.TrusthubV1SupportingDocumentApi();
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

[**TrusthubV1SupportingDocument**](TrusthubV1SupportingDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


# BulkSmsJsonRestApi.BlockedNumbersApi

All URIs are relative to *https://api.bulksms.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blockedNumbersGet**](BlockedNumbersApi.md#blockedNumbersGet) | **GET** /blocked-numbers | List blocked numbers
[**blockedNumbersPost**](BlockedNumbersApi.md#blockedNumbersPost) | **POST** /blocked-numbers | Create a blocked number



## blockedNumbersGet

> BlockedNumber blockedNumbersGet(opts)

List blocked numbers

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.BlockedNumbersApi();
let opts = {
  'minId': 56, // Number | Records with an `id` that is greater or equal to min-id will be returned. The default value is `0`.  You can add 1 to an id that you previously retrieved, to return subsequent records.
  'limit': 56 // Number | The maximum number of records to return. The default value is `10000`. The value cannot be greater than 10000.
};
apiInstance.blockedNumbersGet(opts, (error, data, response) => {
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
 **minId** | **Number**| Records with an &#x60;id&#x60; that is greater or equal to min-id will be returned. The default value is &#x60;0&#x60;.  You can add 1 to an id that you previously retrieved, to return subsequent records. | [optional] 
 **limit** | **Number**| The maximum number of records to return. The default value is &#x60;10000&#x60;. The value cannot be greater than 10000. | [optional] 

### Return type

[**BlockedNumber**](BlockedNumber.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockedNumbersPost

> blockedNumbersPost(requestBody)

Create a blocked number

Blocked numbers are phone numbers to which your account is not permitted to send messages. The numbers can be created via this API, by a recipient replying with a STOP message to one of your previous SENT messages, or by a BulkSMS administrator.  Sending a message to a blocked number will result in the message being assigned a status of &#x60;FAILED.BLOCKED&#x60;. Messages sent to blocked numbers are billed to your account. 

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.BlockedNumbersApi();
let requestBody = ["44123456789"]; // [String] | Maximum size: `1000` items
apiInstance.blockedNumbersPost(requestBody, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)| Maximum size: &#x60;1000&#x60; items | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


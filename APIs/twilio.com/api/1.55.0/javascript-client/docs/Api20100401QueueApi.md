# TwilioApi.Api20100401QueueApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createQueue**](Api20100401QueueApi.md#createQueue) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues.json | 
[**deleteQueue**](Api20100401QueueApi.md#deleteQueue) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json | 
[**fetchQueue**](Api20100401QueueApi.md#fetchQueue) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json | 
[**listQueue**](Api20100401QueueApi.md#listQueue) | **GET** /2010-04-01/Accounts/{AccountSid}/Queues.json | 
[**updateQueue**](Api20100401QueueApi.md#updateQueue) | **POST** /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json | 



## createQueue

> ApiV2010AccountQueue createQueue(accountSid, friendlyName, opts)



Create a queue

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401QueueApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you created to describe this resource. It can be up to 64 characters long.
let opts = {
  'maxSize': 56 // Number | The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
};
apiInstance.createQueue(accountSid, friendlyName, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | 
 **friendlyName** | **String**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. | 
 **maxSize** | **Number**| The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000. | [optional] 

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteQueue

> deleteQueue(accountSid, sid)



Remove an empty queue

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401QueueApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Queue resource to delete
apiInstance.deleteQueue(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Queue resource to delete | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchQueue

> ApiV2010AccountQueue fetchQueue(accountSid, sid)



Fetch an instance of a queue identified by the QueueSid

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401QueueApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Queue resource to fetch
apiInstance.fetchQueue(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Queue resource to fetch | 

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listQueue

> ListQueueResponse listQueue(accountSid, opts)



Retrieve a list of queues belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401QueueApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listQueue(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListQueueResponse**](ListQueueResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateQueue

> ApiV2010AccountQueue updateQueue(accountSid, sid, opts)



Update the queue with the new parameters

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401QueueApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Queue resource to update
let opts = {
  'friendlyName': "friendlyName_example", // String | A descriptive string that you created to describe this resource. It can be up to 64 characters long.
  'maxSize': 56 // Number | The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
};
apiInstance.updateQueue(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Queue resource to update | 
 **friendlyName** | **String**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. | [optional] 
 **maxSize** | **Number**| The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000. | [optional] 

### Return type

[**ApiV2010AccountQueue**](ApiV2010AccountQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


# EnodeApi.WebhooksApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postWebhooksFirehoseTest**](WebhooksApi.md#postWebhooksFirehoseTest) | **POST** /webhooks/firehose/test | Test Firehose Webhook
[**putWebhooksFirehose**](WebhooksApi.md#putWebhooksFirehose) | **PUT** /webhooks/firehose | Update Firehose Webhook



## postWebhooksFirehoseTest

> String postWebhooksFirehoseTest()

Test Firehose Webhook

Trigger a test payload to be sent to your configured Firehose Webhook url.

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ClientAccessToken
let ClientAccessToken = defaultClient.authentications['ClientAccessToken'];
ClientAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.WebhooksApi();
apiInstance.postWebhooksFirehoseTest((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putWebhooksFirehose

> putWebhooksFirehose(opts)

Update Firehose Webhook

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ClientAccessToken
let ClientAccessToken = defaultClient.authentications['ClientAccessToken'];
ClientAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.WebhooksApi();
let opts = {
  'putWebhooksFirehoseRequest': new EnodeApi.PutWebhooksFirehoseRequest() // PutWebhooksFirehoseRequest | 
};
apiInstance.putWebhooksFirehose(opts, (error, data, response) => {
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
 **putWebhooksFirehoseRequest** | [**PutWebhooksFirehoseRequest**](PutWebhooksFirehoseRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


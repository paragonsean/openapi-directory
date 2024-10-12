# FilesComApi.WebhookTestsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postWebhookTests**](WebhookTestsApi.md#postWebhookTests) | **POST** /webhook_tests | Create Webhook Test



## postWebhookTests

> WebhookTestEntity postWebhookTests(url, opts)

Create Webhook Test

Create Webhook Test

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.WebhookTestsApi();
let url = "url_example"; // String | URL for testing the webhook.
let opts = {
  'action': "action_example", // String | action for test body
  'body': {key: null}, // Object | Additional body parameters.
  'encoding': "encoding_example", // String | HTTP encoding method.  Can be JSON, XML, or RAW (form data).
  'fileAsBody': true, // Boolean | Send the file data as the request body?
  'fileFormField': "fileFormField_example", // String | Send the file data as a named parameter in the request POST body
  'headers': {key: null}, // Object | Additional request headers.
  'method': "method_example", // String | HTTP method(GET or POST).
  'rawBody': "rawBody_example" // String | raw body text
};
apiInstance.postWebhookTests(url, opts, (error, data, response) => {
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
 **url** | **String**| URL for testing the webhook. | 
 **action** | **String**| action for test body | [optional] 
 **body** | [**Object**](Object.md)| Additional body parameters. | [optional] 
 **encoding** | **String**| HTTP encoding method.  Can be JSON, XML, or RAW (form data). | [optional] 
 **fileAsBody** | **Boolean**| Send the file data as the request body? | [optional] 
 **fileFormField** | **String**| Send the file data as a named parameter in the request POST body | [optional] 
 **headers** | [**Object**](Object.md)| Additional request headers. | [optional] 
 **method** | **String**| HTTP method(GET or POST). | [optional] 
 **rawBody** | **String**| raw body text | [optional] 

### Return type

[**WebhookTestEntity**](WebhookTestEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


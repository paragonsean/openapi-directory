# FilesComApi.ActionWebhookFailuresApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postActionWebhookFailuresIdRetry**](ActionWebhookFailuresApi.md#postActionWebhookFailuresIdRetry) | **POST** /action_webhook_failures/{id}/retry | retry Action Webhook Failure



## postActionWebhookFailuresIdRetry

> postActionWebhookFailuresIdRetry(id)

retry Action Webhook Failure

retry Action Webhook Failure

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ActionWebhookFailuresApi();
let id = 56; // Number | Action Webhook Failure ID.
apiInstance.postActionWebhookFailuresIdRetry(id, (error, data, response) => {
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
 **id** | **Number**| Action Webhook Failure ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


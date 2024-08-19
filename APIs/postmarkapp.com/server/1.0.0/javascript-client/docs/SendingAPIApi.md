# PostmarkApi.SendingAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendEmail**](SendingAPIApi.md#sendEmail) | **POST** /email | Send a single email
[**sendEmailBatch**](SendingAPIApi.md#sendEmailBatch) | **POST** /email/batch | Send a batch of emails
[**sendEmailBatchWithTemplates**](SendingAPIApi.md#sendEmailBatchWithTemplates) | **POST** /email/batchWithTemplates | Send a batch of email using templates.
[**sendEmailWithTemplate**](SendingAPIApi.md#sendEmailWithTemplate) | **POST** /email/withTemplate | Send an email using a Template



## sendEmail

> SendEmailResponse sendEmail(xPostmarkServerToken, opts)

Send a single email

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.SendingAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'body': new PostmarkApi.SendEmailRequest() // SendEmailRequest | 
};
apiInstance.sendEmail(xPostmarkServerToken, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **body** | [**SendEmailRequest**](SendEmailRequest.md)|  | [optional] 

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEmailBatch

> [SendEmailResponse] sendEmailBatch(xPostmarkServerToken, opts)

Send a batch of emails

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.SendingAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'body': [new PostmarkApi.SendEmailRequest()] // [SendEmailRequest] | 
};
apiInstance.sendEmailBatch(xPostmarkServerToken, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **body** | [**[SendEmailRequest]**](SendEmailRequest.md)|  | [optional] 

### Return type

[**[SendEmailResponse]**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEmailBatchWithTemplates

> [SendEmailResponse] sendEmailBatchWithTemplates(xPostmarkServerToken, body)

Send a batch of email using templates.

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.SendingAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let body = new PostmarkApi.SendEmailTemplatedBatchRequest(); // SendEmailTemplatedBatchRequest | 
apiInstance.sendEmailBatchWithTemplates(xPostmarkServerToken, body, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **body** | [**SendEmailTemplatedBatchRequest**](SendEmailTemplatedBatchRequest.md)|  | 

### Return type

[**[SendEmailResponse]**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEmailWithTemplate

> SendEmailResponse sendEmailWithTemplate(xPostmarkServerToken, body)

Send an email using a Template

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.SendingAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let body = new PostmarkApi.EmailWithTemplateRequest(); // EmailWithTemplateRequest | 
apiInstance.sendEmailWithTemplate(xPostmarkServerToken, body, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **body** | [**EmailWithTemplateRequest**](EmailWithTemplateRequest.md)|  | 

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


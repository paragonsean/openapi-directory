# PostmarkApi.TemplatesAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteTemplate**](TemplatesAPIApi.md#deleteTemplate) | **DELETE** /templates/{templateIdOrAlias} | Delete a Template
[**getSingleTemplate**](TemplatesAPIApi.md#getSingleTemplate) | **GET** /templates/{templateIdOrAlias} | Get a Template
[**listTemplates**](TemplatesAPIApi.md#listTemplates) | **GET** /templates | Get the Templates associated with this Server
[**sendEmailBatchWithTemplates_0**](TemplatesAPIApi.md#sendEmailBatchWithTemplates_0) | **POST** /email/batchWithTemplates | Send a batch of email using templates.
[**sendEmailWithTemplate_0**](TemplatesAPIApi.md#sendEmailWithTemplate_0) | **POST** /email/withTemplate | Send an email using a Template
[**templatesPost**](TemplatesAPIApi.md#templatesPost) | **POST** /templates | Create a Template
[**testTemplateContent**](TemplatesAPIApi.md#testTemplateContent) | **POST** /templates/validate | Test Template Content
[**updateTemplate**](TemplatesAPIApi.md#updateTemplate) | **PUT** /templates/{templateIdOrAlias} | Update a Template



## deleteTemplate

> TemplateDetailResponse deleteTemplate(xPostmarkServerToken, templateIdOrAlias)

Delete a Template

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let templateIdOrAlias = "templateIdOrAlias_example"; // String | The 'TemplateID' or 'Alias' value for the Template you wish to delete.
apiInstance.deleteTemplate(xPostmarkServerToken, templateIdOrAlias, (error, data, response) => {
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
 **templateIdOrAlias** | **String**| The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to delete. | 

### Return type

[**TemplateDetailResponse**](TemplateDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSingleTemplate

> TemplateDetailResponse getSingleTemplate(xPostmarkServerToken, templateIdOrAlias)

Get a Template

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let templateIdOrAlias = "templateIdOrAlias_example"; // String | The 'TemplateID' or 'Alias' value for the Template you wish to retrieve.
apiInstance.getSingleTemplate(xPostmarkServerToken, templateIdOrAlias, (error, data, response) => {
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
 **templateIdOrAlias** | **String**| The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to retrieve. | 

### Return type

[**TemplateDetailResponse**](TemplateDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTemplates

> TemplateListingResponse listTemplates(xPostmarkServerToken, count, offset)

Get the Templates associated with this Server

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let count = 3.4; // Number | The number of Templates to return
let offset = 3.4; // Number | The number of Templates to \"skip\" before returning results.
apiInstance.listTemplates(xPostmarkServerToken, count, offset, (error, data, response) => {
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
 **count** | **Number**| The number of Templates to return | 
 **offset** | **Number**| The number of Templates to \&quot;skip\&quot; before returning results. | 

### Return type

[**TemplateListingResponse**](TemplateListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendEmailBatchWithTemplates_0

> [SendEmailResponse] sendEmailBatchWithTemplates_0(xPostmarkServerToken, body)

Send a batch of email using templates.

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let body = new PostmarkApi.SendEmailTemplatedBatchRequest(); // SendEmailTemplatedBatchRequest | 
apiInstance.sendEmailBatchWithTemplates_0(xPostmarkServerToken, body, (error, data, response) => {
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


## sendEmailWithTemplate_0

> SendEmailResponse sendEmailWithTemplate_0(xPostmarkServerToken, body)

Send an email using a Template

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let body = new PostmarkApi.EmailWithTemplateRequest(); // EmailWithTemplateRequest | 
apiInstance.sendEmailWithTemplate_0(xPostmarkServerToken, body, (error, data, response) => {
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


## templatesPost

> TemplateRecordResponse templatesPost(xPostmarkServerToken, body)

Create a Template

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let body = new PostmarkApi.CreateTemplateRequest(); // CreateTemplateRequest | 
apiInstance.templatesPost(xPostmarkServerToken, body, (error, data, response) => {
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
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

[**TemplateRecordResponse**](TemplateRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## testTemplateContent

> TemplateValidationResponse testTemplateContent(xPostmarkServerToken, opts)

Test Template Content

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'body': new PostmarkApi.TemplateValidationRequest() // TemplateValidationRequest | 
};
apiInstance.testTemplateContent(xPostmarkServerToken, opts, (error, data, response) => {
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
 **body** | [**TemplateValidationRequest**](TemplateValidationRequest.md)|  | [optional] 

### Return type

[**TemplateValidationResponse**](TemplateValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTemplate

> TemplateRecordResponse updateTemplate(xPostmarkServerToken, templateIdOrAlias, body)

Update a Template

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.TemplatesAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let templateIdOrAlias = "templateIdOrAlias_example"; // String | The 'TemplateID' or 'Alias' value for the Template you wish to update.
let body = new PostmarkApi.EditTemplateRequest(); // EditTemplateRequest | 
apiInstance.updateTemplate(xPostmarkServerToken, templateIdOrAlias, body, (error, data, response) => {
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
 **templateIdOrAlias** | **String**| The &#39;TemplateID&#39; or &#39;Alias&#39; value for the Template you wish to update. | 
 **body** | [**EditTemplateRequest**](EditTemplateRequest.md)|  | 

### Return type

[**TemplateRecordResponse**](TemplateRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


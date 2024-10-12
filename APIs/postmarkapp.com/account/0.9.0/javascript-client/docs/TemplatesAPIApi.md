# PostmarkAccountLevelApi.TemplatesAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pushTemplates**](TemplatesAPIApi.md#pushTemplates) | **PUT** /templates/push | Push templates from one server to another



## pushTemplates

> TemplatesPushResponse pushTemplates(xPostmarkAccountToken, body)

Push templates from one server to another

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.TemplatesAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let body = new PostmarkAccountLevelApi.TemplatesPushModel(); // TemplatesPushModel | 
apiInstance.pushTemplates(xPostmarkAccountToken, body, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **body** | [**TemplatesPushModel**](TemplatesPushModel.md)|  | 

### Return type

[**TemplatesPushResponse**](TemplatesPushResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


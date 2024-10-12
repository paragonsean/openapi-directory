# CarboneApi.RenderApi

All URIs are relative to *https://api.carbone.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**renderRenderIdGet**](RenderApi.md#renderRenderIdGet) | **GET** /render/{renderId} | Retreive a generated document from a render ID.
[**renderTemplateIdPost**](RenderApi.md#renderTemplateIdPost) | **POST** /render/{templateId} | Generate a document from a template ID, and a JSON data-set



## renderRenderIdGet

> renderRenderIdGet(renderId, carboneVersion)

Retreive a generated document from a render ID.

Documentation: https://carbone.io/api-reference.html#download-rendered-reports

### Example

```javascript
import CarboneApi from 'carbone_api';

let apiInstance = new CarboneApi.RenderApi();
let renderId = "renderId_example"; // String | Unique identifier of the report
let carboneVersion = 4; // Number | Carbone version
apiInstance.renderRenderIdGet(renderId, carboneVersion, (error, data, response) => {
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
 **renderId** | **String**| Unique identifier of the report | 
 **carboneVersion** | **Number**| Carbone version | [default to 4]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renderTemplateIdPost

> RenderTemplateIdPost200Response renderTemplateIdPost(templateId, carboneVersion, renderTemplateIdPostRequest)

Generate a document from a template ID, and a JSON data-set

Documentation: https://carbone.io/api-reference.html#render-reports

### Example

```javascript
import CarboneApi from 'carbone_api';
let defaultClient = CarboneApi.ApiClient.instance;
// Configure Bearer (eyJhbGci...) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new CarboneApi.RenderApi();
let templateId = "templateId_example"; // String | Unique identifier of the template
let carboneVersion = 4; // Number | Carbone version
let renderTemplateIdPostRequest = new CarboneApi.RenderTemplateIdPostRequest(); // RenderTemplateIdPostRequest | 
apiInstance.renderTemplateIdPost(templateId, carboneVersion, renderTemplateIdPostRequest, (error, data, response) => {
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
 **templateId** | **String**| Unique identifier of the template | 
 **carboneVersion** | **Number**| Carbone version | [default to 4]
 **renderTemplateIdPostRequest** | [**RenderTemplateIdPostRequest**](RenderTemplateIdPostRequest.md)|  | 

### Return type

[**RenderTemplateIdPost200Response**](RenderTemplateIdPost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


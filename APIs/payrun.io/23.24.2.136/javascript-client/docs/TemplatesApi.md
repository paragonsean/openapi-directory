# PayRunIo.TemplatesApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTemplateModel**](TemplatesApi.md#getTemplateModel) | **GET** /Template/{DtoDataType} | Get the object template
[**getTemplates**](TemplatesApi.md#getTemplates) | **GET** /Templates | Get a list of all available data object tempaltes



## getTemplateModel

> File getTemplateModel(dtoDataType, authorization, apiVersion)

Get the object template

Returns a template instance of the specified data type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TemplatesApi();
let dtoDataType = "dtoDataType_example"; // String | The data transfer object type name. E.g PensionPayInstruction
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTemplateModel(dtoDataType, authorization, apiVersion, (error, data, response) => {
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
 **dtoDataType** | **String**| The data transfer object type name. E.g PensionPayInstruction | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplates

> LinkCollection getTemplates(authorization, apiVersion)

Get a list of all available data object tempaltes

Returns a collection of links to all the available data object templates

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TemplatesApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTemplates(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


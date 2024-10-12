# Opendatasoft.MetadataApi

All URIs are relative to *https://public.opendatasoft.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMetadataTemplate**](MetadataApi.md#getMetadataTemplate) | **GET** /{source}/metadata_templates/{metadata_template_type}/{metadata_template_name} | 
[**getMetadataTemplatesType**](MetadataApi.md#getMetadataTemplatesType) | **GET** /{source}/metadata_templates/{metadata_template_type} | 
[**getMetadataTemplatesTypes**](MetadataApi.md#getMetadataTemplatesTypes) | **GET** /{source}/metadata_templates | 



## getMetadataTemplate

> GetMetadataTemplatesType200ResponseMetadataTemplatesInner getMetadataTemplate(source, metadataTemplateType, metadataTemplateName)



A single metadata_template 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.MetadataApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let metadataTemplateType = "'basic'"; // String | 
let metadataTemplateName = "metadataTemplateName_example"; // String | 
apiInstance.getMetadataTemplate(source, metadataTemplateType, metadataTemplateName, (error, data, response) => {
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
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **metadataTemplateType** | **String**|  | [default to &#39;basic&#39;]
 **metadataTemplateName** | **String**|  | 

### Return type

[**GetMetadataTemplatesType200ResponseMetadataTemplatesInner**](GetMetadataTemplatesType200ResponseMetadataTemplatesInner.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetadataTemplatesType

> GetMetadataTemplatesType200Response getMetadataTemplatesType(source, metadataTemplateType)



List of metadata templates available for this type. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.MetadataApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
let metadataTemplateType = "'basic'"; // String | 
apiInstance.getMetadataTemplatesType(source, metadataTemplateType, (error, data, response) => {
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
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]
 **metadataTemplateType** | **String**|  | [default to &#39;basic&#39;]

### Return type

[**GetMetadataTemplatesType200Response**](GetMetadataTemplatesType200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetadataTemplatesTypes

> GetRoot200Response getMetadataTemplatesTypes(source)



List of available metadata templates types, each with their endpoints. 

### Example

```javascript
import Opendatasoft from 'opendatasoft';
let defaultClient = Opendatasoft.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new Opendatasoft.MetadataApi();
let source = "'catalog'"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
apiInstance.getMetadataTemplatesTypes(source, (error, data, response) => {
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
 **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to &#39;catalog&#39;]

### Return type

[**GetRoot200Response**](GetRoot200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# MasterDataApiV1.AttachmentsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveattachment**](AttachmentsApi.md#retrieveattachment) | **GET** /api/dataentities/{acronym}/documents/{id}/{field}/attachments/{file-name} | Retrieve attachment
[**saveattachment**](AttachmentsApi.md#saveattachment) | **POST** /api/dataentities/{acronym}/documents/{id}/{field}/attachments | Save attachment



## retrieveattachment

> retrieveattachment(acronym, id, field, fileName)

Retrieve attachment

Use this API to retrieve a file.    Be sure to include the file extension in the name. Like in this example:  &#x60;&#x60;&#x60;  /dataentities/CL/documents/123/file/attachments/image.png  &#x60;&#x60;&#x60;

### Example

```javascript
import MasterDataApiV1 from 'master_data_api_v1';
let defaultClient = MasterDataApiV1.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV1.AttachmentsApi();
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let field = "'{{field}}'"; // String | Field to attach the file to, as described in admin
let fileName = "'{{file-name}}'"; // String | 
apiInstance.retrieveattachment(acronym, id, field, fileName, (error, data, response) => {
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
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]
 **field** | **String**| Field to attach the file to, as described in admin | [default to &#39;{{field}}&#39;]
 **fileName** | **String**|  | [default to &#39;{{file-name}}&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## saveattachment

> saveattachment(acronym, id, field, file)

Save attachment

This API allows you to save a file in a field of type &#x60;File&#x60;.    When using in javascript, you must add the header &#x60;content-type&#x60; with value &#x60;multipart/form-data;&#x60;    You can upload more than one file. Just add a new field in the &#x60;form-data&#x60; with type &#x60;File&#x60;.

### Example

```javascript
import MasterDataApiV1 from 'master_data_api_v1';
let defaultClient = MasterDataApiV1.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MasterDataApiV1.AttachmentsApi();
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let field = "'{{field}}'"; // String | Field to attach the file to, as described in admin
let file = ["null"]; // [File] | 
apiInstance.saveattachment(acronym, id, field, file, (error, data, response) => {
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
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]
 **field** | **String**| Field to attach the file to, as described in admin | [default to &#39;{{field}}&#39;]
 **file** | **[File]**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


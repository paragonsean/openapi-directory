# WatchfulLi.ExtensionsApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExtensions**](ExtensionsApi.md#getExtensions) | **GET** /extensions | Get a list Extensions
[**getFieldsExtensions**](ExtensionsApi.md#getFieldsExtensions) | **GET** /extensions/metadata | Get the list of fields
[**ignoreExtensionUpdate**](ExtensionsApi.md#ignoreExtensionUpdate) | **POST** /extensions/{id}/ignore | Set &#39;ignore updates&#39; for a given extension / site_id
[**unignoreExtensionUpdate**](ExtensionsApi.md#unignoreExtensionUpdate) | **POST** /extensions/{id}/unignore | Remove &#39;ignore updates&#39; for a given extension
[**updateExtension**](ExtensionsApi.md#updateExtension) | **POST** /extensions/{id}/update | Update the extension on the remote site



## getExtensions

> Extension getExtensions(opts)

Get a list Extensions

Returns a list Extensions

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.ExtensionsApi();
let opts = {
  'extName': "extName_example", // String | Do a 'LIKE' search, you can also use '%'
  'siteids': "siteids_example", // String | List of sites id separated by comma
  'extPrefix': "extPrefix_example", // String | Do a 'LIKE' search, you can also use '%'. technical name of the extension com_xxxx
  'version': "version_example", // String | Do a 'LIKE' search, you can also use '%'
  'vUpdate': 56, // Number | update available for this extension
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
};
apiInstance.getExtensions(opts, (error, data, response) => {
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
 **extName** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **siteids** | **String**| List of sites id separated by comma | [optional] 
 **extPrefix** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;. technical name of the extension com_xxxx | [optional] 
 **version** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **vUpdate** | **Number**| update available for this extension | [optional] 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] 

### Return type

[**Extension**](Extension.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getFieldsExtensions

> String getFieldsExtensions()

Get the list of fields

Returns a list of fields

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.ExtensionsApi();
apiInstance.getFieldsExtensions((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## ignoreExtensionUpdate

> String ignoreExtensionUpdate(id)

Set &#39;ignore updates&#39; for a given extension / site_id

Set &#39;ignore updates&#39; for a given extension / site_id

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.ExtensionsApi();
let id = 789; // Number | ID of the extension
apiInstance.ignoreExtensionUpdate(id, (error, data, response) => {
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
 **id** | **Number**| ID of the extension | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## unignoreExtensionUpdate

> String unignoreExtensionUpdate(id)

Remove &#39;ignore updates&#39; for a given extension

Remove &#39;ignore updates&#39; for a given extension

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.ExtensionsApi();
let id = 789; // Number | ID of the extension
apiInstance.unignoreExtensionUpdate(id, (error, data, response) => {
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
 **id** | **Number**| ID of the extension | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## updateExtension

> String updateExtension(id)

Update the extension on the remote site

Update the extension on the remote site

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.ExtensionsApi();
let id = 789; // Number | ID of the extension
apiInstance.updateExtension(id, (error, data, response) => {
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
 **id** | **Number**| ID of the extension | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


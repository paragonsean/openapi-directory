# AgcoApi.TranslationKeysApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translationKeysCreateTranslationKey**](TranslationKeysApi.md#translationKeysCreateTranslationKey) | **POST** /api/v2/TranslationKeys | Create a translationKey object.
[**translationKeysGet**](TranslationKeysApi.md#translationKeysGet) | **GET** /api/v2/TranslationKeys | Get a paged response of TranslationKeys.
[**translationKeysGetTranslationKey**](TranslationKeysApi.md#translationKeysGetTranslationKey) | **GET** /api/v2/TranslationKeys/{ID} | Get TranslationKey by ID
[**translationKeysUpdateTranslationKey**](TranslationKeysApi.md#translationKeysUpdateTranslationKey) | **PUT** /api/v2/TranslationKeys/{ID} | Update the StringID of the translationKey object.



## translationKeysCreateTranslationKey

> Number translationKeysCreateTranslationKey(oASSupportSharedModelsTranslationKey)

Create a translationKey object.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationKeysApi();
let oASSupportSharedModelsTranslationKey = new AgcoApi.OASSupportSharedModelsTranslationKey(); // OASSupportSharedModelsTranslationKey | 
apiInstance.translationKeysCreateTranslationKey(oASSupportSharedModelsTranslationKey, (error, data, response) => {
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
 **oASSupportSharedModelsTranslationKey** | [**OASSupportSharedModelsTranslationKey**](OASSupportSharedModelsTranslationKey.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## translationKeysGet

> APIIPagedResponseOASSupportSharedModelsTranslationKey translationKeysGet(opts)

Get a paged response of TranslationKeys.



### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationKeysApi();
let opts = {
  'limit': 56, // Number | 
  'offset': 56, // Number | 
  'keyNames': "keyNames_example" // String | Can filter by keyNames, a comma deliminated list.
};
apiInstance.translationKeysGet(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 
 **keyNames** | **String**| Can filter by keyNames, a comma deliminated list. | [optional] 

### Return type

[**APIIPagedResponseOASSupportSharedModelsTranslationKey**](APIIPagedResponseOASSupportSharedModelsTranslationKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationKeysGetTranslationKey

> OASSupportSharedModelsTranslationKey translationKeysGetTranslationKey(ID)

Get TranslationKey by ID

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationKeysApi();
let ID = 56; // Number | 
apiInstance.translationKeysGetTranslationKey(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**OASSupportSharedModelsTranslationKey**](OASSupportSharedModelsTranslationKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationKeysUpdateTranslationKey

> translationKeysUpdateTranslationKey(ID, oASSupportSharedModelsTranslationKey)

Update the StringID of the translationKey object.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationKeysApi();
let ID = 56; // Number | 
let oASSupportSharedModelsTranslationKey = new AgcoApi.OASSupportSharedModelsTranslationKey(); // OASSupportSharedModelsTranslationKey | 
apiInstance.translationKeysUpdateTranslationKey(ID, oASSupportSharedModelsTranslationKey, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **oASSupportSharedModelsTranslationKey** | [**OASSupportSharedModelsTranslationKey**](OASSupportSharedModelsTranslationKey.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


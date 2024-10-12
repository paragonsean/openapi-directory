# AgcoApi.StringTranslationsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stringTranslationsGetTranslation**](StringTranslationsApi.md#stringTranslationsGetTranslation) | **GET** /api/v2/StringTranslations/{stringId}/{languageId} | Get a single translation based upon stringId and languageId
[**stringTranslationsGetTranslations**](StringTranslationsApi.md#stringTranslationsGetTranslations) | **GET** /api/v2/StringTranslations | Get a paged response of Global String Translations.
[**stringTranslationsUpdateTranslation**](StringTranslationsApi.md#stringTranslationsUpdateTranslation) | **PUT** /api/v2/StringTranslations/{stringId}/{languageId} | Update a string value or a state for a string translation.
[**stringTranslationsUpdateTranslations**](StringTranslationsApi.md#stringTranslationsUpdateTranslations) | **PUT** /api/v2/StringTranslations/Batch | Update corrections to string translations



## stringTranslationsGetTranslation

> GlobalResourcesSharedModelsStringTranslation stringTranslationsGetTranslation(stringId, languageId)

Get a single translation based upon stringId and languageId

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringTranslationsApi();
let stringId = "stringId_example"; // String | 
let languageId = 56; // Number | 
apiInstance.stringTranslationsGetTranslation(stringId, languageId, (error, data, response) => {
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
 **stringId** | **String**|  | 
 **languageId** | **Number**|  | 

### Return type

[**GlobalResourcesSharedModelsStringTranslation**](GlobalResourcesSharedModelsStringTranslation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stringTranslationsGetTranslations

> APIIPagedResponseGlobalResourcesSharedModelsStringTranslation stringTranslationsGetTranslations(opts)

Get a paged response of Global String Translations.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringTranslationsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'modifiedAfterTimestamp': "modifiedAfterTimestamp_example" // String | Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
};
apiInstance.stringTranslationsGetTranslations(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **modifiedAfterTimestamp** | **String**| Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array. | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsStringTranslation**](APIIPagedResponseGlobalResourcesSharedModelsStringTranslation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stringTranslationsUpdateTranslation

> stringTranslationsUpdateTranslation(stringId, languageId, globalResourcesSharedModelsStringTranslation)

Update a string value or a state for a string translation.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringTranslationsApi();
let stringId = "stringId_example"; // String | 
let languageId = 56; // Number | 
let globalResourcesSharedModelsStringTranslation = new AgcoApi.GlobalResourcesSharedModelsStringTranslation(); // GlobalResourcesSharedModelsStringTranslation | 
apiInstance.stringTranslationsUpdateTranslation(stringId, languageId, globalResourcesSharedModelsStringTranslation, (error, data, response) => {
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
 **stringId** | **String**|  | 
 **languageId** | **Number**|  | 
 **globalResourcesSharedModelsStringTranslation** | [**GlobalResourcesSharedModelsStringTranslation**](GlobalResourcesSharedModelsStringTranslation.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## stringTranslationsUpdateTranslations

> stringTranslationsUpdateTranslations(globalResourcesSharedModelsStringTranslation)

Update corrections to string translations

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StringTranslationsApi();
let globalResourcesSharedModelsStringTranslation = [new AgcoApi.GlobalResourcesSharedModelsStringTranslation()]; // [GlobalResourcesSharedModelsStringTranslation] | 
apiInstance.stringTranslationsUpdateTranslations(globalResourcesSharedModelsStringTranslation, (error, data, response) => {
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
 **globalResourcesSharedModelsStringTranslation** | [**[GlobalResourcesSharedModelsStringTranslation]**](GlobalResourcesSharedModelsStringTranslation.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


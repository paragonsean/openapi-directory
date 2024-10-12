# AgcoApi.LanguagesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**languagesCreateLanguage**](LanguagesApi.md#languagesCreateLanguage) | **POST** /api/v2/Languages | Add a Language to support for translations. Accepts a Language object. Returns the Id of the created object.
[**languagesDeleteLanguage**](LanguagesApi.md#languagesDeleteLanguage) | **DELETE** /api/v2/Languages/{LocaleID} | Remove a Language from those supported for translations. Marks language as deleted.
[**languagesGetLanguage**](LanguagesApi.md#languagesGetLanguage) | **GET** /api/v2/Languages/{LocaleID} | Get a language by its id. Returns a Language object
[**languagesGetLanguages**](LanguagesApi.md#languagesGetLanguages) | **GET** /api/v2/Languages | Get a list of the languages for which translations are supported. Returns a PagedResponse of Language objects.
[**languagesUpdateLanguage**](LanguagesApi.md#languagesUpdateLanguage) | **PUT** /api/v2/Languages/{LocaleID} | Update a language’s description. Accepts a Language object.



## languagesCreateLanguage

> Number languagesCreateLanguage(globalResourcesSharedModelsLanguage)

Add a Language to support for translations. Accepts a Language object. Returns the Id of the created object.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LanguagesApi();
let globalResourcesSharedModelsLanguage = new AgcoApi.GlobalResourcesSharedModelsLanguage(); // GlobalResourcesSharedModelsLanguage | 
apiInstance.languagesCreateLanguage(globalResourcesSharedModelsLanguage, (error, data, response) => {
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
 **globalResourcesSharedModelsLanguage** | [**GlobalResourcesSharedModelsLanguage**](GlobalResourcesSharedModelsLanguage.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## languagesDeleteLanguage

> languagesDeleteLanguage(localeID)

Remove a Language from those supported for translations. Marks language as deleted.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LanguagesApi();
let localeID = 56; // Number | 
apiInstance.languagesDeleteLanguage(localeID, (error, data, response) => {
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
 **localeID** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## languagesGetLanguage

> GlobalResourcesSharedModelsLanguage languagesGetLanguage(localeID)

Get a language by its id. Returns a Language object

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LanguagesApi();
let localeID = 56; // Number | 
apiInstance.languagesGetLanguage(localeID, (error, data, response) => {
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
 **localeID** | **Number**|  | 

### Return type

[**GlobalResourcesSharedModelsLanguage**](GlobalResourcesSharedModelsLanguage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## languagesGetLanguages

> APIIPagedResponseGlobalResourcesSharedModelsLanguage languagesGetLanguages(opts)

Get a list of the languages for which translations are supported. Returns a PagedResponse of Language objects.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LanguagesApi();
let opts = {
  'limit': 56, // Number | limit the number of Language objects returned. Optional (defaults to 10).
  'offset': 56, // Number | the number of Language objects to skip. Optional (defaults to 0).
  'includeDeleted': true // Boolean | whether to include languages marked as deleted. Defaults to false
};
apiInstance.languagesGetLanguages(opts, (error, data, response) => {
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
 **limit** | **Number**| limit the number of Language objects returned. Optional (defaults to 10). | [optional] 
 **offset** | **Number**| the number of Language objects to skip. Optional (defaults to 0). | [optional] 
 **includeDeleted** | **Boolean**| whether to include languages marked as deleted. Defaults to false | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsLanguage**](APIIPagedResponseGlobalResourcesSharedModelsLanguage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## languagesUpdateLanguage

> languagesUpdateLanguage(localeID, globalResourcesSharedModelsLanguage)

Update a language’s description. Accepts a Language object.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LanguagesApi();
let localeID = 56; // Number | 
let globalResourcesSharedModelsLanguage = new AgcoApi.GlobalResourcesSharedModelsLanguage(); // GlobalResourcesSharedModelsLanguage | 
apiInstance.languagesUpdateLanguage(localeID, globalResourcesSharedModelsLanguage, (error, data, response) => {
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
 **localeID** | **Number**|  | 
 **globalResourcesSharedModelsLanguage** | [**GlobalResourcesSharedModelsLanguage**](GlobalResourcesSharedModelsLanguage.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


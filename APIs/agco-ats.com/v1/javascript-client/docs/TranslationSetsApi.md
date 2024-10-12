# AgcoApi.TranslationSetsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translationSetsDeleteTranslationSetAttribute**](TranslationSetsApi.md#translationSetsDeleteTranslationSetAttribute) | **DELETE** /api/v2/TranslationSetAttributes/{ID} | Delete a set of TranslationSetAttribute object
[**translationSetsGetSourceStrings**](TranslationSetsApi.md#translationSetsGetSourceStrings) | **GET** /api/v2/TranslationSets/{ID}/SourceStrings | Gets the information needed to translate a string in a translation set
[**translationSetsGetStatistics**](TranslationSetsApi.md#translationSetsGetStatistics) | **GET** /api/v2/TranslationSets/{ID}/Statistics | Gets the statistics for translation sets such as the language ids and count of string definitions.
[**translationSetsGetTranslationSet**](TranslationSetsApi.md#translationSetsGetTranslationSet) | **GET** /api/v2/TranslationSets/{ID} | Get a TranslationSet object by its id. Related TranslationSetStrings are NOT returned.
[**translationSetsGetTranslationSetAttributes**](TranslationSetsApi.md#translationSetsGetTranslationSetAttributes) | **GET** /api/v2/TranslationSets/{ID}/Attributes | Get a PagedResponse of TranslationSetAttribute objects
[**translationSetsGetTranslationSetStrings**](TranslationSetsApi.md#translationSetsGetTranslationSetStrings) | **GET** /api/v2/TranslationSets/{ID}/Strings | Get a PagedResponse of TranslationSetString objects
[**translationSetsGetTranslationSets**](TranslationSetsApi.md#translationSetsGetTranslationSets) | **GET** /api/v2/TranslationSets | Get a PagedResponse of TranslationSet objects. Related TranslationSetStrings are NOT returned
[**translationSetsPostTranslationSetAttribute**](TranslationSetsApi.md#translationSetsPostTranslationSetAttribute) | **POST** /api/v2/TranslationSets/{ID}/Attributes | Create a TranslationSetAttribute object
[**translationSetsPostTranslationSetAttributes**](TranslationSetsApi.md#translationSetsPostTranslationSetAttributes) | **POST** /api/v2/TranslationSets/{ID}/Attributes/Batch | No Documentation Found.
[**translationSetsUpdateTranslationSet**](TranslationSetsApi.md#translationSetsUpdateTranslationSet) | **PUT** /api/v2/TranslationSets/{ID} | Update a Translation Set. Accepts a TranslationSet object. Only the state property may be updated.
[**translationSetsUpdateTranslationSetAttribute**](TranslationSetsApi.md#translationSetsUpdateTranslationSetAttribute) | **PUT** /api/v2/TranslationSetAttributes/{ID} | Update a TranslationSetAttribute object
[**translationSetsUpdateTranslationSetAttributes**](TranslationSetsApi.md#translationSetsUpdateTranslationSetAttributes) | **PUT** /api/v2/TranslationSetAttributes/Batch | No Documentation Found.
[**translationSetsUpdateTranslationSetStrings**](TranslationSetsApi.md#translationSetsUpdateTranslationSetStrings) | **PUT** /api/v2/TranslationSets/{ID}/Strings | No Documentation Found.



## translationSetsDeleteTranslationSetAttribute

> translationSetsDeleteTranslationSetAttribute(ID)

Delete a set of TranslationSetAttribute object

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
apiInstance.translationSetsDeleteTranslationSetAttribute(ID, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## translationSetsGetSourceStrings

> APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString translationSetsGetSourceStrings(ID, opts)

Gets the information needed to translate a string in a translation set

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let opts = {
  'limit': 56, // Number | 
  'offset': 56 // Number | 
};
apiInstance.translationSetsGetSourceStrings(ID, opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationSetsGetStatistics

> GlobalResourcesSharedModelsTranslationSetStatistics translationSetsGetStatistics(ID)

Gets the statistics for translation sets such as the language ids and count of string definitions.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
apiInstance.translationSetsGetStatistics(ID, (error, data, response) => {
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

[**GlobalResourcesSharedModelsTranslationSetStatistics**](GlobalResourcesSharedModelsTranslationSetStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationSetsGetTranslationSet

> GlobalResourcesSharedModelsTranslationSet translationSetsGetTranslationSet(ID, opts)

Get a TranslationSet object by its id. Related TranslationSetStrings are NOT returned.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let opts = {
  'includeAttributes': "includeAttributes_example" // String | Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
};
apiInstance.translationSetsGetTranslationSet(ID, opts, (error, data, response) => {
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
 **includeAttributes** | **String**| Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] 

### Return type

[**GlobalResourcesSharedModelsTranslationSet**](GlobalResourcesSharedModelsTranslationSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationSetsGetTranslationSetAttributes

> APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute translationSetsGetTranslationSetAttributes(ID, opts)

Get a PagedResponse of TranslationSetAttribute objects

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let opts = {
  'limit': 56, // Number | 
  'offset': 56, // Number | 
  'name': "name_example" // String | 
};
apiInstance.translationSetsGetTranslationSetAttributes(ID, opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 
 **name** | **String**|  | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationSetsGetTranslationSetStrings

> APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString translationSetsGetTranslationSetStrings(ID, opts)

Get a PagedResponse of TranslationSetString objects

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let opts = {
  'limit': 56, // Number | 
  'offset': 56 // Number | 
};
apiInstance.translationSetsGetTranslationSetStrings(ID, opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationSetsGetTranslationSets

> APIIPagedResponseGlobalResourcesSharedModelsTranslationSet translationSetsGetTranslationSets(opts)

Get a PagedResponse of TranslationSet objects. Related TranslationSetStrings are NOT returned

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let opts = {
  'limit': 56, // Number | 
  'offset': 56, // Number | 
  'translationRequestID': 56, // Number | 
  'state': "state_example", // String | 
  'stringId': "stringId_example", // String | 
  'languageId': 56, // Number | 
  'includeAttributes': "includeAttributes_example" // String | Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
};
apiInstance.translationSetsGetTranslationSets(opts, (error, data, response) => {
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
 **translationRequestID** | **Number**|  | [optional] 
 **state** | **String**|  | [optional] 
 **stringId** | **String**|  | [optional] 
 **languageId** | **Number**|  | [optional] 
 **includeAttributes** | **String**| Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included. | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationSet**](APIIPagedResponseGlobalResourcesSharedModelsTranslationSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationSetsPostTranslationSetAttribute

> Number translationSetsPostTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute)

Create a TranslationSetAttribute object

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let globalResourcesSharedModelsTranslationSetAttribute = new AgcoApi.GlobalResourcesSharedModelsTranslationSetAttribute(); // GlobalResourcesSharedModelsTranslationSetAttribute | 
apiInstance.translationSetsPostTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute, (error, data, response) => {
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
 **globalResourcesSharedModelsTranslationSetAttribute** | [**GlobalResourcesSharedModelsTranslationSetAttribute**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## translationSetsPostTranslationSetAttributes

> translationSetsPostTranslationSetAttributes(ID, globalResourcesSharedModelsTranslationSetAttribute)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let globalResourcesSharedModelsTranslationSetAttribute = [new AgcoApi.GlobalResourcesSharedModelsTranslationSetAttribute()]; // [GlobalResourcesSharedModelsTranslationSetAttribute] | 
apiInstance.translationSetsPostTranslationSetAttributes(ID, globalResourcesSharedModelsTranslationSetAttribute, (error, data, response) => {
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
 **globalResourcesSharedModelsTranslationSetAttribute** | [**[GlobalResourcesSharedModelsTranslationSetAttribute]**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## translationSetsUpdateTranslationSet

> translationSetsUpdateTranslationSet(ID, globalResourcesSharedModelsTranslationSet)

Update a Translation Set. Accepts a TranslationSet object. Only the state property may be updated.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let globalResourcesSharedModelsTranslationSet = new AgcoApi.GlobalResourcesSharedModelsTranslationSet(); // GlobalResourcesSharedModelsTranslationSet | 
apiInstance.translationSetsUpdateTranslationSet(ID, globalResourcesSharedModelsTranslationSet, (error, data, response) => {
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
 **globalResourcesSharedModelsTranslationSet** | [**GlobalResourcesSharedModelsTranslationSet**](GlobalResourcesSharedModelsTranslationSet.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## translationSetsUpdateTranslationSetAttribute

> translationSetsUpdateTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute)

Update a TranslationSetAttribute object

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let globalResourcesSharedModelsTranslationSetAttribute = new AgcoApi.GlobalResourcesSharedModelsTranslationSetAttribute(); // GlobalResourcesSharedModelsTranslationSetAttribute | 
apiInstance.translationSetsUpdateTranslationSetAttribute(ID, globalResourcesSharedModelsTranslationSetAttribute, (error, data, response) => {
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
 **globalResourcesSharedModelsTranslationSetAttribute** | [**GlobalResourcesSharedModelsTranslationSetAttribute**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## translationSetsUpdateTranslationSetAttributes

> translationSetsUpdateTranslationSetAttributes(globalResourcesSharedModelsTranslationSetAttribute)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let globalResourcesSharedModelsTranslationSetAttribute = [new AgcoApi.GlobalResourcesSharedModelsTranslationSetAttribute()]; // [GlobalResourcesSharedModelsTranslationSetAttribute] | 
apiInstance.translationSetsUpdateTranslationSetAttributes(globalResourcesSharedModelsTranslationSetAttribute, (error, data, response) => {
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
 **globalResourcesSharedModelsTranslationSetAttribute** | [**[GlobalResourcesSharedModelsTranslationSetAttribute]**](GlobalResourcesSharedModelsTranslationSetAttribute.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## translationSetsUpdateTranslationSetStrings

> translationSetsUpdateTranslationSetStrings(ID, globalResourcesSharedModelsTranslationSetString)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationSetsApi();
let ID = 56; // Number | 
let globalResourcesSharedModelsTranslationSetString = [new AgcoApi.GlobalResourcesSharedModelsTranslationSetString()]; // [GlobalResourcesSharedModelsTranslationSetString] | 
apiInstance.translationSetsUpdateTranslationSetStrings(ID, globalResourcesSharedModelsTranslationSetString, (error, data, response) => {
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
 **globalResourcesSharedModelsTranslationSetString** | [**[GlobalResourcesSharedModelsTranslationSetString]**](GlobalResourcesSharedModelsTranslationSetString.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


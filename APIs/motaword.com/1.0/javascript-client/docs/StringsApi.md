# MotaWordApi.StringsApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clearTranslationCache**](StringsApi.md#clearTranslationCache) | **DELETE** /continuous_projects/{projectId}/strings/cached | Clear translation cache
[**getContinuousProjectFileStrings**](StringsApi.md#getContinuousProjectFileStrings) | **GET** /continuous_projects/{projectId}/documents/{documentId}/strings | View strings their translations in a continuous document
[**getContinuousProjectStrings**](StringsApi.md#getContinuousProjectStrings) | **GET** /continuous_projects/{projectId}/strings | View strings and translations in continuous project
[**getDocumentTranslations**](StringsApi.md#getDocumentTranslations) | **GET** /projects/{projectId}/documents/{documentId}/translations | View strings and translations of a document
[**getDocumentTranslationsForLanguage**](StringsApi.md#getDocumentTranslationsForLanguage) | **GET** /projects/{projectId}/documents/{documentId}/translations/{language} | View strings and translations of a document for target language
[**getProjectStrings**](StringsApi.md#getProjectStrings) | **GET** /projects/{projectId}/strings | View project strings and translations
[**getProjectStringsForLanguage**](StringsApi.md#getProjectStringsForLanguage) | **GET** /projects/{projectId}/strings/{language} | View strings and translations for target language
[**getProjectTranslations**](StringsApi.md#getProjectTranslations) | **GET** /projects/{projectId}/translations | Deprecated. Use /projects/{projectId}/strings instead.
[**getProjectTranslationsForLanguage**](StringsApi.md#getProjectTranslationsForLanguage) | **GET** /projects/{projectId}/translations/{language} | Deprecated. use /projects/{projectId}/strings/{language} instead.
[**getStrings**](StringsApi.md#getStrings) | **GET** /strings | View account strings (translation memory)
[**getTranslationCache**](StringsApi.md#getTranslationCache) | **GET** /continuous_projects/{projectId}/strings/cached | View cached strings translations in continuous project
[**packageProjectTranslationMemory**](StringsApi.md#packageProjectTranslationMemory) | **POST** /projects/{projectId}/strings/package | Download project translation memory
[**packageProjectTranslationMemoryForLanguage**](StringsApi.md#packageProjectTranslationMemoryForLanguage) | **POST** /projects/{projectId}/strings/{languageCode}/package | Download language-specific project translation memory
[**packageProjectTranslationMemoryForLanguageStatus**](StringsApi.md#packageProjectTranslationMemoryForLanguageStatus) | **GET** /projects/{projectId}/strings/{languageCode}/package/status | Check language-specific translation memory packaging status
[**packageProjectTranslationMemoryStatus**](StringsApi.md#packageProjectTranslationMemoryStatus) | **GET** /projects/{projectId}/strings/package/status | Check translation memory packaging status
[**packageUserTranslationMemory**](StringsApi.md#packageUserTranslationMemory) | **POST** /strings/{languageCode}/package | Download account translation memory
[**packageUserTranslationMemoryForLanguageStatus**](StringsApi.md#packageUserTranslationMemoryForLanguageStatus) | **GET** /strings/{languageCode}/package/status | Check account translation memory packaging status
[**postContinuousProjectFileStrings**](StringsApi.md#postContinuousProjectFileStrings) | **POST** /continuous_projects/{projectId}/documents/strings | Get a list of strings and its translations in the project.
[**recacheTranslations**](StringsApi.md#recacheTranslations) | **POST** /continuous_projects/{projectId}/strings/recache-tms | Recache translations
[**updateTranslationMemoryUnit**](StringsApi.md#updateTranslationMemoryUnit) | **PUT** /strings | Update string translation



## clearTranslationCache

> OperationStatus clearTranslationCache(projectId, opts)

Clear translation cache

Clear/delete continuous project translation cache.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let opts = {
  'locale': "locale_example", // String | Locale
  'fileId': 789 // Number | Continuous Project File ID
};
apiInstance.clearTranslationCache(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **locale** | **String**| Locale | [optional] 
 **fileId** | **Number**| Continuous Project File ID | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjectFileStrings

> StringList getContinuousProjectFileStrings(projectId, documentId)

View strings their translations in a continuous document

View the strings from a document and their translations in your continuous translation project, for all target languages. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let documentId = 179469; // Number | Document ID/Name
apiInstance.getContinuousProjectFileStrings(projectId, documentId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **documentId** | **Number**| Document ID/Name | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinuousProjectStrings

> StringList getContinuousProjectStrings(projectId)

View strings and translations in continuous project

View the strings and their translations in your continuous translation project, for all target languages. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
apiInstance.getContinuousProjectStrings(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentTranslations

> StringList getDocumentTranslations(projectId, documentId)

View strings and translations of a document

View the strings and their translations in your translation project for the specified source document. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let documentId = 179469; // Number | Document ID
apiInstance.getDocumentTranslations(projectId, documentId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **documentId** | **Number**| Document ID | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentTranslationsForLanguage

> StringList getDocumentTranslationsForLanguage(projectId, documentId, language)

View strings and translations of a document for target language

View the strings and their translations in the given target language for the specified source document. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let documentId = 179469; // Number | Document ID
let language = "en-US"; // String | Target language code.
apiInstance.getDocumentTranslationsForLanguage(projectId, documentId, language, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **documentId** | **Number**| Document ID | 
 **language** | **String**| Target language code. | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectStrings

> StringList getProjectStrings(projectId)

View project strings and translations

View the strings and their translations in your translation project, for all target languages. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
apiInstance.getProjectStrings(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectStringsForLanguage

> StringList getProjectStringsForLanguage(projectId, language)

View strings and translations for target language

View the strings and their translations in your translation project for the specified target language. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let language = "en-US"; // String | Target language code
apiInstance.getProjectStringsForLanguage(projectId, language, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **language** | **String**| Target language code | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectTranslations

> StringList getProjectTranslations(projectId)

Deprecated. Use /projects/{projectId}/strings instead.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
apiInstance.getProjectTranslations(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectTranslationsForLanguage

> StringList getProjectTranslationsForLanguage(projectId, language)

Deprecated. use /projects/{projectId}/strings/{language} instead.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let language = "en-US"; // String | Target language code
apiInstance.getProjectTranslationsForLanguage(projectId, language, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **language** | **String**| Target language code | 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStrings

> ClientStrings getStrings(opts)

View account strings (translation memory)

Get a list of all strings and their translations under your account, from all projects. This is your MotaWord translation memory. If you have the related permission, this endpoint will also return strings from your company account.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let opts = {
  'sourceLanguage': "sourceLanguage_example", // String | Source Language Code
  'page': 0 // Number | Requested page
};
apiInstance.getStrings(opts, (error, data, response) => {
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
 **sourceLanguage** | **String**| Source Language Code | [optional] 
 **page** | **Number**| Requested page | [optional] [default to 0]

### Return type

[**ClientStrings**](ClientStrings.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTranslationCache

> ContinuousProjectCache getTranslationCache(projectId, opts)

View cached strings translations in continuous project

MotaWord caches your account intensively (and in a smart way) in real-time translation environments. This endpoint will return the currently cached strings and translations in your continuous translation project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let opts = {
  'flatten': true // Boolean | Flatten cache results and ignore document keys
};
apiInstance.getTranslationCache(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **flatten** | **Boolean**| Flatten cache results and ignore document keys | [optional] 

### Return type

[**ContinuousProjectCache**](ContinuousProjectCache.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packageProjectTranslationMemory

> AsyncOperationStatus packageProjectTranslationMemory(projectId, opts)

Download project translation memory

Package and download project translation memory in TMX format

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let opts = {
  'async': 0, // Number | If you want to package and download the translation memory synchronously, mark this parameter as '0'. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
  'format': "'tmx'" // String | Translation Memory file format
};
apiInstance.packageProjectTranslationMemory(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **async** | **Number**| If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call. | [optional] [default to 0]
 **format** | **String**| Translation Memory file format | [optional] [default to &#39;tmx&#39;]

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## packageProjectTranslationMemoryForLanguage

> AsyncOperationStatus packageProjectTranslationMemoryForLanguage(projectId, languageCode, opts)

Download language-specific project translation memory

Package and download project translation memory in TMX format for a specific target language.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let languageCode = "en-US"; // String | Language Code
let opts = {
  'async': 0, // Number | If you want to package and download the translation memory synchronously, mark this parameter as '0'. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
  'format': "'tmx'" // String | Translation Memory file format
};
apiInstance.packageProjectTranslationMemoryForLanguage(projectId, languageCode, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **languageCode** | **String**| Language Code | 
 **async** | **Number**| If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call. | [optional] [default to 0]
 **format** | **String**| Translation Memory file format | [optional] [default to &#39;tmx&#39;]

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## packageProjectTranslationMemoryForLanguageStatus

> AsyncOperationStatus packageProjectTranslationMemoryForLanguageStatus(projectId, languageCode, asyncRequestKey)

Check language-specific translation memory packaging status

Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let languageCode = "en-US"; // String | Language Code
let asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
apiInstance.packageProjectTranslationMemoryForLanguageStatus(projectId, languageCode, asyncRequestKey, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **languageCode** | **String**| Language Code | 
 **asyncRequestKey** | **String**| Async operation key | 

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packageProjectTranslationMemoryStatus

> AsyncOperationStatus packageProjectTranslationMemoryStatus(projectId, asyncRequestKey)

Check translation memory packaging status

Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
apiInstance.packageProjectTranslationMemoryStatus(projectId, asyncRequestKey, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **asyncRequestKey** | **String**| Async operation key | 

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packageUserTranslationMemory

> AsyncOperationStatus packageUserTranslationMemory(languageCode, opts)

Download account translation memory

Package and download account translation memory in TMX format. If you have the related permission, this will also download your company translation memory.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let languageCode = "en-US"; // String | Source Language Code
let opts = {
  'async': 0, // Number | If you want to package and download the translation memory synchronously, mark this parameter as '0'. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
  'email': 1 // Number | If you don't need us to email the TMX, set this to '0'. Default is 1.
};
apiInstance.packageUserTranslationMemory(languageCode, opts, (error, data, response) => {
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
 **languageCode** | **String**| Source Language Code | 
 **async** | **Number**| If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call. | [optional] [default to 0]
 **email** | **Number**| If you don&#39;t need us to email the TMX, set this to &#39;0&#39;. Default is 1. | [optional] [default to 1]

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## packageUserTranslationMemoryForLanguageStatus

> AsyncOperationStatus packageUserTranslationMemoryForLanguageStatus(languageCode, asyncRequestKey)

Check account translation memory packaging status

Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let languageCode = "en-US"; // String | Language Code
let asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
apiInstance.packageUserTranslationMemoryForLanguageStatus(languageCode, asyncRequestKey, (error, data, response) => {
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
 **languageCode** | **String**| Language Code | 
 **asyncRequestKey** | **String**| Async operation key | 

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postContinuousProjectFileStrings

> StringList postContinuousProjectFileStrings(projectId, opts)

Get a list of strings and its translations in the project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let opts = {
  'continuousProjectDocumentStringsBody': new MotaWordApi.ContinuousProjectDocumentStringsBody() // ContinuousProjectDocumentStringsBody | 
};
apiInstance.postContinuousProjectFileStrings(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **continuousProjectDocumentStringsBody** | [**ContinuousProjectDocumentStringsBody**](ContinuousProjectDocumentStringsBody.md)|  | [optional] 

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recacheTranslations

> OperationStatus recacheTranslations(projectId, opts)

Recache translations

Recache translations for the continuous project.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let projectId = 74; // Number | Project ID
let opts = {
  'locale': "locale_example", // String | Locale
  'fileId': 789 // Number | Continuous Project File ID
};
apiInstance.recacheTranslations(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project ID | 
 **locale** | **String**| Locale | [optional] 
 **fileId** | **Number**| Continuous Project File ID | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTranslationMemoryUnit

> OperationStatus updateTranslationMemoryUnit(opts)

Update string translation

Update the translation of a string from your account strings/translation memory.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.StringsApi();
let opts = {
  'translationMemoryUnit': new MotaWordApi.TranslationMemoryUnit() // TranslationMemoryUnit | 
};
apiInstance.updateTranslationMemoryUnit(opts, (error, data, response) => {
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
 **translationMemoryUnit** | [**TranslationMemoryUnit**](TranslationMemoryUnit.md)|  | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


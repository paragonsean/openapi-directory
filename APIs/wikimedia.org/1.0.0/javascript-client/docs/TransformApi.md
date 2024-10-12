# Wikimedia.TransformApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transformHtmlFromFromLangToToLangPost**](TransformApi.md#transformHtmlFromFromLangToToLangPost) | **POST** /transform/html/from/{from_lang}/to/{to_lang} | Machine-translate content
[**transformHtmlFromFromLangToToLangProviderPost**](TransformApi.md#transformHtmlFromFromLangToToLangProviderPost) | **POST** /transform/html/from/{from_lang}/to/{to_lang}/{provider} | Machine-translate content
[**transformListLanguagepairsGet**](TransformApi.md#transformListLanguagepairsGet) | **GET** /transform/list/languagepairs/ | Lists the language pairs supported by the back-end
[**transformListPairFromToGet**](TransformApi.md#transformListPairFromToGet) | **GET** /transform/list/pair/{from}/{to}/ | Lists the tools available for a language pair
[**transformListToolToolFromGet**](TransformApi.md#transformListToolToolFromGet) | **GET** /transform/list/tool/{tool}/{from} | Lists the tools and language pairs available for the given tool category
[**transformListToolToolFromToGet**](TransformApi.md#transformListToolToolFromToGet) | **GET** /transform/list/tool/{tool}/{from}/{to} | Lists the tools and language pairs available for the given tool category
[**transformListToolToolGet**](TransformApi.md#transformListToolToolGet) | **GET** /transform/list/tool/{tool} | Lists the tools and language pairs available for the given tool category
[**transformWordFromFromLangToToLangWordGet**](TransformApi.md#transformWordFromFromLangToToLangWordGet) | **GET** /transform/word/from/{from_lang}/to/{to_lang}/{word} | Fetch the dictionary meaning of a word
[**transformWordFromFromLangToToLangWordProviderGet**](TransformApi.md#transformWordFromFromLangToToLangWordProviderGet) | **GET** /transform/word/from/{from_lang}/to/{to_lang}/{word}/{provider} | Fetch the dictionary meaning of a word



## transformHtmlFromFromLangToToLangPost

> CxMt transformHtmlFromFromLangToToLangPost(fromLang, toLang, html)

Machine-translate content

Fetches the machine translation for the posted content from the source to the destination language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let fromLang = "fromLang_example"; // String | The source language code
let toLang = "toLang_example"; // String | The target language code
let html = "html_example"; // String | The HTML content to translate
apiInstance.transformHtmlFromFromLangToToLangPost(fromLang, toLang, html, (error, data, response) => {
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
 **fromLang** | **String**| The source language code | 
 **toLang** | **String**| The target language code | 
 **html** | **String**| The HTML content to translate | 

### Return type

[**CxMt**](CxMt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/problem+json


## transformHtmlFromFromLangToToLangProviderPost

> CxMt transformHtmlFromFromLangToToLangProviderPost(fromLang, toLang, provider, html)

Machine-translate content

Fetches the machine translation for the posted content from the source to the destination language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let fromLang = "fromLang_example"; // String | The source language code
let toLang = "toLang_example"; // String | The target language code
let provider = "provider_example"; // String | The machine translation provider id
let html = "html_example"; // String | The HTML content to translate
apiInstance.transformHtmlFromFromLangToToLangProviderPost(fromLang, toLang, provider, html, (error, data, response) => {
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
 **fromLang** | **String**| The source language code | 
 **toLang** | **String**| The target language code | 
 **provider** | **String**| The machine translation provider id | 
 **html** | **String**| The HTML content to translate | 

### Return type

[**CxMt**](CxMt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/problem+json


## transformListLanguagepairsGet

> CxLanguagepairs transformListLanguagepairsGet()

Lists the language pairs supported by the back-end

Fetches the list of language pairs the back-end service can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
apiInstance.transformListLanguagepairsGet((error, data, response) => {
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

[**CxLanguagepairs**](CxLanguagepairs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformListPairFromToGet

> CxListTools transformListPairFromToGet(from, to)

Lists the tools available for a language pair

Fetches the list of tools that are available for the given pair of languages.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let from = "from_example"; // String | The source language code
let to = "to_example"; // String | The target language code
apiInstance.transformListPairFromToGet(from, to, (error, data, response) => {
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
 **from** | **String**| The source language code | 
 **to** | **String**| The target language code | 

### Return type

[**CxListTools**](CxListTools.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## transformListToolToolFromGet

> Object transformListToolToolFromGet(tool, from)

Lists the tools and language pairs available for the given tool category

Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let tool = "tool_example"; // String | The tool category to list tools and language pairs for
let from = "from_example"; // String | The source language code
apiInstance.transformListToolToolFromGet(tool, from, (error, data, response) => {
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
 **tool** | **String**| The tool category to list tools and language pairs for | 
 **from** | **String**| The source language code | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## transformListToolToolFromToGet

> Object transformListToolToolFromToGet(tool, from, to)

Lists the tools and language pairs available for the given tool category

Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let tool = "tool_example"; // String | The tool category to list tools and language pairs for
let from = "from_example"; // String | The source language code
let to = "to_example"; // String | The target language code
apiInstance.transformListToolToolFromToGet(tool, from, to, (error, data, response) => {
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
 **tool** | **String**| The tool category to list tools and language pairs for | 
 **from** | **String**| The source language code | 
 **to** | **String**| The target language code | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## transformListToolToolGet

> Object transformListToolToolGet(tool)

Lists the tools and language pairs available for the given tool category

Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let tool = "tool_example"; // String | The tool category to list tools and language pairs for
apiInstance.transformListToolToolGet(tool, (error, data, response) => {
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
 **tool** | **String**| The tool category to list tools and language pairs for | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## transformWordFromFromLangToToLangWordGet

> CxDict transformWordFromFromLangToToLangWordGet(fromLang, toLang, word)

Fetch the dictionary meaning of a word

Fetches the dictionary meaning of a word from a language and displays it in the target language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let fromLang = "fromLang_example"; // String | The source language code
let toLang = "toLang_example"; // String | The target language code
let word = "word_example"; // String | The word to lookup
apiInstance.transformWordFromFromLangToToLangWordGet(fromLang, toLang, word, (error, data, response) => {
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
 **fromLang** | **String**| The source language code | 
 **toLang** | **String**| The target language code | 
 **word** | **String**| The word to lookup | 

### Return type

[**CxDict**](CxDict.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## transformWordFromFromLangToToLangWordProviderGet

> CxDict transformWordFromFromLangToToLangWordProviderGet(fromLang, toLang, word, provider)

Fetch the dictionary meaning of a word

Fetches the dictionary meaning of a word from a language and displays it in the target language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example

```javascript
import Wikimedia from 'wikimedia';

let apiInstance = new Wikimedia.TransformApi();
let fromLang = "fromLang_example"; // String | The source language code
let toLang = "toLang_example"; // String | The target language code
let word = "word_example"; // String | The word to lookup
let provider = "provider_example"; // String | The dictionary provider id
apiInstance.transformWordFromFromLangToToLangWordProviderGet(fromLang, toLang, word, provider, (error, data, response) => {
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
 **fromLang** | **String**| The source language code | 
 **toLang** | **String**| The target language code | 
 **word** | **String**| The word to lookup | 
 **provider** | **String**| The dictionary provider id | 

### Return type

[**CxDict**](CxDict.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


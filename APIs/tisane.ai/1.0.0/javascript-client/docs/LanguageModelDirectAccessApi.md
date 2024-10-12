# TisaneApiDocumentation.LanguageModelDirectAccessApi

All URIs are relative to *https://api.tisane.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFamilyDetails**](LanguageModelDirectAccessApi.md#getFamilyDetails) | **GET** /lm/family | Get family details
[**listFeatureValues**](LanguageModelDirectAccessApi.md#listFeatureValues) | **GET** /values | List feature values
[**listHypernyms**](LanguageModelDirectAccessApi.md#listHypernyms) | **GET** /hypernyms | List hypernyms
[**listHyponyms**](LanguageModelDirectAccessApi.md#listHyponyms) | **GET** /hyponyms | List hyponyms
[**listInflectedForms**](LanguageModelDirectAccessApi.md#listInflectedForms) | **GET** /inflections | List inflected forms
[**listWordSenses**](LanguageModelDirectAccessApi.md#listWordSenses) | **GET** /senses | List word senses



## getFamilyDetails

> GetFamilyDetails200Response getFamilyDetails(opts)

Get family details

Fetches and outputs metadata for a family from the Tisane language models.

### Example

```javascript
import TisaneApiDocumentation from 'tisane_api_documentation';

let apiInstance = new TisaneApiDocumentation.LanguageModelDirectAccessApi();
let opts = {
  'id': "{family_id}", // String | (Required) a numeric identifier of the family
  'ocpApimSubscriptionKey': "{{apiKey}}" // String | {{apiKeyDescription}}
};
apiInstance.getFamilyDetails(opts, (error, data, response) => {
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
 **id** | **String**| (Required) a numeric identifier of the family | [optional] 
 **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] 

### Return type

[**GetFamilyDetails200Response**](GetFamilyDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFeatureValues

> [String] listFeatureValues(opts)

List feature values

Lists feature values for a particular category of features. This allows obtaining all the values such as entity types, subtypes, abuse types and tags, and more.  Returns the values as a JSON array of strings.

### Example

```javascript
import TisaneApiDocumentation from 'tisane_api_documentation';

let apiInstance = new TisaneApiDocumentation.LanguageModelDirectAccessApi();
let opts = {
  'language': "{language_code}", // String | (Required) Language code
  'type': "{Grammar/Style/Semantics}", // String | (Required) Feature type
  'description': "{feature_list_name}", // String | (Required) Feature list name (localized)
  'ocpApimSubscriptionKey': "{{apiKey}}" // String | {{apiKeyDescription}}
};
apiInstance.listFeatureValues(opts, (error, data, response) => {
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
 **language** | **String**| (Required) Language code | [optional] 
 **type** | **String**| (Required) Feature type | [optional] 
 **description** | **String**| (Required) Feature list name (localized) | [optional] 
 **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHypernyms

> [[ListHypernyms200ResponseInnerInner]] listHypernyms(opts)

List hypernyms

Lists all hypernyms related to a family. A hypernym is a parent concent. E.g. \&quot;vehicle\&quot; is a hypernym of \&quot;truck\&quot;.

### Example

```javascript
import TisaneApiDocumentation from 'tisane_api_documentation';

let apiInstance = new TisaneApiDocumentation.LanguageModelDirectAccessApi();
let opts = {
  'family': "{family_id}", // String | (Required) a numeric identifier of the family
  'maxLevel': "{max_number_of_levels}", // String | (Required) maximum distance from the family
  'ocpApimSubscriptionKey': "{{apiKey}}" // String | {{apiKeyDescription}}
};
apiInstance.listHypernyms(opts, (error, data, response) => {
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
 **family** | **String**| (Required) a numeric identifier of the family | [optional] 
 **maxLevel** | **String**| (Required) maximum distance from the family | [optional] 
 **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] 

### Return type

**[[ListHypernyms200ResponseInnerInner]]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listHyponyms

> listHyponyms(opts)

List hyponyms

Lists all hyponyms related to a family. A hyponym is a child concent. E.g. \&quot;truck\&quot; is a hypernym of \&quot;vehicle\&quot;.

### Example

```javascript
import TisaneApiDocumentation from 'tisane_api_documentation';

let apiInstance = new TisaneApiDocumentation.LanguageModelDirectAccessApi();
let opts = {
  'family': "{family_id}", // String | (Required) a numeric identifier of the family
  'maxLevel': "{max_number_of_levels}", // String | (Required) maximum distance from the family
  'ocpApimSubscriptionKey': "{{apiKey}}" // String | {{apiKeyDescription}}
};
apiInstance.listHyponyms(opts, (error, data, response) => {
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
 **family** | **String**| (Required) a numeric identifier of the family | [optional] 
 **maxLevel** | **String**| (Required) maximum distance from the family | [optional] 
 **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## listInflectedForms

> [ListInflectedForms200ResponseInner] listInflectedForms(opts)

List inflected forms

List inflected forms

### Example

```javascript
import TisaneApiDocumentation from 'tisane_api_documentation';

let apiInstance = new TisaneApiDocumentation.LanguageModelDirectAccessApi();
let opts = {
  'language': "{language_code}", // String | (Required) The language code
  'lexeme': "{lexeme_id}", // String | (Required) The lexeme to inspect
  'family': "{family_id}", // String | (Required) The family to inspect
  'ocpApimSubscriptionKey': "{{apiKey}}" // String | {{apiKeyDescription}}
};
apiInstance.listInflectedForms(opts, (error, data, response) => {
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
 **language** | **String**| (Required) The language code | [optional] 
 **lexeme** | **String**| (Required) The lexeme to inspect | [optional] 
 **family** | **String**| (Required) The family to inspect | [optional] 
 **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] 

### Return type

[**[ListInflectedForms200ResponseInner]**](ListInflectedForms200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWordSenses

> [ListWordSenses200ResponseInner] listWordSenses(opts)

List word senses

Fetches and outputs all senses related to a word.

### Example

```javascript
import TisaneApiDocumentation from 'tisane_api_documentation';

let apiInstance = new TisaneApiDocumentation.LanguageModelDirectAccessApi();
let opts = {
  'language': "{language_code}", // String | (Required) a standard culture code (ISO-639 language code with an optional country extension)
  'word': "{word}", // String | (Required) the word to inspect
  'ocpApimSubscriptionKey': "{{apiKey}}" // String | {{apiKeyDescription}}
};
apiInstance.listWordSenses(opts, (error, data, response) => {
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
 **language** | **String**| (Required) a standard culture code (ISO-639 language code with an optional country extension) | [optional] 
 **word** | **String**| (Required) the word to inspect | [optional] 
 **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] 

### Return type

[**[ListWordSenses200ResponseInner]**](ListWordSenses200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


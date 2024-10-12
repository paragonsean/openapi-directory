# WordAssociationsApi.DefaultApi

All URIs are relative to *https://api.wordassociations.net/associations/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jsonSearchGet**](DefaultApi.md#jsonSearchGet) | **GET** /json/search | 
[**jsonSearchPost**](DefaultApi.md#jsonSearchPost) | **POST** /json/search | 



## jsonSearchGet

> Body jsonSearchGet(text, lang, opts)



Gets associations with the given word or phrase. 

### Example

```javascript
import WordAssociationsApi from 'word_associations_api';
let defaultClient = WordAssociationsApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';

let apiInstance = new WordAssociationsApi.DefaultApi();
let text = ["null"]; // [String] | Word or phrase to find associations with. Tip. You can use multiple parameters 'text' in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text. 
let lang = "lang_example"; // String | Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian; 
let opts = {
  'type': "'stimulus'", // String | Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word. 
  'limit': 50, // Number | Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive. 
  'pos': ["null"], // [String] | Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb 
  'indent': "'true'" // String | Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off; 
};
apiInstance.jsonSearchGet(text, lang, opts, (error, data, response) => {
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
 **text** | [**[String]**](String.md)| Word or phrase to find associations with. Tip. You can use multiple parameters &#39;text&#39; in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text.  | 
 **lang** | **String**| Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian;  | 
 **type** | **String**| Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word.  | [optional] [default to &#39;stimulus&#39;]
 **limit** | **Number**| Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive.  | [optional] [default to 50]
 **pos** | [**[String]**](String.md)| Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb  | [optional] 
 **indent** | **String**| Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off;  | [optional] [default to &#39;true&#39;]

### Return type

[**Body**](Body.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jsonSearchPost

> Body jsonSearchPost(text, lang, opts)



Gets associations with the given word or phrase. 

### Example

```javascript
import WordAssociationsApi from 'word_associations_api';
let defaultClient = WordAssociationsApi.ApiClient.instance;
// Configure API key authorization: internalApiKey
let internalApiKey = defaultClient.authentications['internalApiKey'];
internalApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//internalApiKey.apiKeyPrefix = 'Token';

let apiInstance = new WordAssociationsApi.DefaultApi();
let text = ["null"]; // [String] | Word or phrase to find associations with. Tip. You can use multiple parameters 'text' in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text. 
let lang = "lang_example"; // String | Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian; 
let opts = {
  'type': "'stimulus'", // String | Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word. 
  'limit': 50, // Number | Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive. 
  'pos': ["null"], // [String] | Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb 
  'indent': "'true'" // String | Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off; 
};
apiInstance.jsonSearchPost(text, lang, opts, (error, data, response) => {
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
 **text** | [**[String]**](String.md)| Word or phrase to find associations with. Tip. You can use multiple parameters &#39;text&#39; in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text.  | 
 **lang** | **String**| Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian;  | 
 **type** | **String**| Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word.  | [optional] [default to &#39;stimulus&#39;]
 **limit** | **Number**| Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive.  | [optional] [default to 50]
 **pos** | [**[String]**](String.md)| Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb  | [optional] 
 **indent** | **String**| Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off;  | [optional] [default to &#39;true&#39;]

### Return type

[**Body**](Body.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


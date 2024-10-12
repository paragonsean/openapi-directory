# Wordnik.WordsApi

All URIs are relative to *https://api.wordnik.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRandomWord**](WordsApi.md#getRandomWord) | **GET** /words.json/randomWord | Returns a single random WordObject
[**getRandomWords**](WordsApi.md#getRandomWords) | **GET** /words.json/randomWords | Returns an array of random WordObjects
[**getWordOfTheDay**](WordsApi.md#getWordOfTheDay) | **GET** /words.json/wordOfTheDay | Returns a specific WordOfTheDay
[**reverseDictionary**](WordsApi.md#reverseDictionary) | **GET** /words.json/reverseDictionary | Reverse dictionary search
[**searchWords**](WordsApi.md#searchWords) | **GET** /words.json/search/{query} | Searches words



## getRandomWord

> WordObject getRandomWord(opts)

Returns a single random WordObject

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordsApi();
let opts = {
  'hasDictionaryDef': "'true'", // String | Only return words with dictionary definitions
  'includePartOfSpeech': "includePartOfSpeech_example", // String | CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'excludePartOfSpeech': "excludePartOfSpeech_example", // String | CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'minCorpusCount': 0, // Number | Minimum corpus frequency for terms
  'maxCorpusCount': -1, // Number | Maximum corpus frequency for terms
  'minDictionaryCount': 1, // Number | Minimum dictionary count
  'maxDictionaryCount': -1, // Number | Maximum dictionary count
  'minLength': 5, // Number | Minimum word length
  'maxLength': -1 // Number | Maximum word length
};
apiInstance.getRandomWord(opts, (error, data, response) => {
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
 **hasDictionaryDef** | **String**| Only return words with dictionary definitions | [optional] [default to &#39;true&#39;]
 **includePartOfSpeech** | **String**| CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **excludePartOfSpeech** | **String**| CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **minCorpusCount** | **Number**| Minimum corpus frequency for terms | [optional] [default to 0]
 **maxCorpusCount** | **Number**| Maximum corpus frequency for terms | [optional] [default to -1]
 **minDictionaryCount** | **Number**| Minimum dictionary count | [optional] [default to 1]
 **maxDictionaryCount** | **Number**| Maximum dictionary count | [optional] [default to -1]
 **minLength** | **Number**| Minimum word length | [optional] [default to 5]
 **maxLength** | **Number**| Maximum word length | [optional] [default to -1]

### Return type

[**WordObject**](WordObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getRandomWords

> [WordObject] getRandomWords(opts)

Returns an array of random WordObjects

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordsApi();
let opts = {
  'hasDictionaryDef': "'true'", // String | Only return words with dictionary definitions
  'includePartOfSpeech': "includePartOfSpeech_example", // String | CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'excludePartOfSpeech': "excludePartOfSpeech_example", // String | CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'minCorpusCount': 0, // Number | Minimum corpus frequency for terms
  'maxCorpusCount': -1, // Number | Maximum corpus frequency for terms
  'minDictionaryCount': 1, // Number | Minimum dictionary count
  'maxDictionaryCount': -1, // Number | Maximum dictionary count
  'minLength': 5, // Number | Minimum word length
  'maxLength': -1, // Number | Maximum word length
  'sortBy': "sortBy_example", // String | Attribute to sort by
  'sortOrder': "sortOrder_example", // String | Sort direction
  'limit': 10 // Number | Maximum number of results to return
};
apiInstance.getRandomWords(opts, (error, data, response) => {
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
 **hasDictionaryDef** | **String**| Only return words with dictionary definitions | [optional] [default to &#39;true&#39;]
 **includePartOfSpeech** | **String**| CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **excludePartOfSpeech** | **String**| CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **minCorpusCount** | **Number**| Minimum corpus frequency for terms | [optional] [default to 0]
 **maxCorpusCount** | **Number**| Maximum corpus frequency for terms | [optional] [default to -1]
 **minDictionaryCount** | **Number**| Minimum dictionary count | [optional] [default to 1]
 **maxDictionaryCount** | **Number**| Maximum dictionary count | [optional] [default to -1]
 **minLength** | **Number**| Minimum word length | [optional] [default to 5]
 **maxLength** | **Number**| Maximum word length | [optional] [default to -1]
 **sortBy** | **String**| Attribute to sort by | [optional] 
 **sortOrder** | **String**| Sort direction | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 10]

### Return type

[**[WordObject]**](WordObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getWordOfTheDay

> WordOfTheDay getWordOfTheDay(opts)

Returns a specific WordOfTheDay

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordsApi();
let opts = {
  'date': "date_example" // String | Fetches by date in yyyy-MM-dd
};
apiInstance.getWordOfTheDay(opts, (error, data, response) => {
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
 **date** | **String**| Fetches by date in yyyy-MM-dd | [optional] 

### Return type

[**WordOfTheDay**](WordOfTheDay.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## reverseDictionary

> DefinitionSearchResults reverseDictionary(query, opts)

Reverse dictionary search

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordsApi();
let query = "query_example"; // String | Search term
let opts = {
  'findSenseForWord': "findSenseForWord_example", // String | Restricts words and finds closest sense
  'includeSourceDictionaries': "includeSourceDictionaries_example", // String | Only include these comma-delimited source dictionaries
  'excludeSourceDictionaries': "excludeSourceDictionaries_example", // String | Exclude these comma-delimited source dictionaries
  'includePartOfSpeech': "includePartOfSpeech_example", // String | Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'excludePartOfSpeech': "excludePartOfSpeech_example", // String | Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'minCorpusCount': 5, // Number | Minimum corpus frequency for terms
  'maxCorpusCount': -1, // Number | Maximum corpus frequency for terms
  'minLength': 1, // Number | Minimum word length
  'maxLength': -1, // Number | Maximum word length
  'expandTerms': "expandTerms_example", // String | Expand terms
  'includeTags': "'false'", // String | Return a closed set of XML tags in response
  'sortBy': "sortBy_example", // String | Attribute to sort by
  'sortOrder': "sortOrder_example", // String | Sort direction
  'skip': "'0'", // String | Results to skip
  'limit': 10 // Number | Maximum number of results to return
};
apiInstance.reverseDictionary(query, opts, (error, data, response) => {
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
 **query** | **String**| Search term | 
 **findSenseForWord** | **String**| Restricts words and finds closest sense | [optional] 
 **includeSourceDictionaries** | **String**| Only include these comma-delimited source dictionaries | [optional] 
 **excludeSourceDictionaries** | **String**| Exclude these comma-delimited source dictionaries | [optional] 
 **includePartOfSpeech** | **String**| Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **excludePartOfSpeech** | **String**| Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **minCorpusCount** | **Number**| Minimum corpus frequency for terms | [optional] [default to 5]
 **maxCorpusCount** | **Number**| Maximum corpus frequency for terms | [optional] [default to -1]
 **minLength** | **Number**| Minimum word length | [optional] [default to 1]
 **maxLength** | **Number**| Maximum word length | [optional] [default to -1]
 **expandTerms** | **String**| Expand terms | [optional] 
 **includeTags** | **String**| Return a closed set of XML tags in response | [optional] [default to &#39;false&#39;]
 **sortBy** | **String**| Attribute to sort by | [optional] 
 **sortOrder** | **String**| Sort direction | [optional] 
 **skip** | **String**| Results to skip | [optional] [default to &#39;0&#39;]
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 10]

### Return type

[**DefinitionSearchResults**](DefinitionSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## searchWords

> WordSearchResults searchWords(query, opts)

Searches words

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordsApi();
let query = "query_example"; // String | Search query
let opts = {
  'allowRegex': "'false'", // String | Search term is a Regular Expression
  'caseSensitive': "'true'", // String | Search case sensitive
  'includePartOfSpeech': "includePartOfSpeech_example", // String | Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'excludePartOfSpeech': "excludePartOfSpeech_example", // String | Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
  'minCorpusCount': 5, // Number | Minimum corpus frequency for terms
  'maxCorpusCount': -1, // Number | Maximum corpus frequency for terms
  'minDictionaryCount': 1, // Number | Minimum number of dictionary entries for words returned
  'maxDictionaryCount': -1, // Number | Maximum dictionary definition count
  'minLength': 1, // Number | Minimum word length
  'maxLength': -1, // Number | Maximum word length
  'skip': 0, // Number | Results to skip
  'limit': 10 // Number | Maximum number of results to return
};
apiInstance.searchWords(query, opts, (error, data, response) => {
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
 **query** | **String**| Search query | 
 **allowRegex** | **String**| Search term is a Regular Expression | [optional] [default to &#39;false&#39;]
 **caseSensitive** | **String**| Search case sensitive | [optional] [default to &#39;true&#39;]
 **includePartOfSpeech** | **String**| Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **excludePartOfSpeech** | **String**| Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] 
 **minCorpusCount** | **Number**| Minimum corpus frequency for terms | [optional] [default to 5]
 **maxCorpusCount** | **Number**| Maximum corpus frequency for terms | [optional] [default to -1]
 **minDictionaryCount** | **Number**| Minimum number of dictionary entries for words returned | [optional] [default to 1]
 **maxDictionaryCount** | **Number**| Maximum dictionary definition count | [optional] [default to -1]
 **minLength** | **Number**| Minimum word length | [optional] [default to 1]
 **maxLength** | **Number**| Maximum word length | [optional] [default to -1]
 **skip** | **Number**| Results to skip | [optional] [default to 0]
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 10]

### Return type

[**WordSearchResults**](WordSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


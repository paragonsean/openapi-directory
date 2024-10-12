# Wordnik.WordApi

All URIs are relative to *https://api.wordnik.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAudio**](WordApi.md#getAudio) | **GET** /word.json/{word}/audio | Fetches audio metadata for a word.
[**getDefinitions**](WordApi.md#getDefinitions) | **GET** /word.json/{word}/definitions | Return definitions for a word
[**getEtymologies**](WordApi.md#getEtymologies) | **GET** /word.json/{word}/etymologies | Fetches etymology data
[**getExamples**](WordApi.md#getExamples) | **GET** /word.json/{word}/examples | Returns examples for a word
[**getHyphenation**](WordApi.md#getHyphenation) | **GET** /word.json/{word}/hyphenation | Returns syllable information for a word
[**getPhrases**](WordApi.md#getPhrases) | **GET** /word.json/{word}/phrases | Fetches bi-gram phrases for a word
[**getRelatedWords**](WordApi.md#getRelatedWords) | **GET** /word.json/{word}/relatedWords | Given a word as a string, returns relationships from the Word Graph
[**getScrabbleScore**](WordApi.md#getScrabbleScore) | **GET** /word.json/{word}/scrabbleScore | Returns the Scrabble score for a word
[**getTextPronunciations**](WordApi.md#getTextPronunciations) | **GET** /word.json/{word}/pronunciations | Returns text pronunciations for a given word
[**getTopExample**](WordApi.md#getTopExample) | **GET** /word.json/{word}/topExample | Returns a top example for a word
[**getWordFrequency**](WordApi.md#getWordFrequency) | **GET** /word.json/{word}/frequency | Returns word usage over time



## getAudio

> [AudioFile] getAudio(word, opts)

Fetches audio metadata for a word.

The metadata includes a time-expiring fileUrl which allows reading the audio file directly from the API.  Currently only audio pronunciations from the American Heritage Dictionary in mp3 format are supported.

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to get audio for.
let opts = {
  'useCanonical': "'false'", // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
  'limit': 50 // Number | Maximum number of results to return
};
apiInstance.getAudio(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to get audio for. | 
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]

### Return type

[**[AudioFile]**](AudioFile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getDefinitions

> [Definition] getDefinitions(word, opts)

Return definitions for a word

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to return definitions for
let opts = {
  'limit': 200, // Number | Maximum number of results to return
  'partOfSpeech': "partOfSpeech_example", // String | CSV list of part-of-speech types
  'includeRelated': "'false'", // String | Return related words with definitions
  'sourceDictionaries': ["null"], // [String] | Source dictionary to return definitions from.  If 'all' is received, results are returned from all sources. If multiple values are received (e.g. 'century,wiktionary'), results are returned from the first specified dictionary that has definitions. If left blank, results are returned from the first dictionary that has definitions. By default, dictionaries are searched in this order: ahd-5, wiktionary, webster, century, wordnet
  'useCanonical': "'false'", // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
  'includeTags': "'false'" // String | Return a closed set of XML tags in response
};
apiInstance.getDefinitions(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to return definitions for | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 200]
 **partOfSpeech** | **String**| CSV list of part-of-speech types | [optional] 
 **includeRelated** | **String**| Return related words with definitions | [optional] [default to &#39;false&#39;]
 **sourceDictionaries** | [**[String]**](String.md)| Source dictionary to return definitions from.  If &#39;all&#39; is received, results are returned from all sources. If multiple values are received (e.g. &#39;century,wiktionary&#39;), results are returned from the first specified dictionary that has definitions. If left blank, results are returned from the first dictionary that has definitions. By default, dictionaries are searched in this order: ahd-5, wiktionary, webster, century, wordnet | [optional] 
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]
 **includeTags** | **String**| Return a closed set of XML tags in response | [optional] [default to &#39;false&#39;]

### Return type

[**[Definition]**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getEtymologies

> [String] getEtymologies(word, opts)

Fetches etymology data

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to return
let opts = {
  'useCanonical': "'false'" // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
};
apiInstance.getEtymologies(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to return | 
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getExamples

> ExampleSearchResults getExamples(word, opts)

Returns examples for a word

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to return examples for
let opts = {
  'includeDuplicates': "'false'", // String | Show duplicate examples from different sources
  'useCanonical': "'false'", // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
  'skip': 0, // Number | Results to skip
  'limit': 5 // Number | Maximum number of results to return
};
apiInstance.getExamples(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to return examples for | 
 **includeDuplicates** | **String**| Show duplicate examples from different sources | [optional] [default to &#39;false&#39;]
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]
 **skip** | **Number**| Results to skip | [optional] [default to 0]
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 5]

### Return type

[**ExampleSearchResults**](ExampleSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getHyphenation

> [Syllable] getHyphenation(word, opts)

Returns syllable information for a word

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to get syllables for
let opts = {
  'useCanonical': "'false'", // String | If true will try to return a correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
  'sourceDictionary': "sourceDictionary_example", // String | Get from a single dictionary. Valid options: ahd-5, century, wiktionary, webster, and wordnet.
  'limit': 50 // Number | Maximum number of results to return
};
apiInstance.getHyphenation(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to get syllables for | 
 **useCanonical** | **String**| If true will try to return a correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]
 **sourceDictionary** | **String**| Get from a single dictionary. Valid options: ahd-5, century, wiktionary, webster, and wordnet. | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]

### Return type

[**[Syllable]**](Syllable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPhrases

> [Bigram] getPhrases(word, opts)

Fetches bi-gram phrases for a word

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to fetch phrases for
let opts = {
  'limit': 5, // Number | Maximum number of results to return
  'wlmi': 0, // Number | Minimum WLMI for the phrase
  'useCanonical': "'false'" // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
};
apiInstance.getPhrases(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to fetch phrases for | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 5]
 **wlmi** | **Number**| Minimum WLMI for the phrase | [optional] [default to 0]
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]

### Return type

[**[Bigram]**](Bigram.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getRelatedWords

> [Related] getRelatedWords(word, opts)

Given a word as a string, returns relationships from the Word Graph

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to fetch relationships for
let opts = {
  'useCanonical': "'false'", // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
  'relationshipTypes': "relationshipTypes_example", // String | Limits the total results per type of relationship type
  'limitPerRelationshipType': 10 // Number | Restrict to the supplied relationship types
};
apiInstance.getRelatedWords(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to fetch relationships for | 
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]
 **relationshipTypes** | **String**| Limits the total results per type of relationship type | [optional] 
 **limitPerRelationshipType** | **Number**| Restrict to the supplied relationship types | [optional] [default to 10]

### Return type

[**[Related]**](Related.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getScrabbleScore

> Number getScrabbleScore(word)

Returns the Scrabble score for a word

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to get scrabble score for.
apiInstance.getScrabbleScore(word, (error, data, response) => {
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
 **word** | **String**| Word to get scrabble score for. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTextPronunciations

> [TextPron] getTextPronunciations(word, opts)

Returns text pronunciations for a given word

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to get pronunciations for
let opts = {
  'useCanonical': "'false'", // String | If true will try to return a correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
  'sourceDictionary': "sourceDictionary_example", // String | Get from a single dictionary
  'typeFormat': "typeFormat_example", // String | Text pronunciation type
  'limit': 50 // Number | Maximum number of results to return
};
apiInstance.getTextPronunciations(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to get pronunciations for | 
 **useCanonical** | **String**| If true will try to return a correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]
 **sourceDictionary** | **String**| Get from a single dictionary | [optional] 
 **typeFormat** | **String**| Text pronunciation type | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]

### Return type

[**[TextPron]**](TextPron.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTopExample

> Example getTopExample(word, opts)

Returns a top example for a word

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to fetch examples for
let opts = {
  'useCanonical': "'false'" // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
};
apiInstance.getTopExample(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to fetch examples for | 
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]

### Return type

[**Example**](Example.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getWordFrequency

> FrequencySummary getWordFrequency(word, opts)

Returns word usage over time

### Example

```javascript
import Wordnik from 'wordnik';

let apiInstance = new Wordnik.WordApi();
let word = "word_example"; // String | Word to return
let opts = {
  'useCanonical': "'false'", // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
  'startYear': 1800, // Number | Starting Year
  'endYear': 2012 // Number | Ending Year
};
apiInstance.getWordFrequency(word, opts, (error, data, response) => {
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
 **word** | **String**| Word to return | 
 **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to &#39;false&#39;]
 **startYear** | **Number**| Starting Year | [optional] [default to 1800]
 **endYear** | **Number**| Ending Year | [optional] [default to 2012]

### Return type

[**FrequencySummary**](FrequencySummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


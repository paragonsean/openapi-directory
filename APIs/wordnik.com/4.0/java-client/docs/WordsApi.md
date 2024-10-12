# WordsApi

All URIs are relative to *https://api.wordnik.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRandomWord**](WordsApi.md#getRandomWord) | **GET** /words.json/randomWord | Returns a single random WordObject |
| [**getRandomWords**](WordsApi.md#getRandomWords) | **GET** /words.json/randomWords | Returns an array of random WordObjects |
| [**getWordOfTheDay**](WordsApi.md#getWordOfTheDay) | **GET** /words.json/wordOfTheDay | Returns a specific WordOfTheDay |
| [**reverseDictionary**](WordsApi.md#reverseDictionary) | **GET** /words.json/reverseDictionary | Reverse dictionary search |
| [**searchWords**](WordsApi.md#searchWords) | **GET** /words.json/search/{query} | Searches words |


<a id="getRandomWord"></a>
# **getRandomWord**
> WordObject getRandomWord(hasDictionaryDef, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minDictionaryCount, maxDictionaryCount, minLength, maxLength)

Returns a single random WordObject

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordsApi apiInstance = new WordsApi(defaultClient);
    String hasDictionaryDef = "true"; // String | Only return words with dictionary definitions
    String includePartOfSpeech = "includePartOfSpeech_example"; // String | CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    String excludePartOfSpeech = "excludePartOfSpeech_example"; // String | CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    Integer minCorpusCount = 0; // Integer | Minimum corpus frequency for terms
    Integer maxCorpusCount = -1; // Integer | Maximum corpus frequency for terms
    Integer minDictionaryCount = 1; // Integer | Minimum dictionary count
    Integer maxDictionaryCount = -1; // Integer | Maximum dictionary count
    Integer minLength = 5; // Integer | Minimum word length
    Integer maxLength = -1; // Integer | Maximum word length
    try {
      WordObject result = apiInstance.getRandomWord(hasDictionaryDef, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minDictionaryCount, maxDictionaryCount, minLength, maxLength);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordsApi#getRandomWord");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **hasDictionaryDef** | **String**| Only return words with dictionary definitions | [optional] [default to true] |
| **includePartOfSpeech** | **String**| CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **excludePartOfSpeech** | **String**| CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **minCorpusCount** | **Integer**| Minimum corpus frequency for terms | [optional] [default to 0] |
| **maxCorpusCount** | **Integer**| Maximum corpus frequency for terms | [optional] [default to -1] |
| **minDictionaryCount** | **Integer**| Minimum dictionary count | [optional] [default to 1] |
| **maxDictionaryCount** | **Integer**| Maximum dictionary count | [optional] [default to -1] |
| **minLength** | **Integer**| Minimum word length | [optional] [default to 5] |
| **maxLength** | **Integer**| Maximum word length | [optional] [default to -1] |

### Return type

[**WordObject**](WordObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getRandomWords"></a>
# **getRandomWords**
> List&lt;WordObject&gt; getRandomWords(hasDictionaryDef, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minDictionaryCount, maxDictionaryCount, minLength, maxLength, sortBy, sortOrder, limit)

Returns an array of random WordObjects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordsApi apiInstance = new WordsApi(defaultClient);
    String hasDictionaryDef = "true"; // String | Only return words with dictionary definitions
    String includePartOfSpeech = "includePartOfSpeech_example"; // String | CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    String excludePartOfSpeech = "excludePartOfSpeech_example"; // String | CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    Integer minCorpusCount = 0; // Integer | Minimum corpus frequency for terms
    Integer maxCorpusCount = -1; // Integer | Maximum corpus frequency for terms
    Integer minDictionaryCount = 1; // Integer | Minimum dictionary count
    Integer maxDictionaryCount = -1; // Integer | Maximum dictionary count
    Integer minLength = 5; // Integer | Minimum word length
    Integer maxLength = -1; // Integer | Maximum word length
    String sortBy = "alpha"; // String | Attribute to sort by
    String sortOrder = "asc"; // String | Sort direction
    Integer limit = 10; // Integer | Maximum number of results to return
    try {
      List<WordObject> result = apiInstance.getRandomWords(hasDictionaryDef, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minDictionaryCount, maxDictionaryCount, minLength, maxLength, sortBy, sortOrder, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordsApi#getRandomWords");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **hasDictionaryDef** | **String**| Only return words with dictionary definitions | [optional] [default to true] |
| **includePartOfSpeech** | **String**| CSV part-of-speech values to include (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **excludePartOfSpeech** | **String**| CSV part-of-speech values to exclude (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **minCorpusCount** | **Integer**| Minimum corpus frequency for terms | [optional] [default to 0] |
| **maxCorpusCount** | **Integer**| Maximum corpus frequency for terms | [optional] [default to -1] |
| **minDictionaryCount** | **Integer**| Minimum dictionary count | [optional] [default to 1] |
| **maxDictionaryCount** | **Integer**| Maximum dictionary count | [optional] [default to -1] |
| **minLength** | **Integer**| Minimum word length | [optional] [default to 5] |
| **maxLength** | **Integer**| Maximum word length | [optional] [default to -1] |
| **sortBy** | **String**| Attribute to sort by | [optional] [enum: alpha, count] |
| **sortOrder** | **String**| Sort direction | [optional] [enum: asc, desc] |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 10] |

### Return type

[**List&lt;WordObject&gt;**](WordObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getWordOfTheDay"></a>
# **getWordOfTheDay**
> WordOfTheDay getWordOfTheDay(date)

Returns a specific WordOfTheDay

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordsApi apiInstance = new WordsApi(defaultClient);
    String date = "date_example"; // String | Fetches by date in yyyy-MM-dd
    try {
      WordOfTheDay result = apiInstance.getWordOfTheDay(date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordsApi#getWordOfTheDay");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **date** | **String**| Fetches by date in yyyy-MM-dd | [optional] |

### Return type

[**WordOfTheDay**](WordOfTheDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="reverseDictionary"></a>
# **reverseDictionary**
> DefinitionSearchResults reverseDictionary(query, findSenseForWord, includeSourceDictionaries, excludeSourceDictionaries, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minLength, maxLength, expandTerms, includeTags, sortBy, sortOrder, skip, limit)

Reverse dictionary search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordsApi apiInstance = new WordsApi(defaultClient);
    String query = "query_example"; // String | Search term
    String findSenseForWord = "findSenseForWord_example"; // String | Restricts words and finds closest sense
    String includeSourceDictionaries = "ahd-5"; // String | Only include these comma-delimited source dictionaries
    String excludeSourceDictionaries = "ahd-5"; // String | Exclude these comma-delimited source dictionaries
    String includePartOfSpeech = "includePartOfSpeech_example"; // String | Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    String excludePartOfSpeech = "excludePartOfSpeech_example"; // String | Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    Integer minCorpusCount = 5; // Integer | Minimum corpus frequency for terms
    Integer maxCorpusCount = -1; // Integer | Maximum corpus frequency for terms
    Integer minLength = 1; // Integer | Minimum word length
    Integer maxLength = -1; // Integer | Maximum word length
    String expandTerms = "expandTerms_example"; // String | Expand terms
    String includeTags = "false"; // String | Return a closed set of XML tags in response
    String sortBy = "alpha"; // String | Attribute to sort by
    String sortOrder = "asc"; // String | Sort direction
    String skip = "0"; // String | Results to skip
    Integer limit = 10; // Integer | Maximum number of results to return
    try {
      DefinitionSearchResults result = apiInstance.reverseDictionary(query, findSenseForWord, includeSourceDictionaries, excludeSourceDictionaries, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minLength, maxLength, expandTerms, includeTags, sortBy, sortOrder, skip, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordsApi#reverseDictionary");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| Search term | |
| **findSenseForWord** | **String**| Restricts words and finds closest sense | [optional] |
| **includeSourceDictionaries** | **String**| Only include these comma-delimited source dictionaries | [optional] [enum: ahd-5, century, cmu, macmillan, wiktionary, webster, wordnet] |
| **excludeSourceDictionaries** | **String**| Exclude these comma-delimited source dictionaries | [optional] [enum: ahd-5, century, cmu, macmillan, wiktionary, webster, wordnet] |
| **includePartOfSpeech** | **String**| Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **excludePartOfSpeech** | **String**| Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **minCorpusCount** | **Integer**| Minimum corpus frequency for terms | [optional] [default to 5] |
| **maxCorpusCount** | **Integer**| Maximum corpus frequency for terms | [optional] [default to -1] |
| **minLength** | **Integer**| Minimum word length | [optional] [default to 1] |
| **maxLength** | **Integer**| Maximum word length | [optional] [default to -1] |
| **expandTerms** | **String**| Expand terms | [optional] |
| **includeTags** | **String**| Return a closed set of XML tags in response | [optional] [default to false] [enum: false, true] |
| **sortBy** | **String**| Attribute to sort by | [optional] [enum: alpha, count] |
| **sortOrder** | **String**| Sort direction | [optional] [enum: asc, desc] |
| **skip** | **String**| Results to skip | [optional] [default to 0] |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 10] |

### Return type

[**DefinitionSearchResults**](DefinitionSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="searchWords"></a>
# **searchWords**
> WordSearchResults searchWords(query, allowRegex, caseSensitive, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minDictionaryCount, maxDictionaryCount, minLength, maxLength, skip, limit)

Searches words

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordsApi apiInstance = new WordsApi(defaultClient);
    String query = "query_example"; // String | Search query
    String allowRegex = "false"; // String | Search term is a Regular Expression
    String caseSensitive = "true"; // String | Search case sensitive
    String includePartOfSpeech = "includePartOfSpeech_example"; // String | Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    String excludePartOfSpeech = "excludePartOfSpeech_example"; // String | Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive)
    Integer minCorpusCount = 5; // Integer | Minimum corpus frequency for terms
    Integer maxCorpusCount = -1; // Integer | Maximum corpus frequency for terms
    Integer minDictionaryCount = 1; // Integer | Minimum number of dictionary entries for words returned
    Integer maxDictionaryCount = -1; // Integer | Maximum dictionary definition count
    Integer minLength = 1; // Integer | Minimum word length
    Integer maxLength = -1; // Integer | Maximum word length
    Integer skip = 0; // Integer | Results to skip
    Integer limit = 10; // Integer | Maximum number of results to return
    try {
      WordSearchResults result = apiInstance.searchWords(query, allowRegex, caseSensitive, includePartOfSpeech, excludePartOfSpeech, minCorpusCount, maxCorpusCount, minDictionaryCount, maxDictionaryCount, minLength, maxLength, skip, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordsApi#searchWords");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| Search query | |
| **allowRegex** | **String**| Search term is a Regular Expression | [optional] [default to false] |
| **caseSensitive** | **String**| Search case sensitive | [optional] [default to true] |
| **includePartOfSpeech** | **String**| Only include these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **excludePartOfSpeech** | **String**| Exclude these comma-delimited parts of speech (allowable values are noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive) | [optional] |
| **minCorpusCount** | **Integer**| Minimum corpus frequency for terms | [optional] [default to 5] |
| **maxCorpusCount** | **Integer**| Maximum corpus frequency for terms | [optional] [default to -1] |
| **minDictionaryCount** | **Integer**| Minimum number of dictionary entries for words returned | [optional] [default to 1] |
| **maxDictionaryCount** | **Integer**| Maximum dictionary definition count | [optional] [default to -1] |
| **minLength** | **Integer**| Minimum word length | [optional] [default to 1] |
| **maxLength** | **Integer**| Maximum word length | [optional] [default to -1] |
| **skip** | **Integer**| Results to skip | [optional] [default to 0] |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 10] |

### Return type

[**WordSearchResults**](WordSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |


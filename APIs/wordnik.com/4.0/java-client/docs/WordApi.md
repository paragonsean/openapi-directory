# WordApi

All URIs are relative to *https://api.wordnik.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAudio**](WordApi.md#getAudio) | **GET** /word.json/{word}/audio | Fetches audio metadata for a word. |
| [**getDefinitions**](WordApi.md#getDefinitions) | **GET** /word.json/{word}/definitions | Return definitions for a word |
| [**getEtymologies**](WordApi.md#getEtymologies) | **GET** /word.json/{word}/etymologies | Fetches etymology data |
| [**getExamples**](WordApi.md#getExamples) | **GET** /word.json/{word}/examples | Returns examples for a word |
| [**getHyphenation**](WordApi.md#getHyphenation) | **GET** /word.json/{word}/hyphenation | Returns syllable information for a word |
| [**getPhrases**](WordApi.md#getPhrases) | **GET** /word.json/{word}/phrases | Fetches bi-gram phrases for a word |
| [**getRelatedWords**](WordApi.md#getRelatedWords) | **GET** /word.json/{word}/relatedWords | Given a word as a string, returns relationships from the Word Graph |
| [**getScrabbleScore**](WordApi.md#getScrabbleScore) | **GET** /word.json/{word}/scrabbleScore | Returns the Scrabble score for a word |
| [**getTextPronunciations**](WordApi.md#getTextPronunciations) | **GET** /word.json/{word}/pronunciations | Returns text pronunciations for a given word |
| [**getTopExample**](WordApi.md#getTopExample) | **GET** /word.json/{word}/topExample | Returns a top example for a word |
| [**getWordFrequency**](WordApi.md#getWordFrequency) | **GET** /word.json/{word}/frequency | Returns word usage over time |


<a id="getAudio"></a>
# **getAudio**
> List&lt;AudioFile&gt; getAudio(word, useCanonical, limit)

Fetches audio metadata for a word.

The metadata includes a time-expiring fileUrl which allows reading the audio file directly from the API.  Currently only audio pronunciations from the American Heritage Dictionary in mp3 format are supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to get audio for.
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    Integer limit = 50; // Integer | Maximum number of results to return
    try {
      List<AudioFile> result = apiInstance.getAudio(word, useCanonical, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getAudio");
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
| **word** | **String**| Word to get audio for. | |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 50] |

### Return type

[**List&lt;AudioFile&gt;**](AudioFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getDefinitions"></a>
# **getDefinitions**
> List&lt;Definition&gt; getDefinitions(word, limit, partOfSpeech, includeRelated, sourceDictionaries, useCanonical, includeTags)

Return definitions for a word

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to return definitions for
    Integer limit = 200; // Integer | Maximum number of results to return
    String partOfSpeech = "noun"; // String | CSV list of part-of-speech types
    String includeRelated = "false"; // String | Return related words with definitions
    List<String> sourceDictionaries = Arrays.asList(); // List<String> | Source dictionary to return definitions from.  If 'all' is received, results are returned from all sources. If multiple values are received (e.g. 'century,wiktionary'), results are returned from the first specified dictionary that has definitions. If left blank, results are returned from the first dictionary that has definitions. By default, dictionaries are searched in this order: ahd-5, wiktionary, webster, century, wordnet
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    String includeTags = "false"; // String | Return a closed set of XML tags in response
    try {
      List<Definition> result = apiInstance.getDefinitions(word, limit, partOfSpeech, includeRelated, sourceDictionaries, useCanonical, includeTags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getDefinitions");
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
| **word** | **String**| Word to return definitions for | |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 200] |
| **partOfSpeech** | **String**| CSV list of part-of-speech types | [optional] [enum: noun, adjective, verb, adverb, interjection, pronoun, preposition, abbreviation, affix, article, auxiliary-verb, conjunction, definite-article, family-name, given-name, idiom, imperative, noun-plural, noun-posessive, past-participle, phrasal-prefix, proper-noun, proper-noun-plural, proper-noun-posessive, suffix, verb-intransitive, verb-transitive] |
| **includeRelated** | **String**| Return related words with definitions | [optional] [default to false] |
| **sourceDictionaries** | [**List&lt;String&gt;**](String.md)| Source dictionary to return definitions from.  If &#39;all&#39; is received, results are returned from all sources. If multiple values are received (e.g. &#39;century,wiktionary&#39;), results are returned from the first specified dictionary that has definitions. If left blank, results are returned from the first dictionary that has definitions. By default, dictionaries are searched in this order: ahd-5, wiktionary, webster, century, wordnet | [optional] [enum: all, ahd-5, century, wiktionary, webster, wordnet] |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |
| **includeTags** | **String**| Return a closed set of XML tags in response | [optional] [default to false] [enum: false, true] |

### Return type

[**List&lt;Definition&gt;**](Definition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getEtymologies"></a>
# **getEtymologies**
> List&lt;String&gt; getEtymologies(word, useCanonical)

Fetches etymology data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to return
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    try {
      List<String> result = apiInstance.getEtymologies(word, useCanonical);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getEtymologies");
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
| **word** | **String**| Word to return | |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getExamples"></a>
# **getExamples**
> ExampleSearchResults getExamples(word, includeDuplicates, useCanonical, skip, limit)

Returns examples for a word

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to return examples for
    String includeDuplicates = "false"; // String | Show duplicate examples from different sources
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    Integer skip = 0; // Integer | Results to skip
    Integer limit = 5; // Integer | Maximum number of results to return
    try {
      ExampleSearchResults result = apiInstance.getExamples(word, includeDuplicates, useCanonical, skip, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getExamples");
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
| **word** | **String**| Word to return examples for | |
| **includeDuplicates** | **String**| Show duplicate examples from different sources | [optional] [default to false] [enum: false, true] |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |
| **skip** | **Integer**| Results to skip | [optional] [default to 0] |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 5] |

### Return type

[**ExampleSearchResults**](ExampleSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getHyphenation"></a>
# **getHyphenation**
> List&lt;Syllable&gt; getHyphenation(word, useCanonical, sourceDictionary, limit)

Returns syllable information for a word

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to get syllables for
    String useCanonical = "false"; // String | If true will try to return a correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    String sourceDictionary = "ahd-5"; // String | Get from a single dictionary. Valid options: ahd-5, century, wiktionary, webster, and wordnet.
    Integer limit = 50; // Integer | Maximum number of results to return
    try {
      List<Syllable> result = apiInstance.getHyphenation(word, useCanonical, sourceDictionary, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getHyphenation");
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
| **word** | **String**| Word to get syllables for | |
| **useCanonical** | **String**| If true will try to return a correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |
| **sourceDictionary** | **String**| Get from a single dictionary. Valid options: ahd-5, century, wiktionary, webster, and wordnet. | [optional] [enum: ahd-5, century, wiktionary, webster, wordnet] |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 50] |

### Return type

[**List&lt;Syllable&gt;**](Syllable.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getPhrases"></a>
# **getPhrases**
> List&lt;Bigram&gt; getPhrases(word, limit, wlmi, useCanonical)

Fetches bi-gram phrases for a word

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to fetch phrases for
    Integer limit = 5; // Integer | Maximum number of results to return
    Integer wlmi = 0; // Integer | Minimum WLMI for the phrase
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    try {
      List<Bigram> result = apiInstance.getPhrases(word, limit, wlmi, useCanonical);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getPhrases");
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
| **word** | **String**| Word to fetch phrases for | |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 5] |
| **wlmi** | **Integer**| Minimum WLMI for the phrase | [optional] [default to 0] |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |

### Return type

[**List&lt;Bigram&gt;**](Bigram.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getRelatedWords"></a>
# **getRelatedWords**
> List&lt;Related&gt; getRelatedWords(word, useCanonical, relationshipTypes, limitPerRelationshipType)

Given a word as a string, returns relationships from the Word Graph

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to fetch relationships for
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    String relationshipTypes = "synonym"; // String | Limits the total results per type of relationship type
    Integer limitPerRelationshipType = 10; // Integer | Restrict to the supplied relationship types
    try {
      List<Related> result = apiInstance.getRelatedWords(word, useCanonical, relationshipTypes, limitPerRelationshipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getRelatedWords");
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
| **word** | **String**| Word to fetch relationships for | |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |
| **relationshipTypes** | **String**| Limits the total results per type of relationship type | [optional] [enum: synonym, antonym, variant, equivalent, cross-reference, related-word, rhyme, form, etymologically-related-term, hypernym, hyponym, inflected-form, primary, same-context, verb-form, verb-stem, has_topic] |
| **limitPerRelationshipType** | **Integer**| Restrict to the supplied relationship types | [optional] [default to 10] |

### Return type

[**List&lt;Related&gt;**](Related.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getScrabbleScore"></a>
# **getScrabbleScore**
> Long getScrabbleScore(word)

Returns the Scrabble score for a word

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to get scrabble score for.
    try {
      Long result = apiInstance.getScrabbleScore(word);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getScrabbleScore");
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
| **word** | **String**| Word to get scrabble score for. | |

### Return type

**Long**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getTextPronunciations"></a>
# **getTextPronunciations**
> List&lt;TextPron&gt; getTextPronunciations(word, useCanonical, sourceDictionary, typeFormat, limit)

Returns text pronunciations for a given word

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to get pronunciations for
    String useCanonical = "false"; // String | If true will try to return a correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    String sourceDictionary = "ahd-5"; // String | Get from a single dictionary
    String typeFormat = "ahd-5"; // String | Text pronunciation type
    Integer limit = 50; // Integer | Maximum number of results to return
    try {
      List<TextPron> result = apiInstance.getTextPronunciations(word, useCanonical, sourceDictionary, typeFormat, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getTextPronunciations");
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
| **word** | **String**| Word to get pronunciations for | |
| **useCanonical** | **String**| If true will try to return a correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |
| **sourceDictionary** | **String**| Get from a single dictionary | [optional] [enum: ahd-5, century, cmu, macmillan, wiktionary, webster, wordnet] |
| **typeFormat** | **String**| Text pronunciation type | [optional] [enum: ahd-5, arpabet, gcide-diacritical, IPA] |
| **limit** | **Integer**| Maximum number of results to return | [optional] [default to 50] |

### Return type

[**List&lt;TextPron&gt;**](TextPron.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getTopExample"></a>
# **getTopExample**
> Example getTopExample(word, useCanonical)

Returns a top example for a word

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to fetch examples for
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    try {
      Example result = apiInstance.getTopExample(word, useCanonical);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getTopExample");
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
| **word** | **String**| Word to fetch examples for | |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |

### Return type

[**Example**](Example.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="getWordFrequency"></a>
# **getWordFrequency**
> FrequencySummary getWordFrequency(word, useCanonical, startYear, endYear)

Returns word usage over time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordnik.com/v4");

    WordApi apiInstance = new WordApi(defaultClient);
    String word = "word_example"; // String | Word to return
    String useCanonical = "false"; // String | If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested.
    Integer startYear = 1800; // Integer | Starting Year
    Integer endYear = 2012; // Integer | Ending Year
    try {
      FrequencySummary result = apiInstance.getWordFrequency(word, useCanonical, startYear, endYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WordApi#getWordFrequency");
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
| **word** | **String**| Word to return | |
| **useCanonical** | **String**| If true will try to return the correct word root (&#39;cats&#39; -&gt; &#39;cat&#39;). If false returns exactly what was requested. | [optional] [default to false] [enum: false, true] |
| **startYear** | **Integer**| Starting Year | [optional] [default to 1800] |
| **endYear** | **Integer**| Ending Year | [optional] [default to 2012] |

### Return type

[**FrequencySummary**](FrequencySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |


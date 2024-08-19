# DefaultApi

All URIs are relative to *https://api.languagetoolplus.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkPost**](DefaultApi.md#checkPost) | **POST** /check | Check a text |
| [**languagesGet**](DefaultApi.md#languagesGet) | **GET** /languages | Get a list of supported languages. |
| [**wordsAddPost**](DefaultApi.md#wordsAddPost) | **POST** /words/add | Add word to a dictionary |
| [**wordsDeletePost**](DefaultApi.md#wordsDeletePost) | **POST** /words/delete | Remove word from a dictionary |
| [**wordsGet**](DefaultApi.md#wordsGet) | **GET** /words | List words in dictionaries |


<a id="checkPost"></a>
# **checkPost**
> CheckPost200Response checkPost(language, text, data, username, apiKey, dicts, motherTongue, preferredVariants, enabledRules, disabledRules, enabledCategories, disabledCategories, enabledOnly, level)

Check a text

The main feature - check a text with LanguageTool for possible style and grammar issues.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.languagetoolplus.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String language = "language_example"; // String | A language code like `en-US`, `de-DE`, `fr`, or `auto` to guess the language automatically (see `preferredVariants` below). For languages with variants (English, German, Portuguese) spell checking will only be activated when you specify the variant, e.g. `en-GB` instead of just `en`.
    String text = "text_example"; // String | The text to be checked. This or 'data' is required.
    String data = "data_example"; // String | The text to be checked, given as a JSON document that specifies what's text and what's markup. This or 'text' is required. Markup will be ignored when looking for errors. Example text: <pre>A &lt;b>test&lt;/b></pre>JSON for the example text: <pre>{\\\"annotation\\\":[  {\\\"text\\\": \\\"A \\\"},  {\\\"markup\\\": \\\"&lt;b>\\\"},  {\\\"text\\\": \\\"test\\\"},  {\\\"markup\\\": \\\"&lt;/b>\\\"} ]}</pre> <p>If you have markup that should be interpreted as whitespace, like <tt>&lt;p&gt;</tt> in HTML, you can have it interpreted like this: <pre>{\\\"markup\\\": \\\"&lt;p&gt;\\\", \\\"interpretAs\\\": \\\"\\\\n\\\\n\\\"}</pre><p>The 'data' feature is not limited to HTML or XML, it can be used for any kind of markup. Entities will need to be expanded in this input.
    String username = "username_example"; // String | Set to get Premium API access: Your username/email as used to log in at languagetool.org.
    String apiKey = "apiKey_example"; // String | Set to get Premium API access: <a target='_blank' href='https://languagetool.org/editor/settings/access-tokens'>your API key</a>
    String dicts = "dicts_example"; // String | Comma-separated list of dictionaries to include words from; uses special default dictionary if this is unset
    String motherTongue = "motherTongue_example"; // String | A language code of the user's native language, enabling false friends checks for some language pairs.
    String preferredVariants = "preferredVariants_example"; // String | Comma-separated list of preferred language variants. The language detector used with `language=auto` can detect e.g. English, but it cannot decide whether British English or American English is used. Thus this parameter can be used to specify the preferred variants like `en-GB` and `de-AT`. Only available with `language=auto`. You should set variants for at least German and English, as otherwise the spell checking will not work for those, as no spelling dictionary can be selected for just `en` or `de`.
    String enabledRules = "enabledRules_example"; // String | IDs of rules to be enabled, comma-separated
    String disabledRules = "disabledRules_example"; // String | IDs of rules to be disabled, comma-separated
    String enabledCategories = "enabledCategories_example"; // String | IDs of categories to be enabled, comma-separated
    String disabledCategories = "disabledCategories_example"; // String | IDs of categories to be disabled, comma-separated
    Boolean enabledOnly = false; // Boolean | If true, only the rules and categories whose IDs are specified with `enabledRules` or `enabledCategories` are enabled.
    String level = "default"; // String | If set to `picky`, additional rules will be activated, i.e. rules that you might only find useful when checking formal text.
    try {
      CheckPost200Response result = apiInstance.checkPost(language, text, data, username, apiKey, dicts, motherTongue, preferredVariants, enabledRules, disabledRules, enabledCategories, disabledCategories, enabledOnly, level);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#checkPost");
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
| **language** | **String**| A language code like &#x60;en-US&#x60;, &#x60;de-DE&#x60;, &#x60;fr&#x60;, or &#x60;auto&#x60; to guess the language automatically (see &#x60;preferredVariants&#x60; below). For languages with variants (English, German, Portuguese) spell checking will only be activated when you specify the variant, e.g. &#x60;en-GB&#x60; instead of just &#x60;en&#x60;. | |
| **text** | **String**| The text to be checked. This or &#39;data&#39; is required. | [optional] |
| **data** | **String**| The text to be checked, given as a JSON document that specifies what&#39;s text and what&#39;s markup. This or &#39;text&#39; is required. Markup will be ignored when looking for errors. Example text: &lt;pre&gt;A &amp;lt;b&gt;test&amp;lt;/b&gt;&lt;/pre&gt;JSON for the example text: &lt;pre&gt;{\\\&quot;annotation\\\&quot;:[  {\\\&quot;text\\\&quot;: \\\&quot;A \\\&quot;},  {\\\&quot;markup\\\&quot;: \\\&quot;&amp;lt;b&gt;\\\&quot;},  {\\\&quot;text\\\&quot;: \\\&quot;test\\\&quot;},  {\\\&quot;markup\\\&quot;: \\\&quot;&amp;lt;/b&gt;\\\&quot;} ]}&lt;/pre&gt; &lt;p&gt;If you have markup that should be interpreted as whitespace, like &lt;tt&gt;&amp;lt;p&amp;gt;&lt;/tt&gt; in HTML, you can have it interpreted like this: &lt;pre&gt;{\\\&quot;markup\\\&quot;: \\\&quot;&amp;lt;p&amp;gt;\\\&quot;, \\\&quot;interpretAs\\\&quot;: \\\&quot;\\\\n\\\\n\\\&quot;}&lt;/pre&gt;&lt;p&gt;The &#39;data&#39; feature is not limited to HTML or XML, it can be used for any kind of markup. Entities will need to be expanded in this input. | [optional] |
| **username** | **String**| Set to get Premium API access: Your username/email as used to log in at languagetool.org. | [optional] |
| **apiKey** | **String**| Set to get Premium API access: &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;your API key&lt;/a&gt; | [optional] |
| **dicts** | **String**| Comma-separated list of dictionaries to include words from; uses special default dictionary if this is unset | [optional] |
| **motherTongue** | **String**| A language code of the user&#39;s native language, enabling false friends checks for some language pairs. | [optional] |
| **preferredVariants** | **String**| Comma-separated list of preferred language variants. The language detector used with &#x60;language&#x3D;auto&#x60; can detect e.g. English, but it cannot decide whether British English or American English is used. Thus this parameter can be used to specify the preferred variants like &#x60;en-GB&#x60; and &#x60;de-AT&#x60;. Only available with &#x60;language&#x3D;auto&#x60;. You should set variants for at least German and English, as otherwise the spell checking will not work for those, as no spelling dictionary can be selected for just &#x60;en&#x60; or &#x60;de&#x60;. | [optional] |
| **enabledRules** | **String**| IDs of rules to be enabled, comma-separated | [optional] |
| **disabledRules** | **String**| IDs of rules to be disabled, comma-separated | [optional] |
| **enabledCategories** | **String**| IDs of categories to be enabled, comma-separated | [optional] |
| **disabledCategories** | **String**| IDs of categories to be disabled, comma-separated | [optional] |
| **enabledOnly** | **Boolean**| If true, only the rules and categories whose IDs are specified with &#x60;enabledRules&#x60; or &#x60;enabledCategories&#x60; are enabled. | [optional] [default to false] |
| **level** | **String**| If set to &#x60;picky&#x60;, additional rules will be activated, i.e. rules that you might only find useful when checking formal text. | [optional] [enum: default, picky] |

### Return type

[**CheckPost200Response**](CheckPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the result of checking the text |  -  |

<a id="languagesGet"></a>
# **languagesGet**
> List&lt;LanguagesGet200ResponseInner&gt; languagesGet()

Get a list of supported languages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.languagetoolplus.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<LanguagesGet200ResponseInner> result = apiInstance.languagesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#languagesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;LanguagesGet200ResponseInner&gt;**](LanguagesGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of language objects. |  -  |

<a id="wordsAddPost"></a>
# **wordsAddPost**
> WordsAddPost200Response wordsAddPost(word, username, apiKey, dict)

Add word to a dictionary

Add a word to one of the user&#39;s personal dictionaries. Please note that this feature is considered to be used for personal dictionaries which must not contain more than 500 words. If this is an issue for you, please contact us.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.languagetoolplus.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String word = "word_example"; // String | The word to be added. Must not be a phrase, i.e. cannot contain white space. The word is added to a global dictionary that applies to all languages.
    String username = "username_example"; // String | Your username as used to log in at languagetool.org.
    String apiKey = "apiKey_example"; // String | <a target='_blank' href='https://languagetool.org/editor/settings/access-tokens'>Your API key</a>
    String dict = "dict_example"; // String | Name of the dictionary to add the word to; non-existent dictionaries are created after calling this; if unset, adds to special default dictionary
    try {
      WordsAddPost200Response result = apiInstance.wordsAddPost(word, username, apiKey, dict);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wordsAddPost");
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
| **word** | **String**| The word to be added. Must not be a phrase, i.e. cannot contain white space. The word is added to a global dictionary that applies to all languages. | |
| **username** | **String**| Your username as used to log in at languagetool.org. | |
| **apiKey** | **String**| &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;Your API key&lt;/a&gt; | |
| **dict** | **String**| Name of the dictionary to add the word to; non-existent dictionaries are created after calling this; if unset, adds to special default dictionary | [optional] |

### Return type

[**WordsAddPost200Response**](WordsAddPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the result of adding the word |  -  |

<a id="wordsDeletePost"></a>
# **wordsDeletePost**
> WordsDeletePost200Response wordsDeletePost(word, username, apiKey, dict)

Remove word from a dictionary

Remove a word from one of the user&#39;s personal dictionaries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.languagetoolplus.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String word = "word_example"; // String | The word to be removed.
    String username = "username_example"; // String | Your username as used to log in at languagetool.org.
    String apiKey = "apiKey_example"; // String | <a target='_blank' href='https://languagetool.org/editor/settings/access-tokens'>Your API key</a>
    String dict = "dict_example"; // String | Name of the dictionary to remove the word from; if the dictionary is empty upon calling this, it is deleted; if unset, removes from special default dictionary
    try {
      WordsDeletePost200Response result = apiInstance.wordsDeletePost(word, username, apiKey, dict);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wordsDeletePost");
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
| **word** | **String**| The word to be removed. | |
| **username** | **String**| Your username as used to log in at languagetool.org. | |
| **apiKey** | **String**| &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;Your API key&lt;/a&gt; | |
| **dict** | **String**| Name of the dictionary to remove the word from; if the dictionary is empty upon calling this, it is deleted; if unset, removes from special default dictionary | [optional] |

### Return type

[**WordsDeletePost200Response**](WordsDeletePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the result of removing the word |  -  |

<a id="wordsGet"></a>
# **wordsGet**
> WordsGet200Response wordsGet(username, apiKey, offset, limit, dicts)

List words in dictionaries

List words in the user&#39;s personal dictionaries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.languagetoolplus.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | Your username as used to log in at languagetool.org.
    String apiKey = "apiKey_example"; // String | <a target='_blank' href='https://languagetool.org/editor/settings/access-tokens'>Your API key</a>
    Integer offset = 56; // Integer | Offset of where to start in the list of words. Defaults to 0.
    Integer limit = 56; // Integer | Maximum number of words to return. Defaults to 10.
    String dicts = "dicts_example"; // String | Comma-separated list of dictionaries to include words from; uses special default dictionary if this is unset
    try {
      WordsGet200Response result = apiInstance.wordsGet(username, apiKey, offset, limit, dicts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wordsGet");
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
| **username** | **String**| Your username as used to log in at languagetool.org. | |
| **apiKey** | **String**| &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;Your API key&lt;/a&gt; | |
| **offset** | **Integer**| Offset of where to start in the list of words. Defaults to 0. | [optional] |
| **limit** | **Integer**| Maximum number of words to return. Defaults to 10. | [optional] |
| **dicts** | **String**| Comma-separated list of dictionaries to include words from; uses special default dictionary if this is unset | [optional] |

### Return type

[**WordsGet200Response**](WordsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the user&#39;s words from the given user dictionaries |  -  |


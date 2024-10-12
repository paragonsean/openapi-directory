# TransformApi

All URIs are relative to *https://wikimedia.org/api/rest_v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transformHtmlFromFromLangToToLangPost**](TransformApi.md#transformHtmlFromFromLangToToLangPost) | **POST** /transform/html/from/{from_lang}/to/{to_lang} | Machine-translate content |
| [**transformHtmlFromFromLangToToLangProviderPost**](TransformApi.md#transformHtmlFromFromLangToToLangProviderPost) | **POST** /transform/html/from/{from_lang}/to/{to_lang}/{provider} | Machine-translate content |
| [**transformListLanguagepairsGet**](TransformApi.md#transformListLanguagepairsGet) | **GET** /transform/list/languagepairs/ | Lists the language pairs supported by the back-end |
| [**transformListPairFromToGet**](TransformApi.md#transformListPairFromToGet) | **GET** /transform/list/pair/{from}/{to}/ | Lists the tools available for a language pair |
| [**transformListToolToolFromGet**](TransformApi.md#transformListToolToolFromGet) | **GET** /transform/list/tool/{tool}/{from} | Lists the tools and language pairs available for the given tool category |
| [**transformListToolToolFromToGet**](TransformApi.md#transformListToolToolFromToGet) | **GET** /transform/list/tool/{tool}/{from}/{to} | Lists the tools and language pairs available for the given tool category |
| [**transformListToolToolGet**](TransformApi.md#transformListToolToolGet) | **GET** /transform/list/tool/{tool} | Lists the tools and language pairs available for the given tool category |
| [**transformWordFromFromLangToToLangWordGet**](TransformApi.md#transformWordFromFromLangToToLangWordGet) | **GET** /transform/word/from/{from_lang}/to/{to_lang}/{word} | Fetch the dictionary meaning of a word |
| [**transformWordFromFromLangToToLangWordProviderGet**](TransformApi.md#transformWordFromFromLangToToLangWordProviderGet) | **GET** /transform/word/from/{from_lang}/to/{to_lang}/{word}/{provider} | Fetch the dictionary meaning of a word |


<a id="transformHtmlFromFromLangToToLangPost"></a>
# **transformHtmlFromFromLangToToLangPost**
> CxMt transformHtmlFromFromLangToToLangPost(fromLang, toLang, html)

Machine-translate content

Fetches the machine translation for the posted content from the source to the destination language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String fromLang = "fromLang_example"; // String | The source language code
    String toLang = "toLang_example"; // String | The target language code
    String html = "html_example"; // String | The HTML content to translate
    try {
      CxMt result = apiInstance.transformHtmlFromFromLangToToLangPost(fromLang, toLang, html);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformHtmlFromFromLangToToLangPost");
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
| **fromLang** | **String**| The source language code | |
| **toLang** | **String**| The target language code | |
| **html** | **String**| The HTML content to translate | |

### Return type

[**CxMt**](CxMt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The translated content |  -  |
| **0** | Error |  -  |

<a id="transformHtmlFromFromLangToToLangProviderPost"></a>
# **transformHtmlFromFromLangToToLangProviderPost**
> CxMt transformHtmlFromFromLangToToLangProviderPost(fromLang, toLang, provider, html)

Machine-translate content

Fetches the machine translation for the posted content from the source to the destination language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String fromLang = "fromLang_example"; // String | The source language code
    String toLang = "toLang_example"; // String | The target language code
    String provider = "Apertium"; // String | The machine translation provider id
    String html = "html_example"; // String | The HTML content to translate
    try {
      CxMt result = apiInstance.transformHtmlFromFromLangToToLangProviderPost(fromLang, toLang, provider, html);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformHtmlFromFromLangToToLangProviderPost");
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
| **fromLang** | **String**| The source language code | |
| **toLang** | **String**| The target language code | |
| **provider** | **String**| The machine translation provider id | [enum: Apertium, Yandex, Youdao] |
| **html** | **String**| The HTML content to translate | |

### Return type

[**CxMt**](CxMt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The translated content |  -  |
| **0** | Error |  -  |

<a id="transformListLanguagepairsGet"></a>
# **transformListLanguagepairsGet**
> CxLanguagepairs transformListLanguagepairsGet()

Lists the language pairs supported by the back-end

Fetches the list of language pairs the back-end service can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    try {
      CxLanguagepairs result = apiInstance.transformListLanguagepairsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformListLanguagepairsGet");
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

[**CxLanguagepairs**](CxLanguagepairs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of source and target languages supported by the API |  -  |

<a id="transformListPairFromToGet"></a>
# **transformListPairFromToGet**
> CxListTools transformListPairFromToGet(from, to)

Lists the tools available for a language pair

Fetches the list of tools that are available for the given pair of languages.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String from = "from_example"; // String | The source language code
    String to = "to_example"; // String | The target language code
    try {
      CxListTools result = apiInstance.transformListPairFromToGet(from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformListPairFromToGet");
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
| **from** | **String**| The source language code | |
| **to** | **String**| The target language code | |

### Return type

[**CxListTools**](CxListTools.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of tools available for the language pair |  -  |
| **0** | Error |  -  |

<a id="transformListToolToolFromGet"></a>
# **transformListToolToolFromGet**
> Object transformListToolToolFromGet(tool, from)

Lists the tools and language pairs available for the given tool category

Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String tool = "mt"; // String | The tool category to list tools and language pairs for
    String from = "from_example"; // String | The source language code
    try {
      Object result = apiInstance.transformListToolToolFromGet(tool, from);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformListToolToolFromGet");
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
| **tool** | **String**| The tool category to list tools and language pairs for | [enum: mt, dictionary] |
| **from** | **String**| The source language code | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of language pairs available for a given translation tool |  -  |
| **0** | Error |  -  |

<a id="transformListToolToolFromToGet"></a>
# **transformListToolToolFromToGet**
> Object transformListToolToolFromToGet(tool, from, to)

Lists the tools and language pairs available for the given tool category

Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String tool = "mt"; // String | The tool category to list tools and language pairs for
    String from = "from_example"; // String | The source language code
    String to = "to_example"; // String | The target language code
    try {
      Object result = apiInstance.transformListToolToolFromToGet(tool, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformListToolToolFromToGet");
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
| **tool** | **String**| The tool category to list tools and language pairs for | [enum: mt, dictionary] |
| **from** | **String**| The source language code | |
| **to** | **String**| The target language code | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of language pairs available for a given translation tool |  -  |
| **0** | Error |  -  |

<a id="transformListToolToolGet"></a>
# **transformListToolToolGet**
> Object transformListToolToolGet(tool)

Lists the tools and language pairs available for the given tool category

Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String tool = "mt"; // String | The tool category to list tools and language pairs for
    try {
      Object result = apiInstance.transformListToolToolGet(tool);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformListToolToolGet");
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
| **tool** | **String**| The tool category to list tools and language pairs for | [enum: mt, dictionary] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of language pairs available for a given translation tool |  -  |
| **0** | Error |  -  |

<a id="transformWordFromFromLangToToLangWordGet"></a>
# **transformWordFromFromLangToToLangWordGet**
> CxDict transformWordFromFromLangToToLangWordGet(fromLang, toLang, word)

Fetch the dictionary meaning of a word

Fetches the dictionary meaning of a word from a language and displays it in the target language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String fromLang = "fromLang_example"; // String | The source language code
    String toLang = "toLang_example"; // String | The target language code
    String word = "word_example"; // String | The word to lookup
    try {
      CxDict result = apiInstance.transformWordFromFromLangToToLangWordGet(fromLang, toLang, word);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformWordFromFromLangToToLangWordGet");
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
| **fromLang** | **String**| The source language code | |
| **toLang** | **String**| The target language code | |
| **word** | **String**| The word to lookup | |

### Return type

[**CxDict**](CxDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the dictionary translation for the given word |  -  |
| **0** | Error |  -  |

<a id="transformWordFromFromLangToToLangWordProviderGet"></a>
# **transformWordFromFromLangToToLangWordProviderGet**
> CxDict transformWordFromFromLangToToLangWordProviderGet(fromLang, toLang, word, provider)

Fetch the dictionary meaning of a word

Fetches the dictionary meaning of a word from a language and displays it in the target language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wikimedia.org/api/rest_v1");

    TransformApi apiInstance = new TransformApi(defaultClient);
    String fromLang = "fromLang_example"; // String | The source language code
    String toLang = "toLang_example"; // String | The target language code
    String word = "word_example"; // String | The word to lookup
    String provider = "JsonDict"; // String | The dictionary provider id
    try {
      CxDict result = apiInstance.transformWordFromFromLangToToLangWordProviderGet(fromLang, toLang, word, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransformApi#transformWordFromFromLangToToLangWordProviderGet");
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
| **fromLang** | **String**| The source language code | |
| **toLang** | **String**| The target language code | |
| **word** | **String**| The word to lookup | |
| **provider** | **String**| The dictionary provider id | [enum: JsonDict, Dictd] |

### Return type

[**CxDict**](CxDict.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the dictionary translation for the given word |  -  |
| **0** | Error |  -  |


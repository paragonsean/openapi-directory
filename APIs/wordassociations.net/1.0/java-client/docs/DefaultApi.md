# DefaultApi

All URIs are relative to *https://api.wordassociations.net/associations/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jsonSearchGet**](DefaultApi.md#jsonSearchGet) | **GET** /json/search |  |
| [**jsonSearchPost**](DefaultApi.md#jsonSearchPost) | **POST** /json/search |  |


<a id="jsonSearchGet"></a>
# **jsonSearchGet**
> Body jsonSearchGet(text, lang, type, limit, pos, indent)



Gets associations with the given word or phrase. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordassociations.net/associations/v1.0");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<String> text = Arrays.asList(); // List<String> | Word or phrase to find associations with. Tip. You can use multiple parameters 'text' in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text. 
    String lang = "de"; // String | Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian; 
    String type = "stimulus"; // String | Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word. 
    Integer limit = 50; // Integer | Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive. 
    List<String> pos = Arrays.asList(); // List<String> | Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb 
    String indent = "true"; // String | Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off; 
    try {
      Body result = apiInstance.jsonSearchGet(text, lang, type, limit, pos, indent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jsonSearchGet");
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
| **text** | [**List&lt;String&gt;**](String.md)| Word or phrase to find associations with. Tip. You can use multiple parameters &#39;text&#39; in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text.  | |
| **lang** | **String**| Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian;  | [enum: de, en, es, fr, it, pt, ru] |
| **type** | **String**| Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word.  | [optional] [default to stimulus] [enum: stimulus, response] |
| **limit** | **Integer**| Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive.  | [optional] [default to 50] |
| **pos** | [**List&lt;String&gt;**](String.md)| Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb  | [optional] [enum: noun, adjective, verb, adverb] |
| **indent** | **String**| Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off;  | [optional] [default to true] [enum: true, false] |

### Return type

[**Body**](Body.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Invalid API key |  -  |
| **429** | The monthly limit on the number of requests is exceeded |  -  |
| **501** | The specified language is not supported |  -  |

<a id="jsonSearchPost"></a>
# **jsonSearchPost**
> Body jsonSearchPost(text, lang, type, limit, pos, indent)



Gets associations with the given word or phrase. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.wordassociations.net/associations/v1.0");
    
    // Configure API key authorization: internalApiKey
    ApiKeyAuth internalApiKey = (ApiKeyAuth) defaultClient.getAuthentication("internalApiKey");
    internalApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //internalApiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<String> text = Arrays.asList(); // List<String> | Word or phrase to find associations with. Tip. You can use multiple parameters 'text' in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text. 
    String lang = "de"; // String | Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian; 
    String type = "stimulus"; // String | Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word. 
    Integer limit = 50; // Integer | Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive. 
    List<String> pos = Arrays.asList(); // List<String> | Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb 
    String indent = "true"; // String | Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off; 
    try {
      Body result = apiInstance.jsonSearchPost(text, lang, type, limit, pos, indent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jsonSearchPost");
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
| **text** | [**List&lt;String&gt;**](String.md)| Word or phrase to find associations with. Tip. You can use multiple parameters &#39;text&#39; in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text.  | |
| **lang** | **String**| Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian;  | [enum: de, en, es, fr, it, pt, ru] |
| **type** | **String**| Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word.  | [optional] [default to stimulus] [enum: stimulus, response] |
| **limit** | **Integer**| Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive.  | [optional] [default to 50] |
| **pos** | [**List&lt;String&gt;**](String.md)| Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb  | [optional] [enum: noun, adjective, verb, adverb] |
| **indent** | **String**| Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off;  | [optional] [default to true] [enum: true, false] |

### Return type

[**Body**](Body.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Invalid API key |  -  |
| **429** | The monthly limit on the number of requests is exceeded |  -  |
| **501** | The specified language is not supported |  -  |


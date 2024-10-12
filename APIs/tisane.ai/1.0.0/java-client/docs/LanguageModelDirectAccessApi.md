# LanguageModelDirectAccessApi

All URIs are relative to *https://api.tisane.ai*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFamilyDetails**](LanguageModelDirectAccessApi.md#getFamilyDetails) | **GET** /lm/family | Get family details |
| [**listFeatureValues**](LanguageModelDirectAccessApi.md#listFeatureValues) | **GET** /values | List feature values |
| [**listHypernyms**](LanguageModelDirectAccessApi.md#listHypernyms) | **GET** /hypernyms | List hypernyms |
| [**listHyponyms**](LanguageModelDirectAccessApi.md#listHyponyms) | **GET** /hyponyms | List hyponyms |
| [**listInflectedForms**](LanguageModelDirectAccessApi.md#listInflectedForms) | **GET** /inflections | List inflected forms |
| [**listWordSenses**](LanguageModelDirectAccessApi.md#listWordSenses) | **GET** /senses | List word senses |


<a id="getFamilyDetails"></a>
# **getFamilyDetails**
> GetFamilyDetails200Response getFamilyDetails(id, ocpApimSubscriptionKey)

Get family details

Fetches and outputs metadata for a family from the Tisane language models.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageModelDirectAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tisane.ai");

    LanguageModelDirectAccessApi apiInstance = new LanguageModelDirectAccessApi(defaultClient);
    String id = "{family_id}"; // String | (Required) a numeric identifier of the family
    String ocpApimSubscriptionKey = "{{apiKey}}"; // String | {{apiKeyDescription}}
    try {
      GetFamilyDetails200Response result = apiInstance.getFamilyDetails(id, ocpApimSubscriptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelDirectAccessApi#getFamilyDetails");
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
| **id** | **String**| (Required) a numeric identifier of the family | [optional] |
| **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] |

### Return type

[**GetFamilyDetails200Response**](GetFamilyDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the family for &#39;plot twist&#39; |  -  |

<a id="listFeatureValues"></a>
# **listFeatureValues**
> List&lt;String&gt; listFeatureValues(language, type, description, ocpApimSubscriptionKey)

List feature values

Lists feature values for a particular category of features. This allows obtaining all the values such as entity types, subtypes, abuse types and tags, and more.  Returns the values as a JSON array of strings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageModelDirectAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tisane.ai");

    LanguageModelDirectAccessApi apiInstance = new LanguageModelDirectAccessApi(defaultClient);
    String language = "{language_code}"; // String | (Required) Language code
    String type = "{Grammar/Style/Semantics}"; // String | (Required) Feature type
    String description = "{feature_list_name}"; // String | (Required) Feature list name (localized)
    String ocpApimSubscriptionKey = "{{apiKey}}"; // String | {{apiKeyDescription}}
    try {
      List<String> result = apiInstance.listFeatureValues(language, type, description, ocpApimSubscriptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelDirectAccessApi#listFeatureValues");
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
| **language** | **String**| (Required) Language code | [optional] |
| **type** | **String**| (Required) Feature type | [optional] |
| **description** | **String**| (Required) Feature list name (localized) | [optional] |
| **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List entity subtypes |  -  |

<a id="listHypernyms"></a>
# **listHypernyms**
> List&lt;List&lt;ListHypernyms200ResponseInnerInner&gt;&gt; listHypernyms(family, maxLevel, ocpApimSubscriptionKey)

List hypernyms

Lists all hypernyms related to a family. A hypernym is a parent concent. E.g. \&quot;vehicle\&quot; is a hypernym of \&quot;truck\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageModelDirectAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tisane.ai");

    LanguageModelDirectAccessApi apiInstance = new LanguageModelDirectAccessApi(defaultClient);
    String family = "{family_id}"; // String | (Required) a numeric identifier of the family
    String maxLevel = "{max_number_of_levels}"; // String | (Required) maximum distance from the family
    String ocpApimSubscriptionKey = "{{apiKey}}"; // String | {{apiKeyDescription}}
    try {
      List<List<ListHypernyms200ResponseInnerInner>> result = apiInstance.listHypernyms(family, maxLevel, ocpApimSubscriptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelDirectAccessApi#listHypernyms");
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
| **family** | **String**| (Required) a numeric identifier of the family | [optional] |
| **maxLevel** | **String**| (Required) maximum distance from the family | [optional] |
| **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] |

### Return type

[**List&lt;List&lt;ListHypernyms200ResponseInnerInner&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Hypernyms of Darth Vader |  -  |

<a id="listHyponyms"></a>
# **listHyponyms**
> listHyponyms(family, maxLevel, ocpApimSubscriptionKey)

List hyponyms

Lists all hyponyms related to a family. A hyponym is a child concent. E.g. \&quot;truck\&quot; is a hypernym of \&quot;vehicle\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageModelDirectAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tisane.ai");

    LanguageModelDirectAccessApi apiInstance = new LanguageModelDirectAccessApi(defaultClient);
    String family = "{family_id}"; // String | (Required) a numeric identifier of the family
    String maxLevel = "{max_number_of_levels}"; // String | (Required) maximum distance from the family
    String ocpApimSubscriptionKey = "{{apiKey}}"; // String | {{apiKeyDescription}}
    try {
      apiInstance.listHyponyms(family, maxLevel, ocpApimSubscriptionKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelDirectAccessApi#listHyponyms");
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
| **family** | **String**| (Required) a numeric identifier of the family | [optional] |
| **maxLevel** | **String**| (Required) maximum distance from the family | [optional] |
| **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="listInflectedForms"></a>
# **listInflectedForms**
> List&lt;ListInflectedForms200ResponseInner&gt; listInflectedForms(language, lexeme, family, ocpApimSubscriptionKey)

List inflected forms

List inflected forms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageModelDirectAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tisane.ai");

    LanguageModelDirectAccessApi apiInstance = new LanguageModelDirectAccessApi(defaultClient);
    String language = "{language_code}"; // String | (Required) The language code
    String lexeme = "{lexeme_id}"; // String | (Required) The lexeme to inspect
    String family = "{family_id}"; // String | (Required) The family to inspect
    String ocpApimSubscriptionKey = "{{apiKey}}"; // String | {{apiKeyDescription}}
    try {
      List<ListInflectedForms200ResponseInner> result = apiInstance.listInflectedForms(language, lexeme, family, ocpApimSubscriptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelDirectAccessApi#listInflectedForms");
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
| **language** | **String**| (Required) The language code | [optional] |
| **lexeme** | **String**| (Required) The lexeme to inspect | [optional] |
| **family** | **String**| (Required) The family to inspect | [optional] |
| **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] |

### Return type

[**List&lt;ListInflectedForms200ResponseInner&gt;**](ListInflectedForms200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Inflected forms of \&quot;United States\&quot; in Russian |  -  |

<a id="listWordSenses"></a>
# **listWordSenses**
> List&lt;ListWordSenses200ResponseInner&gt; listWordSenses(language, word, ocpApimSubscriptionKey)

List word senses

Fetches and outputs all senses related to a word.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageModelDirectAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tisane.ai");

    LanguageModelDirectAccessApi apiInstance = new LanguageModelDirectAccessApi(defaultClient);
    String language = "{language_code}"; // String | (Required) a standard culture code (ISO-639 language code with an optional country extension)
    String word = "{word}"; // String | (Required) the word to inspect
    String ocpApimSubscriptionKey = "{{apiKey}}"; // String | {{apiKeyDescription}}
    try {
      List<ListWordSenses200ResponseInner> result = apiInstance.listWordSenses(language, word, ocpApimSubscriptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageModelDirectAccessApi#listWordSenses");
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
| **language** | **String**| (Required) a standard culture code (ISO-639 language code with an optional country extension) | [optional] |
| **word** | **String**| (Required) the word to inspect | [optional] |
| **ocpApimSubscriptionKey** | **String**| {{apiKeyDescription}} | [optional] |

### Return type

[**List&lt;ListWordSenses200ResponseInner&gt;**](ListWordSenses200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Interpretations of \&quot;couscous\&quot; |  -  |


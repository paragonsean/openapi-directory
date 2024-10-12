# QuoteApi

All URIs are relative to *https://quotes.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteAuthorsPopularGet**](QuoteApi.md#quoteAuthorsPopularGet) | **GET** /quote/authors/popular |  |
| [**quoteAuthorsSearchGet**](QuoteApi.md#quoteAuthorsSearchGet) | **GET** /quote/authors/search |  |
| [**quoteBookmarkToggleGet**](QuoteApi.md#quoteBookmarkToggleGet) | **GET** /quote/bookmark/toggle |  |
| [**quoteCategoriesPopularGet**](QuoteApi.md#quoteCategoriesPopularGet) | **GET** /quote/categories/popular |  |
| [**quoteCategoriesSearchGet**](QuoteApi.md#quoteCategoriesSearchGet) | **GET** /quote/categories/search |  |
| [**quoteGet**](QuoteApi.md#quoteGet) | **GET** /quote |  |
| [**quoteLikeToggleGet**](QuoteApi.md#quoteLikeToggleGet) | **GET** /quote/like/toggle |  |
| [**quoteRandomGet**](QuoteApi.md#quoteRandomGet) | **GET** /quote/random |  |
| [**quoteSearchGet**](QuoteApi.md#quoteSearchGet) | **GET** /quote/search |  |


<a id="quoteAuthorsPopularGet"></a>
# **quoteAuthorsPopularGet**
> quoteAuthorsPopularGet(language, detailed, start, limit)



Gets a list of popular author names in the system.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String language = "en"; // String | Language. A same author may have quotes in two or more different languages. So for example 'Mahatma Gandhi' may be returned for language \"en\"(English), and \"மஹாத்மா காந்தி\" may be returned when the language is \"ta\" (Tamil).
    Boolean detailed = false; // Boolean | Should return detailed author information such as `birthday`, `death date`, `occupation`, `description` etc. Only available at certain subscription levels.
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    Integer limit = 5; // Integer | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    try {
      apiInstance.quoteAuthorsPopularGet(language, detailed, start, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteAuthorsPopularGet");
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
| **language** | **String**| Language. A same author may have quotes in two or more different languages. So for example &#39;Mahatma Gandhi&#39; may be returned for language \&quot;en\&quot;(English), and \&quot;மஹாத்மா காந்தி\&quot; may be returned when the language is \&quot;ta\&quot; (Tamil). | [optional] [default to en] |
| **detailed** | **Boolean**| Should return detailed author information such as &#x60;birthday&#x60;, &#x60;death date&#x60;, &#x60;occupation&#x60;, &#x60;description&#x60; etc. Only available at certain subscription levels. | [optional] [default to false] |
| **start** | **Integer**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0] |
| **limit** | **Integer**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 5] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **400** | 400  response |  -  |

<a id="quoteAuthorsSearchGet"></a>
# **quoteAuthorsSearchGet**
> quoteAuthorsSearchGet(query, language, detailed, start, limit)



Gets a list of author names in the system.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String query = "query_example"; // String | Text string to search for in author names
    String language = "en"; // String | Language. A same author may have quotes in two or more different languages. So for example 'Mahatma Gandhi' may be returned for language \"en\"(English), and \"மஹாத்மா காந்தி\" may be returned when the language is \"ta\" (Tamil).
    Boolean detailed = false; // Boolean | Should return detailed author information such as `birthday`, `death date`, `occupation`, `description` etc. Only available at certain subscription levels.
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    Integer limit = 1; // Integer | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    try {
      apiInstance.quoteAuthorsSearchGet(query, language, detailed, start, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteAuthorsSearchGet");
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
| **query** | **String**| Text string to search for in author names | [optional] |
| **language** | **String**| Language. A same author may have quotes in two or more different languages. So for example &#39;Mahatma Gandhi&#39; may be returned for language \&quot;en\&quot;(English), and \&quot;மஹாத்மா காந்தி\&quot; may be returned when the language is \&quot;ta\&quot; (Tamil). | [optional] [default to en] |
| **detailed** | **Boolean**| Should return detailed author information such as &#x60;birthday&#x60;, &#x60;death date&#x60;, &#x60;occupation&#x60;, &#x60;description&#x60; etc. Only available at certain subscription levels. | [optional] [default to false] |
| **start** | **Integer**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0] |
| **limit** | **Integer**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 1] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **400** | 400  response |  -  |

<a id="quoteBookmarkToggleGet"></a>
# **quoteBookmarkToggleGet**
> quoteBookmarkToggleGet(quoteId)



Toggle the user bookmark of the given Quote as a user of the API Key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String quoteId = "quoteId_example"; // String | Quote ID
    try {
      apiInstance.quoteBookmarkToggleGet(quoteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteBookmarkToggleGet");
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
| **quoteId** | **String**| Quote ID | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="quoteCategoriesPopularGet"></a>
# **quoteCategoriesPopularGet**
> quoteCategoriesPopularGet(start, limit)



Gets a list of popular &#x60;Quote&#x60; Categories. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    Integer limit = 5; // Integer | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    try {
      apiInstance.quoteCategoriesPopularGet(start, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteCategoriesPopularGet");
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
| **start** | **Integer**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0] |
| **limit** | **Integer**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 5] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |

<a id="quoteCategoriesSearchGet"></a>
# **quoteCategoriesSearchGet**
> quoteCategoriesSearchGet(query, start, limit)



Gets a list of &#x60;Quote&#x60; Categories matching the query string. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String query = "0"; // String | Text string to search for in the categories
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    Integer limit = 2; // Integer | Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level.
    try {
      apiInstance.quoteCategoriesSearchGet(query, start, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteCategoriesSearchGet");
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
| **query** | **String**| Text string to search for in the categories | [optional] [default to 0] |
| **start** | **Integer**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0] |
| **limit** | **Integer**| Response is paged. This parameter controls how many is returned in the result. The maximum depends on the subscription level. | [optional] [default to 2] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |

<a id="quoteGet"></a>
# **quoteGet**
> QuoteResponse quoteGet(id)



Gets a &#x60;Quote&#x60; with a given &#x60;id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String id = "id_example"; // String | Quote ID
    try {
      QuoteResponse result = apiInstance.quoteGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteGet");
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
| **id** | **String**| Quote ID | [optional] |

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="quoteLikeToggleGet"></a>
# **quoteLikeToggleGet**
> quoteLikeToggleGet(quoteId)



Toggle the user like of the given Quote as a user of the API Key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String quoteId = "quoteId_example"; // String | Quote ID
    try {
      apiInstance.quoteLikeToggleGet(quoteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteLikeToggleGet");
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
| **quoteId** | **String**| Quote ID | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="quoteRandomGet"></a>
# **quoteRandomGet**
> QuoteResponse quoteRandomGet(language, limit)



Gets a &#x60;Random Quote&#x60;. When you are in a hurry this is what you call to get a random famous quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String language = "en"; // String | Language of the Quote. The language must be supported in our system.
    Integer limit = 1; // Integer | No of quotes to return. The max limit depends on the subscription level.
    try {
      QuoteResponse result = apiInstance.quoteRandomGet(language, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteRandomGet");
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
| **language** | **String**| Language of the Quote. The language must be supported in our system. | [optional] [default to en] |
| **limit** | **Integer**| No of quotes to return. The max limit depends on the subscription level. | [optional] [default to 1] |

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="quoteSearchGet"></a>
# **quoteSearchGet**
> QuoteResponse quoteSearchGet(category, author, minlength, maxlength, query, _private, language, limit, sfw)



Search for a &#x60;Quote&#x60; in They Said So platform. Optional &#x60;category&#x60; , &#x60;author&#x60;, &#x60;minlength&#x60;, &#x60;maxlength&#x60; params determines the filters applied while searching for the quote. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    String category = "category_example"; // String | Quote Category
    String author = "author_example"; // String | Quote Author
    Integer minlength = 100; // Integer | Quote minimum Length
    Integer maxlength = 300; // Integer | Quote maximum Length
    String query = "query_example"; // String | keyword to search for in the quote
    Boolean _private = false; // Boolean | Should search private collection? Default searches public collection.
    String language = "en"; // String | Language of the Quote. The language must be supported in our system.
    Integer limit = 1; // Integer | No of quotes to return. The max limit depends on the subscription level.
    Boolean sfw = false; // Boolean | Should search only SFW (Safe For Work) quotes?
    try {
      QuoteResponse result = apiInstance.quoteSearchGet(category, author, minlength, maxlength, query, _private, language, limit, sfw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteSearchGet");
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
| **category** | **String**| Quote Category | [optional] |
| **author** | **String**| Quote Author | [optional] |
| **minlength** | **Integer**| Quote minimum Length | [optional] [default to 100] |
| **maxlength** | **Integer**| Quote maximum Length | [optional] [default to 300] |
| **query** | **String**| keyword to search for in the quote | [optional] |
| **_private** | **Boolean**| Should search private collection? Default searches public collection. | [optional] [default to false] |
| **language** | **String**| Language of the Quote. The language must be supported in our system. | [optional] [default to en] |
| **limit** | **Integer**| No of quotes to return. The max limit depends on the subscription level. | [optional] [default to 1] |
| **sfw** | **Boolean**| Should search only SFW (Safe For Work) quotes? | [optional] [default to false] |

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |


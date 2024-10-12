# PrivateQuotesApi

All URIs are relative to *https://quotes.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteDelete**](PrivateQuotesApi.md#quoteDelete) | **DELETE** /quote |  |
| [**quoteGet_0**](PrivateQuotesApi.md#quoteGet_0) | **GET** /quote |  |
| [**quoteListGet**](PrivateQuotesApi.md#quoteListGet) | **GET** /quote/list |  |
| [**quotePatch**](PrivateQuotesApi.md#quotePatch) | **PATCH** /quote |  |
| [**quotePost**](PrivateQuotesApi.md#quotePost) | **POST** /quote |  |
| [**quotePut**](PrivateQuotesApi.md#quotePut) | **PUT** /quote |  |
| [**quoteTagsAddPost**](PrivateQuotesApi.md#quoteTagsAddPost) | **POST** /quote/tags/add |  |
| [**quoteTagsRemovePost**](PrivateQuotesApi.md#quoteTagsRemovePost) | **POST** /quote/tags/remove |  |


<a id="quoteDelete"></a>
# **quoteDelete**
> quoteDelete(id)



Delete a quote. The user needs to be the owner of the quote to be able to delete it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    String id = "id_example"; // String | Quote ID
    try {
      apiInstance.quoteDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quoteDelete");
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
| **id** | **String**| Quote ID | |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="quoteGet_0"></a>
# **quoteGet_0**
> QuoteResponse quoteGet_0(id)



Gets a &#x60;Quote&#x60; with a given &#x60;id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    String id = "id_example"; // String | Quote ID
    try {
      QuoteResponse result = apiInstance.quoteGet_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quoteGet_0");
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

<a id="quoteListGet"></a>
# **quoteListGet**
> quoteListGet(start, limit)



Get the list of quotes in your private collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    Integer limit = 10; // Integer | Response is paged. This parameter controls how many is returned in the result.
    try {
      apiInstance.quoteListGet(start, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quoteListGet");
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
| **limit** | **Integer**| Response is paged. This parameter controls how many is returned in the result. | [optional] [default to 10] |

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

<a id="quotePatch"></a>
# **quotePatch**
> quotePatch(id, quote, author, language, tags)



Update a quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    String id = "id_example"; // String | Quote ID
    String quote = "quote_example"; // String | Quote
    String author = "author_example"; // String | Quote Author
    String language = "en"; // String | Language. If not supplied an auto detection mechanism will be used to detect a language.
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.quotePatch(id, quote, author, language, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quotePatch");
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
| **id** | **String**| Quote ID | |
| **quote** | **String**| Quote | [optional] |
| **author** | **String**| Quote Author | [optional] |
| **language** | **String**| Language. If not supplied an auto detection mechanism will be used to detect a language. | [optional] [default to en] |
| **tags** | **String**| Comma Separated tags | [optional] |

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

<a id="quotePost"></a>
# **quotePost**
> quotePost(quote, author, tags, language)



Add a new quote to your private collection. Same as &#39;PUT&#39; but added since some clients don&#39;t handle PUT well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    String quote = "quote_example"; // String | Quote
    String author = "author_example"; // String | Quote Author
    String tags = "tags_example"; // String | Comma Separated tags
    String language = "en"; // String | Language. If not supplied an auto detection mechanism will be used to detect a language.
    try {
      apiInstance.quotePost(quote, author, tags, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quotePost");
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
| **quote** | **String**| Quote | |
| **author** | **String**| Quote Author | [optional] |
| **tags** | **String**| Comma Separated tags | [optional] |
| **language** | **String**| Language. If not supplied an auto detection mechanism will be used to detect a language. | [optional] [default to en] |

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

<a id="quotePut"></a>
# **quotePut**
> quotePut(quote, author, tags, language)



Add a new quote to your private collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    String quote = "quote_example"; // String | Quote
    String author = "author_example"; // String | Quote Author
    String tags = "tags_example"; // String | Comma Separated tags
    String language = "en"; // String | Language. If not supplied an auto detection mechanism will be used to detect a language.
    try {
      apiInstance.quotePut(quote, author, tags, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quotePut");
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
| **quote** | **String**| Quote | |
| **author** | **String**| Quote Author | [optional] |
| **tags** | **String**| Comma Separated tags | [optional] |
| **language** | **String**| Language. If not supplied an auto detection mechanism will be used to detect a language. | [optional] [default to en] |

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

<a id="quoteTagsAddPost"></a>
# **quoteTagsAddPost**
> quoteTagsAddPost(id, tags)



Add a tag to a given Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    String id = "id_example"; // String | Quote ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.quoteTagsAddPost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quoteTagsAddPost");
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
| **id** | **String**| Quote ID | |
| **tags** | **String**| Comma Separated tags | |

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

<a id="quoteTagsRemovePost"></a>
# **quoteTagsRemovePost**
> quoteTagsRemovePost(id, tags)



Remove a tag from a given quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateQuotesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    PrivateQuotesApi apiInstance = new PrivateQuotesApi(defaultClient);
    String id = "id_example"; // String | Quote ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.quoteTagsRemovePost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateQuotesApi#quoteTagsRemovePost");
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
| **id** | **String**| Quote ID | |
| **tags** | **String**| Comma Separated tags | |

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


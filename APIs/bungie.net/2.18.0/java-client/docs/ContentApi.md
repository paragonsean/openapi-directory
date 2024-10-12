# ContentApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentGetContentById**](ContentApi.md#contentGetContentById) | **GET** /Content/GetContentById/{id}/{locale}/ |  |
| [**contentGetContentByTagAndType**](ContentApi.md#contentGetContentByTagAndType) | **GET** /Content/GetContentByTagAndType/{tag}/{type}/{locale}/ |  |
| [**contentGetContentType**](ContentApi.md#contentGetContentType) | **GET** /Content/GetContentType/{type}/ |  |
| [**contentRssNewsArticles**](ContentApi.md#contentRssNewsArticles) | **GET** /Content/Rss/NewsArticles/{pageToken}/ |  |
| [**contentSearchContentByTagAndType**](ContentApi.md#contentSearchContentByTagAndType) | **GET** /Content/SearchContentByTagAndType/{tag}/{type}/{locale}/ |  |
| [**contentSearchContentWithText**](ContentApi.md#contentSearchContentWithText) | **GET** /Content/Search/{locale}/ |  |
| [**contentSearchHelpArticles**](ContentApi.md#contentSearchHelpArticles) | **GET** /Content/SearchHelpArticles/{searchtext}/{size}/ |  |


<a id="contentGetContentById"></a>
# **contentGetContentById**
> ContentGetContentById200Response contentGetContentById(id, locale, head)



Returns a content item referenced by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ContentApi apiInstance = new ContentApi(defaultClient);
    Long id = 56L; // Long | 
    String locale = "locale_example"; // String | 
    Boolean head = true; // Boolean | false
    try {
      ContentGetContentById200Response result = apiInstance.contentGetContentById(id, locale, head);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentGetContentById");
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
| **id** | **Long**|  | |
| **locale** | **String**|  | |
| **head** | **Boolean**| false | [optional] |

### Return type

[**ContentGetContentById200Response**](ContentGetContentById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="contentGetContentByTagAndType"></a>
# **contentGetContentByTagAndType**
> ContentGetContentById200Response contentGetContentByTagAndType(locale, tag, type, head)



Returns the newest item that matches a given tag and Content Type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String locale = "locale_example"; // String | 
    String tag = "tag_example"; // String | 
    String type = "type_example"; // String | 
    Boolean head = true; // Boolean | Not used.
    try {
      ContentGetContentById200Response result = apiInstance.contentGetContentByTagAndType(locale, tag, type, head);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentGetContentByTagAndType");
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
| **locale** | **String**|  | |
| **tag** | **String**|  | |
| **type** | **String**|  | |
| **head** | **Boolean**| Not used. | [optional] |

### Return type

[**ContentGetContentById200Response**](ContentGetContentById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="contentGetContentType"></a>
# **contentGetContentType**
> ContentGetContentType200Response contentGetContentType(type)



Gets an object describing a particular variant of content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String type = "type_example"; // String | 
    try {
      ContentGetContentType200Response result = apiInstance.contentGetContentType(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentGetContentType");
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
| **type** | **String**|  | |

### Return type

[**ContentGetContentType200Response**](ContentGetContentType200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="contentRssNewsArticles"></a>
# **contentRssNewsArticles**
> ContentRssNewsArticles200Response contentRssNewsArticles(pageToken, categoryfilter, includebody)



Returns a JSON string response that is the RSS feed for news articles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Zero-based pagination token for paging through result sets.
    String categoryfilter = "categoryfilter_example"; // String | Optionally filter response to only include news items in a certain category.
    Boolean includebody = true; // Boolean | Optionally include full content body for each news item.
    try {
      ContentRssNewsArticles200Response result = apiInstance.contentRssNewsArticles(pageToken, categoryfilter, includebody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentRssNewsArticles");
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
| **pageToken** | **String**| Zero-based pagination token for paging through result sets. | |
| **categoryfilter** | **String**| Optionally filter response to only include news items in a certain category. | [optional] |
| **includebody** | **Boolean**| Optionally include full content body for each news item. | [optional] |

### Return type

[**ContentRssNewsArticles200Response**](ContentRssNewsArticles200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="contentSearchContentByTagAndType"></a>
# **contentSearchContentByTagAndType**
> ContentSearchContentWithText200Response contentSearchContentByTagAndType(locale, tag, type, currentpage, head, itemsperpage)



Searches for Content Items that match the given Tag and Content Type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String locale = "locale_example"; // String | 
    String tag = "tag_example"; // String | 
    String type = "type_example"; // String | 
    Integer currentpage = 56; // Integer | Page number for the search results starting with page 1.
    Boolean head = true; // Boolean | Not used.
    Integer itemsperpage = 56; // Integer | Not used.
    try {
      ContentSearchContentWithText200Response result = apiInstance.contentSearchContentByTagAndType(locale, tag, type, currentpage, head, itemsperpage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentSearchContentByTagAndType");
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
| **locale** | **String**|  | |
| **tag** | **String**|  | |
| **type** | **String**|  | |
| **currentpage** | **Integer**| Page number for the search results starting with page 1. | [optional] |
| **head** | **Boolean**| Not used. | [optional] |
| **itemsperpage** | **Integer**| Not used. | [optional] |

### Return type

[**ContentSearchContentWithText200Response**](ContentSearchContentWithText200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="contentSearchContentWithText"></a>
# **contentSearchContentWithText**
> ContentSearchContentWithText200Response contentSearchContentWithText(locale, ctype, currentpage, head, searchtext, source, tag)



Gets content based on querystring information passed in. Provides basic search and text search capabilities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String locale = "locale_example"; // String | 
    String ctype = "ctype_example"; // String | Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
    Integer currentpage = 56; // Integer | Page number for the search results, starting with page 1.
    Boolean head = true; // Boolean | Not used.
    String searchtext = "searchtext_example"; // String | Word or phrase for the search.
    String source = "source_example"; // String | For analytics, hint at the part of the app that triggered the search. Optional.
    String tag = "tag_example"; // String | Tag used on the content to be searched.
    try {
      ContentSearchContentWithText200Response result = apiInstance.contentSearchContentWithText(locale, ctype, currentpage, head, searchtext, source, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentSearchContentWithText");
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
| **locale** | **String**|  | |
| **ctype** | **String**| Content type tag: Help, News, etc. Supply multiple ctypes separated by space. | [optional] |
| **currentpage** | **Integer**| Page number for the search results, starting with page 1. | [optional] |
| **head** | **Boolean**| Not used. | [optional] |
| **searchtext** | **String**| Word or phrase for the search. | [optional] |
| **source** | **String**| For analytics, hint at the part of the app that triggered the search. Optional. | [optional] |
| **tag** | **String**| Tag used on the content to be searched. | [optional] |

### Return type

[**ContentSearchContentWithText200Response**](ContentSearchContentWithText200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="contentSearchHelpArticles"></a>
# **contentSearchHelpArticles**
> ContentSearchHelpArticles200Response contentSearchHelpArticles(searchtext, size)



Search for Help Articles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    ContentApi apiInstance = new ContentApi(defaultClient);
    String searchtext = "searchtext_example"; // String | 
    String size = "size_example"; // String | 
    try {
      ContentSearchHelpArticles200Response result = apiInstance.contentSearchHelpArticles(searchtext, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentApi#contentSearchHelpArticles");
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
| **searchtext** | **String**|  | |
| **size** | **String**|  | |

### Return type

[**ContentSearchHelpArticles200Response**](ContentSearchHelpArticles200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |


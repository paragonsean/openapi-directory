# QuoteImagesApi

All URIs are relative to *https://quotes.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteImageBackgroundDelete**](QuoteImagesApi.md#quoteImageBackgroundDelete) | **DELETE** /quote/image/background |  |
| [**quoteImageBackgroundListGet**](QuoteImagesApi.md#quoteImageBackgroundListGet) | **GET** /quote/image/background/list |  |
| [**quoteImageBackgroundPost**](QuoteImagesApi.md#quoteImageBackgroundPost) | **POST** /quote/image/background |  |
| [**quoteImageBackgroundSearchGet**](QuoteImagesApi.md#quoteImageBackgroundSearchGet) | **GET** /quote/image/background/search |  |
| [**quoteImageBackgroundTagsAddPost**](QuoteImagesApi.md#quoteImageBackgroundTagsAddPost) | **POST** /quote/image/background/tags/add |  |
| [**quoteImageBackgroundTagsRemovePost**](QuoteImagesApi.md#quoteImageBackgroundTagsRemovePost) | **POST** /quote/image/background/tags/remove |  |
| [**quoteImageDelete**](QuoteImagesApi.md#quoteImageDelete) | **DELETE** /quote/image |  |
| [**quoteImageFontDelete**](QuoteImagesApi.md#quoteImageFontDelete) | **DELETE** /quote/image/font |  |
| [**quoteImageFontListGet**](QuoteImagesApi.md#quoteImageFontListGet) | **GET** /quote/image/font/list |  |
| [**quoteImageFontPost**](QuoteImagesApi.md#quoteImageFontPost) | **POST** /quote/image/font |  |
| [**quoteImageFontSearchGet**](QuoteImagesApi.md#quoteImageFontSearchGet) | **GET** /quote/image/font/search |  |
| [**quoteImageFontTagsAddPost**](QuoteImagesApi.md#quoteImageFontTagsAddPost) | **POST** /quote/image/font/tags/add |  |
| [**quoteImageFontTagsRemovePost**](QuoteImagesApi.md#quoteImageFontTagsRemovePost) | **POST** /quote/image/font/tags/remove |  |
| [**quoteImageGet**](QuoteImagesApi.md#quoteImageGet) | **GET** /quote/image |  |
| [**quoteImagePut**](QuoteImagesApi.md#quoteImagePut) | **PUT** /quote/image |  |
| [**quoteImageSearchGet**](QuoteImagesApi.md#quoteImageSearchGet) | **GET** /quote/image/search |  |


<a id="quoteImageBackgroundDelete"></a>
# **quoteImageBackgroundDelete**
> quoteImageBackgroundDelete(id)



Delete a background image file. The user needs to be the owner of the background image to be able to delete it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Font ID
    try {
      apiInstance.quoteImageBackgroundDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageBackgroundDelete");
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
| **id** | **String**| Font ID | |

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

<a id="quoteImageBackgroundListGet"></a>
# **quoteImageBackgroundListGet**
> quoteImageBackgroundListGet(start)



Lists background images in your private collection.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    Integer start = 56; // Integer | Response is paged. This parameter determines where the response should start.
    try {
      apiInstance.quoteImageBackgroundListGet(start);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageBackgroundListGet");
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
| **start** | **Integer**| Response is paged. This parameter determines where the response should start. | [optional] |

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

<a id="quoteImageBackgroundPost"></a>
# **quoteImageBackgroundPost**
> quoteImageBackgroundPost(image, tags)



Add an image for use later as a quote background image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    File image = new File("/path/to/file"); // File | Image file to add to your collection (png/jpg/gif are supported)
    String tags = "tags_example"; // String | Optional comma separated tags
    try {
      apiInstance.quoteImageBackgroundPost(image, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageBackgroundPost");
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
| **image** | **File**| Image file to add to your collection (png/jpg/gif are supported) | |
| **tags** | **String**| Optional comma separated tags | [optional] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="quoteImageBackgroundSearchGet"></a>
# **quoteImageBackgroundSearchGet**
> quoteImageBackgroundSearchGet(query)



Searches for a background image with a given tag.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String query = "query_example"; // String | Tag string
    try {
      apiInstance.quoteImageBackgroundSearchGet(query);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageBackgroundSearchGet");
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
| **query** | **String**| Tag string | [optional] |

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

<a id="quoteImageBackgroundTagsAddPost"></a>
# **quoteImageBackgroundTagsAddPost**
> quoteImageBackgroundTagsAddPost(id, tags)



Add a tag to a given Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Image ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.quoteImageBackgroundTagsAddPost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageBackgroundTagsAddPost");
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
| **id** | **String**| Image ID | |
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

<a id="quoteImageBackgroundTagsRemovePost"></a>
# **quoteImageBackgroundTagsRemovePost**
> quoteImageBackgroundTagsRemovePost(id, tags)



Remove a tag from a given Image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Image ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.quoteImageBackgroundTagsRemovePost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageBackgroundTagsRemovePost");
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
| **id** | **String**| Image ID | |
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

<a id="quoteImageDelete"></a>
# **quoteImageDelete**
> quoteImageDelete(id)



Delete a quote image. The user needs to be the owner of the quote image to be able to delete it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Quote Image ID
    try {
      apiInstance.quoteImageDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageDelete");
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
| **id** | **String**| Quote Image ID | |

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

<a id="quoteImageFontDelete"></a>
# **quoteImageFontDelete**
> quoteImageFontDelete(id)



Delete a font file. The user needs to be the owner of the font to be able to delete it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Font ID
    try {
      apiInstance.quoteImageFontDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageFontDelete");
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
| **id** | **String**| Font ID | |

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

<a id="quoteImageFontListGet"></a>
# **quoteImageFontListGet**
> quoteImageFontListGet(start)



Lists background images in your private collection.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    Integer start = 56; // Integer | Response is paged. This parameter determines where the response should start.
    try {
      apiInstance.quoteImageFontListGet(start);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageFontListGet");
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
| **start** | **Integer**| Response is paged. This parameter determines where the response should start. | [optional] |

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

<a id="quoteImageFontPost"></a>
# **quoteImageFontPost**
> quoteImageFontPost(font, tags)



Add a font file for use later in creating a quote image. This is essentially a &#x60;PUT&#x60; but not many clients handle PUT with binary stream i.e. a file, gracefully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    File font = new File("/path/to/file"); // File | Font file to add to your collection (ttf/otf are supported)
    String tags = "tags_example"; // String | Optional comma separated tags
    try {
      apiInstance.quoteImageFontPost(font, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageFontPost");
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
| **font** | **File**| Font file to add to your collection (ttf/otf are supported) | |
| **tags** | **String**| Optional comma separated tags | [optional] |

### Return type

null (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="quoteImageFontSearchGet"></a>
# **quoteImageFontSearchGet**
> quoteImageFontSearchGet(query)



Searches for a font with a given tag.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String query = "query_example"; // String | Tag string
    try {
      apiInstance.quoteImageFontSearchGet(query);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageFontSearchGet");
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
| **query** | **String**| Tag string | [optional] |

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

<a id="quoteImageFontTagsAddPost"></a>
# **quoteImageFontTagsAddPost**
> quoteImageFontTagsAddPost(id, tags)



Add a tag to a given font.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Font ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.quoteImageFontTagsAddPost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageFontTagsAddPost");
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
| **id** | **String**| Font ID | |
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

<a id="quoteImageFontTagsRemovePost"></a>
# **quoteImageFontTagsRemovePost**
> quoteImageFontTagsRemovePost(id, tags)



Remove a tag from a given Font.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Font ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.quoteImageFontTagsRemovePost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageFontTagsRemovePost");
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
| **id** | **String**| Font ID | |
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

<a id="quoteImageGet"></a>
# **quoteImageGet**
> quoteImageGet(id, binary)



Gets a Quote image for a given id. Response can be an image file as a binary or a base64 encoded contents wrapped in json. &#x60;TODO&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String id = "id_example"; // String | Quote Image id
    Boolean binary = true; // Boolean | Should the response be a direct file download of the image or a base64 encoded image file wrapped in json?
    try {
      apiInstance.quoteImageGet(id, binary);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageGet");
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
| **id** | **String**| Quote Image id | |
| **binary** | **Boolean**| Should the response be a direct file download of the image or a base64 encoded image file wrapped in json? | [optional] [default to true] |

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

<a id="quoteImagePut"></a>
# **quoteImagePut**
> quoteImagePut(quoteId, bgimageId, bgColor, fontId, textColor, textSize, halign, valign, width, height, branding, includeTransparentLayer)



Create a new quote image for a given quote. Choose background colors/images , choose different font styles and generate a beautiful quote image. Did you just had a feeling of being a god or what?! 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String quoteId = "quoteId_example"; // String | Quote id
    String bgimageId = "theysaidso_default_background_image"; // String | Background Image id ( Will override bgcolor if supplied)
    String bgColor = "bgColor_example"; // String | Background Color(if background image id is not supplied)
    String fontId = "theysaidso_default_font"; // String | Font id
    String textColor = "textColor_example"; // String | Text Color
    String textSize = "textSize_example"; // String | Text/font size
    String halign = "center"; // String | Horizontal text Alignment Value
    String valign = "center"; // String | Vertical text Alignment Value
    Integer width = 56; // Integer | Image Width(By default this takes the width of the background image)
    Integer height = 56; // Integer | Image Height(By default this takes the height of the background image)
    Boolean branding = false; // Boolean | Disable They Said So branding (Only available in certain subscription levels. Ignored in other levels)
    Boolean includeTransparentLayer = true; // Boolean | Should include a transparent layer between the text and the background image? This helps when the background image is bright and obscures the text.
    try {
      apiInstance.quoteImagePut(quoteId, bgimageId, bgColor, fontId, textColor, textSize, halign, valign, width, height, branding, includeTransparentLayer);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImagePut");
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
| **quoteId** | **String**| Quote id | |
| **bgimageId** | **String**| Background Image id ( Will override bgcolor if supplied) | [optional] [default to theysaidso_default_background_image] |
| **bgColor** | **String**| Background Color(if background image id is not supplied) | [optional] |
| **fontId** | **String**| Font id | [optional] [default to theysaidso_default_font] |
| **textColor** | **String**| Text Color | [optional] |
| **textSize** | **String**| Text/font size | [optional] |
| **halign** | **String**| Horizontal text Alignment Value | [optional] [default to center] |
| **valign** | **String**| Vertical text Alignment Value | [optional] [default to center] |
| **width** | **Integer**| Image Width(By default this takes the width of the background image) | [optional] |
| **height** | **Integer**| Image Height(By default this takes the height of the background image) | [optional] |
| **branding** | **Boolean**| Disable They Said So branding (Only available in certain subscription levels. Ignored in other levels) | [optional] [default to false] |
| **includeTransparentLayer** | **Boolean**| Should include a transparent layer between the text and the background image? This helps when the background image is bright and obscures the text. | [optional] [default to true] |

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

<a id="quoteImageSearchGet"></a>
# **quoteImageSearchGet**
> quoteImageSearchGet(category, author, _private)



Gets a Random Quote image. Optional &#x60;category&#x60; param determines the category of quote used in the image. Optional &#x60;author&#x60; param gets the quote image of a given author.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quotes.rest");
    
    // Configure HTTP bearer authorization: BearerAuth
    HttpBearerAuth BearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("BearerAuth");
    BearerAuth.setBearerToken("BEARER TOKEN");

    QuoteImagesApi apiInstance = new QuoteImagesApi(defaultClient);
    String category = "category_example"; // String | Quote Category
    String author = "author_example"; // String | Quote Author
    Boolean _private = false; // Boolean | Should search private collection. Default searches public image collection.
    try {
      apiInstance.quoteImageSearchGet(category, author, _private);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteImagesApi#quoteImageSearchGet");
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
| **_private** | **Boolean**| Should search private collection. Default searches public image collection. | [optional] [default to false] |

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


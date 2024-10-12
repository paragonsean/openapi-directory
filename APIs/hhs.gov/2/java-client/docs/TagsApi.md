# TagsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesTagsFormatGet**](TagsApi.md#resourcesTagsFormatGet) | **GET** /resources/tags.{format} | Get Tags |
| [**resourcesTagsIdFormatGet**](TagsApi.md#resourcesTagsIdFormatGet) | **GET** /resources/tags/{id}.{format} | Get Tag by ID |
| [**resourcesTagsIdMediaFormatGet**](TagsApi.md#resourcesTagsIdMediaFormatGet) | **GET** /resources/tags/{id}/media.{format} | Get MediaItems for Tag |
| [**resourcesTagsIdRelatedFormatGet**](TagsApi.md#resourcesTagsIdRelatedFormatGet) | **GET** /resources/tags/{id}/related.{format} | Get related Tags by ID |
| [**resourcesTagsIdSyndicateFormatGet**](TagsApi.md#resourcesTagsIdSyndicateFormatGet) | **GET** /resources/tags/{id}/syndicate.{format} | Get MediaItems for Tag |
| [**resourcesTagsTagLanguagesFormatGet**](TagsApi.md#resourcesTagsTagLanguagesFormatGet) | **GET** /resources/tags/tagLanguages.{format} | Get TagLanguages |
| [**resourcesTagsTagTypesFormatGet**](TagsApi.md#resourcesTagsTagTypesFormatGet) | **GET** /resources/tags/tagTypes.{format} | Get MediaItems for Tag |


<a id="resourcesTagsFormatGet"></a>
# **resourcesTagsFormatGet**
> List&lt;TagMarshallerWrapped&gt; resourcesTagsFormatGet(format, sort, max, offset, name, nameContains, mediaId, typeId, typeName)

Get Tags

List of Tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String format = "format_example"; // String | Automatically added
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | Return records starting at the offset index.
    String name = "name_example"; // String | Return tags[s] matching the supplied name
    String nameContains = "nameContains_example"; // String | Return tags which contain the supplied partial name.
    Long mediaId = 56L; // Long | Return tags associated with the supplied media id.
    Long typeId = 56L; // Long | Return tags belonging to the supplied tag type id.
    String typeName = "typeName_example"; // String | Return tags belonging to the supplied tag type name.
    try {
      List<TagMarshallerWrapped> result = apiInstance.resourcesTagsFormatGet(format, sort, max, offset, name, nameContains, mediaId, typeId, typeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#resourcesTagsFormatGet");
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
| **format** | **String**| Automatically added | |
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| Return records starting at the offset index. | [optional] |
| **name** | **String**| Return tags[s] matching the supplied name | [optional] |
| **nameContains** | **String**| Return tags which contain the supplied partial name. | [optional] |
| **mediaId** | **Long**| Return tags associated with the supplied media id. | [optional] |
| **typeId** | **Long**| Return tags belonging to the supplied tag type id. | [optional] |
| **typeName** | **String**| Return tags belonging to the supplied tag type name. | [optional] |

### Return type

[**List&lt;TagMarshallerWrapped&gt;**](TagMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of Tags matching the specified query parameters in the specified &#39;format&#39;. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesTagsIdFormatGet"></a>
# **resourcesTagsIdFormatGet**
> List&lt;TagMarshallerWrapped&gt; resourcesTagsIdFormatGet(id, format)

Get Tag by ID

Information about a specific tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | The id of the record to look up
    String format = "format_example"; // String | Automatically added
    try {
      List<TagMarshallerWrapped> result = apiInstance.resourcesTagsIdFormatGet(id, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#resourcesTagsIdFormatGet");
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
| **id** | **Long**| The id of the record to look up | |
| **format** | **String**| Automatically added | |

### Return type

[**List&lt;TagMarshallerWrapped&gt;**](TagMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Tag identified by the &#39;id&#39; in the specified &#39;format&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesTagsIdMediaFormatGet"></a>
# **resourcesTagsIdMediaFormatGet**
> List&lt;MediaItemWrapped&gt; resourcesTagsIdMediaFormatGet(id, format, sort, max, offset)

Get MediaItems for Tag

MediaItem

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | The id of the tag to look up
    String format = "format_example"; // String | Automatically added
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | Return records starting at the offset index.
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesTagsIdMediaFormatGet(id, format, sort, max, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#resourcesTagsIdMediaFormatGet");
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
| **id** | **Long**| The id of the tag to look up | |
| **format** | **String**| Automatically added | |
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| Return records starting at the offset index. | [optional] |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of MediaItems associated with the Tag identified by the &#39;id&#39;. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesTagsIdRelatedFormatGet"></a>
# **resourcesTagsIdRelatedFormatGet**
> List&lt;TagMarshallerWrapped&gt; resourcesTagsIdRelatedFormatGet(id, format, sort, max, offset)

Get related Tags by ID

Information about related tags to a specific tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | The id of the tag to look up
    String format = "format_example"; // String | Automatically added
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | Return records starting at the offset index.
    try {
      List<TagMarshallerWrapped> result = apiInstance.resourcesTagsIdRelatedFormatGet(id, format, sort, max, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#resourcesTagsIdRelatedFormatGet");
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
| **id** | **Long**| The id of the tag to look up | |
| **format** | **String**| Automatically added | |
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| Return records starting at the offset index. | [optional] |

### Return type

[**List&lt;TagMarshallerWrapped&gt;**](TagMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of Tags related to the Tag identified by the &#39;id&#39; in the specified format. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesTagsIdSyndicateFormatGet"></a>
# **resourcesTagsIdSyndicateFormatGet**
> String resourcesTagsIdSyndicateFormatGet(id, format, displayMethod)

Get MediaItems for Tag

MediaItem

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | The id of the record to look up
    String format = "format_example"; // String | Automatically added
    String displayMethod = "displayMethod_example"; // String | Method used to render an html request. Accepts one: [mv, list, feed]
    try {
      String result = apiInstance.resourcesTagsIdSyndicateFormatGet(id, format, displayMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#resourcesTagsIdSyndicateFormatGet");
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
| **id** | **Long**| The id of the record to look up | |
| **format** | **String**| Automatically added | |
| **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Renders the list of MediaItems associated with the Tag identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesTagsTagLanguagesFormatGet"></a>
# **resourcesTagsTagLanguagesFormatGet**
> List&lt;TagLanguageMarshallerWrapped&gt; resourcesTagsTagLanguagesFormatGet(format)

Get TagLanguages

List of Tag Languages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String format = "format_example"; // String | Automatically added
    try {
      List<TagLanguageMarshallerWrapped> result = apiInstance.resourcesTagsTagLanguagesFormatGet(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#resourcesTagsTagLanguagesFormatGet");
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
| **format** | **String**| Automatically added | |

### Return type

[**List&lt;TagLanguageMarshallerWrapped&gt;**](TagLanguageMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of TagLanguages |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesTagsTagTypesFormatGet"></a>
# **resourcesTagsTagTypesFormatGet**
> List&lt;TagTypeMarshallerWrapped&gt; resourcesTagsTagTypesFormatGet(format)

Get MediaItems for Tag

List of Types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String format = "format_example"; // String | Automatically added
    try {
      List<TagTypeMarshallerWrapped> result = apiInstance.resourcesTagsTagTypesFormatGet(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#resourcesTagsTagTypesFormatGet");
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
| **format** | **String**| Automatically added | |

### Return type

[**List&lt;TagTypeMarshallerWrapped&gt;**](TagTypeMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Renders the list of MediaItems associated with the Tag identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |


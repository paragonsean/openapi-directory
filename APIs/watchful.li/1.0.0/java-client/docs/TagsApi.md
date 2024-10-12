# TagsApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTags**](TagsApi.md#createTags) | **POST** /tags | Create a tag |
| [**getSitesByTags**](TagsApi.md#getSitesByTags) | **GET** /tags/{id}/sites | Find sites by tag ID |
| [**getTagById**](TagsApi.md#getTagById) | **GET** /tags/{id} | Find tag by ID |
| [**tagsGet**](TagsApi.md#tagsGet) | **GET** /tags | Get a list of tags |
| [**tagsIdDelete**](TagsApi.md#tagsIdDelete) | **DELETE** /tags/{id} | Delete a specific tag |
| [**tagsMetadataGet**](TagsApi.md#tagsMetadataGet) | **GET** /tags/metadata | Get the list of fields |
| [**updateTag**](TagsApi.md#updateTag) | **PUT** /tags/{id} | Update a tag |


<a id="createTags"></a>
# **createTags**
> Tag createTags(body)

Create a tag

Create a tag

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Tag body = new Tag(); // Tag | JSON object Tag
    try {
      Tag result = apiInstance.createTags(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#createTags");
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
| **body** | [**Tag**](Tag.md)| JSON object Tag | |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Saved successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Not saved |  -  |

<a id="getSitesByTags"></a>
# **getSitesByTags**
> Site getSitesByTags(id, name, accessUrl, jVersion, ip, jUpdate, published, error, nbUpdates, up, fields, limit, limitstart, order)

Find sites by tag ID

Returns a list of sites based with a specific tag id

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | ID of tag that needs to be fetched
    String name = "name_example"; // String | Do a 'LIKE' search, you can also use '%'
    String accessUrl = "accessUrl_example"; // String | Do a 'LIKE' search, you can also use '%'
    String jVersion = "jVersion_example"; // String | Do a 'LIKE' search, you can also use '%'
    String ip = "ip_example"; // String | Do a 'LIKE' search, you can also use '%'
    Integer jUpdate = 1; // Integer | Joomla core update
    Integer published = 1; // Integer | is published
    String error = "error_example"; // String | have errors
    String nbUpdates = "nbUpdates_example"; // String | 
    Integer up = 1; // Integer | is the website online
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    try {
      Site result = apiInstance.getSitesByTags(id, name, accessUrl, jVersion, ip, jUpdate, published, error, nbUpdates, up, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#getSitesByTags");
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
| **id** | **Long**| ID of tag that needs to be fetched | |
| **name** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **accessUrl** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **jVersion** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **ip** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **jUpdate** | **Integer**| Joomla core update | [optional] [enum: 1, 0] |
| **published** | **Integer**| is published | [optional] [enum: 1, 0] |
| **error** | **String**| have errors | [optional] |
| **nbUpdates** | **String**|  | [optional] |
| **up** | **Integer**| is the website online | [optional] [enum: 1, 0] |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] |

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="getTagById"></a>
# **getTagById**
> Tag getTagById(id, fields)

Find tag by ID

Returns a tag based on ID

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | ID of tag that needs to be fetched
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    try {
      Tag result = apiInstance.getTagById(id, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#getTagById");
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
| **id** | **Long**| ID of tag that needs to be fetched | |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **400** | Invalid ID |  -  |
| **403** | Invalid API Key |  -  |

<a id="tagsGet"></a>
# **tagsGet**
> Tag tagsGet(name, type, fields, limit, limitstart, order)

Get a list of tags

Returns a list of tags

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String name = "name_example"; // String | Do a 'LIKE' search, you can also use '%'
    String type = ""; // String | Bootstrap color of the tag
    String fields = "fields_example"; // String | Fields to return separate by comas: name,id
    Long limit = 56L; // Long | Number of object to return (max 100, default 25)
    Long limitstart = 56L; // Long | Start of the return (default 0)
    String order = "order_example"; // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    try {
      Tag result = apiInstance.tagsGet(name, type, fields, limit, limitstart, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsGet");
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
| **name** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] |
| **type** | **String**| Bootstrap color of the tag | [optional] [enum: , default, success, warning, important, info, inverse] |
| **fields** | **String**| Fields to return separate by comas: name,id | [optional] |
| **limit** | **Long**| Number of object to return (max 100, default 25) | [optional] |
| **limitstart** | **Long**| Start of the return (default 0) | [optional] |
| **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |

<a id="tagsIdDelete"></a>
# **tagsIdDelete**
> String tagsIdDelete(id)

Delete a specific tag

Delete a specific tag

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | ID of tag that needs to be deleted
    try {
      String result = apiInstance.tagsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsIdDelete");
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
| **id** | **Long**| ID of tag that needs to be deleted | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag correctly deleted |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="tagsMetadataGet"></a>
# **tagsMetadataGet**
> String tagsMetadataGet()

Get the list of fields

Returns a list of fields

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    TagsApi apiInstance = new TagsApi(defaultClient);
    try {
      String result = apiInstance.tagsMetadataGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#tagsMetadataGet");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="updateTag"></a>
# **updateTag**
> Tag updateTag(id, body)

Update a tag

Update a tag

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    TagsApi apiInstance = new TagsApi(defaultClient);
    Long id = 56L; // Long | ID of tag
    Tag body = new Tag(); // Tag | JSON object of the updated tag
    try {
      Tag result = apiInstance.updateTag(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#updateTag");
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
| **id** | **Long**| ID of tag | |
| **body** | [**Tag**](Tag.md)| JSON object of the updated tag | |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |


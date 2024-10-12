# TagsApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTagGroup**](TagsApi.md#createTagGroup) | **POST** /tag_groups.json | Creates a tag group |
| [**getTag**](TagsApi.md#getTag) | **GET** /tag/{name}.json | Get a specific tag |
| [**getTagGroup**](TagsApi.md#getTagGroup) | **GET** /tag_groups/{id}.json | Get a single tag group |
| [**listTagGroups**](TagsApi.md#listTagGroups) | **GET** /tag_groups.json | Get a list of tag groups |
| [**listTags**](TagsApi.md#listTags) | **GET** /tags.json | Get a list of tags |
| [**updateTagGroup**](TagsApi.md#updateTagGroup) | **PUT** /tag_groups/{id}.json | Update tag group |


<a id="createTagGroup"></a>
# **createTagGroup**
> CreateTagGroup200Response createTagGroup(createTagGroupRequest)

Creates a tag group

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
    defaultClient.setBasePath("http://discourse.local");

    TagsApi apiInstance = new TagsApi(defaultClient);
    CreateTagGroupRequest createTagGroupRequest = new CreateTagGroupRequest(); // CreateTagGroupRequest | 
    try {
      CreateTagGroup200Response result = apiInstance.createTagGroup(createTagGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#createTagGroup");
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
| **createTagGroupRequest** | [**CreateTagGroupRequest**](CreateTagGroupRequest.md)|  | [optional] |

### Return type

[**CreateTagGroup200Response**](CreateTagGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tag group created |  -  |

<a id="getTag"></a>
# **getTag**
> GetTag200Response getTag(name)

Get a specific tag

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
    defaultClient.setBasePath("http://discourse.local");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      GetTag200Response result = apiInstance.getTag(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#getTag");
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
| **name** | **String**|  | |

### Return type

[**GetTag200Response**](GetTag200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | notifications |  -  |

<a id="getTagGroup"></a>
# **getTagGroup**
> GetTagGroup200Response getTagGroup(id)

Get a single tag group

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
    defaultClient.setBasePath("http://discourse.local");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      GetTagGroup200Response result = apiInstance.getTagGroup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#getTagGroup");
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
| **id** | **String**|  | |

### Return type

[**GetTagGroup200Response**](GetTagGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | notifications |  -  |

<a id="listTagGroups"></a>
# **listTagGroups**
> ListTagGroups200Response listTagGroups()

Get a list of tag groups

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
    defaultClient.setBasePath("http://discourse.local");

    TagsApi apiInstance = new TagsApi(defaultClient);
    try {
      ListTagGroups200Response result = apiInstance.listTagGroups();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#listTagGroups");
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

[**ListTagGroups200Response**](ListTagGroups200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tags |  -  |

<a id="listTags"></a>
# **listTags**
> ListTags200Response listTags()

Get a list of tags

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
    defaultClient.setBasePath("http://discourse.local");

    TagsApi apiInstance = new TagsApi(defaultClient);
    try {
      ListTags200Response result = apiInstance.listTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#listTags");
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

[**ListTags200Response**](ListTags200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | notifications |  -  |

<a id="updateTagGroup"></a>
# **updateTagGroup**
> UpdateTagGroup200Response updateTagGroup(id, updateTagGroupRequest)

Update tag group

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
    defaultClient.setBasePath("http://discourse.local");

    TagsApi apiInstance = new TagsApi(defaultClient);
    String id = "id_example"; // String | 
    UpdateTagGroupRequest updateTagGroupRequest = new UpdateTagGroupRequest(); // UpdateTagGroupRequest | 
    try {
      UpdateTagGroup200Response result = apiInstance.updateTagGroup(id, updateTagGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApi#updateTagGroup");
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
| **id** | **String**|  | |
| **updateTagGroupRequest** | [**UpdateTagGroupRequest**](UpdateTagGroupRequest.md)|  | [optional] |

### Return type

[**UpdateTagGroup200Response**](UpdateTagGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tag group updated |  -  |


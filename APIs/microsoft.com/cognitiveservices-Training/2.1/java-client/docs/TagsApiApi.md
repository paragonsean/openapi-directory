# TagsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v2.1/Training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTag**](TagsApiApi.md#createTag) | **POST** /projects/{projectId}/tags | Create a tag for the project |
| [**deleteTag**](TagsApiApi.md#deleteTag) | **DELETE** /projects/{projectId}/tags/{tagId} | Delete a tag from the project |
| [**getTag**](TagsApiApi.md#getTag) | **GET** /projects/{projectId}/tags/{tagId} | Get information about a specific tag |
| [**getTags**](TagsApiApi.md#getTags) | **GET** /projects/{projectId}/tags | Get the tags for a given project and iteration |
| [**updateTag**](TagsApiApi.md#updateTag) | **PATCH** /projects/{projectId}/tags/{tagId} | Update a tag |


<a id="createTag"></a>
# **createTag**
> Tag createTag(projectId, name, trainingKey, description)

Create a tag for the project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v2.1/Training");

    TagsApiApi apiInstance = new TagsApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    String name = "Tag1"; // String | The tag name
    String trainingKey = "{API Key}"; // String | 
    String description = "Description of Tag1"; // String | Optional description for the tag
    try {
      Tag result = apiInstance.createTag(projectId, name, trainingKey, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApiApi#createTag");
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
| **projectId** | **UUID**| The project id | |
| **name** | **String**| The tag name | |
| **trainingKey** | **String**|  | |
| **description** | **String**| Optional description for the tag | [optional] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteTag"></a>
# **deleteTag**
> deleteTag(projectId, tagId, trainingKey)

Delete a tag from the project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v2.1/Training");

    TagsApiApi apiInstance = new TagsApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    UUID tagId = UUID.fromString("9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"); // UUID | Id of the tag to be deleted
    String trainingKey = "{API Key}"; // String | 
    try {
      apiInstance.deleteTag(projectId, tagId, trainingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApiApi#deleteTag");
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
| **projectId** | **UUID**| The project id | |
| **tagId** | **UUID**| Id of the tag to be deleted | |
| **trainingKey** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="getTag"></a>
# **getTag**
> Tag getTag(projectId, tagId, trainingKey, iterationId)

Get information about a specific tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v2.1/Training");

    TagsApiApi apiInstance = new TagsApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project this tag belongs to
    UUID tagId = UUID.fromString("9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"); // UUID | The tag id
    String trainingKey = "{API Key}"; // String | 
    UUID iterationId = UUID.randomUUID(); // UUID | The iteration to retrieve this tag from. Optional, defaults to current training set
    try {
      Tag result = apiInstance.getTag(projectId, tagId, trainingKey, iterationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApiApi#getTag");
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
| **projectId** | **UUID**| The project this tag belongs to | |
| **tagId** | **UUID**| The tag id | |
| **trainingKey** | **String**|  | |
| **iterationId** | **UUID**| The iteration to retrieve this tag from. Optional, defaults to current training set | [optional] |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getTags"></a>
# **getTags**
> List&lt;Tag&gt; getTags(projectId, trainingKey, iterationId)

Get the tags for a given project and iteration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v2.1/Training");

    TagsApiApi apiInstance = new TagsApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    String trainingKey = "{API Key}"; // String | 
    UUID iterationId = UUID.randomUUID(); // UUID | The iteration id. Defaults to workspace
    try {
      List<Tag> result = apiInstance.getTags(projectId, trainingKey, iterationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApiApi#getTags");
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
| **projectId** | **UUID**| The project id | |
| **trainingKey** | **String**|  | |
| **iterationId** | **UUID**| The iteration id. Defaults to workspace | [optional] |

### Return type

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTag"></a>
# **updateTag**
> Tag updateTag(projectId, tagId, trainingKey, tag)

Update a tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TagsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v2.1/Training");

    TagsApiApi apiInstance = new TagsApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    UUID tagId = UUID.fromString("9e27bc1b-7ae7-4e3b-a4e5-36153479dc01"); // UUID | The id of the target tag
    String trainingKey = "{API Key}"; // String | 
    Tag tag = new Tag(); // Tag | The updated tag model
    try {
      Tag result = apiInstance.updateTag(projectId, tagId, trainingKey, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TagsApiApi#updateTag");
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
| **projectId** | **UUID**| The project id | |
| **tagId** | **UUID**| The id of the target tag | |
| **trainingKey** | **String**|  | |
| **tag** | [**Tag**](Tag.md)| The updated tag model | |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


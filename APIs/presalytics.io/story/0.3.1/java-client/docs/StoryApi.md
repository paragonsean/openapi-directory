# StoryApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storyGet**](StoryApi.md#storyGet) | **GET** / | Story: Get List of User Stories |
| [**storyIdAnalytics**](StoryApi.md#storyIdAnalytics) | **GET** /{id}/analytics | Story: View Analytics |
| [**storyIdDelete**](StoryApi.md#storyIdDelete) | **DELETE** /{id} | Story: Delete by Id |
| [**storyIdFileOoxmlautomationidDelete**](StoryApi.md#storyIdFileOoxmlautomationidDelete) | **DELETE** /{id}/file/{ooxml_automation_id} | Story: Delete Subdocument |
| [**storyIdFileOoxmlautomationidGet**](StoryApi.md#storyIdFileOoxmlautomationidGet) | **GET** /{id}/file/{ooxml_automation_id} | Story: Download Updated File |
| [**storyIdFilePost**](StoryApi.md#storyIdFilePost) | **POST** /{id}/file | Story: Upload a File To Existing Story |
| [**storyIdGet**](StoryApi.md#storyIdGet) | **GET** /{id} | Story: Get by Id |
| [**storyIdOutlineGet**](StoryApi.md#storyIdOutlineGet) | **GET** /{id}/outline | Story: Get Story Outline |
| [**storyIdOutlinePost**](StoryApi.md#storyIdOutlinePost) | **POST** /{id}/outline | Story: Post Story Outline |
| [**storyIdPublic**](StoryApi.md#storyIdPublic) | **GET** /{id}/public/ | Story: Public Link to Story Reveal.js Document |
| [**storyIdPut**](StoryApi.md#storyIdPut) | **PUT** /{id} | Story: Modify |
| [**storyIdReveal**](StoryApi.md#storyIdReveal) | **GET** /{id}/reveal | Story: Get Story at Reveal.js Document |
| [**storyIdStatusGet**](StoryApi.md#storyIdStatusGet) | **GET** /{id}/status | Story: Get Story Status |
| [**storyPost**](StoryApi.md#storyPost) | **POST** / | Story: Upload |
| [**storyPostFile**](StoryApi.md#storyPostFile) | **POST** /file | Story: Upload a File |
| [**storyPostFileJson**](StoryApi.md#storyPostFileJson) | **POST** /file/json | Story: Upload a File (base64) |


<a id="storyGet"></a>
# **storyGet**
> List&lt;Story&gt; storyGet(includeRelationships, includeOutline)

Story: Get List of User Stories

Returns a list of stories for this user identifie via the access token presentated to the api

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    Boolean includeRelationships = true; // Boolean | Indicate whether the returned object should include child relationships
    Boolean includeOutline = true; // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    try {
      List<Story> result = apiInstance.storyGet(includeRelationships, includeOutline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyGet");
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
| **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] |
| **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] |

### Return type

[**List&lt;Story&gt;**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of stories for this user |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdAnalytics"></a>
# **storyIdAnalytics**
> String storyIdAnalytics(id)

Story: View Analytics

returns an html document containing session and event metrics for the story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      String result = apiInstance.storyIdAnalytics(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdAnalytics");
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
| **id** | **UUID**| the id from the story object | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An html document containing session analytics for the story |  -  |
| **400** | Bad Request |  -  |
| **401** | An html document containing a login button |  -  |
| **404** | Not found |  -  |

<a id="storyIdDelete"></a>
# **storyIdDelete**
> storyIdDelete(id)

Story: Delete by Id

Remove a story and dependant data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      apiInstance.storyIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdDelete");
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
| **id** | **UUID**| the id from the story object | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdFileOoxmlautomationidDelete"></a>
# **storyIdFileOoxmlautomationidDelete**
> storyIdFileOoxmlautomationidDelete(id, ooxmlAutomationId)

Story: Delete Subdocument

Deletes a subdcoument of this story (e.g., .pptx, .docx, .xlsx)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    UUID ooxmlAutomationId = UUID.randomUUID(); // UUID | the id of the ooxml_automation object
    try {
      apiInstance.storyIdFileOoxmlautomationidDelete(id, ooxmlAutomationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdFileOoxmlautomationidDelete");
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
| **id** | **UUID**| the id from the story object | |
| **ooxmlAutomationId** | **UUID**| the id of the ooxml_automation object | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdFileOoxmlautomationidGet"></a>
# **storyIdFileOoxmlautomationidGet**
> File storyIdFileOoxmlautomationidGet(id, ooxmlAutomationId)

Story: Download Updated File

Redtreives updated story as open office xml file (e.g., .pptx, .docx, .xlsx)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    UUID ooxmlAutomationId = UUID.randomUUID(); // UUID | the id of the ooxml_automation object
    try {
      File result = apiInstance.storyIdFileOoxmlautomationidGet(id, ooxmlAutomationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdFileOoxmlautomationidGet");
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
| **id** | **UUID**| the id from the story object | |
| **ooxmlAutomationId** | **UUID**| the id of the ooxml_automation object | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The latest versiono of the story, in its orginal file format |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdFilePost"></a>
# **storyIdFilePost**
> Story storyIdFilePost(id, replaceExisting, obsoleteId, includeOutline, _file)

Story: Upload a File To Existing Story

Upload a file to an existing story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    Boolean replaceExisting = true; // Boolean | Indicates whether a put or post method would replace the existing contents
    UUID obsoleteId = UUID.randomUUID(); // UUID | A primary key pointing to an obsolete item in the story. Item type is context-dependent
    Boolean includeOutline = true; // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    List<File> _file = Arrays.asList(); // List<File> | 
    try {
      Story result = apiInstance.storyIdFilePost(id, replaceExisting, obsoleteId, includeOutline, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdFilePost");
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
| **id** | **UUID**| the id from the story object | |
| **replaceExisting** | **Boolean**| Indicates whether a put or post method would replace the existing contents | [optional] |
| **obsoleteId** | **UUID**| A primary key pointing to an obsolete item in the story. Item type is context-dependent | [optional] |
| **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] |
| **_file** | **List&lt;File&gt;**|  | [optional] |

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success responses with story object |  -  |
| **415** | Unsupported Media Type |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="storyIdGet"></a>
# **storyIdGet**
> Story storyIdGet(id, includeRelationships, includeOutline, full, refreshCache)

Story: Get by Id

Returns story metadata, inlcuding json object with story outline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    Boolean includeRelationships = true; // Boolean | Indicate whether the returned object should include child relationships
    Boolean includeOutline = true; // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    Boolean full = true; // Boolean | Pull a story object with associated collaborator user, permission, and session data(faster if cached from prior api call)
    Boolean refreshCache = true; // Boolean | Force the api reload the `Story full` object
    try {
      Story result = apiInstance.storyIdGet(id, includeRelationships, includeOutline, full, refreshCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdGet");
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
| **id** | **UUID**| the id from the story object | |
| **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] |
| **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] |
| **full** | **Boolean**| Pull a story object with associated collaborator user, permission, and session data(faster if cached from prior api call) | [optional] |
| **refreshCache** | **Boolean**| Force the api reload the &#x60;Story full&#x60; object | [optional] |

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success responses with story object |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdOutlineGet"></a>
# **storyIdOutlineGet**
> String storyIdOutlineGet(id)

Story: Get Story Outline

Returns Story&#39;s outline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      String result = apiInstance.storyIdOutlineGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdOutlineGet");
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
| **id** | **UUID**| the id from the story object | |

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
| **200** | Stringified Story outline |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **410** | Gone |  -  |

<a id="storyIdOutlinePost"></a>
# **storyIdOutlinePost**
> storyIdOutlinePost(id, body)

Story: Post Story Outline

Update a story outline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    String body = "body_example"; // String | A story outline object
    try {
      apiInstance.storyIdOutlinePost(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdOutlinePost");
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
| **id** | **UUID**| the id from the story object | |
| **body** | **String**| A story outline object | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdPublic"></a>
# **storyIdPublic**
> String storyIdPublic(id)

Story: Public Link to Story Reveal.js Document

returns an html document containing a reveal.js epresentation of the story, if the story if set to is_public &#x3D; True

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      String result = apiInstance.storyIdPublic(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdPublic");
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
| **id** | **UUID**| the id from the story object | |

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
| **200** | An html document containing a reveal.js represenation of the story |  -  |
| **302** | Not Found redirect |  -  |
| **400** | Bad Request |  -  |

<a id="storyIdPut"></a>
# **storyIdPut**
> Story storyIdPut(id, story, includeOutline)

Story: Modify

Update story metadata, including story outline

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    Story story = new Story(); // Story | The updated story object
    Boolean includeOutline = true; // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    try {
      Story result = apiInstance.storyIdPut(id, story, includeOutline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdPut");
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
| **id** | **UUID**| the id from the story object | |
| **story** | [**Story**](Story.md)| The updated story object | |
| **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] |

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success responses with story object |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdReveal"></a>
# **storyIdReveal**
> String storyIdReveal(id)

Story: Get Story at Reveal.js Document

returns an html document containing a reveal.js epresentation of the story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      String result = apiInstance.storyIdReveal(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdReveal");
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
| **id** | **UUID**| the id from the story object | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An html document containing a reveal.js represenation of the story |  -  |
| **400** | Bad Request |  -  |
| **401** | An html document containing a login button |  -  |
| **404** | Not found |  -  |

<a id="storyIdStatusGet"></a>
# **storyIdStatusGet**
> Status storyIdStatusGet(id)

Story: Get Story Status

Returns code indicating whether story has active running background and is healthy (e.g., the latest outline is valid)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      Status result = apiInstance.storyIdStatusGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyIdStatusGet");
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
| **id** | **UUID**| the id from the story object | |

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accepted |  -  |
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyPost"></a>
# **storyPost**
> Story storyPost(outline, includeOutline)

Story: Upload

Upload new story to presalytics api

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    Outline outline = new Outline(); // Outline | A story outline json object
    Boolean includeOutline = true; // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    try {
      Story result = apiInstance.storyPost(outline, includeOutline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyPost");
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
| **outline** | [**Outline**](Outline.md)| A story outline json object | |
| **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] |

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success responses with story object |  -  |
| **415** | Unsupported Media Type |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="storyPostFile"></a>
# **storyPostFile**
> Story storyPostFile(includeOutline, _file)

Story: Upload a File

Upload new story to presalytics api via an Open Office Xml file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    Boolean includeOutline = true; // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    List<File> _file = Arrays.asList(); // List<File> | 
    try {
      Story result = apiInstance.storyPostFile(includeOutline, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyPostFile");
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
| **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] |
| **_file** | **List&lt;File&gt;**|  | [optional] |

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success responses with story object |  -  |
| **415** | Unsupported Media Type |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="storyPostFileJson"></a>
# **storyPostFileJson**
> Story storyPostFileJson(includeOutline, fileUpload)

Story: Upload a File (base64)

Upload new story to presalytics api via an Open Office Xml file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryApi apiInstance = new StoryApi(defaultClient);
    Boolean includeOutline = true; // Boolean | Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times.
    FileUpload fileUpload = new FileUpload(); // FileUpload | A json-formatted object that includes a base64 encoded file (file encoded utf-8)
    try {
      Story result = apiInstance.storyPostFileJson(includeOutline, fileUpload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryApi#storyPostFileJson");
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
| **includeOutline** | **Boolean**| Determines whether a repsonse including story objects should include the story outline.  Defaults to true. Useful for speeding up processing times. | [optional] |
| **fileUpload** | [**FileUpload**](FileUpload.md)| A json-formatted object that includes a base64 encoded file (file encoded utf-8) | [optional] |

### Return type

[**Story**](Story.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success responses with story object |  -  |
| **415** | Unsupported Media Type |  -  |
| **422** | Unprocessable Entity |  -  |


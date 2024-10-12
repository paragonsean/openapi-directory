# BehaviorsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**behaviorListForPath**](BehaviorsApi.md#behaviorListForPath) | **GET** /behaviors/folders/{path} | List Behaviors by path |
| [**deleteBehaviorsId**](BehaviorsApi.md#deleteBehaviorsId) | **DELETE** /behaviors/{id} | Delete Behavior |
| [**getBehaviors**](BehaviorsApi.md#getBehaviors) | **GET** /behaviors | List Behaviors |
| [**getBehaviorsId**](BehaviorsApi.md#getBehaviorsId) | **GET** /behaviors/{id} | Show Behavior |
| [**patchBehaviorsId**](BehaviorsApi.md#patchBehaviorsId) | **PATCH** /behaviors/{id} | Update Behavior |
| [**postBehaviors**](BehaviorsApi.md#postBehaviors) | **POST** /behaviors | Create Behavior |
| [**postBehaviorsWebhookTest**](BehaviorsApi.md#postBehaviorsWebhookTest) | **POST** /behaviors/webhook/test | Test webhook. |


<a id="behaviorListForPath"></a>
# **behaviorListForPath**
> List&lt;BehaviorEntity&gt; behaviorListForPath(path, cursor, perPage, sortBy, filter, filterPrefix, recursive, behavior)

List Behaviors by path

List Behaviors by path

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BehaviorsApi apiInstance = new BehaviorsApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[behavior]=desc`). Valid fields are `behavior`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `behavior`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `behavior`.
    String recursive = "recursive_example"; // String | Show behaviors above this path?
    String behavior = "behavior_example"; // String | DEPRECATED: If set only shows folder behaviors matching this behavior type. Use `filter[behavior]` instead.
    try {
      List<BehaviorEntity> result = apiInstance.behaviorListForPath(path, cursor, perPage, sortBy, filter, filterPrefix, recursive, behavior);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorsApi#behaviorListForPath");
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
| **path** | **String**| Path to operate on. | |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[behavior]&#x3D;desc&#x60;). Valid fields are &#x60;behavior&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] |
| **recursive** | **String**| Show behaviors above this path? | [optional] |
| **behavior** | **String**| DEPRECATED: If set only shows folder behaviors matching this behavior type. Use &#x60;filter[behavior]&#x60; instead. | [optional] |

### Return type

[**List&lt;BehaviorEntity&gt;**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Behaviors objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="deleteBehaviorsId"></a>
# **deleteBehaviorsId**
> deleteBehaviorsId(id)

Delete Behavior

Delete Behavior

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BehaviorsApi apiInstance = new BehaviorsApi(defaultClient);
    Integer id = 56; // Integer | Behavior ID.
    try {
      apiInstance.deleteBehaviorsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorsApi#deleteBehaviorsId");
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
| **id** | **Integer**| Behavior ID. | |

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
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getBehaviors"></a>
# **getBehaviors**
> List&lt;BehaviorEntity&gt; getBehaviors(cursor, perPage, sortBy, behavior, filter, filterPrefix)

List Behaviors

List Behaviors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BehaviorsApi apiInstance = new BehaviorsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[behavior]=desc`). Valid fields are `behavior`.
    String behavior = "behavior_example"; // String | If set, return records where the specified field is equal to the supplied value.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `behavior`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `behavior`.
    try {
      List<BehaviorEntity> result = apiInstance.getBehaviors(cursor, perPage, sortBy, behavior, filter, filterPrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorsApi#getBehaviors");
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
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[behavior]&#x3D;desc&#x60;). Valid fields are &#x60;behavior&#x60;. | [optional] |
| **behavior** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;behavior&#x60;. | [optional] |

### Return type

[**List&lt;BehaviorEntity&gt;**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Behaviors objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getBehaviorsId"></a>
# **getBehaviorsId**
> BehaviorEntity getBehaviorsId(id)

Show Behavior

Show Behavior

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BehaviorsApi apiInstance = new BehaviorsApi(defaultClient);
    Integer id = 56; // Integer | Behavior ID.
    try {
      BehaviorEntity result = apiInstance.getBehaviorsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorsApi#getBehaviorsId");
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
| **id** | **Integer**| Behavior ID. | |

### Return type

[**BehaviorEntity**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Behaviors object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="patchBehaviorsId"></a>
# **patchBehaviorsId**
> BehaviorEntity patchBehaviorsId(id, attachmentDelete, attachmentFile, behavior, description, name, path, value)

Update Behavior

Update Behavior

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BehaviorsApi apiInstance = new BehaviorsApi(defaultClient);
    Integer id = 56; // Integer | Behavior ID.
    Boolean attachmentDelete = true; // Boolean | If true, will delete the file stored in attachment
    File attachmentFile = new File("/path/to/file"); // File | Certain behaviors may require a file, for instance, the \\\"watermark\\\" behavior requires a watermark image
    String behavior = "behavior_example"; // String | Behavior type.
    String description = "description_example"; // String | Description for this behavior.
    String name = "name_example"; // String | Name for this behavior.
    String path = "path_example"; // String | Folder behaviors path.
    String value = "value_example"; // String | The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior.
    try {
      BehaviorEntity result = apiInstance.patchBehaviorsId(id, attachmentDelete, attachmentFile, behavior, description, name, path, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorsApi#patchBehaviorsId");
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
| **id** | **Integer**| Behavior ID. | |
| **attachmentDelete** | **Boolean**| If true, will delete the file stored in attachment | [optional] |
| **attachmentFile** | **File**| Certain behaviors may require a file, for instance, the \\\&quot;watermark\\\&quot; behavior requires a watermark image | [optional] |
| **behavior** | **String**| Behavior type. | [optional] |
| **description** | **String**| Description for this behavior. | [optional] |
| **name** | **String**| Name for this behavior. | [optional] |
| **path** | **String**| Folder behaviors path. | [optional] |
| **value** | **String**| The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior. | [optional] |

### Return type

[**BehaviorEntity**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Behaviors object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postBehaviors"></a>
# **postBehaviors**
> BehaviorEntity postBehaviors(behavior, path, attachmentFile, description, name, value)

Create Behavior

Create Behavior

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BehaviorsApi apiInstance = new BehaviorsApi(defaultClient);
    String behavior = "behavior_example"; // String | Behavior type.
    String path = "path_example"; // String | Folder behaviors path.
    File attachmentFile = new File("/path/to/file"); // File | Certain behaviors may require a file, for instance, the \\\"watermark\\\" behavior requires a watermark image
    String description = "description_example"; // String | Description for this behavior.
    String name = "name_example"; // String | Name for this behavior.
    String value = "value_example"; // String | The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior.
    try {
      BehaviorEntity result = apiInstance.postBehaviors(behavior, path, attachmentFile, description, name, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorsApi#postBehaviors");
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
| **behavior** | **String**| Behavior type. | |
| **path** | **String**| Folder behaviors path. | |
| **attachmentFile** | **File**| Certain behaviors may require a file, for instance, the \\\&quot;watermark\\\&quot; behavior requires a watermark image | [optional] |
| **description** | **String**| Description for this behavior. | [optional] |
| **name** | **String**| Name for this behavior. | [optional] |
| **value** | **String**| The value of the folder behavior.  Can be a integer, array, or hash depending on the type of folder behavior. See The Behavior Types section for example values for each type of behavior. | [optional] |

### Return type

[**BehaviorEntity**](BehaviorEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Behaviors object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postBehaviorsWebhookTest"></a>
# **postBehaviorsWebhookTest**
> StatusEntity postBehaviorsWebhookTest(url, action, body, encoding, headers, method)

Test webhook.

Test webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BehaviorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BehaviorsApi apiInstance = new BehaviorsApi(defaultClient);
    String url = "url_example"; // String | URL for testing the webhook.
    String action = "action_example"; // String | action for test body
    Object body = null; // Object | Additional body parameters.
    String encoding = "encoding_example"; // String | HTTP encoding method.  Can be JSON, XML, or RAW (form data).
    Object headers = null; // Object | Additional request headers.
    String method = "method_example"; // String | HTTP method(GET or POST).
    try {
      StatusEntity result = apiInstance.postBehaviorsWebhookTest(url, action, body, encoding, headers, method);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BehaviorsApi#postBehaviorsWebhookTest");
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
| **url** | **String**| URL for testing the webhook. | |
| **action** | **String**| action for test body | [optional] |
| **body** | [**Object**](Object.md)| Additional body parameters. | [optional] |
| **encoding** | **String**| HTTP encoding method.  Can be JSON, XML, or RAW (form data). | [optional] |
| **headers** | [**Object**](Object.md)| Additional request headers. | [optional] |
| **method** | **String**| HTTP method(GET or POST). | [optional] |

### Return type

[**StatusEntity**](StatusEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Behaviors object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |


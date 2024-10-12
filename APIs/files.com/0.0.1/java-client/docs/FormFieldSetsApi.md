# FormFieldSetsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFormFieldSetsId**](FormFieldSetsApi.md#deleteFormFieldSetsId) | **DELETE** /form_field_sets/{id} | Delete Form Field Set |
| [**getFormFieldSets**](FormFieldSetsApi.md#getFormFieldSets) | **GET** /form_field_sets | List Form Field Sets |
| [**getFormFieldSetsId**](FormFieldSetsApi.md#getFormFieldSetsId) | **GET** /form_field_sets/{id} | Show Form Field Set |
| [**patchFormFieldSetsId**](FormFieldSetsApi.md#patchFormFieldSetsId) | **PATCH** /form_field_sets/{id} | Update Form Field Set |
| [**postFormFieldSets**](FormFieldSetsApi.md#postFormFieldSets) | **POST** /form_field_sets | Create Form Field Set |


<a id="deleteFormFieldSetsId"></a>
# **deleteFormFieldSetsId**
> deleteFormFieldSetsId(id)

Delete Form Field Set

Delete Form Field Set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FormFieldSetsApi apiInstance = new FormFieldSetsApi(defaultClient);
    Integer id = 56; // Integer | Form Field Set ID.
    try {
      apiInstance.deleteFormFieldSetsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldSetsApi#deleteFormFieldSetsId");
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
| **id** | **Integer**| Form Field Set ID. | |

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

<a id="getFormFieldSets"></a>
# **getFormFieldSets**
> List&lt;FormFieldSetEntity&gt; getFormFieldSets(userId, cursor, perPage)

List Form Field Sets

List Form Field Sets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FormFieldSetsApi apiInstance = new FormFieldSetsApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<FormFieldSetEntity> result = apiInstance.getFormFieldSets(userId, cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldSetsApi#getFormFieldSets");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;FormFieldSetEntity&gt;**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of FormFieldSets objects. |  -  |
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

<a id="getFormFieldSetsId"></a>
# **getFormFieldSetsId**
> FormFieldSetEntity getFormFieldSetsId(id)

Show Form Field Set

Show Form Field Set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FormFieldSetsApi apiInstance = new FormFieldSetsApi(defaultClient);
    Integer id = 56; // Integer | Form Field Set ID.
    try {
      FormFieldSetEntity result = apiInstance.getFormFieldSetsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldSetsApi#getFormFieldSetsId");
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
| **id** | **Integer**| Form Field Set ID. | |

### Return type

[**FormFieldSetEntity**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The FormFieldSets object. |  -  |
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

<a id="patchFormFieldSetsId"></a>
# **patchFormFieldSetsId**
> FormFieldSetEntity patchFormFieldSetsId(id, patchFormFieldSets)

Update Form Field Set

Update Form Field Set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FormFieldSetsApi apiInstance = new FormFieldSetsApi(defaultClient);
    Integer id = 56; // Integer | Form Field Set ID.
    PatchFormFieldSets patchFormFieldSets = new PatchFormFieldSets(); // PatchFormFieldSets | 
    try {
      FormFieldSetEntity result = apiInstance.patchFormFieldSetsId(id, patchFormFieldSets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldSetsApi#patchFormFieldSetsId");
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
| **id** | **Integer**| Form Field Set ID. | |
| **patchFormFieldSets** | [**PatchFormFieldSets**](PatchFormFieldSets.md)|  | |

### Return type

[**FormFieldSetEntity**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The FormFieldSets object. |  -  |
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

<a id="postFormFieldSets"></a>
# **postFormFieldSets**
> FormFieldSetEntity postFormFieldSets(postFormFieldSets)

Create Form Field Set

Create Form Field Set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormFieldSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FormFieldSetsApi apiInstance = new FormFieldSetsApi(defaultClient);
    PostFormFieldSets postFormFieldSets = new PostFormFieldSets(); // PostFormFieldSets | 
    try {
      FormFieldSetEntity result = apiInstance.postFormFieldSets(postFormFieldSets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormFieldSetsApi#postFormFieldSets");
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
| **postFormFieldSets** | [**PostFormFieldSets**](PostFormFieldSets.md)|  | |

### Return type

[**FormFieldSetEntity**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The FormFieldSets object. |  -  |
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


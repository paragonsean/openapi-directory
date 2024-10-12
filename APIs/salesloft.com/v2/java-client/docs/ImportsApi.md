# ImportsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ImportsIdJsonDelete**](ImportsApi.md#v2ImportsIdJsonDelete) | **DELETE** /v2/imports/{id}.json | Delete an import |
| [**v2ImportsIdJsonGet**](ImportsApi.md#v2ImportsIdJsonGet) | **GET** /v2/imports/{id}.json | Fetch an import |
| [**v2ImportsIdJsonPut**](ImportsApi.md#v2ImportsIdJsonPut) | **PUT** /v2/imports/{id}.json | Update an import |
| [**v2ImportsJsonGet**](ImportsApi.md#v2ImportsJsonGet) | **GET** /v2/imports.json | List imports |
| [**v2ImportsJsonPost**](ImportsApi.md#v2ImportsJsonPost) | **POST** /v2/imports.json | Create an import |


<a id="v2ImportsIdJsonDelete"></a>
# **v2ImportsIdJsonDelete**
> v2ImportsIdJsonDelete(id, undo)

Delete an import

Deletes an import, by ID only. The associated people can be deleted as part of the deletion process.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String id = "id_example"; // String | Import ID
    String undo = "undo_example"; // String | Whether to delete people on this Import. Possible values are: [not present], all, single.  'single' will delete people who are only present in this Import. 'all' will delete people even if they are present in other Imports. Not specifying this parameter will not delete any people 
    try {
      apiInstance.v2ImportsIdJsonDelete(id, undo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#v2ImportsIdJsonDelete");
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
| **id** | **String**| Import ID | |
| **undo** | **String**| Whether to delete people on this Import. Possible values are: [not present], all, single.  &#39;single&#39; will delete people who are only present in this Import. &#39;all&#39; will delete people even if they are present in other Imports. Not specifying this parameter will not delete any people  | [optional] |

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
| **204** | The import has been deleted successfully |  -  |

<a id="v2ImportsIdJsonGet"></a>
# **v2ImportsIdJsonGet**
> ModelImport v2ImportsIdJsonGet(id)

Fetch an import

Fetches an import, by ID only.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String id = "id_example"; // String | Import ID
    try {
      ModelImport result = apiInstance.v2ImportsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#v2ImportsIdJsonGet");
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
| **id** | **String**| Import ID | |

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ImportsIdJsonPut"></a>
# **v2ImportsIdJsonPut**
> ModelImport v2ImportsIdJsonPut(id, name, userId)

Update an import

Updates an import, by ID only.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String id = "id_example"; // String | Import ID
    String name = "name_example"; // String | Name, recommended to be easily identifiable to a user
    Integer userId = 56; // Integer | ID of the User that owns this Import
    try {
      ModelImport result = apiInstance.v2ImportsIdJsonPut(id, name, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#v2ImportsIdJsonPut");
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
| **id** | **String**| Import ID | |
| **name** | **String**| Name, recommended to be easily identifiable to a user | [optional] |
| **userId** | **Integer**| ID of the User that owns this Import | [optional] |

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ImportsJsonGet"></a>
# **v2ImportsJsonGet**
> List&lt;ModelImport&gt; v2ImportsJsonGet(ids, userIds, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List imports

Fetches multiple imports. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of imports to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<Integer> userIds = Arrays.asList(); // List<Integer> | ID of users to fetch imports for. Using this filter will return an empty array for non-admin users who request other user's imports
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to created_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<ModelImport> result = apiInstance.v2ImportsJsonGet(ids, userIds, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#v2ImportsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of imports to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **userIds** | [**List&lt;Integer&gt;**](Integer.md)| ID of users to fetch imports for. Using this filter will return an empty array for non-admin users who request other user&#39;s imports | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to created_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;ModelImport&gt;**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2ImportsJsonPost"></a>
# **v2ImportsJsonPost**
> ModelImport v2ImportsJsonPost(name, userId)

Create an import

Creates an import. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String name = "name_example"; // String | Name, recommended to be easily identifiable to a user
    Integer userId = 56; // Integer | ID of the User that owns this Import
    try {
      ModelImport result = apiInstance.v2ImportsJsonPost(name, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#v2ImportsJsonPost");
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
| **name** | **String**| Name, recommended to be easily identifiable to a user | [optional] |
| **userId** | **Integer**| ID of the User that owns this Import | [optional] |

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


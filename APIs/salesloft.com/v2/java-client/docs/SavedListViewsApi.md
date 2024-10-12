# SavedListViewsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2SavedListViewsIdJsonDelete**](SavedListViewsApi.md#v2SavedListViewsIdJsonDelete) | **DELETE** /v2/saved_list_views/{id}.json | Delete a saved list view |
| [**v2SavedListViewsIdJsonGet**](SavedListViewsApi.md#v2SavedListViewsIdJsonGet) | **GET** /v2/saved_list_views/{id}.json | Fetch a saved list view |
| [**v2SavedListViewsIdJsonPut**](SavedListViewsApi.md#v2SavedListViewsIdJsonPut) | **PUT** /v2/saved_list_views/{id}.json | Update a saved list view |
| [**v2SavedListViewsJsonGet**](SavedListViewsApi.md#v2SavedListViewsJsonGet) | **GET** /v2/saved_list_views.json | List saved list views |
| [**v2SavedListViewsJsonPost**](SavedListViewsApi.md#v2SavedListViewsJsonPost) | **POST** /v2/saved_list_views.json | Create a saved list view |


<a id="v2SavedListViewsIdJsonDelete"></a>
# **v2SavedListViewsIdJsonDelete**
> v2SavedListViewsIdJsonDelete(id)

Delete a saved list view

Deletes a saved list view. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedListViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    SavedListViewsApi apiInstance = new SavedListViewsApi(defaultClient);
    String id = "id_example"; // String | Saved List View ID
    try {
      apiInstance.v2SavedListViewsIdJsonDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedListViewsApi#v2SavedListViewsIdJsonDelete");
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
| **id** | **String**| Saved List View ID | |

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
| **204** | The saved list view has been deleted successfully |  -  |

<a id="v2SavedListViewsIdJsonGet"></a>
# **v2SavedListViewsIdJsonGet**
> SavedListView v2SavedListViewsIdJsonGet(id)

Fetch a saved list view

Fetches a saved list view, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedListViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    SavedListViewsApi apiInstance = new SavedListViewsApi(defaultClient);
    String id = "id_example"; // String | Saved List View ID
    try {
      SavedListView result = apiInstance.v2SavedListViewsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedListViewsApi#v2SavedListViewsIdJsonGet");
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
| **id** | **String**| Saved List View ID | |

### Return type

[**SavedListView**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2SavedListViewsIdJsonPut"></a>
# **v2SavedListViewsIdJsonPut**
> SavedListView v2SavedListViewsIdJsonPut(id, isDefault, name, viewParams)

Update a saved list view

Updates a saved list view. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedListViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    SavedListViewsApi apiInstance = new SavedListViewsApi(defaultClient);
    String id = "id_example"; // String | Saved List View ID
    Boolean isDefault = true; // Boolean | Whether the saved list view is the default
    String name = "name_example"; // String | The name of the saved list view
    String viewParams = "viewParams_example"; // String | JSON object of list view parameters
    try {
      SavedListView result = apiInstance.v2SavedListViewsIdJsonPut(id, isDefault, name, viewParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedListViewsApi#v2SavedListViewsIdJsonPut");
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
| **id** | **String**| Saved List View ID | |
| **isDefault** | **Boolean**| Whether the saved list view is the default | [optional] |
| **name** | **String**| The name of the saved list view | [optional] |
| **viewParams** | **String**| JSON object of list view parameters | [optional] |

### Return type

[**SavedListView**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2SavedListViewsJsonGet"></a>
# **v2SavedListViewsJsonGet**
> List&lt;SavedListView&gt; v2SavedListViewsJsonGet(ids, view, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List saved list views

Fetches multiple saved list view records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedListViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    SavedListViewsApi apiInstance = new SavedListViewsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of saved list views to fetch. If a record can't be found, that record won't be returned and your request will be successful
    String view = "view_example"; // String | Type of saved list views to fetch.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: name. Defaults to name
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<SavedListView> result = apiInstance.v2SavedListViewsJsonGet(ids, view, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedListViewsApi#v2SavedListViewsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of saved list views to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **view** | **String**| Type of saved list views to fetch. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: name. Defaults to name | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;SavedListView&gt;**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2SavedListViewsJsonPost"></a>
# **v2SavedListViewsJsonPost**
> SavedListView v2SavedListViewsJsonPost(name, view, isDefault, viewParams)

Create a saved list view

Creates a saved list view. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedListViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    SavedListViewsApi apiInstance = new SavedListViewsApi(defaultClient);
    String name = "name_example"; // String | The name of the saved list view
    String view = "view_example"; // String | The type of objects in the saved list view.  Value must be one of: people, companies, or recordings
    Boolean isDefault = true; // Boolean | Whether the saved list view is the default
    String viewParams = "viewParams_example"; // String | JSON object of list view parameters
    try {
      SavedListView result = apiInstance.v2SavedListViewsJsonPost(name, view, isDefault, viewParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedListViewsApi#v2SavedListViewsJsonPost");
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
| **name** | **String**| The name of the saved list view | |
| **view** | **String**| The type of objects in the saved list view.  Value must be one of: people, companies, or recordings | |
| **isDefault** | **Boolean**| Whether the saved list view is the default | [optional] |
| **viewParams** | **String**| JSON object of list view parameters | [optional] |

### Return type

[**SavedListView**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


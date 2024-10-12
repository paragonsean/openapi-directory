# PersonStagesApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2PersonStagesIdJsonDelete**](PersonStagesApi.md#v2PersonStagesIdJsonDelete) | **DELETE** /v2/person_stages/{id}.json | Delete an person stage |
| [**v2PersonStagesIdJsonGet**](PersonStagesApi.md#v2PersonStagesIdJsonGet) | **GET** /v2/person_stages/{id}.json | Fetch a person stage |
| [**v2PersonStagesIdJsonPut**](PersonStagesApi.md#v2PersonStagesIdJsonPut) | **PUT** /v2/person_stages/{id}.json | Update a person stage |
| [**v2PersonStagesJsonGet**](PersonStagesApi.md#v2PersonStagesJsonGet) | **GET** /v2/person_stages.json | List person stages |
| [**v2PersonStagesJsonPost**](PersonStagesApi.md#v2PersonStagesJsonPost) | **POST** /v2/person_stages.json | Create a person stage |


<a id="v2PersonStagesIdJsonDelete"></a>
# **v2PersonStagesIdJsonDelete**
> v2PersonStagesIdJsonDelete(id)

Delete an person stage

Deletes a person stage. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonStagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PersonStagesApi apiInstance = new PersonStagesApi(defaultClient);
    String id = "id_example"; // String | Stage ID
    try {
      apiInstance.v2PersonStagesIdJsonDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonStagesApi#v2PersonStagesIdJsonDelete");
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
| **id** | **String**| Stage ID | |

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
| **204** | The Person Stage has been deleted successfully |  -  |

<a id="v2PersonStagesIdJsonGet"></a>
# **v2PersonStagesIdJsonGet**
> PersonStage v2PersonStagesIdJsonGet(id)

Fetch a person stage

Fetches a person stage, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonStagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PersonStagesApi apiInstance = new PersonStagesApi(defaultClient);
    String id = "id_example"; // String | Stage ID
    try {
      PersonStage result = apiInstance.v2PersonStagesIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonStagesApi#v2PersonStagesIdJsonGet");
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
| **id** | **String**| Stage ID | |

### Return type

[**PersonStage**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2PersonStagesIdJsonPut"></a>
# **v2PersonStagesIdJsonPut**
> PersonStage v2PersonStagesIdJsonPut(id, name)

Update a person stage

Updates a person stage. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonStagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PersonStagesApi apiInstance = new PersonStagesApi(defaultClient);
    String id = "id_example"; // String | Stage ID
    String name = "name_example"; // String | The name of the stage.
    try {
      PersonStage result = apiInstance.v2PersonStagesIdJsonPut(id, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonStagesApi#v2PersonStagesIdJsonPut");
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
| **id** | **String**| Stage ID | |
| **name** | **String**| The name of the stage. | |

### Return type

[**PersonStage**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2PersonStagesJsonGet"></a>
# **v2PersonStagesJsonGet**
> List&lt;PersonStage&gt; v2PersonStagesJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List person stages

Fetches multiple person stage records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonStagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PersonStagesApi apiInstance = new PersonStagesApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of person stages to fetch.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<PersonStage> result = apiInstance.v2PersonStagesJsonGet(ids, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonStagesApi#v2PersonStagesJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of person stages to fetch. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;PersonStage&gt;**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2PersonStagesJsonPost"></a>
# **v2PersonStagesJsonPost**
> PersonStage v2PersonStagesJsonPost(name)

Create a person stage

Creates a person stage. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonStagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    PersonStagesApi apiInstance = new PersonStagesApi(defaultClient);
    String name = "name_example"; // String | The name of the new stage
    try {
      PersonStage result = apiInstance.v2PersonStagesJsonPost(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonStagesApi#v2PersonStagesJsonPost");
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
| **name** | **String**| The name of the new stage | |

### Return type

[**PersonStage**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


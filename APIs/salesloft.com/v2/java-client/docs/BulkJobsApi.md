# BulkJobsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2BulkJobsGet**](BulkJobsApi.md#v2BulkJobsGet) | **GET** /v2/bulk_jobs | List bulk jobs |
| [**v2BulkJobsIdGet**](BulkJobsApi.md#v2BulkJobsIdGet) | **GET** /v2/bulk_jobs/{id} | Fetch a bulk job |
| [**v2BulkJobsIdPut**](BulkJobsApi.md#v2BulkJobsIdPut) | **PUT** /v2/bulk_jobs/{id} | Update a bulk job |
| [**v2BulkJobsPost**](BulkJobsApi.md#v2BulkJobsPost) | **POST** /v2/bulk_jobs | Create a bulk job |


<a id="v2BulkJobsGet"></a>
# **v2BulkJobsGet**
> List&lt;BulkJob&gt; v2BulkJobsGet(state, id, perPage)

List bulk jobs

Fetches multiple bulk job records. The records can be filtered, paged, and sorted according to the respective parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    BulkJobsApi apiInstance = new BulkJobsApi(defaultClient);
    List<String> state = Arrays.asList(); // List<String> | The state of the bulk job. Accepts multiple states. Each state must be one of: open, executing, done
    Object id = null; // Object | Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]=123)
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    try {
      List<BulkJob> result = apiInstance.v2BulkJobsGet(state, id, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkJobsApi#v2BulkJobsGet");
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
| **state** | [**List&lt;String&gt;**](String.md)| The state of the bulk job. Accepts multiple states. Each state must be one of: open, executing, done | [optional] |
| **id** | [**Object**](.md)| Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]&#x3D;123) | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |

### Return type

[**List&lt;BulkJob&gt;**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2BulkJobsIdGet"></a>
# **v2BulkJobsIdGet**
> BulkJob v2BulkJobsIdGet(id)

Fetch a bulk job

Fetches a bulk job, by ID only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    BulkJobsApi apiInstance = new BulkJobsApi(defaultClient);
    Integer id = 56; // Integer | The id for the Bulk Job
    try {
      BulkJob result = apiInstance.v2BulkJobsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkJobsApi#v2BulkJobsIdGet");
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
| **id** | **Integer**| The id for the Bulk Job | |

### Return type

[**BulkJob**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2BulkJobsIdPut"></a>
# **v2BulkJobsIdPut**
> BulkJob v2BulkJobsIdPut(id, name, readyToExecute)

Update a bulk job

Updates a bulk job&#39;s name and / or marks a bulk job as &#39;ready_to_execute&#39;.  May only be updated if the bulk job is still in an \&quot;open\&quot; state.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    BulkJobsApi apiInstance = new BulkJobsApi(defaultClient);
    Integer id = 56; // Integer | The id for the bulk job to which the job data relates
    String name = "name_example"; // String | Name for your bulk job
    Boolean readyToExecute = true; // Boolean | Whether the job is ready to be executed. Must be true or false.
    try {
      BulkJob result = apiInstance.v2BulkJobsIdPut(id, name, readyToExecute);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkJobsApi#v2BulkJobsIdPut");
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
| **id** | **Integer**| The id for the bulk job to which the job data relates | |
| **name** | **String**| Name for your bulk job | [optional] |
| **readyToExecute** | **Boolean**| Whether the job is ready to be executed. Must be true or false. | [optional] |

### Return type

[**BulkJob**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2BulkJobsPost"></a>
# **v2BulkJobsPost**
> BulkJob v2BulkJobsPost(type, name)

Create a bulk job

Creates a bulk job. The type of the bulk job must be included when created.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    BulkJobsApi apiInstance = new BulkJobsApi(defaultClient);
    String type = "type_example"; // String | Type of bulk job. Must be a valid type. Follow link to the bulk job details page above to view supported types.
    String name = "name_example"; // String | Name for your bulk job
    try {
      BulkJob result = apiInstance.v2BulkJobsPost(type, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkJobsApi#v2BulkJobsPost");
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
| **type** | **String**| Type of bulk job. Must be a valid type. Follow link to the bulk job details page above to view supported types. | |
| **name** | **String**| Name for your bulk job | [optional] |

### Return type

[**BulkJob**](BulkJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |


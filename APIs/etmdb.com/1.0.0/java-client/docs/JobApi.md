# JobApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobSearchRead**](JobApi.md#jobSearchRead) | **GET** /api/v1/job/search/{job_title} | Return job details search result |
| [**jobSearchallRead**](JobApi.md#jobSearchallRead) | **GET** /api/v1/job/searchall/{company_name} | Return job details search result |


<a id="jobSearchRead"></a>
# **jobSearchRead**
> jobSearchRead(jobTitle)

Return job details search result

Return job details search result  ### Response Class (Status 200)  * __{job_title}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    JobApi apiInstance = new JobApi(defaultClient);
    String jobTitle = "jobTitle_example"; // String | 
    try {
      apiInstance.jobSearchRead(jobTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobSearchRead");
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
| **jobTitle** | **String**|  | |

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
| **200** |  |  -  |

<a id="jobSearchallRead"></a>
# **jobSearchallRead**
> jobSearchallRead(companyName)

Return job details search result

Return job details search result  ### Response Class (Status 200)  * __{company_name}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    JobApi apiInstance = new JobApi(defaultClient);
    String companyName = "companyName_example"; // String | 
    try {
      apiInstance.jobSearchallRead(companyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobApi#jobSearchallRead");
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
| **companyName** | **String**|  | |

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
| **200** |  |  -  |


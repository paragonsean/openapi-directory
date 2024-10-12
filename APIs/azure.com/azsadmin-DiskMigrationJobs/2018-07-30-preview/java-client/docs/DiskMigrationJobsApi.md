# DiskMigrationJobsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diskMigrationJobsCancel**](DiskMigrationJobsApi.md#diskMigrationJobsCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migrationId}/Cancel |  |
| [**diskMigrationJobsCreate**](DiskMigrationJobsApi.md#diskMigrationJobsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migrationId} |  |
| [**diskMigrationJobsGet**](DiskMigrationJobsApi.md#diskMigrationJobsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs/{migrationId} |  |
| [**diskMigrationJobsList**](DiskMigrationJobsApi.md#diskMigrationJobsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute.Admin/locations/{location}/diskmigrationjobs |  |


<a id="diskMigrationJobsCancel"></a>
# **diskMigrationJobsCancel**
> DiskMigrationJobsGet200Response diskMigrationJobsCancel(subscriptionId, location, migrationId, apiVersion)



Cancel a disk migration job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskMigrationJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskMigrationJobsApi apiInstance = new DiskMigrationJobsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String migrationId = "migrationId_example"; // String | The migration job guid name.
    String apiVersion = "2018-07-30-preview"; // String | Client API Version.
    try {
      DiskMigrationJobsGet200Response result = apiInstance.diskMigrationJobsCancel(subscriptionId, location, migrationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskMigrationJobsApi#diskMigrationJobsCancel");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **migrationId** | **String**| The migration job guid name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2018-07-30-preview] |

### Return type

[**DiskMigrationJobsGet200Response**](DiskMigrationJobsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK --  Disk migration job cancellation is called. |  -  |

<a id="diskMigrationJobsCreate"></a>
# **diskMigrationJobsCreate**
> DiskMigrationJobsGet200Response diskMigrationJobsCreate(subscriptionId, location, migrationId, targetShare, apiVersion, disks)



Create a disk migration job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskMigrationJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskMigrationJobsApi apiInstance = new DiskMigrationJobsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String migrationId = "migrationId_example"; // String | The migration job guid name.
    String targetShare = "targetShare_example"; // String | The target share name.
    String apiVersion = "2018-07-30-preview"; // String | Client API Version.
    List<DiskMigrationJobsCreateRequestInner> disks = Arrays.asList(); // List<DiskMigrationJobsCreateRequestInner> | The parameters of disk list.
    try {
      DiskMigrationJobsGet200Response result = apiInstance.diskMigrationJobsCreate(subscriptionId, location, migrationId, targetShare, apiVersion, disks);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskMigrationJobsApi#diskMigrationJobsCreate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **migrationId** | **String**| The migration job guid name. | |
| **targetShare** | **String**| The target share name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2018-07-30-preview] |
| **disks** | [**List&lt;DiskMigrationJobsCreateRequestInner&gt;**](DiskMigrationJobsCreateRequestInner.md)| The parameters of disk list. | |

### Return type

[**DiskMigrationJobsGet200Response**](DiskMigrationJobsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK --  Disk migration job is created successfully. |  -  |

<a id="diskMigrationJobsGet"></a>
# **diskMigrationJobsGet**
> DiskMigrationJobsGet200Response diskMigrationJobsGet(subscriptionId, location, migrationId, apiVersion)



Returns the requested disk migration job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskMigrationJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskMigrationJobsApi apiInstance = new DiskMigrationJobsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String migrationId = "migrationId_example"; // String | The migration job guid name.
    String apiVersion = "2018-07-30-preview"; // String | Client API Version.
    try {
      DiskMigrationJobsGet200Response result = apiInstance.diskMigrationJobsGet(subscriptionId, location, migrationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskMigrationJobsApi#diskMigrationJobsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **migrationId** | **String**| The migration job guid name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2018-07-30-preview] |

### Return type

[**DiskMigrationJobsGet200Response**](DiskMigrationJobsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The disk migration job has been returned. |  -  |

<a id="diskMigrationJobsList"></a>
# **diskMigrationJobsList**
> DiskMigrationJobsList200Response diskMigrationJobsList(subscriptionId, location, apiVersion, status)



Returns a list of disk migration jobs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiskMigrationJobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DiskMigrationJobsApi apiInstance = new DiskMigrationJobsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Location of the resource.
    String apiVersion = "2018-07-30-preview"; // String | Client API Version.
    String status = "status_example"; // String | The parameters of disk migration job status.
    try {
      DiskMigrationJobsList200Response result = apiInstance.diskMigrationJobsList(subscriptionId, location, apiVersion, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiskMigrationJobsApi#diskMigrationJobsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Location of the resource. | |
| **apiVersion** | **String**| Client API Version. | [default to 2018-07-30-preview] |
| **status** | **String**| The parameters of disk migration job status. | [optional] |

### Return type

[**DiskMigrationJobsList200Response**](DiskMigrationJobsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of disk migration jobs has been returned. |  -  |


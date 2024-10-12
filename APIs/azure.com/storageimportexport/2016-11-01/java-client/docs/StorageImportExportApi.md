# StorageImportExportApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bitLockerKeysList**](StorageImportExportApi.md#bitLockerKeysList) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName}/listBitLockerKeys |  |
| [**jobsCreate**](StorageImportExportApi.md#jobsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} |  |
| [**jobsDelete**](StorageImportExportApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} |  |
| [**jobsGet**](StorageImportExportApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} |  |
| [**jobsListByResourceGroup**](StorageImportExportApi.md#jobsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs |  |
| [**jobsListBySubscription**](StorageImportExportApi.md#jobsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ImportExport/jobs |  |
| [**jobsUpdate**](StorageImportExportApi.md#jobsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ImportExport/jobs/{jobName} |  |
| [**locationsGet**](StorageImportExportApi.md#locationsGet) | **GET** /providers/Microsoft.ImportExport/locations/{locationName} |  |
| [**locationsList**](StorageImportExportApi.md#locationsList) | **GET** /providers/Microsoft.ImportExport/locations |  |
| [**operationsList**](StorageImportExportApi.md#operationsList) | **GET** /providers/Microsoft.ImportExport/operations |  |


<a id="bitLockerKeysList"></a>
# **bitLockerKeysList**
> GetBitLockerKeysResponse bitLockerKeysList(jobName, subscriptionId, resourceGroupName, apiVersion, acceptLanguage)



Returns the BitLocker Keys for all drives in the specified job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String jobName = "jobName_example"; // String | The name of the import/export job.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      GetBitLockerKeysResponse result = apiInstance.bitLockerKeysList(jobName, subscriptionId, resourceGroupName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#bitLockerKeysList");
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
| **jobName** | **String**| The name of the import/export job. | |
| **subscriptionId** | **String**| The subscription ID for the Azure user. | |
| **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**GetBitLockerKeysResponse**](GetBitLockerKeysResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="jobsCreate"></a>
# **jobsCreate**
> JobResponse jobsCreate(jobName, subscriptionId, resourceGroupName, apiVersion, body, acceptLanguage, xMsClientTenantId)



Creates a new job or updates an existing job in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String jobName = "jobName_example"; // String | The name of the import/export job.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    PutJobParameters body = new PutJobParameters(); // PutJobParameters | The parameters used for creating the job
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    String xMsClientTenantId = "xMsClientTenantId_example"; // String | The tenant ID of the client making the request.
    try {
      JobResponse result = apiInstance.jobsCreate(jobName, subscriptionId, resourceGroupName, apiVersion, body, acceptLanguage, xMsClientTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#jobsCreate");
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
| **jobName** | **String**| The name of the import/export job. | |
| **subscriptionId** | **String**| The subscription ID for the Azure user. | |
| **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **body** | [**PutJobParameters**](PutJobParameters.md)| The parameters used for creating the job | |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |
| **xMsClientTenantId** | **String**| The tenant ID of the client making the request. | [optional] |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | An error occurs. |  -  |

<a id="jobsDelete"></a>
# **jobsDelete**
> jobsDelete(jobName, subscriptionId, resourceGroupName, apiVersion, acceptLanguage)



Deletes an existing job. Only jobs in the Creating or Completed states can be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String jobName = "jobName_example"; // String | The name of the import/export job.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      apiInstance.jobsDelete(jobName, subscriptionId, resourceGroupName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#jobsDelete");
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
| **jobName** | **String**| The name of the import/export job. | |
| **subscriptionId** | **String**| The subscription ID for the Azure user. | |
| **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="jobsGet"></a>
# **jobsGet**
> JobResponse jobsGet(jobName, subscriptionId, resourceGroupName, apiVersion, acceptLanguage)



Gets information about an existing job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String jobName = "jobName_example"; // String | The name of the import/export job.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      JobResponse result = apiInstance.jobsGet(jobName, subscriptionId, resourceGroupName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#jobsGet");
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
| **jobName** | **String**| The name of the import/export job. | |
| **subscriptionId** | **String**| The subscription ID for the Azure user. | |
| **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="jobsListByResourceGroup"></a>
# **jobsListByResourceGroup**
> ListJobsResponse jobsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top, $filter, acceptLanguage)



Returns all active and completed jobs in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    Integer $top = 56; // Integer | An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100.
    String $filter = "$filter_example"; // String | Can be used to restrict the results to certain conditions.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      ListJobsResponse result = apiInstance.jobsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top, $filter, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#jobsListByResourceGroup");
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
| **subscriptionId** | **String**| The subscription ID for the Azure user. | |
| **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **$top** | **Integer**| An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100. | [optional] |
| **$filter** | **String**| Can be used to restrict the results to certain conditions. | [optional] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**ListJobsResponse**](ListJobsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="jobsListBySubscription"></a>
# **jobsListBySubscription**
> ListJobsResponse jobsListBySubscription(subscriptionId, apiVersion, $top, $filter, acceptLanguage)



Returns all active and completed jobs in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    Integer $top = 56; // Integer | An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100.
    String $filter = "$filter_example"; // String | Can be used to restrict the results to certain conditions.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      ListJobsResponse result = apiInstance.jobsListBySubscription(subscriptionId, apiVersion, $top, $filter, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#jobsListBySubscription");
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
| **subscriptionId** | **String**| The subscription ID for the Azure user. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **$top** | **Integer**| An integer value that specifies how many jobs at most should be returned. The value cannot exceed 100. | [optional] |
| **$filter** | **String**| Can be used to restrict the results to certain conditions. | [optional] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**ListJobsResponse**](ListJobsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="jobsUpdate"></a>
# **jobsUpdate**
> JobResponse jobsUpdate(jobName, subscriptionId, resourceGroupName, apiVersion, body, acceptLanguage)



Updates specific properties of a job. You can call this operation to notify the Import/Export service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It can also be used to cancel an existing job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String jobName = "jobName_example"; // String | The name of the import/export job.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID for the Azure user.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name uniquely identifies the resource group within the user subscription.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    UpdateJobParameters body = new UpdateJobParameters(); // UpdateJobParameters | The parameters to update in the job
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      JobResponse result = apiInstance.jobsUpdate(jobName, subscriptionId, resourceGroupName, apiVersion, body, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#jobsUpdate");
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
| **jobName** | **String**| The name of the import/export job. | |
| **subscriptionId** | **String**| The subscription ID for the Azure user. | |
| **resourceGroupName** | **String**| The resource group name uniquely identifies the resource group within the user subscription. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **body** | [**UpdateJobParameters**](UpdateJobParameters.md)| The parameters to update in the job | |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="locationsGet"></a>
# **locationsGet**
> Location locationsGet(locationName, apiVersion, acceptLanguage)



Returns the details about a location to which you can ship the disks associated with an import or export job. A location is an Azure region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String locationName = "locationName_example"; // String | The name of the location. For example, West US or westus.
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      Location result = apiInstance.locationsGet(locationName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#locationsGet");
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
| **locationName** | **String**| The name of the location. For example, West US or westus. | |
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**Location**](Location.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="locationsList"></a>
# **locationsList**
> LocationsResponse locationsList(apiVersion, acceptLanguage)



Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      LocationsResponse result = apiInstance.locationsList(apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#locationsList");
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
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**LocationsResponse**](LocationsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |

<a id="operationsList"></a>
# **operationsList**
> ListOperationsResponse operationsList(apiVersion, acceptLanguage)



Returns the list of operations supported by the import/export resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageImportExportApi apiInstance = new StorageImportExportApi(defaultClient);
    String apiVersion = "2016-11-01"; // String | Specifies the API version to use for this request.
    String acceptLanguage = "acceptLanguage_example"; // String | Specifies the preferred language for the response.
    try {
      ListOperationsResponse result = apiInstance.operationsList(apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageImportExportApi#operationsList");
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
| **apiVersion** | **String**| Specifies the API version to use for this request. | [enum: 2016-11-01] |
| **acceptLanguage** | **String**| Specifies the preferred language for the response. | [optional] |

### Return type

[**ListOperationsResponse**](ListOperationsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | An error occurs. |  -  |


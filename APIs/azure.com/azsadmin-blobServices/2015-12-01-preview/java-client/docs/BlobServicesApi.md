# BlobServicesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blobServicesGet**](BlobServicesApi.md#blobServicesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/blobservices/{serviceType} |  |
| [**blobServicesListMetricDefinitions**](BlobServicesApi.md#blobServicesListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/blobservices/{serviceType}/metricdefinitions |  |
| [**blobServicesListMetrics**](BlobServicesApi.md#blobServicesListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/blobservices/{serviceType}/metrics |  |


<a id="blobServicesGet"></a>
# **blobServicesGet**
> BlobService blobServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns the BLOB service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobServicesApi apiInstance = new BlobServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String serviceType = "default"; // String | The service type.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      BlobService result = apiInstance.blobServicesGet(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobServicesApi#blobServicesGet");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **serviceType** | **String**| The service type. | [enum: default] |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**BlobService**](BlobService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The BLOB service has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

<a id="blobServicesListMetricDefinitions"></a>
# **blobServicesListMetricDefinitions**
> BlobServicesListMetricDefinitions200Response blobServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns the list of metric definitions for BLOB service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobServicesApi apiInstance = new BlobServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String serviceType = "default"; // String | The service type.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      BlobServicesListMetricDefinitions200Response result = apiInstance.blobServicesListMetricDefinitions(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobServicesApi#blobServicesListMetricDefinitions");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **serviceType** | **String**| The service type. | [enum: default] |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**BlobServicesListMetricDefinitions200Response**](BlobServicesListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metric definitions for the BLOB service has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

<a id="blobServicesListMetrics"></a>
# **blobServicesListMetrics**
> BlobServicesListMetrics200Response blobServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion)



Returns a list of metrics for BLOB service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobServicesApi apiInstance = new BlobServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String serviceType = "default"; // String | The service type.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      BlobServicesListMetrics200Response result = apiInstance.blobServicesListMetrics(subscriptionId, resourceGroupName, farmId, serviceType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobServicesApi#blobServicesListMetrics");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **serviceType** | **String**| The service type. | [enum: default] |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**BlobServicesListMetrics200Response**](BlobServicesListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metrics has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |


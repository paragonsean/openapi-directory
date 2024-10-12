# DedicatedCloudServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dedicatedCloudServicesCreateOrUpdate**](DedicatedCloudServicesApi.md#dedicatedCloudServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicated cloud service PUT method |
| [**dedicatedCloudServicesDelete**](DedicatedCloudServicesApi.md#dedicatedCloudServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicatedCloudService DELETE method |
| [**dedicatedCloudServicesGet**](DedicatedCloudServicesApi.md#dedicatedCloudServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicatedCloudService GET method |
| [**dedicatedCloudServicesListByResourceGroup**](DedicatedCloudServicesApi.md#dedicatedCloudServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices | Implements list of dedicatedCloudService objects within RG method |
| [**dedicatedCloudServicesListBySubscription**](DedicatedCloudServicesApi.md#dedicatedCloudServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices | Implements list of dedicatedCloudService objects within subscription method |
| [**dedicatedCloudServicesUpdate**](DedicatedCloudServicesApi.md#dedicatedCloudServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudServices/{dedicatedCloudServiceName} | Implements dedicatedCloudService PATCH method |


<a id="dedicatedCloudServicesCreateOrUpdate"></a>
# **dedicatedCloudServicesCreateOrUpdate**
> DedicatedCloudService dedicatedCloudServicesCreateOrUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest)

Implements dedicated cloud service PUT method

Create dedicate cloud service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudServicesApi apiInstance = new DedicatedCloudServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud Service name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    DedicatedCloudService dedicatedCloudServiceRequest = new DedicatedCloudService(); // DedicatedCloudService | Create Dedicated Cloud Service request
    try {
      DedicatedCloudService result = apiInstance.dedicatedCloudServicesCreateOrUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudServicesApi#dedicatedCloudServicesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group | |
| **dedicatedCloudServiceName** | **String**| dedicated cloud Service name | |
| **apiVersion** | **String**| Client API version. | |
| **dedicatedCloudServiceRequest** | [**DedicatedCloudService**](DedicatedCloudService.md)| Create Dedicated Cloud Service request | |

### Return type

[**DedicatedCloudService**](DedicatedCloudService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created or updated successfully, 200 should be returned |  -  |
| **0** | General Error |  -  |

<a id="dedicatedCloudServicesDelete"></a>
# **dedicatedCloudServicesDelete**
> dedicatedCloudServicesDelete(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion)

Implements dedicatedCloudService DELETE method

Delete dedicate cloud service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudServicesApi apiInstance = new DedicatedCloudServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud service name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.dedicatedCloudServicesDelete(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudServicesApi#dedicatedCloudServicesDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group | |
| **dedicatedCloudServiceName** | **String**| dedicated cloud service name | |
| **apiVersion** | **String**| Client API version. | |

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
| **204** | no content. resource does not exist and the request is well formed |  -  |
| **0** | General Error |  * Content-Type -  <br>  |

<a id="dedicatedCloudServicesGet"></a>
# **dedicatedCloudServicesGet**
> DedicatedCloudService dedicatedCloudServicesGet(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion)

Implements dedicatedCloudService GET method

Returns Dedicate Cloud Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudServicesApi apiInstance = new DedicatedCloudServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud Service name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DedicatedCloudService result = apiInstance.dedicatedCloudServicesGet(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudServicesApi#dedicatedCloudServicesGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group | |
| **dedicatedCloudServiceName** | **String**| dedicated cloud Service name | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**DedicatedCloudService**](DedicatedCloudService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="dedicatedCloudServicesListByResourceGroup"></a>
# **dedicatedCloudServicesListByResourceGroup**
> DedicatedCloudServiceListResponse dedicatedCloudServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $skipToken)

Implements list of dedicatedCloudService objects within RG method

Returns list of dedicated cloud services within a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudServicesApi apiInstance = new DedicatedCloudServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation
    Integer $top = 56; // Integer | The maximum number of record sets to return
    String $skipToken = "$skipToken_example"; // String | to be used by nextLink implementation
    try {
      DedicatedCloudServiceListResponse result = apiInstance.dedicatedCloudServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudServicesApi#dedicatedCloudServicesListByResourceGroup");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group | |
| **apiVersion** | **String**| Client API version. | |
| **$filter** | **String**| The filter to apply on the list operation | [optional] |
| **$top** | **Integer**| The maximum number of record sets to return | [optional] |
| **$skipToken** | **String**| to be used by nextLink implementation | [optional] |

### Return type

[**DedicatedCloudServiceListResponse**](DedicatedCloudServiceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="dedicatedCloudServicesListBySubscription"></a>
# **dedicatedCloudServicesListBySubscription**
> DedicatedCloudServiceListResponse dedicatedCloudServicesListBySubscription(subscriptionId, apiVersion, $filter, $top, $skipToken)

Implements list of dedicatedCloudService objects within subscription method

Returns list of dedicated cloud services within a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudServicesApi apiInstance = new DedicatedCloudServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation
    Integer $top = 56; // Integer | The maximum number of record sets to return
    String $skipToken = "$skipToken_example"; // String | to be used by nextLink implementation
    try {
      DedicatedCloudServiceListResponse result = apiInstance.dedicatedCloudServicesListBySubscription(subscriptionId, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudServicesApi#dedicatedCloudServicesListBySubscription");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **apiVersion** | **String**| Client API version. | |
| **$filter** | **String**| The filter to apply on the list operation | [optional] |
| **$top** | **Integer**| The maximum number of record sets to return | [optional] |
| **$skipToken** | **String**| to be used by nextLink implementation | [optional] |

### Return type

[**DedicatedCloudServiceListResponse**](DedicatedCloudServiceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="dedicatedCloudServicesUpdate"></a>
# **dedicatedCloudServicesUpdate**
> DedicatedCloudService dedicatedCloudServicesUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest)

Implements dedicatedCloudService PATCH method

Patch dedicated cloud service&#39;s properties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudServicesApi apiInstance = new DedicatedCloudServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String dedicatedCloudServiceName = "dedicatedCloudServiceName_example"; // String | dedicated cloud service name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    PatchPayload dedicatedCloudServiceRequest = new PatchPayload(); // PatchPayload | Patch Dedicated Cloud Service request
    try {
      DedicatedCloudService result = apiInstance.dedicatedCloudServicesUpdate(subscriptionId, resourceGroupName, dedicatedCloudServiceName, apiVersion, dedicatedCloudServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudServicesApi#dedicatedCloudServicesUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group | |
| **dedicatedCloudServiceName** | **String**| dedicated cloud service name | |
| **apiVersion** | **String**| Client API version. | |
| **dedicatedCloudServiceRequest** | [**PatchPayload**](PatchPayload.md)| Patch Dedicated Cloud Service request | |

### Return type

[**DedicatedCloudService**](DedicatedCloudService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created or updated successfully, 200 should be returned |  -  |
| **0** | General Error |  -  |


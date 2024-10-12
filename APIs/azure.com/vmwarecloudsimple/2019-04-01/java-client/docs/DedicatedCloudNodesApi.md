# DedicatedCloudNodesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dedicatedCloudNodesCreateOrUpdate**](DedicatedCloudNodesApi.md#dedicatedCloudNodesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node PUT method |
| [**dedicatedCloudNodesDelete**](DedicatedCloudNodesApi.md#dedicatedCloudNodesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node DELETE method |
| [**dedicatedCloudNodesGet**](DedicatedCloudNodesApi.md#dedicatedCloudNodesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node GET method |
| [**dedicatedCloudNodesListByResourceGroup**](DedicatedCloudNodesApi.md#dedicatedCloudNodesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes | Implements list of dedicated cloud nodes within RG method |
| [**dedicatedCloudNodesListBySubscription**](DedicatedCloudNodesApi.md#dedicatedCloudNodesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes | Implements list of dedicated cloud nodes within subscription method |
| [**dedicatedCloudNodesUpdate**](DedicatedCloudNodesApi.md#dedicatedCloudNodesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicatedCloudNodeName} | Implements dedicated cloud node PATCH method |


<a id="dedicatedCloudNodesCreateOrUpdate"></a>
# **dedicatedCloudNodesCreateOrUpdate**
> DedicatedCloudNode dedicatedCloudNodesCreateOrUpdate(subscriptionId, resourceGroupName, referer, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest)

Implements dedicated cloud node PUT method

Returns dedicated cloud node by its name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudNodesApi apiInstance = new DedicatedCloudNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String referer = "referer_example"; // String | referer url
    String dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    DedicatedCloudNode dedicatedCloudNodeRequest = new DedicatedCloudNode(); // DedicatedCloudNode | Create Dedicated Cloud Node request
    try {
      DedicatedCloudNode result = apiInstance.dedicatedCloudNodesCreateOrUpdate(subscriptionId, resourceGroupName, referer, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudNodesApi#dedicatedCloudNodesCreateOrUpdate");
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
| **referer** | **String**| referer url | |
| **dedicatedCloudNodeName** | **String**| dedicated cloud node name | |
| **apiVersion** | **String**| Client API version. | |
| **dedicatedCloudNodeRequest** | [**DedicatedCloudNode**](DedicatedCloudNode.md)| Create Dedicated Cloud Node request | |

### Return type

[**DedicatedCloudNode**](DedicatedCloudNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created or updated successfully, 200 should be returned |  * Retry-After -  <br>  * Azure-AsyncOperation -  <br>  * Location -  <br>  |
| **0** | General Error |  -  |

<a id="dedicatedCloudNodesDelete"></a>
# **dedicatedCloudNodesDelete**
> dedicatedCloudNodesDelete(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion)

Implements dedicated cloud node DELETE method

Delete dedicated cloud node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudNodesApi apiInstance = new DedicatedCloudNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.dedicatedCloudNodesDelete(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudNodesApi#dedicatedCloudNodesDelete");
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
| **dedicatedCloudNodeName** | **String**| dedicated cloud node name | |
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

<a id="dedicatedCloudNodesGet"></a>
# **dedicatedCloudNodesGet**
> DedicatedCloudNode dedicatedCloudNodesGet(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion)

Implements dedicated cloud node GET method

Returns dedicated cloud node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudNodesApi apiInstance = new DedicatedCloudNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DedicatedCloudNode result = apiInstance.dedicatedCloudNodesGet(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudNodesApi#dedicatedCloudNodesGet");
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
| **dedicatedCloudNodeName** | **String**| dedicated cloud node name | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**DedicatedCloudNode**](DedicatedCloudNode.md)

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

<a id="dedicatedCloudNodesListByResourceGroup"></a>
# **dedicatedCloudNodesListByResourceGroup**
> DedicatedCloudNodeListResponse dedicatedCloudNodesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $skipToken)

Implements list of dedicated cloud nodes within RG method

Returns list of dedicate cloud nodes within resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudNodesApi apiInstance = new DedicatedCloudNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation
    Integer $top = 56; // Integer | The maximum number of record sets to return
    String $skipToken = "$skipToken_example"; // String | to be used by nextLink implementation
    try {
      DedicatedCloudNodeListResponse result = apiInstance.dedicatedCloudNodesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudNodesApi#dedicatedCloudNodesListByResourceGroup");
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

[**DedicatedCloudNodeListResponse**](DedicatedCloudNodeListResponse.md)

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

<a id="dedicatedCloudNodesListBySubscription"></a>
# **dedicatedCloudNodesListBySubscription**
> DedicatedCloudNodeListResponse dedicatedCloudNodesListBySubscription(subscriptionId, apiVersion, $filter, $top, $skipToken)

Implements list of dedicated cloud nodes within subscription method

Returns list of dedicate cloud nodes within subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudNodesApi apiInstance = new DedicatedCloudNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String $filter = "$filter_example"; // String | The filter to apply on the list operation
    Integer $top = 56; // Integer | The maximum number of record sets to return
    String $skipToken = "$skipToken_example"; // String | to be used by nextLink implementation
    try {
      DedicatedCloudNodeListResponse result = apiInstance.dedicatedCloudNodesListBySubscription(subscriptionId, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudNodesApi#dedicatedCloudNodesListBySubscription");
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

[**DedicatedCloudNodeListResponse**](DedicatedCloudNodeListResponse.md)

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

<a id="dedicatedCloudNodesUpdate"></a>
# **dedicatedCloudNodesUpdate**
> DedicatedCloudNode dedicatedCloudNodesUpdate(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest)

Implements dedicated cloud node PATCH method

Patches dedicated node properties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DedicatedCloudNodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DedicatedCloudNodesApi apiInstance = new DedicatedCloudNodesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group
    String dedicatedCloudNodeName = "dedicatedCloudNodeName_example"; // String | dedicated cloud node name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    PatchPayload dedicatedCloudNodeRequest = new PatchPayload(); // PatchPayload | Patch Dedicated Cloud Node request
    try {
      DedicatedCloudNode result = apiInstance.dedicatedCloudNodesUpdate(subscriptionId, resourceGroupName, dedicatedCloudNodeName, apiVersion, dedicatedCloudNodeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DedicatedCloudNodesApi#dedicatedCloudNodesUpdate");
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
| **dedicatedCloudNodeName** | **String**| dedicated cloud node name | |
| **apiVersion** | **String**| Client API version. | |
| **dedicatedCloudNodeRequest** | [**PatchPayload**](PatchPayload.md)| Patch Dedicated Cloud Node request | |

### Return type

[**DedicatedCloudNode**](DedicatedCloudNode.md)

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


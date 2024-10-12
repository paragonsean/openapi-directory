# InstancePoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**instancePoolsCreateOrUpdate**](InstancePoolsApi.md#instancePoolsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools/{instancePoolName} |  |
| [**instancePoolsDelete**](InstancePoolsApi.md#instancePoolsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools/{instancePoolName} |  |
| [**instancePoolsGet**](InstancePoolsApi.md#instancePoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools/{instancePoolName} |  |
| [**instancePoolsList**](InstancePoolsApi.md#instancePoolsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/instancePools |  |
| [**instancePoolsListByResourceGroup**](InstancePoolsApi.md#instancePoolsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools |  |
| [**instancePoolsUpdate**](InstancePoolsApi.md#instancePoolsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools/{instancePoolName} |  |


<a id="instancePoolsCreateOrUpdate"></a>
# **instancePoolsCreateOrUpdate**
> InstancePool instancePoolsCreateOrUpdate(resourceGroupName, instancePoolName, subscriptionId, apiVersion, parameters)



Creates or updates an instance pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstancePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstancePoolsApi apiInstance = new InstancePoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String instancePoolName = "instancePoolName_example"; // String | The name of the instance pool to be created or updated.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    InstancePool parameters = new InstancePool(); // InstancePool | The requested instance pool resource state.
    try {
      InstancePool result = apiInstance.instancePoolsCreateOrUpdate(resourceGroupName, instancePoolName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstancePoolsApi#instancePoolsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **instancePoolName** | **String**| The name of the instance pool to be created or updated. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**InstancePool**](InstancePool.md)| The requested instance pool resource state. | |

### Return type

[**InstancePool**](InstancePool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the instance pool. |  -  |
| **201** | Successfully created the instance pool. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 MissingSkuName - Sku name is required.   * 400 InstancePoolRequestedVcoreCountIsInvalid - Requested vcore count for instance pool is invalid   * 400 InstancePoolRequestMissingSku - Instance pool request is missing sku   * 400 InstancePoolRequestMissingSkuTier - Instance pool request is missing sku tier   * 400 InstancePoolRequestMissingSkuFamily - Instance pool request is missing sku family   * 400 InstancePoolRequestedSubnetResourceIdIsInvalid - Subnet id for instance pool is null or empty   * 409 InstancePoolBusy - An instance pool is busy with another ongoing operation |  -  |

<a id="instancePoolsDelete"></a>
# **instancePoolsDelete**
> instancePoolsDelete(resourceGroupName, instancePoolName, subscriptionId, apiVersion)



Deletes an instance pool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstancePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstancePoolsApi apiInstance = new InstancePoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String instancePoolName = "instancePoolName_example"; // String | The name of the instance pool to be deleted
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.instancePoolsDelete(resourceGroupName, instancePoolName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstancePoolsApi#instancePoolsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **instancePoolName** | **String**| The name of the instance pool to be deleted | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

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
| **200** | Successfully deleted the instance pool. |  -  |
| **202** | Accepted |  -  |
| **204** | The specified instance pool does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 InstancePoolNotEmpty - An instance pool is not empty   * 404 InstancePoolNotFound - An instance pool cannot be found   * 404 InstancePoolNotFound - An instance pool cannot be found   * 409 InstancePoolBusy - An instance pool is busy with another ongoing operation |  -  |

<a id="instancePoolsGet"></a>
# **instancePoolsGet**
> InstancePool instancePoolsGet(resourceGroupName, instancePoolName, subscriptionId, apiVersion)



Gets an instance pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstancePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstancePoolsApi apiInstance = new InstancePoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String instancePoolName = "instancePoolName_example"; // String | The name of the instance pool to be retrieved.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      InstancePool result = apiInstance.instancePoolsGet(resourceGroupName, instancePoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstancePoolsApi#instancePoolsGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **instancePoolName** | **String**| The name of the instance pool to be retrieved. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**InstancePool**](InstancePool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified instance pool. |  -  |
| **0** | *** Error Responses: ***   * 404 InstancePoolNotFound - An instance pool cannot be found |  -  |

<a id="instancePoolsList"></a>
# **instancePoolsList**
> InstancePoolListResult instancePoolsList(subscriptionId, apiVersion)



Gets a list of all instance pools in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstancePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstancePoolsApi apiInstance = new InstancePoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      InstancePoolListResult result = apiInstance.instancePoolsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstancePoolsApi#instancePoolsList");
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
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**InstancePoolListResult**](InstancePoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of instance pools in a subscription. |  -  |
| **0** | *** Error Responses: *** |  -  |

<a id="instancePoolsListByResourceGroup"></a>
# **instancePoolsListByResourceGroup**
> InstancePoolListResult instancePoolsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Gets a list of instance pools in the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstancePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstancePoolsApi apiInstance = new InstancePoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      InstancePoolListResult result = apiInstance.instancePoolsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstancePoolsApi#instancePoolsListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**InstancePoolListResult**](InstancePoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of instance pools. |  -  |
| **0** | *** Error Responses: *** |  -  |

<a id="instancePoolsUpdate"></a>
# **instancePoolsUpdate**
> InstancePool instancePoolsUpdate(resourceGroupName, instancePoolName, subscriptionId, apiVersion, parameters)



Updates an instance pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstancePoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    InstancePoolsApi apiInstance = new InstancePoolsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String instancePoolName = "instancePoolName_example"; // String | The name of the instance pool to be updated.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    InstancePoolUpdate parameters = new InstancePoolUpdate(); // InstancePoolUpdate | The requested instance pool resource state.
    try {
      InstancePool result = apiInstance.instancePoolsUpdate(resourceGroupName, instancePoolName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstancePoolsApi#instancePoolsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **instancePoolName** | **String**| The name of the instance pool to be updated. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**InstancePoolUpdate**](InstancePoolUpdate.md)| The requested instance pool resource state. | |

### Return type

[**InstancePool**](InstancePool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the instance pool. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid. |  -  |


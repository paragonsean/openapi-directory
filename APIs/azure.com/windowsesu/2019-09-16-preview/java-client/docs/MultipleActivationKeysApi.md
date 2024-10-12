# MultipleActivationKeysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**multipleActivationKeysCreate**](MultipleActivationKeysApi.md#multipleActivationKeysCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} |  |
| [**multipleActivationKeysDelete**](MultipleActivationKeysApi.md#multipleActivationKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} |  |
| [**multipleActivationKeysGet**](MultipleActivationKeysApi.md#multipleActivationKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} |  |
| [**multipleActivationKeysList**](MultipleActivationKeysApi.md#multipleActivationKeysList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.WindowsESU/multipleActivationKeys |  |
| [**multipleActivationKeysListByResourceGroup**](MultipleActivationKeysApi.md#multipleActivationKeysListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys |  |
| [**multipleActivationKeysUpdate**](MultipleActivationKeysApi.md#multipleActivationKeysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.WindowsESU/multipleActivationKeys/{multipleActivationKeyName} |  |


<a id="multipleActivationKeysCreate"></a>
# **multipleActivationKeysCreate**
> MultipleActivationKey multipleActivationKeysCreate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey)



Create a MAK key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultipleActivationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MultipleActivationKeysApi apiInstance = new MultipleActivationKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
    MultipleActivationKey multipleActivationKey = new MultipleActivationKey(); // MultipleActivationKey | Details of the MAK key.
    try {
      MultipleActivationKey result = apiInstance.multipleActivationKeysCreate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultipleActivationKeysApi#multipleActivationKeysCreate");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **multipleActivationKeyName** | **String**| The name of the MAK key. | |
| **multipleActivationKey** | [**MultipleActivationKey**](MultipleActivationKey.md)| Details of the MAK key. | |

### Return type

[**MultipleActivationKey**](MultipleActivationKey.md)

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
| **0** | Error response describing why the operation failed. |  -  |

<a id="multipleActivationKeysDelete"></a>
# **multipleActivationKeysDelete**
> multipleActivationKeysDelete(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName)



Delete a MAK key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultipleActivationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MultipleActivationKeysApi apiInstance = new MultipleActivationKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
    try {
      apiInstance.multipleActivationKeysDelete(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultipleActivationKeysApi#multipleActivationKeysDelete");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **multipleActivationKeyName** | **String**| The name of the MAK key. | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="multipleActivationKeysGet"></a>
# **multipleActivationKeysGet**
> MultipleActivationKey multipleActivationKeysGet(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName)



Get a MAK key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultipleActivationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MultipleActivationKeysApi apiInstance = new MultipleActivationKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
    try {
      MultipleActivationKey result = apiInstance.multipleActivationKeysGet(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultipleActivationKeysApi#multipleActivationKeysGet");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **multipleActivationKeyName** | **String**| The name of the MAK key. | |

### Return type

[**MultipleActivationKey**](MultipleActivationKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="multipleActivationKeysList"></a>
# **multipleActivationKeysList**
> MultipleActivationKeyList multipleActivationKeysList(subscriptionId, apiVersion)



List all Multiple Activation Keys (MAK) created for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultipleActivationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MultipleActivationKeysApi apiInstance = new MultipleActivationKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      MultipleActivationKeyList result = apiInstance.multipleActivationKeysList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultipleActivationKeysApi#multipleActivationKeysList");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**MultipleActivationKeyList**](MultipleActivationKeyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="multipleActivationKeysListByResourceGroup"></a>
# **multipleActivationKeysListByResourceGroup**
> MultipleActivationKeyList multipleActivationKeysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List all Multiple Activation Keys (MAK) in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultipleActivationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MultipleActivationKeysApi apiInstance = new MultipleActivationKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      MultipleActivationKeyList result = apiInstance.multipleActivationKeysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultipleActivationKeysApi#multipleActivationKeysListByResourceGroup");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**MultipleActivationKeyList**](MultipleActivationKeyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="multipleActivationKeysUpdate"></a>
# **multipleActivationKeysUpdate**
> MultipleActivationKey multipleActivationKeysUpdate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey)



Update a MAK key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MultipleActivationKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MultipleActivationKeysApi apiInstance = new MultipleActivationKeysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String multipleActivationKeyName = "multipleActivationKeyName_example"; // String | The name of the MAK key.
    MultipleActivationKeyUpdate multipleActivationKey = new MultipleActivationKeyUpdate(); // MultipleActivationKeyUpdate | Details of the MAK key.
    try {
      MultipleActivationKey result = apiInstance.multipleActivationKeysUpdate(subscriptionId, resourceGroupName, apiVersion, multipleActivationKeyName, multipleActivationKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MultipleActivationKeysApi#multipleActivationKeysUpdate");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **multipleActivationKeyName** | **String**| The name of the MAK key. | |
| **multipleActivationKey** | [**MultipleActivationKeyUpdate**](MultipleActivationKeyUpdate.md)| Details of the MAK key. | |

### Return type

[**MultipleActivationKey**](MultipleActivationKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |


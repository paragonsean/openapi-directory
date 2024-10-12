# ProximityPlacementGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**proximityPlacementGroupsCreateOrUpdate**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} |  |
| [**proximityPlacementGroupsDelete**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} |  |
| [**proximityPlacementGroupsGet**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} |  |
| [**proximityPlacementGroupsListByResourceGroup**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups |  |
| [**proximityPlacementGroupsListBySubscription**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/proximityPlacementGroups |  |
| [**proximityPlacementGroupsUpdate**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} |  |


<a id="proximityPlacementGroupsCreateOrUpdate"></a>
# **proximityPlacementGroupsCreateOrUpdate**
> ProximityPlacementGroup proximityPlacementGroupsCreateOrUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters)



Create or update a proximity placement group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProximityPlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProximityPlacementGroupsApi apiInstance = new ProximityPlacementGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ProximityPlacementGroup parameters = new ProximityPlacementGroup(); // ProximityPlacementGroup | Parameters supplied to the Create Proximity Placement Group operation.
    try {
      ProximityPlacementGroup result = apiInstance.proximityPlacementGroupsCreateOrUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProximityPlacementGroupsApi#proximityPlacementGroupsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ProximityPlacementGroup**](ProximityPlacementGroup.md)| Parameters supplied to the Create Proximity Placement Group operation. | |

### Return type

[**ProximityPlacementGroup**](ProximityPlacementGroup.md)

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

<a id="proximityPlacementGroupsDelete"></a>
# **proximityPlacementGroupsDelete**
> proximityPlacementGroupsDelete(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId)



Delete a proximity placement group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProximityPlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProximityPlacementGroupsApi apiInstance = new ProximityPlacementGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.proximityPlacementGroupsDelete(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProximityPlacementGroupsApi#proximityPlacementGroupsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="proximityPlacementGroupsGet"></a>
# **proximityPlacementGroupsGet**
> ProximityPlacementGroup proximityPlacementGroupsGet(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, includeColocationStatus)



Retrieves information about a proximity placement group .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProximityPlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProximityPlacementGroupsApi apiInstance = new ProximityPlacementGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String includeColocationStatus = "includeColocationStatus_example"; // String | includeColocationStatus=true enables fetching the colocation status of all the resources in the proximity placement group.
    try {
      ProximityPlacementGroup result = apiInstance.proximityPlacementGroupsGet(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, includeColocationStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProximityPlacementGroupsApi#proximityPlacementGroupsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **includeColocationStatus** | **String**| includeColocationStatus&#x3D;true enables fetching the colocation status of all the resources in the proximity placement group. | [optional] |

### Return type

[**ProximityPlacementGroup**](ProximityPlacementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="proximityPlacementGroupsListByResourceGroup"></a>
# **proximityPlacementGroupsListByResourceGroup**
> ProximityPlacementGroupListResult proximityPlacementGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all proximity placement groups in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProximityPlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProximityPlacementGroupsApi apiInstance = new ProximityPlacementGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ProximityPlacementGroupListResult result = apiInstance.proximityPlacementGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProximityPlacementGroupsApi#proximityPlacementGroupsListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ProximityPlacementGroupListResult**](ProximityPlacementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="proximityPlacementGroupsListBySubscription"></a>
# **proximityPlacementGroupsListBySubscription**
> ProximityPlacementGroupListResult proximityPlacementGroupsListBySubscription(apiVersion, subscriptionId)



Lists all proximity placement groups in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProximityPlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProximityPlacementGroupsApi apiInstance = new ProximityPlacementGroupsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ProximityPlacementGroupListResult result = apiInstance.proximityPlacementGroupsListBySubscription(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProximityPlacementGroupsApi#proximityPlacementGroupsListBySubscription");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ProximityPlacementGroupListResult**](ProximityPlacementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="proximityPlacementGroupsUpdate"></a>
# **proximityPlacementGroupsUpdate**
> ProximityPlacementGroup proximityPlacementGroupsUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters)



Update a proximity placement group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProximityPlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProximityPlacementGroupsApi apiInstance = new ProximityPlacementGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ProximityPlacementGroupUpdate parameters = new ProximityPlacementGroupUpdate(); // ProximityPlacementGroupUpdate | Parameters supplied to the Update Proximity Placement Group operation.
    try {
      ProximityPlacementGroup result = apiInstance.proximityPlacementGroupsUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProximityPlacementGroupsApi#proximityPlacementGroupsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ProximityPlacementGroupUpdate**](ProximityPlacementGroupUpdate.md)| Parameters supplied to the Update Proximity Placement Group operation. | |

### Return type

[**ProximityPlacementGroup**](ProximityPlacementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |


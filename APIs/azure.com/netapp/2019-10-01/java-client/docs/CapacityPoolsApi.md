# CapacityPoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**poolsCreateOrUpdate**](CapacityPoolsApi.md#poolsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName} | Create or Update the specified capacity pool within the resource group |
| [**poolsDelete**](CapacityPoolsApi.md#poolsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName} | Delete a capacity pool |
| [**poolsGet**](CapacityPoolsApi.md#poolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName} | Describe a Capacity Pool |
| [**poolsList**](CapacityPoolsApi.md#poolsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools | Describe all Capacity Pools |
| [**poolsUpdate**](CapacityPoolsApi.md#poolsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName} | Update a capacity pool |


<a id="poolsCreateOrUpdate"></a>
# **poolsCreateOrUpdate**
> CapacityPool poolsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, poolName, apiVersion, body)

Create or Update the specified capacity pool within the resource group

Create or Update a capacity pool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacityPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacityPoolsApi apiInstance = new CapacityPoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    CapacityPool body = new CapacityPool(); // CapacityPool | Capacity pool object supplied in the body of the operation.
    try {
      CapacityPool result = apiInstance.poolsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, poolName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacityPoolsApi#poolsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |
| **body** | [**CapacityPool**](CapacityPool.md)| Capacity pool object supplied in the body of the operation. | |

### Return type

[**CapacityPool**](CapacityPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - pool updated |  -  |
| **201** | Pool created |  -  |
| **202** | Accepted -- Create, update or delete request accepted; operation will complete asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolsDelete"></a>
# **poolsDelete**
> poolsDelete(subscriptionId, resourceGroupName, accountName, poolName, apiVersion)

Delete a capacity pool

Delete the specified capacity pool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacityPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacityPoolsApi apiInstance = new CapacityPoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.poolsDelete(subscriptionId, resourceGroupName, accountName, poolName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacityPoolsApi#poolsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

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
| **202** | Accepted -- Create, update or delete request accepted; operation will complete asynchronously |  -  |
| **204** | NoContent -- Resource does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="poolsGet"></a>
# **poolsGet**
> CapacityPool poolsGet(subscriptionId, resourceGroupName, accountName, poolName, apiVersion)

Describe a Capacity Pool

Get details of the specified capacity pool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacityPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacityPoolsApi apiInstance = new CapacityPoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      CapacityPool result = apiInstance.poolsGet(subscriptionId, resourceGroupName, accountName, poolName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacityPoolsApi#poolsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

### Return type

[**CapacityPool**](CapacityPool.md)

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

<a id="poolsList"></a>
# **poolsList**
> CapacityPoolList poolsList(subscriptionId, resourceGroupName, accountName, apiVersion)

Describe all Capacity Pools

List all capacity pools in the NetApp Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacityPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacityPoolsApi apiInstance = new CapacityPoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      CapacityPoolList result = apiInstance.poolsList(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacityPoolsApi#poolsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

### Return type

[**CapacityPoolList**](CapacityPoolList.md)

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

<a id="poolsUpdate"></a>
# **poolsUpdate**
> CapacityPool poolsUpdate(subscriptionId, resourceGroupName, accountName, poolName, apiVersion, body)

Update a capacity pool

Patch the specified capacity pool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacityPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CapacityPoolsApi apiInstance = new CapacityPoolsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    CapacityPoolPatch body = new CapacityPoolPatch(); // CapacityPoolPatch | Capacity pool object supplied in the body of the operation.
    try {
      CapacityPool result = apiInstance.poolsUpdate(subscriptionId, resourceGroupName, accountName, poolName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacityPoolsApi#poolsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |
| **body** | [**CapacityPoolPatch**](CapacityPoolPatch.md)| Capacity pool object supplied in the body of the operation. | |

### Return type

[**CapacityPool**](CapacityPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted -- Create, update or delete request accepted; operation will complete asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |


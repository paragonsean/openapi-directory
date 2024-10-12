# PeeringRegisteredPrefixesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registeredPrefixesCreateOrUpdate**](PeeringRegisteredPrefixesApi.md#registeredPrefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes/{registeredPrefixName} |  |
| [**registeredPrefixesDelete**](PeeringRegisteredPrefixesApi.md#registeredPrefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes/{registeredPrefixName} |  |
| [**registeredPrefixesGet**](PeeringRegisteredPrefixesApi.md#registeredPrefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes/{registeredPrefixName} |  |
| [**registeredPrefixesListByPeering**](PeeringRegisteredPrefixesApi.md#registeredPrefixesListByPeering) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredPrefixes |  |


<a id="registeredPrefixesCreateOrUpdate"></a>
# **registeredPrefixesCreateOrUpdate**
> PeeringRegisteredPrefix registeredPrefixesCreateOrUpdate(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion, registeredPrefix)



Creates a new registered prefix with the specified name under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredPrefixesApi apiInstance = new PeeringRegisteredPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String registeredPrefixName = "registeredPrefixName_example"; // String | The name of the registered prefix.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    PeeringRegisteredPrefix registeredPrefix = new PeeringRegisteredPrefix(); // PeeringRegisteredPrefix | The properties needed to create a registered prefix.
    try {
      PeeringRegisteredPrefix result = apiInstance.registeredPrefixesCreateOrUpdate(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion, registeredPrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredPrefixesApi#registeredPrefixesCreateOrUpdate");
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
| **peeringName** | **String**| The name of the peering. | |
| **registeredPrefixName** | **String**| The name of the registered prefix. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **registeredPrefix** | [**PeeringRegisteredPrefix**](PeeringRegisteredPrefix.md)| The properties needed to create a registered prefix. | |

### Return type

[**PeeringRegisteredPrefix**](PeeringRegisteredPrefix.md)

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
| **0** | Error response describing why the operation has failed. |  -  |

<a id="registeredPrefixesDelete"></a>
# **registeredPrefixesDelete**
> registeredPrefixesDelete(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion)



Deletes an existing registered prefix with the specified name under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredPrefixesApi apiInstance = new PeeringRegisteredPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String registeredPrefixName = "registeredPrefixName_example"; // String | The name of the registered prefix.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.registeredPrefixesDelete(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredPrefixesApi#registeredPrefixesDelete");
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
| **peeringName** | **String**| The name of the peering. | |
| **registeredPrefixName** | **String**| The name of the registered prefix. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

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
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

<a id="registeredPrefixesGet"></a>
# **registeredPrefixesGet**
> PeeringRegisteredPrefix registeredPrefixesGet(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion)



Gets an existing registered prefix with the specified name under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredPrefixesApi apiInstance = new PeeringRegisteredPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String registeredPrefixName = "registeredPrefixName_example"; // String | The name of the registered prefix.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringRegisteredPrefix result = apiInstance.registeredPrefixesGet(resourceGroupName, peeringName, registeredPrefixName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredPrefixesApi#registeredPrefixesGet");
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
| **peeringName** | **String**| The name of the peering. | |
| **registeredPrefixName** | **String**| The name of the registered prefix. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringRegisteredPrefix**](PeeringRegisteredPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation has failed. |  -  |

<a id="registeredPrefixesListByPeering"></a>
# **registeredPrefixesListByPeering**
> PeeringRegisteredPrefixListResult registeredPrefixesListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion)



Lists all registered prefixes under the given subscription, resource group and peering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringRegisteredPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringRegisteredPrefixesApi apiInstance = new PeeringRegisteredPrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringName = "peeringName_example"; // String | The name of the peering.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringRegisteredPrefixListResult result = apiInstance.registeredPrefixesListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringRegisteredPrefixesApi#registeredPrefixesListByPeering");
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
| **peeringName** | **String**| The name of the peering. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringRegisteredPrefixListResult**](PeeringRegisteredPrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation has failed. |  -  |


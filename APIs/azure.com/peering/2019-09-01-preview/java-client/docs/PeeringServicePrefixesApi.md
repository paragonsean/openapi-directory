# PeeringServicePrefixesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**prefixesCreateOrUpdate**](PeeringServicePrefixesApi.md#prefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} |  |
| [**prefixesDelete**](PeeringServicePrefixesApi.md#prefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} |  |
| [**prefixesGet**](PeeringServicePrefixesApi.md#prefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} |  |
| [**prefixesListByPeeringService**](PeeringServicePrefixesApi.md#prefixesListByPeeringService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes |  |


<a id="prefixesCreateOrUpdate"></a>
# **prefixesCreateOrUpdate**
> PeeringServicePrefix prefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix)



Creates a new prefix with the specified name under the given subscription, resource group and peering service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicePrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicePrefixesApi apiInstance = new PeeringServicePrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
    String prefixName = "prefixName_example"; // String | The name of the prefix.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    PeeringServicePrefix peeringServicePrefix = new PeeringServicePrefix(); // PeeringServicePrefix | The properties needed to create a prefix.
    try {
      PeeringServicePrefix result = apiInstance.prefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicePrefixesApi#prefixesCreateOrUpdate");
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
| **peeringServiceName** | **String**| The name of the peering service. | |
| **prefixName** | **String**| The name of the prefix. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **peeringServicePrefix** | [**PeeringServicePrefix**](PeeringServicePrefix.md)| The properties needed to create a prefix. | |

### Return type

[**PeeringServicePrefix**](PeeringServicePrefix.md)

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

<a id="prefixesDelete"></a>
# **prefixesDelete**
> prefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion)



Deletes an existing prefix with the specified name under the given subscription, resource group and peering service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicePrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicePrefixesApi apiInstance = new PeeringServicePrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
    String prefixName = "prefixName_example"; // String | The name of the prefix.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.prefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicePrefixesApi#prefixesDelete");
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
| **peeringServiceName** | **String**| The name of the peering service. | |
| **prefixName** | **String**| The name of the prefix. | |
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

<a id="prefixesGet"></a>
# **prefixesGet**
> PeeringServicePrefix prefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, $expand)



Gets an existing prefix with the specified name under the given subscription, resource group and peering service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicePrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicePrefixesApi apiInstance = new PeeringServicePrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
    String prefixName = "prefixName_example"; // String | The name of the prefix.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String $expand = "$expand_example"; // String | The properties to be expanded.
    try {
      PeeringServicePrefix result = apiInstance.prefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicePrefixesApi#prefixesGet");
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
| **peeringServiceName** | **String**| The name of the peering service. | |
| **prefixName** | **String**| The name of the prefix. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **$expand** | **String**| The properties to be expanded. | [optional] |

### Return type

[**PeeringServicePrefix**](PeeringServicePrefix.md)

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

<a id="prefixesListByPeeringService"></a>
# **prefixesListByPeeringService**
> PeeringServicePrefixListResult prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, $expand)



Lists all prefixes under the given subscription, resource group and peering service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicePrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicePrefixesApi apiInstance = new PeeringServicePrefixesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String $expand = "$expand_example"; // String | The properties to be expanded.
    try {
      PeeringServicePrefixListResult result = apiInstance.prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicePrefixesApi#prefixesListByPeeringService");
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
| **peeringServiceName** | **String**| The name of the peering service. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **$expand** | **String**| The properties to be expanded. | [optional] |

### Return type

[**PeeringServicePrefixListResult**](PeeringServicePrefixListResult.md)

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


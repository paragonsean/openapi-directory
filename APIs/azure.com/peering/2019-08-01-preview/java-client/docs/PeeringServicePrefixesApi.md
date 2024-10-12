# PeeringServicePrefixesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**peeringServicePrefixesCreateOrUpdate**](PeeringServicePrefixesApi.md#peeringServicePrefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} |  |
| [**peeringServicePrefixesDelete**](PeeringServicePrefixesApi.md#peeringServicePrefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} |  |
| [**peeringServicePrefixesGet**](PeeringServicePrefixesApi.md#peeringServicePrefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} |  |
| [**prefixesListByPeeringService**](PeeringServicePrefixesApi.md#prefixesListByPeeringService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes |  |


<a id="peeringServicePrefixesCreateOrUpdate"></a>
# **peeringServicePrefixesCreateOrUpdate**
> PeeringServicePrefix peeringServicePrefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix)



Creates or updates the peering prefix.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
    String prefixName = "prefixName_example"; // String | The prefix name
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    PeeringServicePrefix peeringServicePrefix = new PeeringServicePrefix(); // PeeringServicePrefix | The IP prefix for an peering
    try {
      PeeringServicePrefix result = apiInstance.peeringServicePrefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicePrefixesApi#peeringServicePrefixesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **peeringServiceName** | **String**| The peering service name. | |
| **prefixName** | **String**| The prefix name | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |
| **peeringServicePrefix** | [**PeeringServicePrefix**](PeeringServicePrefix.md)| The IP prefix for an peering | |

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

<a id="peeringServicePrefixesDelete"></a>
# **peeringServicePrefixesDelete**
> peeringServicePrefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion)



removes the peering prefix.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
    String prefixName = "prefixName_example"; // String | The prefix name
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.peeringServicePrefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicePrefixesApi#peeringServicePrefixesDelete");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **peeringServiceName** | **String**| The peering service name. | |
| **prefixName** | **String**| The prefix name | |
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

<a id="peeringServicePrefixesGet"></a>
# **peeringServicePrefixesGet**
> PeeringServicePrefix peeringServicePrefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion)



Gets the peering service prefix.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
    String prefixName = "prefixName_example"; // String | The prefix name.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringServicePrefix result = apiInstance.peeringServicePrefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicePrefixesApi#peeringServicePrefixesGet");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **peeringServiceName** | **String**| The peering service name. | |
| **prefixName** | **String**| The prefix name. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

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
> PeeringServicePrefixListResult prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion)



Lists the peerings prefix in the resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringServicePrefixListResult result = apiInstance.prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion);
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
| **resourceGroupName** | **String**| The resource group name. | |
| **peeringServiceName** | **String**| The peering service name. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

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


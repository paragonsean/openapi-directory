# PeeringServicesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**peeringServicesCreateOrUpdate**](PeeringServicesApi.md#peeringServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} |  |
| [**peeringServicesDelete**](PeeringServicesApi.md#peeringServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} |  |
| [**peeringServicesGet**](PeeringServicesApi.md#peeringServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} |  |
| [**peeringServicesListByResourceGroup**](PeeringServicesApi.md#peeringServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices |  |
| [**peeringServicesListBySubscription**](PeeringServicesApi.md#peeringServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peeringServices |  |
| [**peeringServicesUpdate**](PeeringServicesApi.md#peeringServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} |  |


<a id="peeringServicesCreateOrUpdate"></a>
# **peeringServicesCreateOrUpdate**
> PeeringService peeringServicesCreateOrUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, peeringService)



Creates a new peering service or updates an existing peering with the specified name under the given subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicesApi apiInstance = new PeeringServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    PeeringService peeringService = new PeeringService(); // PeeringService | The properties needed to create or update a peering service.
    try {
      PeeringService result = apiInstance.peeringServicesCreateOrUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, peeringService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicesApi#peeringServicesCreateOrUpdate");
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
| **peeringService** | [**PeeringService**](PeeringService.md)| The properties needed to create or update a peering service. | |

### Return type

[**PeeringService**](PeeringService.md)

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

<a id="peeringServicesDelete"></a>
# **peeringServicesDelete**
> peeringServicesDelete(resourceGroupName, peeringServiceName, subscriptionId, apiVersion)



Deletes an existing peering service with the specified name under the given subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicesApi apiInstance = new PeeringServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.peeringServicesDelete(resourceGroupName, peeringServiceName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicesApi#peeringServicesDelete");
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

<a id="peeringServicesGet"></a>
# **peeringServicesGet**
> PeeringService peeringServicesGet(resourceGroupName, peeringServiceName, subscriptionId, apiVersion)



Gets an existing peering service with the specified name under the given subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicesApi apiInstance = new PeeringServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringService result = apiInstance.peeringServicesGet(resourceGroupName, peeringServiceName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicesApi#peeringServicesGet");
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
| **peeringServiceName** | **String**| The name of the peering. | |
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringService**](PeeringService.md)

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

<a id="peeringServicesListByResourceGroup"></a>
# **peeringServicesListByResourceGroup**
> PeeringServiceListResult peeringServicesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Lists all of the peering services under the given subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicesApi apiInstance = new PeeringServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringServiceListResult result = apiInstance.peeringServicesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicesApi#peeringServicesListByResourceGroup");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringServiceListResult**](PeeringServiceListResult.md)

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

<a id="peeringServicesListBySubscription"></a>
# **peeringServicesListBySubscription**
> PeeringServiceListResult peeringServicesListBySubscription(subscriptionId, apiVersion)



Lists all of the peerings under the given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicesApi apiInstance = new PeeringServicesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PeeringServiceListResult result = apiInstance.peeringServicesListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicesApi#peeringServicesListBySubscription");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**PeeringServiceListResult**](PeeringServiceListResult.md)

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

<a id="peeringServicesUpdate"></a>
# **peeringServicesUpdate**
> PeeringService peeringServicesUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, tags)



Updates tags for a peering service with the specified name under the given subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeeringServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PeeringServicesApi apiInstance = new PeeringServicesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    ResourceTags tags = new ResourceTags(); // ResourceTags | The resource tags.
    try {
      PeeringService result = apiInstance.peeringServicesUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeeringServicesApi#peeringServicesUpdate");
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
| **tags** | [**ResourceTags**](ResourceTags.md)| The resource tags. | |

### Return type

[**PeeringService**](PeeringService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation has failed. |  -  |


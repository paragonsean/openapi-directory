# ElasticPoolsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**elasticPoolsCreateOrUpdate**](ElasticPoolsApi.md#elasticPoolsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |
| [**elasticPoolsDelete**](ElasticPoolsApi.md#elasticPoolsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |
| [**elasticPoolsGet**](ElasticPoolsApi.md#elasticPoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |
| [**elasticPoolsListByServer**](ElasticPoolsApi.md#elasticPoolsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools |  |
| [**elasticPoolsUpdate**](ElasticPoolsApi.md#elasticPoolsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} |  |


<a id="elasticPoolsCreateOrUpdate"></a>
# **elasticPoolsCreateOrUpdate**
> ElasticPool elasticPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters)



Creates a new elastic pool or updates an existing elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be operated on (updated or created).
    ElasticPool parameters = new ElasticPool(); // ElasticPool | The required parameters for creating or updating an elastic pool.
    try {
      ElasticPool result = apiInstance.elasticPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsCreateOrUpdate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **elasticPoolName** | **String**| The name of the elastic pool to be operated on (updated or created). | |
| **parameters** | [**ElasticPool**](ElasticPool.md)| The required parameters for creating or updating an elastic pool. | |

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |

<a id="elasticPoolsDelete"></a>
# **elasticPoolsDelete**
> elasticPoolsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Deletes the elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be deleted.
    try {
      apiInstance.elasticPoolsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsDelete");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **elasticPoolName** | **String**| The name of the elastic pool to be deleted. | |

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
| **200** | OK |  -  |
| **204** | Accepted |  -  |

<a id="elasticPoolsGet"></a>
# **elasticPoolsGet**
> ElasticPool elasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Gets an elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be retrieved.
    try {
      ElasticPool result = apiInstance.elasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsGet");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **elasticPoolName** | **String**| The name of the elastic pool to be retrieved. | |

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="elasticPoolsListByServer"></a>
# **elasticPoolsListByServer**
> ElasticPoolListResult elasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Returns a list of elastic pools in a server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    try {
      ElasticPoolListResult result = apiInstance.elasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsListByServer");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |

### Return type

[**ElasticPoolListResult**](ElasticPoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="elasticPoolsUpdate"></a>
# **elasticPoolsUpdate**
> ElasticPool elasticPoolsUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters)



Updates an existing elastic pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElasticPoolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ElasticPoolsApi apiInstance = new ElasticPoolsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be updated.
    ElasticPoolUpdate parameters = new ElasticPoolUpdate(); // ElasticPoolUpdate | The required parameters for updating an elastic pool.
    try {
      ElasticPool result = apiInstance.elasticPoolsUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElasticPoolsApi#elasticPoolsUpdate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **elasticPoolName** | **String**| The name of the elastic pool to be updated. | |
| **parameters** | [**ElasticPoolUpdate**](ElasticPoolUpdate.md)| The required parameters for updating an elastic pool. | |

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |


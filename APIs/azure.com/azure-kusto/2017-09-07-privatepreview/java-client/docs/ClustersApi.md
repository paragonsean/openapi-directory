# ClustersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clustersCheckNameAvailability**](ClustersApi.md#clustersCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Kusto/locations/{location}/checkNameAvailability |  |
| [**clustersCreateOrUpdate**](ClustersApi.md#clustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} |  |
| [**clustersDelete**](ClustersApi.md#clustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} |  |
| [**clustersGet**](ClustersApi.md#clustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} |  |
| [**clustersList**](ClustersApi.md#clustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Kusto/clusters |  |
| [**clustersListByResourceGroup**](ClustersApi.md#clustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters |  |
| [**clustersListSkusByResource**](ClustersApi.md#clustersListSkusByResource) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/skus |  |
| [**clustersStart**](ClustersApi.md#clustersStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/start |  |
| [**clustersStop**](ClustersApi.md#clustersStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/stop |  |
| [**clustersUpdate**](ClustersApi.md#clustersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName} |  |


<a id="clustersCheckNameAvailability"></a>
# **clustersCheckNameAvailability**
> CheckNameResult clustersCheckNameAvailability(apiVersion, subscriptionId, location, clusterName)



Checks that the cluster name is valid and is not already in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Azure location.
    ClusterCheckNameRequest clusterName = new ClusterCheckNameRequest(); // ClusterCheckNameRequest | The name of the cluster.
    try {
      CheckNameResult result = apiInstance.clustersCheckNameAvailability(apiVersion, subscriptionId, location, clusterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersCheckNameAvailability");
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
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Azure location. | |
| **clusterName** | [**ClusterCheckNameRequest**](ClusterCheckNameRequest.md)| The name of the cluster. | |

### Return type

[**CheckNameResult**](CheckNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Operation to check the kusto resource name availability was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersCreateOrUpdate"></a>
# **clustersCreateOrUpdate**
> Cluster clustersCreateOrUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters)



Create or update a Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Cluster parameters = new Cluster(); // Cluster | The Kusto cluster parameters supplied to the CreateOrUpdate operation.
    try {
      Cluster result = apiInstance.clustersCreateOrUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |
| **parameters** | [**Cluster**](Cluster.md)| The Kusto cluster parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the Cluster. |  -  |
| **201** | Successfully created the cluster. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersDelete"></a>
# **clustersDelete**
> clustersDelete(resourceGroupName, clusterName, subscriptionId, apiVersion)



Deletes a Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      apiInstance.clustersDelete(resourceGroupName, clusterName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersDelete");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- cluster deleted successfully. |  -  |
| **202** | Accepted the delete cluster request. |  -  |
| **204** | NoContent -- cluster does not exist in the subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersGet"></a>
# **clustersGet**
> Cluster clustersGet(resourceGroupName, clusterName, subscriptionId, apiVersion)



Gets a Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      Cluster result = apiInstance.clustersGet(resourceGroupName, clusterName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersGet");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Kusto cluster. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersList"></a>
# **clustersList**
> ClusterListResult clustersList(subscriptionId, apiVersion)



Lists all Kusto clusters within a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      ClusterListResult result = apiInstance.clustersList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersList");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersListByResourceGroup"></a>
# **clustersListByResourceGroup**
> ClusterListResult clustersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Lists all Kusto clusters within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      ClusterListResult result = apiInstance.clustersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersListSkusByResource"></a>
# **clustersListSkusByResource**
> ListResourceSkusResult clustersListSkusByResource(resourceGroupName, clusterName, apiVersion, subscriptionId)



Returns the SKUs available for the provided resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ListResourceSkusResult result = apiInstance.clustersListSkusByResource(resourceGroupName, clusterName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersListSkusByResource");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ListResourceSkusResult**](ListResourceSkusResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersStart"></a>
# **clustersStart**
> clustersStart(resourceGroupName, clusterName, subscriptionId, apiVersion)



Starts a Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      apiInstance.clustersStart(resourceGroupName, clusterName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersStart");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Accepted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersStop"></a>
# **clustersStop**
> clustersStop(resourceGroupName, clusterName, subscriptionId, apiVersion)



Stops a Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      apiInstance.clustersStop(resourceGroupName, clusterName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersStop");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="clustersUpdate"></a>
# **clustersUpdate**
> Cluster clustersUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters)



Update a Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ClustersApi apiInstance = new ClustersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    ClusterUpdate parameters = new ClusterUpdate(); // ClusterUpdate | The Kusto cluster parameters supplied to the Update operation.
    try {
      Cluster result = apiInstance.clustersUpdate(resourceGroupName, clusterName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClustersApi#clustersUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |
| **parameters** | [**ClusterUpdate**](ClusterUpdate.md)| The Kusto cluster parameters supplied to the Update operation. | |

### Return type

[**Cluster**](Cluster.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the Cluster. |  -  |
| **201** | Successfully updated the cluster. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


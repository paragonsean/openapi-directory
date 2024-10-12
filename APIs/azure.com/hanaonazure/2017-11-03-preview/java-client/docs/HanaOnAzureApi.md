# HanaOnAzureApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hanaInstancesCreate**](HanaOnAzureApi.md#hanaInstancesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Creates a SAP HANA instance. |
| [**hanaInstancesDelete**](HanaOnAzureApi.md#hanaInstancesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Deletes a SAP HANA instance. |
| [**hanaInstancesGet**](HanaOnAzureApi.md#hanaInstancesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Gets properties of a SAP HANA instance. |
| [**hanaInstancesList**](HanaOnAzureApi.md#hanaInstancesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HanaOnAzure/hanaInstances | Gets a list of SAP HANA instances in the specified subscription. |
| [**hanaInstancesListByResourceGroup**](HanaOnAzureApi.md#hanaInstancesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances | Gets a list of SAP HANA instances in the specified subscription and the resource group. |
| [**hanaInstancesRestart**](HanaOnAzureApi.md#hanaInstancesRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName}/restart |  |
| [**hanaInstancesShutdown**](HanaOnAzureApi.md#hanaInstancesShutdown) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName}/shutdown |  |
| [**hanaInstancesStart**](HanaOnAzureApi.md#hanaInstancesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName}/start |  |
| [**hanaInstancesUpdate**](HanaOnAzureApi.md#hanaInstancesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Patches the Tags field of a SAP HANA instance. |
| [**operationsList**](HanaOnAzureApi.md#operationsList) | **GET** /providers/Microsoft.HanaOnAzure/operations |  |
| [**sapMonitorsCreate**](HanaOnAzureApi.md#sapMonitorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Creates a SAP monitor. |
| [**sapMonitorsDelete**](HanaOnAzureApi.md#sapMonitorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Deletes a SAP monitor. |
| [**sapMonitorsGet**](HanaOnAzureApi.md#sapMonitorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Gets properties of a SAP monitor. |
| [**sapMonitorsList**](HanaOnAzureApi.md#sapMonitorsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HanaOnAzure/sapMonitors | Gets a list of SAP monitors in the specified subscription. |
| [**sapMonitorsUpdate**](HanaOnAzureApi.md#sapMonitorsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Patches the Tags field of a SAP monitor. |


<a id="hanaInstancesCreate"></a>
# **hanaInstancesCreate**
> HanaInstance hanaInstancesCreate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, hanaInstanceParameter)

Creates a SAP HANA instance.

Creates a SAP HANA instance for the specified subscription, resource group, and instance name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
    HanaInstance hanaInstanceParameter = new HanaInstance(); // HanaInstance | Request body representing a HanaInstance
    try {
      HanaInstance result = apiInstance.hanaInstancesCreate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, hanaInstanceParameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesCreate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | |
| **hanaInstanceParameter** | [**HanaInstance**](HanaInstance.md)| Request body representing a HanaInstance | |

### Return type

[**HanaInstance**](HanaInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created HanaInstance |  -  |
| **201** | Creating HanaInstance |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesDelete"></a>
# **hanaInstancesDelete**
> hanaInstancesDelete(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)

Deletes a SAP HANA instance.

Deletes a SAP HANA instance with the specified subscription, resource group, and instance name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
    try {
      apiInstance.hanaInstancesDelete(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesDelete");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | |

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
| **200** | Deleted HanaInstance |  -  |
| **202** | Deleting HanaInstance |  -  |
| **204** | No HanaInstance to delete |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesGet"></a>
# **hanaInstancesGet**
> HanaInstance hanaInstancesGet(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)

Gets properties of a SAP HANA instance.

Gets properties of a SAP HANA instance for the specified subscription, resource group, and instance name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
    try {
      HanaInstance result = apiInstance.hanaInstancesGet(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesGet");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | |

### Return type

[**HanaInstance**](HanaInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesList"></a>
# **hanaInstancesList**
> HanaInstancesListResult hanaInstancesList(apiVersion, subscriptionId)

Gets a list of SAP HANA instances in the specified subscription.

Gets a list of SAP HANA instances in the specified subscription. The operations returns various properties of each SAP HANA on Azure instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      HanaInstancesListResult result = apiInstance.hanaInstancesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesList");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**HanaInstancesListResult**](HanaInstancesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesListByResourceGroup"></a>
# **hanaInstancesListByResourceGroup**
> HanaInstancesListResult hanaInstancesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Gets a list of SAP HANA instances in the specified subscription and the resource group.

Gets a list of SAP HANA instances in the specified subscription and the resource group. The operations returns various properties of each SAP HANA on Azure instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    try {
      HanaInstancesListResult result = apiInstance.hanaInstancesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |

### Return type

[**HanaInstancesListResult**](HanaInstancesListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesRestart"></a>
# **hanaInstancesRestart**
> hanaInstancesRestart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)



The operation to restart a SAP HANA instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
    try {
      apiInstance.hanaInstancesRestart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesRestart");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesShutdown"></a>
# **hanaInstancesShutdown**
> hanaInstancesShutdown(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)



The operation to shutdown a SAP HANA instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
    try {
      apiInstance.hanaInstancesShutdown(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesShutdown");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesStart"></a>
# **hanaInstancesStart**
> hanaInstancesStart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)



The operation to start a SAP HANA instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
    try {
      apiInstance.hanaInstancesStart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesStart");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hanaInstancesUpdate"></a>
# **hanaInstancesUpdate**
> HanaInstance hanaInstancesUpdate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, tagsParameter)

Patches the Tags field of a SAP HANA instance.

Patches the Tags field of a SAP HANA instance for the specified subscription, resource group, and instance name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
    Tags tagsParameter = new Tags(); // Tags | Request body that only contains the new Tags field
    try {
      HanaInstance result = apiInstance.hanaInstancesUpdate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, tagsParameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#hanaInstancesUpdate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | |
| **tagsParameter** | [**Tags**](Tags.md)| Request body that only contains the new Tags field | |

### Return type

[**HanaInstance**](HanaInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="operationsList"></a>
# **operationsList**
> OperationList operationsList(apiVersion)



Gets a list of SAP HANA management operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      OperationList result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#operationsList");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**OperationList**](OperationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sapMonitorsCreate"></a>
# **sapMonitorsCreate**
> SapMonitor sapMonitorsCreate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, sapMonitorParameter)

Creates a SAP monitor.

Creates a SAP monitor for the specified subscription, resource group, and resource name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
    SapMonitor sapMonitorParameter = new SapMonitor(); // SapMonitor | Request body representing a SAP Monitor
    try {
      SapMonitor result = apiInstance.sapMonitorsCreate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, sapMonitorParameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#sapMonitorsCreate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **sapMonitorName** | **String**| Name of the SAP monitor resource. | |
| **sapMonitorParameter** | [**SapMonitor**](SapMonitor.md)| Request body representing a SAP Monitor | |

### Return type

[**SapMonitor**](SapMonitor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created SapMonitor |  -  |
| **201** | Creating SapMonitor |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sapMonitorsDelete"></a>
# **sapMonitorsDelete**
> sapMonitorsDelete(apiVersion, subscriptionId, resourceGroupName, sapMonitorName)

Deletes a SAP monitor.

Deletes a SAP monitor with the specified subscription, resource group, and monitor name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
    try {
      apiInstance.sapMonitorsDelete(apiVersion, subscriptionId, resourceGroupName, sapMonitorName);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#sapMonitorsDelete");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **sapMonitorName** | **String**| Name of the SAP monitor resource. | |

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
| **200** | Deleted SapMonitor |  -  |
| **202** | Deleting SapMonitor |  -  |
| **204** | No SapMonitor to delete |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sapMonitorsGet"></a>
# **sapMonitorsGet**
> SapMonitor sapMonitorsGet(apiVersion, subscriptionId, resourceGroupName, sapMonitorName)

Gets properties of a SAP monitor.

Gets properties of a SAP monitor for the specified subscription, resource group, and resource name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
    try {
      SapMonitor result = apiInstance.sapMonitorsGet(apiVersion, subscriptionId, resourceGroupName, sapMonitorName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#sapMonitorsGet");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **sapMonitorName** | **String**| Name of the SAP monitor resource. | |

### Return type

[**SapMonitor**](SapMonitor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sapMonitorsList"></a>
# **sapMonitorsList**
> SapMonitorListResult sapMonitorsList(apiVersion, subscriptionId)

Gets a list of SAP monitors in the specified subscription.

Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SapMonitorListResult result = apiInstance.sapMonitorsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#sapMonitorsList");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SapMonitorListResult**](SapMonitorListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="sapMonitorsUpdate"></a>
# **sapMonitorsUpdate**
> SapMonitor sapMonitorsUpdate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, tagsParameter)

Patches the Tags field of a SAP monitor.

Patches the Tags field of a SAP monitor for the specified subscription, resource group, and monitor name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HanaOnAzureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    HanaOnAzureApi apiInstance = new HanaOnAzureApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
    String sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
    Tags tagsParameter = new Tags(); // Tags | Request body that only contains the new Tags field
    try {
      SapMonitor result = apiInstance.sapMonitorsUpdate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, tagsParameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HanaOnAzureApi#sapMonitorsUpdate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group. | |
| **sapMonitorName** | **String**| Name of the SAP monitor resource. | |
| **tagsParameter** | [**Tags**](Tags.md)| Request body that only contains the new Tags field | |

### Return type

[**SapMonitor**](SapMonitor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |


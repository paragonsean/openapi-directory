# FarmsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**farmsCreate**](FarmsApi.md#farmsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId} |  |
| [**farmsGet**](FarmsApi.md#farmsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId} |  |
| [**farmsList**](FarmsApi.md#farmsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms |  |
| [**farmsListMetricDefinitions**](FarmsApi.md#farmsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/metricdefinitions |  |
| [**farmsListMetrics**](FarmsApi.md#farmsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/metrics |  |
| [**farmsStartGarbageCollection**](FarmsApi.md#farmsStartGarbageCollection) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId}/ondemandgc |  |
| [**farmsUpdate**](FarmsApi.md#farmsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage.Admin/farms/{farmId} |  |


<a id="farmsCreate"></a>
# **farmsCreate**
> Farm farmsCreate(subscriptionId, resourceGroupName, farmId, apiVersion, farmObject)



Create a new storage farm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FarmsApi apiInstance = new FarmsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    FarmCreationProperties farmObject = new FarmCreationProperties(); // FarmCreationProperties | Parameters used to create a farm
    try {
      Farm result = apiInstance.farmsCreate(subscriptionId, resourceGroupName, farmId, apiVersion, farmObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmsApi#farmsCreate");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **apiVersion** | **String**| REST Api Version. | |
| **farmObject** | [**FarmCreationProperties**](FarmCreationProperties.md)| Parameters used to create a farm | |

### Return type

[**Farm**](Farm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The new storage farm has been created. |  -  |

<a id="farmsGet"></a>
# **farmsGet**
> Farm farmsGet(subscriptionId, resourceGroupName, farmId, apiVersion)



Returns the Storage properties and settings for a specified storage farm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FarmsApi apiInstance = new FarmsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      Farm result = apiInstance.farmsGet(subscriptionId, resourceGroupName, farmId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmsApi#farmsGet");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**Farm**](Farm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The farm has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

<a id="farmsList"></a>
# **farmsList**
> FarmList farmsList(subscriptionId, resourceGroupName, apiVersion)



Returns a list of all storage farms.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FarmsApi apiInstance = new FarmsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      FarmList result = apiInstance.farmsList(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmsApi#farmsList");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**FarmList**](FarmList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of storage farms has been returned. |  -  |

<a id="farmsListMetricDefinitions"></a>
# **farmsListMetricDefinitions**
> FarmsListMetricDefinitions200Response farmsListMetricDefinitions(subscriptionId, resourceGroupName, farmId, apiVersion)



Returns a list of metric definitions for a storage farm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FarmsApi apiInstance = new FarmsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      FarmsListMetricDefinitions200Response result = apiInstance.farmsListMetricDefinitions(subscriptionId, resourceGroupName, farmId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmsApi#farmsListMetricDefinitions");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**FarmsListMetricDefinitions200Response**](FarmsListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metric definitions has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

<a id="farmsListMetrics"></a>
# **farmsListMetrics**
> FarmsListMetrics200Response farmsListMetrics(subscriptionId, resourceGroupName, farmId, apiVersion)



Returns a list of storage farm metrics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FarmsApi apiInstance = new FarmsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      FarmsListMetrics200Response result = apiInstance.farmsListMetrics(subscriptionId, resourceGroupName, farmId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmsApi#farmsListMetrics");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **apiVersion** | **String**| REST Api Version. | |

### Return type

[**FarmsListMetrics200Response**](FarmsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The list of metrics has been returned. |  -  |
| **404** | NOT FOUND -- The specified farm was not found. |  -  |

<a id="farmsStartGarbageCollection"></a>
# **farmsStartGarbageCollection**
> farmsStartGarbageCollection(subscriptionId, resourceGroupName, farmId, apiVersion)



Start garbage collection on deleted storage objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FarmsApi apiInstance = new FarmsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    try {
      apiInstance.farmsStartGarbageCollection(subscriptionId, resourceGroupName, farmId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmsApi#farmsStartGarbageCollection");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **apiVersion** | **String**| REST Api Version. | |

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
| **200** | OK -- Garbage collection has completed. |  -  |
| **202** | ACCEPTED -- Garbage collection has started. |  -  |

<a id="farmsUpdate"></a>
# **farmsUpdate**
> Farm farmsUpdate(subscriptionId, apiVersion, resourceGroupName, farmId, farmObject)



Update an existing storage farm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FarmsApi apiInstance = new FarmsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id.
    String apiVersion = "apiVersion_example"; // String | REST Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String farmId = "farmId_example"; // String | Farm Id.
    Farm farmObject = new Farm(); // Farm | Farm to update.
    try {
      Farm result = apiInstance.farmsUpdate(subscriptionId, apiVersion, resourceGroupName, farmId, farmObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmsApi#farmsUpdate");
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
| **subscriptionId** | **String**| Subscription Id. | |
| **apiVersion** | **String**| REST Api Version. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **farmId** | **String**| Farm Id. | |
| **farmObject** | [**Farm**](Farm.md)| Farm to update. | |

### Return type

[**Farm**](Farm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The properties and settings of storage farm have been updated. |  -  |


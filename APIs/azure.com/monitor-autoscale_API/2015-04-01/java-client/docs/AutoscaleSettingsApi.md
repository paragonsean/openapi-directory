# AutoscaleSettingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoscaleSettingsCreateOrUpdate**](AutoscaleSettingsApi.md#autoscaleSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} |  |
| [**autoscaleSettingsDelete**](AutoscaleSettingsApi.md#autoscaleSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} |  |
| [**autoscaleSettingsGet**](AutoscaleSettingsApi.md#autoscaleSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} |  |
| [**autoscaleSettingsListByResourceGroup**](AutoscaleSettingsApi.md#autoscaleSettingsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings |  |
| [**autoscaleSettingsListBySubscription**](AutoscaleSettingsApi.md#autoscaleSettingsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/autoscalesettings |  |


<a id="autoscaleSettingsCreateOrUpdate"></a>
# **autoscaleSettingsCreateOrUpdate**
> AutoscaleSettingResource autoscaleSettingsCreateOrUpdate(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId, parameters)



Creates or updates an autoscale setting.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoscaleSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoscaleSettingsApi apiInstance = new AutoscaleSettingsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    AutoscaleSettingResource parameters = new AutoscaleSettingResource(); // AutoscaleSettingResource | Parameters supplied to the operation.
    try {
      AutoscaleSettingResource result = apiInstance.autoscaleSettingsCreateOrUpdate(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoscaleSettingsApi#autoscaleSettingsCreateOrUpdate");
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
| **autoscaleSettingName** | **String**| The autoscale setting name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **parameters** | [**AutoscaleSettingResource**](AutoscaleSettingResource.md)| Parameters supplied to the operation. | |

### Return type

[**AutoscaleSettingResource**](AutoscaleSettingResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to create or update an autoscale setting |  -  |
| **201** | Created autoscale setting |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="autoscaleSettingsDelete"></a>
# **autoscaleSettingsDelete**
> autoscaleSettingsDelete(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId)



Deletes and autoscale setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoscaleSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoscaleSettingsApi apiInstance = new AutoscaleSettingsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      apiInstance.autoscaleSettingsDelete(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoscaleSettingsApi#autoscaleSettingsDelete");
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
| **autoscaleSettingName** | **String**| The autoscale setting name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

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
| **200** | Successful request to delete an autoscale setting |  -  |
| **204** | No content: Successful request to delete an autoscale setting, but the response is intentionally empty |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="autoscaleSettingsGet"></a>
# **autoscaleSettingsGet**
> AutoscaleSettingResource autoscaleSettingsGet(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId)



Gets an autoscale setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoscaleSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoscaleSettingsApi apiInstance = new AutoscaleSettingsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      AutoscaleSettingResource result = apiInstance.autoscaleSettingsGet(resourceGroupName, autoscaleSettingName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoscaleSettingsApi#autoscaleSettingsGet");
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
| **autoscaleSettingName** | **String**| The autoscale setting name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**AutoscaleSettingResource**](AutoscaleSettingResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get one autoscale setting |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="autoscaleSettingsListByResourceGroup"></a>
# **autoscaleSettingsListByResourceGroup**
> AutoscaleSettingResourceCollection autoscaleSettingsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists the autoscale settings for a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoscaleSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoscaleSettingsApi apiInstance = new AutoscaleSettingsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      AutoscaleSettingResourceCollection result = apiInstance.autoscaleSettingsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoscaleSettingsApi#autoscaleSettingsListByResourceGroup");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**AutoscaleSettingResourceCollection**](AutoscaleSettingResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of autoscale settings |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="autoscaleSettingsListBySubscription"></a>
# **autoscaleSettingsListBySubscription**
> AutoscaleSettingResourceCollection autoscaleSettingsListBySubscription(apiVersion, subscriptionId)



Lists the autoscale settings for a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoscaleSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutoscaleSettingsApi apiInstance = new AutoscaleSettingsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      AutoscaleSettingResourceCollection result = apiInstance.autoscaleSettingsListBySubscription(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoscaleSettingsApi#autoscaleSettingsListBySubscription");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**AutoscaleSettingResourceCollection**](AutoscaleSettingResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of autoscale settings |  -  |
| **0** | Error response describing why the operation failed. |  -  |


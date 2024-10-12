# IntegrationServiceEnvironmentManagedApiApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationServiceEnvironmentManagedApisDelete**](IntegrationServiceEnvironmentManagedApiApi.md#integrationServiceEnvironmentManagedApisDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/managedApis/{apiName} |  |
| [**integrationServiceEnvironmentManagedApisGet**](IntegrationServiceEnvironmentManagedApiApi.md#integrationServiceEnvironmentManagedApisGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/managedApis/{apiName} |  |
| [**integrationServiceEnvironmentManagedApisPut**](IntegrationServiceEnvironmentManagedApiApi.md#integrationServiceEnvironmentManagedApisPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName}/managedApis/{apiName} |  |


<a id="integrationServiceEnvironmentManagedApisDelete"></a>
# **integrationServiceEnvironmentManagedApisDelete**
> integrationServiceEnvironmentManagedApisDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion)



Deletes the integration service environment managed Api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentManagedApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentManagedApiApi apiInstance = new IntegrationServiceEnvironmentManagedApiApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiName = "apiName_example"; // String | The api name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationServiceEnvironmentManagedApisDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentManagedApiApi#integrationServiceEnvironmentManagedApisDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroup** | **String**| The resource group. | |
| **integrationServiceEnvironmentName** | **String**| The integration service environment name. | |
| **apiName** | **String**| The api name. | |
| **apiVersion** | **String**| The API version. | |

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
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | Logic error response describing why the operation failed. |  -  |

<a id="integrationServiceEnvironmentManagedApisGet"></a>
# **integrationServiceEnvironmentManagedApisGet**
> ManagedApi integrationServiceEnvironmentManagedApisGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion)



Gets the integration service environment managed Api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentManagedApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentManagedApiApi apiInstance = new IntegrationServiceEnvironmentManagedApiApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group name.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiName = "apiName_example"; // String | The api name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      ManagedApi result = apiInstance.integrationServiceEnvironmentManagedApisGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentManagedApiApi#integrationServiceEnvironmentManagedApisGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroup** | **String**| The resource group name. | |
| **integrationServiceEnvironmentName** | **String**| The integration service environment name. | |
| **apiName** | **String**| The api name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**ManagedApi**](ManagedApi.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Logic error response describing why the operation failed. |  -  |

<a id="integrationServiceEnvironmentManagedApisPut"></a>
# **integrationServiceEnvironmentManagedApisPut**
> ManagedApi integrationServiceEnvironmentManagedApisPut(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion)



Puts the integration service environment managed Api.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentManagedApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentManagedApiApi apiInstance = new IntegrationServiceEnvironmentManagedApiApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group name.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiName = "apiName_example"; // String | The api name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      ManagedApi result = apiInstance.integrationServiceEnvironmentManagedApisPut(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentManagedApiApi#integrationServiceEnvironmentManagedApisPut");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroup** | **String**| The resource group name. | |
| **integrationServiceEnvironmentName** | **String**| The integration service environment name. | |
| **apiName** | **String**| The api name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**ManagedApi**](ManagedApi.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Logic error response describing why the operation failed. |  -  |


# IntegrationServiceEnvironmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationServiceEnvironmentsCreateOrUpdate**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} |  |
| [**integrationServiceEnvironmentsDelete**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} |  |
| [**integrationServiceEnvironmentsGet**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} |  |
| [**integrationServiceEnvironmentsListByResourceGroup**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments |  |
| [**integrationServiceEnvironmentsListBySubscription**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Logic/integrationServiceEnvironments |  |
| [**integrationServiceEnvironmentsUpdate**](IntegrationServiceEnvironmentsApi.md#integrationServiceEnvironmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Logic/integrationServiceEnvironments/{integrationServiceEnvironmentName} |  |


<a id="integrationServiceEnvironmentsCreateOrUpdate"></a>
# **integrationServiceEnvironmentsCreateOrUpdate**
> IntegrationServiceEnvironment integrationServiceEnvironmentsCreateOrUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment)



Creates or updates an integration service environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentsApi apiInstance = new IntegrationServiceEnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationServiceEnvironment integrationServiceEnvironment = new IntegrationServiceEnvironment(); // IntegrationServiceEnvironment | The integration service environment.
    try {
      IntegrationServiceEnvironment result = apiInstance.integrationServiceEnvironmentsCreateOrUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentsApi#integrationServiceEnvironmentsCreateOrUpdate");
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
| **apiVersion** | **String**| The API version. | |
| **integrationServiceEnvironment** | [**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)| The integration service environment. | |

### Return type

[**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)

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
| **0** | Logic error response describing why the operation failed. |  -  |

<a id="integrationServiceEnvironmentsDelete"></a>
# **integrationServiceEnvironmentsDelete**
> integrationServiceEnvironmentsDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion)



Deletes an integration service environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentsApi apiInstance = new IntegrationServiceEnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationServiceEnvironmentsDelete(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentsApi#integrationServiceEnvironmentsDelete");
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
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | Logic error response describing why the operation failed. |  -  |

<a id="integrationServiceEnvironmentsGet"></a>
# **integrationServiceEnvironmentsGet**
> IntegrationServiceEnvironment integrationServiceEnvironmentsGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion)



Gets an integration service environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentsApi apiInstance = new IntegrationServiceEnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationServiceEnvironment result = apiInstance.integrationServiceEnvironmentsGet(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentsApi#integrationServiceEnvironmentsGet");
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
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)

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

<a id="integrationServiceEnvironmentsListByResourceGroup"></a>
# **integrationServiceEnvironmentsListByResourceGroup**
> IntegrationServiceEnvironmentListResult integrationServiceEnvironmentsListByResourceGroup(subscriptionId, resourceGroup, apiVersion, $top)



Gets a list of integration service environments by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentsApi apiInstance = new IntegrationServiceEnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    try {
      IntegrationServiceEnvironmentListResult result = apiInstance.integrationServiceEnvironmentsListByResourceGroup(subscriptionId, resourceGroup, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentsApi#integrationServiceEnvironmentsListByResourceGroup");
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
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |

### Return type

[**IntegrationServiceEnvironmentListResult**](IntegrationServiceEnvironmentListResult.md)

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

<a id="integrationServiceEnvironmentsListBySubscription"></a>
# **integrationServiceEnvironmentsListBySubscription**
> IntegrationServiceEnvironmentListResult integrationServiceEnvironmentsListBySubscription(subscriptionId, apiVersion, $top)



Gets a list of integration service environments by subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentsApi apiInstance = new IntegrationServiceEnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    try {
      IntegrationServiceEnvironmentListResult result = apiInstance.integrationServiceEnvironmentsListBySubscription(subscriptionId, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentsApi#integrationServiceEnvironmentsListBySubscription");
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
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |

### Return type

[**IntegrationServiceEnvironmentListResult**](IntegrationServiceEnvironmentListResult.md)

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

<a id="integrationServiceEnvironmentsUpdate"></a>
# **integrationServiceEnvironmentsUpdate**
> IntegrationServiceEnvironment integrationServiceEnvironmentsUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment)



Updates an integration service environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationServiceEnvironmentsApi apiInstance = new IntegrationServiceEnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroup = "resourceGroup_example"; // String | The resource group.
    String integrationServiceEnvironmentName = "integrationServiceEnvironmentName_example"; // String | The integration service environment name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationServiceEnvironment integrationServiceEnvironment = new IntegrationServiceEnvironment(); // IntegrationServiceEnvironment | The integration service environment.
    try {
      IntegrationServiceEnvironment result = apiInstance.integrationServiceEnvironmentsUpdate(subscriptionId, resourceGroup, integrationServiceEnvironmentName, apiVersion, integrationServiceEnvironment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationServiceEnvironmentsApi#integrationServiceEnvironmentsUpdate");
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
| **apiVersion** | **String**| The API version. | |
| **integrationServiceEnvironment** | [**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)| The integration service environment. | |

### Return type

[**IntegrationServiceEnvironment**](IntegrationServiceEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Logic error response describing why the operation failed. |  -  |


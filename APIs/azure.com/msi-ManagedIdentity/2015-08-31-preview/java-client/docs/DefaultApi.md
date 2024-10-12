# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.ManagedIdentity/operations |  |
| [**userAssignedIdentitiesCreateOrUpdate**](DefaultApi.md#userAssignedIdentitiesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} |  |
| [**userAssignedIdentitiesDelete**](DefaultApi.md#userAssignedIdentitiesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} |  |
| [**userAssignedIdentitiesGet**](DefaultApi.md#userAssignedIdentitiesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} |  |
| [**userAssignedIdentitiesListByResourceGroup**](DefaultApi.md#userAssignedIdentitiesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities |  |
| [**userAssignedIdentitiesListBySubscription**](DefaultApi.md#userAssignedIdentitiesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ManagedIdentity/userAssignedIdentities |  |
| [**userAssignedIdentitiesUpdate**](DefaultApi.md#userAssignedIdentitiesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} |  |


<a id="operationsList"></a>
# **operationsList**
> OperationListResult operationsList(apiVersion)



Lists available operations for the Microsoft.ManagedIdentity provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of API to invoke.
    try {
      OperationListResult result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsList");
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
| **apiVersion** | **String**| Version of API to invoke. | |

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the list of available operations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="userAssignedIdentitiesCreateOrUpdate"></a>
# **userAssignedIdentitiesCreateOrUpdate**
> Identity userAssignedIdentitiesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters)



Create or update an identity in the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
    String resourceName = "resourceName_example"; // String | The name of the identity resource.
    String apiVersion = "apiVersion_example"; // String | Version of API to invoke.
    Identity parameters = new Identity(); // Identity | Parameters to create or update the identity
    try {
      Identity result = apiInstance.userAssignedIdentitiesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userAssignedIdentitiesCreateOrUpdate");
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
| **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | |
| **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | |
| **resourceName** | **String**| The name of the identity resource. | |
| **apiVersion** | **String**| Version of API to invoke. | |
| **parameters** | [**Identity**](Identity.md)| Parameters to create or update the identity | |

### Return type

[**Identity**](Identity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated identity |  -  |
| **201** | Created identity |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="userAssignedIdentitiesDelete"></a>
# **userAssignedIdentitiesDelete**
> userAssignedIdentitiesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion)



Deletes the identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
    String resourceName = "resourceName_example"; // String | The name of the identity resource.
    String apiVersion = "apiVersion_example"; // String | Version of API to invoke.
    try {
      apiInstance.userAssignedIdentitiesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userAssignedIdentitiesDelete");
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
| **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | |
| **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | |
| **resourceName** | **String**| The name of the identity resource. | |
| **apiVersion** | **String**| Version of API to invoke. | |

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
| **200** | OK. Deleted Identity. |  -  |
| **204** | The specified identity does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="userAssignedIdentitiesGet"></a>
# **userAssignedIdentitiesGet**
> Identity userAssignedIdentitiesGet(subscriptionId, resourceGroupName, resourceName, apiVersion)



Gets the identity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
    String resourceName = "resourceName_example"; // String | The name of the identity resource.
    String apiVersion = "apiVersion_example"; // String | Version of API to invoke.
    try {
      Identity result = apiInstance.userAssignedIdentitiesGet(subscriptionId, resourceGroupName, resourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userAssignedIdentitiesGet");
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
| **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | |
| **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | |
| **resourceName** | **String**| The name of the identity resource. | |
| **apiVersion** | **String**| Version of API to invoke. | |

### Return type

[**Identity**](Identity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The requested identity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="userAssignedIdentitiesListByResourceGroup"></a>
# **userAssignedIdentitiesListByResourceGroup**
> UserAssignedIdentitiesListResult userAssignedIdentitiesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the userAssignedIdentities available under the specified ResourceGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
    String apiVersion = "apiVersion_example"; // String | Version of API to invoke.
    try {
      UserAssignedIdentitiesListResult result = apiInstance.userAssignedIdentitiesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userAssignedIdentitiesListByResourceGroup");
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
| **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | |
| **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | |
| **apiVersion** | **String**| Version of API to invoke. | |

### Return type

[**UserAssignedIdentitiesListResult**](UserAssignedIdentitiesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The list of userAssignedIdentities was retrieved and returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="userAssignedIdentitiesListBySubscription"></a>
# **userAssignedIdentitiesListBySubscription**
> UserAssignedIdentitiesListResult userAssignedIdentitiesListBySubscription(subscriptionId, apiVersion)



Lists all the userAssignedIdentities available under the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
    String apiVersion = "apiVersion_example"; // String | Version of API to invoke.
    try {
      UserAssignedIdentitiesListResult result = apiInstance.userAssignedIdentitiesListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userAssignedIdentitiesListBySubscription");
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
| **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | |
| **apiVersion** | **String**| Version of API to invoke. | |

### Return type

[**UserAssignedIdentitiesListResult**](UserAssignedIdentitiesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The list of userAssignedIdentities was retrieved and returned successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="userAssignedIdentitiesUpdate"></a>
# **userAssignedIdentitiesUpdate**
> Identity userAssignedIdentitiesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters)



Update an identity in the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
    String resourceName = "resourceName_example"; // String | The name of the identity resource.
    String apiVersion = "apiVersion_example"; // String | Version of API to invoke.
    Identity parameters = new Identity(); // Identity | Parameters to update the identity
    try {
      Identity result = apiInstance.userAssignedIdentitiesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userAssignedIdentitiesUpdate");
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
| **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | |
| **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | |
| **resourceName** | **String**| The name of the identity resource. | |
| **apiVersion** | **String**| Version of API to invoke. | |
| **parameters** | [**Identity**](Identity.md)| Parameters to update the identity | |

### Return type

[**Identity**](Identity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated identity |  -  |
| **0** | Error response describing why the operation failed. |  -  |


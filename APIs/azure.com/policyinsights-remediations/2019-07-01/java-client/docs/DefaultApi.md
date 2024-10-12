# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**remediationsCancelAtManagementGroup**](DefaultApi.md#remediationsCancelAtManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel |  |
| [**remediationsCancelAtResource**](DefaultApi.md#remediationsCancelAtResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel |  |
| [**remediationsCancelAtResourceGroup**](DefaultApi.md#remediationsCancelAtResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel |  |
| [**remediationsCancelAtSubscription**](DefaultApi.md#remediationsCancelAtSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel |  |
| [**remediationsCreateOrUpdateAtManagementGroup**](DefaultApi.md#remediationsCreateOrUpdateAtManagementGroup) | **PUT** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsCreateOrUpdateAtResource**](DefaultApi.md#remediationsCreateOrUpdateAtResource) | **PUT** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsCreateOrUpdateAtResourceGroup**](DefaultApi.md#remediationsCreateOrUpdateAtResourceGroup) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsCreateOrUpdateAtSubscription**](DefaultApi.md#remediationsCreateOrUpdateAtSubscription) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsDeleteAtManagementGroup**](DefaultApi.md#remediationsDeleteAtManagementGroup) | **DELETE** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsDeleteAtResource**](DefaultApi.md#remediationsDeleteAtResource) | **DELETE** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsDeleteAtResourceGroup**](DefaultApi.md#remediationsDeleteAtResourceGroup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsDeleteAtSubscription**](DefaultApi.md#remediationsDeleteAtSubscription) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsGetAtManagementGroup**](DefaultApi.md#remediationsGetAtManagementGroup) | **GET** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsGetAtResource**](DefaultApi.md#remediationsGetAtResource) | **GET** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsGetAtResourceGroup**](DefaultApi.md#remediationsGetAtResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsGetAtSubscription**](DefaultApi.md#remediationsGetAtSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} |  |
| [**remediationsListDeploymentsAtManagementGroup**](DefaultApi.md#remediationsListDeploymentsAtManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments |  |
| [**remediationsListDeploymentsAtResource**](DefaultApi.md#remediationsListDeploymentsAtResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments |  |
| [**remediationsListDeploymentsAtResourceGroup**](DefaultApi.md#remediationsListDeploymentsAtResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments |  |
| [**remediationsListDeploymentsAtSubscription**](DefaultApi.md#remediationsListDeploymentsAtSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments |  |
| [**remediationsListForManagementGroup**](DefaultApi.md#remediationsListForManagementGroup) | **GET** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations |  |
| [**remediationsListForResource**](DefaultApi.md#remediationsListForResource) | **GET** /{resourceId}/providers/Microsoft.PolicyInsights/remediations |  |
| [**remediationsListForResourceGroup**](DefaultApi.md#remediationsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations |  |
| [**remediationsListForSubscription**](DefaultApi.md#remediationsListForSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations |  |


<a id="remediationsCancelAtManagementGroup"></a>
# **remediationsCancelAtManagementGroup**
> Remediation remediationsCancelAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion)



Cancels a remediation at management group scope.

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
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupId = "managementGroupId_example"; // String | Management group ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsCancelAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCancelAtManagementGroup");
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
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupId** | **String**| Management group ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The remediation that was canceled. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsCancelAtResource"></a>
# **remediationsCancelAtResource**
> Remediation remediationsCancelAtResource(resourceId, remediationName, apiVersion)



Cancel a remediation at resource scope.

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
    String resourceId = "resourceId_example"; // String | Resource ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsCancelAtResource(resourceId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCancelAtResource");
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
| **resourceId** | **String**| Resource ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The remediation that was canceled. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsCancelAtResourceGroup"></a>
# **remediationsCancelAtResourceGroup**
> Remediation remediationsCancelAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion)



Cancels a remediation at resource group scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsCancelAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCancelAtResourceGroup");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The remediation that was canceled. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsCancelAtSubscription"></a>
# **remediationsCancelAtSubscription**
> Remediation remediationsCancelAtSubscription(subscriptionId, remediationName, apiVersion)



Cancels a remediation at subscription scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsCancelAtSubscription(subscriptionId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCancelAtSubscription");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The remediation that was canceled. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsCreateOrUpdateAtManagementGroup"></a>
# **remediationsCreateOrUpdateAtManagementGroup**
> Remediation remediationsCreateOrUpdateAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, parameters)



Creates or updates a remediation at management group scope.

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
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupId = "managementGroupId_example"; // String | Management group ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Remediation parameters = new Remediation(); // Remediation | The remediation parameters.
    try {
      Remediation result = apiInstance.remediationsCreateOrUpdateAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCreateOrUpdateAtManagementGroup");
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
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupId** | **String**| Management group ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated remediation. |  -  |
| **201** | The created remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsCreateOrUpdateAtResource"></a>
# **remediationsCreateOrUpdateAtResource**
> Remediation remediationsCreateOrUpdateAtResource(resourceId, remediationName, apiVersion, parameters)



Creates or updates a remediation at resource scope.

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
    String resourceId = "resourceId_example"; // String | Resource ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Remediation parameters = new Remediation(); // Remediation | The remediation parameters.
    try {
      Remediation result = apiInstance.remediationsCreateOrUpdateAtResource(resourceId, remediationName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCreateOrUpdateAtResource");
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
| **resourceId** | **String**| Resource ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated remediation. |  -  |
| **201** | The created remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsCreateOrUpdateAtResourceGroup"></a>
# **remediationsCreateOrUpdateAtResourceGroup**
> Remediation remediationsCreateOrUpdateAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, parameters)



Creates or updates a remediation at resource group scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Remediation parameters = new Remediation(); // Remediation | The remediation parameters.
    try {
      Remediation result = apiInstance.remediationsCreateOrUpdateAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCreateOrUpdateAtResourceGroup");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated remediation. |  -  |
| **201** | The created remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsCreateOrUpdateAtSubscription"></a>
# **remediationsCreateOrUpdateAtSubscription**
> Remediation remediationsCreateOrUpdateAtSubscription(subscriptionId, remediationName, apiVersion, parameters)



Creates or updates a remediation at subscription scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Remediation parameters = new Remediation(); // Remediation | The remediation parameters.
    try {
      Remediation result = apiInstance.remediationsCreateOrUpdateAtSubscription(subscriptionId, remediationName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsCreateOrUpdateAtSubscription");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated remediation. |  -  |
| **201** | The created remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsDeleteAtManagementGroup"></a>
# **remediationsDeleteAtManagementGroup**
> Remediation remediationsDeleteAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion)



Deletes an existing remediation at management group scope.

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
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupId = "managementGroupId_example"; // String | Management group ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsDeleteAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsDeleteAtManagementGroup");
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
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupId** | **String**| Management group ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted remediation. |  -  |
| **204** | The remediation did not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsDeleteAtResource"></a>
# **remediationsDeleteAtResource**
> Remediation remediationsDeleteAtResource(resourceId, remediationName, apiVersion)



Deletes an existing remediation at individual resource scope.

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
    String resourceId = "resourceId_example"; // String | Resource ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsDeleteAtResource(resourceId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsDeleteAtResource");
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
| **resourceId** | **String**| Resource ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted remediation. |  -  |
| **204** | The remediation did not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsDeleteAtResourceGroup"></a>
# **remediationsDeleteAtResourceGroup**
> Remediation remediationsDeleteAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion)



Deletes an existing remediation at resource group scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsDeleteAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsDeleteAtResourceGroup");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted remediation. |  -  |
| **204** | The remediation did not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsDeleteAtSubscription"></a>
# **remediationsDeleteAtSubscription**
> Remediation remediationsDeleteAtSubscription(subscriptionId, remediationName, apiVersion)



Deletes an existing remediation at subscription scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsDeleteAtSubscription(subscriptionId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsDeleteAtSubscription");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted remediation. |  -  |
| **204** | The remediation did not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsGetAtManagementGroup"></a>
# **remediationsGetAtManagementGroup**
> Remediation remediationsGetAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion)



Gets an existing remediation at management group scope.

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
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupId = "managementGroupId_example"; // String | Management group ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsGetAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsGetAtManagementGroup");
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
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupId** | **String**| Management group ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsGetAtResource"></a>
# **remediationsGetAtResource**
> Remediation remediationsGetAtResource(resourceId, remediationName, apiVersion)



Gets an existing remediation at resource scope.

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
    String resourceId = "resourceId_example"; // String | Resource ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsGetAtResource(resourceId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsGetAtResource");
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
| **resourceId** | **String**| Resource ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsGetAtResourceGroup"></a>
# **remediationsGetAtResourceGroup**
> Remediation remediationsGetAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion)



Gets an existing remediation at resource group scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsGetAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsGetAtResourceGroup");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsGetAtSubscription"></a>
# **remediationsGetAtSubscription**
> Remediation remediationsGetAtSubscription(subscriptionId, remediationName, apiVersion)



Gets an existing remediation at subscription scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      Remediation result = apiInstance.remediationsGetAtSubscription(subscriptionId, remediationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsGetAtSubscription");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListDeploymentsAtManagementGroup"></a>
# **remediationsListDeploymentsAtManagementGroup**
> RemediationDeploymentsListResult remediationsListDeploymentsAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, $top)



Gets all deployments for a remediation at management group scope.

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
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupId = "managementGroupId_example"; // String | Management group ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    try {
      RemediationDeploymentsListResult result = apiInstance.remediationsListDeploymentsAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListDeploymentsAtManagementGroup");
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
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupId** | **String**| Management group ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListDeploymentsAtResource"></a>
# **remediationsListDeploymentsAtResource**
> RemediationDeploymentsListResult remediationsListDeploymentsAtResource(resourceId, remediationName, apiVersion, $top)



Gets all deployments for a remediation at resource scope.

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
    String resourceId = "resourceId_example"; // String | Resource ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    try {
      RemediationDeploymentsListResult result = apiInstance.remediationsListDeploymentsAtResource(resourceId, remediationName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListDeploymentsAtResource");
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
| **resourceId** | **String**| Resource ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListDeploymentsAtResourceGroup"></a>
# **remediationsListDeploymentsAtResourceGroup**
> RemediationDeploymentsListResult remediationsListDeploymentsAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, $top)



Gets all deployments for a remediation at resource group scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    try {
      RemediationDeploymentsListResult result = apiInstance.remediationsListDeploymentsAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListDeploymentsAtResourceGroup");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListDeploymentsAtSubscription"></a>
# **remediationsListDeploymentsAtSubscription**
> RemediationDeploymentsListResult remediationsListDeploymentsAtSubscription(subscriptionId, remediationName, apiVersion, $top)



Gets all deployments for a remediation at subscription scope.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String remediationName = "remediationName_example"; // String | The name of the remediation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    try {
      RemediationDeploymentsListResult result = apiInstance.remediationsListDeploymentsAtSubscription(subscriptionId, remediationName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListDeploymentsAtSubscription");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **remediationName** | **String**| The name of the remediation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediation deployments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListForManagementGroup"></a>
# **remediationsListForManagementGroup**
> RemediationListResult remediationsListForManagementGroup(managementGroupsNamespace, managementGroupId, apiVersion, $top, $filter)



Gets all remediations for the management group.

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
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupId = "managementGroupId_example"; // String | Management group ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      RemediationListResult result = apiInstance.remediationsListForManagementGroup(managementGroupsNamespace, managementGroupId, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListForManagementGroup");
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
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupId** | **String**| Management group ID. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListForResource"></a>
# **remediationsListForResource**
> RemediationListResult remediationsListForResource(resourceId, apiVersion, $top, $filter)



Gets all remediations for a resource.

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
    String resourceId = "resourceId_example"; // String | Resource ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      RemediationListResult result = apiInstance.remediationsListForResource(resourceId, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListForResource");
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
| **resourceId** | **String**| Resource ID. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListForResourceGroup"></a>
# **remediationsListForResourceGroup**
> RemediationListResult remediationsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top, $filter)



Gets all remediations for the subscription.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      RemediationListResult result = apiInstance.remediationsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListForResourceGroup");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remediationsListForSubscription"></a>
# **remediationsListForSubscription**
> RemediationListResult remediationsListForSubscription(subscriptionId, apiVersion, $top, $filter)



Gets all remediations for the subscription.

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
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      RemediationListResult result = apiInstance.remediationsListForSubscription(subscriptionId, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remediationsListForSubscription");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved remediations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


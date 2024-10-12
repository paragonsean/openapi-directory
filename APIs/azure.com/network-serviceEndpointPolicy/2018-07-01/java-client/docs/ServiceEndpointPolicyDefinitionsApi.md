# ServiceEndpointPolicyDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceEndpointPolicyDefinitionsCreateOrUpdate**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName} |  |
| [**serviceEndpointPolicyDefinitionsDelete**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName} |  |
| [**serviceEndpointPolicyDefinitionsGet**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions/{serviceEndpointPolicyDefinitionName} |  |
| [**serviceEndpointPolicyDefinitionsListByResourceGroup**](ServiceEndpointPolicyDefinitionsApi.md#serviceEndpointPolicyDefinitionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName}/serviceEndpointPolicyDefinitions |  |


<a id="serviceEndpointPolicyDefinitionsCreateOrUpdate"></a>
# **serviceEndpointPolicyDefinitionsCreateOrUpdate**
> ServiceEndpointPolicyDefinition serviceEndpointPolicyDefinitionsCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId, serviceEndpointPolicyDefinitions)



Creates or updates a service endpoint policy definition in the specified service endpoint policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPolicyDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPolicyDefinitionsApi apiInstance = new ServiceEndpointPolicyDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
    String serviceEndpointPolicyDefinitionName = "serviceEndpointPolicyDefinitionName_example"; // String | The name of the service endpoint policy definition name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ServiceEndpointPolicyDefinition serviceEndpointPolicyDefinitions = new ServiceEndpointPolicyDefinition(); // ServiceEndpointPolicyDefinition | Parameters supplied to the create or update service endpoint policy operation.
    try {
      ServiceEndpointPolicyDefinition result = apiInstance.serviceEndpointPolicyDefinitionsCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId, serviceEndpointPolicyDefinitions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPolicyDefinitionsApi#serviceEndpointPolicyDefinitionsCreateOrUpdate");
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
| **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | |
| **serviceEndpointPolicyDefinitionName** | **String**| The name of the service endpoint policy definition name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **serviceEndpointPolicyDefinitions** | [**ServiceEndpointPolicyDefinition**](ServiceEndpointPolicyDefinition.md)| Parameters supplied to the create or update service endpoint policy operation. | |

### Return type

[**ServiceEndpointPolicyDefinition**](ServiceEndpointPolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ServiceEndpointPolicyDefinition resource. |  -  |
| **201** | Create successful. The operation returns the resulting ServiceEndpointPolicyDefinition resource. |  -  |

<a id="serviceEndpointPolicyDefinitionsDelete"></a>
# **serviceEndpointPolicyDefinitionsDelete**
> serviceEndpointPolicyDefinitionsDelete(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId)



Deletes the specified ServiceEndpoint policy definitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPolicyDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPolicyDefinitionsApi apiInstance = new ServiceEndpointPolicyDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the Service Endpoint Policy.
    String serviceEndpointPolicyDefinitionName = "serviceEndpointPolicyDefinitionName_example"; // String | The name of the service endpoint policy definition.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.serviceEndpointPolicyDefinitionsDelete(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPolicyDefinitionsApi#serviceEndpointPolicyDefinitionsDelete");
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
| **serviceEndpointPolicyName** | **String**| The name of the Service Endpoint Policy. | |
| **serviceEndpointPolicyDefinitionName** | **String**| The name of the service endpoint policy definition. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource does not exist. |  -  |

<a id="serviceEndpointPolicyDefinitionsGet"></a>
# **serviceEndpointPolicyDefinitionsGet**
> ServiceEndpointPolicyDefinition serviceEndpointPolicyDefinitionsGet(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId)



Get the specified service endpoint policy definitions from service endpoint policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPolicyDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPolicyDefinitionsApi apiInstance = new ServiceEndpointPolicyDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy name.
    String serviceEndpointPolicyDefinitionName = "serviceEndpointPolicyDefinitionName_example"; // String | The name of the service endpoint policy definition name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ServiceEndpointPolicyDefinition result = apiInstance.serviceEndpointPolicyDefinitionsGet(resourceGroupName, serviceEndpointPolicyName, serviceEndpointPolicyDefinitionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPolicyDefinitionsApi#serviceEndpointPolicyDefinitionsGet");
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
| **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy name. | |
| **serviceEndpointPolicyDefinitionName** | **String**| The name of the service endpoint policy definition name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ServiceEndpointPolicyDefinition**](ServiceEndpointPolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ServiceEndpointPolicyDefinition resource. |  -  |

<a id="serviceEndpointPolicyDefinitionsListByResourceGroup"></a>
# **serviceEndpointPolicyDefinitionsListByResourceGroup**
> ServiceEndpointPolicyDefinitionListResult serviceEndpointPolicyDefinitionsListByResourceGroup(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId)



Gets all service endpoint policy definitions in a service end point policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPolicyDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPolicyDefinitionsApi apiInstance = new ServiceEndpointPolicyDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ServiceEndpointPolicyDefinitionListResult result = apiInstance.serviceEndpointPolicyDefinitionsListByResourceGroup(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPolicyDefinitionsApi#serviceEndpointPolicyDefinitionsListByResourceGroup");
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
| **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ServiceEndpointPolicyDefinitionListResult**](ServiceEndpointPolicyDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ServiceEndpointPolicyDefinition resources. |  -  |


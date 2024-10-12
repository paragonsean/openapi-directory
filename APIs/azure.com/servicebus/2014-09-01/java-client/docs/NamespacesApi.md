# NamespacesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**namespacesCheckNameAvailability**](NamespacesApi.md#namespacesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceBus/CheckNameAvailability |  |
| [**namespacesCheckNameSpaceAvailability**](NamespacesApi.md#namespacesCheckNameSpaceAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceBus/CheckNameSpaceAvailability |  |
| [**namespacesCreateOrUpdate**](NamespacesApi.md#namespacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName} |  |
| [**namespacesCreateOrUpdateAuthorizationRule**](NamespacesApi.md#namespacesCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName} |  |
| [**namespacesDelete**](NamespacesApi.md#namespacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName} |  |
| [**namespacesDeleteAuthorizationRule**](NamespacesApi.md#namespacesDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName} |  |
| [**namespacesGet**](NamespacesApi.md#namespacesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName} |  |
| [**namespacesGetAuthorizationRule**](NamespacesApi.md#namespacesGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName} |  |
| [**namespacesListAuthorizationRules**](NamespacesApi.md#namespacesListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/AuthorizationRules |  |
| [**namespacesListByResourceGroup**](NamespacesApi.md#namespacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces |  |
| [**namespacesListBySubscription**](NamespacesApi.md#namespacesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceBus/namespaces |  |
| [**namespacesListPostAuthorizationRules**](NamespacesApi.md#namespacesListPostAuthorizationRules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/AuthorizationRules |  |
| [**namespacesPostAuthorizationRule**](NamespacesApi.md#namespacesPostAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/AuthorizationRules/{authorizationRuleName} |  |
| [**namespacesUpdate**](NamespacesApi.md#namespacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName} |  |


<a id="namespacesCheckNameAvailability"></a>
# **namespacesCheckNameAvailability**
> CheckNameAvailabilityResult namespacesCheckNameAvailability(apiVersion, subscriptionId, parameters)



Check the give namespace name availability.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckNameAvailability parameters = new CheckNameAvailability(); // CheckNameAvailability | Parameters to check availability of the given namespace name
    try {
      CheckNameAvailabilityResult result = apiInstance.namespacesCheckNameAvailability(apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesCheckNameAvailability");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**CheckNameAvailability**](CheckNameAvailability.md)| Parameters to check availability of the given namespace name | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | check availability returned successfully. |  -  |

<a id="namespacesCheckNameSpaceAvailability"></a>
# **namespacesCheckNameSpaceAvailability**
> CheckNameAvailabilityResult namespacesCheckNameSpaceAvailability(apiVersion, subscriptionId, parameters)



Check the give namespace name availability.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckNameAvailability parameters = new CheckNameAvailability(); // CheckNameAvailability | Parameters to check availability of the given namespace name
    try {
      CheckNameAvailabilityResult result = apiInstance.namespacesCheckNameSpaceAvailability(apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesCheckNameSpaceAvailability");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**CheckNameAvailability**](CheckNameAvailability.md)| Parameters to check availability of the given namespace name | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | check availability returned successfully. |  -  |

<a id="namespacesCreateOrUpdate"></a>
# **namespacesCreateOrUpdate**
> NamespaceResource namespacesCreateOrUpdate(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters)



Creates or updates a service namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    NamespaceCreateOrUpdateParameters parameters = new NamespaceCreateOrUpdateParameters(); // NamespaceCreateOrUpdateParameters | Parameters supplied to create a namespace resource.
    try {
      NamespaceResource result = apiInstance.namespacesCreateOrUpdate(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**NamespaceCreateOrUpdateParameters**](NamespaceCreateOrUpdateParameters.md)| Parameters supplied to create a namespace resource. | |

### Return type

[**NamespaceResource**](NamespaceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace created successfully. |  -  |
| **201** | Namespace create request accepted. |  -  |
| **202** | Namespace create or update request accepted. |  -  |

<a id="namespacesCreateOrUpdateAuthorizationRule"></a>
# **namespacesCreateOrUpdateAuthorizationRule**
> SharedAccessAuthorizationRuleResource namespacesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates or updates an authorization rule for a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SharedAccessAuthorizationRuleCreateOrUpdateParameters parameters = new SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access authorization rule.
    try {
      SharedAccessAuthorizationRuleResource result = apiInstance.namespacesCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesCreateOrUpdateAuthorizationRule");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SharedAccessAuthorizationRuleCreateOrUpdateParameters**](SharedAccessAuthorizationRuleCreateOrUpdateParameters.md)| The shared access authorization rule. | |

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace authorization rule created. |  -  |

<a id="namespacesDelete"></a>
# **namespacesDelete**
> namespacesDelete(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Deletes an existing namespace. This operation also removes all associated resources under the namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.namespacesDelete(resourceGroupName, namespaceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesDelete");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Namespace successfully deleted. |  -  |
| **202** | Namespace delete request accepted. |  -  |
| **204** | No content. |  -  |

<a id="namespacesDeleteAuthorizationRule"></a>
# **namespacesDeleteAuthorizationRule**
> namespacesDeleteAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a namespace authorization rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.namespacesDeleteAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesDeleteAuthorizationRule");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Namespace authorization rule successfully deleted. |  -  |
| **204** | No content. |  -  |

<a id="namespacesGet"></a>
# **namespacesGet**
> NamespaceResource namespacesGet(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets a description for the specified namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NamespaceResource result = apiInstance.namespacesGet(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesGet");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NamespaceResource**](NamespaceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace successfully returned. |  -  |

<a id="namespacesGetAuthorizationRule"></a>
# **namespacesGetAuthorizationRule**
> SharedAccessAuthorizationRuleGetResource namespacesGetAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a namespace by rule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleGetResource result = apiInstance.namespacesGetAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesGetAuthorizationRule");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleGetResource**](SharedAccessAuthorizationRuleGetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace authorization rule returned successfully. |  -  |

<a id="namespacesListAuthorizationRules"></a>
# **namespacesListAuthorizationRules**
> SharedAccessAuthorizationRuleListResult namespacesListAuthorizationRules(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets the authorization rules for a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleListResult result = apiInstance.namespacesListAuthorizationRules(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesListAuthorizationRules");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace authorization rules returned successfully. |  -  |

<a id="namespacesListByResourceGroup"></a>
# **namespacesListByResourceGroup**
> NamespaceListResult namespacesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets the available namespaces within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NamespaceListResult result = apiInstance.namespacesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesListByResourceGroup");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NamespaceListResult**](NamespaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespaces successfully returned. |  -  |

<a id="namespacesListBySubscription"></a>
# **namespacesListBySubscription**
> NamespaceListResult namespacesListBySubscription(apiVersion, subscriptionId)



Gets all the available namespaces within the subscription, irrespective of the resource groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NamespaceListResult result = apiInstance.namespacesListBySubscription(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesListBySubscription");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NamespaceListResult**](NamespaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespaces successfully returned. |  -  |

<a id="namespacesListPostAuthorizationRules"></a>
# **namespacesListPostAuthorizationRules**
> SharedAccessAuthorizationRuleListResult namespacesListPostAuthorizationRules(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets the authorization rules for a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleListResult result = apiInstance.namespacesListPostAuthorizationRules(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesListPostAuthorizationRules");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace authorization rules returned successfully. |  -  |

<a id="namespacesPostAuthorizationRule"></a>
# **namespacesPostAuthorizationRule**
> SharedAccessAuthorizationRuleResource namespacesPostAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a namespace by rule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleResource result = apiInstance.namespacesPostAuthorizationRule(resourceGroupName, namespaceName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesPostAuthorizationRule");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace authorization rule returned successfully. |  -  |

<a id="namespacesUpdate"></a>
# **namespacesUpdate**
> NamespaceResource namespacesUpdate(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters)



Updates a service namespace. Once created, this namespace&#39;s resource manifest is immutable. This operation is idempotent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    NamespaceUpdateParameters parameters = new NamespaceUpdateParameters(); // NamespaceUpdateParameters | Parameters supplied to update a namespace resource.
    try {
      NamespaceResource result = apiInstance.namespacesUpdate(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#namespacesUpdate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **namespaceName** | **String**| The namespace name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**NamespaceUpdateParameters**](NamespaceUpdateParameters.md)| Parameters supplied to update a namespace resource. | |

### Return type

[**NamespaceResource**](NamespaceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace updated successfully. |  -  |
| **201** | Namespace update request accepted. |  -  |
| **202** | Namespace update request accepted. |  -  |


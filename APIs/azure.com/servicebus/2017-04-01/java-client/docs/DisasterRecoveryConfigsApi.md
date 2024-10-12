# DisasterRecoveryConfigsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disasterRecoveryConfigsBreakPairing**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsBreakPairing) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/breakPairing |  |
| [**disasterRecoveryConfigsCheckNameAvailability**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/CheckNameAvailability |  |
| [**disasterRecoveryConfigsCreateOrUpdate**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias} |  |
| [**disasterRecoveryConfigsDelete**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias} |  |
| [**disasterRecoveryConfigsFailOver**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsFailOver) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/failover |  |
| [**disasterRecoveryConfigsGet**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias} |  |
| [**disasterRecoveryConfigsGetAuthorizationRule**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/AuthorizationRules/{authorizationRuleName} |  |
| [**disasterRecoveryConfigsList**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs |  |
| [**disasterRecoveryConfigsListAuthorizationRules**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/AuthorizationRules |  |
| [**disasterRecoveryConfigsListKeys**](DisasterRecoveryConfigsApi.md#disasterRecoveryConfigsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceBus/namespaces/{namespaceName}/disasterRecoveryConfigs/{alias}/AuthorizationRules/{authorizationRuleName}/listKeys |  |


<a id="disasterRecoveryConfigsBreakPairing"></a>
# **disasterRecoveryConfigsBreakPairing**
> disasterRecoveryConfigsBreakPairing(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId)



This operation disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.disasterRecoveryConfigsBreakPairing(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsBreakPairing");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Break-Pairing operation is successful. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsCheckNameAvailability"></a>
# **disasterRecoveryConfigsCheckNameAvailability**
> CheckNameAvailabilityResult disasterRecoveryConfigsCheckNameAvailability(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters)



Check the give namespace name availability.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckNameAvailability parameters = new CheckNameAvailability(); // CheckNameAvailability | Parameters to check availability of the given namespace name
    try {
      CheckNameAvailabilityResult result = apiInstance.disasterRecoveryConfigsCheckNameAvailability(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsCheckNameAvailability");
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
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsCreateOrUpdate"></a>
# **disasterRecoveryConfigsCreateOrUpdate**
> ArmDisasterRecovery disasterRecoveryConfigsCreateOrUpdate(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId, parameters)



Creates or updates a new Alias(Disaster Recovery configuration)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ArmDisasterRecovery parameters = new ArmDisasterRecovery(); // ArmDisasterRecovery | Parameters required to create an Alias(Disaster Recovery configuration)
    try {
      ArmDisasterRecovery result = apiInstance.disasterRecoveryConfigsCreateOrUpdate(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsCreateOrUpdate");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ArmDisasterRecovery**](ArmDisasterRecovery.md)| Parameters required to create an Alias(Disaster Recovery configuration) | |

### Return type

[**ArmDisasterRecovery**](ArmDisasterRecovery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Alias(Disaster Recovery configuration) successfully created |  -  |
| **201** | Alias(Disaster Recovery configuration) creation request received |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsDelete"></a>
# **disasterRecoveryConfigsDelete**
> disasterRecoveryConfigsDelete(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId)



Deletes an Alias(Disaster Recovery configuration)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.disasterRecoveryConfigsDelete(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsDelete");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Delete Alias(Disaster Recovery configuration) request accepted |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsFailOver"></a>
# **disasterRecoveryConfigsFailOver**
> disasterRecoveryConfigsFailOver(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId)



Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.disasterRecoveryConfigsFailOver(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsFailOver");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Failover operation is successful. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsGet"></a>
# **disasterRecoveryConfigsGet**
> ArmDisasterRecovery disasterRecoveryConfigsGet(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId)



Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ArmDisasterRecovery result = apiInstance.disasterRecoveryConfigsGet(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsGet");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ArmDisasterRecovery**](ArmDisasterRecovery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the Alias(Disaster Recovery configurations) |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsGetAuthorizationRule"></a>
# **disasterRecoveryConfigsGetAuthorizationRule**
> SBAuthorizationRule disasterRecoveryConfigsGetAuthorizationRule(resourceGroupName, namespaceName, alias, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a namespace by rule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBAuthorizationRule result = apiInstance.disasterRecoveryConfigsGetAuthorizationRule(resourceGroupName, namespaceName, alias, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsGetAuthorizationRule");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SBAuthorizationRule**](SBAuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DisasterRecoveryConfigs authorization rule returned successfully. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsList"></a>
# **disasterRecoveryConfigsList**
> ArmDisasterRecoveryListResult disasterRecoveryConfigsList(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Gets all Alias(Disaster Recovery configurations)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ArmDisasterRecoveryListResult result = apiInstance.disasterRecoveryConfigsList(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsList");
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

[**ArmDisasterRecoveryListResult**](ArmDisasterRecoveryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of Alias(Disaster Recovery configurations) for servicebus namespace |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsListAuthorizationRules"></a>
# **disasterRecoveryConfigsListAuthorizationRules**
> SBAuthorizationRuleListResult disasterRecoveryConfigsListAuthorizationRules(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId)



Gets the authorization rules for a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SBAuthorizationRuleListResult result = apiInstance.disasterRecoveryConfigsListAuthorizationRules(resourceGroupName, namespaceName, alias, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsListAuthorizationRules");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SBAuthorizationRuleListResult**](SBAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DisasterRecoveryConfigs authorization rules returned successfully. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |

<a id="disasterRecoveryConfigsListKeys"></a>
# **disasterRecoveryConfigsListKeys**
> AccessKeys disasterRecoveryConfigsListKeys(resourceGroupName, namespaceName, alias, authorizationRuleName, apiVersion, subscriptionId)



Gets the primary and secondary connection strings for the namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DisasterRecoveryConfigsApi apiInstance = new DisasterRecoveryConfigsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String alias = "alias_example"; // String | The Disaster Recovery configuration name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AccessKeys result = apiInstance.disasterRecoveryConfigsListKeys(resourceGroupName, namespaceName, alias, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigsApi#disasterRecoveryConfigsListKeys");
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
| **alias** | **String**| The Disaster Recovery configuration name | |
| **authorizationRuleName** | **String**| The authorization rule name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AccessKeys**](AccessKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connection strings successfully returned. |  -  |
| **0** | ServiceBus error response describing why the operation failed. |  -  |


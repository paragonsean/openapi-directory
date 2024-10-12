# WcfRelaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wCFRelaysCreateOrUpdate**](WcfRelaysApi.md#wCFRelaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName} |  |
| [**wCFRelaysCreateOrUpdateAuthorizationRule**](WcfRelaysApi.md#wCFRelaysCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules/{authorizationRuleName} |  |
| [**wCFRelaysDelete**](WcfRelaysApi.md#wCFRelaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName} |  |
| [**wCFRelaysDeleteAuthorizationRule**](WcfRelaysApi.md#wCFRelaysDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules/{authorizationRuleName} |  |
| [**wCFRelaysGet**](WcfRelaysApi.md#wCFRelaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName} |  |
| [**wCFRelaysGetAuthorizationRule**](WcfRelaysApi.md#wCFRelaysGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules/{authorizationRuleName} |  |
| [**wCFRelaysListAuthorizationRules**](WcfRelaysApi.md#wCFRelaysListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules |  |
| [**wCFRelaysListByNamespace**](WcfRelaysApi.md#wCFRelaysListByNamespace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays |  |
| [**wCFRelaysListKeys**](WcfRelaysApi.md#wCFRelaysListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules/{authorizationRuleName}/ListKeys |  |
| [**wCFRelaysListPostAuthorizationRules**](WcfRelaysApi.md#wCFRelaysListPostAuthorizationRules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules |  |
| [**wCFRelaysPostAuthorizationRule**](WcfRelaysApi.md#wCFRelaysPostAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules/{authorizationRuleName} |  |
| [**wCFRelaysRegenerateKeys**](WcfRelaysApi.md#wCFRelaysRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/WcfRelays/{relayName}/authorizationRules/{authorizationRuleName}/regenerateKeys |  |


<a id="wCFRelaysCreateOrUpdate"></a>
# **wCFRelaysCreateOrUpdate**
> WcfRelay wCFRelaysCreateOrUpdate(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId, parameters)



Creates or Updates a WCFRelay. This operation is idempotent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    WcfRelay parameters = new WcfRelay(); // WcfRelay | Parameters supplied to create a WCFRelays.
    try {
      WcfRelay result = apiInstance.wCFRelaysCreateOrUpdate(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysCreateOrUpdate");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**WcfRelay**](WcfRelay.md)| Parameters supplied to create a WCFRelays. | |

### Return type

[**WcfRelay**](WcfRelay.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to create WCFRelays succeeded |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysCreateOrUpdateAuthorizationRule"></a>
# **wCFRelaysCreateOrUpdateAuthorizationRule**
> AuthorizationRule wCFRelaysCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates or Updates an authorization rule for a WCFRelays

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    AuthorizationRule parameters = new AuthorizationRule(); // AuthorizationRule | The authorization rule parameters.
    try {
      AuthorizationRule result = apiInstance.wCFRelaysCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysCreateOrUpdateAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**AuthorizationRule**](AuthorizationRule.md)| The authorization rule parameters. | |

### Return type

[**AuthorizationRule**](AuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WCFRelays Authorization rule created |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysDelete"></a>
# **wCFRelaysDelete**
> wCFRelaysDelete(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId)



Deletes a WCFRelays .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.wCFRelaysDelete(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysDelete");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | WCFRelays deleted. |  -  |
| **204** | No Content |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysDeleteAuthorizationRule"></a>
# **wCFRelaysDeleteAuthorizationRule**
> wCFRelaysDeleteAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a WCFRelays authorization rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.wCFRelaysDeleteAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysDeleteAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Request to delete WCFRelay authorizationRule succeeded |  -  |
| **204** | Request accepted but Authorization rule does not exist |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysGet"></a>
# **wCFRelaysGet**
> WcfRelay wCFRelaysGet(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId)



Returns the description for the specified WCFRelays.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      WcfRelay result = apiInstance.wCFRelaysGet(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysGet");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**WcfRelay**](WcfRelay.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved WCFRelays description |  -  |
| **204** | WCFRelays not found |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysGetAuthorizationRule"></a>
# **wCFRelaysGetAuthorizationRule**
> AuthorizationRule wCFRelaysGetAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId)



Get authorizationRule for a WCFRelays by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRule result = apiInstance.wCFRelaysGetAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysGetAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRule**](AuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request for WCFRelays AuthorizationRule succeeded |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysListAuthorizationRules"></a>
# **wCFRelaysListAuthorizationRules**
> AuthorizationRuleListResult wCFRelaysListAuthorizationRules(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId)



Authorization rules for a WCFRelays.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRuleListResult result = apiInstance.wCFRelaysListAuthorizationRules(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysListAuthorizationRules");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRuleListResult**](AuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization rules successfully returned. |  -  |

<a id="wCFRelaysListByNamespace"></a>
# **wCFRelaysListByNamespace**
> WcfRelaysListResult wCFRelaysListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Lists the WCFRelays within the namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      WcfRelaysListResult result = apiInstance.wCFRelaysListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysListByNamespace");
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
| **namespaceName** | **String**| The Namespace Name | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**WcfRelaysListResult**](WcfRelaysListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WCF Relays returned successfully |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysListKeys"></a>
# **wCFRelaysListKeys**
> AuthorizationRuleKeys wCFRelaysListKeys(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId)



Primary and Secondary ConnectionStrings to the WCFRelays.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRuleKeys result = apiInstance.wCFRelaysListKeys(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysListKeys");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRuleKeys**](AuthorizationRuleKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysListPostAuthorizationRules"></a>
# **wCFRelaysListPostAuthorizationRules**
> AuthorizationRuleListResult wCFRelaysListPostAuthorizationRules(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId)



Authorization rules for a WCFRelays.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRuleListResult result = apiInstance.wCFRelaysListPostAuthorizationRules(resourceGroupName, namespaceName, relayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysListPostAuthorizationRules");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRuleListResult**](AuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization rules successfully returned. |  -  |

<a id="wCFRelaysPostAuthorizationRule"></a>
# **wCFRelaysPostAuthorizationRule**
> AuthorizationRule wCFRelaysPostAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId)



Get authorizationRule for a WCFRelays by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRule result = apiInstance.wCFRelaysPostAuthorizationRule(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysPostAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRule**](AuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request for WCFRelays AuthorizationRule succeeded |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="wCFRelaysRegenerateKeys"></a>
# **wCFRelaysRegenerateKeys**
> AuthorizationRuleKeys wCFRelaysRegenerateKeys(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the Primary or Secondary ConnectionStrings to the WCFRelays

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WcfRelaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WcfRelaysApi apiInstance = new WcfRelaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String relayName = "relayName_example"; // String | The relay name
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RegenerateKeysParameters parameters = new RegenerateKeysParameters(); // RegenerateKeysParameters | Parameters supplied to regenerate Auth Rule.
    try {
      AuthorizationRuleKeys result = apiInstance.wCFRelaysRegenerateKeys(resourceGroupName, namespaceName, relayName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WcfRelaysApi#wCFRelaysRegenerateKeys");
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
| **namespaceName** | **String**| The Namespace Name | |
| **relayName** | **String**| The relay name | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RegenerateKeysParameters**](RegenerateKeysParameters.md)| Parameters supplied to regenerate Auth Rule. | |

### Return type

[**AuthorizationRuleKeys**](AuthorizationRuleKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |


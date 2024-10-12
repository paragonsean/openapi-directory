# NotificationHubsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationHubsCheckAvailability**](NotificationHubsApi.md#notificationHubsCheckAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/checkNotificationHubAvailability |  |
| [**notificationHubsCreateOrUpdate**](NotificationHubsApi.md#notificationHubsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName} |  |
| [**notificationHubsCreateOrUpdateAuthorizationRule**](NotificationHubsApi.md#notificationHubsCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName} |  |
| [**notificationHubsDelete**](NotificationHubsApi.md#notificationHubsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName} |  |
| [**notificationHubsDeleteAuthorizationRule**](NotificationHubsApi.md#notificationHubsDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName} |  |
| [**notificationHubsGet**](NotificationHubsApi.md#notificationHubsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName} |  |
| [**notificationHubsGetAuthorizationRule**](NotificationHubsApi.md#notificationHubsGetAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName} |  |
| [**notificationHubsGetPnsCredentials**](NotificationHubsApi.md#notificationHubsGetPnsCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/pnsCredentials |  |
| [**notificationHubsList**](NotificationHubsApi.md#notificationHubsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs |  |
| [**notificationHubsListAuthorizationRules**](NotificationHubsApi.md#notificationHubsListAuthorizationRules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules |  |
| [**notificationHubsListKeys**](NotificationHubsApi.md#notificationHubsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NotificationHubs/namespaces/{namespaceName}/notificationHubs/{notificationHubName}/AuthorizationRules/{authorizationRuleName}/listKeys |  |


<a id="notificationHubsCheckAvailability"></a>
# **notificationHubsCheckAvailability**
> CheckAvailabilityResource notificationHubsCheckAvailability(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters)



Checks the availability of the given notificationHub in a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckAvailabilityParameters parameters = new CheckAvailabilityParameters(); // CheckAvailabilityParameters | The notificationHub name.
    try {
      CheckAvailabilityResource result = apiInstance.notificationHubsCheckAvailability(resourceGroupName, namespaceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsCheckAvailability");
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
| **namespaceName** | **String**| The namespace name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**CheckAvailabilityParameters**](CheckAvailabilityParameters.md)| The notificationHub name. | |

### Return type

[**CheckAvailabilityResource**](CheckAvailabilityResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="notificationHubsCreateOrUpdate"></a>
# **notificationHubsCreateOrUpdate**
> NotificationHubResource notificationHubsCreateOrUpdate(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, parameters)



Creates/Update a NotificationHub in a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    NotificationHubCreateOrUpdateParameters parameters = new NotificationHubCreateOrUpdateParameters(); // NotificationHubCreateOrUpdateParameters | Parameters supplied to the create/update a NotificationHub Resource.
    try {
      NotificationHubResource result = apiInstance.notificationHubsCreateOrUpdate(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsCreateOrUpdate");
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
| **namespaceName** | **String**| The namespace name. | |
| **notificationHubName** | **String**| The notification hub name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**NotificationHubCreateOrUpdateParameters**](NotificationHubCreateOrUpdateParameters.md)| Parameters supplied to the create/update a NotificationHub Resource. | |

### Return type

[**NotificationHubResource**](NotificationHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **201** |  |  -  |

<a id="notificationHubsCreateOrUpdateAuthorizationRule"></a>
# **notificationHubsCreateOrUpdateAuthorizationRule**
> SharedAccessAuthorizationRuleResource notificationHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates/Updates an authorization rule for a NotificationHub

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | Authorization Rule Name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SharedAccessAuthorizationRuleCreateOrUpdateParameters parameters = new SharedAccessAuthorizationRuleCreateOrUpdateParameters(); // SharedAccessAuthorizationRuleCreateOrUpdateParameters | The shared access authorization rule.
    try {
      SharedAccessAuthorizationRuleResource result = apiInstance.notificationHubsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsCreateOrUpdateAuthorizationRule");
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
| **namespaceName** | **String**| The namespace name. | |
| **notificationHubName** | **String**| The notification hub name. | |
| **authorizationRuleName** | **String**| Authorization Rule Name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SharedAccessAuthorizationRuleCreateOrUpdateParameters**](SharedAccessAuthorizationRuleCreateOrUpdateParameters.md)| The shared access authorization rule. | |

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="notificationHubsDelete"></a>
# **notificationHubsDelete**
> notificationHubsDelete(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Deletes a notification hub associated with a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.notificationHubsDelete(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsDelete");
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
| **namespaceName** | **String**| The namespace name. | |
| **notificationHubName** | **String**| The notification hub name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** |  |  -  |

<a id="notificationHubsDeleteAuthorizationRule"></a>
# **notificationHubsDeleteAuthorizationRule**
> notificationHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a notificationHub authorization rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | Authorization Rule Name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.notificationHubsDeleteAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsDeleteAuthorizationRule");
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
| **namespaceName** | **String**| The namespace name. | |
| **notificationHubName** | **String**| The notification hub name. | |
| **authorizationRuleName** | **String**| Authorization Rule Name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** |  |  -  |
| **204** |  |  -  |

<a id="notificationHubsGet"></a>
# **notificationHubsGet**
> NotificationHubResource notificationHubsGet(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Lists the notification hubs associated with a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NotificationHubResource result = apiInstance.notificationHubsGet(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsGet");
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
| **namespaceName** | **String**| The namespace name. | |
| **notificationHubName** | **String**| The notification hub name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NotificationHubResource**](NotificationHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="notificationHubsGetAuthorizationRule"></a>
# **notificationHubsGetAuthorizationRule**
> SharedAccessAuthorizationRuleResource notificationHubsGetAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets an authorization rule for a NotificationHub by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | authorization rule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleResource result = apiInstance.notificationHubsGetAuthorizationRule(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsGetAuthorizationRule");
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
| **namespaceName** | **String**| The namespace name | |
| **notificationHubName** | **String**| The notification hub name. | |
| **authorizationRuleName** | **String**| authorization rule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleResource**](SharedAccessAuthorizationRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="notificationHubsGetPnsCredentials"></a>
# **notificationHubsGetPnsCredentials**
> NotificationHubResource notificationHubsGetPnsCredentials(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Lists the PNS Credentials associated with a notification hub .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NotificationHubResource result = apiInstance.notificationHubsGetPnsCredentials(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsGetPnsCredentials");
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
| **namespaceName** | **String**| The namespace name. | |
| **notificationHubName** | **String**| The notification hub name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NotificationHubResource**](NotificationHubResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="notificationHubsList"></a>
# **notificationHubsList**
> NotificationHubListResult notificationHubsList(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Lists the notification hubs associated with a namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      NotificationHubListResult result = apiInstance.notificationHubsList(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsList");
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
| **namespaceName** | **String**| The namespace name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**NotificationHubListResult**](NotificationHubListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="notificationHubsListAuthorizationRules"></a>
# **notificationHubsListAuthorizationRules**
> SharedAccessAuthorizationRuleListResult notificationHubsListAuthorizationRules(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId)



Gets the authorization rules for a NotificationHub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedAccessAuthorizationRuleListResult result = apiInstance.notificationHubsListAuthorizationRules(resourceGroupName, namespaceName, notificationHubName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsListAuthorizationRules");
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
| **namespaceName** | **String**| The namespace name | |
| **notificationHubName** | **String**| The notification hub name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedAccessAuthorizationRuleListResult**](SharedAccessAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="notificationHubsListKeys"></a>
# **notificationHubsListKeys**
> ResourceListKeys notificationHubsListKeys(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId)



Gets the Primary and Secondary ConnectionStrings to the NotificationHub 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationHubsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationHubsApi apiInstance = new NotificationHubsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String namespaceName = "namespaceName_example"; // String | The namespace name.
    String notificationHubName = "notificationHubName_example"; // String | The notification hub name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The connection string of the NotificationHub for the specified authorizationRule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ResourceListKeys result = apiInstance.notificationHubsListKeys(resourceGroupName, namespaceName, notificationHubName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationHubsApi#notificationHubsListKeys");
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
| **namespaceName** | **String**| The namespace name. | |
| **notificationHubName** | **String**| The notification hub name. | |
| **authorizationRuleName** | **String**| The connection string of the NotificationHub for the specified authorizationRule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ResourceListKeys**](ResourceListKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |


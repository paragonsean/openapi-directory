# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionGroupsCreateOrUpdate**](DefaultApi.md#actionGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} |  |
| [**actionGroupsDelete**](DefaultApi.md#actionGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} |  |
| [**actionGroupsEnableReceiver**](DefaultApi.md#actionGroupsEnableReceiver) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName}/subscribe |  |
| [**actionGroupsGet**](DefaultApi.md#actionGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} |  |
| [**actionGroupsListByResourceGroup**](DefaultApi.md#actionGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups |  |
| [**actionGroupsListBySubscriptionId**](DefaultApi.md#actionGroupsListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/actionGroups |  |
| [**actionGroupsUpdate**](DefaultApi.md#actionGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} |  |


<a id="actionGroupsCreateOrUpdate"></a>
# **actionGroupsCreateOrUpdate**
> ActionGroupResource actionGroupsCreateOrUpdate(resourceGroupName, actionGroupName, subscriptionId, apiVersion, actionGroup)



Create a new action group or update an existing one.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String actionGroupName = "actionGroupName_example"; // String | The name of the action group.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ActionGroupResource actionGroup = new ActionGroupResource(); // ActionGroupResource | The action group to create or use for the update.
    try {
      ActionGroupResource result = apiInstance.actionGroupsCreateOrUpdate(resourceGroupName, actionGroupName, subscriptionId, apiVersion, actionGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionGroupsCreateOrUpdate");
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
| **actionGroupName** | **String**| The name of the action group. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **actionGroup** | [**ActionGroupResource**](ActionGroupResource.md)| The action group to create or use for the update. | |

### Return type

[**ActionGroupResource**](ActionGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An existing action group was successfully updated. |  -  |
| **201** | A new action group was successfully created. |  -  |
| **0** | An error occurred and the action group could not be created or updated. |  -  |

<a id="actionGroupsDelete"></a>
# **actionGroupsDelete**
> actionGroupsDelete(resourceGroupName, actionGroupName, subscriptionId, apiVersion)



Delete an action group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String actionGroupName = "actionGroupName_example"; // String | The name of the action group.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.actionGroupsDelete(resourceGroupName, actionGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionGroupsDelete");
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
| **actionGroupName** | **String**| The name of the action group. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |

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
| **200** | The action group was successfully deleted. |  -  |
| **204** | The action group does not exist. It may have already been deleted. |  -  |
| **0** | An error occurred and the action group could not be deleted. |  -  |

<a id="actionGroupsEnableReceiver"></a>
# **actionGroupsEnableReceiver**
> actionGroupsEnableReceiver(resourceGroupName, actionGroupName, subscriptionId, apiVersion, enableRequest)



Enable a receiver in an action group. This changes the receiver&#39;s status from Disabled to Enabled.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String actionGroupName = "actionGroupName_example"; // String | The name of the action group.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    EnableRequest enableRequest = new EnableRequest(); // EnableRequest | The receiver to re-enable.
    try {
      apiInstance.actionGroupsEnableReceiver(resourceGroupName, actionGroupName, subscriptionId, apiVersion, enableRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionGroupsEnableReceiver");
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
| **actionGroupName** | **String**| The name of the action group. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **enableRequest** | [**EnableRequest**](EnableRequest.md)| The receiver to re-enable. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The receiver was successfully enabled. |  -  |
| **409** | The receiver is already enabled in the action group. |  -  |
| **0** | An error occurred and the receiver could not be enabled, e.g.: 404: The action group was not found or no matching receiver was found in the action group. |  -  |

<a id="actionGroupsGet"></a>
# **actionGroupsGet**
> ActionGroupResource actionGroupsGet(resourceGroupName, actionGroupName, subscriptionId, apiVersion)



Get an action group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String actionGroupName = "actionGroupName_example"; // String | The name of the action group.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ActionGroupResource result = apiInstance.actionGroupsGet(resourceGroupName, actionGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionGroupsGet");
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
| **actionGroupName** | **String**| The name of the action group. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ActionGroupResource**](ActionGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the action group could not be retrieved. 404: The action group does not exist. |  -  |

<a id="actionGroupsListByResourceGroup"></a>
# **actionGroupsListByResourceGroup**
> ActionGroupList actionGroupsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Get a list of all action groups in a resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ActionGroupList result = apiInstance.actionGroupsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionGroupsListByResourceGroup");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ActionGroupList**](ActionGroupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the list of action groups could not be retrieved. |  -  |

<a id="actionGroupsListBySubscriptionId"></a>
# **actionGroupsListBySubscriptionId**
> ActionGroupList actionGroupsListBySubscriptionId(subscriptionId, apiVersion)



Get a list of all action groups in a subscription.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ActionGroupList result = apiInstance.actionGroupsListBySubscriptionId(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionGroupsListBySubscriptionId");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ActionGroupList**](ActionGroupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the list of action groups could not be retrieved. |  -  |

<a id="actionGroupsUpdate"></a>
# **actionGroupsUpdate**
> ActionGroupResource actionGroupsUpdate(subscriptionId, resourceGroupName, actionGroupName, apiVersion, actionGroupPatch)



Updates an existing action group&#39;s tags. To update other fields use the CreateOrUpdate method.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String actionGroupName = "actionGroupName_example"; // String | The name of the action group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ActionGroupPatchBody actionGroupPatch = new ActionGroupPatchBody(); // ActionGroupPatchBody | Parameters supplied to the operation.
    try {
      ActionGroupResource result = apiInstance.actionGroupsUpdate(subscriptionId, resourceGroupName, actionGroupName, apiVersion, actionGroupPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionGroupsUpdate");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **actionGroupName** | **String**| The name of the action group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **actionGroupPatch** | [**ActionGroupPatchBody**](ActionGroupPatchBody.md)| Parameters supplied to the operation. | |

### Return type

[**ActionGroupResource**](ActionGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An existing action group was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


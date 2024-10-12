# ApplianceDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applianceDefinitionsCreateOrUpdate**](ApplianceDefinitionsApi.md#applianceDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions/{applianceDefinitionName} |  |
| [**applianceDefinitionsCreateOrUpdateById**](ApplianceDefinitionsApi.md#applianceDefinitionsCreateOrUpdateById) | **PUT** /{applianceDefinitionId} |  |
| [**applianceDefinitionsDelete**](ApplianceDefinitionsApi.md#applianceDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions/{applianceDefinitionName} |  |
| [**applianceDefinitionsDeleteById**](ApplianceDefinitionsApi.md#applianceDefinitionsDeleteById) | **DELETE** /{applianceDefinitionId} |  |
| [**applianceDefinitionsGet**](ApplianceDefinitionsApi.md#applianceDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions/{applianceDefinitionName} |  |
| [**applianceDefinitionsGetById**](ApplianceDefinitionsApi.md#applianceDefinitionsGetById) | **GET** /{applianceDefinitionId} |  |
| [**applianceDefinitionsListByResourceGroup**](ApplianceDefinitionsApi.md#applianceDefinitionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applianceDefinitions |  |


<a id="applianceDefinitionsCreateOrUpdate"></a>
# **applianceDefinitionsCreateOrUpdate**
> ApplianceDefinition applianceDefinitionsCreateOrUpdate(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId, parameters)



Creates a new appliance definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplianceDefinitionsApi apiInstance = new ApplianceDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String applianceDefinitionName = "applianceDefinitionName_example"; // String | The name of the appliance definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ApplianceDefinition parameters = new ApplianceDefinition(); // ApplianceDefinition | Parameters supplied to the create or update an appliance definition.
    try {
      ApplianceDefinition result = apiInstance.applianceDefinitionsCreateOrUpdate(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceDefinitionsApi#applianceDefinitionsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **applianceDefinitionName** | **String**| The name of the appliance definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ApplianceDefinition**](ApplianceDefinition.md)| Parameters supplied to the create or update an appliance definition. | |

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the appliance definition, including provisioning status. |  -  |
| **201** | Created - Returns information about the appliance definition, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applianceDefinitionsCreateOrUpdateById"></a>
# **applianceDefinitionsCreateOrUpdateById**
> ApplianceDefinition applianceDefinitionsCreateOrUpdateById(applianceDefinitionId, apiVersion, parameters)



Creates a new appliance definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplianceDefinitionsApi apiInstance = new ApplianceDefinitionsApi(defaultClient);
    String applianceDefinitionId = "applianceDefinitionId_example"; // String | The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    ApplianceDefinition parameters = new ApplianceDefinition(); // ApplianceDefinition | Parameters supplied to the create or update an appliance definition.
    try {
      ApplianceDefinition result = apiInstance.applianceDefinitionsCreateOrUpdateById(applianceDefinitionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceDefinitionsApi#applianceDefinitionsCreateOrUpdateById");
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
| **applianceDefinitionId** | **String**| The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name} | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **parameters** | [**ApplianceDefinition**](ApplianceDefinition.md)| Parameters supplied to the create or update an appliance definition. | |

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the appliance definition, including provisioning status. |  -  |
| **201** | Created - Returns information about the appliance definition, including provisioning status. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applianceDefinitionsDelete"></a>
# **applianceDefinitionsDelete**
> applianceDefinitionsDelete(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId)



Deletes the appliance definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplianceDefinitionsApi apiInstance = new ApplianceDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String applianceDefinitionName = "applianceDefinitionName_example"; // String | The name of the appliance definition to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.applianceDefinitionsDelete(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceDefinitionsApi#applianceDefinitionsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **applianceDefinitionName** | **String**| The name of the appliance definition to delete. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applianceDefinitionsDeleteById"></a>
# **applianceDefinitionsDeleteById**
> applianceDefinitionsDeleteById(applianceDefinitionId, apiVersion)



Deletes the appliance definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplianceDefinitionsApi apiInstance = new ApplianceDefinitionsApi(defaultClient);
    String applianceDefinitionId = "applianceDefinitionId_example"; // String | The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.applianceDefinitionsDeleteById(applianceDefinitionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceDefinitionsApi#applianceDefinitionsDeleteById");
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
| **applianceDefinitionId** | **String**| The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name} | |
| **apiVersion** | **String**| The API version to use for this operation. | |

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
| **202** | Accepted - Returns this status until the asynchronous operation has completed. |  -  |
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applianceDefinitionsGet"></a>
# **applianceDefinitionsGet**
> ApplianceDefinition applianceDefinitionsGet(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId)



Gets the appliance definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplianceDefinitionsApi apiInstance = new ApplianceDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String applianceDefinitionName = "applianceDefinitionName_example"; // String | The name of the appliance definition.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      ApplianceDefinition result = apiInstance.applianceDefinitionsGet(resourceGroupName, applianceDefinitionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceDefinitionsApi#applianceDefinitionsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **applianceDefinitionName** | **String**| The name of the appliance definition. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the appliance definition. |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applianceDefinitionsGetById"></a>
# **applianceDefinitionsGetById**
> ApplianceDefinition applianceDefinitionsGetById(applianceDefinitionId, apiVersion)



Gets the appliance definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplianceDefinitionsApi apiInstance = new ApplianceDefinitionsApi(defaultClient);
    String applianceDefinitionId = "applianceDefinitionId_example"; // String | The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      ApplianceDefinition result = apiInstance.applianceDefinitionsGetById(applianceDefinitionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceDefinitionsApi#applianceDefinitionsGetById");
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
| **applianceDefinitionId** | **String**| The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name} | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**ApplianceDefinition**](ApplianceDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the appliance definition. |  -  |
| **404** | Not Found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applianceDefinitionsListByResourceGroup"></a>
# **applianceDefinitionsListByResourceGroup**
> ApplianceDefinitionListResult applianceDefinitionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists the appliance definitions in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplianceDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplianceDefinitionsApi apiInstance = new ApplianceDefinitionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      ApplianceDefinitionListResult result = apiInstance.applianceDefinitionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplianceDefinitionsApi#applianceDefinitionsListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**ApplianceDefinitionListResult**](ApplianceDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of appliance definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


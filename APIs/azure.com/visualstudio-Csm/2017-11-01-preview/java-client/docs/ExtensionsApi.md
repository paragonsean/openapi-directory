# ExtensionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extensionsCreate**](ExtensionsApi.md#extensionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Create |
| [**extensionsDelete**](ExtensionsApi.md#extensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Delete |
| [**extensionsGet**](ExtensionsApi.md#extensionsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Get |
| [**extensionsListByAccount**](ExtensionsApi.md#extensionsListByAccount) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension | Extensions_ListByAccount |
| [**extensionsUpdate**](ExtensionsApi.md#extensionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Update |


<a id="extensionsCreate"></a>
# **extensionsCreate**
> ExtensionResource extensionsCreate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body)

Extensions_Create

Registers the extension with a Visual Studio Team Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
    String extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
    ExtensionResourceRequest body = new ExtensionResourceRequest(); // ExtensionResourceRequest | An object containing additional information related to the extension request.
    try {
      ExtensionResource result = apiInstance.extensionsCreate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#extensionsCreate");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | |
| **extensionResourceName** | **String**| The name of the extension. | |
| **body** | [**ExtensionResourceRequest**](ExtensionResourceRequest.md)| An object containing additional information related to the extension request. | |

### Return type

[**ExtensionResource**](ExtensionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The extension resource was created for the specified account. |  -  |

<a id="extensionsDelete"></a>
# **extensionsDelete**
> extensionsDelete(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName)

Extensions_Delete

Removes an extension resource registration for a Visual Studio Team Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
    String extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
    try {
      apiInstance.extensionsDelete(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#extensionsDelete");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | |
| **extensionResourceName** | **String**| The name of the extension. | |

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
| **200** | The operation succeeded. The extension resource has been deleted for the specified account. |  -  |

<a id="extensionsGet"></a>
# **extensionsGet**
> ExtensionResource extensionsGet(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName)

Extensions_Get

Gets the details of an extension associated with a Visual Studio Team Services account resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
    String extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
    try {
      ExtensionResource result = apiInstance.extensionsGet(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#extensionsGet");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | |
| **extensionResourceName** | **String**| The name of the extension. | |

### Return type

[**ExtensionResource**](ExtensionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the extension resource details for the specified account. |  -  |
| **404** | The specified extension has no plans defined. |  -  |

<a id="extensionsListByAccount"></a>
# **extensionsListByAccount**
> ExtensionResourceListResult extensionsListByAccount(resourceGroupName, subscriptionId, apiVersion, accountResourceName)

Extensions_ListByAccount

Gets the details of the extension resources created within the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
    try {
      ExtensionResourceListResult result = apiInstance.extensionsListByAccount(resourceGroupName, subscriptionId, apiVersion, accountResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#extensionsListByAccount");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | |

### Return type

[**ExtensionResourceListResult**](ExtensionResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains all extension resource details for the specified account. |  -  |

<a id="extensionsUpdate"></a>
# **extensionsUpdate**
> ExtensionResource extensionsUpdate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body)

Extensions_Update

Updates an existing extension registration for the Visual Studio Team Services account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtensionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExtensionsApi apiInstance = new ExtensionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
    String extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
    ExtensionResourceRequest body = new ExtensionResourceRequest(); // ExtensionResourceRequest | An object containing additional information related to the extension request.
    try {
      ExtensionResource result = apiInstance.extensionsUpdate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtensionsApi#extensionsUpdate");
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | |
| **extensionResourceName** | **String**| The name of the extension. | |
| **body** | [**ExtensionResourceRequest**](ExtensionResourceRequest.md)| An object containing additional information related to the extension request. | |

### Return type

[**ExtensionResource**](ExtensionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The extension resource was updated for the specified account. |  -  |


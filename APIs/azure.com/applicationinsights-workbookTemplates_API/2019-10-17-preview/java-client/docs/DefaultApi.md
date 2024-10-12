# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workbookTemplatesCreateOrUpdate**](DefaultApi.md#workbookTemplatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} |  |
| [**workbookTemplatesDelete**](DefaultApi.md#workbookTemplatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} |  |
| [**workbookTemplatesGet**](DefaultApi.md#workbookTemplatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} |  |
| [**workbookTemplatesListByResourceGroup**](DefaultApi.md#workbookTemplatesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates |  |
| [**workbookTemplatesUpdate**](DefaultApi.md#workbookTemplatesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooktemplates/{resourceName} |  |


<a id="workbookTemplatesCreateOrUpdate"></a>
# **workbookTemplatesCreateOrUpdate**
> WorkbookTemplate workbookTemplatesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookTemplateProperties)



Create a new workbook template.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    WorkbookTemplate workbookTemplateProperties = new WorkbookTemplate(); // WorkbookTemplate | Properties that need to be specified to create a new workbook.
    try {
      WorkbookTemplate result = apiInstance.workbookTemplatesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookTemplateProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbookTemplatesCreateOrUpdate");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **workbookTemplateProperties** | [**WorkbookTemplate**](WorkbookTemplate.md)| Properties that need to be specified to create a new workbook. | |

### Return type

[**WorkbookTemplate**](WorkbookTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly created workbook template. |  -  |
| **201** | The newly created workbook template. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbookTemplatesDelete"></a>
# **workbookTemplatesDelete**
> workbookTemplatesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion)



Delete a workbook template.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.workbookTemplatesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbookTemplatesDelete");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
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
| **200** | The workbook template has been successfully deleted. |  -  |
| **204** | The resource doesn&#39;t exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbookTemplatesGet"></a>
# **workbookTemplatesGet**
> WorkbookTemplate workbookTemplatesGet(subscriptionId, resourceGroupName, resourceName, apiVersion)



Get a single workbook template by its resourceName.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      WorkbookTemplate result = apiInstance.workbookTemplatesGet(subscriptionId, resourceGroupName, resourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbookTemplatesGet");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**WorkbookTemplate**](WorkbookTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A workbook template definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbookTemplatesListByResourceGroup"></a>
# **workbookTemplatesListByResourceGroup**
> WorkbookTemplatesListResult workbookTemplatesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get all Workbook templates defined within a specified resource group.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      WorkbookTemplatesListResult result = apiInstance.workbookTemplatesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbookTemplatesListByResourceGroup");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

[**WorkbookTemplatesListResult**](WorkbookTemplatesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more workbook template definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbookTemplatesUpdate"></a>
# **workbookTemplatesUpdate**
> WorkbookTemplate workbookTemplatesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookTemplateUpdateParameters)



Updates a workbook template that has already been added.

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
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    WorkbookTemplateUpdateParameters workbookTemplateUpdateParameters = new WorkbookTemplateUpdateParameters(); // WorkbookTemplateUpdateParameters | Properties that need to be specified to patch a workbook template.
    try {
      WorkbookTemplate result = apiInstance.workbookTemplatesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookTemplateUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbookTemplatesUpdate");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **workbookTemplateUpdateParameters** | [**WorkbookTemplateUpdateParameters**](WorkbookTemplateUpdateParameters.md)| Properties that need to be specified to patch a workbook template. | [optional] |

### Return type

[**WorkbookTemplate**](WorkbookTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workbook template definition updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


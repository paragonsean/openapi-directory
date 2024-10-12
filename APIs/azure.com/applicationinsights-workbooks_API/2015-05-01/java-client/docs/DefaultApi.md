# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workbooksCreateOrUpdate**](DefaultApi.md#workbooksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} |  |
| [**workbooksDelete**](DefaultApi.md#workbooksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} |  |
| [**workbooksGet**](DefaultApi.md#workbooksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} |  |
| [**workbooksListByResourceGroup**](DefaultApi.md#workbooksListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks |  |
| [**workbooksUpdate**](DefaultApi.md#workbooksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroup/{resourceGroupName}/providers/microsoft.insights/workbooks/{resourceName} |  |


<a id="workbooksCreateOrUpdate"></a>
# **workbooksCreateOrUpdate**
> Workbook workbooksCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties)



Create a new workbook.

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
    Workbook workbookProperties = new Workbook(); // Workbook | Properties that need to be specified to create a new workbook.
    try {
      Workbook result = apiInstance.workbooksCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbooksCreateOrUpdate");
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
| **workbookProperties** | [**Workbook**](Workbook.md)| Properties that need to be specified to create a new workbook. | |

### Return type

[**Workbook**](Workbook.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly created workbook. |  -  |
| **201** | The newly created workbook. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbooksDelete"></a>
# **workbooksDelete**
> workbooksDelete(subscriptionId, resourceGroupName, resourceName, apiVersion)



Delete a workbook.

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
      apiInstance.workbooksDelete(subscriptionId, resourceGroupName, resourceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbooksDelete");
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
| **201** | The workbook has been successfully deleted. |  -  |
| **204** | The resource doesn&#39;t exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbooksGet"></a>
# **workbooksGet**
> Workbook workbooksGet(subscriptionId, resourceGroupName, resourceName, apiVersion)



Get a single workbook by its resourceName.

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
      Workbook result = apiInstance.workbooksGet(subscriptionId, resourceGroupName, resourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbooksGet");
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

[**Workbook**](Workbook.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A workbook definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbooksListByResourceGroup"></a>
# **workbooksListByResourceGroup**
> WorkbooksListResult workbooksListByResourceGroup(subscriptionId, resourceGroupName, category, apiVersion, tags, canFetchContent)



Get all Workbooks defined within a specified resource group and category.

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
    String category = "workbook"; // String | Category of workbook to return.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    List<String> tags = Arrays.asList(); // List<String> | Tags presents on each workbook returned.
    Boolean canFetchContent = true; // Boolean | Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks.
    try {
      WorkbooksListResult result = apiInstance.workbooksListByResourceGroup(subscriptionId, resourceGroupName, category, apiVersion, tags, canFetchContent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbooksListByResourceGroup");
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
| **category** | **String**| Category of workbook to return. | [enum: workbook, TSG, performance, retention] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **tags** | [**List&lt;String&gt;**](String.md)| Tags presents on each workbook returned. | [optional] |
| **canFetchContent** | **Boolean**| Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks. | [optional] |

### Return type

[**WorkbooksListResult**](WorkbooksListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list containing 0 or more workbook definitions. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workbooksUpdate"></a>
# **workbooksUpdate**
> Workbook workbooksUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties)



Updates a workbook that has already been added.

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
    Workbook workbookProperties = new Workbook(); // Workbook | Properties that need to be specified to create a new workbook.
    try {
      Workbook result = apiInstance.workbooksUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, workbookProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#workbooksUpdate");
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
| **workbookProperties** | [**Workbook**](Workbook.md)| Properties that need to be specified to create a new workbook. | |

### Return type

[**Workbook**](Workbook.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The workbook definition updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |


# ApplicationPackageApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationPackageActivate**](ApplicationPackageApi.md#applicationPackageActivate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId}/versions/{version}/activate |  |
| [**applicationPackageCreate**](ApplicationPackageApi.md#applicationPackageCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId}/versions/{version} |  |
| [**applicationPackageDelete**](ApplicationPackageApi.md#applicationPackageDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId}/versions/{version} |  |
| [**applicationPackageGet**](ApplicationPackageApi.md#applicationPackageGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/applications/{applicationId}/versions/{version} |  |


<a id="applicationPackageActivate"></a>
# **applicationPackageActivate**
> applicationPackageActivate(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId, parameters)



Activates the specified application package.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationPackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationPackageApi apiInstance = new ApplicationPackageApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String version = "version_example"; // String | The version of the application to activate.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    ActivateApplicationPackageParameters parameters = new ActivateApplicationPackageParameters(); // ActivateApplicationPackageParameters | The parameters for the request.
    try {
      apiInstance.applicationPackageActivate(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationPackageApi#applicationPackageActivate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **applicationId** | **String**| The ID of the application. | |
| **version** | **String**| The version of the application to activate. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**ActivateApplicationPackageParameters**](ActivateApplicationPackageParameters.md)| The parameters for the request. | |

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
| **204** | The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationPackageCreate"></a>
# **applicationPackageCreate**
> ApplicationPackage applicationPackageCreate(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId)



Creates an application package record.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationPackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationPackageApi apiInstance = new ApplicationPackageApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String version = "version_example"; // String | The version of the application.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      ApplicationPackage result = apiInstance.applicationPackageCreate(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationPackageApi#applicationPackageCreate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **applicationId** | **String**| The ID of the application. | |
| **version** | **String**| The version of the application. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**ApplicationPackage**](ApplicationPackage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The operation was successful. The response contains the application package entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationPackageDelete"></a>
# **applicationPackageDelete**
> applicationPackageDelete(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId)



Deletes an application package record and its associated binary file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationPackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationPackageApi apiInstance = new ApplicationPackageApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String version = "version_example"; // String | The version of the application to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      apiInstance.applicationPackageDelete(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationPackageApi#applicationPackageDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **applicationId** | **String**| The ID of the application. | |
| **version** | **String**| The version of the application to delete. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

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
| **204** | The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationPackageGet"></a>
# **applicationPackageGet**
> ApplicationPackage applicationPackageGet(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId)



Gets information about the specified application package.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationPackageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationPackageApi apiInstance = new ApplicationPackageApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String version = "version_example"; // String | The version of the application.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      ApplicationPackage result = apiInstance.applicationPackageGet(resourceGroupName, accountName, applicationId, version, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationPackageApi#applicationPackageGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **applicationId** | **String**| The ID of the application. | |
| **version** | **String**| The version of the application. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**ApplicationPackage**](ApplicationPackage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the application package entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

